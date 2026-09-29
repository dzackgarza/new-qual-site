---
schema: qual/card@1
id: P-BERK90S-07
kind: problem
title: The integral $\int_0^\infty \sin x/[x(x^2+a^2)]\,dx$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared Problem 7 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Evaluated the integral by an absolutely integrable cosine transform and an upper-semicircle residue calculation.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked absolute convergence, Fubini's hypotheses, the residue and contour orientation, the arc estimate at t=0, and the final parameter integral.
---

::: {.problem}
Let $a>0$. Evaluate
$$
\int_0^\infty\frac{\sin x}{x(x^2+a^2)}\,dx.
$$
:::

::: {.hint}
For $x>0$, use
$$
\frac{\sin x}{x}=\int_0^1\cos(tx)\,dt.
$$
The bound
$$
\int_0^1\int_0^\infty
\frac{\abs{\cos(tx)}}{x^2+a^2}\,dx\,dt
\leq\int_0^\infty\frac{dx}{x^2+a^2}<\infty
$$
allows the order of integration to be exchanged. For fixed $t\in[0,1]$,
evaluate the resulting cosine integral by integrating
$z\mapsto e^{itz}/(z^2+a^2)$ around an upper semicircle of radius $R>a$.
The exponential has modulus at most $1$ on the arc, whose integral is
bounded in modulus by $\pi R/(R^2-a^2)$.
:::

::: {.solution}
Fix $a>0$, and write
$$
I(a)\coloneqq\int_0^\infty\frac{\sin x}{x(x^2+a^2)}\,dx,
\qquad
C_a(t)\coloneqq\int_0^\infty\frac{\cos(tx)}{x^2+a^2}\,dx
\quad(0\leq t\leq1).
$$

::: pf

::: {.pf-step #s1}

The defining integrals converge absolutely, and
$$
I(a)=\int_0^1 C_a(t)\,dt.
$$

::: pf-proof

For $x>0$, the inequalities $\abs{\sin x}\leq x$ and
$\abs{\cos(tx)}\leq1$ bound the absolute values of both integrands by
$(x^2+a^2)^{-1}$. This bound is integrable on $(0,\infty)$, since
$$
\int_0^\infty\frac{dx}{x^2+a^2}=\frac{\pi}{2a}.
$$
Also,
$$
\int_0^1\cos(tx)\,dt=\frac{\sin x}{x},
\qquad
\int_0^1\int_0^\infty
\frac{\abs{\cos(tx)}}{x^2+a^2}\,dx\,dt
\leq\frac{\pi}{2a}<\infty.
$$
The integrand is continuous on $[0,1]\times(0,\infty)$, so
[[T-X7XZX|Fubini's theorem]] applies with Lebesgue measure and gives
$$
I(a)=\int_0^\infty\int_0^1
\frac{\cos(tx)}{x^2+a^2}\,dt\,dx
=\int_0^1 C_a(t)\,dt.
$$

:::

:::

::: {.pf-step #s2}

For every $t\in[0,1]$,
$$
C_a(t)=\frac{\pi}{2a}e^{-at}.
$$

Fix $t\in[0,1]$, and define
$$
F_t\colon\CC\setminus\{ia,-ia\}\longrightarrow\CC,
\qquad F_t(z)\coloneqq\frac{e^{itz}}{z^2+a^2}.
$$
For $R>a$, let $\Gamma_R$ be the upper semicircle of radius $R$,
oriented from $R$ to $-R$. The segment from $-R$ to $R$ followed by
$\Gamma_R$ is a positively oriented simple closed contour.

::: pf-proof

::: {.pf-step #s2-1}

For every $R>a$,
$$
\int_{-R}^R F_t(x)\,dx+\int_{\Gamma_R}F_t(z)\,dz
=\frac{\pi}{a}e^{-at}.
$$

::: pf-proof

The only pole of $F_t$ inside this contour is the simple pole at $ia$.
The [[T-ESKLY|simple-pole residue formula]] gives
$$
\Res_{z=ia}F_t(z)
=\lim_{z\to ia}\frac{e^{itz}}{z+ia}
=\frac{e^{-at}}{2ia}.
$$
The [[T-HRPNO|residue theorem]] gives the asserted contour integral as
$2\pi i$ times this residue.

:::

:::

::: {.pf-step #s2-2}

The integral of $F_t$ over $\Gamma_R$ tends to zero as
$R\to\infty$.

::: pf-proof

For $z\in\Gamma_R$, one has $\Im z\geq0$ and $\abs{z}=R$, so
$$
\abs{e^{itz}}=e^{-t\Im z}\leq1,
\qquad
\abs{z^2+a^2}\geq R^2-a^2.
$$
The arc has length $\pi R$, and therefore
$$
\abs{\int_{\Gamma_R}F_t(z)\,dz}
\leq\frac{\pi R}{R^2-a^2}\longrightarrow0.
$$
This estimate holds for every $t\in[0,1]$, including $t=0$.

:::

:::

::: pf-qed

The real-line integral converges absolutely because
$\abs{F_t(x)}=(x^2+a^2)^{-1}$. Letting $R\to\infty$ in step [](#s2-1){.pf-ref}
and using step [](#s2-2){.pf-ref} gives
$$
\int_{-\infty}^{\infty}\frac{e^{itx}}{x^2+a^2}\,dx
=\frac{\pi}{a}e^{-at}.
$$
Taking real parts and using the evenness of
$x\mapsto\cos(tx)/(x^2+a^2)$ yields
$2C_a(t)=\pi e^{-at}/a$, proving step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

The requested value is
$$
I(a)=\boxed{\frac{\pi}{2a^2}\bigl(1-e^{-a}\bigr)}.
$$

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
I(a)=\frac{\pi}{2a}\int_0^1e^{-at}\,dt
=\frac{\pi}{2a}\frac{1-e^{-a}}{a}.
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} establishes convergence, and step [](#s3){.pf-ref} evaluates the integral
for every $a>0$.

:::

:::

:::
