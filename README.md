gitcaca
=======

gitcaca ensures a smooth integration of git, libcaca and gravatar, in
order to display commit authors' avatars in your terminal.

## Installation

Install libcaca, on Debian/Ubuntu:
```
$ sudo apt-get install caca-utils
```

Then install gitcaca:
```
$ sudo python setup.py install
```

## How to use

gitcaca stores by default the fetched avatars in
`/var/tmp/gitcaca`. You can change this, giving the `--path` argument
to gitcaca-fetch and gitcaca-display.

In the root of a git repository, fetch all gravatars by running
```
$ gitcaca-fetch
```

Then you can use gitcaca-display as a pager for some git commands
(it'd nice if we could call an external command with arguments from
`git log --pretty=format:FOO`, but apparently that's not possible. If
you know a way to achieve this, let me know!).

All instances of the string `IMG:email@example.org` will be correctly
replaced by the corresponding avatar.

The easier way is to add git aliases in the [alias] section of your
`~/.gitconfig`:
```
# log on steroids, with pictures
logg = ! git log $1 --pretty=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar) %C(reset)%C(bold blue)%an %C(reset)%C(bold yellow)%d%C(reset)%n%C(white)%s%C(reset) %n %n%bIMG:%ae' | gitcaca-display | less -

# show one commit, with picture
showg = ! git show $1 --pretty=format:'commit %H%nAuthor: %an <%ae>%nDate: %ar%n%n%s%n%n%b%nIMG:%ae' | gitcaca-display -W 30 | less -

# shows the pictures of all authors of a repo
diapo = ! git log $1 --pretty=format:'IMG:%ae' | sort | uniq | gitcaca-display -W 40 | less -
```

## Tips
If the colors are not displayed in your terminal, you can try
adding `--color=always` to your git commands, and replacing `less` by
`less -r`.
