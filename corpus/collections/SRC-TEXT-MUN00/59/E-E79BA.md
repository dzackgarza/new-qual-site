---
schema: qual/card@1
id: E-E79BA
kind: problem
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

(a) Show that $\RR^1$ and $\RR^n$ are not homeomorphic if $n > 1$.

(b) Show that $\RR^2$ and $\RR^n$ are not homeomorphic if $n > 2$.

It is, in fact, true that $\RR^m$ and $\RR^n$ are not homeomorphic if $n \neq m$, but the proof requires more advanced tools of algebraic topology.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}

(a) $\RR^1 \not\cong \RR^n$ for $n > 1$.

::: pf-proof

::: pf-step

Removing a point from $\RR^1$ gives a disconnected space.

::: pf-proof

$\RR^1 \sm \theset{0} = (-\infty, 0) \cup (0, \infty)$ is disconnected.

:::

:::

::: pf-step

Removing a point from $\RR^n$ ($n > 1$) gives a connected space.

::: pf-proof

$\RR^n \sm \theset{0}$ is path-connected (any two points can be joined by a path avoiding the origin).

:::

:::

::: pf-step

Hence $\RR^1 \not\cong \RR^n$.

::: pf-proof

A homeomorphism $h: \RR^1 \to \RR^n$ would restrict to a homeomorphism $\RR^1 \sm \theset{0} \to \RR^n \sm \theset{h(0)}$, and connectedness is a homeomorphism invariant.

:::

:::

:::

:::

::: {.pf-step #s2}

(b) $\RR^2 \not\cong \RR^n$ for $n > 2$.

::: pf-proof

::: pf-step

$\RR^2 \sm \theset{0}$ is not simply connected.

::: pf-proof

$\RR^2 \sm \theset{0}$ deformation-retracts onto $S^1$, so $\pi_1(\RR^2 \sm \theset{0}) = \ZZ \neq 0$.

:::

:::

::: pf-step

$\RR^n \sm \theset{0}$ ($n > 2$) is simply connected.

::: pf-proof

$\RR^n \sm \theset{0}$ deformation-retracts onto $S^{n-1}$, and $\pi_1(S^{n-1}) = 0$ for $n - 1 \ge 2$.

:::

:::

::: pf-step

Hence $\RR^2 \not\cong \RR^n$.

::: pf-proof

A homeomorphism $h: \RR^2 \to \RR^n$ would restrict to a homeomorphism $\RR^2 \sm \theset{0} \to \RR^n \sm \theset{h(0)}$, and $\RR^n \sm \theset{h(0)} \cong \RR^n \sm \theset{0}$ by a translation; but the two spaces have different fundamental groups.

:::

:::

:::

:::

:::

:::
