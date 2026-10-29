---
schema: qual/card@1
id: E-BXDQY
kind: problem
title: Entire functions with $\abs f\le\abs g$ satisfy $f=cg$
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Removable Singularities
  - Entire Functions
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ and $g$ are entire and $\abs{f(z)}\leq \abs{g(z)}$ for all $z\in\CC$.
Show that $f=cg$ for some constant $c$.
::: {.solution}
If $g\equiv0$, then the inequality forces $f\equiv0$, so $c=0$ works.
Assume $g\not\equiv0$, so the zero set $Z$ of $g$ is discrete, and let $h\coloneqq f/g$ on $\CC\setminus Z$.

::: pf

::: {.pf-step #extend}
$h$ extends to an entire function with $\abs h\le1$.

::: pf-proof
On $\CC\setminus Z$, $\abs h\le1$ by hypothesis.
Each $a\in Z$ is an isolated singularity of $h$ near which $h$ is bounded, so it is removable, and the extension still satisfies $\abs h\le1$ by continuity.
:::

:::

::: pf-step
$f=cg$ for some constant $c$.

::: pf-proof
By step [](#extend){.pf-ref} and Liouville's theorem, $h\equiv c$ for some $c\in\CC$.
Then $f=cg$ on $\CC\setminus Z$, hence on $\CC$ by continuity, since $Z$ has empty interior.
:::

:::

:::

:::
