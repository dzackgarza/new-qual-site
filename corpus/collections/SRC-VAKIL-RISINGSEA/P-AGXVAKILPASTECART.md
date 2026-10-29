---
schema: qual/card@1
id: P-AGXVAKILPASTECART
kind: problem
title: Pasting two cartesian squares gives a cartesian outer square
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fiber Products
  - Pasting Lemma
  - Universal Properties
relations: []
review: draft
---

::: {.problem}
Show that if the two squares in this diagram are cartesian, then the outer square is also cartesian:

\begin{tikzcd}
	U \ar[r]\ar[d] & V\ar[d] \\
	W \ar[r]\ar[d] & X\ar[d] \\
	Y \ar[r] & Z
\end{tikzcd}
:::

::: {.solution}
Name the maps $p : U\to V$, $q : U\to W$, $v : V\to X$, $w : W\to X$, $r : W\to Y$, $x : X\to Z$, and $y : Y\to Z$.
The squares commute, so $vp = wq$ and $xw = yr$.
The outer square has sides $xv : V\to Z$ and $rq : U\to Y$, and it commutes because $xvp = xwq = yrq$.
To show it is cartesian, fix an object $T$ and maps $\alpha : T\to V$ and $\beta : T\to Y$ with $xv\alpha = y\beta$.

::: pf

::: {.pf-step #bottom}
There is a unique $\gamma : T\to W$ with $w\gamma = v\alpha$ and $r\gamma = \beta$.

::: pf-proof
The maps $v\alpha : T\to X$ and $\beta : T\to Y$ satisfy $x(v\alpha) = y\beta$, so the bottom square, which is cartesian, gives a unique such $\gamma$.
:::

:::

::: {.pf-step #top}
There is a unique $\delta : T\to U$ with $p\delta = \alpha$ and $q\delta = \gamma$.

::: pf-proof
The maps $\alpha : T\to V$ and $\gamma : T\to W$ satisfy $v\alpha = w\gamma$ by step [](#bottom){.pf-ref}, so the top square, which is cartesian, gives a unique such $\delta$.
:::

:::

::: {.pf-step #existence}
$\delta$ satisfies $p\delta = \alpha$ and $rq\delta = \beta$.

::: pf-proof
By steps [](#top){.pf-ref} and [](#bottom){.pf-ref}, $p\delta = \alpha$ and $rq\delta = r\gamma = \beta$.
:::

:::

::: {.pf-step #uniqueness}
If $\delta' : T\to U$ satisfies $p\delta' = \alpha$ and $rq\delta' = \beta$, then $\delta' = \delta$.

::: pf-proof
The map $q\delta' : T\to W$ satisfies $w(q\delta') = vp\delta' = v\alpha$ and $r(q\delta') = \beta$, so $q\delta' = \gamma$ by the uniqueness in step [](#bottom){.pf-ref}.
Then $p\delta' = \alpha$ and $q\delta' = \gamma$, so $\delta' = \delta$ by the uniqueness in step [](#top){.pf-ref}.
:::

:::

::: pf-qed
For every $T$ and every pair $\alpha, \beta$ with $xv\alpha = y\beta$, steps [](#existence){.pf-ref} and [](#uniqueness){.pf-ref} give exactly one $\delta : T\to U$ with $p\delta = \alpha$ and $rq\delta = \beta$.
This is the universal property of $U = V\times_Z Y$, so the outer square is cartesian.
:::

:::
:::
