---
schema: qual/card@1
id: E-AMD-EBIC3Z5S
kind: problem
title: If $\spec(R)\subseteq\maxspec(R)$ then $R$ is a UFD
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $\operatorname{Spec}(R) \subseteq \operatorname{MaxSpec}(R)$ and $R$ is an integral domain, then $R$ is a UFD.
:::

::: solution
**Goal:** Prove that if $R$ is an integral domain such that every prime ideal is maximal ($\operatorname{Spec}(R) \subseteq \operatorname{MaxSpec}(R)$), then $R$ is a field, and hence a Unique Factorization Domain (UFD).

<1>1. The zero ideal is prime:
    *Proof:*
    <2>1. By definition, a Unique Factorization Domain is an integral domain.
    <2>2. Because $R$ is an integral domain ($ab = 0 \implies a = 0 \text{ or } b = 0$), the zero ideal $(0)$ is a prime ideal of $R$.
    <2>3. Thus $(0) \in \operatorname{Spec}(R)$.

<1>2. The zero ideal is maximal:
    *Proof:*
    <2>1. By the hypothesis $\operatorname{Spec}(R) \subseteq \operatorname{MaxSpec}(R)$, every prime ideal is maximal.
    <2>2. Since $(0) \in \operatorname{Spec}(R)$, it follows that $(0) \in \operatorname{MaxSpec}(R)$.
    <2>3. An ideal $I \subseteq R$ is maximal if and only if the quotient ring $R / I$ is a field.
    <2>4. For $I = (0)$, $R / (0) \cong R$ is a field.

<1>3. Conclusion:
    <2>1. Every field is a Unique Factorization Domain (every non-zero element is a unit, so factorization into irreducible elements is vacuously unique).
    <2>2. Therefore $R$ is a UFD. Q.E.D.
:::
