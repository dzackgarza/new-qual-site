---
schema: qual/card@1
id: P-RVG47
kind: problem
title: A Lie group with no faithful finite-dimensional representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Do you know a Lie group that has no faithful finite-dimensional representation?
:::

::: {.solution}

Let $G=\widetilde{\SL_2(\RR)}$ be the universal covering group of $\SL_2(\RR)$, with covering homomorphism $p\colon G\to\SL_2(\RR)$. Its kernel is central and $\ker p\cong\pi_1(\SL_2(\RR))\cong\ZZ$. Let $\rho\colon G\to\GL(V)$ be a finite-dimensional continuous representation; replacing a real $V$ by $V\otimes_\RR\CC$, we may take $V$ complex.

::: pf

::: {.pf-step #factor}

There is a representation $\rho'$ of $\SL_2(\RR)$ with $d(\rho'\circ p)=d\rho$.

::: pf-proof

The differential $d\rho\colon\mathfrak{sl}_2(\RR)\to\mathfrak{gl}(V)$ extends complex-linearly to a representation of $\mathfrak{sl}_2(\CC)$. Since $\SL_2(\CC)$ is simply connected, this integrates to a representation of $\SL_2(\CC)$; let $\rho'$ be its restriction to $\SL_2(\RR)$. The differential of $\rho'\circ p$ is the restriction of the $\mathfrak{sl}_2(\CC)$-representation to $\mathfrak{sl}_2(\RR)$, which is $d\rho$.

:::

:::

::: {.pf-step #equal}

$\rho=\rho'\circ p$.

::: pf-proof

$G$ is connected and simply connected, so a finite-dimensional representation of $G$ is determined by its differential. Step [](#factor){.pf-ref} shows that the two representations have the same differential.

:::

:::

::: pf-qed

By step [](#equal){.pf-ref}, $\ker p\subseteq\ker\rho$, and $\ker p\cong\ZZ$ is nontrivial. Hence no finite-dimensional representation of $G$ is faithful, and $\boxed{\widetilde{\SL_2(\RR)}}$ is a connected Lie group with no faithful finite-dimensional representation.

:::

:::

:::
