from git import Repo
import subprocess
import os

def clone_repos():
    '''
        Pulls all the remote repositories for the project and saves them inside the folder name.
        for example "common": "repo". It will save the repo in the common folder
    '''
    all_repos = {"common": "git@github.com:tbriggs1/crop-management.git", "frontend": "git@github.com:tbriggs1/crop-react.git"}

    for k, v in all_repos.items():
        try:
            Repo.clone_from(v, k)
        except:
            print("Error folder probably already exists")



def change_branch():
    '''
        We only want to run this script in a development environment, therefore we need to switch the git branch from
        master to develop
    :return:
    '''
    dir = subprocess.run('pwd', capture_output=True, text=True)
    list_dir = os.listdir(dir.stdout.rstrip('\n'))

    for i in list_dir:
        subprocess.run(f'cd {i}; git checkout develop; cd ..', shell=True, capture_output=True, text=True)

def deploy():
    clone_repos()
    change_branch()

    subprocess.run('docker-compose up -d', shell=True)



if __name__ == "__main__":
    deploy()

