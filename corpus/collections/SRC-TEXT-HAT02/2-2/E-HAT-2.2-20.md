---
schema: qual/card@1
id: E-HAT-2.2-20
kind: problem
title: Euler characteristic is multiplicative for products of finite CW complexes
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 20; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the cell count: the product structure has one cell $e^p\times e^q$ of dimension $p+q$ for
    each pair, so $c_r(X\times Y)=\sum_{p+q=r}c_p(X)c_q(Y)$ and the alternating sums factor.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 20 as printed on p. 157. The argument is the cell count and is
    correct; it now cites the product cell structure of p. 8, where Hatcher also notes that the
    cell-complex topology agrees with the product topology when one factor has finitely many
    cells, which is the case here, and the definition of chi as the alternating sum of numbers of
    cells together with Theorem 2.44, both p. 146. What is not covered: no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the product cell structure and the dimension of
    e^p x e^q as p + q with the agreement of the two topologies for finite complexes, the
    cell count in dimension r as the sum over p + q = r, the identification of chi with the
    alternating sum of cell counts (Hatcher p. 146, Theorem 2.44), and the factorization of
    the finite double sum. The computation is Sam's §2.2 Exercise 20, printed p. 12, as the
    card says; the reformatting also separates the source note from the mathematics, which
    had run together in the earlier prose.
---

::: {.problem}
For finite CW complexes $X$ and $Y$, show that $\chi(X \times Y) = \chi(X)\chi(Y)$.
:::

::: {.solution}
The computation is that of **Sam's §2.2 Exercise 20**: the product cell $e_{p}\times e_{q}$ has dimension $p+q$, and summing $(-1)^{p+q}$ over the product cells factorizes the alternating sum into $\chi(X)\chi(Y)$. It is checked here against Hatcher, §2.2 Exercise 20, and against the two facts the book supplies in Chapter 0 and §2.2.

Write $c_{p}(X)$ and $c_{q}(Y)$ for the numbers of cells of dimension $p$ and $q$ in the given finite CW structures.

::: pf

::: {.pf-step #product-cells}
$X\times Y$ is a finite CW complex whose cells are the products $e^{p}\times e^{q}$, one of dimension $p+q$ for each ordered pair of cells.

::: pf-proof
By the product cell structure of Hatcher, Chapter 0 ("Operations on Spaces"), the products of cells are the cells of a CW structure on $X\times Y$ and $\dim(e^{p}\times e^{q})=p+q=\dim e^{p}+\dim e^{q}$. Since $X$ and $Y$ have finitely many cells each, the weak topology of this cell structure agrees with the product topology on $X\times Y$, as the book notes at the same place; so this is a finite CW structure on the product space.
:::

:::

::: {.pf-step #cell-count}
$c_{r}(X\times Y)=\sum_{p+q=r}c_{p}(X)\,c_{q}(Y)$ for every $r$.

::: pf-proof
Each cell of $X\times Y$ is one product $e^{p}\times e^{q}$ and has dimension $p+q$, and the map $(e^{p},e^{q})\mapsto e^{p}\times e^{q}$ is a bijection between pairs of cells and cells of the product. Counting those pairs with $p+q=r$ gives the displayed sum.
:::

:::

::: {.pf-step #chi-is-cell-count}
$\chi(Z)=\sum_{r}(-1)^{r}c_{r}(Z)$ for a finite CW complex $Z$.

::: pf-proof
Hatcher, §2.2 defines $\chi$ by the alternating sum of the ranks of the homology groups, and Theorem 2.44 there shows that for a finite CW complex this equals the alternating sum of the numbers of cells, $\sum_{r}(-1)^{r}c_{r}(Z)$.
:::

:::

::: {.pf-step #multiplicative}
$\chi(X\times Y)=\chi(X)\chi(Y)$.

::: pf-proof
By steps [](#chi-is-cell-count){.pf-ref} and [](#cell-count){.pf-ref},
$$
\chi(X\times Y)=\sum_{r}(-1)^{r}c_{r}(X\times Y)=\sum_{r}\sum_{p+q=r}(-1)^{p+q}c_{p}(X)c_{q}(Y)=\sum_{p,q}(-1)^{p}c_{p}(X)\,(-1)^{q}c_{q}(Y),
$$
and the double sum factors as $\big(\sum_{p}(-1)^{p}c_{p}(X)\big)\big(\sum_{q}(-1)^{q}c_{q}(Y)\big)=\chi(X)\chi(Y)$ by step [](#chi-is-cell-count){.pf-ref}. Both sums are finite — the complexes are finite, so only finitely many $c_{p}$ and $c_{q}$ are nonzero — so regrouping the double sum and factoring it are legitimate.
:::

:::

::: {.pf-step}
$\chi(X\times Y)=\chi(X)\chi(Y)$ for finite CW complexes $X$ and $Y$.

::: pf-proof
Step [](#multiplicative){.pf-ref} is the assertion.
:::

:::

:::
:::
