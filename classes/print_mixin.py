class PrintMixin:

    def __repr__(self):

        val = []

        for i in self.__dict__.values():
            val.append(i)
        return f'{self.__class__.__name__}{val}'
