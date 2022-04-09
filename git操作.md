# git 操作命令

## 怎么看当前git分支是基于哪个分支创建的
git reflog --date=local --all | grep

## 回滚 commit
git reset --mixed HEAD^
git rm --cached 01-Project-Inner/2021/0720-nowtvstructure/code-0728-sample/nowtvstructure