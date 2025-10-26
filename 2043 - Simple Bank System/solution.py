class Bank:
    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        idx1, idx2 = account1 - 1, account2 - 1
        if self.balance[idx1] >= money:
            self.balance[idx1] -= money
            self.balance[idx2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (1 <= account <= self.n):
            return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False