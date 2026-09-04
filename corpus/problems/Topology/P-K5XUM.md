---
schema: qual/card@1
id: P-K5XUM
kind: problem
title: For nonempty $X,Y$, $X\times Y$ is compact iff $X$ and $Y$ are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
  - Tube Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: The UGA Fall 2010 source omits the nonempty-factor hypothesis needed for the converse.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
---

:::{.problem}
Let $X$ and $Y$ be nonempty topological spaces.
Show that $X \cross Y$ is compact if and only if both $X$ and $Y$ are compact.

:::

:::{.concept}
\envlist
- Proof of the tube lemma: 
- Continuous image of compact is compact.
:::


:::{.strategy}
![figures/image_2021-05-21-01-16-52.png](../../assets/figures/image_2021-05-21-01-16-52.png)

Take an open cover of the product, use that vertical fibers are compact to get a finite cover for each fiber.
Use tube lemma to get opens in the base space, run over all $x$ so the tube bases cover $X$.
Use that $X$ is compact to get a finite subcover.

:::


:::{.solution}
<1>1. If $X\times Y$ is compact, then both $X$ and $Y$ are compact.
::: {.proof}
The coordinate projections
\[
\pi_X:X\times Y\to X,
\qquad
\pi_Y:X\times Y\to Y
\]
are continuous.
Because both factors are nonempty, the projections are surjective.
Continuous images of compact spaces are compact, so
\[
X=\pi_X(X\times Y),
\qquad
Y=\pi_Y(X\times Y)
\]
are compact.
:::

<1>2. Suppose $X$ and $Y$ are compact, and let $\mathcal U$ be an open cover of $X\times Y$.
For every $x\in X$, there is an open neighborhood $V_x$ of $x$ such that $V_x\times Y$ is covered by finitely many members of $\mathcal U$.
::: {.proof}
Fix $x\in X$.
The fiber $\{x\}\times Y$ is homeomorphic to the compact space $Y$, so finitely many members
\[
U_{x,1},\ldots,U_{x,m_x}\in\mathcal U
\]
cover it.
Set
\[
W_x=U_{x,1}\cup\cdots\cup U_{x,m_x}.
\]
Then $W_x$ is open in $X\times Y$ and contains $\{x\}\times Y$.
By the tube lemma, there is an open neighborhood $V_x\ni x$ such that
\[
V_x\times Y\subseteq W_x.
\]
Thus the same finitely many $U_{x,j}$ cover $V_x\times Y$.
:::

<1>3. If $X$ and $Y$ are compact, then $X\times Y$ is compact.
::: {.proof}
The family $\{V_x:x\in X\}$ from <1>2 is an open cover of $X$.
Compactness of $X$ gives points $x_1,\ldots,x_r$ such that
\[
X=V_{x_1}\cup\cdots\cup V_{x_r}.
\]
For each $i$, <1>2 supplies finitely many members of $\mathcal U$ covering $V_{x_i}\times Y$.
The union of these finitely many finite subfamilies covers
\[
X\times Y
=\bigcup_{i=1}^r(V_{x_i}\times Y).
\]
Hence $\mathcal U$ has a finite subcover.
:::

<1>4. The nonempty hypothesis is necessary for the implication in <1>1.
::: {.proof}
If $Y=\emptyset$, then $X\times Y=\emptyset$ is compact for every space $X$, including noncompact spaces.
:::

:::
