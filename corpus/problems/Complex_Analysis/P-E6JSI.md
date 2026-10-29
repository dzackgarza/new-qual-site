---
schema: qual/card@1
id: P-E6JSI
kind: problem
title: Schwarz reflection of a holomorphic function across the diameter of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Holomorphic Functions
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
Let $S \coloneqq \{z \in \DD \mid \operatorname{Im}(z) \ge 0\}$ be the closed upper half of the unit disk $\DD$.
Suppose $f: S \to \CC$ is continuous on $S$, real-valued on $S \cap \RR = (-1, 1)$, and holomorphic on the interior $S^\circ = \{z \in \DD \mid \operatorname{Im}(z) > 0\}$.

Prove that $f$ extends to a holomorphic function on the entire unit disk $\DD$ (the Schwarz Reflection Principle).
:::

::: {.solution}

Define $F:\DD\to\CC$ by $F(z)\coloneqq f(z)$ for $\Im z\ge0$ and $F(z)\coloneqq\overline{f(\bar z)}$ for $\Im z<0$.

::: pf

::: {.pf-step #continuous}
$F$ is continuous on $\DD$.

::: pf-proof
Each formula is continuous on its closed half of $\DD$, and on $(-1,1)$ they agree because $\overline{f(x)}=f(x)$ for real $x$.
:::

:::

::: {.pf-step #off-axis}
$F$ is holomorphic on $\DD\setminus\RR$.

::: pf-proof
On the upper half-disc $F=f$.
On the lower half-disc, $F(z)=\overline{f(\bar z)}$ has complex derivative $\overline{f'(\bar z)}$, since $\frac{F(z+h)-F(z)}{h}=\overline{\left(\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}\right)}$.
:::

:::

::: pf-step
$F$ is holomorphic on $\DD$ and extends $f$.

::: pf-proof
By steps [](#continuous){.pf-ref} and [](#off-axis){.pf-ref}, $F$ is continuous on $\DD$ and holomorphic off the line $\RR$, so it is holomorphic on $\DD$ by the Morera argument of [[P-B4WQK]]: $\int_{\partial\Delta}F=0$ for every triangle $\Delta\subset\DD$, because a triangle with a side or vertex on $\RR$ is a limit of triangles translated off $\RR$, and a triangle crossing $\RR$ splits into triangles of those two kinds.
By construction $F=f$ on $S$.
:::

:::

:::

:::
