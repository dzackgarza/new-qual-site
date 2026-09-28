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

<1>1. The integral defining $I(\gamma)$ converges absolutely for every
$\gamma\in\RR$.

::: {.proof}
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

<1>2. The function $I$ is differentiable and
$$
I'(\gamma)
=
\frac{i}{\sqrt{2\pi}}
\int_{-\infty}^{\infty}
(t-i\gamma)e^{-(t-i\gamma)^2/2}\,dt.
$$

::: {.proof}
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

<1>3. For every $\gamma\in\RR$,
$$
I'(\gamma)=0.
$$

::: {.proof}
For fixed $\gamma$,
$$
\frac{d}{dt}
e^{-(t-i\gamma)^2/2}
=
-(t-i\gamma)e^{-(t-i\gamma)^2/2}.
$$
Hence step <1>2 gives
$$
I'(\gamma)
=
-\frac{i}{\sqrt{2\pi}}
\left[
e^{-(t-i\gamma)^2/2}
\right]_{t=-\infty}^{t=\infty}.
$$
By the modulus identity in step <1>1, the boundary values tend to zero as
$t\to\pm\infty$. Thus $I'(\gamma)=0$.
:::

<1>4. The integral is independent of $\gamma$.

::: {.proof}
Step <1>3 shows that the differentiable function
$$
I:\RR\longrightarrow\CC
$$
has derivative zero everywhere. Hence $I$ is constant on the connected
interval $\RR$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is exactly the required conclusion.
:::
:::
