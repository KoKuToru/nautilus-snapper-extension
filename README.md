# nautilus-snapper-extension
Extension for Nautilus, makes it easy to open old versions

<img src="https://rawgit.com/KoKuToru/nautilus-snapper-extension/master/screenshot.png">

#Dependencies
`nautilus-python`

#Install
Archlinux
------------
<a href="https://aur.archlinux.org/packages/nautilus-snapper-extension-git/">MAKEPKG</a>
```bash
yaourt nautilus-snapper-extension-git
```

Others
------------
Copy `nautilus-snapper-extension.py` into `~/.local/share/nautilus-python/extensions`   
Restart Nautilus.

#Usage
Make sure your user has access to the `.snapshots` folders.  
Right click on file, open properties.  
If one or more snapshots exists a new tab `Snapper` will appear.  
Double click on the version you want to open.  
It will open the file with `xdg-open`

#Info
The list in the `Snapper`-tab gets filtered by the  
last modification date of the file/snapshot.   
It wont show multiple results for the same modification date.   
It also wont show the actual state.  

#Todo

* Display the age of the file in min/hours/days.
* Display the description `snapper list` somehow.
* Ability to simply `diff` (context-menu ?).
* Message or something when access to `.snapshots` is denied.

#Bugs
`xdg-open` wont ask for which application to use for unknow 
file extensions.. 
