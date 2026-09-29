---
schema: qual/card@1
id: P-BKF13-5A
kind: problem
title: Evaluation of $\int_0^{2\pi}\cos x/(2+\cos x)\,dx$
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
    Checked against Problem 5A in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the algebraic reduction and the tangent-half-angle evaluation of
    the auxiliary integral over one period.
---

::: {.problem}
Compute

$$
\int _ { 0 } ^ { 2 \pi } { \frac { \cos ( x ) } { 2 + \cos ( x ) } } d x .
$$
:::

::: {.solution}
Set
$$
I\coloneqq
\int_0^{2\pi}\frac{\cos x}{2+\cos x}\,dx.
$$

::: pf

::: {.pf-step #s1}

One has
$$
I
=2\pi
-2\int_0^{2\pi}\frac{dx}{2+\cos x}.
$$

::: pf-proof

Since
$$
\frac{\cos x}{2+\cos x}
=1-\frac2{2+\cos x},
$$
integration over $[0,2\pi]$ gives the formula.

:::

:::

::: {.pf-step #s2}

The auxiliary integral satisfies
$$
\int_0^{2\pi}\frac{dx}{2+\cos x}
=\frac{2\pi}{\sqrt3}.
$$

::: pf-proof

Because $\cos(2\pi-x)=\cos x$,
$$
\int_0^{2\pi}\frac{dx}{2+\cos x}
=2\int_0^\pi\frac{dx}{2+\cos x}.
$$
On $[0,\pi)$ set
$$
t=\tan\frac x2.
$$
Then
$$
\cos x=\frac{1-t^2}{1+t^2},
\qquad
dx=\frac{2\,dt}{1+t^2},
$$
and $t$ runs from $0$ to $+\infty$. Hence
$$
\begin{aligned}
\int_0^\pi\frac{dx}{2+\cos x}
&=
\int_0^\infty
\frac{2\,dt}{t^2+3}\\
&=
\frac2{\sqrt3}
\left[
\arctan\frac t{\sqrt3}
\right]_0^\infty\\
&=
\frac{\pi}{\sqrt3}.
\end{aligned}
$$
Doubling gives the stated value.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{
I
=2\pi-\frac{4\pi}{\sqrt3}
=2\pi\left(1-\frac2{\sqrt3}\right)
}.
$$

::: pf-proof

Substitute step [](#s2){.pf-ref} into step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested value.

:::

:::

:::
