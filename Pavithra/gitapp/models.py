from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
   Book_name=models.CharField(max_length=25);
   Book_serial_number=models.IntegerField(primary_key=True);
   Author_name=models.CharField(max_length=50);
   Number_of_pages=models.IntegerField();
   Genre=models.CharField(max_length=40);
   Year_of_book_published=models.IntegerField();
   No_of_chapters=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
   list_display=("Book_name","Book_serial_number","Author_name","Number_of_pages","Genre","Year_of_book_published","No_of_chapters");


