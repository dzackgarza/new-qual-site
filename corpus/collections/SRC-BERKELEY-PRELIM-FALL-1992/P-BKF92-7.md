---
schema: qual/card@1
id: P-BKF92-7
kind: problem
title: The integral $\int_{|z|=1} e^z/[z(2z+1)^2]\,dz$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Computed the simple residue at 0 and the double-pole residue at -1/2,
    then applied the residue theorem.
---

::: {.problem}
Evaluate
\[
\int_C\frac{e^z}{z(2z+1)^2}\,dz,
\]
where $C$ is the unit circle oriented counterclockwise.
:::

::: {.solution}
Set
$$
R(z)\coloneqq\frac{e^z}{z(2z+1)^2}.
$$

<1>1. The poles of $R$ inside $C$ are a simple pole at $z=0$ and a double pole at $z=-1/2$.

::: {.proof}
The denominator vanishes only at
$$
z=0
\qquad\text{and}\qquad
z=-\frac12.
$$
Both points lie in $\abs z<1$. The factor $z$ occurs to the first power, while
$$
(2z+1)^2=4(z+1/2)^2.
$$
:::

<1>2. The residue at $z=0$ is
$$
\operatorname{Res}(R;0)=1.
$$

::: {.proof}
Since the pole is simple,
$$
\operatorname{Res}(R;0)
=
\lim_{z\to0}\frac{e^z}{(2z+1)^2}
=1.
$$
:::

<1>3. The residue at $z=-1/2$ is
$$
\operatorname{Res}(R;-1/2)
=
-\frac32e^{-1/2}.
$$

::: {.proof}
Using
$$
R(z)
=
\frac{1}{(z+1/2)^2}\frac{e^z}{4z},
$$
the residue at the double pole is
$$
\left.\frac{d}{dz}\left(\frac{e^z}{4z}\right)\right|_{z=-1/2}.
$$
Now
$$
\frac{d}{dz}\left(\frac{e^z}{4z}\right)
=
\frac14e^z\left(\frac1z-\frac1{z^2}\right),
$$
so at $z=-1/2$ this equals
$$
\frac14e^{-1/2}(-2-4)
=
-\frac32e^{-1/2}.
$$
:::

<1>4. The integral is
$$
\boxed{
2\pi i\left(1-\frac32e^{-1/2}\right)}.
$$

::: {.proof}
By the residue theorem and steps <1>2--<1>3,
$$
\begin{aligned}
\int_C R(z)\,dz
&=2\pi i\left(
\operatorname{Res}(R;0)
+\operatorname{Res}(R;-1/2)
\right)\\
&=2\pi i\left(1-\frac32e^{-1/2}\right).
\end{aligned}
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
