---
schema: qual/card@1
id: P-BKS12-5B
kind: problem
title: Increasing functions have a point of continuity
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in f against s12solutions.pdf page 5 problem 5B, keeping the source calligraphic R.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the one-sided monotone limits, construction of disjoint jump intervals, and injection of the discontinuity set into the rationals.
---

::: {.problem}
Let $f : \RR \to \RR$ be an increasing function from the reals to the reals. Show that there is an $x$ such that $f$ is continuous at $x$.
:::

::: {.solution}
Let
$$
D\coloneqq\{x\in\RR:f\text{ is discontinuous at }x\}.
$$

::: pf

::: {.pf-step #one-sided-bounds}
For every $x\in\RR$, the finite numbers
$$
L_x
\coloneqq
\sup_{t<x}f(t)
$$
and
$$
R_x
\coloneqq
\inf_{t>x}f(t)
$$
satisfy
$$
L_x\leq f(x)\leq R_x.
$$

::: pf-proof
Because $f$ is increasing,
$$
f(t)\leq f(x)
$$
for $t<x$, so the nonempty set whose supremum defines $L_x$ is bounded
above. Thus $L_x$ is a finite real number.

Similarly,
$$
f(t)\geq f(x)
$$
for $t>x$, so the nonempty set whose infimum defines $R_x$ is bounded
below. Thus $R_x$ is finite. The displayed inequalities follow directly
from monotonicity.
:::

:::

::: {.pf-step #one-sided-limits}
One has
$$
\lim_{t\to x^-}f(t)=L_x
$$
and
$$
\lim_{t\to x^+}f(t)=R_x.
$$

::: pf-proof
Let $\varepsilon>0$. By the definition of supremum, there is some
$s<x$ with
$$
L_x-\varepsilon<f(s)\leq L_x.
$$
For every $t$ with $s<t<x$, monotonicity gives
$$
L_x-\varepsilon
<
f(s)
\leq
f(t)
\leq
L_x.
$$
Hence the left-hand limit is $L_x$.

The proof on the right is analogous: by the definition of infimum, choose
$u>x$ with
$$
R_x\leq f(u)<R_x+\varepsilon.
$$
Then for $x<t<u$,
$$
R_x
\leq
f(t)
\leq
f(u)
<
R_x+\varepsilon.
$$
:::

:::

::: {.pf-step #continuity-criterion}
The function $f$ is continuous at $x$ exactly when
$$
L_x=f(x)=R_x.
$$

::: pf-proof
If $f$ is continuous at $x$, both one-sided limits equal $f(x)$, so the
claim follows from step [](#one-sided-limits){.pf-ref}.

Conversely, if the three quantities are equal, step [](#one-sided-limits){.pf-ref} shows that both
one-sided limits equal $f(x)$, hence the two-sided limit exists and equals
$f(x)$.
:::

:::

::: {.pf-step #jump-interval-exists}
For every $x\in D$, there is a nonempty open interval
$$
J_x\subseteq(L_x,R_x).
$$

::: pf-proof
By step [](#continuity-criterion){.pf-ref}, if $x\in D$, then either
$$
L_x<f(x)
$$
or
$$
f(x)<R_x.
$$
In the first case set
$$
J_x=(L_x,f(x)),
$$
and in the second case set
$$
J_x=(f(x),R_x).
$$
If both inequalities hold, choose either interval. In every case $J_x$ is
a nonempty open interval.
:::

:::

::: {.pf-step #intervals-disjoint}
If
$$
x<y
$$
are in $D$, then
$$
J_x\cap J_y=\varnothing.
$$

::: pf-proof
Choose any $t$ with
$$
x<t<y.
$$
Monotonicity gives
$$
R_x
\leq
f(t)
\leq
L_y.
$$
Every point of $J_x$ is strictly less than $R_x$, while every point of
$J_y$ is strictly greater than $L_y$. Therefore every point of $J_x$ is
strictly less than every point of $J_y$.
:::

:::

::: {.pf-step #d-countable}
The set $D$ is countable.

::: pf-proof
Every nonempty open interval contains a rational number. For each
$x\in D$, choose
$$
q_x\in J_x\cap\QQ.
$$
Step [](#intervals-disjoint){.pf-ref} shows that the intervals $J_x$ are pairwise disjoint, so
distinct points of $D$ receive distinct rationals. Thus
$$
x\longmapsto q_x
$$
is an injection from $D$ into the countable set $\QQ$.
:::

:::

::: {.pf-step #continuity-point-exists}
There exists
$$
\boxed{x\in\RR}
$$
at which $f$ is continuous.

::: pf-proof
The real line is uncountable, while the discontinuity set $D$ is countable
by step [](#d-countable){.pf-ref}. Hence
$$
\RR\setminus D
\neq
\varnothing.
$$
Every point in this complement is a continuity point.
:::

:::

::: pf-qed
Step [](#continuity-point-exists){.pf-ref} is the required existence statement.
:::

:::

:::
