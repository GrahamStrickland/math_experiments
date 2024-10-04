#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Data:
    string_data: str
    numeric_data: float


class DataStructure:
    data: Data

    def __init__(self, data: Data) -> None:
        self.data = data

    def print_data(self) -> None:
        print(self.data)


def main() -> None:
    print("-" * 84)
    print("Initial data:")
    print("-" * 84)
    data = Data(string_data="something", numeric_data=1.23456789)
    data_structure = DataStructure(data)

    print("data = ", end="")
    print(data)
    print("data_structure.data = ", end="")
    data_structure.print_data()

    print("-" * 84)
    print("Changing data...")
    print("-" * 84)

    data.string_data = "nothing"
    data.numeric_data = 9.87654321

    print("-" * 84)
    print("After changing data:")
    print("-" * 84)
    print("data_structure.data = ", end="")
    data_structure.print_data()
    print("data = ", end="")
    print(data)
    print("-" * 84)


if __name__ == "__main__":
    main()
