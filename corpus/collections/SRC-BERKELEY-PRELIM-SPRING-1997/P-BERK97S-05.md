---
schema: qual/card@1
id: P-BERK97S-05
kind: problem
title: A vertically shifted Gaussian integral is independent of the shift
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Prove that
\[
\int_{-\infty}^{\infty}
\frac{e^{-(t-i\gamma)^2/2}}{\sqrt{2\pi}}\,dt
\]
is independent of the real parameter $\gamma$.
:::

::: {.solution}
For $\gamma\in\RR$, define
$$
I(\gamma)
\coloneqq
\frac1{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
e^{-(t-i\gamma)^2/2}\,dt.
$$

::: pf

::: {.pf-step #s1}

The integral defining $I(\gamma)$ converges absolutely for every
$\gamma\in\RR$.

::: pf-proof

For real $t$ and $\gamma$,
$$
\abs{e^{-(t-i\gamma)^2/2}}
=
e^{-(t^2-\gamma^2)/2}
=
e^{\gamma^2/2}e^{-t^2/2}.
$$
The Gaussian on the right is integrable over $\RR$.

:::

:::

::: {.pf-step #s2}

The function $I$ is differentiable and
$$
I'(\gamma)
=
\frac{i}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
(t-i\gamma)e^{-(t-i\gamma)^2/2}\,dt.
$$

::: pf-proof

Fix $R>0$ and restrict temporarily to $\abs{\gamma}\leq R$. The derivative
of the integrand with respect to $\gamma$ is
$$
i(t-i\gamma)e^{-(t-i\gamma)^2/2}.
$$
Its modulus is at most
$$
(\abs{t}+R)e^{R^2/2}e^{-t^2/2},
$$
which is integrable over $\RR$. Differentiation under the integral sign is
therefore justified on $[-R,R]$. Since $R$ is arbitrary, the displayed
formula holds for every real $\gamma$.

:::

:::

::: {.pf-step #s3}

For every $\gamma\in\RR$,
$$
I'(\gamma)=0.
$$

::: pf-proof

For fixed $\gamma$,
$$
\frac{d}{dt}
e^{-(t-i\gamma)^2/2}
=
-(t-i\gamma)e^{-(t-i\gamma)^2/2}.
$$
Hence step [](#s2){.pf-ref} gives
$$
I'(\gamma)
=
-\frac{i}{\sqrt{2\pi}}
\left[
e^{-(t-i\gamma)^2/2}
\right]_{t=-\infty}^{t=\infty}.
$$
By the modulus identity in step [](#s1){.pf-ref}, the boundary values tend to zero as
$t\to\pm\infty$. Thus $I'(\gamma)=0$.

:::

:::

::: {.pf-step #s4}

The integral is independent of $\gamma$.

::: pf-proof

Step [](#s3){.pf-ref} shows that the differentiable function
$$
I:\RR\longrightarrow\CC
$$
has derivative zero everywhere. Hence $I$ is constant on the connected
interval $\RR$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is exactly the required conclusion.

:::

:::

:::
