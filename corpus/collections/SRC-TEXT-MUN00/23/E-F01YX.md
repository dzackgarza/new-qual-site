---
schema: qual/card@1
id: E-F01YX
kind: problem
title: Arbitrary products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 10, printed p. 152, with Theorem
    23.3, Theorem 23.4 and Theorem 23.6; the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.10, PDF p. 3. The subspace of points fixed off
    a finite set of coordinates is homeomorphic to a finite product, hence connected; their
    union is connected since they share the base point; and the union is dense because a
    product basis element constrains only finitely many coordinates, so Theorem 23.4
    applies. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps covering the three parts, each carrying a `pf-proof`; the claims are the
    prose's own and the published-solution attribution is kept above the proof. Cited by number
    only: Munkres Theorem 23.6 (a finite product of connected spaces is connected), Theorem
    23.3 (a union of connected subspaces with a common point is connected) and Theorem 23.4
    (a space between a connected subspace and its closure is connected). Checked: that the
    restriction of the projection is a homeomorphism onto the finite product, that $\mathbf a$
    lies in every $X_K$, and that the point $\mathbf y$ of step 4 lies in both $X_K$ and the
    given basis element.
---

::: {.exercise}

Let $\theset{X_\alpha}_{\alpha \in J}$ be an indexed family of connected spaces; let $X$ be the product space

$$
X = \prod_{\alpha \in J} X_\alpha.
$$

Let $\mathbf{a} = (a_\alpha)$ be a fixed point of $X$.

(a) Given any finite subset $K$ of $J$, let $X_K$ denote the subspace of $X$ consisting of all points $\mathbf{x} = (x_\alpha)$ such that $x_\alpha = a_\alpha$ for $\alpha \notin K$.
Show that $X_K$ is connected.

(b) Show that the union $Y$ of the spaces $X_K$ is connected.

(c) Show that $X$ equals the closure of $Y$; conclude that $X$ is connected.
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs.

Let $X=\prod_{\alpha\in J}X_{\alpha}$ with each $X_{\alpha}$ connected, fix $\mathbf{a}\in X$, and for finite $K\subset J$ let $X_{K}=\{\mathbf{x}\mid x_{\alpha}=a_{\alpha}\ \text{for}\ \alpha\notin K\}$.

::: pf

::: pf-step

(a) If $K=\{\alpha_{1},\dots,\alpha_{n}\}$, the map $X_{K}\to X_{\alpha_{1}}\times\cdots\times X_{\alpha_{n}}$, $\mathbf{x}\mapsto(x_{\alpha_{1}},\dots,x_{\alpha_{n}})$, is a homeomorphism.

::: pf-proof

The map is the restriction to $X_K$ of the projection of $X$ onto the coordinates in $K$, hence continuous. It is injective because a point of $X_K$ is determined by those $n$ coordinates, the other coordinates being fixed at $a_\alpha$, and it is surjective because any $(x_{\alpha_1},\dots,x_{\alpha_n})$ extends to a point of $X_K$ by setting $x_\alpha=a_\alpha$ off $K$. The inverse, inserting the $a_\alpha$ in the other coordinates, is continuous because each of its coordinate functions is either a projection or constant. So the map is a bijective continuous map with continuous inverse.

:::

:::

::: pf-step

The finite product $X_{\alpha_{1}}\times\cdots\times X_{\alpha_{n}}$ is connected, hence so is $X_{K}$.

::: pf-proof

A finite product of connected spaces is connected (Munkres, Theorem 23.6), applied $n-1$ times to the binary products. By step 1, $X_K$ is homeomorphic to it, and connectedness is a topological property.

:::

:::

::: pf-step

(b) All the $X_{K}$ contain $\mathbf{a}$, so their union $Y$ is connected.

::: pf-proof

A point of $X_K$ agrees with $a_\alpha$ off $K$; the point $\mathbf{a}$ agrees everywhere, so $\mathbf{a}\in X_K$ for every $K$, including $K=\varnothing$. A union of connected subspaces that have a point in common is connected (Munkres, Theorem 23.3), applied to the family $\{X_K\}$.

:::

:::

::: pf-step

(c) Let $\mathbf{x}\in X$ and let $U=\prod U_{\alpha}$ be a product basis element containing $\mathbf{x}$, with $U_{\alpha}=X_{\alpha}$ except for $\alpha\in K$, $K$ finite. Then $\mathbf{y}$, defined by $y_{\alpha}=x_{\alpha}$ for $\alpha\in K$ and $y_{\alpha}=a_{\alpha}$ otherwise, lies in $X_{K}\subset Y$ and in $U$.

::: pf-proof

A basis element of the product topology constrains only finitely many coordinates, which is the finite set $K$; off $K$ we have $U_\alpha=X_\alpha$ and $a_\alpha\in X_\alpha$. On $K$ the point $\mathbf y$ copies $\mathbf x$, so $y_\alpha=x_\alpha\in U_\alpha$ there; off $K$ it satisfies $y_\alpha=a_\alpha\in X_\alpha=U_\alpha$. Hence $\mathbf y\in U$, and $\mathbf y\in X_K$ by its definition.

:::

:::

::: pf-step

So every neighbourhood of $\mathbf{x}$ meets $Y$ and $\mathbf{x}\in\overline Y$; hence $X=\overline Y$.

::: pf-proof

Step 4 produces, inside any basis element $U$ containing $\mathbf x$, a point $\mathbf y\in Y$. A point of the closure of $Y$ is exactly a point every neighbourhood of which meets $Y$, so $\mathbf x\in\overline Y$; and $\mathbf x$ was arbitrary, so $X\subseteq\overline Y\subseteq X$.

:::

:::

::: pf-step

By Theorem 23.4, with $Y\subset X\subset\overline Y$, the space $X$ is connected, and the three parts are proved.

::: pf-proof

$Y$ is connected by step 3, and $Y\subseteq X\subseteq\overline Y$ by the definition of $Y$ and step 5. Munkres, Theorem 23.4 says that if $Y$ is connected and $Y\subseteq Z\subseteq\overline Y$ then $Z$ is connected; with $Z=X$ this gives that $X$ is connected. Part (a) is steps 1--2, part (b) is step 3, and part (c) is steps 4--6.

:::

:::

:::
:::
