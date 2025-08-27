# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON 🔋")

    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF 📴")


# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # inherit from Device
        self.storage = storage
        self.__camera_megapixels = camera_megapixels  # encapsulation (private)

    def take_photo(self):
        print(f"📸 Taking a photo with {self.__camera_megapixels}MP camera")

    def install_app(self, app_name):
        print(f"📲 Installing {app_name}...")

    def get_camera_specs(self):  # controlled access (encapsulation)
        return f"{self.__camera_megapixels} MP"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 108)
phone2 = Smartphone("Apple", "iPhone 15", "128GB", 48)

phone1.power_on()
phone1.take_photo()
print("Camera Specs:", phone1.get_camera_specs())
phone1.install_app("WhatsApp")

phone2.power_on()
phone2.take_photo()
