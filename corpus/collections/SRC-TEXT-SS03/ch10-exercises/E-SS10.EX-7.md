---
schema: qual/card@1
id: E-SS10.EX-7
kind: problem
title: "SS 10.7: Triangular and septagonal number identities via the theta function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
7. Use the product formula for $\Theta$ to prove:

(a) The “triangular number” identity

$$
\prod_ {n = 0} ^ {\infty} (1 + x ^ {n}) (1 - x ^ {2 n + 2}) = \sum_ {n = - \infty} ^ {\infty} x ^ {n (n + 1) / 2},
$$

which holds for $| x | < 1$

(b) The “septagonal number” identity

$$
\prod_ {n = 0} ^ {\infty} (1 - x ^ {5 n + 1}) (1 - x ^ {5 n + 4}) (1 - x ^ {5 n + 5}) = \sum_ {n = - \infty} ^ {\infty} (- 1) ^ {n} x ^ {n (5 n + 3) / 2},
$$

which holds for $| x | < 1$
:::

::: solution
We use the Jacobi triple product in the form
\[
\sum_{n\in\mathbb Z}z^n q^{n(n+1)/2}
=\prod_{m=1}^\infty(1-q^m)(1+zq^m)(1+z^{-1}q^{m-1}),
\qquad |q|<1.
\tag{1}
\]

For part (a), set \(z=1\) and \(q=x\). Then
\[
\sum_{n\in\mathbb Z}x^{n(n+1)/2}
=\prod_{m=1}^\infty(1-x^m)(1+x^m)(1+x^{m-1}).
\]
Since \((1-x^m)(1+x^m)=1-x^{2m}\), this is
\[
\prod_{n=0}^\infty(1+x^n)(1-x^{2n+2}),
\]
which proves the triangular-number identity.

For part (b), in (1) take
\[
q=x^5,
\qquad z=-x^{-1}.
\]
The series side becomes
\[
\sum_{n\in\mathbb Z}(-1)^n
x^{-n}x^{5n(n+1)/2}
=\sum_{n\in\mathbb Z}(-1)^n x^{n(5n+3)/2}.
\]
The product side is
\[
\prod_{m=1}^\infty
(1-x^{5m})(1-x^{5m-1})(1-x^{5m-4}).
\]
Putting \(n=m-1\) in the last two factors rewrites this as
\[
\prod_{n=0}^\infty
(1-x^{5n+1})(1-x^{5n+4})(1-x^{5n+5}),
\]
which is the septagonal-number identity.
:::
