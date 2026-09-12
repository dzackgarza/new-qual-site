---
schema: qual/card@1
id: P-LARQ11
kind: problem
title: The third isomorphism theorem for rings
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts of the third-isomorphism-theorem exercise with Lerman practice problem 11."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked well-defined ideal operations in R/K and the kernel and surjectivity of the canonical map to R/I."
---

::: problem
Let $K\subseteq I$ be ideals of a ring $R$.
Prove that $I/K$ is an ideal of $R/K$ and that
$$
(R/K)/(I/K)\cong R/I.
$$
:::

::: solution
<1>1. The subset $I/K$ is an ideal of $R/K$.
::: proof
Because $K\subseteq I$, the set
$$
I/K=\{i+K:i\in I\}
$$
is well-defined as a subset of $R/K$. It is an additive subgroup: if $i,j\in I$, then
$$
(i+K)-(j+K)=(i-j)+K\in I/K.
$$
If $r+K\in R/K$ and $i+K\in I/K$, then
$$
(r+K)(i+K)=ri+K\in I/K,
$$
and similarly $(i+K)(r+K)=ir+K\in I/K$, because $I$ is a two-sided ideal of $R$. Thus $I/K\triangleleft R/K$.
:::

<1>2. The quotient by $I/K$ is naturally isomorphic to $R/I$.
::: proof
Define
$$
\Phi:R/K\to R/I,
\qquad
\Phi(r+K)=r+I.
$$
This is well-defined: if $r+K=s+K$, then $r-s\in K\subseteq I$, so $r+I=s+I$. It is a ring homomorphism and is surjective, since every class $r+I$ is the image of $r+K$.

Its kernel is
$$
\ker\Phi
=\{r+K:r\in I\}
=I/K.
$$
The first isomorphism theorem therefore gives
$$
(R/K)/(I/K)\cong R/I,
$$
as required.
:::
:::
