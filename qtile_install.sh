#!/usr/bin/env sh

# Welcome
echo "Welcome to my Qtile installation script. This script only works on Arch based distros"

# Deciding which branch you wnat to use
echo "Which theme do you want? You can see a preview of the different themes by taking a look at the different branches of my repo"
echo "1) All themes"
echo "2) Colorful"
echo "3) Gruvbox"
echo "4) Blue"
read THEME

# Installing extra packages
echo "Installing the necessary packages..."
sudo pacman -S nitrogen picom qtile rofi neofetch kitty neovim emacs git 

echo "What AUR helper do you have installed?"
echo "1) yay"
echo "2) paru"
read AUR

if [[ $AUR == '1' ]]; then
    echo "Installing qtile-extras with yay..."
    yay -S qtile-extras
else
    echo "Installing qtile-extras with paru..."
    paru -S qtile-extras
fi

# Cloning the repo
echo "Cloning the repo..."
if [[ $THEME == '1' ]]; then
   	git clone -b gruvbox https://github.com/Aiclys/dotfiles ~/dots/gruvbox/
   	git clone -b colorful https://github.com/Aiclys/dotfiles ~/dots/colorful/
	git clone -b blue https://github.com/Aiclys/dotfiles ~/dots/blue
elif [[ $THEME == '2' ]]; then
	git clone -b colorful https://github.com/Aiclys/dotfiles ~/dots
elif [[ $THEME == '3' ]]; then
	git clone -b gruvbox https://github.com/Aiclys/dotfiles ~/dots
elif [[ $THEME == '4' ]]; then
	git clone -b blue https://github.com/Aiclys/dotfiles ~/dots
fi

# Backups
echo "Do you want to create a backup of your current qtile configuration?"
echo "1) Yes"
echo "2) No"
read BACKUP

if [[ $BACKUP == '1' ]]
then
    echo "Creating backup..."
    mkdir ~/.config/qtile_back
    mv ~/.config/qtile ~/.config/qtile_back
else
    echo "No backup made"
fi

# Moving my dotfiles to your .config folder
echo "Which part of my dots do you want to move to your .config?"
echo "Moving dots into the .config folder..."
mv ~/dots/qtile ~/.config
