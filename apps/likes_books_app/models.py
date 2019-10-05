from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "User object: {} {} {} ".format(self.first_name,self.last_name,self.email)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_books", on_delete=models.CASCADE)
    def __repr__(self):
        return "Book object: {} {} {} ".format(self.name,self.desc, self.uploader)

class Like(models.Model):
    users = models.ForeignKey(User, related_name="liked_users", on_delete=models.CASCADE)
    books = models.ForeignKey(Book, related_name="liked_books", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "Like object: {} {}".format(self.users, self.books)
 