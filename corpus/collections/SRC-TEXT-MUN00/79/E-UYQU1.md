---
schema: qual/card@1
id: E-UYQU1
kind: problem
title: Covering homomorphisms of abelian topological groups
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 79 Exercise 7, printed p. 484. The commutator map of the cover lands in the discrete fibre over e and has connected domain, hence is constant. Checked against the definition of a covering map (the fibre is discrete, printed p. 336) and the convention of p. 478 that the spaces are connected. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Every step now cites Munkres by number and page: the definition of a covering map and of a slice (printed p. 336), the definition of a topological group in the supplementary exercises of §22 (printed p. 145), the Convention of Chapter 13 (printed p. 477), Theorem 23.5 (printed p. 150) that the image of a connected space is connected, and Theorem 24.1 (printed p. 153) that [0,1] is connected. Corrected: the old proof spoke of "the connected set phi(G x G)" without establishing that phi(G x G) is connected -- G x G being connected is what makes its image connected, and neither was cited; the proof now derives constancy of phi from paths in G x G, which is where connectedness enters. The page of the Convention was also given as p. 478 in the previous note, and it is p. 477. The Lamport block structure was rebuilt: the old version had steps whose proofs were steps with no proof of their own. What the certificate does not cover: the continuity of the group operations is the definition of a topological group, not re-proved here.
---

::: {.exercise}

Let $p: \overline{G} \to G$ be a homomorphism of topological groups that is a covering map.
As throughout this chapter, $\overline G$ and $G$ are path connected and locally path connected.
Show that if $G$ is abelian, so is $\overline{G}$.

:::

::: {.solution}

::: pf

::: {.pf-step #commutator}

The commutator map
$$
\phi:\overline G\times\overline G\to\overline G,\qquad \phi(x,y)=xyx^{-1}y^{-1}
$$
is continuous.

::: {.pf-proof}

Multiplication $\overline G\times\overline G\to\overline G$ and inversion $\overline G\to\overline G$ are continuous by the definition of a topological group (supplementary exercises of §22, printed p. 145), and a composite of continuous maps is continuous.

:::

:::

::: {.pf-step #fibre}

The fibre $p^{-1}(e)$ is a discrete subspace of $\overline G$, and $p\circ\phi$ is the constant map at $e$.

::: {.pf-proof}

::: {.pf-step}

Every point of $p^{-1}(e)$ is isolated in $p^{-1}(e)$.

::: {.pf-proof}

Since $p$ is a covering map, $e$ has an open neighbourhood $U$ evenly covered by $p$ (Definition of a covering map, printed p. 336): $p^{-1}(U)$ is the disjoint union of open slices $V_\alpha$, each mapped homeomorphically onto $U$ by $p$. A slice $V_\alpha$ meeting $p^{-1}(e)$ meets it in exactly one point, because $p|_{V_\alpha}$ is injective, so $V_\alpha$ is an open neighbourhood of that point in $\overline G$ meeting $p^{-1}(e)$ in that point alone.

:::

:::

::: {.pf-step}

$p(\phi(x,y))=e$ for all $x,y\in\overline G$.

::: {.pf-proof}

Because $p$ is a homomorphism (p. 330, definition of homomorphism),
$$
p(\phi(x,y))=p(x)p(y)p(x)^{-1}p(y)^{-1}=[p(x),p(y)],
$$
and $[p(x),p(y)]=e$ because $G$ is abelian. So $\phi(\overline G\times\overline G)\subseteq p^{-1}(e)$.

:::

:::

:::

:::

::: {.pf-step #constant}

$\phi$ is constant.

::: {.pf-proof}

::: {.pf-step}

$\overline G\times\overline G$ is path connected.

::: {.pf-proof}

By the Convention of Chapter 13 (printed p. 477), $\overline G$ is path connected. Given points $(x,y)$ and $(x',y')$ of $\overline G\times\overline G$, choose paths $\alpha$ from $x$ to $x'$ and $\beta$ from $y$ to $y'$; then $t\mapsto(\alpha(t),\beta(t))$ is a path from $(x,y)$ to $(x',y')$, because a map into a product is continuous when its coordinate functions are.

:::

:::

::: {.pf-step}

A path in a discrete space is constant.

::: {.pf-proof}

Let $\gamma:[0,1]\to D$ be a path with $D$ discrete. Its image is connected, being the image of the connected space $[0,1]$ (Theorem 24.1, printed p. 153) under a continuous map (Theorem 23.5, printed p. 150). A subspace of a discrete space with more than one point is a separation of itself into two nonempty open singletons, so it is not connected (definition of connectedness, §23); hence $\gamma([0,1])$ is a single point.

:::

:::

:::

:::

::: {.pf-step}

$\overline G$ is abelian.

::: {.pf-proof}

Given $x,y\in\overline G$, the path $t\mapsto\phi(\alpha(t),\beta(t))$ for any paths in $\overline G$ from $x$ and $y$ to the identity $\tilde e$ lies in the discrete space $p^{-1}(e)$ by step [](#fibre){.pf-ref}, so it is constant by step [](#constant){.pf-ref} and its two end values agree:
$$
\phi(x,y)=\phi(\tilde e,\tilde e)=\tilde e .
$$
Thus $xyx^{-1}y^{-1}=\tilde e$, that is, $xy=yx$, for all $x,y\in\overline G$.

:::

:::

:::

:::
