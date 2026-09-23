---
schema: qual/card@1
id: P-BERK96S-03
kind: problem
title: Evaluate $\int_0^{2\pi}(2+\cos\theta)^{-1}\,d\theta$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the symmetry reduction, the tangent half-angle substitution
    through the endpoint limit, and the resulting value.
---

::: {.problem}
Evaluate
\[
\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}.
\]
:::

::: {.solution}
Set
$$
I\coloneqq\int_0^{2\pi}\frac{d\theta}{2+\cos\theta}.
$$

<1>1. One has
$$
I=2\int_0^\pi\frac{d\theta}{2+\cos\theta}.
$$

::: {.proof}
With
$$
f(\theta)\coloneqq\frac{1}{2+\cos\theta},
$$
the substitution $u=2\pi-\theta$ gives
$$
\int_\pi^{2\pi}f(\theta)\,d\theta
=\int_0^\pi f(2\pi-u)\,du.
$$
Since $\cos(2\pi-u)=\cos u$, the last integral equals
$\int_0^\pi f(u)\,du$. Splitting the defining integral for $I$ at
$\pi$ proves the claim.
:::

<1>2. The half-period integral satisfies
$$
\int_0^\pi\frac{d\theta}{2+\cos\theta}
=2\int_0^\infty\frac{dt}{t^2+3}.
$$

::: {.proof}
For $0\leq\theta<\pi$, put
$$
t\coloneqq\tan\frac{\theta}{2}.
$$
Then
$$
\cos\theta=\frac{1-t^2}{1+t^2},
\qquad
d\theta=\frac{2\,dt}{1+t^2},
$$
and $t$ increases from $0$ to $+\infty$ as $\theta$ increases from
$0$ to $\pi$. Hence
$$
\frac{d\theta}{2+\cos\theta}
=
\frac{2\,dt}{t^2+3}.
$$
Applying the substitution first on $[0,b]$ with $b<\pi$ and then
letting $b\uparrow\pi$ yields the stated identity.
:::

<1>3. The requested value is
$$
I=\boxed{\frac{2\pi}{\sqrt3}}.
$$

::: {.proof}
By step <1>2,
$$
\int_0^\pi\frac{d\theta}{2+\cos\theta}
=
\frac{2}{\sqrt3}
\left[
\arctan\left(\frac{t}{\sqrt3}\right)
\right]_{0}^{\infty}
=\frac{\pi}{\sqrt3}.
$$
Step <1>1 therefore gives
$$
I=2\cdot\frac{\pi}{\sqrt3}
=\frac{2\pi}{\sqrt3}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 evaluates the required integral.
:::
:::
