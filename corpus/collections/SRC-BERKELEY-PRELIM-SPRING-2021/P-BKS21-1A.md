---
schema: qual/card@1
id: P-BKS21-1A
kind: problem
title: Volume of the intersection of two perpendicular cylinders
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 cross-sectional integration. The square cross-section and value $16/3$ are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the $z$-range, the side length and area of each cross-section, and the final integral.
---

::: {.problem}
Find the volume of the solid
$$
x^2+z^2\le1,\qquad y^2+z^2\le1.
$$
:::

::: {.solution}
<1>1. For a fixed $z\in[-1,1]$, the cross-section of the solid by the plane of that $z$ is the square
$$
|x|\leq\sqrt{1-z^2},
\qquad
|y|\leq\sqrt{1-z^2}.
$$

::: {.proof}
The two defining inequalities are equivalent, for fixed $z$, to
$$
x^2\leq1-z^2,
\qquad
y^2\leq1-z^2.
$$
Such points exist exactly when $1-z^2\geq0$, namely for $-1\leq z\leq1$, and then the displayed bounds follow.
:::

<1>2. The area of the cross-section in step <1>1 is
$$
A(z)=4(1-z^2).
$$

::: {.proof}
Each side of the square has length
$$
2\sqrt{1-z^2},
$$
so its area is
$$
\left(2\sqrt{1-z^2}\right)^2=4(1-z^2).
$$
:::

<1>3. The volume is
$$
\boxed{V=\frac{16}{3}}.
$$

::: {.proof}
By slicing perpendicular to the $z$-axis and using step <1>2,
$$
\begin{aligned}
V
&=\int_{-1}^{1}A(z)\,dz\\
&=4\int_{-1}^{1}(1-z^2)\,dz\\
&=4\left[z-\frac{z^3}{3}\right]_{-1}^{1}\\
&=\frac{16}{3}.
\end{aligned}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested volume.
:::
:::
