import unittest
from alert.alert_system import AlertSystem

class TestAlertSystem(unittest.TestCase):
    def setUp(self):
        self.alert_system = AlertSystem(temp_threshold=35)

    def test_no_alert_triggered(self):
        data = {"temperature": 30}
        self.alert_system.check_alert(data)
        self.assertFalse(self.alert_system.alert_triggered)

    def test_alert_triggered(self):
        data = {"temperature": 37}
        self.alert_system.check_alert(data)
        self.assertTrue(self.alert_system.alert_triggered)

if __name__ == '__main__':
    unittest.main()
