---
schema: qual/card@1
id: E-SS2.EX-12
kind: problem
title: Harmonic conjugates and Poisson representation on the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
12. Let u be a real-valued function defined on the unit disc D. Suppose that $u$ is twice continuously diferentiable and harmonic, that is,

$$
\triangle u (x, y) = 0
$$

for all $( x , y ) \in \mathbb { D }$

(a) Prove that there exists a holomorphic function f on the unit disc such that

$$
\operatorname{Re} (f) = u.
$$

Also show that the imaginary part of f is uniquely defined up to an additive (real) constant.
[Hint: From the previous chapter we would have $f ^ { \prime } ( z ) =$ $2 \partial u / \partial z$ . Therefore, let $g ( z ) = 2 \partial u / \partial z$ and prove that $g$ is holomorphic. Why can one find $F$ with $F ^ { \prime } = g \ ?$ Prove that $\mathrm { R e } ( F )$ difers from u by a real constant.]

(b) Deduce from this result, and from Exercise 11, the Poisson integral representation formula from the Cauchy integral formula: If u is harmonic in the unit disc and continuous on its closure, then if $z = r e ^ { i \theta }$ one has

$$
u (z) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} P _ {r} (\theta - \varphi) u (\varphi) d \varphi
$$

where $P _ { r } ( \gamma )$ is the Poisson kernel for the unit disc given by

$$
P _ {r} (\gamma) = \frac {1 - r ^ {2}}{1 - 2 r \cos \gamma + r ^ {2}}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) There is a holomorphic $f$ on $\mathbb D$ with $\Re f = u$, and $\Im f$ is unique up to an additive real constant.

::: pf-proof

::: pf-step

$g = 2\frac{\partial u}{\partial z} = u_x - i u_y$ is holomorphic on $\mathbb D$.

::: pf-proof

Since $u$ is $C^2$, $g$ is $C^1$ and $\frac{\partial g}{\partial \bar z} = 2\frac{\partial^2 u}{\partial \bar z \partial z} = \frac{1}{2}\Delta u = 0$.

:::

:::

::: {.pf-step #s1-2}

There is a holomorphic $f$ on $\mathbb D$ with $\Re f = u$.

::: pf-proof

A holomorphic function on a disc has a primitive, so there is $F$ with $F' = g$. Then $\partial_x\Re F = \Re F' = \Re g = u_x$ and $\partial_y\Re F = \Re(iF') = \Re(ig) = u_y$, so $\Re F - u$ has zero gradient on the connected set $\mathbb D$ and equals a real constant $c$. Put $f = F - c$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives existence. If $\Re f_1 = \Re f_2 = u$, then $f_1 - f_2$ is holomorphic with zero real part, hence constant by [[E-SS1.EX-13]], so $f_1 - f_2 = ic$ with $c$ real.

:::

:::

:::

::: pf-step

(b) If $u$ is harmonic in $\mathbb D$ and continuous on $\overline{\mathbb D}$, then for $z=re^{i\theta}$, $0\le r<1$, $u(z) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \varphi) u(e^{i\varphi})\, d\varphi$.

::: pf-proof

::: {.pf-step #s2-1}

For $r<\rho<1$, $u(re^{i\theta}) = \frac{1}{2\pi}\int_0^{2\pi} \frac{\rho^2-r^2}{\rho^2-2\rho r\cos(\theta-\varphi)+r^2}\, u(\rho e^{i\varphi})\, d\varphi$.

::: pf-proof

By step [](#s1){.pf-ref}, $u = \Re f$ with $f$ holomorphic on $\mathbb D$. Part (a) of [[E-SS2.EX-11]] with $R=\rho$ expresses $f(z)$ as the integral of $f(\rho e^{i\varphi})$ against the real kernel $\Re\frac{\rho e^{i\varphi}+z}{\rho e^{i\varphi}-z}$; taking real parts gives the same formula for $u$, and part (b) of [[E-SS2.EX-11]] evaluates the kernel.

:::

:::

::: pf-qed

Fix $z=re^{i\theta}$ and let $\rho\to1^-$ in step [](#s2-1){.pf-ref}. Since $u$ is uniformly continuous on $\overline{\mathbb D}$, $u(\rho e^{i\varphi})\to u(e^{i\varphi})$ uniformly in $\varphi$, and the kernels converge uniformly in $\varphi$ to $P_r(\theta-\varphi)$ because $\rho^2-2\rho r\cos\gamma+r^2\ge(\rho-r)^2$ stays bounded away from $0$. Hence the integrals converge to $\frac{1}{2\pi}\int_0^{2\pi}P_r(\theta-\varphi)u(e^{i\varphi})\,d\varphi$.

:::

:::

:::

:::

:::
