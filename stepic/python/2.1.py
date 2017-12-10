class NonPositiveError(ValueError):
    pass

class PositiveList(list):
    def append(self, object):
        if object > 0:
            super().append(object)
        else:
            raise NonPositiveError


list = PositiveList()
list.append(1)

print(list)

list.append(-1)
