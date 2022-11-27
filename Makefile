# template repository comment for vim 
# https://github.com/rebel1324-cfgs/jetbrain-rider
# https://github.com/rebel1324-cfgs/jetbrain-goland
# https://github.com/rebel1324-cfgs/jetbrain-clion
# https://github.com/rebel1324-cfgs/jetbrain-webstorm
# https://github.com/rebel1324-cfgs/jetbrain-pycharm

# use this one
# '<,'>s/^# \(.*\/jetbrain-\)\(.*\)/git subtree pull --prefix=\2 master

pull:
	git subtree pull --prefix=rider https://github.com/rebel1324-cfgs/jetbrain-rider master --squash
	git subtree pull --prefix=goland https://github.com/rebel1324-cfgs/jetbrain-goland master --squash
	git subtree pull --prefix=clion https://github.com/rebel1324-cfgs/jetbrain-clion master --squash
	git subtree pull --prefix=webstorm https://github.com/rebel1324-cfgs/jetbrain-webstorm master --squash
	git subtree pull --prefix=pycharm https://github.com/rebel1324-cfgs/jetbrain-pycharm master --squash

push:
	git subtree push --prefix=rider https://github.com/rebel1324-cfgs/jetbrain-rider master
	git subtree push --prefix=goland https://github.com/rebel1324-cfgs/jetbrain-goland master 
	git subtree push --prefix=clion https://github.com/rebel1324-cfgs/jetbrain-clion master 
	git subtree push --prefix=webstorm https://github.com/rebel1324-cfgs/jetbrain-webstorm master 
	git subtree push --prefix=pycharm https://github.com/rebel1324-cfgs/jetbrain-pycharm master 
