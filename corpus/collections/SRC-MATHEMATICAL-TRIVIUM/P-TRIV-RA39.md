---
schema: qual/card@1
id: P-TRIV-RA39
kind: problem
title: Volume of the solid of revolution of $y=\arcsin x$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 39, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the volume of a body formed by rotation of the curve y = arcsin x around x-axis in $\mathbb { R } ^ { 3 } , x \in [ 0 , 1 ]$
:::

::: {.solution}
<1>1. Rotating the region under
$$
y=\arcsin x,
\qquad
0\leq x\leq1,
$$
about the $x$-axis gives cross-sectional disks of radius $\arcsin x$.

::: {.proof}
At a fixed $x$, rotation around the $x$-axis turns the vertical segment
$0\leq y\leq\arcsin x$ into a disk of radius $\arcsin x$.
:::

<1>2. Therefore the volume is
$$
V
=
\pi
\int_0^1
(\arcsin x)^2
\,dx.
$$

::: {.proof}
The area of a cross-sectional disk is
$$
\pi(\arcsin x)^2.
$$
Integrate this area from $x=0$ to $x=1$.
:::

<1>3. Set
$$
t=\arcsin x.
$$
Then
$$
x=\sin t,
\qquad
dx=\cos t\,dt,
$$
and the limits become
$$
0\leq t\leq\frac\pi2.
$$

::: {.proof}
These are the inverse-function relations between sine and arcsine on
$[-\pi/2,\pi/2]$.
:::

<1>4. Hence
$$
\int_0^1
(\arcsin x)^2
\,dx
=
\int_0^{\pi/2}
t^2\cos t
\,dt.
$$

::: {.proof}
Substitute the relations from step <1>3.
:::

<1>5. Integration by parts gives
$$
\int_0^{\pi/2}
t^2\cos t
\,dt
=
\frac{\pi^2}{4}
-
2
\int_0^{\pi/2}
t\sin t
\,dt.
$$

::: {.proof}
Take
$$
u=t^2,
\qquad
dv=\cos t\,dt.
$$
Then
$$
du=2t\,dt,
\qquad
v=\sin t.
$$
Thus
$$
\left[t^2\sin t\right]_0^{\pi/2}
-
2\int_0^{\pi/2}t\sin t\,dt
$$
is the value of the integral, and the boundary term equals $\pi^2/4$.
:::

<1>6. One has
$$
\int_0^{\pi/2}
t\sin t
\,dt
=1.
$$

::: {.proof}
Integrate by parts:
$$
\int t\sin t\,dt
=
-t\cos t+\sin t.
$$
Evaluating from $0$ to $\pi/2$ gives $1$.
:::

<1>7. Therefore
$$
\int_0^1
(\arcsin x)^2
\,dx
=
\frac{\pi^2}{4}-2.
$$

::: {.proof}
Combine steps <1>5--<1>6.
:::

<1>8. Hence the volume is
$$
\boxed{
V
=
\pi\left(
\frac{\pi^2}{4}-2
\right)
=
\frac{\pi^3}{4}-2\pi.
}
$$

::: {.proof}
Substitute step <1>7 into step <1>2.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required volume.
:::
:::
