---
schema: qual/card@1
id: P-OSS6X
kind: problem
title: $H_0$ of a nonempty path-connected space is $\ZZ$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified directly that the augmentation kernel in C_0 is exactly the subgroup of singular 0-boundaries.
---

::: {.problem}
Prove directly from the definition that the 0th singular homology of a nonempty path-connected space is isomorphic to $\ZZ$.
:::

::: {.solution}
<1>1. Since $\partial_0=0$,
\[
H_0(X)
=C_0(X)/\operatorname{im}\partial_1.
\]
::: {.proof}
By definition,
\[
H_0(X)=\ker\partial_0/\operatorname{im}\partial_1.
\]
There are no singular chain groups in degree $-1$, so
\[
\partial_0:C_0(X)\longrightarrow0
\]
is the zero map and hence
\[
\ker\partial_0=C_0(X).
\]
:::

<1>2. Define the augmentation homomorphism
\[
\varepsilon:C_0(X)\longrightarrow\ZZ
\]
by
\[
\varepsilon\left(\sum_{i=1}^r n_i[x_i]\right)
=\sum_{i=1}^r n_i.
\]
It is surjective.
::: {.proof}
A singular $0$-simplex is just a point of $X$, so $C_0(X)$ is the free abelian group on the points of $X$.
Since $X$ is nonempty, choose $x_0\in X$.
Then
\[
\varepsilon([x_0])=1,
\]
so $\varepsilon$ is surjective.
:::

<1>3. Every singular $0$-boundary lies in $\ker\varepsilon$.
::: {.proof}
For a singular $1$-simplex
\[
\sigma:\Delta^1\longrightarrow X,
\]
the boundary is
\[
\partial_1\sigma=[\sigma(1)]-[\sigma(0)].
\]
Therefore
\[
\varepsilon(\partial_1\sigma)=1-1=0.
\]
By linearity,
\[
\operatorname{im}\partial_1\subseteq\ker\varepsilon.
\]
:::

<1>4. If $X$ is path connected, then every element of $\ker\varepsilon$ is a singular $0$-boundary.
::: {.proof}
Fix the point $x_0$ from <1>2.
For every $x\in X$, path connectedness gives a path
\[
\sigma_x:[0,1]\longrightarrow X
\]
with
\[
\sigma_x(0)=x_0,
\qquad
\sigma_x(1)=x.
\]
Regarded as a singular $1$-simplex,
\[
\partial_1\sigma_x=[x]-[x_0].
\]

Now let
\[
c=\sum_{i=1}^r n_i[x_i]\in\ker\varepsilon.
\]
Then
\[
\sum_{i=1}^r n_i=0,
\]
and hence
\[
c
=\sum_{i=1}^r n_i([x_i]-[x_0])
=\partial_1\left(\sum_{i=1}^r n_i\sigma_{x_i}\right).
\]
Thus
\[
\ker\varepsilon\subseteq\operatorname{im}\partial_1.
\]
Together with <1>3,
\[
\ker\varepsilon=\operatorname{im}\partial_1.
\]
:::

<1>5. Therefore
\[
H_0(X)\cong\ZZ.
\]
::: {.proof}
By <1>1 and <1>4,
\[
H_0(X)
=C_0(X)/\operatorname{im}\partial_1
=C_0(X)/\ker\varepsilon.
\]
Since $\varepsilon$ is surjective by <1>2, the first isomorphism theorem gives
\[
C_0(X)/\ker\varepsilon
\cong
\operatorname{im}\varepsilon
=\ZZ.
\]
:::
:::
