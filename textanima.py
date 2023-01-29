'''This started as a BBOSPP (By Al Sweigert: https://inventwithpython.com/bigbookpython/) 
project for an animated progress bar and a simulated download as an application of that function.
I have added some additional functions for text based animations for use in other projects'''

'''TODO: Code review, git init, push to git hub'''

import random, time, sys, shutil, re, os

def get_progress_bar(progress, total, bar_width = 40):
    '''Return a string that represents a progress bar.
    has bars = bar_width and has progressed an amount = progress
    out of a total amount'''

    BAR = chr(9608)
    progress_bar = ''
    progress_bar += '['
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
    number_bars = int((progress / total) * bar_width)
    progress_bar += BAR * number_bars
    progress_bar += ' ' * (bar_width - number_bars)
    progress_bar += ']'
    progress_bar += ' ' + str(total) + '/' + str(total)
    return progress_bar


def job_simulation(job_size=100):
    '''Simulate a job to test the progress bar function.
    Also provides boilerplate for implementing the progress bar.'''
    downloaded = 0
    while downloaded < job_size:
        downloaded += random.randint(0, 100)
        bar_str = get_progress_bar(downloaded, job_size)
        print(bar_str, end = '', flush = True)
        time.sleep(0.2)
        print('\b' * len(bar_str), end = '', flush = True)


def spinner_bar(timer):
    '''Animate a spinning bar in place to represent loading progress.'''
    spinner_frames = '|/-\\'
    count = 0
    try:
        while count < timer:
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            for i in range(len(spinner_frames)):
                print(spinner_frames[i], end='', flush=True)
                print('\b', end = '', flush = True)
                time.sleep(0.2)
            count += 1
    except KeyboardInterrupt:
        sys.exit()


def text_crawl(txt):
    '''Function to make supplied text crawl from left to right
    across the terminal similar to a chiron on a news broadcast.
    TODO: refactor.'''

    letter_list = [i for i in txt]
    display_str = ''
    WIDTH = shutil.get_terminal_size()[0]
    count = 1
    count_2 = 1
    try:
        while True:
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            if len(display_str) < len(txt):
                display_str += letter_list[-1 * count]
                count += 1
                print('\r', end='', flush=True)
                for i in reversed(display_str):
                    print(i, end='', flush=True)
                    time.sleep(0.009)
            elif len(display_str) >= len(txt) and len(display_str) != WIDTH:
                display_str += ' '
                print('\r', end='', flush=True)
                for i in reversed(display_str):
                    print(i, end='', flush=True)
                    time.sleep(0.001)
            if len(display_str) == WIDTH and len(re.findall('[a-z]', display_str)) >= 1:
                display_str += ' '
                display_str = display_str[count_2 : ]
                count_2 += 1
                print('\r', end='', flush=True)
                for i in reversed(display_str):
                    print(i, end='', flush=True)
                    time.sleep(0.000025)
            if len(display_str) >= WIDTH and re.findall('[a-z]', display_str) == []:
                display_str = ''
                count = 1
                count_2 = 1
    except KeyboardInterrupt:
        sys.exit()

def ghost_type(txt):
    '''Displays the supplied text letter by letter as if it
    is being typed. '''

    try:
        for i in txt:
            print(i, end='', flush=True)
            time.sleep(0.05)
    except KeyboardInterrupt:
        sys.exit()


def loading_dots(timer):
    '''Another animated loading sequence, 
    using a growing and shirinking string of elipses.'''

    count = 0
    while count < timer:
        try:
            sys.stdout.write("\033[?25l")#removes the terminal cursor
            sys.stdout.flush()
            frames = ['   ', '.', '..', '...']
            for i in range(0, 4):
                time.sleep(0.1)
                print(frames[i], end='', flush=True)
                time.sleep(0.1)
                print('\b' * len(frames[i]), end='', flush=True )
            count += 1
        except KeyboardInterrupt:
            sys.exit()


def center_print(txt):
    '''Prints the supplied text centered in the current terminal
    window.'''

    print(txt.center(shutil.get_terminal_size().columns))


def clear_line():
    '''Clear current line and carriage return the cursor.
    Used for printing mulitiple lines of text one after the
    other in place.'''

    WIDTH = shutil.get_terminal_size()[0]
    print('\r' + ' ' * WIDTH, end='\r', flush=True)

def binary_wipe():
    '''Animated transition.
    Fills the terminal window with growing strings of 1 and 0
    then wipes all content from the terminal.'''

    WIDTH = shutil.get_terminal_size()[0]
    HEIGHT = shutil.get_terminal_size()[1]
    char_list = ['0', '1', ' ']
    display_str = ''

    for i in range(HEIGHT):
        for i in range(WIDTH):
            display_str += random.choice(char_list)
        print(display_str, end='', flush=True)
        time.sleep(0.05)

    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
