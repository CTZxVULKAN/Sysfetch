# Sysfetch
A minimal tool to display system stats.
<br>
![License](https://img.shields.io/github/license/BiswasJishnu/Sysfetch?style=flat-square)
![Platform](https://img.shields.io/static/v1?label=platform&message=Linux&style=flat-square&color=orange)
![Project Banner](./repo/RepoBanner.png)

## Dependencies

* [python](https://www.python.org/) - For obvious reasons.
* [psutil](https://pypi.org/project/psutil/) - Python library for getting system information.
* [Nerd Font Hack](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/Hack) - Patched font used to display icons.
 
<br>

## Screenshots

![Project Screenshot](./repo/screenshot1.png)

<br> 

## Installation 

### Symbolic Link

1. Clone this repository

``` html
git clone https://github.com/BiswasJishnu/Sysfetch.git

```

2. Copy the sysfetch.py

``` html
mkdir ~/.sysfetch
cd Sysfetch
cp sysfetch.py ~/.sysfetch/

```

> * Over here the python file from the git repo directory is being copied to .sysfetch directory. You may change the location.

3. Make the file executable

``` html
cd ~/.sysfetch
sudo chmod +x sysfetch.py

```

4. Make sure python dependencies are installed

``` html
pip3 install psutil
or 
pip install psutil

```

5. Create the symbolic link

```html
sudo ln -s /path/to/sysfetch/sysfetch.py /usr/bin/sysfetch

```

Now you can run the program with 

```html
$ sysfetch
```

> * Incase you need to remove the symbolic link use the command below
> sudo rm /usr/bin/sysfetch
