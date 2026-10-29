---
schema: qual/card@1
id: P-ZZVXB
kind: problem
title: Abelian groups of order 9, and groups of order 27
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Abelian Groups
  - p-Groups
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
(1) Classify all abelian groups of order 9 up to isomorphism. Prove that they are not isomorphic to each other.

(2) Classify all abelian groups of order 27 up to isomorphism, and list the non-abelian groups of order 27.
:::

::: {.solution}

::: pf

::: pf-step

(1) The abelian groups of order $9$ are $\boxed{C_9}$ and $\boxed{C_3\times C_3}$, and they are not isomorphic.

::: pf-proof

By the fundamental theorem of finite abelian groups, an abelian group of order $3^2$ is $\prod_i C_{3^{a_i}}$ for a partition $(a_i)$ of $2$, giving these two. $C_9$ has an element of order $9$, while every element of $C_3\times C_3$ has order dividing $3$.

:::

:::

::: pf-step

(2) The abelian groups of order $27$ are $\boxed{C_{27},\ C_9\times C_3,\ C_3^3}$, pairwise nonisomorphic.

::: pf-proof

The partitions of $3$ are $(3)$, $(2,1)$, $(1,1,1)$. The three groups have exponents $27$, $9$, $3$.

:::

:::

::: pf-step

(2) The nonabelian groups of order $27$ are the Heisenberg group
$$
\boxed{UT_3(\FF_3)
=\left\{
\begin{pmatrix}
1&a&b\\0&1&c\\0&0&1
\end{pmatrix}
:a,b,c\in\FF_3
\right\}}
$$
of exponent $3$, and
$$
\boxed{C_9\rtimes C_3=\langle x,y\mid x^9=y^3=1,\ yxy^{-1}=x^4\rangle},
$$
which has an element of order $9$; these two are nonisomorphic.

::: pf-proof

That every nonabelian group of order $p^3$, $p$ odd, is one of these two is the standard classification of groups of order $p^3$. Both are nonabelian: in $UT_3(\FF_3)$ the elementary matrices $E_{12}$ and $E_{23}$ do not commute, and in $C_9\rtimes C_3$, $yxy^{-1}=x^4\ne x$; the relation is consistent because $4^3=64\equiv1\pmod 9$. In $UT_3(\FF_3)$, $(I+N)^3=I+3N+3N^2+N^3=I$ for strictly upper triangular $N$, so it has exponent $3$, while $x$ has order $9$ in $C_9\rtimes C_3$.

:::

:::

:::

:::
