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
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.10, PDF p. 3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs.

Let $X=\prod_{\alpha\in J}X_{\alpha}$ with each $X_{\alpha}$ connected, fix $\mathbf{a}\in X$, and for finite $K\subset J$ let $X_{K}=\{\mathbf{x}\mid x_{\alpha}=a_{\alpha}\ \text{for}\ \alpha\notin K\}$.

(a) If $K=\{\alpha_{1},\dots,\alpha_{n}\}$, the map $X_{K}\to X_{\alpha_{1}}\times\cdots\times X_{\alpha_{n}}$, $\mathbf{x}\mapsto(x_{\alpha_{1}},\dots,x_{\alpha_{n}})$, is a homeomorphism (it is a bijective continuous map with continuous inverse given by inserting the $a_{\alpha}$). The finite product is connected by Theorem 23.6, hence so is $X_{K}$.

(b) All the $X_{K}$ contain $\mathbf{a}$, so their union $Y$ is connected by Theorem 23.3.

(c) Let $\mathbf{x}\in X$ and let $U=\prod U_{\alpha}$ be a product basis element containing $\mathbf{x}$, with $U_{\alpha}=X_{\alpha}$ except for $\alpha\in K$, $K$ finite. Define $\mathbf{y}$ by $y_{\alpha}=x_{\alpha}$ for $\alpha\in K$ and $y_{\alpha}=a_{\alpha}$ otherwise; then $\mathbf{y}\in X_{K}\subset Y$, and $\mathbf{y}\in U$ because $y_{\alpha}=x_{\alpha}\in U_{\alpha}$ on $K$ and $y_{\alpha}=a_{\alpha}\in U_{\alpha}=X_{\alpha}$ off $K$. So every neighbourhood of $\mathbf{x}$ meets $Y$ and $\mathbf{x}\in\overline Y$. Hence $X=\overline Y$, and by Theorem 23.4 (with $Y\subset X\subset\overline Y$) $X$ is connected.
:::
