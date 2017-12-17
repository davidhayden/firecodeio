# Firecode.io

[Firecode.io](https://www.firecode.io/) provides real-world coding challenges to help developers prepare for technical interviews. It supports C, C++, Java, and Python. Here are some solutions to those challenges.

## Installation

The best way to view the solutions is to clone the github repository.

### Step 1: Clone the Repository

```
$ git clone https://github.com/davidhayden/firecodeio.git
```

### Step 2: Run Python Doctests

Solutions created with Python should include *doctests*, and you can run these tests by simply running the scripts.

For example, if you want to run the doctests for a Fibonacci challenge, you can run them in a couple of ways.

```
$ python fib.py -v
```

or

```
$ python -m doctest fib.py -v
```

By default, doctests won't display anything for passing tests. The *-v* (verbose) option will allow you to see these results.

## Solutions

As with any challenge there are multiple solutions. I purposely like to solve the solutions using different algorithms regardless of whether the algorithm is naive or ideal.

### Fibonacci

For example, one of the first coding challenges was the classic naive recursive Fibonacci algorithm for finding the nth Fibonacci number in the sequence.

[fib.py](fib.py)

```py
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)
```

This gets really problematic for larger numbers, and many developers will recognize the issue of *overlapping sub-problems*. An alternative algorithm could use *memoization*.

[fib-memo.py](fib-memo.py)

```py
def fib(n):
    if n < 2:
        return n

    memo = [0, 1]

    for i in range(2, n):
        memo.append(memo[i-1] + memo[i - 2])

    return memo[n]
```

This sacrifices a bit of memory for performance. However, this can be futher improved using a simple loop, which reduces memory usage and solves overlapping sub-problems.

[fib-loop.py](fib-loop.py)

```py
def fib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b
 
    return a
```

The point is that there are many algorithms to solve these challenges, which makes algorithms so fascinating. We evaluate these algorithms based on time and space complexities, which is beyond the scope of this repository.

https://en.wikipedia.org/wiki/Big_O_notation

## License
This code is made available under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

## Credits
Created and maintained by David Hayden.
