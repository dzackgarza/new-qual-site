---
schema: qual/card@1
id: P-AGH412POLESATFINITESET
kind: problem
title: A rational function with poles at a prescribed finite set of points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Linear Systems
  - Divisors
relations: []
review: draft
---

::: {.problem}
Again let $X$ be a curve, and let $P_1, \ldots, P_r \in X$ be points. Then there is a rational function $f \in K(X)$ having poles (of some order) at each of the $P_i$, and regular elsewhere.
:::

::: {.solution}
Let $g$ be the genus of $X$, let $D=P_1+\cdots+P_r$, and let $L(E)=\{f\in K(X) \st f=0 \text{ or } (f)+E\ge0\}$, so that $\ell(E)=\dim_k L(E)$.

::: pf

::: {.pf-step #s1}

Fix $n$ with $n-1>2g-2$. For each $i$, there is $f_i\in L(nD)$ with a pole of order exactly $n$ at $P_i$.

::: pf-proof

The divisors $nD$ and $nD-P_i$ both have degree greater than $2g-2$, so by Riemann-Roch and the vanishing of $\ell(K-E)$ for $\deg E>2g-2$,
$$
\ell(nD)-\ell(nD-P_i)=(rn+1-g)-(rn-1+1-g)=1.
$$
An element $f_i\in L(nD)\setminus L(nD-P_i)$ has $v_{P_i}(f_i)\ge -n$ but not $v_{P_i}(f_i)\ge -n+1$, so $v_{P_i}(f_i)=-n$.

:::

:::

::: {.pf-step #s2}

Some $f\in L(nD)$ has a pole of order exactly $n$ at every $P_i$.

::: pf-proof

For each $i$, the set $H_i=L(nD-P_i)$ is a subspace of $L(nD)$, and it is proper by step [](#s1){.pf-ref}. A vector space over the infinite field $k$ is not a union of finitely many proper subspaces, so there is $f\in L(nD)$ outside $H_1\cup\cdots\cup H_r$. As in step [](#s1){.pf-ref}, $v_{P_i}(f)=-n$ for every $i$.

:::

:::

::: pf-qed

The function $f$ of step [](#s2){.pf-ref} satisfies $(f)+nD\ge0$, so it is regular at every point outside $\{P_1,\ldots,P_r\}$, and it has a pole at each $P_i$.

:::

:::

:::
