---
schema: qual/card@1
id: P-IV4XE
kind: problem
title: $\int_{\RR}\frac{e^{i\xi x}}{\cosh x}\,dx$ for $\xi\in\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
---

::: {.problem}
Let $\xi\in \RR$, evaluate
$$
\int_\RR {e^{i\xi x} \over \cosh(x)} \dx
.$$

:::

::: {.solution}
Let $f(z)=e^{i\xi z}/\cosh z$ and $I=\int_\RR f(x)\,dx$, which converges absolutely because $\abs{f(x)}=1/\cosh x\le 2e^{-\abs{x}}$.
For $R>0$ let $\Gamma_R$ be the positively oriented boundary of the rectangle with vertices $\pm R$ and $\pm R+i\pi$.

::: pf

::: {.pf-step #poles}
The only zero of $\cosh$ inside $\Gamma_R$ is $i\pi/2$, and $2\pi i\Res_{z=i\pi/2}f=2\pi e^{-\pi\xi/2}$.

::: pf-proof
$\cosh z=0$ if and only if $e^{2z}=-1$, that is $z\in i\pi(\tfrac12+\ZZ)$. Only $i\pi/2$ has imaginary part in $(0,\pi)$. The zero is simple because $\cosh'(i\pi/2)=\sinh(i\pi/2)=i\neq0$, so the residue is $e^{i\xi(i\pi/2)}/i=e^{-\pi\xi/2}/i$.
:::

:::

::: {.pf-step #top}
The top edge contributes $e^{-\pi\xi}\int_{-R}^R f(x)\,dx$.

::: pf-proof
$\cosh(x+i\pi)=-\cosh x$ and $e^{i\xi(x+i\pi)}=e^{-\pi\xi}e^{i\xi x}$. The top edge runs from $R+i\pi$ to $-R+i\pi$, so its integral is $-\int_{-R}^R\frac{e^{-\pi\xi}e^{i\xi x}}{-\cosh x}\,dx=e^{-\pi\xi}\int_{-R}^Rf(x)\,dx$.
:::

:::

::: {.pf-step #sides}
The two vertical edges contribute integrals that tend to $0$ as $R\to\infty$.

::: pf-proof
On $z=\pm R+it$ with $0\le t\le\pi$, $\abs{e^{i\xi z}}=e^{-\xi t}\le e^{\pi\abs{\xi}}$ and $\abs{\cosh z}\ge\frac12(e^{R}-e^{-R})$. Each edge has length $\pi$, so each integral is at most $2\pi e^{\pi\abs{\xi}}/(e^R-e^{-R})\to0$.
:::

:::

::: {.pf-step #value}
$$
\boxed{\int_\RR\frac{e^{i\xi x}}{\cosh x}\,dx=\frac{\pi}{\cosh(\pi\xi/2)}}
$$

::: pf-proof
By the residue theorem and steps [](#poles){.pf-ref}, [](#top){.pf-ref} and [](#sides){.pf-ref}, letting $R\to\infty$ gives $(1+e^{-\pi\xi})I=2\pi e^{-\pi\xi/2}$. Hence $I=\dfrac{2\pi}{e^{\pi\xi/2}+e^{-\pi\xi/2}}=\dfrac{\pi}{\cosh(\pi\xi/2)}$.
:::

:::

::: pf-qed
Step [](#value){.pf-ref} is the requested value.
:::

:::

:::
