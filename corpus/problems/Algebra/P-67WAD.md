---
schema: qual/card@1
id: P-67WAD
kind: problem
title: The splitting field of $x^3-2$ is $\QQ(\sqrt[3]{2},\zeta_3)$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Roots of Unity
  - Field Extensions
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
Show that the splitting field of $f(x) = x^3-2$ over $\QQ$ is $\QQ(\sqrt[3]{2}, \zeta_3)$ (where $\zeta_3 = e^{2\pi i/3}$).
:::

::: {.solution}
Let $\alpha=\sqrt[3]{2}$, let $L$ be the splitting field of $x^3-2$ over $\QQ$ in $\CC$, and let $K=\QQ(\alpha,\zeta_3)$.

::: pf

::: {.pf-step #roots}
The roots of $x^3-2$ are $\alpha$, $\zeta_3\alpha$ and $\zeta_3^2\alpha$.

::: pf-proof
Each is a root because $\zeta_3^3=1$, and they are distinct because $\alpha\ne0$ and $1,\zeta_3,\zeta_3^2$ are distinct.
:::

:::

::: pf-step
$L\subseteq K$.

::: pf-proof
$K$ contains all roots listed in step [](#roots){.pf-ref}, and $L$ is generated over $\QQ$ by those roots.
:::

:::

::: pf-step
$K\subseteq L$, so $L=\QQ(\sqrt[3]{2},\zeta_3)$.

::: pf-proof
$L$ contains $\alpha$ and $\zeta_3\alpha$ by step [](#roots){.pf-ref}, hence also $\zeta_3=\zeta_3\alpha/\alpha$.
:::

:::

:::

:::

::: {.remark}
$[L:\QQ]=6$: $[\QQ(\alpha):\QQ]=3$ by Eisenstein at $2$, and $\zeta_3\notin\RR\supset\QQ(\alpha)$ is a root of $x^2+x+1$, so adjoining it has degree $2$.
:::
