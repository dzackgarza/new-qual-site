---
schema: qual/card@1
id: E-CGVE4
kind: exercise
title: "- Show that a countable union of null sets is null."
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
---

::: exercise
- Show that a countable union of null sets is null.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that a countable union of null sets is null.

<1>1. Let $\{N_n\}$ be null sets, i.e. $\mu(N_n) = 0$ for all $n$.
    Proof: setup.
<1>2. $\mu\!\left(\bigcup_n N_n\right) \leq \sum_n \mu(N_n)$.
    Proof: countable subadditivity of the measure.
<1>3. $\sum_n \mu(N_n) = 0$, so $\mu(\bigcup_n N_n) = 0$.
    Proof: each term is $0$ by hypothesis; a measure is nonnegative, so $\mu(\bigcup_n N_n) \geq 0$ and <1>2 forces it to be $0$.
<1>4. Q.E.D.
    Proof: <1>3 says the union is null.
:::
