sudo kill $(ps aux | grep 'python webcalc.py' | awk '{print $2}') >2& 
sudo python webcalc.py &
