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

::: {.solution}
<1>1. The function \(|\sin x|\) is \(\pi\)-periodic.

::: {.proof}
For every \(x\in\mathbb R\),
\[
|\sin(x+\pi)|
=
|-\sin x|
=
|\sin x|.
\]
:::

<1>2. One period has integral
\[
\int_0^\pi|\sin x|\,dx=2.
\]

::: {.proof}
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

<1>3. The interval \([0,10\pi]\) consists of ten consecutive periods of \(|\sin x|\).

::: {.proof}
By step <1>1, for each integer \(k=0,\ldots,9\),
\[
\int_{k\pi}^{(k+1)\pi}|\sin x|\,dx
=
\int_0^\pi|\sin x|\,dx
=2
\]
by step <1>2.
:::

<1>4. Therefore
\[
\boxed{\displaystyle \int_0^{10\pi}|\sin x|\,dx=20.}
\]

::: {.proof}
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

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
