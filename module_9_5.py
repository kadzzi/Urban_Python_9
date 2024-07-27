class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        elif (stop - start > 0 > step) or (stop - start < 0 < step):
            raise StepValueError('Шаг направлен за пределы диапазона!')
        else:
            self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        value_to_return = self.pointer
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step

        else:
            if self.pointer < self.stop:
                raise StopIteration()
            else:
                self.pointer += self.step

        return value_to_return


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as ext:
    print(ext.message)

try:
    iter2 = Iterator(10, 1)
    for i in iter2:
        print(i, end=' ')
    print()
except StepValueError as ext:
    print(ext.message)

iter3 = Iterator(-5, 1)
iter4 = Iterator(6, 15, 2)
iter5 = Iterator(5, 1, -1)


for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
