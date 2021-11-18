import argparse

parser = argparse.ArgumentParser();
parser.add_argument("--first", default="Admin", help='First Name')
 parser.add_argument("--last", default="Admin", help='Last Name')
parser.add_argument("-p", "--pay", default=1000, dest='EPAY', metavar='PAY', type=int, help='Payment')
    parser.add_argument("--secret", help=argparse.SUPPRESS)

mgrp = parser.add_mutually_exclusive_group()
mgrp.add_argument('--xml', action='store_true', help="Get xml data")
mgrp.add_argument('--html', action='store_true', help="Get html data")
mgrp.add_argument('--yaml', action='store_true', help="Get yaml data")
mgrp.add_argument('--json', action='store_true', help="Get json data")

 args = parser.parse_args()


# args.first, args.last, args.pay


class Employee:
    """A sample Employee class."""

    raise_amt = 1.05

     def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        print(self.__dict__)

     @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


@property
def fullname(self):
    return '{} {}'.format(self.first, self.last)

def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)


def monthly_schedule(self, month):
    # response = requests.get(f'http://company.com/{self.last}/{month}')
    # if response.ok:
    #     return response.text
    # else:
    #     return 'Bad Response!'
    pass

# --- end of class definition ---

 if __name__ == "__main__":
    first, last, pay = args.first, args.last, args.EPAY
    emp = Employee(first, last, pay)
