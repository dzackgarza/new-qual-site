---
schema: qual/card@1
id: P-JHUMAY09ANB
kind: problem
title: The unique right-half-plane solution of $z+e^{-z}=2+i$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the equation and right-half-plane restriction with May 2009 problem 2 in the retained JHU extraction; replaced the non-mathematical title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Located every possible solution in the same radius-one disk, checked strict Rouche dominance on its boundary and concluded uniqueness with multiplicity one."
---

2. How many solutions does the equation

$$
z + e ^ { - z } = 2 + i
$$

have in the half-plane Re $z > 0 ?$ Prove that your answer is correct.

::: solution
There is exactly $\boxed{1}$ solution in the right half-plane,
and it is a simple zero of $z+e^{-z}-(2+i)$.

<1>1. Every right-half-plane solution lies in $B=\{z:|z-(2+i)|<1\}$.
::: proof
If $z$ satisfies the equation and $\operatorname{Re}z>0$,
then
$$
|z-(2+i)|=|e^{-z}|=e^{-\operatorname{Re}z}<1.
$$
Thus $z\in B$. Conversely every point of $B$ has real
part greater than one, so all zeros in $B$ lie in the
required half-plane. It remains to count the zeros there.
:::

<1>2. There is precisely one zero in $B$, counted with multiplicity.
::: proof
For $|z-(2+i)|=1$ one has $\operatorname{Re}z\geq1$.
Consequently
$$
|e^{-z}|=e^{-\operatorname{Re}z}\leq e^{-1}<1=|z-(2+i)|.
$$
Both $z-(2+i)$ and $e^{-z}$ are entire, so Rouché's
theorem on this circle gives the same number of zeros
inside for $z+e^{-z}-(2+i)$ as for $z-(2+i)$ [@SS03].
The latter has exactly one simple zero. Thus the former
has one zero counted with multiplicity, which means that
there is one distinct zero and its multiplicity is one.
By step <1>1 no right-half-plane solution lies outside $B$.
This gives the asserted complete count.
:::
:::
