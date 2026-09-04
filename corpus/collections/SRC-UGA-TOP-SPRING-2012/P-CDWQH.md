---
schema: qual/card@1
id: P-CDWQH
kind: problem
title: $H_0(X)\cong\ZZ$ for path-connected $X$
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
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked directly that the augmentation kernel equals the subgroup of singular 0-boundaries.
---

::: problem
Give a self-contained proof that the zeroth homology $H_0 (X)$ is isomorphic to $\ZZ$ for every path-connected space $X$.
:::

::: {.solution}
<1>1. The singular chain group \(C_0(X)\) is the free abelian group on the points of \(X\).
::: {.proof}
A singular \(0\)-simplex is a continuous map
\[
\Delta^0\to X.
\]
Since \(\Delta^0\) consists of one point, giving such a map is exactly the same as choosing a point \(x\in X\). Write the corresponding generator of \(C_0(X)\) as \([x]\). Thus every \(0\)-chain has the form
\[
c=\sum_{i=1}^r n_i[x_i],
\qquad n_i\in\mathbb Z.
\]
:::

<1>2. Define the augmentation homomorphism
\[
\varepsilon:C_0(X)\to\mathbb Z,
\qquad
\varepsilon\left(\sum_i n_i[x_i]\right)=\sum_i n_i.
\]
Every singular \(0\)-boundary lies in \(\ker\varepsilon\).
::: {.proof}
A singular \(1\)-simplex is a path
\[
\sigma:\Delta^1=[0,1]\to X.
\]
Its boundary is
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

<1>3. If \(X\) is path-connected, then for any two points \(x,y\in X\),
\[
[y]-[x]\in\operatorname{im}\partial_1.
\]
::: {.proof}
Path-connectedness gives a continuous path
\[
\gamma:[0,1]\to X
\]
with
\[
\gamma(0)=x,
\qquad
\gamma(1)=y.
\]
Regard \(\gamma\) as a singular \(1\)-simplex.
Then
\[
\partial_1\gamma=[y]-[x].
\]
:::

<1>4. If \(X\) is path-connected and nonempty, then
\[
\ker\varepsilon\subseteq\operatorname{im}\partial_1.
\]
::: {.proof}
Fix a point \(x_0\in X\). Let
\[
c=\sum_{i=1}^r n_i[x_i]\in\ker\varepsilon.
\]
Then
\[
\sum_{i=1}^r n_i=0,
\]
so
\[
c
=
\sum_{i=1}^r n_i\bigl([x_i]-[x_0]\bigr).
\]
By <1>3, each difference \([x_i]-[x_0]\) is a singular \(0\)-boundary.
Hence \(c\in\operatorname{im}\partial_1\).
:::

<1>5. Consequently,
\[
\ker\varepsilon=\operatorname{im}\partial_1.
\]
::: {.proof}
The inclusion
\[
\operatorname{im}\partial_1\subseteq\ker\varepsilon
\]
is <1>2, and the reverse inclusion is <1>4.
:::

<1>6. The augmentation induces an isomorphism
\[
\boxed{H_0(X;\mathbb Z)\cong\mathbb Z}.
\]
::: {.proof}
Since \(C_{-1}(X)=0\), the boundary map out of \(C_0(X)\) is zero, so
\[
H_0(X;\mathbb Z)
=
\frac{C_0(X)}{\operatorname{im}\partial_1}.
\]
By <1>5,
\[
H_0(X;\mathbb Z)
=
\frac{C_0(X)}{\ker\varepsilon}.
\]
The map \(\varepsilon\) is surjective because
\[
\varepsilon([x_0])=1.
\]
Hence the first isomorphism theorem gives
\[
\frac{C_0(X)}{\ker\varepsilon}
\cong
\mathbb Z.
\]
Explicitly, the isomorphism sends the homology class of a \(0\)-chain to the sum of its coefficients, and its inverse sends
\[
m\longmapsto m[x_0].
\]
:::
:::
