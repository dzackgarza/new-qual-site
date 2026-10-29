---
schema: qual/card@1
id: E-O73XQ
kind: problem
title: $G/Z(G)$ cyclic implies $G$ abelian; $G/N$ abelian iff $[G,G]\le N$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Commutators
  - Normal Subgroups
relations: []
review: draft
---

::: {.exercise}
(a) Show that if $G/Z(G)$ is cyclic then $G$ is abelian.

(b) Show that $G/N$ is abelian iff $[G, G] \leq N$.

(c) Show that normal subgroups are not necessarily contained in $Z(G)$.
:::

::: {.hint}
For (c), consider the subgroup of order $3$ in $S_3$.
:::

::: {.solution}
In (b), $N$ is a normal subgroup of $G$.

::: pf

::: pf-step
(a) If $G/Z(G)$ is cyclic, then $G$ is abelian.

::: pf-proof
Write $Z=Z(G)$ and $G/Z=\generators{xZ}$. For $a,b\in G$ there are integers $n,m$ and $h_1,h_2\in Z$ with $a=x^nh_1$ and $b=x^mh_2$. Since $h_1,h_2$ are central and powers of $x$ commute with each other,
$$
ab=x^nh_1x^mh_2=x^{n+m}h_1h_2=x^mh_2x^nh_1=ba.
$$
:::

:::

::: pf-step
(b) $G/N$ is abelian if and only if $[G,G]\le N$.

::: pf-proof
For $a,b\in G$, one has $aNbN=bNaN$ if and only if $a^{-1}b^{-1}ab\in N$. Hence $G/N$ is abelian if and only if every commutator lies in $N$, which holds if and only if the subgroup $[G,G]$ they generate lies in $N$.
:::

:::

::: pf-step
(c) The normal subgroup $A_3\trianglelefteq S_3$ is not contained in $Z(S_3)$.

::: pf-proof
$A_3$ has index $2$, so it is normal. The center of $S_3$ is trivial: a transposition does not commute with a $3$-cycle, and two distinct transpositions do not commute. So $A_3\not\subseteq Z(S_3)=1$.
:::

:::

:::

:::
