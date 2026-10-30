---
schema: qual/card@1
id: P-BKS19-1B
kind: problem
title: Evaluation of $\int_0^{\pi/2}\sin x\cos x/(\sin^4x+\cos^4x)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 tangent-substitution calculation. The substitutions and value $\pi/4$ are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the reduction by dividing through by $\cos^4x$, both changes of variables, and the final arctangent evaluation.
---

::: {.problem}
Evaluate
$$
I=\int_0^{\pi/2}\frac{\sin x\cos x}{\sin^4x+\cos^4x}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

With the substitution $t=\tan x$,
$$
I=\int_0^\infty\frac{t}{1+t^4}\,dt.
$$


::: pf-proof

For $0\leq x<\pi/2$, divide numerator and denominator by $\cos^4x$:
$$
\frac{\sin x\cos x}{\sin^4x+\cos^4x}
=
\frac{\tan x\,\sec^2x}{1+\tan^4x}.
$$
Since $dt=\sec^2x\,dx$, while $\tan0=0$ and $\tan x\to\infty$ as $x\to(\pi/2)^-$, the improper-integral substitution gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

With $y=t^2$,
$$
I=\frac12\int_0^\infty\frac{dy}{1+y^2}.
$$


::: pf-proof

Since $dy=2t\,dt$, step [](#s1-1){.pf-ref} becomes
$$
\int_0^\infty\frac{t}{1+t^4}\,dt
=
\frac12\int_0^\infty\frac{dy}{1+y^2}.
$$

:::

:::

::: {.pf-step #s1-3}

The value of the integral is
$$
\boxed{I=\frac{\pi}{4}}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
I
=
\frac12\left[\arctan y\right]_{0}^{\infty}
=
\frac12\cdot\frac{\pi}{2}
=
\frac{\pi}{4}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
