---
schema: qual/card@1
id: P-BKS17-1A
kind: problem
title: $\int_{-\infty}^\infty\sin x/x\,dx=\int_{-\infty}^\infty\sin^2x/x^2\,dx$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 2 problem 1A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 integration-by-parts solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified absolute convergence of the squared-sinc integral, the finite-interval substitution and integration by parts, and the two independent improper limits.
---

::: {.problem}
Show that the following improper Riemann integrals exist and are equal:

$$
\int_{-\infty}^{\infty} \frac{\sin(x)}{x} \, dx = \int_{-\infty}^{\infty} \frac{\sin^2(x)}{x^2} \, dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The improper integral
$$
J\coloneqq\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx
$$
exists absolutely.


::: pf-proof

Near $0$,
$$
\frac{\sin^2x}{x^2}\longrightarrow1,
$$
so the apparent singularity is removable and the integrand is bounded on a neighborhood of $0$. For $\abs{x}\geq1$,
$$
0\leq\frac{\sin^2x}{x^2}\leq\frac1{x^2},
$$
and $1/x^2$ is integrable on both tails. Hence the integral exists absolutely.

:::

:::

::: {.pf-step #s1-2}

For every $L,R>0$,
$$
\int_{-2L}^{2R}\frac{\sin x}{x}\,dx
=
\left[\frac{\sin^2t}{t}\right]_{-L}^{R}
+
\int_{-L}^{R}\frac{\sin^2t}{t^2}\,dt.
$$


::: pf-proof

With the substitution $x=2t$,
$$
\int_{-2L}^{2R}\frac{\sin x}{x}\,dx
=
\int_{-L}^{R}\frac{\sin(2t)}{t}\,dt
=
\int_{-L}^{R}\frac{2\sin t\cos t}{t}\,dt.
$$
Since
$$
\frac{d}{dt}\sin^2t=2\sin t\cos t,
$$
integration by parts gives
$$
\int_{-L}^{R}\frac{2\sin t\cos t}{t}\,dt
=
\left[\frac{\sin^2t}{t}\right]_{-L}^{R}
+
\int_{-L}^{R}\frac{\sin^2t}{t^2}\,dt.
$$
To justify the integration by parts across $t=0$, split the integral at $\pm\varepsilon$ and let $\varepsilon\downarrow0$; the boundary terms $\sin^2(\pm\varepsilon)/(\pm\varepsilon)$ tend to $0$.

:::

:::

::: {.pf-step #s1-3}

Both improper integrals in the problem exist and
$$
\boxed{
\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx
=
\int_{-\infty}^{\infty}\frac{\sin^2x}{x^2}\,dx
}.
$$


::: pf-proof

Let $L,R\to\infty$ independently in step [](#s1-2){.pf-ref}. Since $\abs{\sin t}\leq1$,
$$
\frac{\sin^2R}{R}\longrightarrow0,
\qquad
\frac{\sin^2(-L)}{-L}\longrightarrow0.
$$
By step [](#s1-1){.pf-ref},
$$
\int_{-L}^{R}\frac{\sin^2t}{t^2}\,dt\longrightarrow J.
$$
Therefore the left side of the identity in step [](#s1-2){.pf-ref} has a limit as $L,R\to\infty$, which proves existence of the improper integral of $\sin x/x$, and that limit equals $J$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves both existence and equality.

:::

:::

:::
