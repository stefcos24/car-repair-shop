# GIT Workflow and naming branches

## Instruction to start project
- Choose issue from Trello (e.g. CRM-1 Customers)
- Locally switch to release/2023.1 branch and make
```bash
$ git pull
```
- After that create new branch feature/CRM-1-customers
(we must follow this concept to have more readable worktree)
**feature/{issue_number}-{name of issue}**
```bash
$ git branch feature/CRM-1-customers
```
- When we created new branch we need to position ourselves on that branch
```bash
$ git checkout feature/CRM-1-customers
```
- **This two commands in git for creating and checkout on branch can be
done in one line with git checkout and adding -b to end** but it is right
either way
```bash
$ git checkout -b feature/CRM-1-customers
```
- When we are positioned on that branch then we start working on 
new issue
- After we complete our journey and work is done for that issue, then
we must track all files where we made changes **git status** - where we
check tracking and untracking files
```bash
$ git status
```
- After that we have all red untracked files and use **git add** to 
add it. We can use --all on the end to track all files in one or put 
name of file on each one.
```bash
$ git add --all
```
- When we have all tracking files, now we commit it. Message must be 
provided like this **{issue_number} {what you did}**
```bash
$ git commit -m "CRM-1 Added new Customer model and CRUD operations"
```
- Now we switch on release branch and create git pull to have
last changes made on that branch
```bash
$ git checkout release/2023.1
$ git pull
```
- After that we come back to our branch CRM-1-customers and merge
everything from release into our branch
```bash
$ git checkout feature/CRM-1-customers
$ git merge release/2023.1
```
- In the end we need only to push our branch.
```bash
$ git push
```
