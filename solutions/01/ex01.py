from dataclasses import dataclass

@dataclass
class NoDefault:
    fld_1: int

@dataclass
class WithDefault:
    # TODO: add the expected values as field defaults
    fld_1: int = 42
    fld_2: str = 'hello'

@dataclass
class WithMethod:
    fld_1: float = 1.41421356
    fld_2: float = 0.70710678

    # TODO: implement fld_sum() function
    def fld_sum(self):
        return self.fld_1 + self.fld_2
