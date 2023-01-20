# integers are not iterables
user = ['mike', 'han', 'fred', 'ken', 'linda', 'sam', 'stev', 'matty']
loop1 = iter(user)
while True:
    try:
        user = next(loop1)
        print(user)
    except StopIteration:
        break


class portfolio:
    def __init__(self):
        self.holdings = {}

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = portfolio()
p.buy('alpha', 200)
p.buy('linda', 800)
p.sell('jon', 200)
p.sell('geth', 230)
for (ticker, shares) in p:
    print(ticker, shares)
import itertools

ranks = list(range(2, 11)) + ['J', 'K', 'Q', 'A']
ranks = [str(rank) for rank in ranks]
print(ranks)
