---
schema: qual/card@1
id: P-ALGF24A
kind: problem
title: Group of order $2pq$ has normal subgroups of orders $pq$ and $q$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Compared the statement with Problem 1 on page 2 of the official FA24 algebra exam PDF.
- event: solution-written
  by: gpt-6-astra-pro
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Verified the nontrivial sign character of the regular action and characteristicity of the unique Sylow q-subgroup of its kernel.
---

::: problem
Suppose $p < q$ are odd primes and $G$ is a group of order $2pq$.
Prove that $G$ has two normal subgroups $N_1 \subseteq N_2$ such that $|N_2| = pq$ and $|N_1| = q$.
:::

::: {.solution}
<1>1. The sign of the left regular action defines a surjective homomorphism
\[
\varepsilon:G\longrightarrow\{1,-1\}.
\]
::: {.proof}
For $g\in G$, let $L_g$ be the permutation $h\mapsto gh$ of the underlying set of $G$.
Since $L_{gh}=L_gL_h$, the map $\varepsilon(g)=\operatorname{sgn}(L_g)$ is a homomorphism.

There is an element $t\ne1$ with $t^2=1$: otherwise the $2pq-1$ nonidentity elements would partition into two-element sets $\{g,g^{-1}\}$, contradicting their odd number.
The permutation $L_t$ has no fixed points, since $th=h$ would imply $t=1$, and $L_t^2$ is the identity.
It is therefore a product of $pq$ disjoint transpositions.
As $pq$ is odd,
\[
\varepsilon(t)=(-1)^{pq}=-1,
\]
so $\varepsilon$ is surjective.
:::

<1>2. The subgroup $N_2=\ker\varepsilon$ is normal in $G$ and has order $pq$.
::: {.proof}
A kernel is normal, and surjectivity in <1>1 gives $[G:N_2]=2$.
Hence $|N_2|=|G|/2=pq$.
:::

<1>3. The unique Sylow $q$-subgroup $N_1$ of $N_2$ is normal in $G$ and has order $q$.
::: {.proof}
By the Sylow theorems, the number $n_q$ of Sylow $q$-subgroups of $N_2$ satisfies
\[
n_q\mid p,\qquad n_q\equiv1\pmod q.
\]
Its only possible values are $1$ and $p$.
Since $1<p<q$, the second value is not congruent to $1$ modulo $q$.
Thus $n_q=1$; write $N_1$ for this unique subgroup, which has order $q$.

For every $g\in G$, normality of $N_2$ implies that $gN_1g^{-1}$ is a subgroup of $N_2$ of order $q$.
Uniqueness forces $gN_1g^{-1}=N_1$.
Therefore $N_1\trianglelefteq G$, and $N_1\subseteq N_2$ gives the required pair.
:::
:::
