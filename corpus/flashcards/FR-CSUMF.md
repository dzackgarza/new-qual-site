---
schema: qual/card@1
id: FR-CSUMF
kind: proof
title: Proof of Borel-Cantelli Lemma
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.proof}
*Proof of Borel Cantelli:*

- If $E = \limsup_j E_j$ with $\sum m(E_j) < \infty$ then $m(E) = 0$.

- If $E_j$ are measurable, then $\limsup_j E_j$ is measurable.

- If $\sum_j m(E_j) < \infty$, then $\sum_{j=N}^\infty m(E_j) \converges{N\to\infty}\to 0$ as the tail of a convergent sequence.

- $$E = \limsup_j E_j = \intersect_{k=1}^\infty \union_{j=k}^\infty E_j \implies E \subseteq \union_{j=k}^\infty E_j \quad \forall k $$

- $$E \subset \union_{j=k}^\infty E_j \implies m(E) \leq \sum_{j=k}^\infty m(E_j) \converges{k\to\infty}\to 0.$$
:::
