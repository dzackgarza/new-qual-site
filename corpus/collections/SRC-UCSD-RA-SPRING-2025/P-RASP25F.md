---
schema: qual/card@1
id: P-RASP25F
kind: problem
title: "Weak convergence of bounded sequences with asymptotically orthogonal inner products"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(\xi_m)_{m \geq 1}$ be a sequence of vectors in a Hilbert space $H$.
Assume that $\|\xi_m\| \leq 1$ and $\lim_{n \to \infty} \langle \xi_n, \xi_m \rangle = 0$ for every $m \geq 1$.
Prove that $\lim_{n \to \infty} \langle \xi_n, \xi \rangle = 0$ for every $\xi \in H$.
:::


::: solution
<1>1. Prove convergence on the closed span of the sequence.
::: proof
Let
\[
M:=\overline{\operatorname{span}}\{\xi_m:m\ge1\}.
\]
By hypothesis,
\[
\langle \xi_n,\xi_m\rangle\longrightarrow0
\]
for every fixed $m$. By linearity, the same is true for every finite linear combination $\eta$ of the $\xi_m$:
\[
\langle \xi_n,\eta\rangle\longrightarrow0.
\]

Now fix $\xi\in M$ and $\varepsilon>0$. Choose such a finite linear combination $\eta$ with
\[
\|\xi-\eta\|<\varepsilon.
\]
Using $\|\xi_n\|\le1$,
\[
|\langle \xi_n,\xi\rangle|
\le |\langle \xi_n,\eta\rangle|+\|\xi_n\|\,\|\xi-\eta\|
\le |\langle \xi_n,\eta\rangle|+\varepsilon.
\]
Taking $n\to\infty$ gives
\[
\limsup_{n\to\infty}|\langle \xi_n,\xi\rangle|\le\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\langle \xi_n,\xi\rangle\longrightarrow0
\]
for every $\xi\in M$.
:::

<1>2. Extend the conclusion to all of $H$.
::: proof
Every $\xi\in H$ has an orthogonal decomposition
\[
\xi=\xi_M+\xi_\perp,
\qquad
\xi_M\in M,
\quad
\xi_\perp\in M^\perp.
\]
Since every $\xi_n\in M$,
\[
\langle \xi_n,\xi_\perp\rangle=0.
\]
Therefore
\[
\langle \xi_n,\xi\rangle
=\langle \xi_n,\xi_M\rangle
\longrightarrow0
\]
by Step 1. Hence
\[
\boxed{\xi_n\rightharpoonup0\text{ in }H.}
\]
:::
:::
