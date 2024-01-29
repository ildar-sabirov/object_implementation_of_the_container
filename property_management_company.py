from house import House

class PropertyManagementCompany:
    def __init__(self, name: str):
        self.__name = name
        self.__houses = []
        self.__next_company = None

    def get_name(self) -> str:
        return self.__name

    def get_houses(self) -> list[House]:
        return self.__houses

    def add_house(self, house: House) -> None:
        self.__houses.append(house)

    def remove_house(self) -> None:
        if self.__houses:
            self.__houses.pop()

    def set_next_company(self, next_company) -> None:
        self.__next_company = next_company

    def get_next_company(self):
        return self.__next_company
