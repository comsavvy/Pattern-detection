import unittest
from detect import Detect


long_url = ('PyBites My Reading List | 12 Rules for Life - #booksdiedeme.siejdis. '
            'that expand the mind! '
            'www.google.com/telephone/wire....  '
            'http://pbreadinglist.herokuapp.com/books/'
            'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter '
            "http://-www.pip.org "            
            ' #psychology #philosophy')

short_url = ("google.com "
             "twitter.com "
             "facebook.com"
             " University of ilorin .org"
             " pybites.com")

TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')


class MyTestCase(unittest.TestCase):
    def test_long_url(self):
        expected = ['www.google.com/telephone/wire',\
                    'http://pbreadinglist.herokuapp.com/books/TvEqDAAAQBAJ#.XVOriU5z2tA.twitter',\
                    'www.pip.org']
        self.assertEqual(Detect(long_url).url, expected)

    def test_short_url(self):
        expected = ['google.com', 'twitter.com', 'facebook.com', "pybites.com"]
        self.assertEqual(Detect(short_url).url, expected)


if __name__ == '__main__':
    unittest.main()
