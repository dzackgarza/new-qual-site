---
schema: qual/card@1
id: P-BERK95S-14
kind: problem
title: A linear relation among initial data for decaying solutions of $y'''-y=0$
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
  note: The retained PDF confirms the coefficient b in a y(0)+b y'(0)+c y''(0)=d; the extraction dropped it.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $y:\mathbb R\to\mathbb R$ be three times differentiable and satisfy
\[
y'''-y=0.
\]
Suppose
\[
\lim_{x\to\infty}y(x)=0.
\]
Find real numbers $a,b,c,d$, not all zero, such that
\[
ay(0)+by'(0)+cy''(0)=d.
\]
:::

::: {.solution}
Put
$$
\omega\coloneqq\frac{\sqrt3}{2}.
$$

<1>1. Every real solution of $y'''-y=0$ has the form
$$
y(x)
=
A e^x
+e^{-x/2}\bigl(B\cos(\omega x)+C\sin(\omega x)\bigr)
$$
for real constants $A,B,C$.

::: {.proof}
The characteristic polynomial is
$$
r^3-1
=(r-1)(r^2+r+1),
$$
whose roots are
$$
1,
\qquad
-\frac12\pm i\frac{\sqrt3}{2}.
$$
The standard real solution basis for a constant-coefficient linear
ODE therefore gives the displayed form.
:::

<1>2. The hypothesis $\lim_{x\to\infty}y(x)=0$ forces $A=0$.

::: {.proof}
The oscillatory term in step <1>1 is bounded in absolute value by
$$
e^{-x/2}(\abs B+\abs C),
$$
which tends to zero. If $A\ne0$, then $Ae^x$ is unbounded in absolute
value as $x\to\infty$, so the sum cannot tend to zero. Hence $A=0$.
:::

<1>3. For a decaying solution,
$$
y(0)+y'(0)+y''(0)=0.
$$

::: {.proof}
By step <1>2,
$$
y(x)
=
e^{-x/2}\bigl(B\cos(\omega x)+C\sin(\omega x)\bigr).
$$
At $x=0$,
$$
y(0)=B,
$$
and differentiation gives
$$
y'(0)
=-\frac B2+\frac{\sqrt3}{2}C,
\qquad
y''(0)
=-\frac B2-\frac{\sqrt3}{2}C.
$$
Adding the three displayed values gives zero.
:::

<1>4. One valid choice is
$$
\boxed{a=b=c=1,\qquad d=0}.
$$

::: {.proof}
These four real numbers are not all zero, and step <1>3 gives
$$
ay(0)+by'(0)+cy''(0)
=y(0)+y'(0)+y''(0)
=0
=d.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 supplies the required constants.
:::
:::
