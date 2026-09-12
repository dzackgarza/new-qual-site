---
schema: qual/card@1
id: P-BKS07-1B
kind: problem
title: UC Berkeley Spring 2007 prelim 1B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
If $c \in \mathbb { R }$ , say that a real-valued function $f : \mathbb { R } \to \mathbb { R }$ is periodic with period c if it satisfies $f ( x + c ) = f ( x )$ for all $x \in \mathbb { R }$ •

(i) Let V be the set of continuous real-valued functions f having a positive integer as a period.
Prove that V is a vector space.

(ii) Let $p _ { 1 } < p _ { 2 } < . . . < p _ { n } < . . .$ . be the sequence of prime numbers, and for each i, let $f _ { i }$ be a function whose minimal positive period is $p _ { i }$ . Prove that the functions $f _ { 1 } , f _ { 2 } , \ldots$ . are linearly independent in V .
:::

::: {.solution}
(i) The set of all functions $\mathbb { R } \to \mathbb { R }$ is a vector space, so it suffices to check that V contains 0 and is closed under addition and scalar multiplication.
The only nontrivial claim is closure under addition.
Suppose $f , g \in V$ , say with periods c and d. Any positive integer multiple of a period is a period of the same function, so $f , g$ have cd as a common period.
Thus $f + g$ has cd as a period (and it is continuous).

(ii) Suppose not.
Then there exists a relation

$$
a _ { 1 } f _ { 1 } + \cdots + a _ { n } f _ { n } = 0
$$

where $a _ { i } \in \mathbb { R }$ and $a _ { n } \neq 0$ Solving for $f _ { n }$ shows that $f _ { n }$ has $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ as a period.
It also has $p _ { n }$ as a period.
Now $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ and $p _ { n }$ are relatively prime, so 1 is an integer combination of $p _ { 1 } p _ { 2 } \cdots p _ { n - 1 }$ and $p _ { n }$ . Any integer combination of periods is a period, so in particular 1 is also a period of $f _ { n }$ . This contradicts the hypothesis that $p _ { n }$ is the minimal period of $f _ { n }$
:::
