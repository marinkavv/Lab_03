import threading
import time


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()


class TransferOperation:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def run(self):

        accounts = sorted([self.from_account, self.to_account], key=id)

        lock1 = accounts[0].lock
        lock2 = accounts[1].lock

        with lock1:
            time.sleep(0.01)

            with lock2:
                self.from_account.balance -= self.amount
                self.to_account.balance += self.amount

                print(
                    f"Transfer from {self.from_account.name} "
                    f"to {self.to_account.name} successful."
                )


def main():

    account1 = Account("Alice", 100)
    account2 = Account("Bob", 200)

    op1 = TransferOperation(account1, account2, 50)
    op2 = TransferOperation(account2, account1, 30)

    t1 = threading.Thread(target=op1.run)
    t2 = threading.Thread(target=op2.run)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"\nКінцевий баланс Alice: {account1.balance}")
    print(f"Кінцевий баланс Bob: {account2.balance}")


if __name__ == "__main__":
    main()
