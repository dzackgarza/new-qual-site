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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with three steps, each carrying a `pf-proof`, and the two remarks that follow the proof are
    kept verbatim outside it. The diagonal counterexample and both remarks are unchanged. Cited
    by number only: Exercise I.1.1 of the book for the closed sets of $\AA^1$ being the finite
    ones, and the definition of the product topology. Checked: that a nonempty Zariski-open
    subset of $\AA^1$ is the complement of a finite set, and that a $z$ avoiding finitely many
    values exists over an infinite field.
---

::: {.problem}
Identify $\AA^2$ with $\AA^1 \times \AA^1$ in the natural way.
Show that the Zariski topology on $\AA^2$ is not the product topology of the Zariski topologies on the two copies of $\AA^1$.
:::

::: {.solution}

::: pf

::: pf-step

The diagonal $\Delta=V(x-y)$ is Zariski closed in $\AA^2$, and it is not closed in the product topology on $\AA^1\times\AA^1$.

::: pf-proof

$x-y$ is a polynomial, so its zero set is Zariski closed. For the second claim it suffices, by the definition of the product topology, to show that no basic open box $U\times V$ contained in the complement of $\Delta$ can contain a point of the complement: the complement is then not open in the product topology.

:::

:::

::: pf-step

Suppose $\Delta$ were closed in the product topology. Then $\AA^2\setminus\Delta$ is open in the product, so it contains a basic box $U\times V$ around each of its points. On $\AA^1$ the Zariski topology is cofinite, so $U=\AA^1\setminus\{p_1,\dots,p_m\}$ and $V=\AA^1\setminus\{q_1,\dots,q_n\}$.

::: pf-proof

If $\Delta$ were closed, its complement would be open; a basic open set of the product is a product $U\times V$ of nonempty open subsets of the factors, and a nonempty open subset of $\AA^1$ in the Zariski topology is the complement of a finite set, because the closed sets of $\AA^1$ are the finite sets and $\AA^1$ itself (the zero sets of polynomials in one variable, Hartshorne Exercise I.1.1).

:::

:::

::: pf-step

Over an infinite field pick $z$ distinct from every $p_i$ and $q_j$; then $(z,z)$ lies in $U\times V$ and on $\Delta$, contradicting $U\times V\subseteq\AA^2\setminus\Delta$. Hence the Zariski topology on $\AA^2$ is not the product topology.

::: pf-proof

The field is infinite, so only finitely many values $p_1,\dots,p_m,q_1,\dots,q_n$ are excluded and a $z$ outside them exists. Then $z\in U$ and $z\in V$, so $(z,z)\in U\times V$, while $z-z=0$ shows $(z,z)\in V(x-y)=\Delta$; that contradicts $U\times V\subseteq\AA^2\setminus\Delta$. Since the diagonal is Zariski closed and not product-closed, the two topologies differ.

:::

:::

:::
:::

::: {.remark}
Erratum: an alternative argument sometimes given uses the hyperbola $V(xy-1)$, whose projection $\pi_x(V(xy-1)) = \AA^1 \sm \theset{0}$ is not closed, and claims that projections would be closed maps if $\AA^2$ had the product topology.
Projections from a product topology are open maps but need not be closed, so that argument does not work.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.4, text version `tmp/sources/hartshorne-solutions-borcherds.md`, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.4, text version `tmp/sources/hartshorne-solutions-park.md`: both take the diagonal $Z(x-y)$, closed in $\AA^2$ and not closed in the product, Park by listing the closed sets of the product as finite unions of sets of the form $V_1\times V_2$ with each $V_i$ empty, finite or everything.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.4, text version `tmp/sources/hartshorne-solutions-troiani.md`, argues that every closed set of $\AA^1\times\AA^1$ is finite, which is false — $\AA^1\times\{b\}$ is an infinite closed set of the product — and then uses that $Z(y-x)$ is infinite.
The proof above uses the diagonal as all three do, and instead of comparing against a list of closed sets it intersects a basic open box around a point off the diagonal with the diagonal, which is the missing argument in the argument Borcherds and Troiani leave at one sentence.
Agree with Borcherds and Park, and agree with Troiani's example and conclusion but not with its reason.
:::
