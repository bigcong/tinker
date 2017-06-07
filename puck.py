import os
import time

import axe


def go():
    t = str(int(time.time() * 1000))
    t_x = '/sdcard/img/' + t + '_x.png'
    t_y = '/sdcard/img/' + t + '_y.png'

    os.system('adb shell screencap -p ' + t_x + ' & adb shell input tap 500 500')
    time.sleep(1)
    os.system('adb shell screencap -p ' + t_y)


def gogo():
    os.system('adb shell rm -rf /sdcard/img/*')
    for i in range(10):
        go();
    os.system('rm -rf img')
    os.system('adb pull /sdcard/img .')
    axe.go()


if __name__ == '__main__':
    for i in range(100):
        gogo()

# sched = BlockingScheduler()
# sched.add_job(go, 'interval', seconds=1)
# sched.start()
