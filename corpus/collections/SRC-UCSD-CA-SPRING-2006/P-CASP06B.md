---
schema: qual/card@1
id: P-CASP06B
kind: problem
title: "Subharmonic function growth estimate and Liouville-type theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP06_220_Complex_Analysis_Qual.pdf,
    Problem 2 (20 points), parts a) and b). The card's statement is that problem verbatim,
    including the hypothesis lim u(z)/log|z| = 0 at infinity in part b.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Supplied the Fubini step the prose
    compressed into one chain of inequalities: the r-integral of the disc integral splits into the
    annulus part, where the inner r-integral is log(R_2/|z|), and the disc {|z| < R_1}, where it is
    the positive constant log(R_2/R_1) -- that discarded positive term is exactly where the
    inequality of part (a) comes from, and the card now says so. In part (b) the passage from the
    pointwise hypothesis to M(T) = o(log T) is now its own step, and the gradient estimate is
    attributed to Cauchy's estimates for the analytic function u is the real part of, with the
    growth of sup over the disc of radius R about a fixed point recorded. No retained published
    solution covers this problem, so the argument is the card's own.
---

::: {.problem}
Suppose that $u$ is a $C^2$ subharmonic function on the whole complex plane.

(a) Prove that for any positive $R_1$ and $R_2$ with $R_2 > R_1$, $$\int_0^{2\pi} \left(u(R_2 e^{i\theta}) - u(R_1 e^{i\theta})\right)d\theta \geq \int_{R_1 \leq \abs{z} \leq R_2} \log\left(\frac{R_2}{\abs{z}}\right) \Delta u \, dx\,dy.$$

(b) Show that if $u$ satisfies $\lim_{z \to \infty} \frac{u(z)}{\log\abs{z}} = 0$, then $u$ must be a constant.
:::

::: {.solution}
This is Problem 2 of the UCSD complex-analysis qualifying exam of Spring 2006 (`assets/attachments/SP06_220_Complex_Analysis_Qual.pdf`). No published solution set is transcribed: the argument is the card's own.

::: pf

::: {.pf-step #green}
With $M(r)=\int_{0}^{2\pi}u(re^{i\theta})\,d\theta$ one has $rM'(r)=\int_{\abs{z}\leq r}\Delta u\,dA(z)$ for every $r>0$.

::: pf-proof
In polar coordinates the Laplacian integrates to
$$\int_{\abs{z}\leq r}\Delta u\,dA=\int_{0}^{2\pi}\int_{0}^{r}\left(u_{\rho\rho}+\tfrac1\rho u_{\rho}\right)\rho\,d\rho\,d\theta=\int_{0}^{2\pi}\Big[\rho\,u_{\rho}(\rho e^{i\theta})\Big]_{\rho=0}^{\rho=r}d\theta=r\int_{0}^{2\pi}u_{\rho}(re^{i\theta})\,d\theta,$$
and differentiating under the integral sign gives $M'(r)=\int_{0}^{2\pi}u_{\rho}(re^{i\theta})\,d\theta$; the integrand is continuous on $\theset{\rho>0}$ and $u$ is $C^{2}$, so both steps are legitimate.
:::
:::

::: {.pf-step #parta}
(a) $\int_{0}^{2\pi}(u(R_{2}e^{i\theta})-u(R_{1}e^{i\theta}))\,d\theta\geq\int_{R_{1}\leq\abs{z}\leq R_{2}}\log\frac{R_{2}}{\abs{z}}\,\Delta u\,dA(z)$ for $0<R_{1}<R_{2}$.

::: pf-proof
By step [](#green){.pf-ref},
$$M(R_{2})-M(R_{1})=\int_{R_{1}}^{R_{2}}\frac{1}{r}\left(\int_{\abs{z}\leq r}\Delta u(z)\,dA(z)\right)dr.$$
Fubini applies, since the integrand is continuous on the compact annulus, and $\int_{R_{1}}^{R_{2}}\frac{dr}{r}$ over the $r$ with $r\geq\abs{z}$ equals $\log\frac{R_{2}}{\abs{z}}$ for $\abs{z}\in[R_{1},R_{2}]$ and is $0$ for $\abs{z}>R_{2}$; for $\abs{z}<R_{1}$ the inner integral over $r$ is $\log\frac{R_{2}}{R_{1}}>0$. Hence
$$M(R_{2})-M(R_{1})=\int_{R_{1}\leq\abs{z}\leq R_{2}}\log\frac{R_{2}}{\abs{z}}\,\Delta u\,dA+\log\frac{R_{2}}{R_{1}}\int_{\abs{z}<R_{1}}\Delta u\,dA,$$
and the second term is nonnegative because $u$ is subharmonic, so $\Delta u\geq0$.
:::
:::

::: {.pf-step #annulus}
For $0<R_{1}<R<T$ one has $M(T)-M(R_{1})\geq\log\frac{T}{R}\int_{R_{1}\leq\abs{z}\leq R}\Delta u\,dA$.

::: pf-proof
Part (a) with $R_{2}=T$ bounds $M(T)-M(R_{1})$ below by the integral of $\log\frac{T}{\abs{z}}\Delta u$ over the annulus $R_{1}\leq\abs{z}\leq T$, and that integral is at least the integral over the smaller annulus $R_{1}\leq\abs{z}\leq R$, where $\log\frac{T}{\abs{z}}\geq\log\frac{T}{R}$; the integrand is nonnegative there because $\Delta u\geq0$.
:::
:::

::: {.pf-step #average}
The hypothesis of (b) gives $M(T)=o(\log T)$ as $T\to\infty$.

::: pf-proof
$M(T)=\int_{0}^{2\pi}u(Te^{i\theta})\,d\theta\leq2\pi\sup_{\abs{z}=T}\abs{u(z)}$, and $\lim_{z\to\infty}u(z)/\log\abs{z}=0$ says that for every $\varepsilon>0$ there is $S$ with $\abs{u(z)}\leq\varepsilon\log\abs{z}$ for $\abs{z}>S$. So $\abs{M(T)}\leq2\pi\varepsilon\log T$ for $T>S$, which is the asserted $o(\log T)$.
:::
:::

::: {.pf-step #laplacian}
$\Delta u\equiv0$ on $\CC$.

::: pf-proof
Divide the inequality of step [](#annulus){.pf-ref} by $\log T$ and let $T\to\infty$: the left side tends to $0$, since $M(T)=o(\log T)$ by step [](#average){.pf-ref} and $M(R_{1})$ is fixed. So $\int_{R_{1}\leq\abs{z}\leq R}\Delta u\,dA\leq0$ for all $0<R_{1}<R<1$; the integrand is nonnegative, so the integral is $0$. As $R_{1}<R$ are arbitrary the annuli exhaust $\CC\setminus\{0\}$, and $\Delta u$ is continuous, so $\Delta u\equiv0$.
:::
:::

::: {.pf-step #gradient}
$u$ is constant.

::: pf-proof
$\Delta u\equiv0$ makes $u$ harmonic on the simply connected domain $\CC$, so $u$ is the real part of an entire function and Cauchy's estimates applied to it give, for every $a$ and every $R>0$,
$$\abs{\nabla u(a)}\leq\frac{C}{R}\sup_{\abs{z-a}\leq R}\abs{u(z)}$$
with an absolute constant $C$. For fixed $a$ and large $R$ the disc $\abs{z-a}\leq R$ lies in $\abs{z}\leq R+\abs{a}$, so $\sup_{\abs{z-a}\leq R}\abs{u(z)}=o(\log R)$ by the growth hypothesis; hence $\abs{\nabla u(a)}\leq C\log R/R\to0$ as $R\to\infty$, giving $\nabla u(a)=0$. As $a$ is arbitrary, $\nabla u\equiv0$ on the connected set $\CC$ and $u$ is constant.
:::
:::
:::

:::
