---
schema: qual/card@1
id: E-HAT-1.A-9
kind: problem
title: Index $n$ subgroup has at most $n$ conjugates; existence of normal subgroup of finite index contained in $H$
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used monodromy on the n-sheeted fiber to identify conjugates with point stabilizers, and the kernel/core to obtain a finite-index normal subgroup.
---

::: {.problem}
Using covering spaces, show that an index $n$ subgroup $H$ of a group $G$ has at most $n$ conjugate subgroups $gHg^{-1}$ in $G$.
Apply this to show that there exists a normal subgroup $K \subset G$ of finite index with $K \subset H$.
[For the latter statement, consider the intersection of all the conjugate subgroups $gHg^{-1}$. This is the maximal normal subgroup of $G$ contained in $H$.]
:::

::: {.solution}
Let $H\le G$ have index $n$.
Regard $G$ as the fundamental group of a connected CW complex and let
\[
p:\widetilde X_H\to X
\]
be the connected covering corresponding to $H$.
Its fiber over the basepoint has $n$ points and can be identified with the coset set $G/H$.

::: pf

::: {.pf-step #s1}

The conjugates of $H$ are precisely the stabilizers of points of the transitive $G$-set $G/H$.

::: pf-proof

For the left action of $G$ on $G/H$, the stabilizer of the coset $gH$ is
\[
\operatorname{Stab}(gH)
=\{k\in G:kgH=gH\}
=gHg^{-1}.
\]
In covering-space language, changing the chosen lift of the basepoint from the point corresponding to $H$ to the point corresponding to $gH$ changes the associated subgroup by conjugation to $gHg^{-1}$.

:::

:::

::: {.pf-step #s2}

Hence $H$ has at most $n$ distinct conjugate subgroups.

::: pf-proof

There are exactly $n$ points in $G/H$ and therefore at most $n$ distinct point stabilizers. By step [](#s1){.pf-ref} these are the conjugates of $H$.

:::

:::

::: {.pf-step #s3}

Let
\[
K=\bigcap_{g\in G}gHg^{-1}.
\]
Then $K$ is normal in $G$ and $K\subseteq H$.

::: pf-proof

Containment in $H$ follows from the term $g=1$.
For $a\in G$,
\[
aKa^{-1}
=\bigcap_{g\in G}agHg^{-1}a^{-1}
=\bigcap_{u\in G}uHu^{-1}
=K,
\]
where $u=ag$ ranges over all of $G$.
Thus $K\trianglelefteq G$.

:::

:::

::: {.pf-step #s4}

The subgroup $K$ has finite index in $G$.

::: pf-proof

By step [](#s2){.pf-ref} only finitely many distinct conjugates of $H$ occur, say
\[
H_1,\dots,H_r,
\qquad r\le n.
\]
Each has index $n$.
The diagonal map
\[
G/(H_1\cap\cdots\cap H_r)
\longrightarrow
\prod_{i=1}^r G/H_i,
\qquad
gK\longmapsto(gH_1,\dots,gH_r)
\]
is injective.
Therefore
\[
[G:K]\le\prod_{i=1}^r[G:H_i]=n^r<\infty.
\]
Equivalently, $K$ is the kernel of the monodromy homomorphism
\[
G\longrightarrow\operatorname{Sym}(G/H)\cong S_n,
\]
so in fact $[G:K]\le n!$.

:::

:::

::: pf-step

Thus there is a finite-index normal subgroup
\[
\boxed{K\trianglelefteq G,\qquad K\subseteq H.}
\]

::: pf-proof

Combine steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
