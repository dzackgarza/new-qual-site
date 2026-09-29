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

::: pf

::: {.pf-step #s1}

Let $a\in H^1(\mathbb{RP}^n;\mathbb F_2)$ be the standard generator. Then
$$
H^*(\mathbb{RP}^n;\mathbb F_2)\cong\mathbb F_2[a]/(a^{n+1}),
$$
so $a^n\ne0$.

::: pf-proof

This is the standard mod-$2$ cohomology ring of real projective space.

:::

:::

::: {.pf-step #s2}

If $A\subset\mathbb{RP}^n$ is contractible, then $a|_A=0$.

::: pf-proof

Positive-degree cohomology of a contractible space vanishes.

:::

:::

::: {.pf-step #s3}

If a space is covered by $k$ closed subsets $A_1,\dots,A_k$ on each of which classes $u_1,\dots,u_k$ respectively restrict to zero, then
$$
u_1\smile\cdots\smile u_k=0.
$$

::: pf-proof

For each $i$, exactness for the pair gives a relative lift $\widetilde u_i\in H^*(X,A_i)$. Their relative cup product lies in
$$
H^*(X,A_1\cup\cdots\cup A_k)=H^*(X,X)=0,
$$
and maps to the absolute product.

:::

:::

::: {.pf-step #s4}

If $\mathbb{RP}^n$ were covered by $k\le n$ contractible closed subsets, then $a^k=0$.

::: pf-proof

Apply steps [](#s2){.pf-ref} and [](#s3){.pf-ref} with $u_i=a$.

:::

:::

::: pf-step

But $a^k\ne0$ for every $k\le n$. Therefore
$$
\boxed{k>n}.
$$

::: pf-proof

The powers $1,a,\dots,a^n$ are nonzero in the ring from step [](#s1){.pf-ref}, contradicting step [](#s4){.pf-ref}.

:::

:::

:::

:::
