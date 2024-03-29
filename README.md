# Объектная реализация контейнера на основе комбинированной структуры

Дисциплина: «Структуры и алгоритмы обработки данных»

## Цель работы: 

Получение навыков разработки объектных программ, включая создание набора собственных взаимосвязанных классов для объектной реализации специализированного контейнера. Контейнер предназначен для хранения и обработки данных некоторой информационной задачи. Контейнер представляет собой двухуровневую структуру данных, в которой уровни реализуются разными способами – один статически на базе массива (непрерывная реализация), другой – динамически с использованием адресных связей (связная реализация).

## Требования:

- Полная объектная реализация с определением классов для всех элементов реализуемой структуры: информационные объекты (обязательно!), объекты-элементы списка (динамическая реализация), объекты-списки, объект-контейнер
- Имена классов, свойств и методов должны носить содержательный смысл и соответствовать информационной задаче
- Соблюдение принципа инкапсуляции – использование в классах только закрытых свойств и реализация необходимого набора методов доступа
- Реализация в классах всех необходимых методов: конструкторы, методы доступа к свойствам, методы добавления и удаления на каждом из двух уровней, метод поиска (при необходимости)
- Возможность сохранения всей структуры во внешнем файле с обратной загрузкой

## Вариант реализации контейнера:

Объектная реализация контейнера на основе комбинированной структуры «Динамический упорядоченный список массивов-стеков»

## Варианты информационного наполнения контейнера:

Задача «Квартирный фонд»  
  - информационные объекты: квартиры жилого дома (свойства: НомерКвартиры, Площадь)
  - квартиры объединяются в рамках объекта Дом (свойство: НомерДома)
  - дома объединяются в рамках объекта-контейнера УправляющаяКомпания (свойство – Название)

## Ожидаемый результат:
	
С помощью диалога с пользователем программа должна создавать контейнер, изменять его, сохранять этот контейнер и загружать контейнер из внешнего файла.

## Запуск диалогового окна:
  ```
  python main.py
  ```

