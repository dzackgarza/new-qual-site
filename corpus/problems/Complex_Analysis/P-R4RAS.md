---
schema: qual/card@1
id: P-R4RAS
kind: problem
title: Continuity, differentiability, and $C^1$ regularity of $\frac{xy}{\sqrt{x^2+y^2}}$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Is the following function continuous, differentiable, continuously differentiable?
$$
\begin{aligned}
f: \RR^2 &\to \RR  \\
f(x, y) &= 
\begin{cases}
{xy \over \sqrt{x^2 + y^2}} & (x, y) \neq (0, 0) \\
0 & \text{else}.
\end{cases}
\end{aligned}
$$
:::

::: {.solution}
Away from $(0,0)$ the function $f$ is smooth, so only the origin needs attention.

::: pf

::: pf-step

$f$ is continuous on $\RR^2$.

::: pf-proof

Since $\abs{xy}\le\frac12(x^2+y^2)$,
$$
\abs{f(x,y)}\le\frac12\sqrt{x^2+y^2}\longrightarrow0=f(0,0).
$$

:::

:::

::: {.pf-step #not-diff}

$f$ is not differentiable at $(0,0)$.

::: pf-proof

$f$ vanishes on both axes, so both partial derivatives at the origin are $0$, and a derivative there would be the zero map. That would require $\abs{f(x,y)}/\sqrt{x^2+y^2}\to0$. Along $y=x\ne0$,
$$
\frac{\abs{f(x,x)}}{\sqrt{2x^2}}=\frac{x^2/(\sqrt2\abs x)}{\sqrt2\abs x}=\frac12.
$$

:::

:::

::: pf-step

$f$ is $\boxed{\text{continuous, differentiable exactly on } \RR^2\setminus\{0\}, \text{ and not } C^1 \text{ on } \RR^2}$.

::: pf-proof

$f$ is smooth away from the origin, and a $C^1$ function is differentiable everywhere, which step [](#not-diff){.pf-ref} rules out.

:::

:::

:::

:::
