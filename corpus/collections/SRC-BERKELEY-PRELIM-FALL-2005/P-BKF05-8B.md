---
schema: qual/card@1
id: P-BKF05-8B
kind: problem
title: The integral of $e^{iz}/z$ over a large upper semicircle tends to zero
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained semicircle parametrization and decay
    estimate. The proof below replaces the source's bounded-convergence step
    by the explicit bound |I_R|<=pi/R using the chord estimate for sine.
---

::: {.problem}
For \(R>0\), let
\[
\Gamma_R=\{z\in\mathbb C:|z|=R,\ \operatorname{Im}z\ge0\}
\]
be the upper semicircle, oriented counterclockwise.
Prove that
\[
\lim_{R\to\infty}\int_{\Gamma_R}\frac{e^{iz}}{z}\,dz=0.
\]
:::

::: {.solution}
For $R>0$, write
$$
I_R=\int_{\Gamma_R}\frac{e^{iz}}{z}\,dz.
$$

<1>1. The counterclockwise parametrization
$$
z=Re^{i\theta},
\qquad
0\le\theta\le\pi,
$$
gives
$$
I_R
=
i\int_0^\pi e^{iR\cos\theta-R\sin\theta}\,d\theta.
$$

::: {.proof}
For this parametrization,
$$
dz=iRe^{i\theta}\,d\theta
$$
and $z=Re^{i\theta}$. Therefore
$$
\begin{aligned}
I_R
&=
\int_0^\pi
\frac{e^{iRe^{i\theta}}}{Re^{i\theta}}
iRe^{i\theta}\,d\theta
\\
&=
i\int_0^\pi
e^{iR(\cos\theta+i\sin\theta)}\,d\theta
\\
&=
i\int_0^\pi
e^{iR\cos\theta-R\sin\theta}\,d\theta.
\end{aligned}
$$
:::

<1>2. For every $R>0$,
$$
\abs{I_R}
\le
\int_0^\pi e^{-R\sin\theta}\,d\theta.
$$

::: {.proof}
By step <1>1 and the triangle inequality,
$$
\abs{I_R}
\le
\int_0^\pi
\abs{e^{iR\cos\theta-R\sin\theta}}\,d\theta.
$$
Since
$$
\abs{e^{iR\cos\theta-R\sin\theta}}
=
e^{-R\sin\theta},
$$
the claimed estimate follows.
:::

<1>3. For $0\le\theta\le\pi/2$,
$$
\sin\theta\ge\frac{2\theta}{\pi}.
$$

::: {.proof}
The function $\sin\theta$ is concave on $[0,\pi/2]$, so its graph
lies above the chord joining
$$
(0,0)
\qquad\text{and}\qquad
(\pi/2,1).
$$
That chord has equation $y=2\theta/\pi$.
:::

<1>4. For every $R>0$,
$$
\abs{I_R}\le\frac{\pi}{R}.
$$

::: {.proof}
Using step <1>2 and the symmetry
$\sin(\pi-\theta)=\sin\theta$,
$$
\int_0^\pi e^{-R\sin\theta}\,d\theta
=
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta.
$$
By step <1>3,
$$
\begin{aligned}
2\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
&\le
2\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta
\\
&=
\frac{\pi}{R}(1-e^{-R})
\\
&\le
\frac{\pi}{R}.
\end{aligned}
$$
Combining this with step <1>2 proves the estimate.
:::

<1>5. Therefore
$$
\boxed{\lim_{R\to\infty}I_R=0}.
$$

::: {.proof}
By step <1>4,
$$
0\le\abs{I_R}\le\frac{\pi}{R},
$$
and the right-hand side tends to zero.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required limit.
:::
:::
