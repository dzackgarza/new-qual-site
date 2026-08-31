---
schema: qual/card@1
id: P-ALGF18D
kind: problem
title: Tensor product of projective modules is projective
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A$ be a unital commutative ring.
Suppose $P$ and $Q$ are two projective $A$-modules.
Prove that $P \otimes_A Q$ is a projective $A$-module.
:::

::: {.solution}
<1>1. $P$ is a direct summand of a free module: $P \oplus P' \cong A^{(I)}$ for some set $I$.
::: {.proof}
a module is projective iff it is a direct summand of a free module.
:::

<1>2. $Q$ is a direct summand of a free module: $Q \oplus Q' \cong A^{(J)}$ for some set $J$.
::: {.proof}
same characterization.
:::

<1>3. $(P \oplus P') \otimes_A (Q \oplus Q') \cong A^{(I)} \otimes_A A^{(J)} \cong A^{(I \times J)}$ is free.
::: {.proof}
tensor product distributes over direct sums, and $A^{(I)} \otimes_A A^{(J)} \cong A^{(I \times J)}$.
:::

<1>4. $P \otimes_A Q$ is a direct summand of $(P \oplus P') \otimes_A (Q \oplus Q')$.
::: {.proof}
expanding the tensor product, $P \otimes Q$ appears as a direct summand (the tensor product distributes over direct sums, so $(P \oplus P') \otimes (Q \oplus Q') \cong (P \otimes Q) \oplus (P \otimes Q') \oplus (P' \otimes Q) \oplus (P' \otimes Q')$).
:::

<1>5. Hence $P \otimes_A Q$ is a direct summand of a free module, so it is projective.
::: {.proof}
<1>3, <1>4, and the characterization in <1>1.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
