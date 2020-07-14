
# ff stands for "find files"
ff () { find . -maxdepth 1 -iname "*$1*" -print; }

mkcd () { mkdir -p "$@" && cd "$@" ; }

# References:-
# * https://github.com/awhan/ap_configs_hall/blob/master/bashrc - contains a
#   lot of functions that might be useful.
