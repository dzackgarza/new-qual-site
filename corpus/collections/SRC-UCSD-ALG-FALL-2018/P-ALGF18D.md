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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2018 source; the statement agrees with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that projective modules are direct summands of free modules, tensor products distribute over those direct sums, and the resulting ambient tensor product is free.
---

::: {.problem}
Let $A$ be a unital commutative ring.
Suppose $P$ and $Q$ are two projective $A$-modules.
Prove that $P \otimes_A Q$ is a projective $A$-module.
:::

::: {.solution}

::: pf

::: {.pf-step #p-summand-of-free}
$P$ is a direct summand of a free module: $P \oplus P' \cong A^{(I)}$ for some set $I$.

::: pf-proof
a module is projective iff it is a direct summand of a free module.
:::

:::

::: pf-step
$Q$ is a direct summand of a free module: $Q \oplus Q' \cong A^{(J)}$ for some set $J$.

::: pf-proof
same characterization.
:::

:::

::: {.pf-step #sum-tensor-free}
$(P \oplus P') \otimes_A (Q \oplus Q') \cong A^{(I)} \otimes_A A^{(J)} \cong A^{(I \times J)}$ is free.

::: pf-proof
tensor product distributes over direct sums, and $A^{(I)} \otimes_A A^{(J)} \cong A^{(I \times J)}$.
:::

:::

::: {.pf-step #pq-summand}
$P \otimes_A Q$ is a direct summand of $(P \oplus P') \otimes_A (Q \oplus Q')$.

::: pf-proof
expanding the tensor product, $P \otimes Q$ appears as a direct summand (the tensor product distributes over direct sums, so $(P \oplus P') \otimes (Q \oplus Q') \cong (P \otimes Q) \oplus (P \otimes Q') \oplus (P' \otimes Q) \oplus (P' \otimes Q')$).
:::

:::

::: {.pf-step #pq-projective}
Hence $P \otimes_A Q$ is a direct summand of a free module, so it is projective.

::: pf-proof
step [](#sum-tensor-free){.pf-ref}, step [](#pq-summand){.pf-ref}, and the characterization in step [](#p-summand-of-free){.pf-ref}.
:::

:::

::: pf-qed
step [](#pq-projective){.pf-ref}.
:::

:::
:::
