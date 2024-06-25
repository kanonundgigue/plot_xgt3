# data_loader.py
from abc import ABC, abstractmethod
import xgtool3 as xgt3

class DataLoader(ABC):
    @abstractmethod
    def load_data(self, filename):
        pass

class Gtool3DataLoader(DataLoader):
    def load_data(self, filename):
        file = xgt3.Gtool3(filename)
        data = file.open()
        return data
