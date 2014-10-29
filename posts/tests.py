from django.test import TestCase
from posts.models import Post


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
