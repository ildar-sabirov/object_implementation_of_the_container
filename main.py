from dialog import Dialog

def print_menu():
    print("\nВыберите действие:")
    print("0. Выбрать компанию")
    print("1. Добавить компанию")
    print("2. Добавить дом")
    print("3. Удалить дом")
    print("4. Добавить квартиру")
    print("5. Удалить квартиру")
    print("6. Вывести информацию")
    print("7. Сохранить структуру в файл")
    print("8. Загрузить структуру из файла")
    print("9. Вывести список компаний")
    print("10. Выйти")


def main():
    dialog_instance = Dialog()

    while True:
        print_menu()
        choice = input("Введите номер действия: ")

        if choice == "10":
            print("Программа завершена.")
            break
        elif choice == "0":
            dialog_instance.choose_or_create_company()
        elif choice == "1":
            company_name = input("Введите название компании: ")
            dialog_instance.create_company(company_name)
        elif choice == "2":
            house_number = int(input("Введите номер дома: "))
            dialog_instance.add_house(house_number)
        elif choice == "3":
            dialog_instance.remove_house()
        elif choice == "4":
            house_number = int(input("Введите номер дома для добавления квартиры: "))
            apartment_number = int(input("Введите номер квартиры: "))
            area = float(input("Введите площадь квартиры: "))
            dialog_instance.add_apartment(house_number, apartment_number, area)
        elif choice == "5":
            dialog_instance.remove_apartment()
        elif choice == "6":
            print(dialog_instance.display_information())
        elif choice == "7":
            filename = input("Введите имя файла для сохранения: ")
            dialog_instance.save_to_file(filename)
        elif choice == "8":
            filename = input("Введите имя файла для загрузки: ")
            dialog_instance.load_from_file(filename)
        elif choice == "9":
            print("Список компаний:")
            dialog_instance.print_companies()
        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
