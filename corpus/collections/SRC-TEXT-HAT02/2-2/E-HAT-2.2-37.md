---
schema: qual/card@1
id: E-HAT-2.2-37
kind: exercise
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
---

Give an elementary derivation for the Mayer–Vietoris sequence in simplicial homology for a $\Delta$-complex $X$ decomposed as the union of subcomplexes $A$ and $B$.

::: {.solution}
<1>1. Let $C_n(X)$, $C_n(A)$, $C_n(B)$, $C_n(A \cap B)$ be the simplicial chain groups.
::: {.proof}
setup.
:::

<1>2. There is a short exact sequence of chain complexes $$0 \to C_n(A \cap B) \xrightarrow{(i_*, j_*)} C_n(A) \oplus C_n(B) \xrightarrow{k_* - \ell_*} C_n(A + B) \to 0,$$ where $i, j$ are the inclusions of $A \cap B$ into $A$ and $B$, and $k, \ell$ are the inclusions of $A$ and $B$ into $X$ (with $C_n(A + B) = C_n(X)$ since $A \cup B = X$).
::: {.proof}
the map $C_n(A \cap B) \to C_n(A) \oplus C_n(B)$ is injective (a simplex in $A \cap B$ is determined by its images in $A$ and $B$), and the map $C_n(A) \oplus C_n(B) \to C_n(X)$ is surjective (every simplex of $X$ lies in $A$ or $B$), with exactness in the middle (a pair $(a, b)$ maps to $0$ iff $a = b$ as chains, i.e. iff it comes from $A \cap B$).
:::

<1>3. This short exact sequence of chain complexes induces a long exact sequence in homology: $$\cdots \to H_n(A \cap B) \to H_n(A) \oplus H_n(B) \to H_n(X) \to H_{n-1}(A \cap B) \to \cdots.$$ Proof: the standard long exact sequence in homology associated to a short exact sequence of chain complexes.

<1>4. This is the Mayer–Vietoris sequence.
::: {.proof}
<1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
