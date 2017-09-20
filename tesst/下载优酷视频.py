import re
import threading
import  os
import requests


def go(url):
    cmd = 'you-get --format=flvhd "' + url + '"'
    print(cmd)
    os.system(cmd)


def test(gg=33):
    print(gg)


if __name__ == '__main__':
    r = requests.get('http://list.youku.com/albumlist/show/id_49354991.html?spm=a2h0k.8191403.0.0&sf=10100')

    myPage = r.content.decode("utf8")
    print(myPage)

    # <a href="(.*?)" title="莫烦

    mm = re.findall('<div class="p-thumb"><a href="(.*?)" title="', myPage)
    i = 0;

    for u in mm:
        url = 'http:' + u

        print(url)

        threading.Thread(target=go(url)).start()
