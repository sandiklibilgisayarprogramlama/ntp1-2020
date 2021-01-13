class Okul:

    def __init__(self,x) :
        self._x=x

    def get_x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._x

    def set_x(self,yeni_x):
        """[summary]

        Args:
            yeni_x ([type]): [description]
        """
        self._x=yeni_x

    x=property(get_x,set_x)