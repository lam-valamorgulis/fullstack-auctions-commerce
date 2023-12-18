from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class User(AbstractUser):
  def __str__(self):
    return f"{self.id} | {self.username} | {self.email}"


class AuctionsListings(models.Model):
  titleList = models.CharField(max_length = 150,blank=False, default="")
  description = models.CharField(max_length = 150,blank=False, default="")
  url = models.CharField(max_length = 300,blank=True, default= "")
  price = models.FloatField(blank=False, default= 0)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  active = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.creator.id} | {self.titleList} | {self.description} | {self.price} | {self.url} | {self.active}"

class Cart(models.Model):
  cart_user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
  cart_listing = models.ForeignKey(AuctionsListings,on_delete=models.CASCADE,default="")
  add_watch_list = models.BooleanField(default=False)
  def __str__(self):
    return f"{self.cart_user.id} | {self.cart_listing.id} | {self.add_watch_list}"
  

class Bids(models.Model):
  bid_user_pk = models.ForeignKey(User,on_delete=models.CASCADE,default="")
  bid_item_pk = models.ForeignKey(AuctionsListings,on_delete=models.CASCADE,default="")
  bidPrice = models.FloatField(blank=False, default=0)
  is_winning_bid = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.bidPrice} | {self.bid_user_pk.id} | {self.bid_item_pk.id} | {self.is_winning_bid}"

class Comment(models.Model):
  comment_user = models.ForeignKey(User,on_delete=models.CASCADE,default="")
  comment_item = models.ForeignKey(AuctionsListings,on_delete=models.CASCADE,default="")
  comment = models.CharField(max_length = 300,blank=False, default="")
  date_time = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
    return f"{self.date_time} | {self.comment}"

class Categories(models.Model):
  CATEGORY = [
    ("Miscellaneous", "Miscellaneous"),
    ("Movies and Television", "Movies and Television"),
    ("Sports", "Sports"),
    ("Arts and Crafts", "Arts and Crafts"),
    ("Clothing", "Clothing"),
    ("Books", "Books"),
  ]
  category_item = models.ForeignKey(AuctionsListings,on_delete=models.CASCADE,default="")
  category = models.CharField(max_length=64, choices=CATEGORY, default=None)

  def __str__(self):
    return f"{self.category} | {self.category_item}"


