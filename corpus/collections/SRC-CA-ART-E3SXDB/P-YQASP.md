---
schema: qual/card@1
id: P-YQASP
kind: problem
title: $\lim_{x\to+\infty}\int_{\gamma_x}f=iAb$ when $f(x+iy)\to A$ independently
  of $y$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Limits
relations: []
review: draft
---

::: {.problem}
Assume $f$ is continuous in the region $\theset{x+iy \suchthat x\geq x_0, ~ 0\leq y \leq b}$, and the following limit exists independent of $y$:
\[
\lim_{x\to +\infty}f(x+iy) = A
.\]

Show that if $\gamma_x \definedas \theset{z = x+it \suchthat 0 \leq t \leq b}$, then
\[
\lim_{x\to +\infty} \int_{\gamma_x} f(z) \,dz = iAb
.\]
:::

::: {.solution}
The convergence $f(x+iy)\to A$ "independent of $y$" means uniform convergence in $y\in[0,b]$:
$$\sup_{0\le y\le b}\abs{f(x+iy)-A}\longrightarrow0\qquad(x\to+\infty).$$
Parametrize $\gamma_x$ by $z=x+it$, $0\le t\le b$, so $dz=i\,dt$ and $\length(\gamma_x)=b$.

<1>1. $\displaystyle\int_{\gamma_x} A \,dz = iAb$ for every $x\ge x_0$.

::: {.proof}
$\int_{\gamma_x} A\,dz = \int_0^b A\, i\,dt = iAb$.
:::

<1>2. For every $x\ge x_0$,
$$\abs{\int_{\gamma_x} f(z)\,dz - iAb} \le b\sup_{0\le y\le b}\abs{f(x+iy)-A}.$$

::: {.proof}
By step <1>1,
$$\abs{\int_{\gamma_x} f(z) \,dz - iAb} = \abs{\int_{\gamma_x} \bigl(f(z) - A\bigr) \,dz} \le \length(\gamma_x)\sup_{z\in\gamma_x}\abs{f(z)-A}.$$
The supremum is finite because $f$ is continuous on the compact segment $\gamma_x$.
:::

<1>3. Q.E.D.

::: {.proof}
By uniform convergence, the right-hand side of step <1>2 tends to $0$ as $x\to+\infty$, so $\lim_{x\to +\infty} \int_{\gamma_x} f(z) \,dz = \boxed{iAb}$.
:::
:::
