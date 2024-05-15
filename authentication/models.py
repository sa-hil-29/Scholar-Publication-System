from django.db import models

class Faculty(models.Model):
    email = models.EmailField(primary_key=True, max_length=25)
    name = models.CharField(max_length=25)
    EmployeeId = models.TextField(max_length=10, unique=True)
    
class Journal(models.Model):
    JournalId = models.TextField(primary_key=True)
    email = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    journalName = models.CharField(max_length=100)
    publicationDate = models.TimeField()
    
    def __str__(self,):
        return f"Journal {self.journalIid} - Publication Date: {self.publicationDate} - Email: {self.email}"

class BookChapter(models.Model):
    chapterId = models.TextField(primary_key=True, max_length=10)
    email = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    chapterName = models.CharField(max_length=100)
    publicationDate = models.TimeField()
    
    def __str__(self,):
        return f"BookChapter {self.chapterId} - Publication Date: {self.publicationDate} - Email: {self.email}"


class Book(models.Model):
    bookId = models.TextField(primary_key=True, max_length=10)
    email = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    bookName = models.CharField(max_length=100)
    publicationDate = models.TimeField()
    
    def __str__(self,):
        return f"Book {self.bookId} - Publication Date: {self.publicationDate} - Email: {self.email}"
