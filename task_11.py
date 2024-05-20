class Dessert:

    def __init__(self, name=None, calories=1):
        self.__check_calories(calories)
        self.__check_name(name)

        self.__calories = calories
        self.__name = name

    @classmethod
    def __check_calories(cls, calories):
        if not isinstance(calories, int) or not calories >= 1:
            raise TypeError(
                'Нужно передать калории десерта в виде натурального числа.'
            )

    @classmethod
    def __check_name(cls, name):
        if not isinstance(name, str) and name is not None:
            raise TypeError('Нужно передать название десерта в виде строки.')

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__check_calories(calories)
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__check_name(name)
        self.__name = name

    def is_healthy(self):
        if 1 < self.__calories < 200:
            return True
        return False

    def is_delicious(self):
        return True
