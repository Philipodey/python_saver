from unittest import TestCase

from class_practice.Native import Native


class TestNative(TestCase):
    def test_native_object(self):
        my_native = Native("Philip", "scv23030")
        print(my_native)
        print(my_native.get_name)
        my_native.set_name("Philip")
        print("The name of the student of is", my_native.get_name())
        my_native.set_scv_id("scv23030")
        prin
        t("The students scv id is", my_native.get_scv_id())

