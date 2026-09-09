---
schema: qual/card@1
id: P-22OXL
kind: problem
title: Unique proper nontrivial normal subgroup of $S_n$ ($n\geq 5$) is $A_n$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Permutations
  - Simple Groups
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
- Show that $S_{n\geq 5}$ has one normal subgroup: $A_n$.
:::

::: {.solution}
The literal statement has the trivial exceptions $\{1\}$ and $S_n$; the intended claim
is that $A_n$ is the unique proper nontrivial normal subgroup of $S_n$ for $n\ge 5$.

<1>1. For $n\ge 5$, $A_n$ is simple.
::: {.proof}
We use the standard simplicity theorem for alternating groups: $A_n$ is simple for every
$n\ge 5$.
:::

<1>2. Let $N\trianglelefteq S_n$. Then $N\cap A_n\trianglelefteq A_n$, so
\[
N\cap A_n\in\{1,A_n\}.
\]
::: {.proof}
The intersection of two normal subgroups of $S_n$ is normal in $S_n$, hence in $A_n$.
Apply <1>1.
:::

<1>3. If $N\cap A_n=A_n$, then either $N=A_n$ or $N=S_n$.
::: {.proof}
In this case $A_n\le N\le S_n$. Since $[S_n:A_n]=2$, there are no intermediate subgroups
other than the endpoints.
:::

<1>4. If $N\cap A_n=1$, then $N=1$.
::: {.proof}
The composite
\[
N\hookrightarrow S_n\twoheadrightarrow S_n/A_n\cong C_2
\]
has kernel $N\cap A_n=1$, so $N$ embeds in $C_2$. Thus $|N|\le 2$. If $|N|=2$, write
$N=\{1,\tau\}$. Normality forces $g\tau g^{-1}=\tau$ for every $g\in S_n$, so
$\tau\in Z(S_n)$. But $Z(S_n)=1$ for $n\ge 3$: if a nonidentity permutation $\sigma$
moves $i$ to $j\ne i$, choose $k\notin\{i,j\}$; then the transposition $(j\ k)$ does not
commute with $\sigma$. Hence $|N|\ne2$, so $N=1$.
:::

<1>5. Therefore the normal subgroups of $S_n$ are exactly
\[
1,\qquad A_n,\qquad S_n,
\]
and $A_n$ is the unique proper nontrivial normal subgroup.
::: {.proof}
Combine <1>2--<1>4.
:::
:::
