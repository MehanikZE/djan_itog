


from rest_framework.test import APITestCase


class TasksTest(APITestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_act(self):
        url = "/api/tasks/"
        resp = self.client.get(url)
        resp_j = resp.json()
        self.assertEqual(401, resp.status_code)
        self.assertIn("detail", resp_j.keys())
        self.assertEqual("Учетные данные не были предоставлены.", resp_j["detail"])
