import unittest
from selenium import webdriver

class TestHostelManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def test_title(self):
        self.driver.get("file:///path/to/your/file.html")  # Replace with the actual path to your HTML file
        expected_title = "Hostel Management System"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title, f"Expected title: '{expected_title}', Actual title: '{actual_title}'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
