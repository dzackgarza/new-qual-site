---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-11
kind: problem
title: A monotone increasing function has at most countably many jump discontinuities
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Limits
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Show that if $f:\RR\to\RR$ is monotone increasing, then $f$ has at most a countable set of jump discontinuities.
:::

::: {.solution}
For $x\in\RR$, define the one-sided limits
$$
f(x-)=\sup_{t<x}f(t),
\qquad
f(x+)=\inf_{t>x}f(t).
$$

::: pf

::: {.pf-step #s1}

These one-sided limits are finite and satisfy
$$
f(x-)\le f(x)\le f(x+).
$$

::: pf-proof

Because $f$ is increasing,
$$
f(x-1)\le f(t)\le f(x)
\qquad(x-1<t<x),
$$
so the set of values to the left of $x$ is bounded above and nonempty;
its supremum is finite. Likewise
$$
f(x)\le f(t)\le f(x+1)
\qquad(x<t<x+1),
$$
so the values to the right have a finite infimum. Monotonicity gives the
displayed inequalities.

:::

:::

::: {.pf-step #s2}

The function $f$ is continuous at $x$ if and only if
$$
f(x-)=f(x+).
$$

::: pf-proof

If $f$ is continuous at $x$, both one-sided limits equal $f(x)$.

Conversely, suppose
$$
f(x-)=f(x+)=L.
$$
Step [](#s1){.pf-ref} gives
$$
L\le f(x)\le L,
$$
so $f(x)=L$. Given $\varepsilon>0$, the definitions of supremum and
infimum give points $u<x<v$ sufficiently close to $x$ with
$$
L-\varepsilon<f(u)\le L\le f(v)<L+\varepsilon.
$$
For every $t\in(u,v)$, monotonicity yields
$$
f(u)\le f(t)\le f(v),
$$
hence $\abs{f(t)-f(x)}<\varepsilon$. Thus $f$ is continuous at $x$.

:::

:::

::: pf-step

Every discontinuity $x$ determines a nonempty open interval
$$
J_x=(f(x-),f(x+)).
$$

::: pf-proof

By step [](#s2){.pf-ref}, discontinuity means $f(x-)\ne f(x+)$. Step [](#s1){.pf-ref} orders
these quantities, so necessarily
$$
f(x-)<f(x+).
$$
Therefore $J_x$ is a nonempty open interval.

:::

:::

::: {.pf-step #s4}

If $x<y$ are discontinuities, then
$$
J_x\cap J_y=\varnothing.
$$

::: pf-proof

Let $s$ satisfy $x<s<y$. By the definitions of the one-sided limits,
$$
f(x+)\le f(s)\le f(y-).
$$
Thus $f(x+)\le f(y-)$.
Hence every point of $J_x$ is strictly less than every point of $J_y$.

:::

:::

::: {.pf-step #s5}

The set of discontinuities injects into $\QQ$.

::: pf-proof

For each discontinuity $x$, choose a rational number
$$
q_x\in J_x,
$$
which is possible because $\QQ$ is dense in $\RR$. By step [](#s4){.pf-ref},
distinct discontinuities have disjoint intervals $J_x$, so their chosen
rationals are distinct. Thus
$$
x\longmapsto q_x
$$
is injective from the discontinuity set into $\QQ$.

:::

:::

::: {.pf-step #s6}

The discontinuity set is finite or countably infinite.

::: pf-proof

By step [](#s5){.pf-ref} it is in bijection with a subset of the countable set
$\QQ$. Therefore it is at most countable.

:::

:::

::: pf-qed

Every discontinuity of a monotone function is a jump discontinuity, because both one-sided limits exist by step [](#s1){.pf-ref}. By step [](#s6){.pf-ref}, a monotone increasing $f$ therefore has at most countably many jump discontinuities.

:::

:::

:::
