---
schema: qual/card@1
id: E-20CHL
kind: problem
title: Continuity implies separate continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $F: X \times Y \to Z$.
We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \to Z$ defined by $h(x) = F(x \times y_0)$ is continuous, and for each $x_0$ in $X$, the map $k: Y \to Z$ defined by $k(y) = F(x_0 \times y)$ is continuous.
Show that if $F$ is continuous, then $F$ is continuous in each variable separately.
:::

::: {.solution}
For $y_0\in Y$ let $i_{y_0}\colon X\to X\times Y$, $i_{y_0}(x)=(x,y_0)$, and for $x_0\in X$ let $j_{x_0}\colon Y\to X\times Y$, $j_{x_0}(y)=(x_0,y)$.

<1>1. The maps $i_{y_0}$ and $j_{x_0}$ are continuous.

::: {.proof}
A map into $X\times Y$ is continuous if and only if its compositions with the projections $\pi_X$ and $\pi_Y$ are continuous.
Here $\pi_X\circ i_{y_0}=\operatorname{id}_X$ and $\pi_Y\circ i_{y_0}$ is the constant map at $y_0$; likewise $\pi_X\circ j_{x_0}$ is constant at $x_0$ and $\pi_Y\circ j_{x_0}=\operatorname{id}_Y$.
Identity and constant maps are continuous.
:::

<1>2. Q.E.D.

::: {.proof}
The maps of the problem are $h=F\circ i_{y_0}$ and $k=F\circ j_{x_0}$, composites of continuous maps by step <1>1 and the hypothesis on $F$.
:::
:::
