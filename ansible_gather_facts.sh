sudo systemctl start ssh
ansible --version
ansible webservers -m ping
ansible webservers -m gather_facts --tree ./tmp_facts

