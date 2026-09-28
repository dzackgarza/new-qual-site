---
schema: qual/card@1
id: P-TIE-F09-04
kind: problem
title: $\int_0^\infty\frac{x\sin x}{x^2+a^2}\,dx$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 4.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The Fall 2009/Tie appearances omit a hypothesis on a. The Azoff
    appearance explicitly states a>0, and the later Spring 2020 UGA
    appearance states the corresponding whole-line identity for all a>0.
    The canonical card now includes a>0 so the parameter and requested value
    are unambiguous.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Integrated z exp(iz)/(z^2+a^2) over an upper semicircle, proved the arc
    contribution tends to zero by an elementary sine bound, evaluated the
    residue at ia, and took imaginary parts and evenness to obtain
    (pi/2)e^(-a).
---

::: {.problem}
Let $a>0$. Evaluate

$$
\int _ { 0 } ^ { \infty } { \frac { x \sin x } { x ^ { 2 } + a ^ { 2 } } } d x .
$$
:::

::: {.solution}
Set
$$
F(z)=\frac{ze^{iz}}{z^2+a^2}.
$$
For $R>a$, let $C_R$ be the positively oriented contour consisting of
$[-R,R]$ and the upper semicircle
$$
\Gamma_R=\{Re^{i\theta}:0\leq\theta\leq\pi\}.
$$

<1>1. The only pole of $F$ inside $C_R$ is $z=ia$, and
$$
\Res(F;ia)=\frac{e^{-a}}2.
$$

::: {.proof}
Since
$$
z^2+a^2=(z-ia)(z+ia),
$$
the poles are $\pm ia$. Because $a>0$, only $ia$ lies in the upper
half-plane. Its residue is
$$
\begin{aligned}
\Res(F;ia)
&=
\lim_{z\to ia}
\frac{ze^{iz}}{z+ia}\\
&=
\frac{ia\,e^{-a}}{2ia}\\
&=
\frac{e^{-a}}2.
\end{aligned}
$$
:::

<1>2. The integral over the semicircular arc tends to zero:
$$
\int_{\Gamma_R}F(z)\,dz\longrightarrow0
$$
as $R\to\infty$.

::: {.proof}
On $z=Re^{i\theta}$,
$$
\abs{e^{iz}}=e^{-R\sin\theta}.
$$
Also, for $R>a$,
$$
\abs{z^2+a^2}
\geq
R^2-a^2,
$$
so
$$
\abs{F(Re^{i\theta})}
\leq
\frac{R}{R^2-a^2}e^{-R\sin\theta}.
$$
Parametrizing the arc gives
$$
\abs{
\int_{\Gamma_R}F(z)\,dz
}
\leq
\frac{R^2}{R^2-a^2}
\int_0^\pi e^{-R\sin\theta}\,d\theta.
$$

For $0\leq\theta\leq\pi/2$,
$$
\sin\theta\geq\frac{2\theta}{\pi}.
$$
By symmetry,
$$
\begin{aligned}
\int_0^\pi e^{-R\sin\theta}\,d\theta
&=
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta\\
&\leq
2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta\\
&=
\frac{\pi}{R}(1-e^{-R})\\
&\leq
\frac{\pi}{R}.
\end{aligned}
$$
Therefore
$$
\abs{
\int_{\Gamma_R}F(z)\,dz
}
\leq
\frac{\pi R}{R^2-a^2}
\longrightarrow0.
$$
:::

<1>3. One has
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x e^{ix}}{x^2+a^2}\,dx
=
\pi i e^{-a}.
$$

::: {.proof}
By the residue theorem and step <1>1,
$$
\int_{C_R}F(z)\,dz
=
2\pi i\Res(F;ia)
=
\pi i e^{-a}.
$$
Thus
$$
\int_{-R}^{R}\frac{x e^{ix}}{x^2+a^2}\,dx
+
\int_{\Gamma_R}F(z)\,dz
=
\pi i e^{-a}.
$$
Letting $R\to\infty$ and using step <1>2 gives the displayed limit.
:::

<1>4. The symmetric sine integrals satisfy
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x\sin x}{x^2+a^2}\,dx
=
\pi e^{-a}.
$$

::: {.proof}
Taking imaginary parts in step <1>3 gives
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x\sin x}{x^2+a^2}\,dx
=
\pi e^{-a}.
$$
:::

<1>5. The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{x\sin x}{x^2+a^2}\,dx
=
\frac{\pi}{2}e^{-a}.
}
$$

::: {.proof}
The function
$$
x\longmapsto\frac{x\sin x}{x^2+a^2}
$$
is even. Hence for every $R>0$,
$$
\int_{-R}^{R}
\frac{x\sin x}{x^2+a^2}\,dx
=
2\int_0^R
\frac{x\sin x}{x^2+a^2}\,dx.
$$
Step <1>4 therefore proves that the half-line improper integral converges
and has the displayed value.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested value.
:::
:::

::: {.remark}
Some retained UGA/Tie appearances omit a condition on the parameter $a$.
The Azoff appearance explicitly states $a>0$, and a later UGA appearance
states the corresponding whole-line identity for all $a>0$. The problem
above records that hypothesis explicitly.
:::
