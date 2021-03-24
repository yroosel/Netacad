clear
ip addr
sudo systemctl start ssh
ansible webservers -m ping
ansible webservers -m command -a "/bin/echo hello world"
sudo systemctl status apache2
cat /etc/apache2/ports.conf
cat /etc/apache2/sites-available/000-default.conf
