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

::: pf

::: {.pf-step #residue-at-ia}
The only pole of $F$ inside $C_R$ is $z=ia$, and
$$
\Res(F;ia)=\frac{e^{-a}}2.
$$

::: pf-proof
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

:::

::: {.pf-step #arc-integral-vanishes}
The integral over the semicircular arc tends to zero:
$$
\int_{\Gamma_R}F(z)\,dz\longrightarrow0
$$
as $R\to\infty$.

::: pf-proof
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

:::

::: {.pf-step #complex-integral-limit}
One has
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x e^{ix}}{x^2+a^2}\,dx
=
\pi i e^{-a}.
$$

::: pf-proof
By the residue theorem and step [](#residue-at-ia){.pf-ref},
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
Letting $R\to\infty$ and using step [](#arc-integral-vanishes){.pf-ref} gives the displayed limit.
:::

:::

::: {.pf-step #sine-integral-limit}
The symmetric sine integrals satisfy
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x\sin x}{x^2+a^2}\,dx
=
\pi e^{-a}.
$$

::: pf-proof
Taking imaginary parts in step [](#complex-integral-limit){.pf-ref} gives
$$
\lim_{R\to\infty}
\int_{-R}^{R}
\frac{x\sin x}{x^2+a^2}\,dx
=
\pi e^{-a}.
$$
:::

:::

::: {.pf-step #half-line-value}
The requested value is
$$
\boxed{
\int_0^{\infty}
\frac{x\sin x}{x^2+a^2}\,dx
=
\frac{\pi}{2}e^{-a}.
}
$$

::: pf-proof
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
Step [](#sine-integral-limit){.pf-ref} therefore proves that the half-line improper integral converges
and has the displayed value.
:::

:::

::: pf-qed
Step [](#half-line-value){.pf-ref} is the requested value.
:::

:::

:::

::: {.remark}
Some retained UGA/Tie appearances omit a condition on the parameter $a$.
The Azoff appearance explicitly states $a>0$, and a later UGA appearance
states the corresponding whole-line identity for all $a>0$. The problem
above records that hypothesis explicitly.
:::
