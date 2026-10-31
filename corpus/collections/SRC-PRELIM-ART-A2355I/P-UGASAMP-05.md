---
schema: qual/card@1
id: P-UGASAMP-05
kind: problem
title: $\int_0^{10\pi}\abs{\sin x}\,dx$
classification:
  areas: [prelim]
  topics:
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Evaluate
$$
\int_0^{10\pi}\abs{\sin x}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $\abs{\sin x}$ is $\pi$-periodic.


::: pf-proof

For every $x\in\RR$,
$$
\abs{\sin(x+\pi)}
=
\abs{-\sin x}
=
\abs{\sin x}.
$$

:::

:::

::: {.pf-step #s1-2}

One period has integral
$$
\int_0^\pi\abs{\sin x}\,dx=2.
$$


::: pf-proof

On $[0,\pi]$, one has $\sin x\ge0$, so
$$
\int_0^\pi\abs{\sin x}\,dx
=
\int_0^\pi\sin x\,dx
=
[-\cos x]_0^\pi
=
2.
$$

:::

:::

::: {.pf-step #s1-3}

The interval $[0,10\pi]$ consists of ten consecutive periods of $\abs{\sin x}$.


::: pf-proof

By step [](#s1-1){.pf-ref}, for each integer $k=0,\ldots,9$,
$$
\int_{k\pi}^{(k+1)\pi}\abs{\sin x}\,dx
=
\int_0^\pi\abs{\sin x}\,dx
=2
$$
by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\displaystyle \int_0^{10\pi}\abs{\sin x}\,dx=20.}
$$


::: pf-proof

Add the ten integrals from step [](#s1-3){.pf-ref}:
$$
\int_0^{10\pi}\abs{\sin x}\,dx
=
\sum_{k=0}^{9}\int_{k\pi}^{(k+1)\pi}\abs{\sin x}\,dx
=
\sum_{k=0}^{9}2
=20.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
