import unittest
import test_utils

from musikk import queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.instance = queue.Queue()
        self.instance_with_items = queue.Queue()
        self.test_items = ['Track 1', 'Track 2']
        self.instance_with_items.add_items(self.test_items)
        self.assertEqual(self.test_items, self.instance_with_items.get_items())
    
    def test_get_items_empty(self):
        items = self.instance.get_items()
        self.assertEqual(len(items), 0)

    def test_add_items_append(self):
        self.instance_with_items.add_items(['Track 3', 'Track 4'], append=True)
        result = self.instance_with_items.get_items()
        self.assertEqual(['Track 1', 'Track 2', 'Track 3', 'Track 4'], result)

    def test_add_items_overwrite(self):
        self.instance_with_items.add_items(['Track 3', 'Track 4'])
        result = self.instance_with_items.get_items()
        self.assertEqual(['Track 3', 'Track 4'], result)

    def test_size(self):
        size = self.instance_with_items.size()
        self.assertEqual(len(self.test_items), size)

    def test_clear(self):
        self.instance_with_items.clear()
        items = self.instance_with_items.get_items()
        self.assertEqual(0, len(items))

    def test_get_item_failure(self):
        self.assertIsNone(self.instance.get_item(0))

    def test_get_item(self):
        self.assertEqual(self.test_items[1], self.instance_with_items.get_item(1))

    def test_get_index_initial_value_is_zero(self):
        self.assertEqual(0, self.instance.get_index())

    def test_get_current_with_no_items(self):
        self.assertIsNone(self.instance.get_current())

    def test_get_current(self):
        self.assertEqual(self.test_items[0], self.instance_with_items.get_current())

    def test_set_index_failure(self):
        current = self.instance.get_index()
        self.assertIsNone(self.instance.set_index(1))
        self.assertEqual(current, self.instance.get_index())

    def test_set_index(self):
        self.assertEqual(self.test_items[1], self.instance_with_items.set_index(1))
        self.assertEqual(1, self.instance_with_items.get_index())

    def test_get_next_at_end(self):
        self.assertIsNone(self.instance.get_next())

    def test_get_next(self):
        self.assertEqual(self.test_items[1], self.instance_with_items.get_next())

    def test_next_at_end(self):
        end = len(self.test_items) - 1
        self.instance_with_items.set_index(end)
        self.assertIsNone(self.instance_with_items.next())
        # also assert index is unchanged
        self.assertEqual(end, self.instance_with_items.get_index())

    def test_next(self):
        expected_index = 1
        self.assertEqual(self.test_items[expected_index], self.instance_with_items.next())
        self.assertEqual(expected_index, self.instance_with_items.get_index())

    def test_get_previous_at_start(self):
        self.assertIsNone(self.instance_with_items.get_previous())

    def test_get_previous(self):
        self.instance_with_items.set_index(1)
        self.assertEqual(self.test_items[0], self.instance_with_items.get_previous())

    def test_previous_at_start(self):
        self.assertIsNone(self.instance_with_items.previous())
        # also assert index is unchanged
        self.assertEqual(0, self.instance_with_items.get_index())

    def test_previous(self):
        self.instance_with_items.set_index(1)
        expected_index = 0
        self.assertEqual(self.test_items[expected_index], self.instance_with_items.previous())
        self.assertEqual(expected_index, self.instance_with_items.get_index())
