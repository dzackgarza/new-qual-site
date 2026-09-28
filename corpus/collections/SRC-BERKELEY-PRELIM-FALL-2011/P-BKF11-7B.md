---
schema: qual/card@1
id: P-BKF11-7B
kind: problem
title: Evaluation of $\int_0^{2\pi} d\theta/(1+\frac12\sin\theta)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the unit-circle substitution, the two poles of the rational
    integrand, the interior pole, and its residue.
---

::: {.problem}
Find
$$
\int_0^{2\pi}\frac{1}{1+\frac12\sin\theta}\,d\theta.
$$
:::

::: {.solution}
Let $C$ be the positively oriented unit circle.

<1>1. Under the substitution $z=e^{i\theta}$, the integral becomes
$$
\int_C\frac{4}{z^2+4iz-1}\,dz.
$$

::: {.proof}
On $C$,
$$
d\theta=\frac{dz}{iz},
\qquad
\sin\theta=\frac{z-z^{-1}}{2i}.
$$
Therefore
$$
\begin{aligned}
\frac{1}{1+\frac12\sin\theta}\,d\theta
&=
\frac{1}
{1+\frac{z-z^{-1}}{4i}}
\frac{dz}{iz}\\
&=
\frac{4}{z^2+4iz-1}\,dz.
\end{aligned}
$$
Traversing $0\le\theta\le2\pi$ traces $C$ once counterclockwise.
:::

<1>2. The poles of the integrand in step <1>1 are
$$
z_\pm=(-2\pm\sqrt3)i,
$$
and exactly
$$
z_+=(-2+\sqrt3)i
$$
lies inside $C$.

::: {.proof}
The quadratic formula applied to
$$
z^2+4iz-1=0
$$
gives the displayed roots. Their moduli are
$$
\abs{z_+}=2-\sqrt3<1,
\qquad
\abs{z_-}=2+\sqrt3>1.
$$
Thus only $z_+$ is enclosed by $C$.
:::

<1>3. The residue at the interior pole is
$$
\operatorname*{Res}_{z=z_+}
\frac{4}{z^2+4iz-1}
=\frac{2}{\sqrt3\,i}.
$$

::: {.proof}
The pole $z_+$ is simple, so
$$
\operatorname*{Res}_{z=z_+}
\frac{4}{z^2+4iz-1}
=\frac{4}{2z_++4i}.
$$
Since $z_+=(-2+\sqrt3)i$,
$$
2z_++4i=2\sqrt3\,i,
$$
which gives the stated residue.
:::

<1>4. The value of the integral is
$$
\boxed{\frac{4\pi}{\sqrt3}}.
$$

::: {.proof}
By the residue theorem and steps <1>2 and <1>3,
$$
\int_C\frac{4}{z^2+4iz-1}\,dz
=2\pi i\frac{2}{\sqrt3\,i}
=\frac{4\pi}{\sqrt3}.
$$
Step <1>1 identifies this contour integral with the integral in the
problem.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
