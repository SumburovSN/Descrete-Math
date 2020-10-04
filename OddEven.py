
class OddEven:

    def __init__(self, start, is_big=False):
        self.sequence = []
        if is_big:
            self.build_sequence2(start)
        else:
            self.build_sequence(start)

    @staticmethod
    def next_number(number):
        if number % 2 == 0:
            return int(number/2)
        else:
            return number*3 + 1

    def build_sequence(self, number):
        if number in self.sequence:  # base case
            self.sequence.append(number)
            return
        else:
            self.sequence.append(number)
            self.build_sequence(self.next_number(number))

    def build_sequence2(self, number):
        while number not in self.sequence:
            self.sequence.append(number)
            self.build_sequence(self.next_number(number))

    def save_in_file(self, file="OddEven.txt"):
        file = open(file, "w")
        file.write(str(self.sequence) + ";\n")
        file.close()


if __name__ == '__main__':

    max_length = [0, 0]
    for number in range(3, 1001):
        my_sequence = OddEven(number)
        my_sequence_length = len(my_sequence.sequence)
        if my_sequence_length > max_length[1]:
            max_length[0] = number
            max_length[1] = my_sequence_length
        my_sequence.save_in_file("positiveOddEven.txt")
        print(my_sequence.sequence)

    print(max_length)

    max_length = [0, 0]
    for number in range(-3, -1001, -1):
        my_sequence = OddEven(number)
        my_sequence_length = len(my_sequence.sequence)
        if my_sequence_length > max_length[1]:
            max_length[0] = number
            max_length[1] = my_sequence_length
        my_sequence.save_in_file("negativeOddEven.txt")
        print(my_sequence.sequence)

    print(max_length)

    my_sequence = OddEven(11111111111111111111111)
    print(my_sequence.sequence)
    print(len(my_sequence.sequence))

    # if input("Do you want to save output in file? (Y/y) :") in ("y", "Y"):
    #     my_sequence.save_in_file()

