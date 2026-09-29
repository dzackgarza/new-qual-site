---
schema: qual/card@1
id: E-AMD-DCVAD27P
kind: problem
title: The union of all maximal ideals is the set of non-units
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Rings
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
Show that $\bigcup_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m} = R \setminus R^\times$.
:::

::: {.solution}

::: pf

::: {.pf-step #maximal-ideal-elements-are-nonunits}
Every element of a maximal ideal is a nonunit.

::: pf-proof
Let \(\mathfrak m\) be maximal and let \(x\in\mathfrak m\). If \(x\) were a unit, then
\[
1=x^{-1}x\in\mathfrak m,
\]
contradicting that \(\mathfrak m\) is proper. Hence
\[
\bigcup_{\mathfrak m\in\operatorname{MaxSpec}(R)}\mathfrak m
\subseteq R\setminus R^\times.
\]
:::

:::

::: {.pf-step #nonunits-lie-in-maximal-ideal}
Every nonunit belongs to a maximal ideal.

::: pf-proof
Let \(x\in R\) be a nonunit. Then \((x)\ne R\), so \((x)\) is a proper ideal. Every proper ideal of a ring with identity is contained in a maximal ideal (Zorn's lemma), so \((x)\) is contained in some maximal ideal \(\mathfrak m\). Thus \(x\in\mathfrak m\), and therefore
\[
R\setminus R^\times
\subseteq
\bigcup_{\mathfrak m\in\operatorname{MaxSpec}(R)}\mathfrak m.
\]
:::

:::

::: pf-qed
Combining steps [](#maximal-ideal-elements-are-nonunits){.pf-ref} and [](#nonunits-lie-in-maximal-ideal){.pf-ref} gives
\[
\boxed{\bigcup_{\mathfrak m\in\operatorname{MaxSpec}(R)}\mathfrak m=R\setminus R^\times.}
\]
:::

:::

:::
