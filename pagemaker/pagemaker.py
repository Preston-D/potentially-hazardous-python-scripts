# Author Preston D
# Purpose to clone a file and open it in a browser a specified amount of times
# Practical Usage, to send impression events on ads that have unique placement urls to test analytics on placemnts of ads
# October 2020

import shutil
import os
import webbrowser

def main():
  original = r'html_to_clone/cloneme.html'
  for i in range(10):
    newname = "clone" + str(i)
    target = r'html_files_out/'+str(newname)+'.html'
    shutil.copyfile(original, target)
    filename = 'file:///'+os.getcwd()+'/' + 'html_files_out/'+str(newname)+'.html'
    webbrowser.open_new_tab(filename)

if __name__ == "__main__":
    main()
