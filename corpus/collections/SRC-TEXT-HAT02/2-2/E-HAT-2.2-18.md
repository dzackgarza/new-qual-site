---
schema: qual/card@1
id: E-HAT-2.2-18
kind: problem
title: Relative cellular chain complex for CW pair
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
  - Relative Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 18; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular-chain proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: $H_n(X^n,X^{n-1}\cup A^n)$ is free on the $n$-cells outside $A$ and
    agrees with the quotient $C_n^{CW}(X)/C_n^{CW}(A)$; the quotient differential is well defined
    because $C_*^{CW}(A)$ is a subcomplex, so it squares to zero; and the short exact sequence of
    chain complexes with the five lemma identifies the homology of the quotient with $H_n(X,A)$,
    the comparison maps coming from naturality of the cellular-to-singular isomorphism.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 18 as printed on p. 157, including the printed A^i in the second
    entry of the pair. Step (s1) had appealed to an unnamed "relative cellular calculation" for
    the basis of H_n(X^n, X^{n-1} union A^n); it now collapses the subcomplex to a wedge of one
    n-sphere per n-cell of X outside A and cites Proposition 2.22 p. 124 with Corollary 2.25
    p. 126, together with Lemma 2.34(a) p. 137. Step (s2) now cites Theorem 2.16 p. 117 for the
    long exact sequence, Theorem 2.35 p. 139 for the two identifications, p. 127 for naturality,
    and notes that Hatcher's five lemma is unnumbered on p. 129. What is not covered: the
    five-lemma comparison is not written out map by map, and no certificate was produced.
---

::: {.problem}
For a CW pair $(X, A)$ show there is a relative cellular chain complex formed by the groups $H_i(X^i, X^{i-1} \cup A^i)$, having homology groups isomorphic to $H_n(X, A)$.
:::

::: {.solution}
Let $A$ be a CW subcomplex of $X$ and put $A^n=A\cap X^n$. The inclusion of cellular chain complexes $C_*^{CW}(A)\hookrightarrow C_*^{CW}(X)$ is degreewise injective. Form the quotient chain complex
$$
C_*^{CW}(X,A)=C_*^{CW}(X)/C_*^{CW}(A).
$$

::: pf

::: {.pf-step #s1}

In every degree $n$, the quotient chain group is naturally
$$
C_n^{CW}(X,A)\cong H_n(X^n,X^{n-1}\cup A^n).
$$

::: pf-proof

The cellular chain group $H_n(X^n,X^{n-1})$ is free on the $n$-cells of $X$ by Lemma 2.34(a) (p. 137), and $H_n(A^n,A^{n-1})$ is free on the subset of $n$-cells in $A$. Their quotient is free on the $n$-cells of $X$ outside $A$. The characteristic maps of these remaining cells give the same basis for $H_n(X^n,X^{n-1}\cup A^n)$: collapsing the subcomplex $X^{n-1}\cup A^n$ gives a wedge of one $n$-sphere per $n$-cell of $X$ outside $A$, the pair is good, so Proposition 2.22 (p. 124) identifies the relative group with the reduced homology of that wedge, which is free on those spheres by Corollary 2.25 (p. 126). This includes degree zero: the group is free on the vertices of $X$ outside $A$.

:::

:::

::: {.pf-step #s2}

The groups in step [](#s1){.pf-ref} carry a differential, and their chain complex computes $H_n(X,A)$.

::: pf-proof

Because $A$ is a subcomplex, its cellular differential is the restriction of that of $X$, so the quotient differential is well defined and squares to zero. The short exact sequence of cellular chain complexes
$$
0\to C_*^{CW}(A)\to C_*^{CW}(X)\to C_*^{CW}(X,A)\to0
$$
gives a long exact sequence in homology by Theorem 2.16 (p. 117). Theorem 2.35 (p. 139) identifies $H_n(C_*^{CW}(A))$ and $H_n(C_*^{CW}(X))$ with $H_n(A)$ and $H_n(X)$, and the comparison of that sequence with the long exact sequence of the pair $(X,A)$ is natural in the sense of p. 127, so the connecting maps agree by their chain-level definitions (p. 115). The five lemma, stated without a number on p. 129, therefore identifies the remaining terms:
$$
\boxed{H_n(C_*^{CW}(X,A))\cong H_n(X,A).}
$$

:::

:::

:::
:::
