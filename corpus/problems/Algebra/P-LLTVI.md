---
schema: qual/card@1
id: P-LLTVI
kind: problem
title: Subgroups of $\ZZ^2$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Abelian Groups
  - Free Modules
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Describe the subgroups of $\ZZ^2$.
:::

::: {.solution}
Every subgroup $H\le\ZZ^2$ is a free abelian group of rank $0$, $1$, or $2$.

<1>1. Rank $0$ gives only the zero subgroup.

<1>2. Every rank-$1$ subgroup is infinite cyclic.
::: {.proof}
Since $\ZZ$ is a PID, every submodule of the free module $\ZZ^2$ is free. A rank-$1$ subgroup therefore has the form
\[
H=\ZZ(a,b)
\]
for some nonzero vector $(a,b)\in\ZZ^2$.
:::

<1>3. Every rank-$2$ subgroup has finite index and admits a Smith normal form.
::: {.proof}
Choose a basis $v_1,v_2$ of $H$ and form the $2\times2$ integer matrix whose columns are $v_1,v_2$. Smith normal form gives unimodular matrices $U,V\in GL_2(\ZZ)$ such that
\[
UAV=\begin{pmatrix}d_1&0\\0&d_2\end{pmatrix},
\qquad d_1,d_2>0,
\quad d_1\mid d_2.
\]
Thus, after an automorphism of $\ZZ^2$,
\[
H=d_1\ZZ\oplus d_2\ZZ.
\]
In particular,
\[
[\ZZ^2:H]=d_1d_2<\infty.
\]
:::

Equivalently, every subgroup is either $0$, cyclic, or a rank-$2$ lattice of finite index in $\ZZ^2$.
:::
