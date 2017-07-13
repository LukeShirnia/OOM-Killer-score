# OOM-Killer
Script is designed to asses the systems process and their oom_score

 
  

To run script:

` bash <(curl -s https://raw.githubusercontent.com/luke7858/OOM-Killer-score/master/score_check.sh)`


Or 

 `for i in $(find /proc -maxdepth 1 -type d); do if [ -f "$i"/oom_score ]; then printf "$(cat "$i"/oom_score) "; pid=$(echo "$i" | awk -F'/' '{print $3}';); if [ "$(cat "$i"/oom_score)" -ge 1 ];then printf "$(ps -p "$pid" -o comm=) "; fi; printf "$i/oom_score \n"; fi; done | awk '$1 > 1' | sort -nr -k1 `
 

##Example output:##




121 mysqld /proc/24828/oom_score

103 rackspace-monit /proc/15168/oom_score 

94 varnishd /proc/13528/oom_score 

84 varnishd /proc/13527/oom_score 

45 php-fpm /proc/25685/oom_score 

44 php-fpm /proc/25686/oom_score 

42 php-fpm /proc/6820/oom_score 

42 php-fpm /proc/25687/oom_score 

41 php-fpm /proc/25684/oom_score 

40 php-fpm /proc/25683/oom_score 

39 php-fpm /proc/26555/oom_score 

36 php-fpm /proc/2879/oom_score 

36 php-fpm /proc/2868/oom_score 

19 php-fpm /proc/25681/oom_score 

17 firewalld /proc/529/oom_score 

16 driveclient /proc/21200/oom_score 

13 python /proc/10338/oom_score 

10 tuned /proc/871/oom_score 

9 polkitd /proc/4899/oom_score 

8 fail2ban-server /proc/13549/oom_score 

6 php-fpm /proc/25692/oom_score 

6 php-fpm /proc/25691/oom_score 

6 php-fpm /proc/25690/oom_score 

6 php-fpm /proc/25689/oom_score 

6 php-fpm /proc/25688/oom_score 
