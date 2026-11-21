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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §79 Exercise 7, printed p. 484. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-1527760-E-UYQU1.md, read whole.
    Math StackExchange 1527760, asked by Empiromancer on 2015-11-13, has one answer, 1527797 by Tsemo
    Aristide (2015-11-13), which proves the exercise under the exercise's hypotheses: p(m(x,y)) = 1_G because
    G is abelian, so the commutator map lands in the fibre of the identity, which is discrete, and the domain
    is connected, so the map is constant at the identity. That proof is the card's, and the card now says so
    with its URL; its steps add the path-connected version of the connectedness argument (the chapter's
    convention, printed p. 477, gives path connectedness, which the answer does not use) and prove the
    discreteness of the fibre and the multiplication's continuity from the book. Nothing in the answer is
    wrong or assumes more than Munkres does.
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

The argument is that of Tsemo Aristide, answer 1527797 (https://math.stackexchange.com/a/1527797), posted 2015-11-13 to Math Stack Exchange question 1527760, "Covering space of an abelian topological group is abelian if the covering map is a homomorphism" (https://math.stackexchange.com/questions/1527760, asked by Empiromancer on the same day), in three sentences: the commutator map $m:\overline G\times\overline G\to\overline G$ has image in $p^{-1}(e)$, which is discrete, and since $\overline G$ is connected its image is connected, hence the identity. The steps below write that argument out, using the path connectedness that the Convention of Chapter 13 gives in place of connectedness, so that the path argument replaces "the image of a connected set is connected"; the discreteness of the fibre, the identification of $p\circ\phi$ with the commutator in $G$, and the conclusion are the answer's.

::: pf

::: {.pf-step #commutator}

The commutator map
$$
\phi:\overline G\times\overline G\to\overline G,\qquad \phi(x,y)=xyx^{-1}y^{-1}
$$
is continuous.

::: {.pf-proof}

Multiplication $\overline G\times\overline G\to\overline G$ and inversion $\overline G\to\overline G$ are continuous by the definition of a topological group (supplementary exercises of §22), and a composite of continuous maps is continuous.

:::

:::

::: {.pf-step #fibre}

The fibre $p^{-1}(e)$ is a discrete subspace of $\overline G$, and $p\circ\phi$ is the constant map at $e$.

::: {.pf-proof}

::: {.pf-step}

Every point of $p^{-1}(e)$ is isolated in $p^{-1}(e)$.

::: {.pf-proof}

Since $p$ is a covering map, $e$ has an open neighbourhood $U$ evenly covered by $p$ (Definition of a covering map, §53): $p^{-1}(U)$ is the disjoint union of open slices $V_\alpha$, each mapped homeomorphically onto $U$ by $p$. A slice $V_\alpha$ meeting $p^{-1}(e)$ meets it in exactly one point, because $p\restrict_{V_\alpha}$ is injective, so $V_\alpha$ is an open neighbourhood of that point in $\overline G$ meeting $p^{-1}(e)$ in that point alone.

:::

:::

::: {.pf-step}

$p(\phi(x,y))=e$ for all $x,y\in\overline G$.

::: {.pf-proof}

Because $p$ is a homomorphism (§52, definition of homomorphism),
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

By the Convention of Chapter 13 , $\overline G$ is path connected. Given points $(x,y)$ and $(x',y')$ of $\overline G\times\overline G$, choose paths $\alpha$ from $x$ to $x'$ and $\beta$ from $y$ to $y'$; then $t\mapsto(\alpha(t),\beta(t))$ is a path from $(x,y)$ to $(x',y')$, because a map into a product is continuous when its coordinate functions are.

:::

:::

::: {.pf-step}

A path in a discrete space is constant.

::: {.pf-proof}

Let $\gamma:[0,1]\to D$ be a path with $D$ discrete. Its image is connected, being the image of the connected space $[0,1]$ (Theorem 24.1) under a continuous map (Theorem 23.5). A subspace of a discrete space with more than one point is a separation of itself into two nonempty open singletons, so it is not connected (definition of connectedness, §23); hence $\gamma([0,1])$ is a single point.

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
