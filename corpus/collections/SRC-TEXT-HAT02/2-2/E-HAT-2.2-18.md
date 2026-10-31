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

The cellular chain group $H_n(X^n,X^{n-1})$ is free on the $n$-cells of $X$, and $H_n(A^n,A^{n-1})$ is free on the subset of $n$-cells in $A$. Their quotient is free on the $n$-cells of $X$ outside $A$. The characteristic maps of these remaining cells give the same basis for $H_n(X^n,X^{n-1}\cup A^n)$, by the relative cellular calculation. This includes degree zero: the group is free on the vertices of $X$ outside $A$.

:::

:::

::: {.pf-step #s2}

The groups in step [](#s1){.pf-ref} carry a differential, and their chain complex computes $H_n(X,A)$.

::: pf-proof

Because $A$ is a subcomplex, its cellular differential is the restriction of that of $X$, so the quotient differential is well defined and squares to zero. The short exact sequence of cellular chain complexes
$$
0\to C_*^{CW}(A)\to C_*^{CW}(X)\to C_*^{CW}(X,A)\to0
$$
gives a long exact sequence in homology. Naturality of the cellular-to-singular comparison identifies the first two terms and maps with the corresponding terms in the long exact sequence of the pair $(X,A)$. The connecting maps agree by their chain-level definitions. The five lemma therefore identifies the remaining terms:
$$
\boxed{H_n(C_*^{CW}(X,A))\cong H_n(X,A).}
$$

:::

:::

:::
:::
