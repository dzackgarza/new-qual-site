---
schema: qual/card@1
id: P-BKF83-1
kind: problem
title: Fourier transform of $\operatorname{sech}^2x$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the height-pi contour identity, the double-pole residue at i*pi/2, decay on the vertical sides, and the lambda=0 limit.
---

::: {.problem}
Let $\lambda\in\mathbb R$. Evaluate
\[
\int_0^\infty (\operatorname{sech}x)^2\cos(\lambda x)\,dx,
\]
where
\[
\operatorname{sech}x=\frac{2}{e^x+e^{-x}}.
\]
:::

::: {.solution}

::: pf

::: pf-step

For $\lambda>0$, set
$$
F_\lambda(z)\coloneqq
\frac{e^{i\lambda z}}{\cosh^2 z}.
$$
On the rectangle with vertices
$$
-R,\quad R,\quad R+i\pi,\quad -R+i\pi,
$$
the only pole of $F_\lambda$ is the double pole
$$
z_0=\frac{i\pi}{2}.
$$

::: pf-proof

The zeros of $\cosh z$ are
$$
z=\frac{(2k+1)i\pi}{2},
\qquad
k\in\ZZ.
$$
Exactly one of them lies in the strip
$$
0<\operatorname{Im}z<\pi,
$$
namely $z_0=i\pi/2$. Since each zero of $\cosh z$ is simple,
$F_\lambda$ has a double pole there.

:::

:::

::: {.pf-step #s2}

The residue at $z_0=i\pi/2$ is
$$
\operatorname{Res}_{z=z_0}F_\lambda
=
-i\lambda e^{-\pi\lambda/2}.
$$

::: pf-proof

Write
$$
z=z_0+w.
$$
Then
$$
\cosh(z_0+w)=i\sinh w,
$$
so
$$
F_\lambda(z_0+w)
=
-e^{-\pi\lambda/2}
\frac{e^{i\lambda w}}{\sinh^2w}.
$$
As $w\to0$,
$$
\frac1{\sinh^2w}
=
\frac1{w^2}+O(1),
\qquad
e^{i\lambda w}
=
1+i\lambda w+O(w^2).
$$
Thus the coefficient of $w^{-1}$ is
$$
-i\lambda e^{-\pi\lambda/2},
$$
which is the residue.

:::

:::

::: {.pf-step #s3}

If
$$
I(\lambda)
\coloneqq
\int_{-\infty}^{\infty}
\frac{e^{i\lambda x}}{\cosh^2x}\,dx,
$$
then for $\lambda>0$,
$$
I(\lambda)
=
\frac{\pi\lambda}{\sinh(\pi\lambda/2)}.
$$

::: pf-proof

Let $B_R$ denote the integral of $F_\lambda$ along the bottom edge of the
rectangle:
$$
B_R
=
\int_{-R}^{R}
\frac{e^{i\lambda x}}{\cosh^2x}\,dx.
$$
Along the top edge, oriented from $R+i\pi$ to $-R+i\pi$, use
$$
\cosh(x+i\pi)=-\cosh x
$$
to obtain
$$
\int_{\text{top}}F_\lambda(z)\,dz
=
-e^{-\pi\lambda}B_R.
$$

On either vertical edge,
$$
\begin{aligned}
\abs{\cosh(\pm R+iy)}^2
&=
\cosh^2R\cos^2y+\sinh^2R\sin^2y\\
&=
\sinh^2R+\cos^2y\\
&\ge
\sinh^2R.
\end{aligned}
$$
Also, for $0\le y\le\pi$,
$$
\abs{e^{i\lambda(\pm R+iy)}}=e^{-\lambda y}\le1.
$$
Each vertical edge has length $\pi$, so its integral has absolute value at
most
$$
\frac{\pi}{\sinh^2R},
$$
which tends to zero.

The residue theorem and step [](#s2){.pf-ref} therefore give, after letting
$R\to\infty$,
$$
\left(1-e^{-\pi\lambda}\right)I(\lambda)
=
2\pi i
\left(-i\lambda e^{-\pi\lambda/2}\right)
=
2\pi\lambda e^{-\pi\lambda/2}.
$$
Since
$$
1-e^{-\pi\lambda}
=
2e^{-\pi\lambda/2}\sinh(\pi\lambda/2),
$$
the stated formula follows.

:::

:::

::: {.pf-step #s4}

For $\lambda>0$,
$$
\int_0^\infty
(\operatorname{sech}x)^2\cos(\lambda x)\,dx
=
\frac{\pi\lambda}{2\sinh(\pi\lambda/2)}.
$$

::: pf-proof

The function $\operatorname{sech}^2x$ is even. Therefore the sine part of
$I(\lambda)$ is odd and integrates to zero, while the cosine part is even.
Thus
$$
I(\lambda)
=
2\int_0^\infty
(\operatorname{sech}x)^2\cos(\lambda x)\,dx.
$$
Apply step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The formula extends to every real $\lambda$, with value $1$ at
$\lambda=0$:
$$
\boxed{
\int_0^\infty
(\operatorname{sech}x)^2\cos(\lambda x)\,dx
=
\begin{cases}
\dfrac{\pi\lambda}{2\sinh(\pi\lambda/2)},&\lambda\ne0,\\[3mm]
1,&\lambda=0.
\end{cases}}
$$

::: pf-proof

The original integral is an even function of $\lambda$. The quotient
$$
\frac{\pi\lambda}{2\sinh(\pi\lambda/2)}
$$
is also even, so step [](#s4){.pf-ref} gives the formula for $\lambda<0$ as well.
For $\lambda=0$,
$$
\int_0^\infty\operatorname{sech}^2x\,dx
=
\left[\tanh x\right]_0^\infty
=1.
$$
This also equals the limit of the displayed quotient as
$\lambda\to0$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the requested evaluation for every real $\lambda$.

:::

:::

:::
