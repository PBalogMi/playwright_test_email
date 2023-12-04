import unittest
from unittest.mock import Mock, patch
from playwright.sync_api import Page
from src.logout import Logout


class TestLogout(unittest.TestCase):

    def setUp(self):
        self.mocked_page = Mock(spec=Page)
        self.logout = Logout(self.mocked_page)

    def test_execute_logout(self):
        credentials = {"account_name": "Test User", "email": "test@example.com"}

        with patch.object(self.mocked_page, "get_by_label") as mock_get_by_label, \
                patch.object(self.mocked_page, "frame_locator") as mock_frame_locator, \
                patch.object(self.mocked_page, "get_by_role") as mock_get_by_role:

            mock_get_by_label.return_value = mock_get_by_label
            mock_get_by_label.click.return_value = None
            mock_frame_locator.return_value = mock_frame_locator
            mock_frame_locator.get_by_role.return_value = mock_get_by_role
            mock_get_by_role.click.return_value = None

            self.logout.execute_logout(credentials)

            mock_get_by_label.assert_called_once_with(f"Google Account: {credentials['account_name']}  \n({credentials['email']})")
            mock_get_by_label.click.assert_called()

            mock_frame_locator.assert_called_once_with("iframe[name=\"account\"]")
            mock_frame_locator.get_by_role.assert_called_once_with("link", name="Sign out")
            mock_get_by_role.click.assert_called()
