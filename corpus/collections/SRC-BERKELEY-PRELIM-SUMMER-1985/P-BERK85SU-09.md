---
schema: qual/card@1
id: P-BERK85SU-09
kind: problem
title: Maximum principle and uniqueness for $u''=e^x u$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    At a positive interior local maximum the second derivative is nonpositive,
    while the equation gives u''=e^x u>0; the negative-minimum case is
    analogous. With zero endpoint values, any nonzero solution would attain
    either a positive interior maximum or a negative interior minimum.
---

::: {.problem}
Let $u:[0,1]\to\mathbb R$ be a $C^2$ function satisfying
\[
u''(x)=e^x u(x).
\]

1. Show that if $0<x_0<1$, then $u$ cannot have a positive local maximum at $x_0$, and cannot have a negative local minimum there.
2. If $u(0)=u(1)=0$, prove that $u(x)\equiv0$ on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part 1: $u$ cannot have a positive local maximum at an interior
point.

::: pf-proof

Suppose $0<x_0<1$ and $u$ has a positive local maximum at $x_0$.
Since $u$ is $C^2$, the second-derivative test gives
$$
u''(x_0)\le0.
$$
On the other hand, the differential equation gives
$$
u''(x_0)
=
e^{x_0}u(x_0)
>
0,
$$
because $e^{x_0}>0$ and $u(x_0)>0$. This is a contradiction.

:::

:::

::: {.pf-step #s2}

Part 1: $u$ cannot have a negative local minimum at an interior
point.

::: pf-proof

Suppose $0<x_0<1$ and $u$ has a negative local minimum at $x_0$.
The second-derivative test gives
$$
u''(x_0)\ge0.
$$
But
$$
u''(x_0)
=
e^{x_0}u(x_0)
<
0,
$$
since $u(x_0)<0$. This is again a contradiction.

:::

:::

::: {.pf-step #s3}

Under the additional hypothesis $u(0)=u(1)=0$, the function
$u$ cannot take a positive value.

::: pf-proof

If $u(x)>0$ for some $x\in(0,1)$, continuity on the compact interval
$[0,1]$ gives a point $x_0$ where $u$ attains its maximum. That
maximum is positive. Since the endpoint values are both $0$, the
maximizer satisfies $0<x_0<1$. It is therefore a positive local
maximum, contradicting step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Under the same boundary conditions, the function $u$ cannot
take a negative value.

::: pf-proof

If $u(x)<0$ for some $x\in(0,1)$, continuity gives a point $x_0$
where $u$ attains its minimum on $[0,1]$. That minimum is negative,
so the zero endpoint values force $0<x_0<1$. This is a negative local
minimum, contradicting step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Part 2 gives
$$
\boxed{u(x)\equiv0\text{ on }[0,1]}.
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $u$ takes neither positive nor negative
values. Hence $u(x)=0$ for every $x\in[0,1]$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part 1, and step [](#s5){.pf-ref} proves part 2.

:::

:::

:::
