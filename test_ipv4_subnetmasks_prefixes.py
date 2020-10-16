import unittest
import ipv4_subnetmasks_prefixes as prf

class test_ip_subnet_prefixes(unittest.TestCase):

    def test_get_net_prefix(self):
        self.assertEqual(prf.get_net_prefix('255.255.255.252'), '/30')    
        #self.assertTrue()
        #self.assertFalse()
        #with self.assertRaises(TypeError):
        
    def test_get_netmask(self):
        self.assertEqual(prf.get_netmask('/24'), '255.255.255.0')    

    def test_get_number_ip_addresses(self):
        self.assertEqual(prf.get_number_ip_addresses('/24'), 256)    

    def test_get_number_ip_hosts(self):
        self.assertEqual(prf.get_number_ip_hosts('/24'), 254)

    def test_get_network_bits(self):
        self.assertEqual(prf.get_network_bits('255.255.255.0') , '1111 1111 1111 1111 1111 1111 0000 0000')
        

if __name__ == '__main__':
    unittest.main()
