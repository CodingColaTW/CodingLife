import os
import git
import schedule
import time
from datetime import datetime

# 設置 Git repository 的路徑
repo_path = r'C:\Users\spark\Desktop\CodingLife\auto_program'

def commit_changes():
    repo = git.Repo(repo_path)
    repo.git.add('--all')
    commit_message = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

# 設置每天晚上11:30自動執行
schedule.every().day.at("23:30").do(commit_changes)

while True:
    schedule.run_pending()
    time.sleep(1)
