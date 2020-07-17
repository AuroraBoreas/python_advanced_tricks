import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.blog import Blog
from unittest import mock
import unittest

class TestBlog(unittest.TestCase):
    @mock.patch('lib.blog.Blog')
    def test_blog_posts(self, mock_Blog):
        blog = mock_Blog()
        blog.posts.return_value = [
            {
                'userId': 1,
                'id':1,
                'title': 'Test Title',
                'body': 'Cillum do cillum et ea ad voluptate laboris commodo elit mollit commodo occaecat aliqua. Quis voluptate aliquip ea esse nisi proident non aliquip nostrud. Enim et elit sint aliqua voluptate velit ad eu consectetur. Duis laborum incididunt do nulla eiusmod ad ex do. Adipisicing sunt incididunt id adipisicing mollit. Deserunt aliquip mollit labore aliquip aliqua.'
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # additional assertions
        assert mock_Blog is Blog
        assert mock_Blog.called
        blog.posts.assert_called_with() # we called posts method with no arguments
        blog.posts.assert_called_once_with() # we called the posts method once
        blog.posts.assert_called_with(1, 2, 3) # test false cuz passing arguments that the method doesnt need
        blog.reset_mock() #reset mock object
        blog.posts.assert_not_called() # after resetting, posts has not been called


if __name__ == "__main__":
    unittest.main()