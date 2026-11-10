---
schema: qual/card@1
id: P-AGHPRODTOP
kind: problem
title: The Zariski topology on $\AA^2$ against the product topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Products
relations:
- kind: related-to
  target: FE-ISIPR
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.4 (scan page 22
    of the retained PDF). What was checked: the printed text against the card's
    statement — the identification of A^2 with A^1 x A^1 in the natural way and the
    assertion that the Zariski topology on A^2 is not the product topology of the
    two Zariski topologies. The card renders the book's "If we identify ..." as an
    imperative "Identify ...", which states the same thing and changes no
    mathematics; nothing else differs, and the exercise carries no star. No repair
    was needed. What was not checked: the solution was read only for consistency
    with the statement, not re-derived.
---

::: {.problem}
Identify $\AA^2$ with $\AA^1 \times \AA^1$ in the natural way.
Show that the Zariski topology on $\AA^2$ is not the product topology of the Zariski topologies on the two copies of $\AA^1$.
:::

::: {.solution}
The diagonal $\Delta = V(x-y)$ is Zariski closed in $\AA^2$, and it is not closed in the product topology.

Suppose it were.
Then $\AA^2 \sm \Delta$ is open in the product, so it contains a basic box $U \times V$ around each of its points.
On $\AA^1$ the Zariski topology is cofinite, so $U = \AA^1 \sm \theset{p_1,\ldots,p_m}$ and $V = \AA^1 \sm \theset{q_1,\ldots,q_n}$.
Over an infinite field pick $z$ distinct from every $p_i$ and $q_j$; then $(z,z)$ lies in $U \times V$ and on $\Delta$, contradicting $U \times V \subseteq \AA^2 \sm \Delta$.

:::

::: {.remark}
Erratum: an alternative argument sometimes given uses the hyperbola $V(xy-1)$, whose projection $\pi_x(V(xy-1)) = \AA^1 \sm \theset{0}$ is not closed, and claims that projections would be closed maps if $\AA^2$ had the product topology.
Projections from a product topology are open maps but need not be closed, so that argument does not work.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.4, PDF p. 1, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.4, PDF p. 2: both take the diagonal $Z(x-y)$, closed in $\AA^2$ and not closed in the product, Park by listing the closed sets of the product as finite unions of sets of the form $V_1\times V_2$ with each $V_i$ empty, finite or everything.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.4, PDF p. 2, argues that every closed set of $\AA^1\times\AA^1$ is finite, which is false — $\AA^1\times\{b\}$ is an infinite closed set of the product — and then uses that $Z(y-x)$ is infinite.
The proof above uses the diagonal as all three do, and instead of comparing against a list of closed sets it intersects a basic open box around a point off the diagonal with the diagonal, which is the missing argument in the argument Borcherds and Troiani leave at one sentence.
Agree with Borcherds and Park, and agree with Troiani's example and conclusion but not with its reason.
:::
