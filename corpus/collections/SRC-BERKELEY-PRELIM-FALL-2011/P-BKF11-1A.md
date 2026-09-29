---
schema: qual/card@1
id: P-BKF11-1A
kind: problem
title: Volume of the intersection of two perpendicular unit cylinders
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the horizontal cross-sections and the resulting one-variable
    volume integral.
---

::: {.problem}
Find the volume of the solid given by
$$
x^2+z^2\le 1,\qquad y^2+z^2\le 1.
$$
:::

::: {.hint}
Use an integral of the form
$$
\int_{-1}^1(\text{something})\,dz.
$$
:::

::: {.solution}
Let
$$
S\coloneqq
\{(x,y,z)\in\RR^3:
x^2+z^2\le1,\ y^2+z^2\le1\}.
$$

::: pf

::: {.pf-step #s1}

For each $z\in[-1,1]$, the horizontal cross-section
$$
S_z\coloneqq\{(x,y)\in\RR^2:(x,y,z)\in S\}
$$
is the square
$$
[-\sqrt{1-z^2},\sqrt{1-z^2}]^2,
$$
and therefore has area
$$
A(z)=4(1-z^2).
$$

::: pf-proof

Fix $z\in[-1,1]$. The two defining inequalities for $S$ are equivalent
to
$$
x^2\le1-z^2,
\qquad
y^2\le1-z^2.
$$
Thus both $x$ and $y$ range independently over
$[-\sqrt{1-z^2},\sqrt{1-z^2}]$. The resulting square has side length
$2\sqrt{1-z^2}$, so its area is $4(1-z^2)$.

:::

:::

::: {.pf-step #s2}

The volume of $S$ is
$$
\operatorname{Vol}(S)
=\int_{-1}^1 4(1-z^2)\,dz.
$$

::: pf-proof

If $\abs{z}>1$, then $x^2+z^2\le1$ has no real solution, so $S$ has
no cross-section there. By Fubini's theorem, the volume is the integral
of the cross-sectional area. Step [](#s1){.pf-ref} gives that area for
$-1\le z\le1$, yielding the displayed integral.

:::

:::

::: {.pf-step #s3}

The volume is
$$
\boxed{\operatorname{Vol}(S)=\frac{16}{3}}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
\operatorname{Vol}(S)
&=4\int_{-1}^1(1-z^2)\,dz\\
&=4\left[z-\frac{z^3}{3}\right]_{-1}^1\\
&=4\left(\frac23-\left(-\frac23\right)\right)\\
&=\frac{16}{3}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested volume.

:::

:::

:::
