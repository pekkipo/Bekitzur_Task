
class Calculator(object):

    def __init__(self, equation):
        self.equation = equation
        self.numbers_dict = {
            0: ' ', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'twenty',
            30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'
        }

    def solve_equation(self):
        return eval(self.equation)

    def show_answer(self):
        print(self.spell_number(self.solve_equation()))

    def spell_number(self, number):

            thousand = 1000
            million = thousand * 1000
            billion = million * 1000
            trillion = billion * 1000

            assert (0 <= number)

            if (number < 20):
                return self.numbers_dict[number]

            if (number < 100):
                if number % 10 == 0:
                    return self.numbers_dict[number]
                else:
                    return self.numbers_dict[number // 10 * 10] + self.numbers_dict[number % 10]

            if (number < thousand):
                if number % 100 == 0:
                    return self.numbers_dict[number // 100] + ' hundred'
                else:
                    return self.numbers_dict[number // 100] + ' hundred and ' + self.spell_number(number % 100)

            if (number < million):
                if number % thousand == 0:
                    return self.spell_number(number // thousand) + ' thousand'
                else:
                    return self.spell_number(number // thousand) + ' thousand ' + self.spell_number(number % thousand)

            if (number < billion):
                if (number % million) == 0:
                    return self.spell_number(number // million) + ' million'
                else:
                    return self.spell_number(number // million) + ' million ' + self.spell_number(number % million)

            if (number < trillion):
                if (number % billion) == 0:
                    return self.spell_number(number // million) + ' billion'
                else:
                    return self.spell_number(number // million) + ' billion ' + self.spell_number(number % billion)

            if (number % trillion == 0):
                return self.spell_number(number // trillion) + ' trillion'
            else:
                return self.spell_number(number // trillion) + ' trillion ' + self.spell_number(number % trillion)

            raise AssertionError('Number is larger than a trillion: %s' % str(number))


