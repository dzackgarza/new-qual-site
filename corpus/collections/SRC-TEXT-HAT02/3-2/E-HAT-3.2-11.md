---
schema: qual/card@1
id: E-HAT-3.2-11
kind: problem
title: Maps $S^{k+\ell} \to S^k \times S^\ell$ are trivial on top homology
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 11; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: $a\smile b$ generates $H^{k+\ell}(S^k\times S^\ell)$ and both factors die
    under $f^*$ since $H^k$ and $H^\ell$ of $S^{k+\ell}$ vanish for $0<k,\ell$; so
    $f^*(a\smile b)=0$ and pairing with the fundamental class shows $f_*[S^{k+\ell}]=0$.
---

::: {.problem}
Using cup products, show that every map $S^{k+\ell} \to S^k \times S^\ell$ induces the trivial homomorphism $H_{k+\ell}(S^{k+\ell}) \to H_{k+\ell}(S^k \times S^\ell)$, assuming $k > 0$ and $\ell > 0$.
:::

::: {.solution}
Let $\alpha\in H^k(S^k;\ZZ)$ and $\beta\in H^\ell(S^\ell;\ZZ)$ be generators. Their pullbacks $a$ and $b$ under the two projections from $S^k\times S^\ell$ have product
$$
a\smile b\in H^{k+\ell}(S^k\times S^\ell;\ZZ)
$$
equal to a generator, by the cohomology cross-product calculation. This remains true when $k=\ell$, when the two classes lie in the same cohomological degree.

For any map $f:S^{k+\ell}\to S^k\times S^\ell$, both $H^k(S^{k+\ell};\ZZ)$ and $H^\ell(S^{k+\ell};\ZZ)$ vanish because $k,\ell>0$. Thus $f^*a=f^*b=0$, and naturality of the cup product gives $f^*(a\smile b)=0$. Evaluation on the fundamental class satisfies
$$
\langle a\smile b,f_*[S^{k+\ell}]\rangle
=\langle f^*(a\smile b),[S^{k+\ell}]\rangle=0.
$$
The pairing of the top cohomology generator with the top homology generator of $S^k\times S^\ell$ is $\pm1$. Hence $f_*[S^{k+\ell}]=0$, proving that the induced top-homology map is zero.
:::
