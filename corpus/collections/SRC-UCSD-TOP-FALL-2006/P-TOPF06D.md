---
schema: qual/card@1
id: P-TOPF06D
kind: problem
title: "RP^n cannot be covered by fewer than n+1 contractible closed subsets"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Projective Spaces
  - Covering Dimension
relations: []
review: draft
---

::: {.problem}
Assume that $\mathbb{RP}^n$ can be covered by $k$ contractible closed subsets.
Prove that $k > n$.

Hint: Use the mod $2$ cohomology ring structure of $\mathbb{RP}^n$ and the fact that the degree $1$ generator restricts to zero on any contractible subset.
:::

::: {.solution}
<1>1. Let $a\in H^1(\mathbb{RP}^n;\mathbb F_2)$ be the standard generator. Then
$$
H^*(\mathbb{RP}^n;\mathbb F_2)\cong\mathbb F_2[a]/(a^{n+1}),
$$
so $a^n\ne0$.
::: {.proof}
This is the standard mod-$2$ cohomology ring of real projective space.
:::

<1>2. If $A\subset\mathbb{RP}^n$ is contractible, then $a|_A=0$.
::: {.proof}
Positive-degree cohomology of a contractible space vanishes.
:::

<1>3. If a space is covered by $k$ closed subsets $A_1,\dots,A_k$ on each of which classes $u_1,\dots,u_k$ respectively restrict to zero, then
$$
u_1\smile\cdots\smile u_k=0.
$$
::: {.proof}
For each $i$, exactness for the pair gives a relative lift $\widetilde u_i\in H^*(X,A_i)$. Their relative cup product lies in
$$
H^*(X,A_1\cup\cdots\cup A_k)=H^*(X,X)=0,
$$
and maps to the absolute product.
:::

<1>4. If $\mathbb{RP}^n$ were covered by $k\le n$ contractible closed subsets, then $a^k=0$.
::: {.proof}
Apply <1>2--<1>3 with $u_i=a$.
:::

<1>5. But $a^k\ne0$ for every $k\le n$. Therefore
$$
\boxed{k>n}.
$$
::: {.proof}
The powers $1,a,\dots,a^n$ are nonzero in the ring from <1>1, contradicting <1>4.
:::
:::
