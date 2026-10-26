---
schema: qual/card@1
id: P-TRIV-RA22
kind: problem
title: $\int_0^{\pi^2}\cos\sqrt x\,dx$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\int _ { 0 } ^ { \pi ^ { 2 } } \cos { \sqrt { x } } d x .$
:::

::: pf

::: pf-step

Set
$$
u=\sqrt x.
$$
Then
$$
x=u^2,
\qquad
dx=2u\,du.
$$


::: pf-proof

Differentiate $x=u^2$.

:::

:::

::: pf-step

The limits transform as
$$
x=0\longmapsto u=0,
\qquad
x=\pi^2\longmapsto u=\pi.
$$


::: pf-proof

Take the nonnegative square root at both endpoints.

:::

:::

::: pf-step

Therefore
$$
\int_0^{\pi^2}\cos\sqrt x\,dx
=
2\int_0^\pi u\cos u\,du.
$$


::: pf-proof

Substitute the relations from steps <1>1--<1>2.

:::

:::

::: pf-step

Integration by parts gives
$$
\int_0^\pi u\cos u\,du
=
-2.
$$


::: pf-proof

Take
$$
a=u,
\qquad
db=\cos u\,du,
$$
so
$$
da=du,
\qquad
b=\sin u.
$$
Then
$$
\begin{aligned}
\int_0^\pi u\cos u\,du
&=
\left[u\sin u\right]_0^\pi
-
\int_0^\pi\sin u\,du\\
&=
0-2\\
&=
-2.
\end{aligned}
$$

:::

:::

::: pf-step

Hence
$$
\boxed{
\int_0^{\pi^2}\cos\sqrt x\,dx=-4.
}
$$


::: pf-proof

Combine steps <1>3 and <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required value.

:::

:::
