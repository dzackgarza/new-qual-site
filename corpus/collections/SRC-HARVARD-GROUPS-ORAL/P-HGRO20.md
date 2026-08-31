---
schema: qual/card@1
id: P-HGRO20
kind: problem
title: A subgroup of least prime index is normal
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $H\leq G$, where $G$ is finite.
Suppose $[G:H]$ is the smallest prime that divides $|G|$.
Prove that $H$ is normal in $G$.
:::

::: {.solution}
<1>1. $G$ acts on $G/H$ by left multiplication, giving $\varphi:G\to S_{[G:H]}$.
::: {.proof}
action.
:::

<1>2. $\ker\varphi =\bigcap_{g}gHg^{-1}$ is the core, $\ker\varphi\le H$.
::: {.proof}
core.
:::

<1>3. $[G:\ker\varphi]$ divides $[G:H]! =p!$ where $p=[G:H]$ is smallest prime dividing $|G|$.
::: {.proof}
$|\operatorname{im}\varphi|$ divides $p!$.
:::

<1>4. $[G:\ker\varphi]$ is divisible by $p$ and its prime divisors divide $|G|$, but $p$ is smallest, so $[G:\ker\varphi]=p$.
::: {.proof}
<1>3.
:::

<1>5. Hence $[H:\ker\varphi]=1$, so $\ker\varphi=H$, so $H$ normal.
::: {.proof}
$[G:H]=p=[G:\ker\varphi]$ and $\ker\varphi\le H$.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
