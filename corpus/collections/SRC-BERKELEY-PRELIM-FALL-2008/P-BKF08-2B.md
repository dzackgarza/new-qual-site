---
schema: qual/card@1
id: P-BKF08-2B
kind: problem
title: Evaluation of $\int_0^\infty dx/(1+x^\alpha)$ for $\alpha>1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the logarithm branch for arbitrary real alpha>1, the unique
    pole in the sector, both arc estimates, the ray orientations, and the
    residue calculation.
---

::: {.problem}
Evaluate
$$
\int_0^{\infty}\frac{dx}{1+x^{\alpha}}
$$
for $\alpha>1$.
:::

::: {.solution}
Put
$$
\theta\coloneqq\frac{2\pi}{\alpha}.
$$
Since $0<\theta<2\pi$, choose $\delta>0$ with
$\theta+2\delta<2\pi$. On the sector
$$
S_\delta
=\{re^{i\varphi}:r>0,\ -\delta<\varphi<\theta+\delta\},
$$
choose the holomorphic logarithm whose imaginary part lies in
$(-\delta,\theta+\delta)$, and define
$z^\alpha\coloneqq\exp(\alpha\log z)$ there. In particular, this
definition is holomorphic on a neighborhood of the closed sector between
the rays of arguments $0$ and $\theta$, away from the origin.

<1>1. The function
$$
F(z)\coloneqq\frac1{1+z^\alpha}
$$
has exactly one pole in the sector $0<\arg z<\theta$, namely
$$
z_0=e^{\pi i/\alpha},
$$
and
$$
\operatorname{Res}_{z=z_0}F(z)=-\frac{e^{\pi i/\alpha}}{\alpha}.
$$

::: {.proof}
For $z=re^{i\varphi}$ with $0<\varphi<\theta=2\pi/\alpha$, the equation
$z^\alpha=-1$ forces
$$
r^\alpha=1,
\qquad
\alpha\varphi=\pi,
$$
because $0<\alpha\varphi<2\pi$. Hence $r=1$ and
$\varphi=\pi/\alpha$, proving uniqueness of $z_0$.

The zero of $1+z^\alpha$ at $z_0$ is simple, since its derivative is
$\alpha z^{\alpha-1}$ and $z_0\ne0$. Therefore
$$
\begin{aligned}
\operatorname{Res}_{z=z_0}F(z)
&=\frac1{\alpha z_0^{\alpha-1}}\\
&=\frac{z_0}{\alpha z_0^\alpha}\\
&=-\frac{z_0}{\alpha}
=-\frac{e^{\pi i/\alpha}}{\alpha}.
\end{aligned}
$$
:::

<1>2. Let $C_{\varepsilon,R}$ be the positively oriented boundary of
$$
\{re^{i\varphi}:\varepsilon<r<R,\ 0<\varphi<\theta\},
$$
where $0<\varepsilon<1<R$. Then
$$
\int_{C_{\varepsilon,R}}F(z)\,dz
=-\frac{2\pi i}{\alpha}e^{\pi i/\alpha}.
$$

::: {.proof}
By step <1>1, $z_0$ is the unique pole enclosed by the contour. The
residue theorem gives
$$
\int_{C_{\varepsilon,R}}F(z)\,dz
=2\pi i\operatorname{Res}_{z=z_0}F(z)
=-\frac{2\pi i}{\alpha}e^{\pi i/\alpha}.
$$
:::

<1>3. The two radial sides of $C_{\varepsilon,R}$ contribute
$$
\left(1-e^{2\pi i/\alpha}\right)
\int_{\varepsilon}^{R}\frac{dr}{1+r^\alpha}.
$$

::: {.proof}
On the lower ray $z=r$, so its contribution is
$$
\int_{\varepsilon}^{R}\frac{dr}{1+r^\alpha}.
$$
On the upper ray, parametrized in the contour direction by
$z=re^{i\theta}$ with $r$ decreasing from $R$ to $\varepsilon$, one has
$$
z^\alpha=r^\alpha e^{i\alpha\theta}=r^\alpha
$$
and $dz=e^{i\theta}dr$. Hence the upper-ray contribution is
$$
-e^{i\theta}\int_{\varepsilon}^{R}\frac{dr}{1+r^\alpha}.
$$
Since $\theta=2\pi/\alpha$, adding the two contributions proves the
claim.
:::

<1>4. The circular-arc contributions tend to $0$ as
$\varepsilon\to0$ and $R\to\infty$.

::: {.proof}
On the inner arc, for sufficiently small $\varepsilon$,
$$
\abs{1+z^\alpha}\ge1-\varepsilon^\alpha,
$$
while the arc length is $\theta\varepsilon$. Thus its integral has
absolute value at most
$$
\frac{\theta\varepsilon}{1-\varepsilon^\alpha}\longrightarrow0.
$$

On the outer arc,
$$
\abs{1+z^\alpha}\ge R^\alpha-1,
$$
and the arc length is $\theta R$. Hence its integral has absolute value
at most
$$
\frac{\theta R}{R^\alpha-1}\longrightarrow0,
$$
because $\alpha>1$.
:::

<1>5. If
$$
I\coloneqq\int_0^\infty\frac{dx}{1+x^\alpha},
$$
then
$$
\left(1-e^{2\pi i/\alpha}\right)I
=-\frac{2\pi i}{\alpha}e^{\pi i/\alpha}.
$$

::: {.proof}
Combine steps <1>2 and <1>3, then let
$\varepsilon\to0$ and $R\to\infty$. Step <1>4 removes the two arc
integrals. The improper integral $I$ converges because the integrand is
bounded near $0$ and is $O(x^{-\alpha})$ at infinity with $\alpha>1$.
:::

<1>6. The value of the integral is
$$
\boxed{
\int_0^\infty\frac{dx}{1+x^\alpha}
=\frac{\pi}{\alpha\sin(\pi/\alpha)}
}.
$$

::: {.proof}
Using
$$
1-e^{2\pi i/\alpha}
=-2i e^{\pi i/\alpha}\sin\left(\frac{\pi}{\alpha}\right),
$$
step <1>5 becomes
$$
-2i e^{\pi i/\alpha}\sin\left(\frac{\pi}{\alpha}\right)I
=-\frac{2\pi i}{\alpha}e^{\pi i/\alpha}.
$$
Canceling the nonzero common factors yields the displayed formula.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the requested evaluation.
:::
:::
