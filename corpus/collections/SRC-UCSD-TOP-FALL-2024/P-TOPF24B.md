---
schema: qual/card@1
id: P-TOPF24B
kind: problem
title: Examples separating $\pi_2$ and $H_2$
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Give an explicit example:
(a) of a topological space $X$ with $\pi_2(X) = 0$ and $H_2(X) \neq 0$, and
(b) of a topological space $Y$ with $\pi_2(Y) \neq 0$ and $H_2(Y) = 0$.
:::

::: solution
<1>1. For part (a), take $X=T^2=S^1\times S^1$.
<2>1. The universal covering map $\mathbb R^2\to T^2$ induces an isomorphism on homotopy groups in every degree at least $2$.
<2>2. Since $\mathbb R^2$ is contractible,
$$
\pi_2(T^2)\cong \pi_2(\mathbb R^2)=0.
$$
<2>3. Give $T^2$ its standard CW structure with one $0$-cell, two $1$-cells, and one $2$-cell attached by the commutator word $aba^{-1}b^{-1}$.
<2>4. In the cellular chain complex, the boundary $C_2(T^2)\to C_1(T^2)$ is zero because the total exponent of each $1$-cell in the attaching word is zero. There are no $3$-cells. Hence
$$
H_2(T^2;\mathbb Z)=\ker(C_2\to C_1)\cong \mathbb Z\ne0.
$$

<1>2. For part (b), take $Y=\mathbb{RP}^2$.
<2>1. The universal covering map $S^2\to\mathbb{RP}^2$ induces an isomorphism on $\pi_2$, so
$$
\pi_2(\mathbb{RP}^2)\cong\pi_2(S^2)\cong\mathbb Z\ne0.
$$
<2>2. Give $\mathbb{RP}^2$ its standard CW structure with one cell in each dimension $0,1,2$.
<2>3. Its cellular boundary map $C_2\to C_1$ is multiplication by $2$. Therefore
$$
H_2(\mathbb{RP}^2;\mathbb Z)=\ker(\mathbb Z\xrightarrow{\,2\,}\mathbb Z)=0.
$$

<1>3. Thus $T^2$ and $\mathbb{RP}^2$ give the required examples.
:::
