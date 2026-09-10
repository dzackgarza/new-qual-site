---
schema: qual/card@1
id: P-UHFLP
kind: problem
title: Bounded continuous real functions are complete in the supremum norm
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Completeness
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: The preserved Emory source states a max norm on all continuous functions over a complete metric space. That is not well-defined in general; the card corrects the theorem to bounded continuous functions with the supremum norm. Completeness of the domain is unnecessary.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $X$ be a metric space and let $C_b(X,\mathbb R)$ be the vector space of bounded continuous functions $f:X\to\mathbb R$. Define
$$
\|f\|_\infty:=\sup_{x\in X}|f(x)|.
$$
Prove that $(C_b(X,\mathbb R),\|\cdot\|_\infty)$ is complete.
:::

::: solution
<1>1. Construct the pointwise limit.
::: proof
Let $(f_n)$ be Cauchy in the supremum norm. For every $x\in X$ and every $m,n$,
\[
|f_n(x)-f_m(x)|\le \|f_n-f_m\|_\infty.
\]
Hence $(f_n(x))$ is a Cauchy sequence in $\mathbb R$, so it converges. Define
\[
f(x):=\lim_{n\to\infty}f_n(x).
\]
:::

<1>2. Prove uniform convergence.
::: proof
Fix $\varepsilon>0$. Since $(f_n)$ is Cauchy, there exists $N$ such that
\[
\|f_n-f_m\|_\infty<\varepsilon
\]
for all $m,n\ge N$. Fix $n\ge N$ and let $m\to\infty$. For every $x\in X$,
\[
|f_n(x)-f(x)|\le\varepsilon.
\]
Taking the supremum over $x$ gives
\[
\|f_n-f\|_\infty\le\varepsilon.
\]
Thus $f_n\to f$ uniformly.
:::

<1>3. Show that the limit belongs to $C_b(X,\mathbb R)$.
::: proof
Uniform limits of continuous functions are continuous, so $f$ is continuous. Also, for any fixed $N$,
\[
\|f\|_\infty
\le \|f-f_N\|_\infty+\|f_N\|_\infty<\infty.
\]
Thus $f$ is bounded. Therefore $f\in C_b(X,\mathbb R)$, and every Cauchy sequence in the supremum norm converges in that norm. Hence
\[
\boxed{C_b(X,\mathbb R)\text{ is a Banach space}.}
\]
:::
:::
