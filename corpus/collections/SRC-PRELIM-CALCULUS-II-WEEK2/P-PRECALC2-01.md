---
schema: qual/card@1
id: P-PRECALC2-01
kind: problem
title: Arc length of the upper unit semicircle
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the length of the curve $( x ( t ) , y ( t ) ) = ( \cos ( t ) , \sin ( t ) )$ for $0 \leq t \leq \pi ?$
:::

::: {.solution}
<1>1. The coordinate derivatives are
\[
\boxed{x'(t)=-\sin t}
\]
and
\[
\boxed{y'(t)=\cos t}.
\]

::: {.proof}
Differentiate
\[
x(t)=\cos t,
\qquad
y(t)=\sin t.
\]
:::

<1>2. The speed of the parametrized curve is
\[
\boxed{
\sqrt{x'(t)^2+y'(t)^2}=1}.
\]

::: {.proof}
By step <1>1,
\[
\begin{aligned}
\sqrt{x'(t)^2+y'(t)^2}
&=
\sqrt{\sin^2t+\cos^2t}\\
&=
\sqrt1\\
&=
1.
\end{aligned}
\]
:::

<1>3. Therefore the arc length is
\[
L
=
\int_0^\pi
\sqrt{x'(t)^2+y'(t)^2}\,dt
=
\int_0^\pi1\,dt.
\]

::: {.proof}
Apply the arc-length formula for a \(C^1\) parametrized plane curve and use
step <1>2.
:::

<1>4. Hence
\[
\boxed{L=\pi}.
\]

::: {.proof}
Evaluate
\[
\int_0^\pi1\,dt
=
\pi.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested length.
:::
:::
