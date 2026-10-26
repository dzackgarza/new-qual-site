---
schema: qual/card@1
id: P-UGASAMP-05
kind: problem
title: $\int_0^{10\pi}|\sin x|\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Evaluate
\[
\int_0^{10\pi}|\sin x|\,dx.
\]
:::

::: pf

::: pf-step

The function \(|\sin x|\) is \(\pi\)-periodic.


::: pf-proof

For every \(x\in\mathbb R\),
\[
|\sin(x+\pi)|
=
|-\sin x|
=
|\sin x|.
\]

:::

:::

::: pf-step

One period has integral
\[
\int_0^\pi|\sin x|\,dx=2.
\]


::: pf-proof

On \([0,\pi]\), one has \(\sin x\ge0\), so
\[
\int_0^\pi|\sin x|\,dx
=
\int_0^\pi\sin x\,dx
=
[-\cos x]_0^\pi
=
2.
\]

:::

:::

::: pf-step

The interval \([0,10\pi]\) consists of ten consecutive periods of \(|\sin x|\).


::: pf-proof

By step <1>1, for each integer \(k=0,\ldots,9\),
\[
\int_{k\pi}^{(k+1)\pi}|\sin x|\,dx
=
\int_0^\pi|\sin x|\,dx
=2
\]
by step <1>2.

:::

:::

::: pf-step

Therefore
\[
\boxed{\displaystyle \int_0^{10\pi}|\sin x|\,dx=20.}
\]


::: pf-proof

Add the ten integrals from step <1>3:
\[
\int_0^{10\pi}|\sin x|\,dx
=
\sum_{k=0}^{9}\int_{k\pi}^{(k+1)\pi}|\sin x|\,dx
=
\sum_{k=0}^{9}2
=20.
\]

:::

:::

::: pf-qed

Step <1>4 gives the requested value.

:::

:::
