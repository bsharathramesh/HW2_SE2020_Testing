from git import Repo
import os
os.system('ruby bug_fix_ruby.rb')
repo_dir = ""
repo = Repo(repo_dir,search_parent_directories=True)

#Please Enter The absolute path of the log.txt file here!
# example : file_list = ['/home/sbangal2/SE2020/HW2_SE2020_Testing/Ruby/log.txt'] 
file_list = ['/Users/nischalkashyap/Downloads/Fall 2020/SE2020/slave/Adarsh/HW2_SE2020_Testing/Ruby/log.txt']

commit_message = "Testing Scenarios Logs"
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
