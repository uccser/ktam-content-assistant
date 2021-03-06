from tests.BaseTestWithDB import BaseTestWithDB
from tests.pikau.PikauTestDataGenerator import PikauTestDataGenerator
from django.urls import reverse


class GoalViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = PikauTestDataGenerator()

    def test_pikau_goal_view_with_no_goals(self):
        url = reverse("pikau:goal_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["goals"]), 0)

    def test_pikau_goal_view_with_one_goal(self):
        self.test_data.create_goal(1)

        url = reverse("pikau:goal_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["goals"]), 1)
        self.assertQuerysetEqual(
            response.context["goals"],
            ["<Goal: <p>Description for goal 1.</p>>"]
        )

    def test_pikau_goal_view_with_two_goals(self):
        self.test_data.create_goal(1)
        self.test_data.create_goal(2)

        url = reverse("pikau:goal_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["goals"]), 2)
        self.assertQuerysetEqual(
            response.context["goals"],
            [
                "<Goal: <p>Description for goal 1.</p>>",
                "<Goal: <p>Description for goal 2.</p>>",
            ]
        )

    def test_pikau_goal_view_order(self):
        self.test_data.create_goal(3)
        self.test_data.create_goal(2)
        self.test_data.create_goal(1)

        url = reverse("pikau:goal_list")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["goals"]), 3)
        self.assertQuerysetEqual(
            response.context["goals"],
            [
                "<Goal: <p>Description for goal 1.</p>>",
                "<Goal: <p>Description for goal 2.</p>>",
                "<Goal: <p>Description for goal 3.</p>>",
            ]
        )
