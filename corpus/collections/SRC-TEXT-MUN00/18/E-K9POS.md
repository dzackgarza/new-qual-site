---
schema: qual/card@1
id: E-K9POS
kind: problem
title: Continuous images of limit points
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Limit Points
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Suppose that $f: X \to Y$ is continuous.
If $x$ is a limit point of the subset $A$ of $X$, is it necessarily true that $f(x)$ is a limit point of $f(A)$?
:::

::: {.solution}
**Goal.** Decide whether continuity of $f: X \to Y$ and $x$ a limit point of $A$ force $f(x)$ to be a limit point of $f(A)$.

<1>1. The statement is false in general.
<2>1. Counterexample: $X = Y = \RR$, $A = \theset{1/n : n \in \NN}$, and $f$ the constant map $f \equiv 0$.
::: {.proof}
$0$ is a limit point of $A$ (the sequence $1/n \to 0$), but $f(A) = \theset{0}$ has no limit point (a singleton has no limit point).
:::
<2>2. $f$ is continuous.
::: {.proof}
a constant map is continuous.
:::

<1>2. The correct statement requires $f$ to be injective (or at least $f(x) \notin f(A)$ in a neighborhood).
<2>1. If $f$ is continuous and $x$ is a limit point of $A$, then $f(x) \in \overline{f(A)}$.
::: {.proof}
for any neighborhood $V$ of $f(x)$, $f^{-1}(V)$ is a neighborhood of $x$, so it meets $A$ in a point $a \neq x$; then $f(a) \in V \cap f(A)$, so $V$ meets $f(A)$.
:::
<2>2. $f(x)$ is a limit point of $f(A)$ iff additionally $f(x) \notin f(A)$ or $f$ is injective near $x$.
::: {.proof}
a limit point must be approached by points of $f(A)$ distinct from $f(x)$; the counterexample in <1>1 fails exactly because $f$ collapses $A$ to the single point $f(x)$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 shows the answer is "no"; <1>2 gives the corrected statement.
:::
:::
