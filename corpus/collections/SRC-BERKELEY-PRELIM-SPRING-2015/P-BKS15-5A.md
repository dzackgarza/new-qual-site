---
schema: qual/card@1
id: P-BKS15-5A
kind: problem
title: Difference of contour integrals for $e^{\pi/z}/(z^2+4)$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the annular residue-theorem reduction and both simple-pole residues at z=2i and z=-2i.
---

::: {.problem}
Compute the difference
$$
\int_{|z|=3}\frac{e^{\pi/z}}{z^2+4}\,dz-
\int_{|z|=1}\frac{e^{\pi/z}}{z^2+4}\,dz,
$$
where both integrals are taken counterclockwise.
:::

::: {.solution}
Set
$$
f(z)\coloneqq\frac{e^{\pi/z}}{z^2+4}.
$$

<1>1. In the annulus
$$
1<\abs{z}<3,
$$
the only singularities of $f$ are the simple poles $z=2i$ and $z=-2i$.

::: {.proof}
The factor $e^{\pi/z}$ is holomorphic away from $z=0$, which lies inside the inner circle and hence outside the annulus. Also
$$
z^2+4=(z-2i)(z+2i),
$$
so the only zeros of the denominator are $\pm2i$, both of modulus $2$ and both simple.
:::

<1>2. The required difference equals
$$
2\pi i\left(
\operatorname{Res}_{z=2i}f
+
\operatorname{Res}_{z=-2i}f
\right).
$$

::: {.proof}
Apply the residue theorem to the annulus $1<\abs{z}<3$. Its positively oriented boundary consists of the outer circle $\abs{z}=3$ counterclockwise and the inner circle $\abs{z}=1$ clockwise. Thus the boundary integral is exactly the stated outer counterclockwise integral minus the stated inner counterclockwise integral. Step <1>1 identifies the poles in the annulus.
:::

<1>3. One has
$$
\operatorname{Res}_{z=2i}f=-\frac14.
$$

::: {.proof}
Since $2i$ is a simple zero of $z^2+4$,
$$
\begin{aligned}
\operatorname{Res}_{z=2i}f
&=
\frac{e^{\pi/(2i)}}{2(2i)}\\
&=
\frac{e^{-i\pi/2}}{4i}\\
&=
\frac{-i}{4i}
=
-\frac14.
\end{aligned}
$$
:::

<1>4. One has
$$
\operatorname{Res}_{z=-2i}f=-\frac14.
$$

::: {.proof}
Similarly,
$$
\begin{aligned}
\operatorname{Res}_{z=-2i}f
&=
\frac{e^{\pi/(-2i)}}{2(-2i)}\\
&=
\frac{e^{i\pi/2}}{-4i}\\
&=
\frac{i}{-4i}
=
-\frac14.
\end{aligned}
$$
:::

<1>5. Therefore the required difference is
$$
\boxed{-\pi i}.
$$

::: {.proof}
Substitute steps <1>3 and <1>4 into step <1>2:
$$
2\pi i\left(-\frac14-\frac14\right)
=
-\pi i.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested value.
:::
:::
