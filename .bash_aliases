alias ll='ls -al'
alias gadd='git add .'
alias gst='git status'
__git_complete gst _git_status
alias gci='git commit'
__git_complete gci _git_commit
alias gco='git checkout'
__git_complete gco _git_checkout
alias push='git push'
__git_complete push _git_push
alias pull='git pull'
__git_complete pull _git_pull
alias fetch='git fetch'
__git_complete fetch _git_fetch
alias gbr='git branch'
__git_complete gbr _git_branch

