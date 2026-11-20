---
schema: qual/card@1
id: E-HAT-2.3-4
kind: problem
title: Wedge axiom follows from other axioms for finite wedge sums
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Wedge Sums
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.3, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the binary case: the retraction of $X\vee Y$ onto $X$ is a left inverse of the inclusion,
    so $i_*$ is split injective and the connecting map vanishes; the quotient map to $Y$ is the
    identity on $Y$, so $Y\to X\vee Y\to Y$ is the identity and the second map is onto; and the
    retraction onto $Y$ supplies the section that splits the sequence. Finite wedges then follow by
    induction.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 4 of §2.3 as printed on p. 165, and the fact is the one Hatcher
    points out on p. 160. The binary argument is correct: (X vee Y)/X = Y, the retraction onto X
    makes i_* split injective, and the inclusion of Y provides a section of the quotient-induced
    map so that map is onto and the connecting homomorphism vanishes; the sequence splits by the
    two retractions. The step now names both reasons instead of only the first, and the exactness
    axiom is cited to p. 160. What is not covered: no certificate.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 4 of §2.3, printed p. 165, and axioms (1) and (2) of printed
    p. 160; the solution is DeMason's, Hatcher 2.3.4, printed pp. 83--84 of
    `tmp/sources/demason-m382c-hatcher-20210404.pdf`. Checked in the binary case: the pair
    $(X\vee Y,X)$ has $(X\vee Y)/X\cong Y$, so the reduced sequence runs
    $\widetilde h_n(X)\to\widetilde h_n(X\vee Y)\to\widetilde h_n(Y)\to\widetilde h_{n-1}(X)$; the
    retraction onto $X$ makes the first map split injective, the retraction onto $Y$ is a left
    inverse of the inclusion $Y\subset X\vee Y$ and so makes the third map surjective, and
    exactness in the middle is the exactness axiom itself, so the two retractions cut the sequence
    into short exact sequences. The splitting lemma then gives the direct sum, and the induction is
    DeMason's, run on $(X_1\vee\cdots\vee X_n,X_{n+1})$ with the same two retractions. The card's
    sentence that the connecting map out of $\widetilde h_n(Y)$ is zero records the same fact as
    the surjectivity of $j_*$ once exactness at $\widetilde h_n(Y)$ is granted. The sentence and
    citation that closed the card were merged into the head of the solution, where the printed
    pages now stand. Not claimed: a certificate, and the infinite wedge, which is exactly where
    the axiom fails (Exercise 2 of the same page, and Hatcher's remark on printed p. 161).
---

::: {.problem}
Show that the wedge axiom for homology theories follows from the other axioms in the case of finite wedge sums.
:::

::: {.solution}
It suffices to prove the binary case and then induct. This is the deduction Hatcher points out on p. 160, where the third axiom is said to follow from the first two for finite wedge sums, and not in general for infinite ones.

The binary case and the induction are transcribed from **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.3.4. The exercise is Exercise 4 of §2.3; the axioms used are (1) and (2) of printed p. 160.

Let $X\vee Y$ be the wedge at the common basepoint $*$. Regard $X$ as a subcomplex of $X\vee Y$. Then
$$
(X\vee Y)/X\cong Y.
$$

::: pf

::: pf-step

The long exact sequence of the pair $(X\vee Y,X)$ splits into short exact sequences
$$
0\longrightarrow\widetilde h_n(X)
\longrightarrow\widetilde h_n(X\vee Y)
\longrightarrow\widetilde h_n(Y)\longrightarrow0.
$$

::: pf-proof

The exactness axiom, axiom (2) of p. 160, uses the quotient $(X\vee Y)/X\cong Y$ directly.
The retraction $r:X\vee Y\to X$ collapsing $Y$ to the wedge point satisfies $r\circ i=\mathrm{id}_X$. Hence $i_*:\widetilde h_n(X)\to\widetilde h_n(X\vee Y)$ is split injective. Also the inclusion $Y\subset X\vee Y$ is a section of the quotient-induced map $j_*$, so $j_*$ is surjective and the connecting map out of $\widetilde h_n(Y)$ is zero. These two facts cut the long exact sequence into the displayed short exact sequences.

:::

:::

::: pf-step

The sequence splits naturally, so
$$
\widetilde h_n(X\vee Y)\cong
\widetilde h_n(X)\oplus\widetilde h_n(Y).
$$

::: pf-proof

The retraction $X\vee Y\to Y$ collapsing $X$ supplies a section of the quotient-induced map to $\widetilde h_n(Y)$. Equivalently, the two inclusions induce the direct-sum map, and the two retractions give its inverse.

:::

:::

:::

Iterating the binary isomorphism gives the wedge axiom for every finite wedge sum.


:::
