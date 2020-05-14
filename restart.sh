sudo kill $(ps aux | grep 'python webcalc/webrestapi.py' | awk '{print $2}') 
tmux
sudo python webcalc/webrestapi.py &
tmux detach
