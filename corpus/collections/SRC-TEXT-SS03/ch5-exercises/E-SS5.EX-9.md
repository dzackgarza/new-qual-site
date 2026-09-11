---
schema: qual/card@1
id: E-SS5.EX-9
kind: problem
title: "SS 5.9: A binary product expansion of 1/(1-z)"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
9. Prove that if $| z | < 1$ , then

$$
(1 + z) (1 + z ^ {2}) (1 + z ^ {4}) (1 + z ^ {8}) \dots = \prod_ {k = 0} ^ {\infty} (1 + z ^ {2 ^ {k}}) = \frac {1}{1 - z}.
$$
:::

::: solution
For every $N\ge0$, repeated use of
\[
1-w^2=(1-w)(1+w)
\]
gives the finite identity
\[
(1-z)\prod_{k=0}^{N}(1+z^{2^k})
=1-z^{2^{N+1}}.
\tag{1}
\]
Indeed, each factorization successively replaces $1-z^{2^j}$ by
\[
(1-z^{2^{j-1}})(1+z^{2^{j-1}}).
\]
If $|z|<1$, then
\[
z^{2^{N+1}}\longrightarrow0.
\]
Since $1-z\ne0$, taking $N\to\infty$ in (1) gives
\[
\boxed{
\prod_{k=0}^{\infty}(1+z^{2^k})=\frac1{1-z}}.
\]
Thus the product converges and has the stated value throughout the open unit disc.
:::
