---
schema: qual/card@1
id: P-N4I2S
kind: problem
title: Solvability and nonnilpotence of small symmetric groups
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Nilpotent Groups
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the retained Hungerford II.7 exercise statement and independent standard treatments of the solvable series for $S_4$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $S_n$ is solvable for $n\leq 4$ but $S_3$ and $S_4$ are not nilpotent.
:::

::: solution
<1>1. The groups $S_1$ and $S_2$ are solvable.
::: proof
Both are abelian, and every abelian group is solvable.
:::

<1>2. The group $S_3$ is solvable.
::: proof
The chain
\[
S_3\trianglerighteq A_3\trianglerighteq\{e\}
\]
is a normal series. Its factors are
\[
S_3/A_3\cong\ZZ_2,
\qquad
A_3\cong\ZZ_3,
\]
which are abelian. Hence $S_3$ is solvable.
:::

<1>3. The group $S_4$ is solvable.
::: proof
Let
\[
V=\{e,(12)(34),(13)(24),(14)(23)\}.
\]
Conjugation in $S_4$ preserves cycle type, so it permutes the three nonidentity
elements of $V$; hence $V\trianglelefteq S_4$. Also $V\le A_4$. Thus
\[
S_4\trianglerighteq A_4\trianglerighteq V\trianglerighteq\{e\}
\]
is a normal series, and its factors have orders $2$, $3$, and $4$ respectively.
More precisely,
\[
S_4/A_4\cong\ZZ_2,
\qquad
A_4/V\cong\ZZ_3,
\qquad
V\cong\ZZ_2^2.
\]
All factors are abelian, so $S_4$ is solvable.
:::

<1>4. The center of $S_3$ is trivial.
::: proof
A central element must commute with $(12)$. Of the six elements of $S_3$, the
centralizer of $(12)$ is $\{e,(12)\}$. But $(12)$ does not commute with $(23)$,
so the only central element is $e$.
:::

<1>5. The center of $S_4$ is trivial.
::: proof
Let $\sigma\in Z(S_4)$. Since $\sigma$ commutes with every transposition,
\[
\sigma(ij)\sigma^{-1}=(ij)
\]
for every $i\ne j$. But conjugation relabels a transposition:
\[
\sigma(ij)\sigma^{-1}=(\sigma(i)\ \sigma(j)).
\]
Hence $\{\sigma(i),\sigma(j)\}=\{i,j\}$ for every pair $i\ne j$. Fixing $i$
and choosing two distinct $j,k\ne i$ forces $\sigma(i)=i$. Thus every point is
fixed and $\sigma=e$.
:::

<1>6. The groups $S_3$ and $S_4$ are not nilpotent.
::: proof
Every nontrivial nilpotent group has nontrivial center: if its upper central
series reaches the whole group, the first nontrivial term is contained in the
center. By <1>4 and <1>5, both $S_3$ and $S_4$ are nontrivial with trivial
center. Therefore neither is nilpotent.
:::
:::
