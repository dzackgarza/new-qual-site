---
schema: qual/card@1
id: FD-OFT7I
kind: definition
title: 'Definition: Measurable Function'
prompts:
- Which preimages must be measurable for $f$ to be a measurable function?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
$f:\RR \to \bar \RR$ is Lebesgue/Borel measurable iff
$$
\{x \in E \mid f(x)>a\}=f^{-1}((a, \infty]) \in \mathcal{M}_L, \mathcal{M}_B
,$$
the collection of Lebesgue/Borel measurable *sets* respectively.

> Mnemonic: preimage of a ray should be a measurable set.
:::
