---
schema: qual/card@1
id: P-EQGG7
kind: problem
title: $z\tan z-a$ has only real roots for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Trigonometry
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Not source-checked: this collection's `provenance` is empty and no retained text of the
    related textbook (Stein--Shakarchi) is in `tmp/sources`. The statement was checked
    mathematically only, and its truth for $a>0$ is what the proof below establishes.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this problem. Structured the card's own argument:
    the tangent addition formula for $x+iy$, the denominator's positivity for $y\ne0$,
    vanishing of the imaginary part of $z\tan z$, and the substitution that makes the
    real part strictly negative. Checked the algebra
    $x\sin2x-y\sinh2y=-(x^2+y^2)\sinh2y/y$ under $\sin2x=-(x/y)\sinh2y$.
---

::: {.problem}
Prove that for $a> 0$, $z\tan z - a$ has only real roots.
:::

::: {.solution}

No retained solution set covers this problem; the argument below is the card's own.

::: pf

::: {.pf-step #tangent-formula}
For $z=x+iy$,
$$
\tan(x+iy)=\frac{\sin2x+i\sinh2y}{\cos2x+\cosh2y},
$$
so
$$
z\tan z=\frac{x\sin2x-y\sinh2y+i\bigl(x\sinh2y+y\sin2x\bigr)}{\cos2x+\cosh2y}.
$$

::: pf-proof
This is the standard addition formula for tangent in terms of real and imaginary parts. Multiplying $x+iy$ by the numerator and dividing by the real number $\cos2x+\cosh2y$ gives the displayed real and imaginary parts.
:::
:::

::: {.pf-step #denominator}
If $y\ne0$, then $\cos2x+\cosh2y>0$.

::: pf-proof
Since $\cosh2y\ge1$ and $\cos2x\ge-1$, the sum is nonnegative; equality would force $\cosh2y=1$, which happens only at $y=0$.
:::
:::

::: {.pf-step #imaginary-part}
If $z=x+iy$ is a zero of $z\tan z-a$ with $y\ne0$, then
$$
x\sinh2y+y\sin2x=0,
\qquad\text{so}\qquad
\sin2x=-\frac{x}{y}\sinh2y.
$$

::: pf-proof
The equation $z\tan z=a$ with $a$ real makes $z\tan z$ real. Its imaginary part, displayed in step [](#tangent-formula){.pf-ref}, vanishes because the denominator is real and nonzero by step [](#denominator){.pf-ref}. Solving for $\sin2x$ gives the second identity, using $y\ne0$.
:::
:::

::: {.pf-step #negative-real-part}
Under the identity of step [](#imaginary-part){.pf-ref},
$$
\operatorname{Re}(z\tan z)
=-\frac{(x^2+y^2)\sinh2y}{y\,(\cos2x+\cosh2y)}<0.
$$

::: pf-proof
Substituting $\sin2x=-(x/y)\sinh2y$ into the real part gives
$$
x\sin2x-y\sinh2y=-\frac{x^2}{y}\sinh2y-y\sinh2y
=-\frac{(x^2+y^2)\sinh2y}{y}.
$$
For $y\ne0$ the factor $\sinh2y/y$ is positive and the denominator is positive by step [](#denominator){.pf-ref}; since $x^2+y^2>0$, the quotient is negative.
:::
:::

::: {.pf-step #conclusion}
Every zero of $z\tan z-a$ with $a>0$ is real.

::: pf-proof
If $y\ne0$, step [](#negative-real-part){.pf-ref} contradicts $z\tan z=a>0$. Hence $y=0$ for every zero.
:::
:::

:::
:::
