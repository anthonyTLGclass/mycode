# List of helpful tips to use git from the command line in Linux
step 1: Create a github repository (change license to "GNU General Public License v3.0" instead of default "none")

step 2: Create Personal Access Token (Settings-->Developer Settings-->Personal access tokens-->Tokens (Classic)-->Generate new token-->Generate new token (classic)-->create title for key (check repo box)-->Click green Generate token-->Token is displayed and be used when syncing Linux Terminal with github

step 3: Sync Terminal with Github (run lines below in Terminal)
  - student@bchd:~$ git config --global credential.helper store
  - git config --global user.name "Mona Lisa"
  - student@bchd:~$ git config --global user.email "MonaLisa@example.com"
  - student@bchd:~$ mv ~/mycode/ ~/mycode-backup/ 2>/dev/null
  - git clone https://github.com/YOUR USER NAME/mycode ~/mycode
  - cd /home/student/mycode/
  - touch /home/student/mycode/alta3research.txt
  - git status
  - git add *
  - git commit -m "First commit to learn about version controlling"
  - git push origin HEAD

  - can use get pull to get changes from an existing repository (https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)
            - $ git pull REMOTE-NAME BRANCH-NAME
              # Grabs online updates and merges them with your local work
              If you do a git pull origin <remote branch name>, it will fetch the remote branch and then merge it into your current local branch.

ref: https://stackoverflow.com/questions/8196544/what-are-the-git-concepts-of-head-master-origin

I highly recommend the book "Pro Git" by Scott Chacon. Take time and really read it, while exploring an actual git repo as you do.

HEAD: the current commit your repo is on. Most of the time HEAD points to the latest commit in your current branch, but that doesn't have to be the case. HEAD really just means "what is my repo currently pointing at".

In the event that the commit HEAD refers to is not the tip of any branch, this is called a "detached head".

master: the name of the default branch that git creates for you when first creating a repo. In most cases, "master" means "the main branch". Most shops have everyone pushing to master, and master is considered the definitive view of the repo. But it's also common for release branches to be made off of master for releasing. Your local repo has its own master branch, that almost always follows the master of a remote repo.

origin: the default name that git gives to your main remote repo. Your box has its own repo, and you most likely push out to some remote repo that you and all your coworkers push to. That remote repo is almost always called origin, but it doesn't have to be.

HEAD is an official notion in git. HEAD always has a well-defined meaning. master and origin are common names usually used in git, but they don't have to be.

# Scripts in Python
The first line of a script is usually an opportunity to describe the program that should be called to run the script. For Python, a Shebang might look like, #!/usr/bin/python3, or #!/usr/bin/env python3.Although it may take various forms, the purpose is to describe the program that should be called to run the script.

For example, a Python program without a shebang line requires you to preface the script with the word python, or python3. Scripts with a properly declared shebang line do not require this. That's because the first line describes to the interpreter the program that should be running the script.

shebang example
  #!/usr/bin/env python3
  print("ello!")
  print("Did you say, hello?")
  print("No, I said ello, but that\'s close enough.")

remove example
  #!/bin/rm
  # This script calls on the executable called **rm** (remove), which is
  # installed to the */bin* directory. When this script is run,
  # bash will execute this script with *rm*, which will remove (delete)
  # the script :p




