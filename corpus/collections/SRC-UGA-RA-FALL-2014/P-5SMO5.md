---
schema: qual/card@1
id: P-5SMO5
kind: problem
title: $g\in L^\infty([0,1])$ orthogonal to every continuous function vanishes a.e.
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Density
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the UGA Fall 2014 real-analysis qualifying exam recorded by the collection source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $g\in L^\infty([0, 1])$
Prove that
\[
\int _{[0,1]} f(x) g(x)\, dx = 0 
\quad\text{for all continuous } f:[0, 1] \to \RR 
\implies g(x) = 0 \text{ almost everywhere. }
\]
:::

::: concept
\envlist

- Polar decomposition: $f = \sign(f) \cdot \abs{f}$.
- $L^\infty[0, 1] \subseteq L^1[0, 1]$.

:::

::: solution
<1>1. Use density of continuous functions in $L^1([0,1])$.
::: proof
Because $g\in L^\infty([0,1])$, it also belongs to $L^1([0,1])$. Define
\[
\sigma(x)=
\begin{cases}
\operatorname{sgn}(g(x)),&g(x)\ne0,\\
0,&g(x)=0.
\end{cases}
\]
Then $\sigma\in L^1([0,1])$. Since $C([0,1])$ is dense in $L^1([0,1])$, there are $f_k\in C([0,1])$ such that
\[
\|f_k-\sigma\|_1\longrightarrow0.
\]
:::

<1>2. Pass the orthogonality identity to the $L^1$ limit.
::: proof
By the hypothesis,
\[
\int_0^1 f_k(x)g(x)\,dx=0
\qquad\text{for every }k.
\]
Moreover,
\[
\left|\int_0^1 (f_k-\sigma)g\,dx\right|
\le \|g\|_\infty\,\|f_k-\sigma\|_1
\longrightarrow0.
\]
Hence
\[
0=\lim_{k\to\infty}\int_0^1 f_kg
=\int_0^1 \sigma g
=\int_0^1 |g|.
\]
Therefore $|g|=0$ almost everywhere, so
\[
\boxed{g=0\quad\text{a.e. on }[0,1].}
\]
:::
:::
