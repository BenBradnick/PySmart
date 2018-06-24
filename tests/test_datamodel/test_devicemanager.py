from pysmart.datamodel.devicemanager import DeviceManager
from pysmart.datamodel.device import Device
from pysmart.framework.devicestate import DeviceState
import unittest


class DeviceManagerCreation(unittest.TestCase):

    def test_new_DeviceManager_has_empty_device_list_when_devices_is_None(self):
        device_manager = DeviceManager()

        self.assertEquals(0, len(device_manager.device_list))

    def test_new_DeviceManager_has_single_device_in_device_list_when_devices_is_device(self):
        device_name = "Light"
        device = Device(device_name)

        device_manager = DeviceManager(devices=device)

        self.assertEquals(1, len(device_manager.device_list))
        self.assertEquals(device_name, device_manager.device_list[0].name)

    def test_new_DeviceManager_has_three_devices_in_device_list_when_devices_contains_three_devices(self):
        device1_name = "Light"
        device2_name = "Lamp"
        device3_name = "Plug"
        devices = [
            Device(device1_name),
            Device(device2_name),
            Device(device3_name)
        ]

        device_manager = DeviceManager(devices=devices)

        self.assertEquals(3, len(device_manager.device_list))
        self.assertEquals(device1_name, device_manager.device_list[0].name)
        self.assertEquals(device2_name, device_manager.device_list[1].name)
        self.assertEquals(device3_name, device_manager.device_list[2].name)

    def test_new_DeviceManager_raises_ValueError_when_initialised_with_duplicates(self):
        device_name = "Light"
        devices = [
            Device(device_name),
            Device(device_name)
        ]

        self.assertRaises(ValueError, DeviceManager, devices=devices)

    def test_new_DeviceManager_raises_TypeError_when_given_non_Device_types(self):
        string_arg = "String"
        float_arg = 3.4
        integer_arg = 3
        bool_arg = False

        self.assertRaises(TypeError, DeviceManager, devices=string_arg)
        self.assertRaises(TypeError, DeviceManager, devices=float_arg)
        self.assertRaises(TypeError, DeviceManager, devices=integer_arg)
        self.assertRaises(TypeError, DeviceManager, devices=bool_arg)


class AddMethod(unittest.TestCase):

    def test_adding_to_empty_DeviceManager_adds_device_to_device_list(self):
        device_manager = DeviceManager()
        device_name = "Toaster"
        device = Device(device_name)

        device_manager.add(device)

        self.assertEquals(1, len(device_manager.device_list))
        self.assertEquals(device_name, device_manager.device_list[0].name)

    def test_adding_to_non_empty_DeviceManager_adds_device_to_end_of_device_list(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_manager = DeviceManager(device1)

        device_manager.add(device2)

        self.assertEquals(2, len(device_manager.device_list))
        self.assertEquals(device2_name, device_manager.device_list[1].name)

    def test_adding_non_Device_type_raises_TypeError(self):
        device_manager = DeviceManager()
        string_arg = "String"
        bool_arg = True
        float_arg = 3.5
        integer_arg = 3

        self.assertRaises(TypeError, device_manager.add, string_arg)
        self.assertRaises(TypeError, device_manager.add, bool_arg)
        self.assertRaises(TypeError, device_manager.add, float_arg)
        self.assertRaises(TypeError, device_manager.add, integer_arg)
        self.assertEquals(0, len(device_manager.device_list))

    def test_adding_existing_device_raises_ValueError(self):
        device_name = "Lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)

        self.assertRaises(ValueError, device_manager.add, device)


class AddListMethod(unittest.TestCase):

    def test_adding_list_to_empty_DeviceManager_adds_list_to_device_list(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_manager = DeviceManager()

        device_manager.add(device1)
        device_manager.add(device2)

        self.assertEquals(2, len(device_manager.device_list))
        self.assertEquals(device1_name, device_manager.device_list[0].name)
        self.assertEquals(device2_name, device_manager.device_list[1].name)

    def test_adding_list_to_non_empty_DeviceManager_adds_list_to_end_of_device_list(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device3_name = "Bedroom light"
        device4_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device3 = Device(device3_name)
        device4 = Device(device4_name)
        initial_device_list = [device1, device2]
        additional_device_list = [device3, device4]
        device_manager = DeviceManager(devices=initial_device_list)

        device_manager.add_list(additional_device_list)

        self.assertEquals(4, len(device_manager.device_list))
        self.assertEquals(device1_name, device_manager.device_list[0].name)
        self.assertEquals(device2_name, device_manager.device_list[1].name)
        self.assertEquals(device3_name, device_manager.device_list[2].name)
        self.assertEquals(device4_name, device_manager.device_list[3].name)

    def test_adding_single_device_instead_of_list_still_adds_device_to_device_list(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device3_name = "Bedroom light"
        device4_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device3 = Device(device3_name)
        device4 = Device(device4_name)
        initial_device_list = [device1, device2, device3]
        device_manager = DeviceManager(devices=initial_device_list)

        device_manager.add_list(device4)

        self.assertEquals(4, len(device_manager.device_list))
        self.assertEquals(device1_name, device_manager.device_list[0].name)
        self.assertEquals(device2_name, device_manager.device_list[1].name)
        self.assertEquals(device3_name, device_manager.device_list[2].name)
        self.assertEquals(device4_name, device_manager.device_list[3].name)

    def test_adding_non_Device_Types_raises_TypeError(self):
        device_manager = DeviceManager()
        arg_list = [4.0, 3, "String", False]

        self.assertRaises(TypeError, device_manager.add_list, arg_list)
        self.assertEquals(0, len(device_manager.device_list))

    def test_adding_duplicate_device_raises_ValueError(self):
        device_name = "Lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)

        self.assertRaises(ValueError, device_manager.add_list, device)

    def test_adding_duplicate_devices_raises_ValueError(self):
        device_name = "Lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)
        additional_device_list = [device, device]

        self.assertRaises(ValueError, device_manager.add_list, additional_device_list)


class FindMethod(unittest.TestCase):

    def test_returns_device_when_device_with_device_name_exists(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device3_name = "Bedroom light"
        device4_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device3 = Device(device3_name)
        device4 = Device(device4_name)
        device_list = [device1, device2, device3, device4]
        device_manager = DeviceManager(devices=device_list)

        found_device = device_manager.find("Lamp")

        self.assertEquals("Lamp", found_device.name)

    def test_returns_None_when_device_with_device_name_does_not_exist(self):
        device1_name = "Toaster"
        device2_name = "Lamp"
        device3_name = "Bedroom light"
        device4_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device3 = Device(device3_name)
        device4 = Device(device4_name)
        device_list = [device1, device2, device3, device4]
        device_manager = DeviceManager(devices=device_list)

        found_device = device_manager.find("Bathroom heater")

        self.assertEquals(None, found_device)


class DeviceWithSameNameAlreadyExistsMethod(unittest.TestCase):

    def test_returns_True_for_device_name_already_used(self):
        device_name = "Bedroom lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)

        self.assertEquals(
            True, device_manager.device_with_same_name_already_exists(device)
        )

    def test_returns_False_for_device_name_not_yet_used(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_manager = DeviceManager(devices=device1)

        self.assertEquals(
            False, device_manager.device_with_same_name_already_exists(device2)
        )


class DeleteMethod(unittest.TestCase):

    def test_removes_device_with_device_name_from_device_list_with_one_device(self):
        device_name = "Bedroom lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)

        device_manager.delete(device_name)

        self.assertEquals(0, len(device_manager.device_list))

    def test_removes_device_with_device_name_from_device_list_with_two_devices(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_manager = DeviceManager(devices=[device1, device2])

        device_manager.delete(device1_name)

        self.assertEquals(1, len(device_manager.device_list))
        self.assertEquals(device2_name, device_manager.device_list[0].name)

    def test_does_nothing_to_empty_device_list(self):
        device_manager = DeviceManager()

        device_manager.delete("Bathroom heater")

        self.assertEquals(0, len(device_manager.device_list))

    def test_does_not_remove_device_when_device_name_does_not_exist(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_manager = DeviceManager(devices=[device1, device2])

        device_manager.delete("Bathroom heater")

        self.assertEquals(2, len(device_manager.device_list))
        self.assertEquals(device1_name, device_manager.device_list[0].name)
        self.assertEquals(device2_name, device_manager.device_list[1].name)


class TurnOnMethod(unittest.TestCase):

    def test_switches_state_of_device_to_on_when_device_with_name_exists(self):
        device_name = "Bedroom lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)

        device_manager.turn_on(device_name)

        self.assertEquals(DeviceState.ON, device_manager.find(device_name).state)

    def test_switches_state_of_correct_device_to_on_when_multiple_devices_exist(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_list = [device1, device2]
        device_manager = DeviceManager(devices=device_list)

        device_manager.turn_on(device2_name)

        self.assertEquals(DeviceState.ON, device_manager.find(device2_name).state)
        self.assertEquals(DeviceState.OFF, device_manager.find(device1_name).state)

    def test_does_not_switch_state_of_any_device_if_device_does_not_exist(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_list = [device1, device2]
        device_manager = DeviceManager(devices=device_list)

        device_manager.turn_on("Heating")

        self.assertEquals(DeviceState.OFF, device_manager.find(device2_name).state)
        self.assertEquals(DeviceState.OFF, device_manager.find(device1_name).state)


class TurnOffMethod(unittest.TestCase):

    def test_switches_state_of_device_to_off_when_device_with_name_exists(self):
        device_name = "Bedroom lamp"
        device = Device(device_name)
        device_manager = DeviceManager(devices=device)
        device_manager.turn_on(device_name)

        device_manager.turn_off(device_name)

        self.assertEquals(DeviceState.OFF, device_manager.find(device_name).state)

    def test_switches_state_of_correct_device_to_off_when_multiple_devices_exist(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_list = [device1, device2]
        device_manager = DeviceManager(devices=device_list)
        device_manager.turn_on(device1_name)
        device_manager.turn_on(device2_name)

        device_manager.turn_off(device2_name)

        self.assertEquals(DeviceState.OFF, device_manager.find(device2_name).state)
        self.assertEquals(DeviceState.ON, device_manager.find(device1_name).state)

    def test_does_not_switch_state_of_any_device_if_device_does_not_exist(self):
        device1_name = "Bedroom lamp"
        device2_name = "Living room light"
        device1 = Device(device1_name)
        device2 = Device(device2_name)
        device_list = [device1, device2]
        device_manager = DeviceManager(devices=device_list)
        device_manager.turn_on(device1_name)
        device_manager.turn_on(device2_name)

        device_manager.turn_off("Heating")

        self.assertEquals(DeviceState.ON, device_manager.find(device2_name).state)
        self.assertEquals(DeviceState.ON, device_manager.find(device1_name).state)
