---
schema: qual/card@1
id: PR-SHFPUSHEX
kind: proposition
title: Exactness of pushforward, and pullback to a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Direct Image Functor
  - Inverse Image Functor
  - Exact Sequences
relations:
- kind: uses
  target: PR-C9ZEK
review: draft
prompts:
- Show that pushforward is left exact, and exact along a closed embedding.
- For $i \colon \{x\} \hookrightarrow X$, show that $i^{-1} \mathcal{F} \cong \mathcal{F}_x$.
---

::: {.proposition}
Let $f \colon X \to Y$ be continuous and $0 \to \mcf' \to \mcf \to \mcf''$ an exact sequence of sheaves of abelian groups on $X$.

1. $0 \to f_* \mcf' \to f_* \mcf \to f_* \mcf''$ is exact.

2. If $f$ is a homeomorphism onto a closed subset of $Y$, then $f_*$ is exact.

3. For $i \colon \{x\} \hookrightarrow X$ the inclusion of a point, $i^{-1} \mcf \cong \mcf_x$.
:::

::: {.remark}
Without the closed-image hypothesis part 2 fails: for $j \colon \CC^* \hookrightarrow \CC$ the exponential sequence $0 \to 2\pi i \ZZ \to \OO \to \OO^* \to 0$ on $\CC^*$ is exact, but $j_* \OO \to j_* \OO^*$ is not surjective on stalks at $0$, since $z$ has no logarithm on any punctured disc.
:::
