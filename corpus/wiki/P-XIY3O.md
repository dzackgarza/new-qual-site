---
schema: qual/card@1
id: P-XIY3O
kind: problem
title: "State and prove Green's Theorem for rectangles."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
State and prove Green's Theorem for rectangles.
Use this to prove Cauchy's Theorem for functions that are analytic in a rectangle.
:::

:::{.problem title="Variant"}
Suppose $f\in C_\CC^1(\Omega)$ and $T\subset \Omega$ is a triangle with $T^\circ \subset \Omega$.

- Apply Green's theorem to show that $\int_T f(z) ~dz = 0$.
- Assume that $f'$ is continuous and prove Goursat's theorem.

> Hint: Green's theorem states
\[
\int_{T} F d x+G d y=\int_{T^\circ}\left(\frac{\partial G}{\partial x}-\frac{\partial F}{\partial y}\right) d x d y
.\]

:::

:::{.solution}
Green's theorem:
if $\Omega$ is a domain with positively oriented boundary with $u, v$ continuously differentiable in $\bar\Omega$, then
\[
\int_{\bd \Omega} u\dx + v\dy = \iint_{\Omega}\qty{v_x - u_y}\dx\dy
.\]
Now use that if $f = u+iv$ is analytic in a region, it satisfies Cauchy-Riemann:
\[
u_x = v_y \qquad u_y = -v_x
.\]

Now integrating $f$:
\[
\oint_{\bd\Omega} f(z) \dz 
&= \oint_{\bd\Omega} (u+iv)(\dx + i\dy )\\
&= \oint_{\bd\Omega} \qty{u\dx - v\dy} + i\oint_{\bd\Omega} \qty{v\dx + u\dy} \\
&= \iint_\Omega\qty{v_x + u_y}\dx\dy + \iint_\Omega\qty{u_x - v_y}\dx\dy \\
&= \iint_\Omega\qty{v_x -v_x }\dx\dy + \iint_\Omega\qty{u_x - u_x}\dx\dy \\
&= 0
.\]
:::

## No polynomials converging uniformly to $1/z$

:::{.problem title="?"}
Prove that there is no sequence of polynomials that uniformly converge to $f(z) = {1\over z}$ on $S^1$.

:::

:::{.solution}

- By Cauchy's integral formula, $\int_{S^1} f = 2\pi i$
- If $p_j$ is any polynomial, then $p_j$ is holomorphic in $\DD$, so $\int_{S^1} p_j = 0$.
- Contradiction: compact sets in $\CC$ are bounded, so 
  \[
  \abs{\int f - \int p_j} 
  &\leq \int \abs{p_j - f} \\
  &\leq \int \norm{p_j - f}_\infty  \\
  &= \norm{p_j - f}_\infty \int_{S^1} 1 \,dz \\
  &= \norm{p_j-f}_\infty \cdot 2\pi \\
  &\to 0
  \]
  which forces $\int f = \int p_j = 0$.
:::
