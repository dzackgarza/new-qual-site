---
schema: qual/card@1
id: E-SS5.EX-14
kind: problem
title: "Deduce from Hadamard’s theorem that if  is entire and of growth order  that is n"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
14. Deduce from Hadamard’s theorem that if $F$ is entire and of growth order $\rho$ that is non-integral, then F has infinitely many zeros.
:::

::: solution
Suppose, toward a contradiction, that the entire function $F$ has only finitely many zeros. Hadamard's factorization theorem then reduces to
\[
F(z)=e^{P(z)}Q(z),
\]
where $P$ and $Q$ are polynomials and $Q$ records the finitely many zeros of $F$.

If $P$ is constant, then $F$ is a polynomial and therefore has growth order $0$.

If $P$ has degree $d\ge1$, then $F$ has growth order exactly $d$. Indeed, the upper bound
\[
|F(z)|\le A e^{B|z|^d}
\]
is immediate from polynomial growth of $P$ and $Q$. Conversely, write the leading term of $P$ as $cz^d$, $c\ne0$, and choose an angle $\theta$ so that $ce^{id\theta}=|c|$. Along $z=re^{i\theta}$,
\[
\Re P(z)=|c|r^d+O(r^{d-1}),
\]
while $\log|Q(z)|=O(\log r)$ away from the finitely many zeros of $Q$. Hence
\[
\log|F(re^{i\theta})|=|c|r^d+O(r^{d-1}),
\]
which rules out every growth-order bound with exponent $<d$.

Thus an entire function with only finitely many zeros has growth order either $0$ or a positive integer. Since the given order $\rho$ is non-integral, this is impossible. Therefore $F$ has infinitely many zeros.
:::
