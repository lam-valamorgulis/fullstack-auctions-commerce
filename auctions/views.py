from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
from django.db.models import Count, Max
from django.contrib.auth.decorators import login_required
from .models import AuctionsListings, User, Bids, Cart, Comment, Categories
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import localtime, activate,is_aware
import pytz
from tzlocal import get_localzone
local_tz = get_localzone()
timezone.activate(local_tz)



def index(request):
  if request.user.is_authenticated:
    user = request.user
    cart_count = Cart.objects.filter(cart_user = user,add_watch_list = True).count()
    return render(request, "auctions/index.html",{
      "all_Listings" : AuctionsListings.objects.all().filter(active = True),
      "watch_list_count": cart_count,
      })
  return render(request, "auctions/index.html",{
      "all_Listings" : AuctionsListings.objects.all().filter(active = True)
      })   


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='/login')
def create(request) :
  current_user = request.user
  all_category = Categories._meta.get_field("category").choices
  cart_count = Cart.objects.filter(cart_user = current_user,add_watch_list = True).count()
  
  if request.method == "POST":
    title =  request.POST["title"]
    description = request.POST["description"]
    url =  request.POST["url"]
    bid =  request.POST["bid"]
    newListing = AuctionsListings(titleList=title, description= description, url=url, price=bid)
    newListing.creator = request.user
    newListing.active = True
    newListing.save()

    category = Categories(category = request.POST["category"], category_item = newListing)
    category.save()
    
    return HttpResponseRedirect(reverse("index"))
    
  return render(request, "auctions/create.html", {
    "watch_list_count": cart_count,
    "all_category" : all_category
  })


def listing(request,id):
  # Current user, listing, all comment
  listing = AuctionsListings.objects.get(pk=id)
  current_user = request.user
  owner_bid = current_user.id == listing.creator.id
  all_comment = Comment.objects.filter(comment_item = listing)

  # ADD TO WATCH LIST
  if request.method == "POST" and "add_watch_list" in request.POST :
    # change cart record add watch list to True
    id_cart = float(request.POST["cart_id"])
    get_cart = Cart.objects.get(pk = id_cart)
    get_cart.add_watch_list = True
    get_cart.save()

    return render(request, "auctions/listing.html", {
      "listing":listing,
      "addToWatchList" : get_cart.add_watch_list,
      "cart_id" : get_cart.id,
      "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
      "is_owner_bid" : owner_bid,
      "all_comment" : all_comment
    })

  # REMOVE FROM WATCH LIST
  if request.method == "POST" and "remove_watch_list" in request.POST:
    id_cart = float(request.POST["cart_id"])
    get_cart = Cart.objects.get(pk = id_cart)
    get_cart.add_watch_list = False
    get_cart.save()

    return render(request, "auctions/listing.html", {
      "listing":listing,
      "addToWatchList" : get_cart.add_watch_list,
      "cart_id" : get_cart.id,
      "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
      "is_owner_bid" : owner_bid,
      "all_comment" : all_comment
    })

  # PLACE BID
  if request.method == "POST" and "place_bid" in request.POST:
    cart = Cart.objects.filter(cart_user = current_user, cart_listing = listing)
    owner_bid = current_user.id == listing.creator.id

    # get new bid form user
    new_bid = request.POST["place_bid"]
    # check bid less than starting point, send message
    if float(new_bid) <= listing.price :
      return render(request, "auctions/listing.html",{
        "listing":listing,
        "addToWatchList" : cart.values()[0]["add_watch_list"],
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "is_owner_bid" : owner_bid,
        "message": "Bid must higher than current bid",
        "all_comment" : all_comment
      })
      
    else: 
      new_bid_obj = Bids(bid_user_pk=current_user, bid_item_pk= listing, bidPrice = new_bid)
      new_bid_obj.save()
      listing.price = float(new_bid)
      listing.save()
        
      return render(request, "auctions/listing.html",{
      "listing":listing,
      "addToWatchList" : cart.values()[0]["add_watch_list"],
      "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
      "is_owner_bid" : owner_bid,
      "all_comment" : all_comment
      })
    
      
  # COMMENT
  if request.method == "POST"and "comment" in request.POST:
    owner_bid = current_user.id == listing.creator.id
    get_comment = request.POST["comment"]
    comment = Comment(comment_user = current_user, comment_item = listing, comment = get_comment, date_time = (timezone.now()))
    comment.save()
    # all_comment = Comment.objects.filter(comment_item = listing)
    time = timezone.now()
    
    return render(request, "auctions/listing.html",{
        "listing":listing,
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "is_owner_bid" : owner_bid,
        "all_comment" : all_comment
    })

  # VIEWING ITEM
    # User not authenticated
  if not request.user.is_authenticated:
    # all_comment = Comment.objects.filter(comment_item = listing)
    return render(request, "auctions/listing.html", {
      "listing":listing,
      "all_comment" : all_comment
    })
    # User authenticated
  else :
    cart = Cart.objects.filter(cart_user = current_user, cart_listing = listing)
    owner_bid = current_user.id == listing.creator.id
    all_comment = Comment.objects.filter(comment_item = listing)
    
    # if have cart record then rendering current cart state view listing
    if cart:
      return render(request, "auctions/listing.html",{
        "listing":listing,
        "addToWatchList" : cart.values()[0]["add_watch_list"],
        "cart_id" : cart.values()[0]["id"],
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "is_owner_bid" : owner_bid,
        "all_comment" : all_comment
      })
     # not have cart record and user is not owner list => creat new cart record (user, listing)
    elif not cart and not owner_bid:
      new_cart = Cart(cart_user = current_user, cart_listing = listing, add_watch_list = False)
      new_cart.save()

      # render add watch list button
      return render(request, "auctions/listing.html",{
        "listing":listing,
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "addToWatchList" : new_cart.add_watch_list,
        "cart_id" : new_cart.id,
        "is_owner_bid" : owner_bid,
        "all_comment" : all_comment
      })

      # if user is owner listing => dont have function add or remove watch list
    else :
      return render(request, "auctions/listing.html",{
        "listing":listing,
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "is_owner_bid" : owner_bid,
        "all_comment" : all_comment
      })
      
    
@login_required(login_url='/login')
def watch_list(request): 
  watch_list_count= Cart.objects.filter(add_watch_list=True).count()
  watch_list_items = []
  cart_items = Cart.objects.filter(cart_user = request.user,add_watch_list = True).values()
  for cart_item in cart_items :
    watch_list_items.append(AuctionsListings.objects.get(pk = float(cart_item["cart_listing_id"])))
  
  if request.method == "POST" and "remove_id" in request.POST:
    id_listing = float(request.POST["remove_id"])
    listing = AuctionsListings.objects.get(pk = id_listing)
    get_cart = Cart.objects.filter(cart_listing = listing)
    get_cart.update(add_watch_list = False)
    return HttpResponseRedirect(reverse("watch_list"))
    
  return render(request, "auctions/watchlist.html",{
    "watch_list_items": watch_list_items,
    "watch_list_count": watch_list_count,
  })

@login_required(login_url='/login')
def closebid(request,id):
  current_user = request.user
  winning_bid = (Bids.objects.filter(bid_item_pk= AuctionsListings.objects.get(pk=id))).order_by("-bidPrice")

  # close bid and make listing no longer active and set bid to winning bid
  if request.method == "POST" and not winning_bid:
    listing = AuctionsListings.objects.get(pk=id)
    owner_bid = current_user.id == listing.creator.id
    cart = Cart.objects.filter(cart_user = current_user, cart_listing = listing)
    return render(request, "auctions/listing.html",{
        "listing":listing,
        "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
        "is_owner_bid" : owner_bid,
        "message": "No one bids on this item",
        "all_comment" : Comment.objects.filter(comment_item = listing)
      })
  if request.method == "POST":
    winning_bid[0].is_winning_bid = True
    winning_bid[0].save()
    win_user = winning_bid[0].bid_user_pk
    win_price = winning_bid[0].bidPrice
    win_listing = winning_bid[0].bid_item_pk
    win_listing.active = False
    win_listing.save()
    
    return render(request, "auctions/winning.html",{
      "current_user" : current_user,
      "win_listing" : win_listing,
      "win_price" : win_price,
      "win_user" : win_user
  })
  # showing winner bid item if signed in close bid page
  if winning_bid and winning_bid.bid_item_pk.active == False:
    return render(request, "auctions/winning.html",{
      "winning_bid" : winning_bid,
      "current_user" : current_user,
      "win_listing" : winning_bid.bid_item_pk,
      "win_price" : winning_bid.bidPrice,
      "win_user" : winning_bid.bid_user_pk
    }) 
  else :
    return HttpResponseRedirect(reverse("index"))

@login_required(login_url='/login')
def winning_list(request):
  current_user = request.user
  all_winning_list = Bids.objects.filter(bid_user_pk=current_user, is_winning_bid = True)
 
  return render(request, "auctions/winning_list.html",{
    "all_winning_list" : all_winning_list
  })

@login_required(login_url='/login')
def categories(request):
  all_categories = Categories.objects.order_by().values('category').distinct()
  current_user = request.user
 
  return render(request, "auctions/categories.html",{
    "all_categories": all_categories,
    "watch_list_count": Cart.objects.filter(cart_user = current_user,add_watch_list = True).count(),
  })

@login_required(login_url='/login')
def detail_category(request,category):
  item_active = []
  message=""
  get_category = Categories.objects.filter(category=category)
  for item in get_category:
    if item.category_item.active:
      item_active.append(item)
      
  if len(item_active) == 0:
    message = "No current active listing"
    return render(request, "auctions/detail_category.html",{
    "message" : message
  })
  else :
    return render(request, "auctions/detail_category.html",{
      "get_category": item_active,
    })
      
    


  