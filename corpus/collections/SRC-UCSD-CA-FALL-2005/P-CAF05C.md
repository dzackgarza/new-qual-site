---
schema: qual/card@1
id: P-CAF05C
kind: problem
title: "Minimum modulus principle for analytic functions on bounded domains"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and repaired a gap: the earlier prose asserted that g =
    1/f is continuous on the closure while only f zero-free on G had been assumed, which
    fails if f vanishes on the boundary. The card now splits into the case where f has a
    boundary zero, giving the minimum 0 on the boundary at once, and the case where f is
    zero-free on the closure, where 1/f is holomorphic on G and continuous on the closure.
    The extreme value theorem on the compact closure, the exclusion of an interior minimiser
    through the maximum modulus principle on the connected region, and the conclusion are
    checked. The argument is the card's own; no retained set is cited.
---

::: {.problem}
Prove that if $f$ is a non-constant analytic function on a bounded region $G \subset \CC$ and is continuous on $\overline{G}$, then either $f$ has a zero in $G$ or $\abs{f(z)}$ reaches its minimum value on $\partial G$.
:::

::: {.remark}
The Fall 2005 source says only that $G$ is a bounded open set. Connectedness is
necessary: on a disconnected open set, a zero-free holomorphic function may be
constant with smaller modulus on one component and nonconstant on another. The
statement above makes the intended region hypothesis explicit.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it.

::: pf

::: {.pf-step #setup}
$G$ is a bounded region, $f$ is analytic on $G$ and continuous on $\overline{G}$, and $f$ is non-constant on $G$. Suppose $f$ has no zero in $G$.

::: pf-proof
These are the hypotheses and the first alternative of the conclusion, assumed false so that the second may be proved.
:::

:::

::: {.pf-step #compact}
$\overline{G}$ is compact and $\abs{f}$ is continuous on it, so $\abs{f}$ attains a minimum there; and $f$ is continuous, so $f(\overline{G})$ is compact, hence bounded.

::: pf-proof
$G$ is bounded, so $\overline{G}$ is bounded and closed, hence compact in $\CC$. The function $z\mapsto\abs{f(z)}$ is continuous on $\overline{G}$ as a composite of continuous maps, so it attains a minimum at some point of $\overline{G}$ by the extreme value theorem, and $f(\overline{G})$ is compact.
:::

:::

::: {.pf-step #boundary-zero}
If $f$ vanishes at some point of $\partial G$, then $\abs{f}$ attains its minimum on $\partial G$.

::: pf-proof
$\overline{G}=G\cup\partial G$ and $f$ has no zero in $G$ by step [](#setup){.pf-ref}, so a zero of $f$ on $\overline{G}$ lies on $\partial G$; there $\abs{f}=0$, which is the least possible value of $\abs{f}$. So the minimum of $\abs{f}$ over $\overline{G}$ is $0$ and it is attained on $\partial G$.
:::

:::

::: {.pf-step #reciprocal}
If $f$ has no zero on $\overline{G}$, then $g=1/f$ is holomorphic on $G$ and continuous on $\overline{G}$.

::: pf-proof
$f$ is zero-free and holomorphic on $G$, so $g=1/f$ is holomorphic on $G$; and $f$ is continuous and nonvanishing on $\overline{G}$, so $g$ is continuous there as a quotient of continuous functions with nonvanishing denominator. This is the case the earlier prose assumed without separating it: continuity of $g$ on $\overline{G}$ needs $f$ zero-free on $\overline{G}$, not merely on $G$.
:::

:::

::: {.pf-step #no-interior-minimum}
In the case of step [](#reciprocal){.pf-ref}, no point of $G$ minimizes $\abs{f}$ over $\overline{G}$.

::: pf-proof
Suppose $a\in G$ minimizes $\abs{f}$. Since $f$ is zero-free on $\overline{G}$, $\abs{f(a)}>0$, and $\abs{g}=1/\abs{f}$ attains at $a$ its maximum over $\overline{G}$, in particular a local maximum at the interior point $a$. Then $g$ is constant on $G$ by the maximum modulus principle, applied on the connected open set $G$; hence $f=1/g$ is constant on $G$, contradicting step [](#setup){.pf-ref}.
:::

:::

::: {.pf-step}
Either $f$ has a zero in $G$ or $\abs{f}$ attains its minimum on $\partial G$.

::: pf-proof
If $f$ has no zero in $G$, then step [](#compact){.pf-ref} provides a minimizing point of $\abs{f}$ on $\overline{G}=\mathring{G}\cup\partial G$. If $f$ vanishes somewhere on $\partial G$, step [](#boundary-zero){.pf-ref} gives the second alternative. Otherwise step [](#reciprocal){.pf-ref} applies and step [](#no-interior-minimum){.pf-ref} excludes every interior minimizer, so each minimizing point, and there is one, lies on $\partial G$; again the second alternative holds.
:::

:::

:::
:::
