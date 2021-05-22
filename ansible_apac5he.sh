# show ipv4 address
echo "-----"
echo "IPV4 ADDRESSES "
ip addr  | grep "inet "
echo "-----"
# show the ansible.cfg file
echo "ANSIBLE CONFIG " 
cat ansible.cfg
# show the ansible hosts file
echo "-----"
echo "ANSIBLE INVENTORY "
cat hosts
echo '-----'
# Verify status of Apache on local server
echo "VERIFY IF APACHE2 IS ACTIVE"
sudo systemctl status apache2
echo '-----'
# Verify Apache ports
echo "VERIFY APACHE TCP PORTS"
cat /etc/apache2/ports.conf | grep Listen
echo '-----'
# Verify Apache sites available
echo "VERIFY APACHE SITES AVAILABLE"
cat /etc/apache2/sites-available/000-default.conf | grep "<VirtualHost"
echo '-----'
# test Apache webserver#
echo "APACHE WEBSERVER TEST"
curl 192.0.2.3 | grep "It works"
echo '-----'
echo "ANSIBLE PING "
ansible webservers -m ping
echo '-----'
# Verify communication with webservers
ansible webservers -m command -a "/bin/echo Hello from Apache2"
# Ansible Gather Facts from webservers
#ansible webservers -m gather_facts --tree ./tmp_facts 