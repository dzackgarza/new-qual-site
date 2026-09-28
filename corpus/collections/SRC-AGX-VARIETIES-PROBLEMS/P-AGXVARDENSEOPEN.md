---
schema: qual/card@1
id: P-AGXVARDENSEOPEN
kind: problem
title: Nonempty Zariski-open subsets of an affine variety are dense
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Density
  - Irreducibility
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 2.7 in the recorded source. It assumes k=C and
    an affine variety X, and asks to show that every nonempty Zariski-open
    subset U of X is dense.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Restored the source's nonempty hypothesis and affine-variety context. The
    imported statement "open sets are dense" was false for the empty open set.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the equivalence between irreducibility and intersection of
    nonempty open subsets, and the closure argument for a nonempty open set.
---

::: {.problem}
Let $X$ be an affine variety over $\CC$. Show that every nonempty Zariski-open
subset $U\subseteq X$ is dense in $X$.
:::

::: {.solution}
<1>1. Any two nonempty Zariski-open subsets of $X$ intersect.

::: {.proof}
An affine variety is irreducible by definition. Let
$$
U,V\subseteq X
$$
be nonempty open subsets. If
$$
U\cap V=\emptyset,
$$
then
$$
X=(X\setminus U)\cup(X\setminus V).
$$
Both complements are proper closed subsets because $U$ and $V$ are nonempty.
This expresses $X$ as the union of two proper closed subsets, contradicting
irreducibility. Hence
$$
U\cap V\neq\emptyset.
$$
:::

<1>2. Every nonempty open subset $U\subseteq X$ satisfies
$$
\boxed{\overline U=X.}
$$

::: {.proof}
Suppose
$$
\overline U\subsetneq X.
$$
Then
$$
V=X\setminus\overline U
$$
is a nonempty open subset of $X$. Since
$$
U\subseteq\overline U,
$$
one has
$$
U\cap V=\emptyset,
$$
contradicting step <1>1. Therefore $\overline U=X$, so $U$ is dense.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is exactly the assertion of the problem.
:::
:::
