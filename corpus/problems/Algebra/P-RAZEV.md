---
schema: qual/card@1
id: P-RAZEV
kind: problem
title: Wedderburn's theorem and rational group algebras
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Semisimplicity
  - Algebras
relations: []
review: draft
---

::: problem
State the Artin--Wedderburn theorem for finite-dimensional semisimple algebras, and describe the rational group algebras of $C_5$, $C_2\times C_2$, and $Q_8$.
:::

::: {.solution}
The Artin--Wedderburn theorem says that every finite-dimensional semisimple algebra over a field is isomorphic to a finite product
\[
\prod_i M_{n_i}(D_i),
\]
where each $D_i$ is a finite-dimensional division algebra over the base field.

Since $\QQ$ has characteristic $0$, Maschke's theorem makes $\QQ[G]$ semisimple for every finite group $G$.

<1>1. $G=C_5$.
::: {.proof}
Using
\[
\QQ[C_5]\cong \QQ[x]/(x^5-1)
\]
and
\[
x^5-1=(x-1)\Phi_5(x),
\]
with $\Phi_5$ irreducible over $\QQ$, the Chinese remainder theorem gives
\[
\QQ[C_5]\cong \QQ\times\QQ(\zeta_5).
\]
:::

<1>2. $G=C_2\times C_2$.
::: {.proof}
All four irreducible characters are one-dimensional and rational-valued. Hence
\[
\QQ[C_2\times C_2]\cong \QQ^4.
\]
:::

<1>3. $G=Q_8$.
::: {.proof}
The quaternion group has four one-dimensional rational representations and one quaternionic irreducible component. Accordingly,
\[
\QQ[Q_8]
\cong
\QQ^4\times(-1,-1)_{\QQ},
\]
where $(-1,-1)_{\QQ}$ is the rational Hamilton quaternion division algebra
\[
\QQ\langle i,j\mid i^2=j^2=-1,\ ij=-ji\rangle.
\]
The dimensions are $4+4=8$, as required.
:::
:::
