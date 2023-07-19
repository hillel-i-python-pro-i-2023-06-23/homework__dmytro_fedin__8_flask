import pandas as pd

from application.services.csv_handler import read_csv_content


class CsvProcessor:
    def __init__(self):
        self.data_frame = None

    def get_data_frame(self):
        self.data_frame = read_csv_content()

    @staticmethod
    def get_mean(data_frame: pd.DataFrame) -> float:
        mean_value = data_frame.mean()

        return mean_value

    @staticmethod
    def get_cm_from_inches(value: float) -> float:
        cm = value * 2.54

        return cm

    @staticmethod
    def get_kg_from_pounds(value: float) -> float:
        kg = value * 0.453592
        return kg

    def get_mean_height(self) -> float:
        mean_height = self.get_mean(self.data_frame["Height(Inches)"])
        cm = self.get_cm_from_inches(mean_height)

        return cm

    def get_mean_weight(self) -> float:
        mean_weight = self.get_mean(self.data_frame["Weight(Pounds)"])
        kg = self.get_kg_from_pounds(mean_weight)

        return kg

    def print_csv_data(self) -> None:
        self.get_data_frame()

        height = self.get_mean_height()
        weight = self.get_mean_weight()
        print(
            f'Mean height is {"%.1f" % height} cm. Mean weight is {"%.1f" % weight} kg.'
        )
