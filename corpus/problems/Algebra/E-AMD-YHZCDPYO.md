---
schema: qual/card@1
id: E-AMD-YHZCDPYO
kind: problem
title: $\mathrm{rad}(IJ)=\mathrm{rad}(I)\cap\mathrm{rad}(J)$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that $\text{rad}(IJ) = \text{rad}(I) \intersect \text{rad}(J)$
:::


::: {.solution}

::: pf

::: {.pf-step #rad-ij-subset-cap}
One has $\operatorname{rad}(IJ)\subseteq\operatorname{rad}(I)\cap\operatorname{rad}(J)$.

::: pf-proof
Since $IJ\subseteq I$ and $IJ\subseteq J$, monotonicity of radicals gives
\[
\operatorname{rad}(IJ)\subseteq\operatorname{rad}(I),
\qquad
\operatorname{rad}(IJ)\subseteq\operatorname{rad}(J).
\]
Hence
\[
\operatorname{rad}(IJ)\subseteq\operatorname{rad}(I)\cap\operatorname{rad}(J).
\]
:::

:::

::: {.pf-step #cap-subset-rad-ij}
One has $\operatorname{rad}(I)\cap\operatorname{rad}(J)\subseteq\operatorname{rad}(IJ)$.

::: pf-proof
Let $x\in\operatorname{rad}(I)\cap\operatorname{rad}(J)$. Then for some integers $m,n\ge1$,
\[
x^m\in I,
\qquad
x^n\in J.
\]
Therefore
\[
x^{m+n}=x^m x^n\in IJ,
\]
so $x\in\operatorname{rad}(IJ)$.
:::

:::

::: pf-step
Therefore
\[
\operatorname{rad}(IJ)=\operatorname{rad}(I)\cap\operatorname{rad}(J).
\]

::: pf-proof
Combine steps [](#rad-ij-subset-cap){.pf-ref} and [](#cap-subset-rad-ij){.pf-ref}.
:::

:::

:::

:::
