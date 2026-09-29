---
schema: qual/card@1
id: E-AMD-DGMOEV2O
kind: problem
title: $P\cap H\in\syl_p(H)$ for $P\in\syl_p(G)$ and $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
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

::: {.exercise}
Let $P\in \operatorname{Syl}_p(G)$ where $H\trianglelefteq G$ and show that $P\cap H \in \operatorname{Syl}_p(H)$.
:::

::: {.solution}
Let \(P\in\operatorname{Syl}_p(G)\) and \(H\trianglelefteq G\).

::: pf

::: {.pf-step #p-cap-h-is-p-subgroup}
The subgroup \(P\cap H\) is a \(p\)-subgroup of \(H\).

::: pf-proof
It is a subgroup of the \(p\)-group \(P\), so its order is a power of \(p\).
:::

:::

::: {.pf-step #p-cap-h-index-prime-to-p}
Its index in \(H\) is prime to \(p\).

::: pf-proof
Since \(H\trianglelefteq G\), the product \(PH\) is a subgroup. The product formula gives
\[
|PH|=\frac{|P||H|}{|P\cap H|}.
\]
Hence
\[
[H:P\cap H]
=\frac{|H|}{|P\cap H|}
=\frac{|PH|}{|P|}
=[PH:P].
\]
Because \(P\le PH\le G\),
\[
[G:P]=[G:PH][PH:P].
\]
Thus \([H:P\cap H]=[PH:P]\) divides \([G:P]\). Since \(P\) is Sylow, \([G:P]\) is prime to \(p\), so \([H:P\cap H]\) is prime to \(p\).
:::

:::

::: pf-qed
A \(p\)-subgroup of \(H\) whose index is prime to \(p\) has the full \(p\)-part of \(|H|\). By steps [](#p-cap-h-is-p-subgroup){.pf-ref} and [](#p-cap-h-index-prime-to-p){.pf-ref}, therefore
\[
\boxed{P\cap H\in\operatorname{Syl}_p(H).}
\]
:::

:::

:::
