
class StringComparisonError(Exception):
    pass


class StringComparison:

    @staticmethod
    def compare(a, b):
        try:
            return a.lower() == b.lower()
        except ValueError:
            raise StringComparisonError("Name Does Not Match")

    @staticmethod
    def adder(a, b):
        try:
            return float(a) + float(b)
        except ValueError:
            raise StringComparisonError("Name Does Not Match")


def _test():
    sc = StringComparison()
    print(sc.compare("Mike", "Mike"))
    print(sc.adder(4, 5))


if __name__ == '__main__':
    _test()