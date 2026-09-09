---
schema: qual/card@1
id: P-HYQCG
kind: problem
title: Composition series, solvability, and nilpotence
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Nilpotent Groups
  - Solvable Groups
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
- Define what a composition series is, and state what it means for a group to be simple, solvable, or nilpotent.

  - How are the derived and lower/upper central series defined?
    What type(s) of the groups above does each series correspond to?
:::


::: {.solution}
<1>1. A **composition series** of a finite group $G$ is a subnormal series
\[
G=G_0\triangleright G_1\triangleright\cdots\triangleright G_n=1
\]
in which each factor $G_i/G_{i+1}$ is simple.
::: {.proof}
Equivalently, each $G_{i+1}$ is a maximal proper normal subgroup of $G_i$. The Jordan–Hölder theorem says that the multiset of composition factors is independent of the chosen composition series, up to isomorphism and order.
:::

<1>2. A nontrivial group is **simple** if its only normal subgroups are $1$ and itself.
::: {.proof}
This is the standard definition.
:::

<1>3. The **derived series** is
\[
G^{(0)}=G,
\qquad
G^{(i+1)}=[G^{(i)},G^{(i)}].
\]
A group is **solvable** iff $G^{(n)}=1$ for some $n$.
::: {.proof}
Each quotient
\[
G^{(i)}/G^{(i+1)}
\]
is abelian. Conversely, a finite normal series with abelian factors forces the derived series to descend through the series and eventually reach $1$.
:::

<1>4. The **lower central series** is
\[
\gamma_1(G)=G,
\qquad
\gamma_{i+1}(G)=[\gamma_i(G),G].
\]
A group is nilpotent iff $\gamma_{c+1}(G)=1$ for some $c$.
::: {.proof}
This is one standard characterization of nilpotence; the least such $c$ is the nilpotency class.
:::

<1>5. The **upper central series** is
\[
Z_0(G)=1,
\qquad
Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G)).
\]
A group is nilpotent iff $Z_c(G)=G$ for some $c$.
::: {.proof}
The upper and lower central series give equivalent characterizations of nilpotence. The upper series builds $G$ by successive central extensions, while the lower series measures iterated commutators.
:::

Thus composition series concern simple factors, the derived series detects solvability, and the lower/upper central series detect nilpotence. Every nilpotent group is solvable, but not conversely.
:::
