---
schema: qual/card@1
id: P-7ALW6
kind: problem
title: Galois group of $\QQ(\sqrt{2},\sqrt{3})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
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
What is the Galois group of $\QQ(\sqrt{2}, \sqrt{3}) / \QQ$?
:::

::: {.solution}
Let $K=\QQ(\sqrt2,\sqrt3)$.

::: pf

::: {.pf-step #degree}
$K/\QQ$ is Galois of degree $4$.

::: pf-proof
$K$ is the splitting field of $(x^2-2)(x^2-3)$, so $K/\QQ$ is Galois. If $\sqrt3=a+b\sqrt2$ with $a,b\in\QQ$, squaring gives $2ab\sqrt2=3-a^2-2b^2$, so $ab=0$; $b=0$ makes $\sqrt3$ rational and $a=0$ makes $\sqrt{3/2}$ rational, both false. Hence $\sqrt3\notin\QQ(\sqrt2)$ and $[K:\QQ]=2\cdot2=4$.
:::

:::

::: pf-step
$\Gal(K/\QQ)\cong\boxed{C_2\times C_2}$.

::: pf-proof
A $\QQ$-automorphism maps $\sqrt2\mapsto\pm\sqrt2$ and $\sqrt3\mapsto\pm\sqrt3$ and is determined by these two signs. By step [](#degree){.pf-ref} there are $4$ automorphisms, so all four sign choices occur. Each nonidentity automorphism squares to the identity, so the group of order $4$ has no element of order $4$.
:::

:::

:::

:::
