from web import myapp
import unittest

class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = myapp.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Congratulations' in rv.data

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

if __name__ == '__main__':
    unittest.main()
