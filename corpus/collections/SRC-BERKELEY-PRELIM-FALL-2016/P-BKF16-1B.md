---
schema: qual/card@1
id: P-BKF16-1B
kind: problem
title: The Gaussian integral and surface areas of spheres via $\Gamma$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F16_Exam.pdf problem 1B, which prints S_3 = 4 pi/3; kept with an erratum remark.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: rectangular
    and polar integration give the gamma formula, and the recurrence yields
    the stated Gaussian integral and S_4.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the polar Jacobian, the t=r^2 substitution, the gamma
    integration-by-parts boundary terms, and the evaluations C=sqrt(pi) and
    S_4=2 pi^2.
---

::: {.problem}
Let $C = \int_{-\infty}^{\infty} e^{-x^2}\,dx$ and let $S_n$ be the $(n-1)$-dimensional "surface area" of the unit sphere in $\mathbb{R}^n$ (so $S_2 = 2\pi$, $S_3 = 4\pi/3$).

(a) Prove that $C^n = S_n \Gamma(n/2)/2$, where $\Gamma(s) = \int_0^\infty e^{-t} t^{s-1}\,dt$.
(Evaluate the integral of $e^{-(x_1^2 + \cdots + x_n^2)}$ over $\mathbb{R}^n$ in rectangular and polar coordinates.)

(b) Show that $s\Gamma(s) = \Gamma(s+1)$ and $\Gamma(1) = 1$.

(c) Evaluate $C$.
(Hint: $S_2 = 2\pi$.)

(d) Evaluate $S_4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

In rectangular coordinates,
$$
\int_{\RR^n}
e^{-(x_1^2+\cdots+x_n^2)}
\,dx_1\cdots dx_n
=
C^n.
$$

::: pf-proof

The integrand factors as
$$
\prod_{j=1}^n e^{-x_j^2}
$$
and is nonnegative. By Tonelli's theorem,
$$
\begin{aligned}
\int_{\RR^n}
e^{-(x_1^2+\cdots+x_n^2)}
\,dx_1\cdots dx_n
&=
\prod_{j=1}^n
\int_{-\infty}^{\infty}e^{-x_j^2}\,dx_j\\
&=
C^n.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

In polar coordinates, the same integral equals
$$
S_n
\int_0^\infty
e^{-r^2}r^{n-1}\,dr.
$$

::: pf-proof

The integrand depends only on the Euclidean radius
$$
r=\sqrt{x_1^2+\cdots+x_n^2}.
$$
The polar-coordinate volume element is
$$
r^{n-1}\,dr\,d\omega,
$$
and integration of $d\omega$ over the unit sphere gives its surface
area $S_n$.

:::

:::

::: {.pf-step #s3}

One has
$$
\int_0^\infty
e^{-r^2}r^{n-1}\,dr
=
\frac12\Gamma\left(\frac n2\right).
$$

::: pf-proof

Set
$$
t=r^2.
$$
Then
$$
dt=2r\,dr
$$
and
$$
r^{n-1}\,dr
=
\frac12
t^{n/2-1}\,dt.
$$
Therefore
$$
\begin{aligned}
\int_0^\infty
e^{-r^2}r^{n-1}\,dr
&=
\frac12
\int_0^\infty
e^{-t}t^{n/2-1}\,dt\\
&=
\frac12\Gamma\left(\frac n2\right).
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

Hence
$$
\boxed{
C^n
=
\frac{S_n}{2}
\Gamma\left(\frac n2\right).
}
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} compute the same integral, and step [](#s3){.pf-ref} evaluates
the radial factor. Equating the two expressions proves part (a).

:::

:::

::: {.pf-step #s5}

One has
$$
\boxed{\Gamma(1)=1}.
$$

::: pf-proof

Directly from the definition,
$$
\Gamma(1)
=
\int_0^\infty e^{-t}\,dt
=
\left[-e^{-t}\right]_0^\infty
=
1.
$$

:::

:::

::: {.pf-step #s6}

For every $s>0$,
$$
\boxed{\Gamma(s+1)=s\Gamma(s)}.
$$

::: pf-proof

Integrating by parts,
$$
\begin{aligned}
\Gamma(s+1)
&=
\int_0^\infty e^{-t}t^s\,dt\\
&=
\left[-e^{-t}t^s\right]_0^\infty
+
s\int_0^\infty e^{-t}t^{s-1}\,dt.
\end{aligned}
$$
For $s>0$, the boundary term vanishes: $t^s\to0$ as $t\downarrow0$,
and $e^{-t}t^s\to0$ as $t\to\infty$. Thus
$$
\Gamma(s+1)=s\Gamma(s).
$$
Together with step [](#s5){.pf-ref} this proves part (b).

:::

:::

::: {.pf-step #s7}

The Gaussian integral is
$$
\boxed{C=\sqrt\pi}.
$$

::: pf-proof

Set $n=2$ in step [](#s4){.pf-ref}. Using
$$
S_2=2\pi
$$
and step [](#s5){.pf-ref},
$$
C^2
=
\frac{2\pi}{2}\Gamma(1)
=
\pi.
$$
Since the integrand defining $C$ is positive, $C>0$, so
$$
C=\sqrt\pi.
$$
This proves part (c).

:::

:::

::: {.pf-step #s8}

The surface area of the unit $3$-sphere in $\RR^4$ is
$$
\boxed{S_4=2\pi^2}.
$$

::: pf-proof

Set $n=4$ in step [](#s4){.pf-ref}. By steps [](#s5){.pf-ref} and [](#s6){.pf-ref},
$$
\Gamma(2)=1\cdot\Gamma(1)=1.
$$
By step [](#s7){.pf-ref},
$$
C^4=\pi^2.
$$
Thus
$$
\pi^2
=
\frac{S_4}{2},
$$
so
$$
S_4=2\pi^2.
$$
This proves part (d).

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove parts (a)--(d),
respectively.

:::

:::

:::

::: {.remark}
The source's parenthetical value $S_3 = 4\pi/3$ is an erratum: the surface area of the unit sphere in $\mathbb{R}^3$ is $S_3 = 4\pi$, and $4\pi/3$ is the volume of the unit ball.
The formula in (a) gives $S_3 = 2C^3/\Gamma(3/2) = 2\pi^{3/2}/(\sqrt{\pi}/2) = 4\pi$.
:::
