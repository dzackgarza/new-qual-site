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

Prove the Borsuk-Ulam theorem: that if $n > m \geq 1$, then there is no map $g : S^n \to S^m$ which satisfies $g(-x) = -g(x)$ for all $x$.

::: {.solution}
<1>1. Suppose an antipodal-equivariant map $g:S^n\to S^m$ existed, with $n>m\ge1$.
::: {.proof}
We derive a contradiction.
:::

<1>2. The map descends to
$$
\bar g:\mathbb{RP}^n\to\mathbb{RP}^m.
$$
::: {.proof}
The relation $g(-x)=-g(x)$ means that $g$ maps antipodal orbits to antipodal orbits.
:::

<1>3. The induced map on fundamental groups is nontrivial, hence an isomorphism
$$
\bar g_*:\mathbb Z/2\to\mathbb Z/2.
$$
::: {.proof}
A generator of $\pi_1(\mathbb{RP}^n)$ lifts to a path in $S^n$ from $x$ to $-x$. Its image under $g$ is a path from $g(x)$ to $-g(x)$, which projects to the nontrivial loop in $\mathbb{RP}^m$. Thus the generator maps to the generator.
:::

<1>4. If $u\in H^1(\mathbb{RP}^m;\mathbb F_2)$ and $v\in H^1(\mathbb{RP}^n;\mathbb F_2)$ are the standard generators, then
$$
\bar g^*(u)=v.
$$
::: {.proof}
Degree-$1$ mod-$2$ cohomology is $\operatorname{Hom}(\pi_1,\mathbb F_2)$ here, and <1>3 shows the induced homomorphism is nonzero.
:::

<1>5. But
$$
0=\bar g^*(u^{m+1})=v^{m+1},
$$
which is impossible.
::: {.proof}
The cohomology rings are
$$
H^*(\mathbb{RP}^r;\mathbb F_2)\cong\mathbb F_2[t]/(t^{r+1}).
$$
Thus $u^{m+1}=0$ in the target, while $v^{m+1}\ne0$ in $H^{m+1}(\mathbb{RP}^n;\mathbb F_2)$ because $m+1\le n$.
:::

<1>6. Hence no antipodal-equivariant map $S^n\to S^m$ exists when $n>m\ge1$.
::: {.proof}
The supposition in <1>1 leads to the contradiction in <1>5.
:::
:::
