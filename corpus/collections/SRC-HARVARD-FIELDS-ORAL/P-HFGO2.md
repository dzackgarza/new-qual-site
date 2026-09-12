---
schema: qual/card@1
id: P-HFGO2
kind: problem
title: A sum of algebraic numbers is algebraic
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
If $\alpha$ and $\beta$ are algebraic over $\mathbb Q$, prove that $\alpha+\beta$ is algebraic over $\mathbb Q$.
:::

::: solution
Set
\[
K=\mathbb Q(\alpha,\beta).
\]

<1>1. The extension $K/\mathbb Q$ is finite.
::: proof
Since $\alpha$ is algebraic over $\mathbb Q$,
\[
[\mathbb Q(\alpha):\mathbb Q]<\infty.
\]
The element $\beta$ is algebraic over $\mathbb Q$, hence also algebraic over
the larger field $\mathbb Q(\alpha)$. Therefore
\[
[K:\mathbb Q(\alpha)]<\infty.
\]
By the tower law,
\[
[K:\mathbb Q]
=[K:\mathbb Q(\alpha)]
[\mathbb Q(\alpha):\mathbb Q]
<\infty.
\]
:::

<1>2. Every element of the finite extension $K/\mathbb Q$ is algebraic over
$\mathbb Q$.
::: proof
Let $\gamma\in K$. If $d=[K:\mathbb Q]$, then the $d+1$ elements
\[
1,\gamma,\gamma^2,\ldots,\gamma^d
\]
are linearly dependent over $\mathbb Q$. Thus there are rational numbers
$c_0,\ldots,c_d$, not all zero, such that
\[
c_0+c_1\gamma+\cdots+c_d\gamma^d=0.
\]
Hence $\gamma$ satisfies a nonzero polynomial in $\mathbb Q[x]$.
:::

<1>3. Therefore $\alpha+\beta$ is algebraic over $\mathbb Q$.
::: proof
The sum $\alpha+\beta$ belongs to $K$, so apply <1>2.
:::
:::
