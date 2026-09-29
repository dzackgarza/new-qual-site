---
schema: qual/card@1
id: P-3AEDF
kind: problem
title: Harmonic conjugate of a $C^3$ harmonic function on a disc
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $u(x,y)$ be harmonic and have continuous partial derivatives of order three in an open disc of radius $R>0$.

a.
Let two points $(a,b), (x,y)$ in this disk be given. Show that the following integral is independent of the path in this disk joining these points:
$$
v(x,y) = \int_{a,b}^{x,y} ( -\frac{\partial u}{\partial y}dx +  \frac{\partial u}{\partial x}dy)
.$$

b. 
In parts:

- Prove that $u(x,y)+i v(x,y)$ is an analytic function in this disc.
- Prove that $v(x,y)$ is harmonic in this disc.
:::

::: {.solution}
**Goal:** Let $D = D((x_0, y_0), R) \subset \mathbb{R}^2$ be an open disk, and let $u \in C^3(D)$ be a real-valued harmonic function ($\Delta u = u_{xx} + u_{yy} = 0$).
1. (a) Prove that the differential 1-form $\omega = -u_y \, dx + u_x \, dy$ is closed, and that the line integral $\int_{(a,b)}^{(x,y)} \omega$ is independent of the path in $D$.
2. (b)(i) Prove that $f(z) = u(x,y) + i v(x,y)$ is analytic (holomorphic) in $D$.
3. (b)(ii) Prove that $v(x,y)$ is harmonic in $D$.

---

### Part (a): Path Independence of the Line Integral

::: pf

::: pf-step
**The differential form $\omega = P\,dx + Q\,dy$ with $P = -u_y$ and $Q = u_x$ is $C^1$ and closed on $D$.**

::: pf-proof

::: pf-step
Since $u \in C^3(D)$, the partial derivatives $P = -u_y$ and $Q = u_x$ are in $C^2(D)$, hence $C^1(D)$.

::: pf-proof
Continuous differentiability of orders up to 3.
:::

:::

::: pf-step
Compute the curl / exterior derivative:
$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \frac{\partial}{\partial x}(u_x) - \frac{\partial}{\partial y}(-u_y) = u_{xx} + u_{yy} = \Delta u.$$

::: pf-proof
Clairaut's theorem on equality of mixed partials and direct differentiation.
:::

:::

::: pf-step
Since $u$ is harmonic on $D$, $\Delta u = 0$, which implies $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$ everywhere in $D$.

::: pf-proof
Hypothesis that $u$ is harmonic.
:::

:::

:::

:::

::: pf-step
**Closed 1-forms on simply connected domains are exact, hence path independent.**

::: pf-proof

::: pf-step
An open disk $D$ in $\mathbb{R}^2$ is convex, hence simply connected.

::: pf-proof
Standard geometric property of open disks.
:::

:::

::: pf-step
By Green's Theorem (or Poincaré's Lemma), the line integral of a $C^1$ closed 1-form along any closed piecewise smooth curve $\gamma$ contained in $D$ is zero: $\oint_\gamma \omega = 0$.

::: pf-proof
$\oint_\gamma P\,dx+Q\,dy = \iint_{\text{Int}(\gamma)} (Q_x - P_y)\,dA = \iint_{\text{Int}(\gamma)} 0\,dA = 0$.
:::

:::

::: {.pf-step #s2-3}
If $\gamma_1, \gamma_2$ are any two piecewise smooth paths in $D$ from $(a,b)$ to $(x,y)$, then $\gamma_1 - \gamma_2$ is a closed loop, so $\int_{\gamma_1} \omega - \int_{\gamma_2} \omega = \oint_{\gamma_1 - \gamma_2} \omega = 0 \implies \int_{\gamma_1} \omega = \int_{\gamma_2} \omega$.

::: pf-proof
Additivity of path integrals.
:::

:::

::: pf-step
Therefore, the function $v(x,y) = \int_{(a,b)}^{(x,y)} (-u_y\,dx + u_x\,dy)$ is well-defined and independent of path in $D$.

::: pf-proof
Follows from step [](#s2-3){.pf-ref}.
:::

:::

:::

:::

:::

---

### Part (b)(i): Holomorphicity of $u(x,y) + i v(x,y)$

::: pf

::: pf-step
**Compute the partial derivatives of $v(x,y)$.**

::: pf-proof

::: pf-step
By the Fundamental Theorem of Calculus for line integrals of exact forms, $\nabla v(x,y) = (P(x,y), Q(x,y)) = (-u_y(x,y), u_x(x,y))$.

::: pf-proof
Differentiating $v(x,y) = \int_{(a,b)}^{(x,y)} (P\,dx + Q\,dy)$ with respect to $x$ and $y$ along axis-parallel segments.
:::

:::

::: {.pf-step #s3-2}
Explicitly, $v_x = -u_y$ and $v_y = u_x$.

::: pf-proof
Extracting components from the preceding step.
:::

:::

:::

:::

::: pf-step
**$f(z) = u(x,y) + i v(x,y)$ satisfies the Cauchy-Riemann equations in $D$.**

::: pf-proof

::: pf-step
The Cauchy-Riemann equations are $u_x = v_y$ and $u_y = -v_x$.

::: pf-proof
Standard definition.
:::

:::

::: pf-step
From step [](#s3-2){.pf-ref}, $v_y = u_x$ and $v_x = -u_y \iff u_y = -v_x$.

::: pf-proof
Direct comparison with step [](#s3-2){.pf-ref}.
:::

:::

::: pf-step
Since $u \in C^3(D)$, its partial derivatives $u_x, u_y, v_x, v_y$ are in $C^1(D)$ and are continuous.

::: pf-proof
Real differentiability follows from continuity of first partial derivatives.
:::

:::

::: pf-step
A complex function $f = u+iv$ whose real and imaginary parts are $C^1$ and satisfy the Cauchy-Riemann equations is analytic (holomorphic) on $D$.

::: pf-proof
Standard characterization of complex differentiability.
:::

:::

:::

:::

:::

---

### Part (b)(ii): Harmonicity of $v(x,y)$

::: pf

::: pf-step
**$v(x,y)$ satisfies the Laplace equation $\Delta v = 0$ on $D$.**

::: pf-proof

::: {.pf-step #s5-1}
Since $v \in C^2(D)$, compute its second partial derivatives using step [](#s3-2){.pf-ref}:
$$v_{xx} = \frac{\partial}{\partial x}(v_x) = \frac{\partial}{\partial x}(-u_y) = -u_{yx}.$$
$$v_{yy} = \frac{\partial}{\partial y}(v_y) = \frac{\partial}{\partial y}(u_x) = u_{xy}.$$

::: pf-proof
Differentiating step [](#s3-2){.pf-ref} with respect to $x$ and $y$.
:::

:::

::: {.pf-step #s5-2}
Since $u \in C^3(D) \subseteq C^2(D)$, Clairaut's theorem guarantees $u_{yx} = u_{xy}$.

::: pf-proof
Equality of mixed partials for $C^2$ functions.
:::

:::

::: pf-step
Therefore, $\Delta v = v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0$.

::: pf-proof
Substitution of step [](#s5-2){.pf-ref} into step [](#s5-1){.pf-ref}.
:::

:::

::: pf-step
Thus, $v(x,y)$ is harmonic in $D$.

::: pf-proof
Definition of harmonic function.
:::

:::

:::

:::

:::
:::
