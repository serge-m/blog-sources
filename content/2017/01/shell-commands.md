Title: Shell commands
Author: SergeM
Date: 2017-01-08 11:10:00
Slug: shell-commands
Tags: linux,useful,ubuntu


Some linux commands that I'll probably need in the future


Kill processes occupying a certain port:
```
fuser -k 8080/tcp
``` 


Add user to a group
```
sudo usermod -aG group user
```


Remove user from a group
```
sudo gpasswd -d user group
```


Change shell for user `user` to bash
```
chsh -s /bin/bash user
```


Encode/decode binary file to ascii using command line 

[link](/encodedecode-binary-file-to-ascii.html)


Restart now:
```
shutdown -r 0
```

## SSH
generate key:
```
ssh-keygen
```

generate RSA key of length 4096 to file `my_key`
```
ssh-keygen -t rsa -b 4096 -C "your@e-mail.com" -f my_key
```

Generate md5 fingerprint of the key (works in newer ubuntu, 16):
```
ssh-keygen -lf ./my_key -E md5
```

## Detach process
Sometimes I need to detach from a process running on a remote machine so that it continues running after I logout.


Using the Job Control of bash to send the process into the background:

* `Ctrl+Z` to stop (pause) the program and get back to the shell.
* `bg` to run it in the background.
* `disown -h [job-spec]` where `[job-spec]` is the job number (like %1 for the first running job; find about your number with the jobs command) so that the job isn't killed when the terminal closes.

[source](https://stackoverflow.com/a/625436)



## Vim
[vimCheatSheet](https://www.fprintf.net/vimCheatSheet.html)
[another vim cheat scheet](https://vim.rtorr.com/)
