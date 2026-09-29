---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P8
kind: problem
title: Simplicial homology of the connected sum of two projective planes via a $\Delta$-complex structure
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Cell Complexes
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
(May 2016) Construct a $\Delta$-complex structure, and use it to compute the simplicial homology groups, for the connected sum of two projective planes.
:::

::: {.solution}
Let $K=\mathbb{R}P^2\#\mathbb{R}P^2$. Take the unit square with corners $P=(0,0)$, $Q=(1,0)$, $R=(0,1)$, $S=(1,1)$, and identify its sides by the edges
$$
a\colon P\to Q \text{ and } R\to S,
\qquad
b\colon P\to R \text{ and } S\to Q,
$$
so that the boundary word read from $P$ counterclockwise is $a\,b^{-1}a^{-1}b^{-1}$. Add the diagonal $c\colon P\to S$.

::: pf

::: pf-step

The quotient is homeomorphic to $K$.

::: pf-proof

The edge $a$ occurs once with each exponent and $b$ occurs twice with exponent $-1$, so the quotient is a closed nonorientable surface. The identifications give $P\sim R$ and $Q\sim S$ (from $a$) and $P\sim S$ and $R\sim Q$ (from $b$), so all four corners become one vertex $v$. With one vertex, two edges, and one face, $\chi=1-2+1=0$. By the classification of closed surfaces, the nonorientable surface with $\chi=0$ is $\#^2\mathbb{R}P^2=K$.

:::

:::

::: pf-step

The diagonal cuts the square into two $2$-simplices $U=[P,R,S]$ and $L=[P,S,Q]$, and together with $v$ and the edges $a,b,c$ this is a $\Delta$-complex structure on $K$ with
$$
\partial_2 U=a+b-c,
\qquad
\partial_2 L=-a+b+c,
\qquad
\partial_1=0.
$$

::: pf-proof

In $U=[P,R,S]$ the faces are $[R,S]=a$, $[P,S]=c$, $[P,R]=b$, each oriented from the lower to the higher vertex, so $\partial_2 U=[R,S]-[P,S]+[P,R]=a-c+b$. In $L=[P,S,Q]$ the faces are $[S,Q]=b$, $[P,Q]=a$, $[P,S]=c$, so $\partial_2 L=[S,Q]-[P,Q]+[P,S]=b-a+c$. Every edge begins and ends at $v$, so $\partial_1=0$.

:::

:::

::: {.pf-step #s3}

$H_2(K)=0$.

::: pf-proof

If $\partial_2(xU+yL)=0$, the coefficients of $a$ and $b$ give $x-y=0$ and $x+y=0$, so $x=y=0$. There are no $3$-simplices, so $H_2(K)=\ker\partial_2=0$.

:::

:::

::: {.pf-step #s4}

$H_1(K)\cong\mathbb Z\oplus\mathbb Z/2$.

::: pf-proof

$H_1(K)=\ker\partial_1/\operatorname{im}\partial_2=\mathbb Z\langle a,b,c\rangle/\langle a+b-c,\,-a+b+c\rangle$. In the basis $a,b,c'$ with $c'=a+b-c$, the relations are $c'$ and $-a+b+(a+b-c')=2b-c'$. Hence the quotient is $\mathbb Z\langle a,b\rangle/\langle 2b\rangle\cong\mathbb Z\oplus\mathbb Z/2$.

:::

:::

::: pf-qed

With one vertex and $\partial_1=0$, $H_0(K)=C_0\cong\mathbb Z$. Together with steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\boxed{H_0(K)\cong\mathbb Z,\qquad H_1(K)\cong\mathbb Z\oplus\mathbb Z/2,\qquad H_n(K)=0\ (n\ge2).}
$$

:::

:::

:::
