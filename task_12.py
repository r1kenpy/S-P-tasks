class JellyBean:

    def __init__(self, flavor):
        self.__check_flavor(flavor)
        self.__flavor = flavor

    @classmethod
    def __check_flavor(cls, flavor):
        if not isinstance(flavor, str) and flavor is not None:
            raise TypeError('Нужно передать вкус дисерта в виде строки.')

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__check_flavor(flavor)
        self.__flavor = flavor


class Dessert(JellyBean):

    def __init__(self, name=None, calories=1, flavor=None):
        super().__init__(flavor)
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
        return 1 < self.__calories < 200

    def is_delicious(self):
        return not self.flavor == 'black licorice'
