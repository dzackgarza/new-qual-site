---
schema: qual/card@1
id: P-BKS19-4A
kind: problem
title: Evaluation of $\int_{-\infty}^\infty x\sin x/(1+x^2)^2\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 integration-by-parts and residue calculation. The value $\pi/(2e)$ is correct; the solution below supplies the boundary and contour estimates.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified absolute convergence, the integration-by-parts reduction, the residue at $z=i$, and decay of the upper-semicircle contribution.
---

::: {.problem}
Evaluate
$$
I=\int_{-\infty}^{\infty}\frac{x\sin x}{(1+x^2)^2}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integral satisfies
$$
I=\frac12\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx.
$$


::: pf-proof

Both improper integrals are absolutely convergent. Since
$$
\frac{x}{(1+x^2)^2}
=
-\frac12\frac{d}{dx}\left(\frac1{1+x^2}\right),
$$
integration by parts on $[-R,R]$ gives
$$
\int_{-R}^{R}\frac{x\sin x}{(1+x^2)^2}\,dx
=
-\frac12\left[\frac{\sin x}{1+x^2}\right]_{-R}^{R}
+\frac12\int_{-R}^{R}\frac{\cos x}{1+x^2}\,dx.
$$
The boundary term tends to $0$ as $R\to\infty$, which yields the claimed identity.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\int_{-\infty}^{\infty}\frac{e^{ix}}{1+x^2}\,dx=\frac{\pi}{e}.
$$


::: pf-proof

Let
$$
g(z)\coloneqq\frac{e^{iz}}{1+z^2}
$$
and integrate over the positively oriented semicircle consisting of $[-R,R]$ and the upper semicircular arc $\Gamma_R$, with $R>1$. The only pole enclosed is the simple pole at $z=i$, whose residue is
$$
\operatorname{Res}_{z=i}g(z)
=
\frac{e^{ii}}{2i}
=
\frac{e^{-1}}{2i}.
$$
Hence the residue theorem gives
$$
\int_{-R}^{R}\frac{e^{ix}}{1+x^2}\,dx
+\int_{\Gamma_R}g(z)\,dz
=
\frac{\pi}{e}.
$$
On $\Gamma_R$, $\operatorname{Im}z\geq0$, so $\abs{e^{iz}}=e^{-\operatorname{Im}z}\leq1$, while
$$
\abs{1+z^2}\geq R^2-1.
$$
Since $\Gamma_R$ has length $\pi R$,
$$
\abs{\int_{\Gamma_R}g(z)\,dz}
\leq
\frac{\pi R}{R^2-1}
\longrightarrow0.
$$
Letting $R\to\infty$ proves the displayed integral.

:::

:::

::: {.pf-step #s1-3}

The cosine integral is
$$
\int_{-\infty}^{\infty}\frac{\cos x}{1+x^2}\,dx=\frac{\pi}{e}.
$$


::: pf-proof

Take real parts in step [](#s1-2){.pf-ref}. The integral is absolutely convergent, so taking the real part commutes with integration.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{I=\frac{\pi}{2e}}.
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into the reduction from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value.

:::

:::

:::
