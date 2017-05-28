import re
import requests
import os
import threading


def go(url):
    cmd = 'you-get --format=flvhd "' + url + '"'
    print(cmd)
    os.system(cmd)


def test(gg=33):
    print(gg)


if __name__ == '__main__':
    r = requests.get('http://v.youku.com/v_show/id_XMjY3MTQ2MDE0OA==.html?spm=a2h0j.8191423.item_XMjY3MTQ2MDE0OA==.A')

    myPage = r.content.decode("utf8")
    print(myPage)
    mm = re.findall('<a class="sn"  href="(.*?)"', myPage)
    i = 0;

    for u in mm:
        url = 'http:' + u

        print(url)
        if i == 28:
            threading.Thread(target=go(url)).start()
        i=i+1
