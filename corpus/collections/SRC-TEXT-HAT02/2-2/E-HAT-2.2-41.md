---
schema: qual/card@1
id: E-HAT-2.2-41
kind: problem
title: Euler characteristic equals alternating sum of dimensions of $H_n(X; F)$ over a field
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 41; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the dimension count: over a field the cellular chain groups have dimension $c_n$, and
    $\dim C_n=\dim B_n+\dim H_n+\dim B_{n-1}$ makes the two boundary sums cancel in the alternating
    sum.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 41 as printed on p. 159. The dimension count is correct: with
    Z_n = ker d_n and B_n = im d_{n+1}, dim C_n = dim B_n + dim H_n + dim B_{n-1}, and the two
    boundary sums telescope away. What was missing and is now supplied: chi as the alternating sum
    of cell counts is the definition on p. 146, and that the cellular complex with field
    coefficients computes H_*(X;F) is the coefficient form of Theorem 2.35 p. 139, used in that
    form in Example 2.50 p. 154. What is not covered: no certificate.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 41, printed p. 159, which asks for the equality of the Euler characteristic with the alternating sum of the dimensions of $H_n(X;F)$ over a field. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own. Checked: the two short exact sequences, the dimension count, and the cancellation of the $B$-terms in the alternating sum.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said no retained solution set covers the exercise, and that is false:
    `tmp/sources/hatcher-solutions-guanyu-li.md` solves it under the older numbering, at the heading
    "Exercise 2.2.19 (2.2.41)", by the same finite-dimensional complex and the same alternating-sum
    cancellation. The rendered sentence now cites it and says what the card adds, the two short exact
    sequences made explicit. Found by screening the residue's absence claims against the retained
    inventory after two such claims were found false in the §30 and §31 Munkres cards; no step of the
    proof changed, and the statement was re-read against Hatcher printed p. 159.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 168 carries the running head 159, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
---

::: {.problem}
This is Exercise 41 of Section 2.2 of Hatcher, *Algebraic Topology* (2002), read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf`; the statement below is its wording.

For $X$ a finite CW complex and $F$ a field, show that the Euler characteristic $\chi(X)$ can also be computed by the formula $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$, the alternating sum of the dimensions of the vector spaces $H_n(X; F)$.
:::

::: {.solution}
The retained published solution is Guanyu Li's *Hatcher solutions*, which answers this exercise under the older numbering "Exercise 2.2.19 (2.2.41)": it takes the $F$-coefficient cellular complex, notes each $C_i$ is finite dimensional because $X$ is a finite CW complex, and cancels the boundary dimensions in the alternating sum. The card states the same count with the two short exact sequences written out. Checked against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 41. The point is the dimension count over a field: $\dim C_n=\dim B_n+\dim H_n+\dim B_{n-1}$, whose boundary terms cancel in the alternating sum.

::: pf

::: {.pf-step #chain}
The cellular chain groups $C_n=C_n^{CW}(X;F)$ are finite-dimensional over $F$ with $\dim_FC_n=c_n$, the number of $n$-cells, and $H_n(C_*)\cong H_n(X;F)$.

::: pf-proof
The cellular chain complex of a CW complex has one basis element per $n$-cell over any coefficient ring, and its homology computes the singular homology with those coefficients (Theorem 2.35, in its coefficient form). Since $X$ is a finite CW complex, only finitely many $c_n$ are nonzero.
:::
:::

::: {.pf-step #exact}
With $Z_n=\ker d_n$ and $B_n=\operatorname{im}d_{n+1}$ there are short exact sequences $0\to Z_n\to C_n\to B_{n-1}\to0$ and $0\to B_n\to Z_n\to H_n\to0$.

::: pf-proof
The image of $d_n$ is $B_{n-1}$, and $d_n$ kills $Z_n$, so the first sequence is exact; the kernel of $Z_n\to H_n$ is $B_n$ by the definition of homology, giving the second.
:::
:::

::: {.pf-step #dimension}
$\dim C_n=\dim B_n+\dim H_n+\dim B_{n-1}$ for every $n$.

::: pf-proof
For a short exact sequence of finite-dimensional vector spaces the middle dimension is the sum of the outer two, so the first sequence gives $\dim C_n=\dim Z_n+\dim B_{n-1}$ and the second gives $\dim Z_n=\dim B_n+\dim H_n$.
:::
:::

::: {.pf-step #alternating}
$\chi(X)=\sum_n(-1)^n\dim_FH_n(X;F)$.

::: pf-proof
By step [](#chain){.pf-ref} $\chi(X)=\sum_n(-1)^n\dim C_n$, and substituting step [](#dimension){.pf-ref} gives three sums. The terms involving $B_m$ occur as $(-1)^m\dim B_m$ from the first summand with index $m$ and as $(-1)^{m+1}\dim B_m$ from the third summand with index $m+1$, so they cancel in pairs; what remains is $\sum_n(-1)^n\dim_FH_n(X;F)$.
:::
:::

:::
:::
