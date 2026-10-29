---
schema: qual/card@1
id: P-TRIV-DE35
kind: problem
title: Expansion of $\delta''(x-x_0)/(1+x-x_0)$ in derivatives of $\delta$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 35, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the coefficients a, b, c so that

$$
\delta ^ { \prime \prime } ( x - x _ { 0 } ) \frac { 1 } { ( 1 + x - x _ { 0 } ) } = a \delta ^ { \prime \prime } ( x - x _ { 0 } ) + b \delta ^ { \prime } ( x - x _ { 0 } ) + c \delta ( x - x _ { 0 } ) .
$$
:::

::: {.solution}

Set
$$
g(x)=\frac1{1+x-x_0}.
$$

::: pf

::: {.pf-step #s1-1}

For every smooth function $g$ near $x_0$,
$$
g\,\delta_{x_0}''
=g(x_0)\delta_{x_0}''-2g'(x_0)\delta_{x_0}'+g''(x_0)\delta_{x_0}.
$$


::: pf-proof

For any test function $\phi$,
$$
\langle g\delta_{x_0}'',\phi\rangle
=\langle\delta_{x_0}'',g\phi\rangle
=(g\phi)''(x_0).
$$
The product rule gives
$$
(g\phi)''(x_0)
=g(x_0)\phi''(x_0)+2g'(x_0)\phi'(x_0)+g''(x_0)\phi(x_0).
$$
Since
$$
\langle\delta_{x_0}'',\phi\rangle=\phi''(x_0),
\qquad
\langle\delta_{x_0}',\phi\rangle=-\phi'(x_0),
$$
this is exactly the action of the displayed distribution.

:::

:::

::: {.pf-step #s1-2}

For the present $g$,
$$
g(x_0)=1,
\qquad
g'(x_0)=-1,
\qquad
g''(x_0)=2.
$$


::: pf-proof

Differentiation gives
$$
g'(x)=-(1+x-x_0)^{-2},
\qquad
g''(x)=2(1+x-x_0)^{-3}.
$$
Evaluate at $x=x_0$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\frac{\delta''(x-x_0)}{1+x-x_0}
=\boxed{\delta''(x-x_0)+2\delta'(x-x_0)+2\delta(x-x_0)},
$$
so
$$
\boxed{a=1,\qquad b=2,\qquad c=2}.
$$


::: pf-proof

Substitute the three values from step [](#s1-2){.pf-ref} into the identity in step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested coefficients.

:::

:::

:::
