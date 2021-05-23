from base_validator import Validator


class StupidValidator(Validator):
    def validate(self, data) -> bool:
        return True
