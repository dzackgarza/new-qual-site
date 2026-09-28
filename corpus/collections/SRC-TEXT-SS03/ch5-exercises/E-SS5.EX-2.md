---
schema: qual/card@1
id: E-SS5.EX-2
kind: problem
title: "SS 5.2: Orders of growth of standard entire functions"
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

::: {.exercise}
2. Find the order of growth of the following entire functions:

(a) $p ( z )$ where p is a polynomial.

(b) $e ^ { b z ^ { n } }$ for $b \neq 0$

(c) $e ^ { e ^ { z } }$
:::

::: {.solution}
Recall that the order of an entire function $f$ is the infimum of the positive numbers $\rho$ for which
\[
|f(z)|\le A e^{B|z|^\rho}
\]
for suitable $A,B>0$.

For (a), every polynomial has order $0$. Indeed, if $p$ has degree $m$, then $|p(z)|=O(|z|^m)$, and for every $\rho>0$ one has
\[
|z|^m\le C_\rho e^{|z|^\rho}
\]
for all $z$. Thus the infimum of admissible positive $\rho$ is $0$.

For (b),
\[
|e^{bz^n}|=e^{\Re(bz^n)}\le e^{|b||z|^n},
\]
so the order is at most $n$. Choose $\theta$ so that
\[
b e^{in\theta}=|b|.
\]
Then along $z=re^{i\theta}$,
\[
|e^{bz^n}|=e^{|b|r^n}.
\]
No bound $Ae^{Br^\rho}$ with $\rho<n$ can dominate this as $r\to\infty$. Hence the order is exactly
\[
\boxed n.
\]

For (c), along the positive real axis,
\[
|e^{e^x}|=e^{e^x}.
\]
If this function had finite order $\rho$, then for suitable $A,B>0$ we would have
\[
e^{e^x}\le A e^{Bx^\rho}
\]
for all large $x$, equivalently
\[
e^x\le \log A+Bx^\rho,
\]
which is impossible. Therefore $e^{e^z}$ has infinite order.
:::
