from ruiseki import Ruseki


class Ruseki_control:

    def readRuiseki(self, csv_path, driver):
        ru = Ruseki()
        return ru.readRuseki(csv_path, driver)
