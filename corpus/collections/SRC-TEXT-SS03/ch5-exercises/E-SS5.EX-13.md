---
schema: qual/card@1
id: E-SS5.EX-13
kind: problem
title: "SS 5.13: The equation e^z = z has infinitely many solutions"
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
13. Show that the equation $e ^ { z } - z = 0$ has infinitely many solutions in $\mathbb { C } .$

[Hint: Apply Hadamard’s theorem.]
:::

::: solution
Let
\[
F(z)=e^z-z.
\]
This is an entire function of order at most $1$. Suppose, for contradiction, that it had only finitely many zeros. Hadamard's factorization theorem would then give
\[
F(z)=e^{az+b}Q(z)
\]
for some constants $a,b\in\mathbb C$ and a polynomial $Q$ whose zeros are exactly those finitely many zeros of $F$.

Along the negative real axis,
\[
F(x)=e^x-x\sim -x\qquad(x\to-\infty),
\]
so
\[
\log|F(x)|=\log|x|+o(1).
\tag{1}
\]
If $m=\deg Q$, the factorization gives
\[
\log|F(x)|=(\Re a)x+m\log|x|+O(1).
\tag{2}
\]
Comparing (1) and (2) forces
\[
\Re a=0,
\qquad
m=1.
\tag{3}
\]

On the positive real axis, however,
\[
F(x)=e^x-x\sim e^x,
\]
so
\[
\log|F(x)|=x+o(1).
\tag{4}
\]
But (2) and (3) give only
\[
\log|F(x)|=\log x+O(1),
\]
contradicting (4). Therefore $e^z-z$ has infinitely many zeros in $\mathbb C$.
:::
