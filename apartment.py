class Apartment:
    def __init__(self, apartment_number: int, area: float):
        self.__apartment_number = apartment_number
        self.__area = area

    def get_apartment_number(self) -> int:
        return self.__apartment_number

    def get_area(self) -> float:
        return self.__area
