from django.test import Client
from django.test import TestCase
from posts.models.post import Post


class PostModelTest(TestCase):

    def test_post_has_all_fields(self):
        post = Post()
        fields = ["author", "title", "date", "body", "id"]
        for field in fields:
            self.assertTrue(hasattr(post, field))

    def test_save(self):
        post = Post.objects.create(author="Me", title="How to test django",
                                   body="Some body", date="2014-11-24")
        self.assertEqual(post.author, "Me")
        self.assertEqual(post.body, "Some body")

    def test_returns_created_1_day_ago_if_created_yeterday(self):
        post = Post.objects.create(author="Me", title="How to test django",
                                   body="Some body", date="2014-10-29")
        self.assertEqual(post.created_at(), 'created 1 day ago')

    def test_returns_created_2_days_ago_if_created_yeterday(self):
        post = Post.objects.create(author="Me", title="How to test django",
                                   body="Some body", date="2014-10-28")
        self.assertEqual(post.created_at(), 'created 2 days ago')