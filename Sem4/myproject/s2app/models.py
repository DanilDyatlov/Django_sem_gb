from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=80)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return (f"Author("
                f"firstname='{self.firstname}, '"
                f"lastname='{self.lastname}, '"
                f"email='{self.email}, '"
                f"biography='{self.biography}, '"
                f"birthday='{self.birthday})'"
                )


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_stamp = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __repr__(self):
        return (f"Article("
                f"title='{self.title}, '"
                f"content='{self.content}, '"
                f"time_stamp='{self.time_stamp}, '"
                f"author='{self.author}, '"
                f"category='{self.category}, '"
                f"views='{self.views}, '"
                f"is_published='{self.is_published}, '"
                )


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp_create = models.DateTimeField()
    time_stamp_modify = models.DateTimeField()

    def __repr__(self):
        return (f"Comment("
                f"author=f'{self.author}'"
                f"article=f'{self.article}'"
                f"content=f'{self.content}'"
                f"time_stamp_create=f'{self.time_stamp_create}'"
                f"time_stamp_modify=f'{self.time_stamp_modify}'"
                )