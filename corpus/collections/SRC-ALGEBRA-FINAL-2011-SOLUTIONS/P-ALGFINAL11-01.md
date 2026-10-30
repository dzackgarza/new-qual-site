---
schema: qual/card@1
id: P-ALGFINAL11-01
kind: problem
title: Classify groups of order 105
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order $105$.

(a) Show that $G$ has a normal subgroup of order $5$ or $7$.

(b) Show that $G$ has a cyclic normal subgroup of order $35$.

(c) Show that the Sylow $5$- and $7$-subgroups of $G$ are both normal.

(d) Classify groups of order $105$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) A Sylow $5$-subgroup $F$ or a Sylow $7$-subgroup $S$ of $G$ is normal.

::: pf-proof
If $F$ is not normal, the number of Sylow $5$-subgroups is $1+5k>1$ and divides $21$, so it is $21$. Distinct subgroups of order $5$ meet trivially, so $G$ has $21\cdot 4=84$ elements of order $5$. Likewise, if $S$ is not normal, the number of Sylow $7$-subgroups is $1+7k>1$ and divides $15$, so it is $15$, and $G$ has $15\cdot 6=90$ elements of order $7$. As $84+90>105$, $F$ or $S$ is normal.
:::

:::

::: {.pf-step #s2}
(b) $FS$ is a cyclic normal subgroup of order $35$.

::: pf-proof
By step [](#s1){.pf-ref}, one of $F$, $S$ is normal, so $FS$ is a subgroup. As $F\cap S=1$ by Lagrange's theorem, $\cardinality{FS}=35$. A group of order $35$ is cyclic, because $5\nmid 7-1$. The index $[G:FS]=3$ is the smallest prime dividing $\cardinality{G}$, so $FS$ is normal: the action of $G$ on $G/FS$ gives a homomorphism $G\to S_3$ whose image has order dividing $\gcd(105,6)=3$, so its kernel lies in $FS$ and has index $1$ or $3$, and hence equals $FS$.
:::

:::

::: {.pf-step #s3}
(c) $F$ and $S$ are normal in $G$.

::: pf-proof
The cyclic group $FS$ has exactly one subgroup of order $5$ and one of order $7$, so $F$ and $S$ are characteristic in $FS$. A characteristic subgroup of a normal subgroup is normal, so $F,S\trianglelefteq G$ by step [](#s2){.pf-ref}.
:::

:::

::: {.pf-step #s4}
(d) There are exactly two groups of order $105$ up to isomorphism: $\ZZ/105$ and $(\ZZ/7\rtimes\ZZ/3)\times\ZZ/5$.

::: pf-proof
Let $T$ be a Sylow $3$-subgroup. Since $S\trianglelefteq G$, $TS$ is a subgroup of order $21$, and it meets the normal subgroup $F$ trivially, so $G=F\rtimes TS$. As $\cardinality{\Aut(F)}=4$ is prime to $21$, the action $TS\to\Aut(F)$ is trivial, and $G\cong F\times TS$. The groups of order $21$ are $\ZZ/21$ and the nonabelian $\ZZ/7\rtimes\ZZ/3$, because $3\mid 7-1$. This gives the two groups listed, and they are not isomorphic because only the first is abelian.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer (a), (b), (c) and (d).
:::

:::

:::
