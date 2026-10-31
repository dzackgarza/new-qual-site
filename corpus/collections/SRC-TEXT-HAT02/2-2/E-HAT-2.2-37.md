---
schema: qual/card@1
id: E-HAT-2.2-37
kind: problem
title: Elementary derivation of Mayer–Vietoris sequence in simplicial homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Simplicial Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 37.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the derivation: for subcomplexes of a $\Delta$-complex every simplex of $A\cup B$ lies in
    $A$ or in $B$ and one lying in both lies in $A\cap B$, so
    $0\to C_*(A\cap B)\to C_*(A)\oplus C_*(B)\to C_*(X)\to0$ is degreewise short exact and the maps
    commute with boundaries; its homology sequence is Mayer-Vietoris. This is exactly the point at
    which the $\Delta$-complex hypothesis is used, the identity $C_*(A+B)=C_*(X)$ failing for
    singular chains. The two closing steps are read at the level of their claims.
---

::: {.problem}
Give an elementary derivation for the Mayer–Vietoris sequence in simplicial homology for a $\Delta$-complex $X$ decomposed as the union of subcomplexes $A$ and $B$.
:::

::: {.solution}

::: pf

::: pf-step

Let $C_n(X)$, $C_n(A)$, $C_n(B)$, $C_n(A \cap B)$ be the simplicial chain groups.

::: pf-proof

setup.

:::

:::

::: pf-step

There is a short exact sequence of chain complexes $$0 \to C_n(A \cap B) \xrightarrow{(i_*, j_*)} C_n(A) \oplus C_n(B) \xrightarrow{k_* - \ell_*} C_n(A + B) \to 0,$$ where $i, j$ are the inclusions of $A \cap B$ into $A$ and $B$, and $k, \ell$ are the inclusions of $A$ and $B$ into $X$ (with $C_n(A + B) = C_n(X)$ since $A \cup B = X$).

::: pf-proof

the map $C_n(A \cap B) \to C_n(A) \oplus C_n(B)$ is injective (a simplex in $A \cap B$ is determined by its images in $A$ and $B$), and the map $C_n(A) \oplus C_n(B) \to C_n(X)$ is surjective (every simplex of $X$ lies in $A$ or $B$), with exactness in the middle (a pair $(a, b)$ maps to $0$ iff $a = b$ as chains, i.e. iff it comes from $A \cap B$).

:::

:::

::: {.pf-step #s3}

This short exact sequence of chain complexes induces a long exact sequence in homology: $$\cdots \to H_n(A \cap B) \to H_n(A) \oplus H_n(B) \to H_n(X) \to H_{n-1}(A \cap B) \to \cdots.$$ Proof: the standard long exact sequence in homology associated to a short exact sequence of chain complexes.

:::

::: {.pf-step #s4}

This is the Mayer–Vietoris sequence.

::: pf-proof

Step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref}.

:::

:::

:::
