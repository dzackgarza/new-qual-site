---
schema: qual/card@1
id: P-HPN6K
kind: problem
title: $\ZZ$
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
  - Homeomorphisms
relations: []
review: draft
---

::: problem
- $\ZZ$

- $\ts{1}$

- $\ts{p \in \ZZ^{\geq 0} \st p\text{ is prime}}$

- $\ts{ {1\over n} \st n\in \ZZ^{\geq 0}}$

- $\ts{ {1\over n} \st n\in \ZZ^{\geq 0}} \union \ts{0}$

- Prove that $\RR^n$ is not homeomorphic to $\RR$ for any $n\geq 2$.

- Is it true that the closure of a product is the product of the closures?
:::

::: {.solution}
<1>1. The first five displayed subsets have no governing instruction in the original migrated source, so that portion of the card is incomplete.
::: {.proof}
The initial migrated version consists of the five bare subsets followed immediately by two independent questions; no request such as “find the closures” or “decide compactness” precedes the list.
:::

<1>2. For every $n\ge2$, $\mathbb R^n$ is not homeomorphic to $\mathbb R$.
::: {.proof}
If $h:\mathbb R^n\to\mathbb R$ were a homeomorphism, then deleting any point $x$ would give a homeomorphism $\mathbb R^n\setminus\{x\}\cong\mathbb R\setminus\{h(x)\}$. For $n\ge2$, $\mathbb R^n\setminus\{x\}$ is path-connected, while $\mathbb R\setminus\{h(x)\}$ has two connected components, a contradiction.
:::

<1>3. For arbitrary subsets $A\subseteq X$ and $B\subseteq Y$,
$$\boxed{\overline{A\times B}^{\,X\times Y}=\overline A^{\,X}\times\overline B^{\,Y}.}$$
::: {.proof}
If $(x,y)$ lies in the left closure, continuity of the projections gives $x\in\overline A$ and $y\in\overline B$. Conversely, if $x\in\overline A$ and $y\in\overline B$, every basic neighborhood $U\times V$ of $(x,y)$ meets $A\times B$ because $U\cap A\ne\varnothing$ and $V\cap B\ne\varnothing$.
:::
:::
