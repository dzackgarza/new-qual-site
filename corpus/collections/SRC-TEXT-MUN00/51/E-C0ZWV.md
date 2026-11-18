---
schema: qual/card@1
id: E-C0ZWV
kind: problem
title: Homotopy classes into an interval and out of a path-connected space
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The claim that [I,Y] has one class requires Y nonempty if path connectedness is allowed to hold vacuously for the empty space.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 51: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-51-homotopy-of-paths/problem-2-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-51-homotopy-of-paths/problem-2-solution.txt),
    and against Munkres, Topology (2000), Section 51 Exercise 2, printed p. 330. dbFin gives (a) as the straight-line homotopy into the convex interval and (b) in one sentence, that a segment of a path is homotopic to the path and that path-connectedness lets one join the two; the card writes both out. What was corrected: the stored statement had added the word nonempty to part (b). The book prints "Show that if Y is path connected, the set [I,Y] has a single element", and Munkres's definition of path connected quantifies over pairs of points, so the empty space satisfies it vacuously while [I,empty] is empty, not a singleton. The printed wording is restored and the solution now names the point of Y that the argument needs and records that Y empty is the one exception.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same two parts. The reading confirmed that the argument for
    (b) does not smuggle in the nonemptiness it needs: it chooses a path between the values of two given
    maps, so it applies to every nonempty path connected Y, and the card now says so at the step where
    the choice is made and again at the last step, where the empty space is named as the one exception to
    the printed statement. Continuity of the straight-line homotopy and of the constant homotopy is
    justified rather than asserted. The statement is unchanged and remains the printed one; checked
    against Munkres, Topology (2000), Section 51 Exercise 2, printed p. 330.
---

::: {.exercise}

Given spaces $X$ and $Y$, let $[X, Y]$ denote the set of homotopy classes of maps of $X$ into $Y$.

(a) Let $I = [0, 1]$.
Show that for any $X$, the set $[X, I]$ has a single element.

(b) Show that if $Y$ is path connected, the set $[I, Y]$ has a single element.
:::

::: {.solution}

The argument is the one located in **dbFin, "Section 51: Problem 2 Solution"** (`tmp/sources/dbfin/section-51-homotopy-of-paths/problem-2-solution.txt`), which gives (a) as the straight-line homotopy into the convex interval and (b) in a sentence; both are written out here.

The statement was checked against Munkres, *Topology* (2000), §51 Exercise 2, printed p. 330, with the definition of homotopy of maps on printed p. 323 and that of a path connected space in §24. Part (b) is stated as the book prints it, with no nonemptiness hypothesis, and the solution records where that matters: Munkres defines a path connected space by a condition on *pairs* of points, so the empty space satisfies it vacuously, while $[I,\varnothing]$ is empty rather than a singleton. Every nonempty path connected $Y$ is covered by the argument, which begins by choosing a path between the values of two given maps.

Throughout, $I=[0,1]$, $[X,Y]$ is the set of homotopy classes of maps $X\to Y$, and two maps $f,g\colon X\to Y$ are homotopic when there is a continuous $H\colon X\times I\to Y$ with $H(x,0)=f(x)$ and $H(x,1)=g(x)$; $c_{y}$ denotes the constant map at $y$.

::: pf

::: {.pf-step #a}

(a) For every space $X$ the set $[X,I]$ has a single element.

:::: pf-proof

Let $f,g\colon X\to I$ be two maps into the interval.

::: {.pf-step #straight-line}

$H(x,t)\coloneqq(1-t)f(x)+tg(x)$ defines a continuous map $X\times I\to I$ with $H(x,0)=f(x)$ and $H(x,1)=g(x)$.

::: pf-proof

Each of the maps $(x,t)\mapsto f(x)$, $(x,t)\mapsto g(x)$ and $(x,t)\mapsto t$ is continuous on $X\times I$ — the first two as composites of $f$ and $g$ with the projection (Theorem 18.4), the third as a projection — so their products and sum are continuous (Theorem 21.5). Its values lie in $I$ because $I$ is convex: for $u,v\in[0,1]$ and $t\in[0,1]$ the convex combination $(1-t)u+tv$ lies in $[0,1]$. The two endpoint computations are immediate.

:::

:::

::: pf-step

Any two maps $X\to I$ are homotopic, so $[X,I]$ has exactly one element.

::: pf-proof

Given $f,g\colon X\to I$, step [](#straight-line){.pf-ref} supplies a homotopy from $f$ to $g$. Homotopy is an equivalence relation on the maps $X\to I$, so all of them lie in one class; and there is at least one such map, for instance the constant map at $0$. Hence $[X,I]$ has a single element.

:::

:::

::::

:::

::: {.pf-step #b}

(b) For a nonempty path connected space $Y$ the set $[I,Y]$ has a single element.

:::: pf-proof

Let $f,g\colon I\to Y$ be two maps; they exist because $Y$ is nonempty and every point of $Y$ gives a constant map.

::: {.pf-step #interval-to-constant}

$f\simeq c_{f(0)}$ and $g\simeq c_{g(0)}$.

::: pf-proof

The map $F\colon I\times I\to Y$, $F(s,t)\coloneqq f\big((1-t)s\big)$, is continuous, being a composite of $f$ with the continuous map $(s,t)\mapsto(1-t)s$ of $I\times I$ into $I$ (Theorems 18.4 and 21.5); moreover $F(s,0)=f(s)$ and $F(s,1)=f(0)$, so $F$ is a homotopy from $f$ to the constant map $c_{f(0)}$. The same formula with $g$ in place of $f$ homotopes $g$ to $c_{g(0)}$.

:::

:::

::: {.pf-step #constants}

If $Y$ is nonempty and path connected, then $c_{f(0)}\simeq c_{g(0)}$.

::: pf-proof

By path connectedness there is a path $\alpha\colon I\to Y$ from $f(0)$ to $g(0)$, that is a continuous map with $\alpha(0)=f(0)$ and $\alpha(1)=g(0)$. The map $A\colon I\times I\to Y$, $A(s,t)\coloneqq\alpha(t)$, is continuous, being a composite of $\alpha$ with the projection onto the second factor, and $A(s,0)=f(0)$, $A(s,1)=g(0)$; so $A$ is a homotopy from $c_{f(0)}$ to $c_{g(0)}$.

:::

:::

::::

:::

::: pf-step

Therefore $[X,I]$ has a single element for every $X$, and $[I,Y]$ has a single element for every nonempty path connected $Y$; the empty space is the one exception to the printed statement of (b).

::: pf-proof

Part [](#a){.pf-ref} is the first assertion. For the second, let $Y$ be nonempty and path connected and let $f,g\colon I\to Y$: step [](#b){.pf-ref} gives $f\simeq c_{f(0)}$ and $g\simeq c_{g(0)}$ by step [](#interval-to-constant){.pf-ref}, and $c_{f(0)}\simeq c_{g(0)}$ by step [](#constants){.pf-ref}, so $f$ and $g$ are homotopic and $[I,Y]$ has one element. For $Y=\varnothing$ the space is path connected vacuously, no map $I\to\varnothing$ exists, and $[I,\varnothing]=\varnothing$ is not a singleton; that is the single case the printed statement does not cover.

:::

:::

:::

:::
