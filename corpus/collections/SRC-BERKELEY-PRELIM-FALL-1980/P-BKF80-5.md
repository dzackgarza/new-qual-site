---
schema: qual/card@1
id: P-BKF80-5
kind: problem
title: Evaluate $\int_0^\infty x^{m-1}/(1+x^n)\,dx$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $m,n$ be positive integers with $0<m<n$. Evaluate
$$
\int_0^\infty \frac{x^{m-1}}{1+x^n}\,dx.
$$
:::

::: {.solution}
Set
$$
I\coloneqq\int_0^\infty\frac{x^{m-1}}{1+x^n}\,dx,
\qquad
\theta\coloneqq\frac{\pi m}{n}.
$$

<1>1. The improper integral $I$ converges.

::: {.proof}
Near $0$ the integrand is $O(x^{m-1})$, which is integrable because $m>0$. As $x\to\infty$,
$$
\frac{x^{m-1}}{1+x^n}=O(x^{m-n-1}),
$$
and $m-n-1<-1$ because $m<n$. Hence the integral converges at both endpoints.
:::

<1>2. Let
$$
h(z)\coloneqq\frac{z^{m-1}}{1+z^n}.
$$
For $R>1$, integrate $h$ counterclockwise around the sector bounded by the rays $\arg z=0$ and $\arg z=2\pi/n$ and the circle $\abs z=R$. Then
$$
\int_{\Gamma_R}h(z)\,dz
=\left(1-e^{2\pi i m/n}\right)
\int_0^R\frac{x^{m-1}}{1+x^n}\,dx+o(1)
$$
as $R\to\infty$.

::: {.proof}
Along the positive real ray, the radial contribution is
$$
\int_0^R\frac{x^{m-1}}{1+x^n}\,dx.
$$
On the upper ray write $z=re^{2\pi i/n}$. Its orientation is from $R$ back to $0$, and
$$
h(z)\,dz
=e^{2\pi i m/n}\frac{r^{m-1}}{1+r^n}\,dr.
$$
Thus that ray contributes
$$
-e^{2\pi i m/n}\int_0^R\frac{r^{m-1}}{1+r^n}\,dr.
$$

On the circular arc $\abs z=R$ one has, for sufficiently large $R$,
$$
\abs{h(z)}
\leq \frac{R^{m-1}}{R^n-1},
$$
while the arc length is $2\pi R/n$. Hence its integral is $O(R^{m-n})$, which tends to $0$ because $m<n$.
:::

<1>3. The sector contains exactly one pole of $h$, namely
$$
z_0=e^{i\pi/n},
$$
and
$$
\operatorname{Res}_{z=z_0}h(z)
=-\frac1n e^{i\pi m/n}.
$$

::: {.proof}
The poles of $h$ are the roots of $z^n=-1$, with arguments $(2k+1)\pi/n$. Exactly one of these has argument strictly between $0$ and $2\pi/n$, namely $z_0=e^{i\pi/n}$. It is simple, and therefore
$$
\begin{aligned}
\operatorname{Res}_{z=z_0}h(z)
&=\frac{z_0^{m-1}}{n z_0^{n-1}}\\
&=\frac{z_0^{m-n}}n
=-\frac{z_0^m}{n}
=-\frac1n e^{i\pi m/n}.
\end{aligned}
$$
:::

<1>4. The value of the integral is
$$
I=\boxed{\frac{\pi}{n}\csc\left(\frac{\pi m}{n}\right)}.
$$

::: {.proof}
By the residue theorem and step <1>3,
$$
\int_{\Gamma_R}h(z)\,dz
=-\frac{2\pi i}{n}e^{i\pi m/n}
$$
for all sufficiently large $R$. Letting $R\to\infty$ in step <1>2 and using step <1>1 yields
$$
\left(1-e^{2i\theta}\right)I
=-\frac{2\pi i}{n}e^{i\theta}.
$$
Since
$$
1-e^{2i\theta}=-2i e^{i\theta}\sin\theta,
$$
and $0<\theta<\pi$, division gives
$$
I=\frac{\pi}{n\sin\theta}
=\frac{\pi}{n}\csc\left(\frac{\pi m}{n}\right).
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
