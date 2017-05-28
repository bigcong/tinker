import re
import requests


if __name__ == '__main__':
    r = requests.get('http://www.dy2018.com/i/97873.html?t=1490963819776&jdfwkey=kpspl2')
    myPage = r.content.decode("gbk")
    print(myPage)
    urls = re.findall('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)"', myPage)
    print(len(urls))
    for i in urls:
        print(i)

