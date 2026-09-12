---
schema: qual/card@1
id: P-C2EQN
kind: problem
title: The class equation, and a nontrivial normal subgroup of a $p$-group meets the
  center
classification:
  areas:
  - algebra
  topics:
  - Class Equation
  - p-Groups
  - Normal Subgroups
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
a. State the class equation.

b. Suppose $|G| = p^k$ and $H$ is a normal subgroup of $G$ with $|H| > 1$.
Show that $H$ contains a non-identity element of the center $Z(G)$ of $G$.
:::

::: {.solution}
<1>1. If \(x_1,\dots,x_r\) represent the noncentral conjugacy classes of a finite group \(G\), then the class equation is
\[
|G|=|Z(G)|+\sum_{i=1}^r [G:C_G(x_i)].
\]
::: {.proof}
The conjugacy class of \(x\in G\) has cardinality \([G:C_G(x)]\) by orbit-stabilizer for the conjugation action. The central elements are exactly the singleton conjugacy classes. Partitioning \(G\) into its conjugacy classes therefore gives the displayed equation.
:::

<1>2. Let \(G\) act on the normal subgroup \(H\) by conjugation. The fixed-point set of this action is
\[
H^G=H\cap Z(G).
\]
::: {.proof}
Normality of \(H\) ensures that conjugation by every element of \(G\) preserves \(H\). An element \(h\in H\) is fixed by every conjugation map exactly when \(ghg^{-1}=h\) for every \(g\in G\), equivalently \(h\in Z(G)\).
:::

<1>3. Every nontrivial orbit of the conjugation action of \(G\) on \(H\) has cardinality divisible by \(p\).
::: {.proof}
For \(h\in H\), orbit-stabilizer gives
\[
|G\cdot h|=[G:C_G(h)].
\]
Since \(|G|=p^k\), every subgroup index is a power of \(p\). If the orbit is not a singleton, its size is therefore a positive power of \(p\), hence divisible by \(p\).
:::

<1>4. The cardinality \(|H\cap Z(G)|\) is divisible by \(p\).
::: {.proof}
Partitioning \(H\) into conjugation orbits gives
\[
|H|=|H\cap Z(G)|+\sum_j |\mathcal O_j|,
\]
where the \(\mathcal O_j\) are the nontrivial orbits. Because \(H\) is a nontrivial subgroup of the finite \(p\)-group \(G\), its order is a positive power of \(p\), hence divisible by \(p\). By <1>3 every term in the sum is divisible by \(p\). Therefore \(|H\cap Z(G)|\equiv0\pmod p\).
:::

<1>5. Hence \(H\) contains a nonidentity element of \(Z(G)\).
::: {.proof}
The intersection \(H\cap Z(G)\) contains the identity, so it is nonempty. By <1>4 its cardinality is a positive multiple of \(p\), hence at least \(p\ge2\). Therefore it contains an element other than the identity.
:::
:::
