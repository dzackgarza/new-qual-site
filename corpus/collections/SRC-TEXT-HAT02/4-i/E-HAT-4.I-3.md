---
schema: qual/card@1
id: E-HAT-4.I-3
kind: problem
title: "Skeletons of suspended lens spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.I, Exercise 3 and Proposition 4I.3; the stored statement matches the corrected current source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps and supplied three things it used implicitly: that a
    high-dimensional lens space is a finite skeleton of the infinite one, so its suspension's
    (2k+1)-skeleton is the corresponding skeleton of the suspension of K; that the minimal cell
    structure of the X_i makes the (2k+1)-skeleton of the wedge the wedge of the skeleta, which is
    what allows F to be restricted skeleton by skeleton after cellular approximation; and that both
    skeleta are simply connected because the minimal models have no 1-cells, so that the homology
    form of Whitehead's theorem applies. Also recorded what the argument does not re-derive: the
    homology computation of Proposition 4I.3, which is used degree by degree as stated there. Not
    re-read this session: printed pp. 468 and 349 and Corollary 4.33 on p. 367.

---

::: {.problem}
Extending Proposition 4I.3, show that the $(2k+1)$-skeleton of the suspension of a high-dimensional lens space with fundamental group of order $p^n$ is homotopy equivalent to the wedge sum of the $(2k+1)$-skeleta of the spaces $X_i$, if these $X_i$'s are chosen to have the minimum number of cells in each dimension, as described in the remarks following the proof.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.I Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.I Exercise 3, which extends Proposition 4I.3 (printed p. 468) to finite skeleta.

Let $K=K(\ZZ_{p^{n}},1)$ be the infinite-dimensional lens space, so that $\Sigma K\simeq X_{1}\vee\cdots\vee X_{p-1}$ by Proposition 4I.3. Take the $X_{i}$ in the minimal form described in the remarks following that proof: one $0$-cell and one cell in each dimension congruent to $2i$ or $2i+1$ modulo $2p-2$, and no other positive-dimensional cells. Write $L$ for a lens space with $\pi_{1}=\ZZ_{p^{n}}$ of dimension at least $2k$.

::: pf

::: {.pf-step #skeleton}
$L$ is a finite skeleton of $K$, so $(\Sigma L)^{(2k+1)}=(\Sigma K)^{(2k+1)}$.

::: pf-proof
The standard infinite lens space is the union of its finite-dimensional lens spaces, each an $(m-1)$-skeleton of the next, so $L=K^{(m)}$ for $m=\dim L+1$. Suspension commutes with skeleta one dimension up: $\Sigma K^{(m)}=(\Sigma K)^{(m+1)}$, since a cell of dimension $d$ gives a cell of dimension $d+1$. If $\dim L\geq2k$ then $m\geq2k+1$ and $(\Sigma L)^{(2k+1)}=(\Sigma K)^{(2k+1)}$.
:::

:::

::: {.pf-step #wedge}
$\bigl(\bigvee_{i}X_{i}\bigr)^{(2k+1)}=\bigvee_{i}X_{i}^{(2k+1)}$.

::: pf-proof
A wedge is the quotient of the disjoint union identifying the basepoints, and a cell of the wedge is a cell of exactly one $X_{i}$; the cells of dimension at most $2k+1$ in the wedge are therefore exactly the cells of dimension at most $2k+1$ in the individual $X_{i}$, which is the assertion. This is where the minimal cell structure is used: it is a CW structure, so skeleta are subcomplexes and the identification is legitimate.
:::

:::

::: {.pf-step #homology}
The map $F\colon\Sigma K\to\bigvee_{i}X_{i}$ of Proposition 4I.3 restricts to a map $F^{(2k+1)}$ of $(2k+1)$-skeleta inducing an isomorphism on homology in every degree.

::: pf-proof
$F$ may be taken cellular by the cellular approximation theorem (printed p. 349), and a cellular map carries the $m$-skeleton into the $m$-skeleton, giving $F^{(2k+1)}$ by steps [](#skeleton){.pf-ref} and [](#wedge){.pf-ref}. The homology of both sides in degrees $\le2k+1$ is computed in Proposition 4I.3 degree by degree — the $i$-th telescope retaining exactly the dimensions congruent to $2i$ modulo $2p-2$ — and the same computation applies to the skeleta because the cells above $2k+1$ contribute nothing in those degrees. Both skeleta are $(2k+1)$-dimensional CW complexes, so their homology vanishes above degree $2k+1$; hence $F^{(2k+1)}_{*}$ is an isomorphism in all degrees.
:::

:::

::: {.pf-step #simply-connected}
Both sides of $F^{(2k+1)}$ are simply connected.

::: pf-proof
$\Sigma K$ has no $1$-cells: the minimal models $X_{i}$ have one $0$-cell and their lowest positive-dimensional cells lie in dimensions $2i,2i+1\geq2$, so the wedge has no $1$-cell, and the $1$-skeleton of $\Sigma K$ is a point. A CW complex with a single $0$-cell and no $1$-cells has trivial fundamental group, and the same holds for the skeleta, which are subcomplexes of such complexes.
:::

:::

::: {.pf-step}
$(\Sigma L)^{(2k+1)}\simeq\bigvee_{i=1}^{p-1}X_{i}^{(2k+1)}$.

::: pf-proof
By step [](#homology){.pf-ref} $F^{(2k+1)}$ is a homology isomorphism between simply connected CW complexes, so it is a homotopy equivalence by the homology form of Whitehead's theorem (Corollary 4.33, printed p. 367). Replacing the source by the skeleton of $\Sigma L$ via step [](#skeleton){.pf-ref} gives the stated homotopy equivalence.
:::

:::

:::

:::
