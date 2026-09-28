---
title: Meromorphic functions
order: 30
topics:
- Meromorphic Functions
- Mittag-Leffler Theorem
- Partial Fractions
---

# Meromorphic functions

A meromorphic function on an open set is holomorphic except on a discrete set, at each point of which it has a pole.

[[D-7DFVJ]]

[[T-UBWL2]]

::: {.proof}
Since $\infty$ is removable or a pole, $f$ has no poles in $\ts{\abs z > R}$ for some $R$, and the poles in the compact disc $\abs z\leq R$ are isolated, hence finitely many: $z_1,\ldots,z_N$.
Let $P_j$ be the principal part of $f$ at $z_j$, a polynomial in $(z-z_j)\inv$ without constant term, and let $P_\infty$ be the polynomial part of the Laurent series of $f$ on $\abs z>R$ with its constant term omitted, so that $f - P_\infty$ is bounded near $\infty$.
Then $g \coloneqq f - P_\infty - \sum_j P_j$ has only removable singularities in $\CC$, so it extends to an entire function, and it is bounded near $\infty$ because each $P_j\to 0$ as $z\to\infty$.
By Liouville's theorem $g$ is constant, so $f = g + P_\infty + \sum_j P_j$ is rational.
:::

[[T-DB3DO]]

::: {.remark}
The [[complex-analysis/counting-zeros/the-argument-principle|argument principle]] counts zeros minus poles of a meromorphic function, and [[complex-analysis/residues-and-contours/the-residue-theorem|the residue theorem]] applies to meromorphic functions with finitely many poles in the region, where each residue is the coefficient $c_{-1}$ of a Laurent series with finitely many negative terms.
:::
