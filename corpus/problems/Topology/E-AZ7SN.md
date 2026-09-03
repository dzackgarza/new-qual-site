---
schema: qual/card@1
id: E-AZ7SN
kind: problem
title: A continuous real-valued function on a compact space attains its bounds
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
Show that if $f:X\to \RR$ and $X$ is compact then $f$ is bounded and attains its min/max.
:::

::: {.solution}
**Goal:** Show that if $f: X \to \RR$ is continuous and $X$ is compact, then $f$ is bounded and attains its minimum and maximum.

<1>1. $f(X)$ is compact in $\RR$.
::: {.proof}
Continuous image of the compact space $X$.
:::

<1>2. $f(X)$ is closed and bounded.
::: {.proof}
Compact subsets of $\RR$ are closed and bounded (Heine--Borel).
:::

<1>3. $f$ is bounded.
::: {.proof}
$f(X)$ bounded (<1>2) means $f$ is bounded above and below.
:::

<1>4. $f$ attains its supremum.
<2>1. $\sup f(X)$ is finite.
::: {.proof}
$f(X)$ is bounded above (<1>2). <2>2. $\sup f(X) \in f(X)$.
:::
::: {.proof}
$f(X)$ is closed (<1>2), and the supremum of a bounded set lies in its closure; since the set is closed, the supremum belongs to it.
:::
<2>3. Some $x_{\max} \in X$ satisfies $f(x_{\max}) = \max f$.
::: {.proof}
$\sup f(X) \in f(X)$ means $\sup f(X) = f(x_{\max})$ for some $x_{\max} \in X$.
:::

<1>5. $f$ attains its infimum.
::: {.proof}
Same argument as <1>4 with $\inf$ in place of $\sup$ (or apply <1>4 to $-f$).
:::

<1>6. Q.E.D.
::: {.proof}
<1>3 gives boundedness; <1>4 and <1>5 give attainment of max and min.
:::
:::
