from agent_selector_advanced import agent_selector
import unittest

#three agent detail lists and issues lists were created for testing. They are tested on all three selection modes.

class TestAgent(unittest.TestCase):

    agents_1 = [{'is_available': True, 'available_since': '06/22/2020 08:22 AM', 'Roles': ['Sales', 'Services']},
          {'is_available': True, 'available_since': '06/22/2020 12:59 PM', 'Roles': ['Support', 'Services']},
          {'is_available': False, 'available_since': '06/22/2020 06:38 PM', 'Roles': ['Chinese Language', 'Services']},
          {'is_available': True, 'available_since': '06/22/2020 12:05 PM', 'Roles': ['Sales', 'Spanish Language']},
          {'is_available': False, 'available_since': '06/22/2020 10:03 AM', 'Roles': ['Chinese Language', 'Spanish Language']},
          {'is_available': True, 'available_since': '06/22/2020 07:07 PM', 'Roles': ['Customer Service', 'Support']}]
    issues_1 = ['Sales', 'Support', 'Sales', 'Sales', 'Chinese Language']
    result_leastbusy_1 = {0: [0], 1: [1], 2: [0], 3: [0], 4: []}
    result_allavailable_1 = {0: [0, 3], 1: [1, 5], 2: [0, 3], 3: [0, 3], 4: []}
    result_random_1 = [{0: [0], 1: [5], 2: [0], 3: [0], 4: []},  {0: [0], 1: [1], 2: [0], 3: [0], 4: []},
                       {0: [3], 1: [5], 2: [0], 3: [0], 4: []},  {0: [3], 1: [1], 2: [0], 3: [0], 4: []},
                       {0: [0], 1: [5], 2: [3], 3: [0], 4: []},  {0: [0], 1: [1], 2: [3], 3: [0], 4: []},
                       {0: [0], 1: [5], 2: [0], 3: [3], 4: []},  {0: [0], 1: [1], 2: [0], 3: [3], 4: []},
                       {0: [3], 1: [5], 2: [3], 3: [0], 4: []},  {0: [3], 1: [1], 2: [3], 3: [0], 4: []},
                       {0: [3], 1: [5], 2: [0], 3: [3], 4: []},  {0: [3], 1: [1], 2: [0], 3: [3], 4: []},
                       {0: [0], 1: [5], 2: [3], 3: [3], 4: []},  {0: [0], 1: [1], 2: [3], 3: [3], 4: []},
                       {0: [3], 1: [5], 2: [3], 3: [3], 4: []},  {0: [3], 1: [1], 2: [3], 3: [3], 4: []}]
    
    agents_2 = [{'is_available': True, 'available_since': '06/22/2020 12:37 PM', 'Roles': ['Customer Service', 'Support']},
            {'is_available': True, 'available_since': '06/22/2020 09:14 AM', 'Roles': ['Customer Service', 'Spanish Language']},
            {'is_available': True, 'available_since': '06/22/2020 04:35 PM', 'Roles': ['Chinese Language', 'Support']},
            {'is_available': True, 'available_since': '06/22/2020 12:28 PM', 'Roles': ['Chinese Language', 'Services']},
            {'is_available': False, 'available_since': '06/22/2020 05:23 PM', 'Roles': ['Services', 'Chinese Language']},
            {'is_available': False, 'available_since': '06/22/2020 03:01 PM', 'Roles': ['Spanish Language', 'Customer Service']},
            {'is_available': False, 'available_since': '06/22/2020 05:38 PM', 'Roles': ['Services', 'Chinese Language']},
            {'is_available': False, 'available_since': '06/22/2020 09:33 AM', 'Roles': ['Services', 'Chinese Language']}]
    issues_2 = ['Sales', 'Support', 'Sales']
    result_leastbusy_2 = {0: [], 1: [0], 2: []}
    result_allavailable_2 = {0: [], 1: [0, 2], 2: []}
    result_random_2 = [{0: [], 1: [2], 2: []}, {0: [], 1: [0], 2: []}]
    
    agents_3 = [{'is_available': False, 'available_since': '06/22/2020 01:13 PM', 'Roles': ['Spanish Language', 'Support']},
            {'is_available': True, 'available_since': '06/22/2020 07:52 PM', 'Roles': ['Customer Service', 'Support']},
            {'is_available': True, 'available_since': '06/22/2020 05:42 PM', 'Roles': ['Support', 'Customer Service']},
            {'is_available': False, 'available_since': '06/22/2020 06:22 PM', 'Roles': ['Sales', 'Chinese Language']},
            {'is_available': False, 'available_since': '06/22/2020 05:00 PM', 'Roles': ['Support', 'Sales']},
            {'is_available': False, 'available_since': '06/22/2020 02:47 PM', 'Roles': ['Support', 'Sales']},
            {'is_available': False, 'available_since': '06/22/2020 03:12 PM', 'Roles': ['Support', 'Services']},
            {'is_available': False, 'available_since': '06/22/2020 08:54 AM', 'Roles': ['Spanish Language', 'Customer Service']},
            {'is_available': False, 'available_since': '06/22/2020 05:34 PM', 'Roles': ['Chinese Language', 'Spanish Language']},
            {'is_available': False, 'available_since': '06/22/2020 11:29 AM', 'Roles': ['Customer Service', 'Spanish Language']},
            {'is_available': False, 'available_since': '06/22/2020 04:12 PM', 'Roles': ['Spanish Language', 'Sales']},
            {'is_available': True, 'available_since': '06/22/2020 11:53 AM', 'Roles': ['Spanish Language', 'Support']}]
    issues_3 = ['Spanish Language']
    result_leastbusy_3 = {0: [11]}
    result_allavailable_3 = {0: [11]}
    result_random_3 = {0: [11]}
    
    def _init_(self):
        self.agents_1
        self.issues_1 
        self.result_leastbusy_1
        self.result_allavailable_1
        self.result_random_1
        self.agents_2
        self.issues_2
        self.result_leastbusy_2
        self.result_allavailable_2
        self.result_random_2
        self.agents_3
        self.issues_3
        self.result_leastbusy_3
        self.result_allavailable_3
        self.result_random_3
        
    def test_least_busy(self):
        self.assertEqual(agent_selector(self.agents_1, 'least busy', self.issues_1), self.result_leastbusy_1)
        self.assertEqual(agent_selector(self.agents_2, 'least busy', self.issues_2), self.result_leastbusy_2)
        self.assertEqual(agent_selector(self.agents_3, 'least_busy', self.issues_3), self.result_leastbusy_3)
        
    def test_all_available(self):
        self.assertEqual(agent_selector(self.agents_1, 'all available', self.issues_1), self.result_allavailable_1)
        self.assertEqual(agent_selector(self.agents_2, 'all available', self.issues_2), self.result_allavailable_2)
        self.assertEqual(agent_selector(self.agents_3, 'all available', self.issues_3), self.result_allavailable_3)
        
    def test_random(self):
        self.assertEqual(agent_selector(self.agents_3, 'random', self.issues_3), self.result_random_3)
        self.assertIn(agent_selector(self.agents_2, 'random', self.issues_2), self.result_random_2, msg = None)
        self.assertIn(agent_selector(self.agents_1, 'random', self.issues_1), self.result_random_1, msg = None)
                
if __name__ == '__main__':
    unittest.main(verbosity = 2)
    
    
    
    
    
    






