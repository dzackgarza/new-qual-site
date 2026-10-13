---
schema: qual/card@1
id: P-TRIV-RA37
kind: problem
title: Area of the surface of revolution of $y=\sin x$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 37, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the surface area of a body formed by rotation of a curve $y = \sin x$ around x-axis in $\mathbb { R } ^ { 3 } , x \in [ 0 , \pi ]$
:::

::: {.solution}
<1>1. For a graph $y=y(x)\geq0$ rotated about the $x$-axis, the surface area is
$$
S
=
2\pi
\int_a^b
y(x)
\sqrt{1+(y'(x))^2}
\,dx.
$$

::: {.proof}
This is the standard surface-of-revolution formula.
:::

<1>2. For
$$
y=\sin x,
$$
one has
$$
y'=\cos x.
$$

::: {.proof}
Differentiate the sine function.
:::

<1>3. Therefore
$$
S
=
2\pi
\int_0^\pi
\sin x
\sqrt{1+\cos^2x}
\,dx.
$$

::: {.proof}
On $[0,\pi]$, one has $\sin x\geq0$. Substitute step <1>2 into the formula
from step <1>1.
:::

<1>4. Set
$$
u=\cos x.
$$
Then
$$
du=-\sin x\,dx,
$$
and
$$
x=0\longmapsto u=1,
\qquad
x=\pi\longmapsto u=-1.
$$

::: {.proof}
Differentiate $u=\cos x$ and evaluate the endpoints.
:::

<1>5. Hence
$$
S
=
2\pi
\int_{-1}^{1}
\sqrt{1+u^2}
\,du
=
4\pi
\int_0^1
\sqrt{1+u^2}
\,du.
$$

::: {.proof}
Use step <1>4. The integrand is even, giving the second equality.
:::

<1>6. An antiderivative is
$$
\int\sqrt{1+u^2}\,du
=
\frac12
\left(
u\sqrt{1+u^2}
+
\operatorname{arsinh}u
\right)
+
C.
$$

::: {.proof}
Differentiate the right-hand side, using
$$
\frac{d}{du}\operatorname{arsinh}u
=
\frac1{\sqrt{1+u^2}}.
$$
The derivative simplifies to $\sqrt{1+u^2}$.
:::

<1>7. Therefore
$$
\int_0^1
\sqrt{1+u^2}
\,du
=
\frac12
\left(
\sqrt2
+
\operatorname{arsinh}1
\right).
$$

::: {.proof}
Evaluate the antiderivative from step <1>6 at $u=1$ and $u=0$.
:::

<1>8. Since
$$
\operatorname{arsinh}1
=
\log(1+\sqrt2),
$$
the surface area is
$$
\boxed{
S
=
2\pi
\left(
\sqrt2
+
\log(1+\sqrt2)
\right).
}
$$

::: {.proof}
Substitute step <1>7 into step <1>5 and use the logarithmic formula for
$\operatorname{arsinh}$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required surface area.
:::
:::
