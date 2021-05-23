from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, data) -> bool:
        pass
