---
schema: qual/card@1
id: E-HAT-2.B-10
kind: problem
title: "Homology of $\\mathbb{RP}^\\infty$ via transfer"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the determinant or transfer-sequence argument, including the mod-2 endpoint maps.
---

::: {.problem}
Use the transfer sequence for the covering $S^\infty \to \mathbb{RP}^\infty$ to compute $H_n(\mathbb{RP}^\infty; \mathbb{Z}_2)$.
:::

::: {.solution}
Let
\[
p:S^\infty\longrightarrow\mathbb{RP}^\infty
\]
be the antipodal double cover, and use $\mathbb Z_2$ coefficients throughout. Hatcher's transfer sequence is
\[
\cdots\to H_n(\mathbb{RP}^\infty)
\overset{\tau_*}{\longrightarrow}H_n(S^\infty)
\overset{p_*}{\longrightarrow}H_n(\mathbb{RP}^\infty)
\overset{\delta}{\longrightarrow}H_{n-1}(\mathbb{RP}^\infty)\to\cdots .
\]

<1>1. Since $S^\infty$ is contractible,
\[
H_n(S^\infty;\mathbb Z_2)=0\quad(n>0),
\qquad
H_0(S^\infty;\mathbb Z_2)=\mathbb Z_2.
\]
::: {.proof}
The infinite sphere $S^\infty$ is contractible, so it has the homology of a point.
:::

<1>2. For every $n\ge2$, the connecting map is an isomorphism
\[
\delta:H_n(\mathbb{RP}^\infty;\mathbb Z_2)
\xrightarrow{\cong}
H_{n-1}(\mathbb{RP}^\infty;\mathbb Z_2).
\]
::: {.proof}
The portion of the transfer sequence around these groups is
\[
0\longrightarrow H_n(\mathbb{RP}^\infty)
\overset{\delta}{\longrightarrow}H_{n-1}(\mathbb{RP}^\infty)
\longrightarrow0,
\]
since the adjacent positive-dimensional homology groups of $S^\infty$ vanish.
:::

<1>3. The same conclusion holds for $n=1$:
\[
H_1(\mathbb{RP}^\infty;\mathbb Z_2)\cong H_0(\mathbb{RP}^\infty;\mathbb Z_2)\cong\mathbb Z_2.
\]
::: {.proof}
At the bottom of the transfer sequence we have
\[
0\to H_1(\mathbb{RP}^\infty)
\overset{\delta}{\longrightarrow}H_0(\mathbb{RP}^\infty)
\overset{\tau_*}{\longrightarrow}H_0(S^\infty)
\overset{p_*}{\longrightarrow}H_0(\mathbb{RP}^\infty)\to0.
\]
Both spaces are connected, so $p_*$ is the identity isomorphism on $H_0\cong\mathbb Z_2$. Exactness therefore forces $\tau_*=0$ and $\delta$ to be an isomorphism.
:::

<1>4. Therefore
\[
\boxed{H_n(\mathbb{RP}^\infty;\mathbb Z_2)\cong\mathbb Z_2\quad\text{for every }n\ge0.}
\]
::: {.proof}
The degree-zero group is $\mathbb Z_2$ because $\mathbb{RP}^\infty$ is connected. Apply the isomorphisms of <1>2--<1>3 inductively.
:::
:::
