import math
import time

class ParkingService:
    def __init__(self, parking_area):
        self.parking_area = parking_area
        self.car_schedule = {}
    
    def car_in(self, car):
        if (self.parking_area.is_park_full()):
            print("Parking lot is full")
        else:
            self.parking_area.park_car(car)
            self.car_schedule[car.get_plat_no()] = time.time()
            plat_no = car.get_plat_no()
            print(f"Car with plat number {plat_no} is in at Timestamp {self.car_schedule[car.get_plat_no()]}")

    def remove_car(self, car):
        del self.car_schedule[car.get_plat_no()]
        
    def car_out(self, car):
        self.parking_area.remove_car(car)
        difference_time = time.time() - self.car_schedule[car.get_plat_no()]
        parking_price = math.ceil(difference_time / 10) * 1000
        plat_no = car.get_plat_no()
        print(f"Car with plat_number {plat_no} is out and the price is Rp. {parking_price}")
        self.remove_car(car)