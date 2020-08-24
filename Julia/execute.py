from git import Repo
import os
os.system('julia HW2_Julia_G19_buggy.jl')
repo_dir = ""
repo = Repo(repo_dir,search_parent_directories=True)

#Please Enter The absolute path of the log.txt file here!
file_list = ['/home/sbangal2/SE2020/HW2_SE2020_Testing/Julia/log.txt']

commit_message = "Testing Scenarios Logs"
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()

