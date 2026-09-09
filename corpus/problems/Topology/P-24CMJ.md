---
schema: qual/card@1
id: P-24CMJ
kind: problem
title: $\pi_1(S^1\vee S^1)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Compute the fundamental group $\pi_1(S^1 \vee S^1, x_0)$ of the wedge sum of two circles (the figure eight space).
:::

::: solution
Let $X=S^1_a\vee S^1_b$ with wedge point $x_0$.

<1>1. Choose points $p_a\in S^1_a\setminus\{x_0\}$ and $p_b\in S^1_b\setminus\{x_0\}$, and put
$$
U=X\setminus\{p_b\},
\qquad
V=X\setminus\{p_a\}.
$$
Then $U\simeq S^1_a$, $V\simeq S^1_b$, and $U\cap V$ is contractible.

<1>2. Therefore
$$
\pi_1(U,x_0)\cong\mathbb Z,
\qquad
\pi_1(V,x_0)\cong\mathbb Z,
\qquad
\pi_1(U\cap V,x_0)=1.
$$

<1>3. Seifert--van Kampen gives
$$
\pi_1(S^1\vee S^1,x_0)
\cong
\mathbb Z*\mathbb Z
\cong F_2.
$$
Thus the figure eight has free fundamental group on the two circle loops.
:::
