from datetime import datetime, timezone
from unittest import TestCase
from kestrel import filters


class FiltersTest(TestCase):

    def test_is_after(self):
        midnight = datetime(2018, 7, 15, 0, 0, 0, tzinfo=timezone.utc)
        morning = datetime(2018, 7, 15, 6, 0, 0, tzinfo=timezone.utc)
        noon = datetime(2018, 7, 15, 12, 0, 0, tzinfo=timezone.utc)

        is_after = filters.is_after(morning)
        self.assertTrue(is_after(noon))
        self.assertFalse(is_after(midnight))

    def test_is_before(self):
        midnight = datetime(2018, 7, 15, 0, 0, 0, tzinfo=timezone.utc)
        morning = datetime(2018, 7, 15, 6, 0, 0, tzinfo=timezone.utc)
        noon = datetime(2018, 7, 15, 12, 0, 0, tzinfo=timezone.utc)

        is_before = filters.is_before(morning)
        self.assertTrue(is_before(midnight))
        self.assertFalse(is_before(noon))

    def test_is_night(self):
        midnight = datetime(2018, 7, 15, 0, 0, 0, tzinfo=timezone.utc)
        noon = datetime(2018, 7, 15, 12, 0, 0, tzinfo=timezone.utc)
        self.assertTrue(filters.is_night(midnight))
        self.assertFalse(filters.is_night(noon))
