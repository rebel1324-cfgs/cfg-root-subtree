# template repository comment for vim 
# https://github.com/rebel1324-cfgs/jetbrain-rider
# https://github.com/rebel1324-cfgs/jetbrain-goland
# https://github.com/rebel1324-cfgs/jetbrain-clion
# https://github.com/rebel1324-cfgs/jetbrain-webstorm
# https://github.com/rebel1324-cfgs/jetbrain-pycharm

# use this one
# '<,'>s/^# \(.*\/jetbrain-\)\(.*\)/git subtree pull --prefix=\2 master

pull:
	git subtree pull --prefix=rider https://github.com/rebel1324-cfgs/jetbrain-rider master
	git subtree pull --prefix=goland https://github.com/rebel1324-cfgs/jetbrain-goland master
	git subtree pull --prefix=clion https://github.com/rebel1324-cfgs/jetbrain-clion master
	git subtree pull --prefix=webstorm https://github.com/rebel1324-cfgs/jetbrain-webstorm master
	git subtree pull --prefix=pycharm https://github.com/rebel1324-cfgs/jetbrain-pycharm master
