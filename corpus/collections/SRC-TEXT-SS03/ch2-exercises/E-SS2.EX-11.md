---
schema: qual/card@1
id: E-SS2.EX-11
kind: problem
title: The Cauchy formula with kernel $\Re\frac{\zeta+z}{\zeta-z}$ and the Poisson kernel
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, and the two identities rechecked:
    part (b) follows by multiplying by the conjugate of the denominator, whose real part is
    R^2 - r^2 and whose imaginary part is -2iRr sin(gamma); and the identity
    zeta(1/(zeta-z) - 1/(zeta-w)) = Re((zeta+z)/(zeta-z)) on |zeta| = R now carries its
    intermediate step, which the prose omitted: from w = R^2/conj(z) and R^2 = zeta conj(zeta)
    one gets -zeta/(zeta-w) = conj(z)/(conj(zeta) - conj(z)), and the sum is
    1 + 2 Re(z/(zeta-z)) = Re((zeta+z)/(zeta-z)). Also checked: |w| = R^2/|z| > R so Cauchy's
    theorem applies to f(zeta)/(zeta-w) and Cauchy's formula to f(zeta)/(zeta-z), with R < R_0
    so that f is holomorphic on a neighbourhood of the closed disc; d zeta = i zeta d phi turns
    1/(2 pi i) d zeta into zeta d phi/(2 pi). The case z = 0 is the mean value property, as the
    prose says. Added: the resulting Poisson formula, obtained by rotating so that part (b)
    applies. Statement unchanged; no retained solution set covers the exercises of
    Stein-Shakarchi, so the card's solution states the argument is its own.
---

::: {.exercise}
Let $f$ be a holomorphic function on the disk $D_{R_0}(0) \subset \CC$ of radius $R_0 > 0$.

(a) Prove that whenever $0 < R < R_0$ and $\abs{z} < R$,
$$
f(z) = \frac{1}{2\pi} \int_0^{2\pi} f(R e^{i\varphi}) \operatorname{Re}\left( \frac{R e^{i\varphi} + z}{R e^{i\varphi} - z} \right) d\varphi.
$$

(b) Show that
$$
\operatorname{Re}\left( \frac{R e^{i\gamma} + r}{R e^{i\gamma} - r} \right) = \frac{R^2 - r^2}{R^2 - 2Rr\cos\gamma + r^2}.
$$

[Hint: For the first part, note that if $w = R^2/\overline{z}$, then the integral of $f(\zeta)/(\zeta - w)$ around the circle of radius $R$ centered at the origin is zero. Use this, together with the usual Cauchy integral formula, to deduce the desired identity.]
:::

::: {.solution}
Part (b) is an algebra computation with a complex conjugate; part (a) is the printed hint's route, the Cauchy formula at $z$ minus the vanishing integral of $f(\zeta)/(\zeta-w)$ at the reflected point $w=R^2/\overline z$, after which the difference of the two kernels is rewritten as the real part of $(\zeta+z)/(\zeta-z)$. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi. Used below are Cauchy's theorem and Cauchy's integral formula on a disc (Chapter 2, Theorems 4.1 and 4.4) and the mean value property, which is the formula at $z=0$.

::: pf

::: {.pf-step #partb}
(b) For real $r$ and real $\gamma$, $\displaystyle\Re\frac{Re^{i\gamma}+r}{Re^{i\gamma}-r}=\frac{R^2-r^2}{R^2-2Rr\cos\gamma+r^2}$.

::: pf-proof
Multiply numerator and denominator by $\overline{Re^{i\gamma}-r}=Re^{-i\gamma}-r$:
$$
\frac{Re^{i\gamma}+r}{Re^{i\gamma}-r}=\frac{(Re^{i\gamma}+r)(Re^{-i\gamma}-r)}{\abs{Re^{i\gamma}-r}^2}.
$$
The denominator is $\abs{Re^{i\gamma}-r}^2=R^2-2Rr\cos\gamma+r^2$. The numerator expands to $R^2-Rre^{i\gamma}+rRe^{-i\gamma}-r^2=R^2-r^2-2iRr\sin\gamma$, whose real part is $R^2-r^2$ and whose imaginary part is purely imaginary. Taking real parts gives the display.
:::

:::


::: {.pf-step #setup}
Let $0<\abs z<R<R_0$ and put $w=R^2/\overline z$. Then $\abs w>R$, so $f$ is holomorphic on a disc containing the closed disc of radius $R$, and
$$
f(z)=\frac1{2\pi i}\oint_{\abs\zeta=R}f(\zeta)\Bigl(\frac1{\zeta-z}-\frac1{\zeta-w}\Bigr)\dd\zeta .$$

::: pf-proof
$\abs w=R^2/\abs z>R$. Also $R<R_0$ and $f$ is holomorphic on $D_{R_0}(0)$, so $f$ is holomorphic on a neighbourhood of the closed disc $\abs\zeta\le R$. Cauchy's integral formula (Chapter 2, Theorem 4.4) gives $f(z)=\frac1{2\pi i}\oint_{\abs\zeta=R}\frac{f(\zeta)}{\zeta-z}\,\dd\zeta$, the point $z$ being inside the circle. Since $\zeta\mapsto f(\zeta)/(\zeta-w)$ is holomorphic on and inside the circle $\abs\zeta=R$, Cauchy's theorem (Chapter 2, Theorem 4.1) gives $\oint_{\abs\zeta=R}\frac{f(\zeta)}{\zeta-w}\,\dd\zeta=0$. Subtracting the second identity from the first gives the display.
:::

:::


::: {.pf-step #kernel}
On the circle $\abs\zeta=R$, $\displaystyle\zeta\Bigl(\frac1{\zeta-z}-\frac1{\zeta-w}\Bigr)=\Re\frac{\zeta+z}{\zeta-z}$.

::: pf-proof
On $\abs\zeta=R$ one has $R^2=\zeta\overline\zeta$, so
$$
\zeta-w=\zeta-\frac{R^2}{\overline z}=\frac{\zeta\overline z-R^2}{\overline z}=\frac{\zeta\overline z-\zeta\overline\zeta}{\overline z}=\frac{\zeta(\overline z-\overline\zeta)}{\overline z},
$$
hence $-\dfrac{\zeta}{\zeta-w}=\dfrac{\overline z}{\overline\zeta-\overline z}$. Therefore
$$
\zeta\Bigl(\frac1{\zeta-z}-\frac1{\zeta-w}\Bigr)=\frac{\zeta}{\zeta-z}+\frac{\overline z}{\overline\zeta-\overline z}.
$$
Now $\dfrac{\zeta}{\zeta-z}=1+\dfrac{z}{\zeta-z}$, and $\dfrac{\overline z}{\overline\zeta-\overline z}=\overline{\Bigl(\dfrac{z}{\zeta-z}\Bigr)}$, so the sum equals $1+2\Re\dfrac{z}{\zeta-z}$. On the other hand
$$
\frac{\zeta+z}{\zeta-z}=\frac{(\zeta-z)+2z}{\zeta-z}=1+\frac{2z}{\zeta-z},
$$
whose real part is $1+2\Re\frac{z}{\zeta-z}$. The two expressions agree.
:::

:::


::: {.pf-step #parta}
(a) For $0<\abs z<R$, $\displaystyle f(z)=\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\Re\Bigl(\frac{Re^{i\varphi}+z}{Re^{i\varphi}-z}\Bigr)\dd\varphi$.

::: pf-proof
Parametrize $\zeta=Re^{i\varphi}$, so that $\dd\zeta=iRe^{i\varphi}\dd\varphi=i\zeta\,\dd\varphi$ and $\frac1{2\pi i}\dd\zeta=\frac{\zeta}{2\pi}\dd\varphi$. By step [](#setup){.pf-ref},
$$
f(z)=\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\,\zeta\Bigl(\frac1{\zeta-z}-\frac1{\zeta-w}\Bigr)\dd\varphi
=\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\Re\Bigl(\frac{Re^{i\varphi}+z}{Re^{i\varphi}-z}\Bigr)\dd\varphi,
$$
the second equality by step [](#kernel){.pf-ref} with $\zeta=Re^{i\varphi}$.
:::

:::


::: {.pf-step #origin}
At $z=0$ the same identity holds, and it is the mean value property: $f(0)=\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\,\dd\varphi$.

::: pf-proof
At $z=0$ the kernel of step [](#kernel){.pf-ref} is $\Re\frac{\zeta}{\zeta}=1$ for every $\zeta$ on the circle, so the right-hand side of part (a) is $\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\dd\varphi$; and that equals $f(0)$ by the mean value property, which is Cauchy's integral formula at the centre of the disc (Chapter 2, Theorem 4.4 with $z=0$). So the formula of part (a) holds for every $\abs z<R$, which is what the statement asks.
:::

:::


::: {.pf-step #poisson}
Combining the two parts, for $z=re^{i\theta}$ with $0\le r<R$, $\displaystyle f(z)=\frac1{2\pi}\int_0^{2\pi}f(Re^{i\varphi})\frac{R^2-r^2}{R^2-2Rr\cos(\varphi-\theta)+r^2}\,\dd\varphi$.

::: pf-proof
Rotating by $e^{-i\theta}$ reduces the kernel to the case of part (b): with $\gamma=\varphi-\theta$, the quotient $\frac{Re^{i\varphi}+z}{Re^{i\varphi}-z}$ equals $\frac{Re^{i\gamma}+r}{Re^{i\gamma}-r}$ after multiplying numerator and denominator by $e^{-i\theta}$, and a real factor does not change a real part; taking real parts of the value computed in step [](#partb){.pf-ref} gives the displayed kernel. This is the Poisson formula for the disc, and it is recorded here because it is the form in which the identity of part (a) is usually applied.
:::

:::

:::
:::
