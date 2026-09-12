---
schema: qual/card@1
id: P-BKS03-8B
kind: problem
title: Counting cube roots of $1$ modulo $30030$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $N=30030$, the product of the first six primes.
How many integers $0\le x<N$ satisfy
\[
N\mid x^3-1?
\]
:::

::: {.solution}
We want the number of solutions to $x ^ { 3 } = 1$ in the ring $\mathbb { Z } / N \mathbb { Z }$ . By the Chinese Remainder Theorem, $\mathbb { Z } / N \mathbb { Z }$ is isomorphic as a ring to $\begin{array} { r } { \prod _ { p \in \{ 2 , 3 , 5 , 7 , 1 1 , 1 3 \} } \mathbb { Z } / p \mathbb { Z } } \end{array}$ . Thus the answer is $\begin{array} { r } { \prod _ { p \in \{ 2 , 3 , 5 , 7 , 1 1 , 1 3 \} } n _ { p } } \end{array}$ , where $n _ { p }$ is the number of solutions to $x ^ { 3 } - 1$ in $\mathbb { Z } / p \mathbb { Z }$ . Now $n _ { p }$ is the number of elements of order dividing 3 in the multiplicative group $( \mathbb { Z } / p \mathbb { Z } ) ^ { \ast }$ . Since $( \mathbb { Z } / p \mathbb { Z } ) ^ { \ast }$ is cyclic of order $p - 1$ , we have $n _ { p } = 3$ if 3 divides $p - 1$ , and $n _ { p } = 1$ otherwise.
Thus the answer is

$$
n _ { 2 } n _ { 3 } n _ { 5 } n _ { 7 } n _ { 1 1 } n _ { 1 3 } = 1 \cdot 1 \cdot 1 \cdot 3 \cdot 1 \cdot 3 = 9 .
$$
:::
