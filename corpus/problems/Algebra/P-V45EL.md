---
schema: qual/card@1
id: P-V45EL
kind: problem
title: Representations of a finite $p$-group on a vector space over a finite field of characteristic $p$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - p-Groups
  - Characteristic
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite $p$-group and let $V$ be a nonzero finite-dimensional vector space over a finite field $k$ of characteristic $p$. What can be said about a representation
$$
G\to \GL(V)?
$$
:::

::: {.solution}

::: pf

::: {.pf-step #fixed}

Every such representation has a nonzero fixed vector: $V^G\ne0$.

::: pf-proof

Let $G$ act on the finite set $V$. Every orbit has size dividing $\abs{G}$, a power of $p$, so every orbit of size greater than $1$ has cardinality divisible by $p$. Therefore $\abs{V}\equiv \abs{V^G}\pmod p$. Since $\abs{V}=\abs{k}^{\dim V}$ is divisible by $p$, $\abs{V^G}\equiv0\pmod p$. The zero vector is fixed, so $\abs{V^G}\ge p$ and there is a nonzero fixed vector.

:::

:::

::: pf-step

Every irreducible $k$-representation of $G$ is the trivial one-dimensional representation.

::: pf-proof

If $V$ is irreducible, then $V^G$ is a $G$-stable subspace, nonzero by step [](#fixed){.pf-ref}, so $V^G=V$ and $G$ acts trivially. Every subspace is then $G$-stable, so irreducibility forces $\dim_kV=1$.

:::

:::

::: pf-step

Every finite-dimensional representation $V$ has a filtration $0=V_0\subset V_1\subset\cdots\subset V_n=V$ by $G$-stable subspaces whose successive quotients are trivial one-dimensional representations.

::: pf-proof

Induct on $\dim V$. By step [](#fixed){.pf-ref}, choose a nonzero fixed vector $v$ and let $V_1=kv$. Apply the induction hypothesis to $V/V_1$ and take preimages in $V$.

:::

:::

:::

:::
