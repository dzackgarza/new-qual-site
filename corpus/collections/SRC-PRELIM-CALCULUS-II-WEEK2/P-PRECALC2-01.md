---
schema: qual/card@1
id: P-PRECALC2-01
kind: problem
title: Arc length of the upper unit semicircle
classification:
  areas:
  - prelim
  topics:
  - Arc Length
  - Parametric Curves
relations: []
review: draft
---

::: {.problem}
What is the length of the curve $(x(t),y(t))=(\cos t,\sin t)$ for $0\le t\le\pi$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The coordinate derivatives are
$$
\boxed{x'(t)=-\sin t}
$$
and
$$
\boxed{y'(t)=\cos t}.
$$


::: pf-proof

Differentiate
$$
x(t)=\cos t,
\qquad
y(t)=\sin t.
$$

:::

:::

::: {.pf-step #s1-2}

The speed of the parametrized curve is
$$
\boxed{
\sqrt{x'(t)^2+y'(t)^2}=1}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\sqrt{x'(t)^2+y'(t)^2}
&=
\sqrt{\sin^2t+\cos^2t}\\
&=
\sqrt1\\
&=
1.
\end{aligned}
$$

:::

:::

::: pf-step

Therefore the arc length is
$$
L
=
\int_0^\pi
\sqrt{x'(t)^2+y'(t)^2}\,dt
=
\int_0^\pi1\,dt.
$$


::: pf-proof

Apply the arc-length formula for a $C^1$ parametrized plane curve and use
step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{L=\pi}.
$$


::: pf-proof

Evaluate
$$
\int_0^\pi1\,dt
=
\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested length.

:::

:::

:::
