---
schema: qual/card@1
id: P-BKF79-9
kind: problem
title: Differentiate the Gaussian integral with respect to its scale parameter
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Scaled the Gaussian integral by u=sqrt(t)x to obtain
    f(t)=sqrt(pi)t^{-1/2} for t>0, then differentiated this explicit
    formula.
---

::: {.problem}
Given
\[
\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi,
\]
define for $t>0$
\[
f(t)=\int_{-\infty}^{\infty}e^{-t x^2}\,dx.
\]
Find $f'(t)$ explicitly.
:::

::: {.solution}
<1>1. For every $t>0$,
$$
f(t)=\frac{\sqrt\pi}{\sqrt t}.
$$

::: {.proof}
Set
$$
u=\sqrt t\,x.
$$
Since $t>0$, this substitution gives
$$
x=\frac{u}{\sqrt t},
\qquad
dx=\frac{du}{\sqrt t},
$$
and therefore
$$
\begin{aligned}
f(t)
&=
\int_{-\infty}^{\infty}e^{-t x^2}\,dx\\
&=
\frac{1}{\sqrt t}
\int_{-\infty}^{\infty}e^{-u^2}\,du\\
&=
\frac{\sqrt\pi}{\sqrt t},
\end{aligned}
$$
using the given Gaussian integral.
:::

<1>2. For every $t>0$,
$$
f'(t)
=
\boxed{-\frac{\sqrt\pi}{2t^{3/2}}}.
$$

::: {.proof}
By step <1>1,
$$
f(t)=\sqrt\pi\,t^{-1/2}.
$$
Differentiating this explicit formula gives
$$
f'(t)
=
-\frac12\sqrt\pi\,t^{-3/2}
=
-\frac{\sqrt\pi}{2t^{3/2}}.
$$
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the requested derivative.
:::
:::
