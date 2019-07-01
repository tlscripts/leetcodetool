import os
import requests
import json
import shutil

class Leet:

    def __init__(self):
        self.api_url = 'https://leetcode.com/api/problems/all/'
        self.info = requests.get(self.api_url).json()
        self.folders = ['hard', 'medium', 'easy']

    def gather(self):
        os.system('git clone https://github.com/kamyu104/LeetCode-Solutions')
        shutil.move('LeetCode-Solutions/Python/', '.')
        os.chdir('Python')

        for folder in self.folders:
            if not os.path.exists(folder):
                os.mkdir(folder)

    def move_to(self, file, folder):
        shutil.move(file, folder)

    def main(self):
        self.gather()
        files = os.listdir('.')
        for x in self.info['stat_status_pairs']:
            slug = x['stat']['question__title_slug']
            lvl = x['difficulty']['level']
            a = slug+'.py' 
            if os.path.isfile(a):
                if lvl == 3:
                    self.move_to(a, 'hard')
                if lvl == 2:
                    self.move_to(a, 'medium')
                if lvl == 1:
                    self.move_to(a, 'easy')

if __name__ == '__main__':
    leet = Leet()
    leet.main()





