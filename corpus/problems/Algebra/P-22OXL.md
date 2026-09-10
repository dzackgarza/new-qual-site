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
Let $n\ge5$. Show that $A_n$ is the unique proper nontrivial normal subgroup of $S_n$.
:::


::: {.solution}
Let $N\trianglelefteq S_n$ be proper and nontrivial.

<1>1. The intersection $N\cap A_n$ is a normal subgroup of $A_n$.
::: {.proof}
Both $N$ and $A_n$ are normal in $S_n$. Hence $N\cap A_n$ is normal in $S_n$, and therefore in the subgroup $A_n$.
:::

<1>2. Since $A_n$ is simple for $n\ge5$, either
\[
N\cap A_n=\{e\}
\qquad\text{or}\qquad
N\cap A_n=A_n.
\]
::: {.proof}
For $n\ge5$, the alternating group $A_n$ is nonabelian simple, so its only normal subgroups are $\{e\}$ and $A_n$. Apply this to <1>1.
:::

<1>3. If $N\cap A_n=A_n$, then $N=A_n$.
::: {.proof}
The equality says $A_n\subseteq N$. Since $[S_n:A_n]=2$, there is no subgroup strictly between $A_n$ and $S_n$. Thus $N=A_n$ or $N=S_n$. Because $N$ is proper, $N=A_n$.
:::

<1>4. The case $N\cap A_n=\{e\}$ is impossible.
::: {.proof}
Restrict the sign homomorphism
\[
\operatorname{sgn}:S_n\to\{\pm1\}
\]
to $N$. Its kernel is
\[
N\cap\ker(\operatorname{sgn})=N\cap A_n=\{e\},
\]
so $N$ embeds in a group of order $2$. Since $N$ is nontrivial, $|N|=2$.

A normal subgroup of order $2$ is central: if $N=\{e,z\}$, conjugation by any element of $S_n$ must preserve the unique nonidentity element $z$, so $gz=zg$ for every $g\in S_n$. Thus $z\in Z(S_n)$.

But $Z(S_n)=\{e\}$ for $n\ge3$. Indeed, if a nonidentity permutation $z$ sends $i$ to $j\ne i$, choose $k$ distinct from $i,j$. Then the transposition $(i\ k)$ does not commute with $z$. This contradiction rules out $N\cap A_n=\{e\}$.
:::

<1>5. Therefore $A_n$ is the unique proper nontrivial normal subgroup of $S_n$.
::: {.proof}
By <1>2, only the two cases in <1>3 and <1>4 can occur. The second is impossible, and the first forces $N=A_n$.
:::
:::
