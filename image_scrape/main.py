import glob

def build_list():
  file_list = []
  # root_dir needs a trailing slash (i.e. /root/dir/)
  root_dir = '/Users/prestonduffield/'
  extensions = ("**/*.jpeg",)
  for extension in extensions:
    for filename in glob.iglob(root_dir + extension, recursive=True):
      file_list.append(filename)
      print(filename)
  return file_list

def main():
  # build a list of files
  file_list = build_list()
  # copy files to the list
  # for file_s in file_list:
  #   print(file_s)




if __name__ == "__main__":
  main()
  print("done")
