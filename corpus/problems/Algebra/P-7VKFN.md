---
schema: qual/card@1
id: P-7VKFN
kind: problem
title: The quaternion group and the number of elements of each order
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Group Presentations
  - Classification
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

::: {.problem}
What is the quaternion group $Q_8$? Give its presentation and list the number of elements of each order.
:::

::: {.solution}

::: pf

::: {.pf-step #def}

$Q_8=\{\pm1,\pm i,\pm j,\pm k\}$, with multiplication determined by
$$
i^2=j^2=k^2=ijk=-1,
$$
and
$$
Q_8=\langle i,j\mid i^4=1,\ i^2=j^2,\ jij^{-1}=i^{-1}\rangle.
$$

::: pf-proof

The relations give $k=ij$, so $i$ and $j$ generate. In $Q_8$, $i^4=(-1)^2=1$, $i^2=-1=j^2$, and, since $j^{-1}=-j$, $ji=-k$ and $kj=-i$,
$$
jij^{-1}=-(ji)j=kj=-i=i^{-1}.
$$
The presented group has order at most $8$: every element is $i^aj^b$ with $0\le a\le3$ and $0\le b\le1$, since $j^2=i^2$ and $ji=i^{-1}j$. As $Q_8$ is a quotient of it of order $8$, the two are isomorphic.

:::

:::

::: pf-step

$Q_8$ has $\boxed{1}$ element of order $1$, $\boxed{1}$ element of order $2$, and $\boxed{6}$ elements of order $4$.

::: pf-proof

The identity $1$ has order $1$ and $-1$ has order $2$. By step [](#def){.pf-ref}, each of $\pm i,\pm j,\pm k$ squares to $-1$, so it has order $4$. In particular, $-1$ is the unique involution of $Q_8$.

:::

:::

:::

:::
