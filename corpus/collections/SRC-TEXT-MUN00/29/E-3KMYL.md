---
schema: qual/card@1
id: E-3KMYL
kind: problem
title: Local compactness of products
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 2, printed p. 186, with Tychonoff's
    theorem and the projections of §19; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.2, PDF pp. 21-22. Local compactness of a
    product forces every factor outside a finite set to be compact, through projections of a
    compact neighbourhood, and the converse assembles compact factors with compact
    neighbourhoods. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 29.2, PDF pp. 21-22). Checked against the book: §29 Exercise 2 as printed
    (p. 186); the definition of local compactness (p. 185); Theorem 26.5 (p. 166) for the
    compactness of a projection of C; Theorem 37.3 (p. 234) for Tychonoff. Two points the
    retained text leaves implicit are now stated: that the projection of a product-basic
    set is open, which is what makes each coordinate in the finite set locally compact, and
    that the coordinates outside that set are compact because the basis element equals the
    factor there. No repair to the printed statement.
---

::: {.exercise}

Let $\theset{X_\alpha}$ be an indexed family of nonempty spaces.

(a) Show that if $\prod X_\alpha$ is locally compact, then each $X_\alpha$ is locally compact and $X_\alpha$ is compact for all but finitely many values of $\alpha$.

(b) Prove the converse, assuming the Tychonoff theorem.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.2, PDF pp. 21--22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps.

Throughout, a space is locally compact at a point when some compact subspace contains a neighbourhood of that point (Munkres, *Topology* (2000), §29, printed p. 185), the topologies on products are the product topologies, and $\pi_\beta$ is the projection to the factor $X_\beta$.

::: pf

::: {.pf-step #a}
(a) If $\prod_\alpha X_\alpha$ is locally compact, then each $X_\alpha$ is locally compact and all but finitely many of the $X_\alpha$ are compact.

::: pf-proof

::: {.pf-step #a-basic}
For every point $\mathbf{x}$ of the product there are a compact $C\subset\prod_\alpha X_\alpha$ and a finite set $F$ of indices such that the product-basic set $\prod_\alpha U_\alpha$, where $U_\alpha=X_\alpha$ for $\alpha\notin F$ and $U_\alpha$ is a neighbourhood of $x_\alpha$ for $\alpha\in F$, contains $\mathbf{x}$ and lies in $C$.

::: pf-proof
Local compactness at $\mathbf{x}$ supplies a compact $C$ containing a neighbourhood of $\mathbf{x}$; that neighbourhood contains a basis element for the product topology, which has the form $\prod_\alpha U_\alpha$ with $U_\alpha=X_\alpha$ for all $\alpha$ outside a finite set $F$ (§19).
:::

:::

::: {.pf-step #a-outside}
$X_\beta$ is compact for every $\beta\notin F$.

::: pf-proof
The projection $\pi_\beta$ is continuous, so $\pi_\beta(C)$ is compact (Theorem 26.5, printed p. 166), and it is a subspace of $X_\beta$. On the other hand $U_\beta=X_\beta$ for $\beta\notin F$, and $\pi_\beta\big(\prod_\alpha U_\alpha\big)=U_\beta$, so $X_\beta\subset\pi_\beta(C)$. Hence $X_\beta=\pi_\beta(C)$ is compact, and a compact space is locally compact at each of its points (printed p. 185).
:::

:::

::: {.pf-step #a-inside}
$X_\beta$ is locally compact also for $\beta\in F$, and therefore (a) holds.

::: pf-proof
Let $\beta\in F$; the factors are nonempty, so choose a point $\mathbf{x}$ of the product with $x_\beta$ prescribed. Step [](#a-basic){.pf-ref} applied at $\mathbf{x}$ produces a compact $C$ and a basis element $\prod_\alpha U_\alpha\subset C$ containing $\mathbf{x}$, and the projection $\pi_\beta$ is an open map, so $\pi_\beta\big(\prod_\alpha U_\alpha\big)=U_\beta$ is a neighbourhood of $x_\beta$ lying in the compact set $\pi_\beta(C)$. As $x_\beta$ was arbitrary, $X_\beta$ is locally compact, and with step [](#a-outside){.pf-ref} all but finitely many factors are compact, which is (a).
:::

:::

:::

:::

::: {.pf-step #b}
(b) Conversely, if every $X_\alpha$ is locally compact and all but finitely many of them are compact, then $\prod_\alpha X_\alpha$ is locally compact.

::: pf-proof

::: {.pf-step #b-factors}
For each $\alpha$ there are a compact $C_\alpha\subset X_\alpha$ and a neighbourhood $U_\alpha$ of $x_\alpha$ with $U_\alpha\subset C_\alpha$, with $U_\alpha=C_\alpha=X_\alpha$ for all but finitely many $\alpha$.

::: pf-proof
Let $F$ be the finite set of indices at which $X_\alpha$ is not compact. For $\alpha\notin F$ put $U_\alpha=C_\alpha=X_\alpha$, which is compact and a neighbourhood of $x_\alpha$. For $\alpha\in F$ local compactness at $x_\alpha$ gives a compact $C_\alpha$ containing a neighbourhood $U_\alpha$ of $x_\alpha$. So $U_\alpha=C_\alpha=X_\alpha$ for all but the finitely many indices in $F$.
:::

:::

::: {.pf-step #b-product}
$\prod_\alpha C_\alpha$ is compact and contains $\prod_\alpha U_\alpha$, which is a neighbourhood of $\mathbf{x}$; hence the product is locally compact at $\mathbf{x}$.

::: pf-proof
Each $C_\alpha$ is compact, so $\prod_\alpha C_\alpha$ is compact in the product topology by the Tychonoff theorem (Theorem 37.3, printed p. 234), which is the hypothesis of this part. Since $U_\alpha\subset C_\alpha$ for every $\alpha$, the product $\prod_\alpha U_\alpha$ lies in $\prod_\alpha C_\alpha$, and it is a basis element of the product topology because $U_\alpha=X_\alpha$ for all $\alpha$ outside the finite set $F$ of step [](#b-factors){.pf-ref}; it contains $\mathbf{x}$ since each $U_\alpha$ contains $x_\alpha$. As $\mathbf{x}$ was arbitrary, the product is locally compact.
:::

:::

:::

:::

:::

:::
