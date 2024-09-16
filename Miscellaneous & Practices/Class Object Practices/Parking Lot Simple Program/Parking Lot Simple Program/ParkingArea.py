class ParkingArea:
    CONST_FULL_PARKING_LOT = 10
    def __init__(self):
        self.parking_lot = {}
    
    def park_car(self, car):
        self.parking_lot[car.get_plat_no()] = True

    def is_park_full(self):
        if (len(self.parking_lot) == self.CONST_FULL_PARKING_LOT):
            return True
        else:
            return False
    
    def remove_car(self, car):
        del self.parking_lot[car.get_plat_no()]