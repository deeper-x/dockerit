from unittest import TestCase, mock, main as run_test
from client import Client

class TestClient(TestCase):
    def setUp(self):
        self.__c = Client()

    @mock.patch('client.docker')
    def test_is_connection(self, mock_docker):
        connected = self.__c.new_connection()

        self.assertTrue(connected)


if __name__ == '__main__':
    run_test()