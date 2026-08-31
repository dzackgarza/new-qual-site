---
schema: qual/card@1
id: E-SS4.EX-11
kind: exercise
title: "One can give a neater formulation of the result in Exercise 10 by proving the fo"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
---

::: exercise
11. One can give a neater formulation of the result in Exercise 10 by proving the following fact.

Suppose $f ( z )$ is an entire function of strict order 2, that is,

$$
f (z) = O (e ^ {c _ {1} | z | ^ {2}})
$$

for some $c _ { 1 } > 0$ . Suppose also that for x real,

$$
f (x) = O (e ^ {- c _ {2} | x | ^ {2}})
$$

for some $c _ { 2 } > 0$ . Then

$$
| f (x + i y) | = O (e ^ {- a x ^ {2} + b y ^ {2}})
$$

for some $a , b > 0$ . The converse holds: if $|f(x+iy)| = O(e^{-ax^2 + by^2})$ for some $a, b > 0$, then restricting to the real axis ($y = 0$) gives $f(x) = O(e^{-ax^2})$, which is the second hypothesis with $c_2 = a$; and the whole-plane bound $f(z) = O(e^{c_1|z|^2})$ follows with $c_1 = b$, since $-ax^2 + by^2 \le b(x^2 + y^2) = b|z|^2$.
:::
