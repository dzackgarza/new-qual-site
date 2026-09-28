---
schema: qual/card@1
id: E-7I6BT
kind: problem
title: Closures of intervals in finer topologies on the line
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the lower limit topology on $\mathbb{R}$ and the topology given by the basis $\mathcal{C}$ of Exercise 8 of §13. Determine the closures of the intervals $A = (0, \sqrt{2})$ and $B = (\sqrt{2}, 3)$ in these two topologies.
:::

::: {.solution}
Let $\mathcal T_{\mathcal C}$ be the topology with basis $\mathcal C=\{[a,b):a<b,\ a,b\in\mathbb Q\}$ of [[E-NKQY9]].
Both $\mathbb R_\ell$ and $\mathcal T_{\mathcal C}$ are finer than the standard topology, so each closure lies in the standard closure: $\overline A\subseteq[0,\sqrt2]$ and $\overline B\subseteq[\sqrt2,3]$.
A point $x$ lies in the closure of a set $S$ if and only if every basic open set containing $x$ meets $S$.

<1>1. In $\mathbb R_\ell$, $\overline A=\boxed{[0,\sqrt2)}$.

::: {.proof}
Every basic set $[c,d)$ containing $0$ meets $A$ in $(0,\min(d,\sqrt2))\ne\varnothing$, so $0\in\overline A$; the points of $(0,\sqrt2)$ lie in $A$.
The basic set $[\sqrt2,2)$ contains $\sqrt2$ and misses $A$, so $\sqrt2\notin\overline A$.
:::

<1>2. In $\mathbb R_\ell$, $\overline B=\boxed{[\sqrt2,3)}$.

::: {.proof}
Every basic set $[c,d)$ containing $\sqrt2$ has $c\le\sqrt2<d$ and meets $B$ in $(\sqrt2,\min(d,3))\ne\varnothing$, so $\sqrt2\in\overline B$.
The basic set $[3,4)$ contains $3$ and misses $B$, so $3\notin\overline B$.
:::

<1>3. A basic set $[a,b)\in\mathcal C$ containing an irrational number $z$ satisfies $a<z<b$.

::: {.proof}
$a\le z<b$ and $a\ne z$ because $a$ is rational.
:::

<1>4. In $\mathcal T_{\mathcal C}$, $\overline A=\boxed{[0,\sqrt2]}$.

::: {.proof}
Every $[a,b)\in\mathcal C$ containing $0$ meets $A$ in $(0,\min(b,\sqrt2))\ne\varnothing$, so $0\in\overline A$.
By step <1>3, every $[a,b)\in\mathcal C$ containing $\sqrt2$ has $a<\sqrt2$ and so meets $A$ in $(\max(0,a),\sqrt2)\ne\varnothing$; hence $\sqrt2\in\overline A$.
:::

<1>5. In $\mathcal T_{\mathcal C}$, $\overline B=\boxed{[\sqrt2,3)}$.

::: {.proof}
Every $[a,b)\in\mathcal C$ containing $\sqrt2$ has $\sqrt2<b$ and so meets $B$ in $(\sqrt2,\min(b,3))\ne\varnothing$; hence $\sqrt2\in\overline B$.
The set $[3,4)\in\mathcal C$ contains $3$ and misses $B$, so $3\notin\overline B$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the closures in $\mathbb R_\ell$, and steps <1>4 and <1>5 give the closures in $\mathcal T_{\mathcal C}$.
:::
:::
