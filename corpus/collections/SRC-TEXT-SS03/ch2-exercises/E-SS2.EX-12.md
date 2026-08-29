---
schema: qual/card@1
id: E-SS2.EX-12
kind: exercise
title: "Let u be a real-valued function defined on the unit disc D"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: exercise
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
**Part (a).**

<1>1. Define $g(z) = 2\frac{\partial u}{\partial z} = u_x - i u_y$.
Proof: $\frac{\partial u}{\partial z} = \frac{1}{2}(u_x - i u_y)$.

<1>2. $g$ is holomorphic.
Proof: $\frac{\partial g}{\partial \bar z} = 2\frac{\partial^2 u}{\partial \bar z \partial z} = \frac{1}{2}\Delta u = 0$ (since $u$ is harmonic), so $g$ satisfies the Cauchy–Riemann equations.

<1>3. Since $\DD$ is simply connected, $g$ has a primitive $F$ with $F' = g$.
Proof: a holomorphic function on a simply connected domain has a primitive.

<1>4. $\operatorname{Re} F$ differs from $u$ by a real constant.
Proof: $\frac{\partial}{\partial x}\operatorname{Re} F = \operatorname{Re} F' = \operatorname{Re} g = u_x$, and $\frac{\partial}{\partial y}\operatorname{Re} F = \operatorname{Re}(iF') = \operatorname{Re}(ig) = u_y$; hence $\operatorname{Re} F$ and $u$ have the same gradient, so they differ by a constant.

<1>5. Hence $f = F - c$ (for a suitable real constant $c$) is holomorphic with $\operatorname{Re} f = u$.
Proof: <1>4.

<1>6. The imaginary part is unique up to an additive real constant.
Proof: if $\operatorname{Re} f_1 = \operatorname{Re} f_2 = u$, then $f_1 - f_2$ is holomorphic with zero real part, hence constant (purely imaginary), so $f_1 - f_2 = ic$ for a real constant $c$.

**Part (b).**

<1>1. By part (a), $u = \operatorname{Re} f$ for a holomorphic $f$ on $\DD$, continuous on $\overline{\DD}$.
Proof: part (a) and the hypothesis that $u$ is continuous on the closure.

<1>2. By the Cauchy integral formula (Exercise 11), for $z = re^{i\theta}$,
$$f(z) = \frac{1}{2\pi}\int_0^{2\pi} \frac{e^{i\varphi} + z}{e^{i\varphi} - z} u(\varphi)\, d\varphi.$$
Proof: the Cauchy integral formula for the disk, applied to $f$ and taking real parts.

<1>3. Taking real parts gives the Poisson integral formula
$$u(z) = \frac{1}{2\pi}\int_0^{2\pi} P_r(\theta - \varphi) u(\varphi)\, d\varphi,$$
where $P_r(\gamma) = \frac{1 - r^2}{1 - 2r\cos\gamma + r^2}$.
Proof: $\operatorname{Re}\frac{e^{i\varphi} + re^{i\theta}}{e^{i\varphi} - re^{i\theta}} = \frac{1 - r^2}{1 - 2r\cos(\theta - \varphi) + r^2} = P_r(\theta - \varphi)$.

<1>4. Q.E.D.
Proof: <1>6 (a) and <1>3 (b).
:::
