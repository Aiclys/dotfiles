#⠰⢀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⡐
#⠰⢀
#⠰⢀   |      |
#⠰⢀   ||    ||   \   /      
#⠰⢀   | |  | |    \ /     
#⠰⢀   |  ||  |     |      
#⠰⢀   |      |     |      |
#⠰⢀   |      |     |       \              
#⠰⢀  
#⠰⢀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⠰⡀⠆⡐
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

#############
#  IMPORTS  #
#############

import os
import time
import subprocess
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.widget import base
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import EzKey as Key2



###############
#  VARIABLES  #
###############

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
#terminal = guess_terminal()



      ###################
     #  @@@@@@@@@@@@@@@  #
    #   @ KEYBINDINGS @   #
     #  @@@@@@@@@@@@@@@  #
      ###################

keys = [

    ##########################
    # SWITCH BETWEEN WINDOWS #
    ##########################
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
        desc="Move focus up"),
    Key(
        [mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),


    ###############
    # MOVE WINDOW #
    ###############
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


    ###############
    # GROW WINDOW #
    ###############
    Key(
        [mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),

    Key(
        [mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),

    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),

    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
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

    ###############
    # SCREENSHOTS #
    ###############
    Key(
        [mod, "shift"], "p", 
        lazy.spawn("flameshot"), 
        desc="Launch Flameshot"
    ),

    Key(
        [mod, alt], "p", 
        lazy.spawn("scrot 'Screenshot_%Y-%m-%d_$wx$h.png' -e 'mv $f $$(xdg-user-dir PICTURES) ; viewnior $$(xdg-user-dir PICTURES)/$f'"), 
        desc="Takes a Screenshot"
    ),

    ##############
    #LAUNCH APPS #
    ##############
    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),

    Key(
        [mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
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
        [mod, "shift"], "t", 
        lazy.spawn(file_browser), 
        desc="Launch file browser"
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
        [mod, "shift"], "v", 
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

    ########
    # MISC #
    ########
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
        lazy.spawn(rofi_path_dmenu1), 
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


    #########
    # AUDIO #
    #########
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



        ##############
       #  @@@@@@@@@@  #
     ##   @ GROUPS @   ##
       #  @@@@@@@@@@  #
        ##############


groups = [
    Group(
        "1", 
        matches=[Match(wm_class=["LibreWolf"])],
        spawn=browser, label=""
    ),

    Group(
        "2",
        matches=[Match(wm_class=["VSCodium"])],
        label=""
    ),

    Group(
        "3", 
        matches=[Match(wm_class=["obsidian"])], 
        label=""
    ),

    Group(
        "4",
        matches=[Match(wm_class=["FreeTube"])], 
        label=""
    ),

    Group(
        "5",
        matches=[Match(wm_class=["Thunar"])], 
        label=""
    ),

    Group(
        "6",
        matches=[Match(wm_class=["Spotify"])], 
        label=""
    ),

    Group(
        "7", 
        matches=[Match(wm_class=["discord", "Signal"])], 
        spawn=dc, label=""
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



#######################
#  COLORS AND THEMES  #
#######################

#Tokyo Night x Catpuccin Mocha
tokyo_black = "#0F0F1C"
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








#Gruvbox



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
        border_normal=tokyo_black,
        border_width=3,
        margin=10
    ),

    layout.MonadThreeCol(
        border_focus=tokyo_grey,
        border_normal=tokyo_black,
        border_width=3,
        border_on_single=True,
        margin=10
    ),

    # layout.MonadWide(),

    # layout.RatioTile(),

    # layout.Slice(),

    layout.Spiral(
        border_focus=tokyo_grey,
        border_normal=tokyo_black,
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
        border_normal=tokyo_black,
        border_width=3,
        fullscreen_border_width=3
    ),

]



#########
#  BAR  #
#########

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
                background = tokyo_light_black
            ),
            widget.Image(
                filename = "~/.config/qtile/archlogo.png",
                background = tokyo_light_black,
                margin = 3,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(
                        f'{terminal} -e nvim {home}/.config/qtile/config.py'
                    )
                }
                #mouse_callbacks = {
                #  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e bash-pipes")
                #}
            ),
            widget.Spacer(
                length = 20,
                background = tokyo_light_black
            ),
            widget.GroupBox(
                font = "Iosevka Nerd Font",
                fontsize = 18,
                foreground = tokyo_cyan,
                background = tokyo_light_black,
                borderwidth = 8,
                highlight_method = "block",
                this_current_screen_border = tokyo_light_black,
                active = tokyo_blue,
                inactive = tokyo_white
            ),
            widget.Spacer(
                length = 20,
                background = tokyo_light_black
            ),
            widget.WindowName(
                background = tokyo_light_black,
                foreground = tokyo_grey,
                empty_group_string = "",
                fontsize = 15
            ),
            widget.Spacer(
                length = 70,
                background = tokyo_light_black
            ),
            widget.Sep(
                linewidth = 3,
                margin = 5,
                background = tokyo_light_black
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_light_black
            ),
            widget.Image(
                filename = "~/.config/qtile/volume.png",
                background = tokyo_light_black,
                foreground = tokyo_grey,
                margin = 3,
            ),
            widget.Volume(
                foreground = tokyo_green,
                background = tokyo_light_black,
                # emoji = True,
                # emoji_list = ['🔇', '🔈', '🔉', '🔊'],
                fontsize = 15
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_light_black
            ),
            widget.Sep(
                linewidth = 3,
                margin = 5,
                background = tokyo_light_black
            ),
            widget.CurrentLayout(
                foreground = tokyo_white,
                background = tokyo_light_black,
                fontsize = 15,
                padding = 10
            ),
            widget.Sep(
                linewidth = 3,
                margin = 5,
                background = tokyo_light_black
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_light_black
            ),
            widget.Image(
                filename = "~/.config/qtile/cpu.png",
                background = tokyo_light_black,
                foreground = tokyo_cyan,
                margin = 3,

            ),
            widget.CPU(
                format = "{load_percent}% ",
                foreground = cat_peach,
                background = tokyo_light_black,
                fontsize = 15,
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e gtop")
                }
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_light_black
            ),
            widget.Sep(
                linewidth = 3,
                margin = 5,
                background = tokyo_light_black
            ),
            widget.Spacer(
                length = 10,
                background = tokyo_light_black
            ),
            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 17,
                text = "",
                #text= "",
                foreground = tokyo_blue,
                background = tokyo_light_black,
            ),
            widget.Memory(
                background = tokyo_light_black,
                foreground = tokyo_blue,
                fontsize = 15,
                mouse_callbacks = {
                  'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                }
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
                background = tokyo_light_black
            ),
            widget.Sep(
                linewidth = 3,
                margin = 5,
                background = tokyo_light_black
            ),
            widget.Spacer(
                length = bar.STRETCH,
                background = tokyo_light_black
            ),
            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = tokyo_light_cyan,
                background = tokyo_light_black
            ),
            widget.Net(
                format = "{down} ↓↑ {up}",
                foreground = tokyo_light_cyan,
                background = tokyo_light_black,
                update_interval = 2,
                #mouse_callbacks = {
                #    'Button1': lambda : qtile.cmd_spawn(f"networkmanager_dmenu {dmenu_conf}")
                #}
            ),
            widget.Sep(
                size_percent = 60,
                linewidth = 3,
                background = tokyo_light_black
            ),
            widget.Spacer(
                length = 5,
                background = tokyo_light_black
            ),
            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = tokyo_red,
                background = tokyo_light_black
            ),
            widget.Clock(
                format = '%b %d-%Y',
                foreground = tokyo_red,
                background = tokyo_light_black
            ),
            widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = "",
                foreground = tokyo_green,
                background = tokyo_light_black
            ),
            widget.Clock(
                format = '%I:%M:%S %p',
                foreground = tokyo_green,
                background = tokyo_light_black
            ),
            widget.Systray(
                background = tokyo_light_black 
            ),
            widget.Spacer(
                length = 5,
                background = tokyo_light_black 
            )
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
    border_normal=tokyo_black,
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


#########################
#  HOOKS AND AUTOSTART  #
#########################

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
