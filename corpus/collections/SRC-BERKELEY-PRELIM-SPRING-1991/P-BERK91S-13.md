---
schema: qual/card@1
id: P-BERK91S-13
kind: problem
title: Evaluate $\lim_{R\to\infty}\int_{-R}^R\sin x/(x-3i)\,dx$
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
  date: 2026-09-23
  note: Compared the symmetric truncation, sine numerator, and denominator with Problem 13 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Prove that
$$
\lim_{R\to\infty}\int_{-R}^{R}\frac{\sin x}{x-3i}\,dx
$$
exists, and find its value.
:::

::: {.solution}
Define $g,f:\CC\setminus\{3i,-3i\}\to\CC$ by
$$
g(z)\coloneqq\frac{z}{z^2+9},
\qquad
f(z)\coloneqq e^{iz}g(z).
$$
For $R>3$, put
$$
I_R\coloneqq\int_{-R}^{R}\frac{\sin x}{x-3i}\,dx,
\qquad
J_R\coloneqq\int_{-R}^{R}f(x)\,dx,
$$
and let $C_R$ be the upper semicircle parametrized by
$z=Re^{i\theta}$ for $0\le\theta\le\pi$, oriented from $R$ to $-R$.

<1>1. For every $R>3$, $I_R=\operatorname{Im}J_R$.

::: {.proof}
Rationalizing the denominator gives
$$
\frac{\sin x}{x-3i}
=\frac{x\sin x}{x^2+9}+3i\frac{\sin x}{x^2+9}.
$$
The second term is odd, so its integral over $[-R,R]$ vanishes.
Since $\operatorname{Im}f(x)=x\sin x/(x^2+9)$ for real $x$,
$$
I_R=\int_{-R}^{R}\frac{x\sin x}{x^2+9}\,dx
=\operatorname{Im}J_R.
$$
:::

<1>2. The integral of $f$ over $C_R$ tends to zero as $R\to\infty$.

::: {.proof}
For $z\in C_R$, the reverse triangle inequality gives
$$
\abs{g(z)}\le\frac{R}{R^2-9}.
$$
Applying [[T-ZO5UU|Jordan's lemma]] with exponent $\alpha=1$ yields
$$
\abs{\int_{C_R}f(z)\,dz}
\le\frac{\pi R}{R^2-9}\longrightarrow0.
$$
:::

<1>3. The limit of $J_R$ is $\pi i e^{-3}$.

::: {.proof}
The real segment from $-R$ to $R$, followed by $C_R$, is the
positively oriented boundary of the upper half-disk. The only
[[D-AUD6K|pole]] of $f$ inside it is the
[[D-AUD6K|simple pole]] at $3i$, whose residue is
$$
\Res_{z=3i}f
=\lim_{z\to3i}\frac{ze^{iz}}{z+3i}
=\frac{e^{-3}}2.
$$
The [[T-HRPNO|residue theorem]] therefore gives
$$
J_R+\int_{C_R}f(z)\,dz=\pi i e^{-3}.
$$
Step <1>2 proves the claimed limit.
:::

<1>4. The requested limit is $\boxed{\pi e^{-3}}$.

::: {.proof}
By steps <1>1 and <1>3 and continuity of the imaginary-part map,
$$
\lim_{R\to\infty}I_R
=\operatorname{Im}\left(\lim_{R\to\infty}J_R\right)
=\operatorname{Im}(\pi i e^{-3})
=\pi e^{-3}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves existence and evaluates the symmetric improper integral.
:::
:::
