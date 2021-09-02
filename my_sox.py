import sox as sox_obj
import time
import os
import subprocess
from playing_song import *


def recording_audio():
    process = subprocess.Popen(['rec', '-d', 'recorded_song.mp3', 'trim', '0', '10'], stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)


def audio_record():
    if os.system('rec -d /home/navya/Documents/my_song.mp3 trim 0 20') == 0:
        return True, 'successfully executed'
    else:
        return False, 'command not found'


'''
def audio_test():
    time.sleep(30)
    tfm = sox.Transformer()
    tfm.trim(0, 10)
    tfm.build('/home/navya/Documents/my_song.mp3', '/home/navya/Android_Robot/Resources_files/my_file.mp3')
    # os.remove('/home/navya/Documents/new_file.mp3')
    audio_info = sox.file_info.info('/home/navya/Android_Robot/Resources_files/my_file.mp3')
    status = sox.file_info.stat('/home/navya/Android_Robot/Resources_files/my_file.mp3')
    # return audio_info, status
    print(status)
    max_amp = status['Maximum amplitude']
    min_amp = status['Minimum amplitude']
    avg_amp = status['Midline amplitude']
    res_amp = status['Mean    norm']
    if res_amp == avg_amp:
        return "normal sound"
    elif res_amp > avg_amp:
        return "huge sound"
    elif res_amp < avg_amp:
        return "low sound"
    else:
        return "silent"

'''


def max_min_vol(filename):
    time.sleep(5)
    status = sox_obj.file_info.stat(filename)
    print(status)
    # max_vol, min_vol = status['Maximum amplitude'], status['Minimum amplitude']
    print("max vol :", status['Maximum amplitude'])
    print("min vol :", status['Minimum amplitude'])
    avg_amp = status['Midline amplitude']
    # res_amp = status['Mean    norm']
    res_amp = status['Mean    amplitude']
    if res_amp == avg_amp:
        print("normal sound")
    elif res_amp > avg_amp:
        print("huge sound")
    elif res_amp < avg_amp:
        print("low sound")
    else:
        print("silent")




if __name__ == '__main__':
    #open_app('Music Player')
    #print(play_song())
    #print("input file :")
    #max_min_vol('LifeOfRam.mp3')
    recording_audio()
    # sox_obj.file_info.stat('recorded_song.mp3')
    print("output file :")
    max_min_vol('recorded_song.mp3')
