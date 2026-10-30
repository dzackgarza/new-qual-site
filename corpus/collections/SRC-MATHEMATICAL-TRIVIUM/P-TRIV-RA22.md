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
Find $\int_0^{\pi^2} \cos\sqrt{x}\, dx$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Therefore
$$
\int_0^{\pi^2}\cos\sqrt x\,dx
=
2\int_0^\pi u\cos u\,du.
$$


::: pf-proof

Substitute the relations from steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\int_0^{\pi^2}\cos\sqrt x\,dx=-4.
}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required value.

:::

:::

:::
