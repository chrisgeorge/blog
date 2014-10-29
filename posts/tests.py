from django.test import TestCase
from posts.models import Post


class PostModelTest(TestCase):

    def test_post_has_all_fields(self):
        post = Post()
        fields = ["author", "title", "date", "body", "id"]
        for field in fields:
            self.assertTrue(hasattr(post, field))
