---
schema: qual/card@1
id: P-FO36C
kind: problem
title: Lower and upper central series, nilpotent groups, and solvable groups
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Define lower central series, upper central series, nilpotent and solvable groups.
:::

::: {.solution}
<1>1. The **lower central series** of $G$ is $G = \gamma_1(G) \ge \gamma_2(G) \ge \cdots$, where $\gamma_{i+1}(G) = [\gamma_i(G), G]$.
::: {.proof}
definition of the lower central series.
:::

<1>2. The **upper central series** of $G$ is $1 = Z_0(G) \le Z_1(G) \le \cdots$, where $Z_{i+1}(G)/Z_i(G) = Z(G/Z_i(G))$.
::: {.proof}
definition of the upper central series.
:::

<1>3. $G$ is **nilpotent** if the lower central series reaches $1$ (equivalently, the upper central series reaches $G$).
::: {.proof}
definition of nilpotent.
:::

<1>4. The **derived series** of $G$ is $G = G^{(0)} \ge G^{(1)} \ge \cdots$, where $G^{(i+1)} = [G^{(i)}, G^{(i)}]$.
::: {.proof}
definition of the derived series.
:::

<1>5. $G$ is **solvable** if the derived series reaches $1$.
::: {.proof}
definition of solvable.
:::

<1>6. Q.E.D.
::: {.proof}
<1>1–<1>5.
:::
:::
