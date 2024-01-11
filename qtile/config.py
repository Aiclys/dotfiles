#                                                                                                                                                           
# _______ _    _ _____  ______ ______ _______ _____ _      ______ 
#|__   __| |  | |  __ \|  ____|  ____|__   __|_   _| |    |  ____|
#   | |  | |__| | |__) | |__  | |__     | |    | | | |    | |__   
#   | |  |  __  |  _  /|  __| |  __|    | |    | | | |    |  __|  
#   | |  | |  | | | \ \| |____| |____   | |   _| |_| |____| |____ 
#   |_|  |_|  |_|_|  \_\______|______|  |_|  |_____|______|______|
#                                                                                                                                                                 
#  __  __               _   _ _                         __ _         _
# |  \/  |             | | (_) |                       / _(_)       | |
# | \  / |_   _    __ _| |_ _| | ___    ___ ___  _ __ | |_ _  __ _  | |
# | |\/| | | | |  / _` | __| | |/ _ \  / __/ _ \| '_ \|  _| |/ _` | | |
# | |  | | |_| | | (_| | |_| | |  __/ | (_| (_) | | | | | | | (_| | |_|
# |_|  |_|\__, |  \__, |\__|_|_|\___|  \___\___/|_| |_|_| |_|\__, | (_)
#          __/ |     | |                                      __/ |
#         |___/      |_|                                     |___/
#
#
#
#
#
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#####################################
# ---------- @@@@@@@@@@@ ---------- #
# ---------- @ IMPORTS @ ---------- #
# ---------- @@@@@@@@@@@ ---------- #
#####################################

import colors
import os
import time
import subprocess
from libqtile import qtile
from libqtile import bar, layout, hook, extension
from libqtile.widget import base
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import EzKey as Key2
from datetime import datetime 
from qtile_extras import widget 
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupWidget
from qtile_extras.widget.mixins import ExtendedPopupMixin
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration, BorderDecoration



######################################
# ----------@@@@@@@@@@@@@ ---------- #
# ----------@ VARIABLES @ ---------- #
# ----------@@@@@@@@@@@@@ ---------- #
######################################

#KEYS
mod = "mod4"
alt = "mod1"

#PATHS
home = os.path.expanduser("~")
rofi_path_dmenu1 = home + "/.config/rofi/launchers/type-1/launcher.sh"
rofi_path_dmenu2 = home + "/.config/rofi/launchers/type-2/launcher.sh"
rofi_path_dmenu3 = home + "/.config/rofi/launchers/type-3/launcher.sh"
rofi_path_dmenu4 = home + "/.config/rofi/launchers/type-4/launcher.sh"
rofi_path_dmenu5 = home + "/.config/rofi/launchers/type-5/launcher.sh"
rofi_path_dmenu6 = home + "/.config/rofi/launchers/type-6/launcher.sh"
rofi_path_dmenu7 = home + "/.config/rofi/launchers/type-7/launcher.sh"
rofi_path_powermenu1 = home + "/.config/rofi/powermenu/type-1/powermenu.sh"
rofi_path_powermenu2 = home + "/.config/rofi/powermenu/type-2/powermenu.sh"
rofi_path_powermenu3 = home + "/.config/rofi/powermenu/type-3/powermenu.sh"
rofi_path_powermenu4 = home + "/.config/rofi/powermenu/type-4/powermenu.sh"
rofi_path_powermenu5 = home + "/.config/rofi/powermenu/type-5/powermenu.sh"
rofi_path_powermenu6 = home + "/.config/rofi/powermenu/type-6/powermenu.sh"

#APPS
terminal = "kitty"
browser = "librewolf"
browser2 = "brave"
file_browser = "thunar"
dc = "discord"
obi = "obsidian"
vs = "vscodium"
music = "spotify"
film = "freetube"
em = "emacs"
nv = "kitty -e nvim"
wall = "nitrogen"
mail = "thunderbird"
vbox = "virtualbox"
bit = "bitwarden"
#terminal = guess_terminal()


###################
#COLORS AND THEMES#  
###################

colors = colors.DoomOne

white = "#FFFFFF"
grey = "#d0d0d0"
alena_orange= "#f7896b"
weird_blue = "#81A1C1"

tokyo_black = "#000000"
tokyo_light_black = "#1A1C31"
tokyo_red = "#D22942"
tokyo_light_red = "#DE4259"
tokyo_green = "#17B67C"
tokyo_light_green = "#3FD7A0"
tokyo_yellow = "#F2A174"
tokyo_light_yellow = "#EEC09F"
tokyo_blue = "#8B8AF1"
tokyo_light_blue = "#A7A5FB"
tokyo_magenta = "#D78AF1"
tokyo_light_magenta = "#E5A5FB"
tokyo_cyan = "#4FCFEB"
tokyo_light_cyan = "#82E3F8"
tokyo_grey = "#B4C0EC"
tokyo_white = "#CAD3F5"

#Catppuccin

cat_mauve = "#DDB6F2"
cat_pink = "#F5C2E7"
cat_maroon = "#E8A2AF"
cat_red = "#F28FAD"
cat_peach = "#F8BD96"


#Solarized Dark
sol_base00 = "#657b83"
sol_base0 = "#839496"
sol_base01 = "#586e75"
sol_base02 = "#073642"
sol_base03 = "#002b36"
sol_base1 = "#93a1a1"
sol_base2 = "#eee8d5"
sol_base3 = "#fdf6e3"
sol_yellow = "#b58900"
sol_orange ="#cb4b16"
sol_red ="#dc322f"
sol_magenta ="#d33682"
sol_violet = "#6c71c4"
sol_blue = "#268bd2"
sol_cyan = "#2aa198"
sol_green = "#859900"
sol_dark_green = "#1D1D1D"




###################################################
# --------------- @@@@@@@@@@@@@@@ --------------- #
# --------------- @ KEYBINDINGS @ --------------- #
# --------------- @@@@@@@@@@@@@@@ --------------- #
###################################################

keys = [

    ########################
    #SWITCH BETWEEN WINDOWS#
    ########################
    Key(
        [mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),

    Key(
        [mod], "l", 
        lazy.layout.right(),
        desc="Move focus to right"
    ),

    Key(
        [mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),

    Key(
        [mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),

    Key(
        [mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),

    Key(
        [mod], "Up", 
        lazy.layout.up()
    ),

    Key(
        [mod], "Down", 
        lazy.layout.down()
    ),

    Key(
        [mod], "Left", 
        lazy.layout.left()
    ),
    
    Key(
        [mod], "Right", 
        lazy.layout.right()
    ),


    #############
    #MOVE WINDOW#
    #############
    Key(
        [mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
    ),

    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),

    Key(
        [mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),

    Key(
        [mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),

    Key(
        [mod, "shift"], "Up", 
        lazy.layout.shuffle_up()
    ),

    Key(
        [mod, "shift"], "Down", 
        lazy.layout.shuffle_down()
    ),

    Key(
        [mod, "shift"], "Left", 
        lazy.layout.swap_left()
    ),
    
    Key(
        [mod, "shift"], "Right", 
        lazy.layout.swap_right()
    ),


    #############
    #GROW WINDOW#
    #############
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),

    Key(
        [mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),

    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),

    Key(
        [mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),

    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),

    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),

    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),

    Key(
        [mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    
    Key(
        [mod], "z",
        lazy.layout.flip(),
    ),

    Key(
        [mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),

    Key(
        [mod, "shift"], "Return", 
        lazy.layout.toggle_split(), 
        desc="Toggle between split and unsplit sides of stack"
    ),

    Key(
        [mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),


    #############
    #SCREENSHOTS#
    #############
    Key(
        [mod, "shift"], "s", 
        lazy.spawn("flameshot"), 
        desc="Launch Flameshot"
    ),

    Key(
        [mod, alt], "s", 
        lazy.spawn("scrot 'Screenshot_%Y-%m-%d_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) ; viewnior $$(xdg-user-dir PICTURES)/$f'"), 
        desc="Takes a Screenshot"
    ),


    #############
    #LAUNCH APPS#
    #############
    Key([mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),

    Key(
        [mod], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    Key(
        [mod, "shift"], "b", 
        lazy.spawn(browser2), 
        desc="Launch Brave"
    ),

    Key(
        [mod, "shift"], "l", 
        lazy.spawn(browser), 
        desc="Launch LibreWolf"
    ),

    Key(
        [mod, "shift"], "f", 
        lazy.spawn(file_browser), 
        desc="Launch file browser"
    ),

    Key(
        [mod, "shift"], "t", 
        lazy.spawn("tor-browser"), 
        desc="Launch Tor Browser"
    ),

    Key(
        [mod, "shift"], "o", 
        lazy.spawn(obi), 
        desc="Launch Obsidian"
    ),

    Key([mod, "shift"], "d", 
        lazy.spawn(dc), 
        desc="Launch Discord"
    ),

    Key(
        [mod, "shift"], "s", 
        lazy.spawn(music), 
        desc="Launch Spotify"
    ),

    Key(
        [mod, "shift"], "y", 
        lazy.spawn(film), 
        desc="Launch FreeTube"
    ),

    Key(
        [mod, "shift"], "c", 
        lazy.spawn(vs), 
        desc="Launch VSCodium"
    ),

    Key(
        [mod, "shift"], "e", 
        lazy.spawn(em), 
        desc="Launch Emacs"
    ),

    Key(
        [mod, "shift"], "n", 
        lazy.spawn(nv), 
        desc="Launch Neovim"
    ),

    Key(
        [mod, "shift"], "w", 
        lazy.spawn(wall), 
        desc="Launch Nitrogen"
    ),

    Key(
        [mod, "shift"], "m", 
        lazy.spawn(mail), 
        desc="Launch Thunderbird"
    ),
    
    Key(
        [mod, "shift"], "v",
        lazy.spawn(vbox),
        desc="Launch VirtualBox"
    ),

    Key([mod, "shift"], "p",
        lazy.spawn(bit),
        desc="Launch Bitwarden"
    ),

    ######
    #MISC#
    ######
    Key(
        [mod], "b",
        lazy.hide_show_bar(),
        desc="Hides the bar"
    ),

    Key(
        [mod], "f", 
        lazy.window.toggle_fullscreen(), 
        desc="Toggle fullscreen on the focused window"
    ),

    Key(
        [mod], "t", 
        lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"
    ),

    Key(
        [mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),

    Key(
        [mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),

    Key(
        [mod], "r", 
        lazy.spawn(rofi_path_dmenu2), 
        desc="Launch dmenu"
    ),

    Key(
        [mod], "p", 
        lazy.spawn(rofi_path_powermenu2), 
        desc="Launch powermenu"
    ),

    #Key(
    #    [mod], "r", 
    #    lazy.spawn("rofi -show drun -show-icons"), 
    #    desc="Launch rofi app-launcher"
    #),

    Key(
        [mod], "l", 
        lazy.spawn("betterlockscreen -l"), 
        desc="Lock screen"
    ),


    #######
    #AUDIO#
    #######
    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer -D pulse sset Master 1%+"),
        desc="Raise volume"
    ),

    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn("amixer -D pulse sset Master 1%-"),
        desc="Lower volume"
    ),

    Key(
        [], "XF86AudioMute", 
        lazy.spawn("amixer set Master toggle"),
        desc="Mute"
    ),
]



####################################
# ---------- @@@@@@@@@@ ---------- #
# ---------- @ GROUPS @ ---------- #
# ---------- @@@@@@@@@@ ---------- #
####################################


groups = [
    Group(
        "1", 
        matches=[Match(wm_class=["LibreWolf"])],
        spawn=browser, label="web"
    ),

    Group(
        "2",
        matches=[Match(wm_class=["VSCodium"])],
        label="code"
    ),

    Group(
        "3", 
        matches=[Match(wm_class=["obsidian"])], 
        label="note"
    ),

    Group(
        "4",
        matches=[Match(wm_class=["FreeTube"])], 
        label="watch"
    ),

    Group(
        "5",
        matches=[Match(wm_class=["Thunar"])], 
        label="files"
    ),

    Group(
        "6",
        matches=[Match(wm_class=["Spotify"])], 
        label="music"
    ),

    Group(
        "7", 
        matches=[Match(wm_class=["discord", "Signal"])], 
        spawn=dc, label="comm"
    ),
]

#Labels
# "߷"
# "֎"
# "০"
# "১"
# "২"
# "ೱ"
# "࿋"
# "࿌"
# "᳃"
# "⌘"
# "" Firefox
# "" Terminal
# "", ""Spotify
# "" Thunar
# "" Code
# "" Server
# "" Games
# "" Media


#groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )



#############
#  LAYOUTS  #
#############

layouts = [
    #layout.Columns(
    #    border_focus=tokyo_grey, 
    #    border_normal=tokyo_black, 
    #    border_on_single=True, 
    #    border_width=3,
    #    margin=10
    #),
    layout.MonadThreeCol(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        border_on_single=True,
        margin=10
    ),


    #layout.Max(
    #    border_focus=tokyo_grey,
    #    border_normal=tokyo_black,
    #    border_width=3,
    #    margin=10
    #),

    #layout.Stack(
    #    num_stacks=2,
    #    border_focus=tokyo_grey,
    #    border_normal=tokyo_black,
    #    border_width=3,
    #    margin=10
    #),

    # layout.Bsp(),

    # layout.Matrix(),

    layout.MonadTall(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        margin=10
    ),

    # layout.MonadWide(),

    # layout.RatioTile(),

    # layout.Slice(),

    layout.Spiral(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        margin=10
    ),

    # layout.Stack(),

    # layout.Tile(),

    layout.TreeTab(),

    # layout.VerticalTile(),

    # layout.Zoomy(),

    layout.Floating(
        border_focus=tokyo_grey,
        border_normal=tokyo_light_black,
        border_width=3,
        fullscreen_border_width=3
    ),

]



#################################
# ---------- @@@@@@@ ---------- #
# ---------- @ BAR @ ---------- #
# ---------- @@@@@@@ ---------- #
#################################

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def open_neofetch(qtile):
    qtile.cmd_spawn('kitty -e neofetch')



def init_widgets_list():
    widgets_list = [
            widget.Spacer(
                length = 2,
                background = tokyo_black
            ),

            widget.Image(
                filename = "~/.config/qtile/archlogo.png",
                background = tokyo_black,
                margin = 3,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(
                        f'{terminal} -e nvim {home}/.config/qtile/config.py'
                    )
                },
                #mouse_callbacks = {
                #  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e bash-pipes")
                #}
            ),


            widget.GroupBox(
                font = "Iosevka Nerd Font",
                fontsize = 18,
                background = tokyo_black,
                borderwidth = 8,
                highlight_method = "block",
                this_current_screen_border = grey,
                inactive = white, 
                active = weird_blue, 
            ),

            widget.Spacer(
                length = 0,
                background = tokyo_black,
            ),

            widget.WindowName(
                background = weird_blue,
                foreground = white,
                empty_group_string = "[threenineone@azathoth]$",
                fontsize = 15,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right") 
                #]
            ),

            #widget.Spacer(
            #    length = 70,
            #    background = tokyo_light_magenta,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.Spacer(
                length = 10,
                background = tokyo_black,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right") 
                #]

            ),
            #widget.Spacer(
            #   length = 10,
            #    background =sol_base03, 
            #    decorations = [
            #        PowerLineDecoration(path="arrow_right") 
            #    ]
#
#            ),
            #widget.Image(
            #    filename = "~/.config/qtile/volume.png",
            #    background = tokyo_light_cyan,
            #    foreground = tokyo_grey,
            #    margin = 3,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),
            widget.NvidiaSensors(
                foreground = weird_blue,
                fmt = "GPU: {}",
                background = tokyo_black,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_black
            ),

            widget.Volume(
                foreground = "#81A1C1",
                background = tokyo_black,
                fmt = '🕫  Vol: {}',
                #emoji = True, 
                #emoji_list = ['🔇', '🔈', '🔉', '🔊'],
                fontsize = 15,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            widget.Spacer(
                length = 10,
                background = tokyo_black
            ),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.CurrentLayout(
                foreground = "#81A1C1",
                background = tokyo_black,
                fontsize = 15,
                #padding = 10,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.Spacer(
                length = 10,
                background = tokyo_black
            ),

            #widget.Image(
            #    filename = "~/.config/qtile/cpu.png",
            #    margin = 3
            #),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_black
            #),

            widget.CPU(
            #    format = "{load_percent}% ",
                foreground = "#81A1C1",
                background = tokyo_black,
                fontsize = 15,
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e gtop")
                },
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            #widget.Spacer(
            #    length = 10,
            #    background = tokyo_light_black
            #),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_light_black
            #),

            widget.Spacer(
                 length = 10,
                 background = tokyo_black
            ),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 17,
                text = "",
                #text= "",
                foreground = "#81A1C1",
                background = tokyo_black,
            ),

            widget.Memory(
                background = tokyo_black,
                foreground = "#81A1C1",
                fontsize = 15,
                mouse_callbacks = {
                  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                },
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            #widget.MemoryGraph(
            #    background = tokyo_light_black,
            #    graph_color = tokyo_magenta,
            #    fill_color = tokyo_magenta,
            #    border_color = tokyo_black,
            #    mouse_callbacks = {
            #      'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
            #    }
            #),

            widget.Spacer(
                length = 10,
                background = tokyo_black
            ),

            #widget.Sep(
            #    linewidth = 3,
            #    margin = 5,
            #    background = tokyo_grey
            #),

            #widget.Spacer(
            #    length = bar.STRETCH,
            #    background = sol_base01,
            #    decorations = [
            #        PowerLineDecoration()
            #    ]
            #),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = "#81A1C1",
                background = tokyo_black
            ),

            widget.Net(
                format = "{down} ↓↑ {up}",
                foreground = "#81A1C1",
                background = tokyo_black,
                update_interval = 2,
                #mouse_callbacks = {
                #    'Button1': lambda : qtile.cmd_spawn(f"networkmanager_dmenu {dmenu_conf}")
                #}
                #decorations = [
                #   PowerLineDecoration(path="arrow_right")
                #]
            ),

            #widget.Sep(
            #    size_percent = 60,
            #    linewidth = 3,
            #    background = tokyo_light_black
            #),

            widget.Spacer(
                length = 10,
                background = tokyo_black
            ),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = "#81A1C1",
                background = tokyo_black,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            widget.Clock(
                format = '%b %d-%Y',
                foreground = "#81A1C1",
                background = tokyo_black,
                #decorations = [
                #    PowerLineDecoration(path="arrow_right")
                #]
            ),

            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = "#81A1C1",
                background = tokyo_black
            ),

            widget.Clock(
                format = '%I:%M:%S %p',
                foreground = "#81A1C1",
                background = tokyo_black,
                #decorations = [
                #PowerLineDecoration(path="arrow_right")
                #]
            ),

            widget.Systray(
                background = tokyo_black, 
            ),

            widget.Spacer(
                length = 5,
                background = tokyo_black,
            ),
    ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=30, opacity=0.9, margin=[5,10,0,10]))]

screens = init_screens()
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),

    Drag(
        [mod], "Button3", 
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),

    Click(
        [mod], "Button2", 
        lazy.window.bring_to_front()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=tokyo_grey,
    border_normal=tokyo_light_black,
    border_width=3,
    fullscreen_border_width=3
        
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


#################################################
# ---------- @@@@@@@@@@@@@@@@@@@@@@@ ---------- #
# ---------- @ HOOKS AND AUTOSTART @ ---------- #
# ---------- @@@@@@@@@@@@@@@@@@@@@@@ ---------- #
#################################################

@hook.subscribe.startup_once
def autostart():
    auto_home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([auto_home])
    time.sleep(2)
    subprocess.call(["picom", "--experimental-backends", "-b"])












# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
