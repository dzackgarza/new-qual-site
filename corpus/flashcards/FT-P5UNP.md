---
schema: qual/card@1
id: FT-P5UNP
kind: theorem
title: Fatou's Lemma
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
relations: []
review: draft
---

::: {.theorem title="Fatou's Lemma"}
If $\theset{f_n} \subset L^+$, then
$$
\int \liminf f_n \leq \liminf \int f_n
$$

- Pulling the limit out makes it bigger

- Pushing the limit in means integrating a smaller function, making the whole thing smaller.
:::
