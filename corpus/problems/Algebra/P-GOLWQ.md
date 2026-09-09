---
schema: qual/card@1
id: P-GOLWQ
kind: problem
title: A field homomorphism is zero or injective
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
- Show that any field morphism is either 0 or injective.
:::

::: solution
Let $\phi:F	o R$ be a ring homomorphism with $F$ a field. Its kernel is an ideal of $F$. A field has only the ideals $(0)$ and $F$, so either
\[
\ker\phi=(0)
\]
or
\[
\ker\phi=F.
\]
In the first case $\phi$ is injective. In the second case $\phi(x)=0$ for every $x\in F$, so $\phi$ is the zero map. Thus every ring homomorphism from a field is either zero or injective.

If ring homomorphisms are required to preserve $1$, the zero case is excluded whenever $R
e0$.
:::
