---
schema: qual/card@1
id: E-SS7.EX-4
kind: exercise
title: "Dirichlet L-series for periodic coefficients"
classification:
  areas:
  - complex-analysis
  topics: ['Zeta Function', 'Prime Number Theorem', 'Dirichlet Series']
relations: []
review: draft
---

::: exercise
4. Suppose $\{ a _ { n } \} _ { n = 1 } ^ { \infty }$ is a sequence of complex numbers such that $a _ { n } = a _ { m }$ if $n \equiv m$ mod $q$ for some positive integer $q .$ Define the Dirichlet L-series associated to $\left\{ a _ { n } \right\}$ by

$$

L (s) = \sum_ {n = 1} ^ {\infty} \frac {a _ {n}}{n ^ {s}} \quad \mathrm{for} \operatorname{Re} (s) > 1.

$$

Also, with $a _ { 0 } = a _ { q }$ , let

$$

Q (x) = \sum_ {m = 0} ^ {q - 1} a _ {q - m} e ^ {m x}.

$$

Show, as in Exercises 15 and 16 of the previous chapter, that

$$

L (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {\infty} \frac {Q (x) x ^ {s - 1}}{e ^ {q x} - 1} d x, \quad \mathrm{for} \operatorname{Re} (s) > 1.

$$

Prove as a result that $L ( s )$ is continuable into the complex plane, with the only possible singularity a pole at $s = 1$ . In fact, $L ( s )$ is regular at $s = 1$ if and only if $\textstyle \sum _ { m = 0 } ^ { q - 1 } a _ { m } = 0$ . Note the connection with the Dirichlet $L ( s , \chi )$ series, taken up in Book I, Chapter 8, and that as a consequence, $L ( s , \chi )$ is regular at $s = 1$ if and only if $\chi$ is a non-trivial character.
:::
