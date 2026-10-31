---
schema: qual/card@1
id: P-US4ES
kind: problem
title: Continuity equivalent to lower and upper semicontinuity, and sequential characterization
  of lower semicontinuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $(X,d)$ be a metric space.
A function $f \colon X \to \RR$ is said to be lower semi-continuous (l.s.c) if $f^{-1}(a,\infty)  = \{x \in X \, \colon \,  f(x)> a\}$ is open in $X$ for every $a \in \RR$.
Analogously, $f$ is upper semi-continuous (u.s.c) if $f^{-1}(-\infty, b) = \{x \in X \, \colon \,  f(x)<b\}$ is open in $X$ for every $b \in \RR$.

(a) Prove that a function $f \colon X \to \RR$ is continuous if and only if $f$ is both l.s.c. and u.s.c.

(b) Prove that $f$ is lower semi-continuous if and only if $\liminf_{n \to \infty} f(x_n) \geq f(x)$ whenever $\{x_n\}_{n=1}^\infty \subseteq X$ such that $x_n \to x$ in $X$.
:::

::: {.solution}

::: pf

::: pf-step

$f$ is continuous if and only if it is both lower and upper semicontinuous.

::: pf-proof

::: pf-step

If $f$ is continuous, then it is both lower and upper semicontinuous.

::: pf-proof

For every $a,b\in\RR$, the intervals $(a,\infty)$ and $(-\infty,b)$ are open in $\RR$.
Continuity makes their inverse images under $f$ open in $X$, as required.

:::

:::

::: pf-step

If $f$ is both lower and upper semicontinuous, then it is continuous.

::: pf-proof

For every $a<b$, one has
$$
f^{-1}((a,b))=f^{-1}((a,\infty))\cap f^{-1}((-\infty,b)).
$$
Both factors are open by the respective semicontinuity hypotheses, so their intersection is open.
Every open subset of $\RR$ is a union of open intervals, and inverse images preserve unions.
Therefore inverse images of all open subsets of $\RR$ are open in $X$.

:::

:::

:::

:::

::: pf-step

$f$ is lower semicontinuous if and only if $\liminf_{n\to\infty}f(x_n)\ge f(x)$ whenever $x_n\to x$ in $X$.

::: pf-proof

::: pf-step

If $f$ is lower semicontinuous and $x_n\to x$, then $\liminf_{n\to\infty}f(x_n)\ge f(x)$.

::: pf-proof

Fix $a<f(x)$. The set $U=f^{-1}((a,\infty))$ is open and contains $x$. Convergence $x_n\to x$ implies $x_n\in U$ eventually, hence $f(x_n)>a$ eventually.
Consequently $\liminf_n f(x_n)\ge a$.
Since this holds for every $a<f(x)$, the desired inequality follows.

:::

:::

::: pf-step

If the sequential liminf inequality holds for every convergent sequence, then $f$ is lower semicontinuous.

::: pf-proof

Suppose otherwise.
There is $a\in\RR$ such that $U=f^{-1}((a,\infty))$ is not open, and a point $x\in U$ that is not an interior point of $U$.
For every integer $n\ge1$, the ball $B(x,1/n)$ meets $X\setminus U$; pick $x_n$ in that intersection.
Then $x_n\to x$, while $f(x_n)\le a$ for all $n$.
Thus
$$
\liminf_{n\to\infty}f(x_n)\le a<f(x),
$$
contradicting the assumed sequential inequality.

:::

:::

:::

:::

:::

:::
