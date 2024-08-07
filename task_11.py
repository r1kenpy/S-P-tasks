class Dessert:

    def __init__(self, name=None, calories=1):
        self.__calories = calories
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def is_healthy(self):
        return (
            isinstance(self.__calories, (int, float))
            and 1 < self.__calories < 200
        )

    def is_delicious(self):
        return True
