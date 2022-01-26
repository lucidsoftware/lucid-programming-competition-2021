# Pyramid Profits

You've been hired by an enthusiastic entrepreneur named Jude.

Using the profits from some early investments in certain meme-related cryptocurrencies,
Jude recently founded a company that sells high-fashion cryptocurrency-related accessories
and meme-inspired personal care products. Particularly popular are the company's awkward side-glance monkey sunglasses
as well as a "custom-engineered" solid-titanium crypto wallet (okay, it is really just some low-grade flash memory wrapped in recycled aluminum,
but who is going to know?).

Tired of the day-to-day hustle of managing and fulfilling individual sales, Jude hires some
internet strangers to actually deal with the business of finding customers and selling to them.
For every sale made, the salesperson will get a percentage commission of the sale and Jude will keep the rest.
However, many of the internet strangers that Jude hired quickly realize that they can also hire yet more
internet strangers to work for _them_ in exchange for splitting their portion of the profits.
This pattern continues, forming a deep network of internet strangers working for other internet strangers,
each of them selling Jude's products.

No matter who makes the sale, a contract is a contract.
If a salesperson negotiates that they will keep 10% of the profit and give their boss 90% for every sale made,
they owe their immediate boss the 90% regardless of whether they personally made the sale or whether someone working below them made the sale.

For example, suppose that Jude hires Ian and agrees that Ian can keep 40% of the profit from any sale made by Ian or someone working (directly or indirectly) for Ian.
Then, Ian hires Kathy and agrees that Kathy can keep 20% of Ian's portion of the profit for any sale made by Kathy or someone working (directly or indirectly) for Kathy.
If Kathy makes a sale worth $1000, _she does not keep 20% of the $1000_.
The bosses are always paid first, starting from the top.
This means that Jude keeps 60% ($600) of the $1000 sale.
The remaining 40% ($400) would be passed to Ian, who keeps 80% of the 40% ($320) for himself and passes the remaining 20% of the 40% ($80) to Kathy.

You are only entitled to profits resulting from a sales made by you or someone working for you.
For instance, if Ian makes a sale worth $2000, then Jude would keep 60% ($1200) and pass the remaining 40% ($800) to Ian.
Ian keeps 100% of the $800 and passes nothing ($0) to Kathy, because Kathy (or someone working for Kathy) did not have any part in the sale.
Kathy will **not** receive payouts from every sale made by Ian.
Kathy will only receive payouts for sales in which she (or someone working below her) made the sale.

Using the power of crypto contracts, no one is able to cheat their contract and keep more than their agreed upon portion.

Given the complete network of salespeople and a list of sales for the day, compute how much everyone earns for the day.
You should round the final profit for each salesperson to the nearest whole number.

## Input
As input, you will receive the following:

* The number of salespeople in the network, not including Jude.
* For each salesperson, their name followed by the name of their immediate boss in the network, followed by the integer percentage of **their immediate boss's profits** they are allowed to keep.
* The number of sales made for the day
* For each sale, the name of the salesperson that made the sale and the total profit in that sale

The input will be formatted as follows:
```
<number of salespeople>
<salesperson> <direct boss> <percentage of boss's profit>
<salesperson> <direct boss> <percentage of boss's profit>
<salesperson> <direct boss> <percentage of boss's profit>
...
<number of sales>
<salesperson> <profit>
<salesperson> <profit>
<salesperson> <profit>
...
```

## Output
Output each salesperson's total earnings for the day, rounded to the nearest whole number.
For each salesperson, include earnings from all sales made directly by them or indirectly by someone working below them.
You should include all salespeople in your output, including those that earned nothing.
Your output list should be alphabetized by name.
Make sure to include Jude in the list.

```
<salesperson> <earnings>
<salesperson> <earnings>
...
```

## Constraints
* Each salesperson has _exactly_ one boss in the network.
* A saleperson may hire additional salepeople to work under them, but is not required to do so.
* The profit from a single sale will always be a positive integer less than 2,147,483,647.
* Jude does not have a boss and will thus always be at the top of the network.
* The name of each salesperson is unique and composed of alphanumeric characters.

## Examples

### Input 0
```
2
Ian Jude 50
Kathy Ian 10
2
Kathy 1000
Ian 2500
```

### Output 0
```
Ian 1700
Jude 1750
Kathy 50
```

### Input 1
```
3
Yvonne Arthur 20
Jamal Arthur 50
Arthur Jude 30
4
Yvonne 12000
Jamal 8000
Jude 4150
Arthur 500
```

### Output 1
```

```
