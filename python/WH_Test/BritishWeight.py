"""
@author: Matthias Stadlinger
@klasse: 5CN
"""
class BritishWeight:
    """Testcases
    >>> b1 = BritishWeight(13)
    >>> b2 = BritishWeight(16)
    >>> print(b1)
    13 lb
    >>> print(b2)
    1 st 2 lb
    >>> b3 = b1 + b2
    >>> print(b3)
    2 st 1 lb
    >>> b4 = BritishWeight(14)
    >>> print(b4)
    1 st 0 lb
    """

    def __init__(self, pounds: int, stones: int = 0):
        """
        Konstruktor
        :param pounds:
        :param stones:
        """
        self.pound = pounds + stones * 14

    def __str__(self) -> str:
        """
        To String
        :return: Pfund in Pfund oder Stone und Pfund
        """
        if self.pound // 14 == 0:
            return str(self.pound) + " lb"
        else:
            return str(self.pound // 14) + " st " + str(self.pound % 14) + " lb"

    def __add__(self, other: 'BritishWeight') -> 'BritishWeight':
        """
        Addition

        :param other: anderes Gewicht
        :return: Summe der Gewichte
        """
        return BritishWeight(self.pound + other.pound)
