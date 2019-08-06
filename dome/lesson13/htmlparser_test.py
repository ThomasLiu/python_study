from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import Request,urlopen
import re

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

def get_data(url):
   req = Request(url)
   req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
   with urlopen(req, timeout=25) as f:
      data = f.read()
      print(f'Status: {f.status} {f.reason}')
   return data.decode("utf-8")

class MyHTMLParser2(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata='' # 设置一个空的标志位
        self.info = []

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):

        if self.__parsedata == 'name':
            # 通过标志位判断，输出打印标签内容
            self.info.append(f'会议名称:{data}')

        if self.__parsedata == 'time':
            self.info.append(f'会议时间:{data}')

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                self.info.append(f'会议年份:{data.strip()}')

        if self.__parsedata == 'location':
            self.info.append(f'会议地点:{data} \n')

def main():
   parser = MyHTMLParser2()
   URL = 'https://www.python.org/events/python-events/'
   data = get_data(URL)
   parser.feed(data)
   for s in parser.info:
      print(s)

if __name__ == '__main__':
   main()
