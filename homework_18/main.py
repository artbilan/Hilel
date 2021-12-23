from female import Female
from male import Male


if __name__ == "__main__":
    marina = Female("female", "white")
    print(marina.do_talk())

    lisa = Female
    print(lisa.do_work(Female))

    john = Male
    print(john.do_work(Male))






