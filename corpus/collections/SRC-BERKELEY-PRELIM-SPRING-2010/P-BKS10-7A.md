---
schema: qual/card@1
id: P-BKS10-7A
kind: problem
title: Evaluation of $\int_0^\infty\frac{x\sin 2x}{x^2+3}\,dx$ by residues
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the upper-half-plane residue, the explicit semicircle decay estimate, and the factor relating the full-line imaginary part to the requested half-line integral.
---

::: {.problem}
Use residues to compute
$$
\int_0^\infty \frac{x\sin(2x)}{x^2+3}\,dx.
$$
:::

::: {.solution}
Set
$$
F(z)\coloneqq\frac{ze^{2iz}}{z^2+3}.
$$
For $R>\sqrt3$, let $C_R$ be the upper semicircle
$$
z=Re^{i\theta},
\qquad
0\leq\theta\leq\pi,
$$
oriented from $R$ to $-R$.

<1>1. The semicircular contribution tends to zero:
$$
\lim_{R\to\infty}\int_{C_R}F(z)\,dz=0.
$$

::: {.proof}
On $C_R$,
$$
\abs{z^2+3}
\geq
R^2-3
$$
and
$$
\abs{e^{2iz}}
=
e^{-2R\sin\theta}.
$$
Since
$$
\abs{dz}=R\,d\theta,
$$
one obtains
$$
\abs{\int_{C_R}F(z)\,dz}
\leq
\frac{R^2}{R^2-3}
\int_0^\pi e^{-2R\sin\theta}\,d\theta.
$$
For $0\leq\theta\leq\pi/2$,
$$
\sin\theta\geq\frac{2\theta}{\pi}.
$$
By symmetry,
$$
\begin{aligned}
\int_0^\pi e^{-2R\sin\theta}\,d\theta
&\leq
2\int_0^{\pi/2}e^{-4R\theta/\pi}\,d\theta\\
&\leq
\frac{\pi}{2R}.
\end{aligned}
$$
Therefore
$$
\abs{\int_{C_R}F(z)\,dz}
\leq
\frac{\pi R}{2(R^2-3)}
\longrightarrow0.
$$
:::

<1>2. The only pole of $F$ in the upper half-plane is
$$
z=i\sqrt3,
$$
and its residue is
$$
\operatorname{Res}_{z=i\sqrt3}F(z)
=
\frac12e^{-2\sqrt3}.
$$

::: {.proof}
The poles are at
$$
z=\pm i\sqrt3,
$$
so only $i\sqrt3$ lies in the upper half-plane. Since the pole is simple,
$$
\begin{aligned}
\operatorname{Res}_{z=i\sqrt3}F(z)
&=
\frac{i\sqrt3\,e^{2i(i\sqrt3)}}{2i\sqrt3}\\
&=
\frac12e^{-2\sqrt3}.
\end{aligned}
$$
:::

<1>3. One has
$$
\lim_{R\to\infty}
\int_{-R}^{R}\frac{xe^{2ix}}{x^2+3}\,dx
=
\pi i e^{-2\sqrt3}.
$$

::: {.proof}
For $R>\sqrt3$, the residue theorem on the contour consisting of
$[-R,R]$ and $C_R$ gives
$$
\int_{-R}^{R}\frac{xe^{2ix}}{x^2+3}\,dx
+
\int_{C_R}F(z)\,dz
=
2\pi i
\operatorname{Res}_{z=i\sqrt3}F(z).
$$
Apply steps <1>1 and <1>2 and let $R\to\infty$.
:::

<1>4. The requested integral is
$$
\boxed{
\int_0^\infty\frac{x\sin(2x)}{x^2+3}\,dx
=
\frac{\pi}{2}e^{-2\sqrt3}
}.
$$

::: {.proof}
Taking imaginary parts in step <1>3 gives
$$
\lim_{R\to\infty}
\int_{-R}^{R}\frac{x\sin(2x)}{x^2+3}\,dx
=
\pi e^{-2\sqrt3}.
$$
The integrand
$$
x\longmapsto\frac{x\sin(2x)}{x^2+3}
$$
is even. Hence, for every $R>0$,
$$
\int_{-R}^{R}\frac{x\sin(2x)}{x^2+3}\,dx
=
2\int_0^R\frac{x\sin(2x)}{x^2+3}\,dx.
$$
Dividing the limiting identity by $2$ proves the displayed value and, at
the same time, the existence of the improper integral.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required residue evaluation.
:::
:::
