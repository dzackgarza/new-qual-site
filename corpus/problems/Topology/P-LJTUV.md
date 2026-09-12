---
schema: qual/card@1
id: P-LJTUV
kind: problem
title: $\pi_i(T^n)=0$ for $i\geq 2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Covering Spaces
  - Product Topology
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
Compute the higher homotopy groups $\pi_i(T^n)$ of the $n$-torus $T^n = (S^1)^n$ for all $i \ge 2$.
:::

::: solution
<1>1. The product of the universal covering maps $\mathbb R\to S^1$ gives a universal covering map
$$
p:\mathbb R^n\longrightarrow T^n=(S^1)^n.
$$
The total space $\mathbb R^n$ is contractible.

<1>2. A covering map induces an isomorphism on homotopy groups in every degree $i\ge2$.
::: proof
For $i\ge2$, every based map $S^i\to T^n$ lifts uniquely after choosing the lift of the basepoint, since $S^i$ is simply connected. The same lifting statement for homotopies shows that this correspondence induces a bijection on based homotopy classes, hence an isomorphism on $\pi_i$.
:::

<1>3. Therefore, for every $i\ge2$,
$$
\pi_i(T^n)\cong\pi_i(\mathbb R^n)=0.
$$
Thus $T^n$ is aspherical.
:::
