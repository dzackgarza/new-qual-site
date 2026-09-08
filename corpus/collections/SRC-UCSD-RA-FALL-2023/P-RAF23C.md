---
schema: qual/card@1
id: P-RAF23C
kind: problem
title: "Measure equality implies density one"
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
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a $\sigma$-compact locally compact Hausdorff space.
Let $\mu$ be a Radon measure on $X$.
Let $f \geq 0$ be a measurable function.
Prove that if for any open subset $U$, $\mu(U) = \int_U f\,d\mu$, then $f = 1$ $\mu$-a.e.
:::

::: solution
<1>1. Show that $f\le1$ almost everywhere.
::: proof
Fix $\varepsilon>0$ and set
\[
A_\varepsilon:=\{x:f(x)\ge1+\varepsilon\}.
\]
Suppose $\mu(A_\varepsilon)>0$. Since $\mu$ is Radon, there is a compact set
\[
K\subset A_\varepsilon
\]
with $0<\mu(K)<\infty$. By outer regularity, choose an open set $U\supset K$ such that
\[
\mu(U)<\left(1+\frac\varepsilon2\right)\mu(K).
\]
But the hypothesis gives
\[
\mu(U)=\int_U f\,d\mu
\ge \int_K f\,d\mu
\ge (1+\varepsilon)\mu(K),
\]
contradicting the choice of $U$. Hence
\[
\mu(A_\varepsilon)=0.
\]
Taking $\varepsilon=1/m$ and a countable union gives
\[
f\le1\qquad\mu\text{-a.e.}
\]
:::

<1>2. Use the open-set identity to rule out $f<1$ on a set of positive measure.
::: proof
After changing $f$ on a null set if necessary, assume $0\le f\le1$ everywhere. For every open set $U$,
\[
0=\mu(U)-\int_U f\,d\mu
=\int_U(1-f)\,d\mu.
\]
Thus the nonnegative function $1-f$ has integral zero on every open set.

Because $X$ is $\sigma$-compact and locally compact Hausdorff, it admits a countable cover by relatively compact open sets $U_j$. On each $U_j$,
\[
\int_{U_j}(1-f)\,d\mu=0,
\]
so $1-f=0$ almost everywhere on $U_j$. Taking the countable union yields
\[
\boxed{f=1\quad\mu\text{-a.e. on }X.}
\]
:::
:::
