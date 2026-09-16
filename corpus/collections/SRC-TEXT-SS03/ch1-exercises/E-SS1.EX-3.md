---
schema: qual/card@1
id: E-SS1.EX-3
kind: problem
title: "SS 1.3: Solutions of z^n = omega and their count"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
3. With $\omega = s e ^ { i \varphi }$ , where $s \geq 0$ and $\varphi \in \mathbb { R }$ , solve the equation $z ^ { n } = \omega$ in C where n is a natural number.
   How many solutions are there?
:::

::: {.solution}
Let
\[
\omega=se^{i\varphi},\qquad s\ge0.
\]
If $s=0$, then $z^n=0$ has the unique solution $z=0$.

Assume $s>0$. Writing $z=re^{i\theta}$, the equation $z^n=\omega$ gives
\[
r^n=s,
\qquad
n\theta=\varphi+2\pi k
\]
for some $k\in\mathbb Z$. Hence
\[
z_k=s^{1/n}\exp\!\left(i\frac{\varphi+2\pi k}{n}\right),
\qquad k=0,1,\ldots,n-1.
\]
These $n$ values are distinct, since equality of $z_k$ and $z_\ell$ would imply $(k-\ell)/n\in\mathbb Z$, impossible for distinct $k,\ell\in\{0,\ldots,n-1\}$. Every integer $k$ is congruent modulo $n$ to one of these, so these are all solutions.

Thus there is one solution when $\omega=0$, and exactly $n$ solutions when $\omega\ne0$.
:::
