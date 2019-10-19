# Expected Coin Tosses

Calculates expected number of coin tosses to get a particular pattern (provided as input).

## Motivation

One would usually expect that on average it would require same number of tosses to get HHT or HTH. But it turns out that it is not so.
HHT requires 8 tosses and HTH required 10 tosses on average.
So I wanted to check what do other numbers turn out to be? Can I spot a pattern?
Since it was a tedious job to setup a Markov Chain each time and calculate expectations by hand, I decided to write a program instead.

## Working

We setup a NFA which accepts only those strings which end with the provided pattern. Convert it to a DFA using minimal subset construction. And then looking at this DFA as a directed graph we obtain our desired Markov Chain.
Calculating the absorption probability in the Markov chain so obtained, yields the required answer.

## Installation

```
$ pip3 install automata-lib
```

## Usage

```
$ python3 toss.py
$ pattern=HHT
$ 8.0
```


## Related Links

https://math.stackexchange.com/questions/3389508/building-expectations-recursively
https://math.stackexchange.com/questions/816140/why-is-the-expected-number-coin-tosses-to-get-hth-is-10
https://math.stackexchange.com/questions/1862489/markov-chain-average-waiting-time
https://www.reddit.com/r/math/comments/43toen/til_when_flipping_a_fair_coin_until_either_hht_or/
