from django.test import Client
from django.test import TestCase
from posts.models.post import Post


class PostViewTest(TestCase):

    def test_list_posts(self):
        client = Client()
        post_one = Post.objects.create(author="Me", title="How to test django",
                                       body="Some body1", date="2014-10-28")
        second_post = Post.objects.create(author="Me", title="How to test django",
                                          body="Some body1", date="2014-10-28")
        third_post = Post.objects.create(author="them", title="How to test django",
                                         body="Some body 3", date="2014-10-10")

        response = client.get('/posts/')
        templates = [template.name for template in response.templates]
        all_posts = response.context['post_list']

        self.assertIn(post_one, all_posts)
        self.assertIn(second_post, all_posts)
        self.assertIn(third_post, all_posts)
        self.assertEqual(response.status_code, 200)
        self.assertIn('index.html', templates)
