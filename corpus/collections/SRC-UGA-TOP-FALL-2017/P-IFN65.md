---
schema: qual/card@1
id: P-IFN65
kind: problem
title: Freely homotopic loops on a closed genus-$2$ surface that are not homotopic
  rel basepoint
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Fall 2017 topology exam and restored the source instruction that no proof of the example is required.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the non-well-defined map to F(a_1,b_1) with a valid homomorphism to a free group that detects the nontrivial commutator.
---

::: problem
Let $M$ be a compact orientable surface of genus $2$ without boundary.
Give an example of a pair of loops
\[
\gamma_0,\gamma_1:S^1\longrightarrow M
\]
with $\gamma_0(1)=\gamma_1(1)$ such that there is a continuous map
\[
\Gamma:[0,1]\times S^1\longrightarrow M
\]
with
\[
\Gamma(0,t)=\gamma_0(t),
\qquad
\Gamma(1,t)=\gamma_1(t)
\]
for all $t\in S^1$, but such that there is no such map $\Gamma$ with the additional property
\[
\Gamma(s,1)=\gamma_0(1)
\qquad\text{for all }s\in[0,1].
\]
You are not required to prove that your example satisfies the stated property.
:::

::: {.solution}
Choose a base point $x_0\in M$ and standard generators
\[
\pi_1(M,x_0)
=\left\langle a_1,b_1,a_2,b_2
\mathrel{\big|}
[a_1,b_1][a_2,b_2]=1
\right\rangle.
\]
Let $\alpha$ and $\beta$ be based loops representing $a_1$ and $b_1$, respectively, and set
\[
\gamma_0=\alpha,
\qquad
\gamma_1=\beta*\alpha*\overline\beta.
\]

<1>1. The loops $\gamma_0$ and $\gamma_1$ are freely homotopic.
::: {.proof}
Their classes in the fundamental group satisfy
\[
[\gamma_1]
=b_1a_1b_1^{-1}.
\]
Two based loops in a path-connected space are freely homotopic exactly when their fundamental-group elements are conjugate.
Hence $\gamma_0$ and $\gamma_1$ are freely homotopic.
Equivalently, there exists
\[
\Gamma:[0,1]\times S^1\longrightarrow M
\]
with the required endpoint conditions, without requiring the point $\Gamma(s,1)$ to remain fixed during the homotopy.
:::

<1>2. The elements $a_1$ and $b_1$ do not commute in $\pi_1(M,x_0)$.
::: {.proof}
Let $F(x,y)$ be the free group on $x,y$.
Define a map on the generators of the surface presentation by
\[
a_1\longmapsto x,
\qquad
b_1\longmapsto y,
\qquad
a_2\longmapsto y,
\qquad
b_2\longmapsto x.
\]
The relator maps to
\[
[x,y][y,x]
=[x,y][x,y]^{-1}
=1,
\]
so this assignment induces a homomorphism
\[
\rho:\pi_1(M,x_0)\longrightarrow F(x,y).
\]
If $a_1$ and $b_1$ commuted, then $[a_1,b_1]=1$, and therefore
\[
[x,y]=\rho([a_1,b_1])=1.
\]
But
\[
[x,y]=xyx^{-1}y^{-1}
\]
is a nonempty reduced word in the free group $F(x,y)$, so it is not the identity.
Thus $[a_1,b_1]\ne1$.
:::

<1>3. There is no homotopy from $\gamma_0$ to $\gamma_1$ that keeps the common base point fixed.
::: {.proof}
A homotopy with
\[
\Gamma(s,1)=x_0
\qquad\text{for every }s\in[0,1]
\]
would be a based homotopy and would imply
\[
[\gamma_0]=[\gamma_1]
\]
in $\pi_1(M,x_0)$.
Thus
\[
a_1=b_1a_1b_1^{-1},
\]
which is equivalent to $a_1$ and $b_1$ commuting.
This contradicts <1>2. Therefore the displayed pair has the required properties.
:::
:::
