from apartment import Apartment
from house import House
from property_management_company import PropertyManagementCompany

class Dialog:
    def __init__(self):
        self.__companies = []
        self.__company = None
        self.__head = None

    def create_company(self, name: str) -> None:
        new_company = PropertyManagementCompany(name)
        self.__companies.append(new_company)
        if not self.__head:
            self.__head = new_company
        else:
            current_company = self.__head
            previous_company = None
            while current_company and current_company.get_name() < name:
                previous_company = current_company
                current_company = current_company.get_next_company()
            if previous_company:
                previous_company.set_next_company(new_company)
                new_company.set_next_company(current_company)
            else:
                new_company.set_next_company(self.__head)
                self.__head = new_company

    def choose_or_create_company(self) -> None:
        if self.__companies:
            print("Выберите компанию:")
            for index, company in enumerate(self.__companies):
                print(f"{index + 1}. {company.get_name()}")

            choice = input(
                "Введите номер компании или введите новое название, "
                "чтобы создать компанию: "
            )

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.__companies):
                    self.__company = self.__companies[index]
                    print(f"Выбрана компания {self.__company.get_name()}.")
                else:
                    print("Некорректный номер компании.")
            else:
                company = self.find_company_by_name(choice)
                if company:
                    self.__company = company
                    print(f"Выбрана компания {self.__company.get_name()}.")
                else:
                    print(
                        f"Компания с названием {choice} не найдена. "
                        f"Создайте новую компанию."
                    )
                    new_company_name = choice
                    self.create_company(new_company_name)
                    self.__company = self.find_company_by_name(new_company_name)
                    print(f"Создана новая компания {new_company_name}.")
        else:
            print("Нет доступных компаний.")

    def find_company_by_name(self, name: str):
        current_company = self.__head
        while current_company:
            if current_company.get_name() == name:
                return current_company
            current_company = current_company.get_next_company()
        return None

    def print_companies(self) -> None:
        current_company = self.__head
        while current_company:
            print(current_company.get_name())
            current_company = current_company.get_next_company()

    def add_house(self, house_number: int) -> None:
        if self.__company is not None:
            house = House(house_number)
            self.__company.add_house(house)
            print(
                f"Дом с номером {house_number} добавлен в "
                f"компанию {self.__company.get_name()}."
            )
        else:
            print("Компания не выбрана. Пожалуйста, выберите компанию.")

    def remove_house(self) -> None:
        if self.__company is not None:
            houses = self.__company.get_houses()
            if houses:
                self.__company.remove_house()
                print(
                    f"Последний добавленный дом удален из "
                    f"компании {self.__company.get_name()}."
                )
            else:
                print(
                    "В выбранной компании нет добавленных домов. "
                    "Удаление дома не выполнено."
                )
        else:
            print("Компания не выбрана. Пожалуйста, выберите компанию.")

    def add_apartment(self, house_number: int, apartment_number: int,
                      area: float) -> None:
        if self.__company is not None:
            houses = self.__company.get_houses()
            house = next((h for h in houses if h.get_house_number() == house_number),
                         None)
            if house:
                apartment = Apartment(apartment_number, area)
                house.add_apartment(apartment)
                print(
                    f"Квартира с номером {apartment_number} добавлена в "
                    f"дом {house_number}."
                )
            else:
                print(
                    f"Дом с номером {house_number} не найден в выбранной компании. "
                    f"Квартира не может быть добавлена."
                )
        else:
            print("Компания не выбрана. Пожалуйста, выберите компанию.")

    def remove_apartment(self) -> None:
        if self.__company is not None:
            houses = self.__company.get_houses()
            if houses:
                last_house = houses[-1]
                apartments = last_house.get_apartments()
                if apartments:
                    last_house.remove_apartment()
                    print("Последняя добавленная квартира удалена.")
                else:
                    print(
                        "В последнем добавленном доме нет добавленных квартир. "
                        "Удаление квартиры не выполнено."
                    )
            else:
                print(
                    "В выбранной компании нет добавленных домов. "
                    "Удаление квартиры не выполнено."
                )
        else:
            print("Компания не выбрана. Пожалуйста, выберите компанию.")

    def display_information(self) -> str:
        result = ""
        if self.__company is not None:
            result += f"Управляющая компания: {self.__company.get_name()}"
            for house in self.__company.get_houses():
                result += f"\n  Дом {house.get_house_number()}"
                for apartment in house.get_apartments():
                    result += (
                        f"\n    Квартира {apartment.get_apartment_number()}, "
                        f"Площадь: {apartment.get_area()}"
                    )
        else:
            result += "Компания не инициализирована."
        return result

    def save_to_file(self, filename: str) -> None:
        try:
            with open(filename, "w") as file:
                if self.__company:
                    file.write(f"{self.__company.get_name()}\n")

                    for house in self.__company.get_houses():
                        file.write(f"{house.get_house_number()}\n")

                        for apartment in house.get_apartments():
                            file.write(
                                f"{apartment.get_apartment_number()} "
                                f"{apartment.get_area()}\n"
                            )

                        file.write("\n")
                else:
                    print("Компания не выбрана. Структура не может быть сохранена.")
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")

    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, "r") as file:
                company_name = file.readline().strip()
                if not company_name:
                    print("Файл пустой. Нет данных для загрузки.")
                    return

                new_company = PropertyManagementCompany(company_name)

                while True:
                    house_number_str = file.readline().strip()
                    if not house_number_str:
                        break

                    house_number = int(house_number_str)
                    house = House(house_number)
                    new_company.add_house(house)

                    while True:
                        apartment_info = file.readline().strip()
                        if not apartment_info:
                            break

                        apartment_data = apartment_info.split()
                        apartment_number = int(apartment_data[0])
                        area = float(apartment_data[1])
                        apartment = Apartment(apartment_number, area)
                        house.add_apartment(apartment)

                    if not file.readline().strip():
                        break

                self.__companies.append(new_company)
                if not self.__head:
                    self.__head = new_company
                else:
                    current_company = self.__head
                    previous_company = None
                    while current_company and (
                            current_company.get_name() < new_company.get_name()
                    ):
                        previous_company = current_company
                        current_company = current_company.get_next_company()
                    if previous_company:
                        previous_company.set_next_company(new_company)
                        new_company.set_next_company(current_company)
                    else:
                        new_company.set_next_company(self.__head)
                        self.__head = new_company
                print(f"Структура загружена из файла {filename}.")
        except Exception as e:
            print(f"Ошибка при загрузке из файла: {e}")
