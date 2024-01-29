from apartment import Apartment

class House:
    def __init__(self, house_number: int):
        self.__house_number = house_number
        self.__apartments = []

    def get_house_number(self) -> int:
        return self.__house_number

    def get_apartments(self) -> list[Apartment]:
        return self.__apartments

    def add_apartment(self, apartment: Apartment) -> None:
        self.__apartments.append(apartment)

    def remove_apartment(self) -> None:
        if self.__apartments:
            self.__apartments.pop()
