---
schema: qual/card@1
id: P-ALGS04F
kind: problem
title: "Every projective module is flat"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Prove that a projective $R$-module is flat.

Hint: First prove the case for a free $R$-module.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A free $R$-module is flat.

::: pf-proof

::: {.pf-step #s1-1}

A free module $R^{(I)}$ is a direct sum of copies of $R$.

::: pf-proof

definition.

:::

:::

::: {.pf-step #s1-2}

$R$ is flat: tensoring with $R$ is the identity functor, which is exact.

::: pf-proof

$R \otimes_R M \cong M$ naturally.

:::

:::

::: {.pf-step #s1-3}

A direct sum of flat modules is flat.

::: pf-proof

tensor product commutes with direct sums, and a direct sum of exact sequences is exact.

:::

:::

::: pf-step

Hence $R^{(I)}$ is flat.

::: pf-proof

Steps [](#s1-1){.pf-ref}, [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s2}

A projective module $P$ is a direct summand of a free module: $P \oplus Q \cong R^{(I)}$.

::: pf-proof

characterization of projective modules.

:::

:::

::: {.pf-step #s3}

A direct summand of a flat module is flat.

::: pf-proof

::: {.pf-step #s3-1}

Let $0 \to M' \to M \to M'' \to 0$ be exact.

::: pf-proof

take an arbitrary short exact sequence.

:::

:::

::: {.pf-step #s3-2}

$0 \to (P \oplus Q) \otimes M' \to (P \oplus Q) \otimes M \to (P \oplus Q) \otimes M'' \to 0$ is exact.

::: pf-proof

$P \oplus Q \cong R^{(I)}$ is flat (step [](#s1){.pf-ref}).

:::

:::

::: {.pf-step #s3-3}

This sequence is the direct sum of the sequences for $P$ and for $Q$, so the $P$-sequence $0 \to P \otimes M' \to P \otimes M \to P \otimes M'' \to 0$ is exact.

::: pf-proof

a direct summand of an exact sequence is exact.

:::

:::

::: pf-step

Hence $P$ is flat.

::: pf-proof

Steps [](#s3-1){.pf-ref}, [](#s3-2){.pf-ref} and [](#s3-3){.pf-ref}.

:::

:::

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::
