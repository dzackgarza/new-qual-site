---
schema: qual/card@1
id: P-BKF13-3A
kind: problem
title: Convergence of the iteration $x_{n+1}=1/(1+x_n)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 3A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the invariant interval, the unique positive fixed point, and the
    contraction estimate giving convergence from every positive initial value.
---

::: {.problem}
Define a set of positive real numbers as follows.
Let $x _ { 0 } > 0$ be any positive number, and let $x _ { n + 1 } = ( 1 + x _ { n } ) ^ { - 1 }$ for all $n \geq 0$ . Prove that this sequence converges, and find its limit.
:::

::: {.solution}
Let
$$
f(x)\coloneqq\frac1{1+x},
$$
so that $x_{n+1}=f(x_n)$.

::: pf

::: {.pf-step #s1}

For every positive initial value $x_0$,
$$
\frac12<x_n<\frac23
\qquad
(n\ge3).
$$

::: pf-proof

Since $x_0>0$,
$$
0<x_1<1.
$$
Therefore
$$
\frac12<x_2<1,
$$
and hence
$$
\frac12<x_3<\frac23.
$$
If $1/2<x<2/3$, then
$$
\frac35<f(x)<\frac23,
$$
so in particular $1/2<f(x)<2/3$. Induction now gives the displayed
bound for every $n\ge3$.

:::

:::

::: {.pf-step #s2}

The map $f$ has a unique positive fixed point
$$
\alpha\coloneqq\frac{\sqrt5-1}{2},
$$
and $\alpha\in(1/2,2/3)$.

::: pf-proof

The fixed-point equation is
$$
x=\frac1{1+x},
$$
equivalently
$$
x^2+x-1=0.
$$
Its unique positive root is
$$
\alpha=\frac{\sqrt5-1}{2}.
$$
If the iteration starts at $x_0=\alpha$, then every term equals
$\alpha$. Applying step [](#s1){.pf-ref} to this particular initial value gives
$1/2<\alpha<2/3$.

:::

:::

::: {.pf-step #s3}

On $(1/2,2/3)$ one has
$$
\lvert f'(x)\rvert<\frac49.
$$

::: pf-proof

Since
$$
f'(x)=-\frac1{(1+x)^2},
$$
the inequality $x>1/2$ gives
$$
\lvert f'(x)\rvert
=\frac1{(1+x)^2}
<\frac1{(3/2)^2}
=\frac49.
$$

:::

:::

::: {.pf-step #s4}

For every $n\ge3$,
$$
\lvert x_{n+1}-\alpha\rvert
\le
\frac49\lvert x_n-\alpha\rvert.
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, both $x_n$ and $\alpha$ lie in
$(1/2,2/3)$. The mean value theorem and step [](#s3){.pf-ref} give
$$
\lvert f(x_n)-f(\alpha)\rvert
\le
\frac49\lvert x_n-\alpha\rvert.
$$
Since $f(x_n)=x_{n+1}$ and $f(\alpha)=\alpha$, this is the desired
estimate.

:::

:::

::: {.pf-step #s5}

The sequence converges to
$$
\boxed{\frac{\sqrt5-1}{2}}.
$$

::: pf-proof

Iterating step [](#s4){.pf-ref} gives, for $n\ge3$,
$$
\lvert x_n-\alpha\rvert
\le
\left(\frac49\right)^{n-3}
\lvert x_3-\alpha\rvert.
$$
The right-hand side tends to $0$, so $x_n\to\alpha$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves convergence and identifies the limit.

:::

:::

:::
