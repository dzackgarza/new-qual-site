---
schema: qual/card@1
id: P-WKGRZ
kind: problem
title: A $p$-group acting on a set of cardinality not divisible by $p$ has a fixed
  point
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's orbit argument into numbered steps; orbit-stabilizer, the congruence and
    the conclusion are unchanged. Checked: that the orbit size divides the order of the p-group,
    the identification of singleton orbits with fixed points, and the congruence. Not checked
    against a printed source: no solution set is retained for this source in tmp/sources and the
    card records no page.
---

::: {.problem}
Let a finite $p$-group $G$ act on a finite set $X$ with $p\nmid \cardinality{X}$. Prove that the action has a fixed point.
:::

::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $G$ is a finite $p$-group acting on a finite set $X$ with $p\nmid\cardinality{X}$, and $X^{G}$ is the set of points fixed by every element of $G$.

::: pf

::: {.pf-step #orbitsize}

Every orbit has cardinality a power of $p$.

::: pf-proof

By orbit--stabilizer the orbit of $x$ has cardinality $\subgroupindex{G:G_{x}}=\cardinality{G}/\cardinality{G_x}$; a quotient of a $p$-group is a $p$-group, so this is $p^{k}$ for some $k\geq0$.

:::

:::

::: {.pf-step #fixed}

An orbit has cardinality $1$ exactly when it consists of a fixed point.

::: pf-proof

An orbit of size $1$ is $\theset{x}$ with $gx=x$ for every $g\in G$, that is $x\in X^{G}$; conversely a fixed point has the singleton orbit.

:::

:::

::: {.pf-step #divisible}

Every orbit of size greater than $1$ has cardinality divisible by $p$.

::: pf-proof

By step [](#orbitsize){.pf-ref} the size is $p^{k}$, and it exceeds $1$ only when $k\geq1$.

:::

:::

::: {.pf-step #cong}

$\cardinality{X}\equiv\cardinality{X^{G}}\pmod p$.

::: pf-proof

The orbits partition $X$, so $\cardinality{X}$ is the sum of the orbit sizes; the size-$1$ orbits contribute $\cardinality{X^{G}}$ and all others are divisible by $p$ by step [](#divisible){.pf-ref}.

:::

:::

::: {.pf-step #done}

$X^{G}\neq\varnothing$.

::: pf-proof

If $X^{G}$ were empty, step [](#cong){.pf-ref} would give $p\mid\cardinality{X}$, contrary to hypothesis; so some point is fixed.

:::

:::

:::

:::
