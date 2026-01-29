### Configure Email:
`git config --global sendemail.smtp-encryption tls`  
`git config --global sendemail.smtpserver zeus.spd.analog.com`  

### Outlook Email format:
`https://elinux.org/Mail_client_tips`  

### Configure Upstream Tree:
`git remote add upstream https://github.com/torvalds/linux`  
`git fetch upstream`  
`git worktree add -b regmap_7_17_format_wr ../torvalds_linux upstream/master` 

### Create Patches:
`git format-patch HEAD~1`  
or  
with cover letter: `git format-patch --cover-letter HEAD~2 -o iio-adrf6780`  

### New patch version:
`git format-patch -v4 HEAD~2 -o iio-adrf6780`  

### Resend patch:
`git format-patch --subject-prefix="RESEND PATCH" -v4 HEAD~2 -o iio-adrf6780`

### Obtain Maintainters:
`./scripts/get_maintainer.pl 0001-regmap-add-support-for-7-17-register-formating.patch`  

### Send Patches:
`git send-email --to=antoniu.miclaus@analog.com --cc=antoniu.miclaus@analog.com 0001-regmap-add-support-for-7-17-register-formating.patch`  
or  
with script: `git send-email --to-cmd='./scripts/get_maintainer.pl --norolestats 000*' 0001-regmap-add-support-for-7-17-register-formating.patch`  
or  
with thread: `git send-email --thread 000*`  
