#
# ~/.bashrc
#

### EXPORT ###
export EDITOR='neovim'

#PATH
export PATH=/home/nyrs/.config/emacs/bin:$PATH
export PATH=/home/nyrs/code/scripts:$PATH


# If not running interactively, don't do anything
[[ $- != *i* ]] && return


PS1='[\u@\h \W]\$ '




### ALIASES ###

#list
alias ls='ls --color=auto'
alias la='ls -a'

#pacman 
alias spu='sudo pacman -Syu'
alias sps='sudo pacman -S'
alias searpac='sudo pacman -Ss'
alias spr='sudo pacman -R'
alias sprs='sudo pacman -Rs'

#AUR
alias aur='paru -S'

#show dependencies
function_depends()  {
    search=$(echo "$1")
    sudo pacman -Sii $search | grep "Required" | sed -e "s/Required By     : //g" | sed -e "s/  /\n/g"
    }

alias depends='function_depends'

#fix typo's
alias cd..='cd ..'
alias update='sudo pacman -Syu'
alias updqte='sudo pacman -Syu'
alias upate='sudo pacman -Syu'
alias updte='sudo pacman -Syu'

#fun
alias nf='neofetch'

alias grep='grep --color=auto'
