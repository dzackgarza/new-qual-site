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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Prove that a projective $R$-module is flat.

Hint: First prove the case for a free $R$-module.
:::

::: {.solution}
<1>1. A free $R$-module is flat.
<2>1. A free module $R^{(I)}$ is a direct sum of copies of $R$.
Proof: definition.
<2>2. $R$ is flat: tensoring with $R$ is the identity functor, which is exact.
Proof: $R \otimes_R M \cong M$ naturally.
<2>3. A direct sum of flat modules is flat.
Proof: tensor product commutes with direct sums, and a direct sum of exact sequences is exact.
<2>4. Hence $R^{(I)}$ is flat.
Proof: <2>1–<2>3.

<1>2. A projective module $P$ is a direct summand of a free module: $P \oplus Q \cong R^{(I)}$.
Proof: characterization of projective modules.

<1>3. A direct summand of a flat module is flat.
<2>1. Let $0 \to M' \to M \to M'' \to 0$ be exact.
Proof: take an arbitrary short exact sequence.
<2>2. $0 \to (P \oplus Q) \otimes M' \to (P \oplus Q) \otimes M \to (P \oplus Q) \otimes M'' \to 0$ is exact.
Proof: $P \oplus Q \cong R^{(I)}$ is flat (<1>1).
<2>3. This sequence is the direct sum of the sequences for $P$ and for $Q$, so the $P$-sequence $0 \to P \otimes M' \to P \otimes M \to P \otimes M'' \to 0$ is exact.
Proof: a direct summand of an exact sequence is exact.
<2>4. Hence $P$ is flat.
Proof: <2>1–<2>3.

<1>4. Q.E.D.
Proof: <1>2 and <1>3.
:::
