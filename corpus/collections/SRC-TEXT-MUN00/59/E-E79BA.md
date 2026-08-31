---
schema: qual/card@1
id: E-E79BA
kind: exercise
title: Euclidean spaces of different dimensions are not homeomorphic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

(a) Show that $\mathbb{R}^1$ and $\mathbb{R}^n$ are not homeomorphic if $n > 1$.

(b) Show that $\mathbb{R}^2$ and $\mathbb{R}^n$ are not homeomorphic if $n > 2$.

It is, in fact, true that $\mathbb{R}^m$ and $\mathbb{R}^n$ are not homeomorphic if $n \neq m$, but the proof requires more advanced tools of algebraic topology.
:::

::: {.solution}
**Goal.** Show $\RR^1 \not\cong \RR^n$ for $n > 1$ and $\RR^2 \not\cong \RR^n$ for $n > 2$.

<1>1. (a) $\RR^1 \not\cong \RR^n$ for $n > 1$.
<2>1. Removing a point from $\RR^1$ gives a disconnected space.
::: {.proof}
$\RR^1 \sm \theset{0} = (-\infty, 0) \cup (0, \infty)$ is disconnected.
:::
<2>2. Removing a point from $\RR^n$ ($n > 1$) gives a connected space.
::: {.proof}
$\RR^n \sm \theset{0}$ is path-connected (any two points can be joined by a path avoiding the origin).
:::
<2>3. Hence $\RR^1 \not\cong \RR^n$.
::: {.proof}
connectedness is a homeomorphism invariant, and a homeomorphism would preserve the number of connected components after removing a point.
:::

<1>2. (b) $\RR^2 \not\cong \RR^n$ for $n > 2$.
<2>1. $\RR^2 \sm \theset{0}$ is not simply connected.
::: {.proof}
$\RR^2 \sm \theset{0}$ deformation-retracts onto $S^1$, so $\pi_1(\RR^2 \sm \theset{0}) = \ZZ \neq 0$.
:::
<2>2. $\RR^n \sm \theset{0}$ ($n > 2$) is simply connected.
::: {.proof}
$\RR^n \sm \theset{0}$ deformation-retracts onto $S^{n-1}$, and $\pi_1(S^{n-1}) = 0$ for $n - 1 \ge 2$.
:::
<2>3. Hence $\RR^2 \not\cong \RR^n$.
::: {.proof}
$\pi_1$ is a homeomorphism invariant, and the two spaces have different $\pi_1$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2 prove (a) and (b).
:::
:::
