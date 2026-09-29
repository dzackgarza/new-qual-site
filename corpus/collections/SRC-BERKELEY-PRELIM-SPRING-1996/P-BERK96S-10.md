---
schema: qual/card@1
id: P-BERK96S-10
kind: problem
title: $e^x>x^t$ for every $x>0$ exactly when $0<t<e$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the minimum of x/log x at e, the x<=1 case, and the sharp
    failure at x=e for every t>=e.
---

::: {.problem}
Show that a positive constant $t$ satisfies
\[
e^x>x^t
\qquad\text{for every }x>0
\]
if and only if
\[
t<e.
\]
:::

::: {.solution}
For $x>1$, define
$$
h(x)\coloneqq\frac{x}{\log x}.
$$

::: pf

::: {.pf-step #s1}

The function $h$ has minimum value $e$ on $(1,\infty)$, attained at
$x=e$.

::: pf-proof

Differentiation gives
$$
h'(x)
=
\frac{\log x-1}{(\log x)^2}.
$$
Thus $h'(x)<0$ for $1<x<e$, $h'(e)=0$, and $h'(x)>0$ for $x>e$.
Therefore $h$ decreases on $(1,e]$ and increases on $[e,\infty)$, so
$$
h(x)\geq h(e)=e
$$
for every $x>1$.

:::

:::

::: {.pf-step #s2}

If $0<t<e$, then
$$
e^x>x^t
$$
for every $x>0$.

::: pf-proof

If $0<x\leq1$, then
$$
x^t\leq1<e^x.
$$
If $x>1$, then step [](#s1){.pf-ref} gives
$$
t<e\leq\frac{x}{\log x}.
$$
Since $\log x>0$, this implies
$$
t\log x<x.
$$
Exponentiating gives
$$
x^t<e^x.
$$

:::

:::

::: {.pf-step #s3}

If $t\geq e$, then the inequality fails for $x=e$.

::: pf-proof

At $x=e$,
$$
x^t=e^t\geq e^e=e^x.
$$
Thus the required strict inequality does not hold for every positive $x$.

:::

:::

::: {.pf-step #s4}

A positive constant $t$ satisfies the required inequality for every
$x>0$ if and only if
$$
\boxed{t<e}.
$$

::: pf-proof

Step [](#s2){.pf-ref} proves sufficiency, and step [](#s3){.pf-ref} proves necessity.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is exactly the desired equivalence.

:::

:::

:::
