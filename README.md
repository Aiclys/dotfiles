
```
                    .___      __    _____.__.__                 
  _____ ___.__.   __| _/_____/  |__/ ____\__|  |   ____   ______
 /     <   |  |  / __ |/  _ \   __\   __\|  |  | _/ __ \ /  ___/
|  Y Y  \___  | / /_/ (  <_> )  |  |  |  |  |  |_\  ___/ \___ \ 
|__|_|  / ____| \____ |\____/|__|  |__|  |__|____/\___  >____  >
      \/\/           \/                               \/     \/ 
                                                                                                                  
```




## **Download:**

**Step 1 (clone the repository):**
```
git clone https://github.com/Aiclys/qtile-dotfiles ~/dots
```

**Step 2 (create a backup):**
```
cd ~/.config/qtile
touch config_back.py
cp config.py config_back.py
```
(do the same thing with your other files if needed)

**Step 3 (move the files into your .config directory):**
```
cp ~/dots/qtile/config.py ~/.config/qtile/config.py
mv ~/dots/qtile/autostart.sh ~/.config/qtile
chmod +x ~/.config/qtile/autostart.sh
mv ~/dots/qtile/archlogo.png ~/.config/qtile
mv ~/dots/qtile/cpu.png ~/.config/qtile
mv ~/dots/qtile/volume.png ~/.config/qtile  
```

Repeat this process with the other folders (picom, betterlockscreen, kitty and rofi)

## **Screenshots:**

1:
![Screenshot](https://github.com/Aiclys/qtile-dotfiles/blob/main/new_dots.png)

2:
![Screenshot](https://github.com/Aiclys/qtile-dotfiles/blob/main/Screenshot_2023-12-07_3440x1440.png)

3:
![Screenshot](https://github.com/Aiclys/qtile-dotfiles/blob/main/screen_new.png)


Do `git clone https://github.com/Aiclys/My-Wallpaper ~/Wallpapers` or manually install [my wallpapers](https://github.com/Aiclys/My-Wallpaper) from my other repo to get them.

## **Software I use:**
```
 OS: ArcoLinux
 WM: qtile
 Compositor: picom
 App Launcher and Powermenu: rofi
 Utilities and fun scripts: neofetch; pfetch; bash-pipes; shell-color-scripts; cmatrix
 Terminal: kitty
 Lockscreen: betterlockscreen
 Browser: librewolf-bin; brave-bin
 Editor: emacs; neovim (Lazyvim Distro)
 File browser: thunar
 Communication: discord
 Music: spotify
 Entertainment: freetube-bin
 Screenshots: flameshot
```
Do
```
sudo pacman -S picom qtile rofi neofetch kitty neovim thunar discord emacs flameshot
```
and 
```
 yay -S betterlockscreen pfetch bash-pipes shell-color-scripts spotify freetube-bin librewolf-bin brave-bin cmatrix
```
 or
```
 paru -S betterlockscreen pfetch bash-pipes shell-color-scripts spotify freetube-bin librewolf-bin brave-bin cmatrix
```
to install on Arch based distros.


## **To-Dos:**
+ **installation script**
+ **fix rofi config and scripts**


## **CREDITS:**
+ ![rofi](https://github.com/adi1090x/rofi)
