---
schema: qual/card@1
id: P-UCTOP-FA12-7
kind: problem
title: Borsuk-Ulam theorem
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
---

::: {.problem}
Prove the Borsuk-Ulam theorem: that if $n > m \geq 1$, then there is no map $g : S^n \to S^m$ which satisfies $g(-x) = -g(x)$ for all $x$.
:::

::: {.solution}

::: pf

::: {.pf-step #suppose-equivariant-map}
Suppose an antipodal-equivariant map $g:S^n\to S^m$ existed, with $n>m\ge1$.

::: pf-proof
We derive a contradiction.
:::

:::

::: pf-step
The map descends to
$$
\bar g:\mathbb{RP}^n\to\mathbb{RP}^m.
$$

::: pf-proof
The relation $g(-x)=-g(x)$ means that $g$ maps antipodal orbits to antipodal orbits.
:::

:::

::: {.pf-step #pi1-map-isomorphism}
The induced map on fundamental groups is nontrivial, hence an isomorphism
$$
\bar g_*:\mathbb Z/2\to\mathbb Z/2.
$$

::: pf-proof
A generator of $\pi_1(\mathbb{RP}^n)$ lifts to a path in $S^n$ from $x$ to $-x$. Its image under $g$ is a path from $g(x)$ to $-g(x)$, which projects to the nontrivial loop in $\mathbb{RP}^m$. Thus the generator maps to the generator.
:::

:::

::: pf-step
If $u\in H^1(\mathbb{RP}^m;\mathbb F_2)$ and $v\in H^1(\mathbb{RP}^n;\mathbb F_2)$ are the standard generators, then
$$
\bar g^*(u)=v.
$$

::: pf-proof
Degree-$1$ mod-$2$ cohomology is $\operatorname{Hom}(\pi_1,\mathbb F_2)$ here, and step [](#pi1-map-isomorphism){.pf-ref} shows the induced homomorphism is nonzero.
:::

:::

::: {.pf-step #contradiction-reached}
But
$$
0=\bar g^*(u^{m+1})=v^{m+1},
$$
which is impossible.

::: pf-proof
The cohomology rings are
$$
H^*(\mathbb{RP}^r;\mathbb F_2)\cong\mathbb F_2[t]/(t^{r+1}).
$$
Thus $u^{m+1}=0$ in the target, while $v^{m+1}\ne0$ in $H^{m+1}(\mathbb{RP}^n;\mathbb F_2)$ because $m+1\le n$.
:::

:::

::: pf-step
Hence no antipodal-equivariant map $S^n\to S^m$ exists when $n>m\ge1$.

::: pf-proof
The supposition in step [](#suppose-equivariant-map){.pf-ref} leads to the contradiction in step [](#contradiction-reached){.pf-ref}.
:::

:::

:::

:::
