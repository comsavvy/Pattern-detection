#!usr/bin/python
import re


class Detect:
    """
    Detect(text: str)\n
    class for detecting some basic patterns such as:\n
    * Number
    * URL
    * Hashtags

    """
    def __init__(self, text: str):
        self.text = text

    def long_url(self: None) -> list:
        """
        This can be use to match only long url (Standard URL)\n
        e.g. www.google.com, www.stackoverflow.com/, https://www.twitter.com
        """
        return None if (url := re.findall(r'(?:http://)?(?:\w+\.\S+\.\S+[^.\s)])', self.text)) == [] else url

    def short_url(self: None):
        """
        This method can be used to capture short url or long
        But it can capture non-url as url e.g olusola.og, sholay.pb etc
        i.e The pattern is base on 1 or more dot(.)
        """
        return None if (url := re.findall(r'(?:http://)?\w+\.\S*', self.text)) == [] else url

    @property
    def number(self) -> list:
        """
        The method will capture all the numbers in a string

        """
        return None if (num := re.findall(r'\d+', self.text)) == [] else num

    @property
    def url(self):
        """
        url will first perform operation on long_url, if it returns None then it will move on to
        short_url method and return the value e.g values or None
        But if the long_url requirement is mearnt it stop moving the control to short_url.
        """
        return self.short_url() if (r := self.long_url()) is None else r

    @property
    def hashtags(self):
        """
        Checking for hashtags in a text e.g
        #sholay, #comsavvy, #endsars etc.
        """
        return None if (exp := re.findall(r'[^A-Za-z](#[\w]*)', self.text)) == [] else exp


if __name__ == "__main__":
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
                 " www.facebook.com"
                 " university of ilorin .org")
    a = Detect(long_url).url
    print(a)
