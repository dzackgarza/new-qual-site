---
schema: qual/card@1
id: P-ALGREV1-09
kind: problem
title: Isomorphic subgroups and quotient groups
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, true/sometimes/false question 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Classified the assertion as sometimes true; in C4×C2 two isomorphic normal C2 subgroups yield quotients C2×C2 and C4."
---

::: {.problem}
Classify the following assertion as true, sometimes true, or false: if $H\cong K$, then $G/H\cong G/K$.
:::

::: solution
The assertion is **sometimes true**.

<1>1. There are cases in which the quotients are isomorphic.
::: proof
For example, if $H=K$, then certainly $H\cong K$ and
$$
G/H=G/K.
$$
Thus the assertion can hold.
:::

<1>2. Isomorphic normal subgroups can give nonisomorphic quotients.
::: proof
Let
$$
G=\mathbb Z_4\times\mathbb Z_2,
$$
and take
$$
H=\langle(2,0)\rangle,
\qquad
K=\langle(0,1)\rangle.
$$
Since $G$ is abelian, both subgroups are normal, and both are isomorphic to
$\mathbb Z_2$. However,
$$
G/H\cong
(\mathbb Z_4/\langle2\rangle)\times\mathbb Z_2
\cong\mathbb Z_2\times\mathbb Z_2,
$$
whereas
$$
G/K\cong\mathbb Z_4.
$$
The first quotient has no element of order $4$, while the second does, so
they are not isomorphic.
:::

<1>3. Conclude the classification.
::: proof
The assertion holds in step <1>1 and fails in step <1>2. Hence
$$
\boxed{\text{sometimes true}.}
$$
:::
:::
