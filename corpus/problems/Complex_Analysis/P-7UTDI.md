---
schema: qual/card@1
id: P-7UTDI
kind: problem
title: Constancy of holomorphic functions of constant modulus, real part, argument,
  or conjugate
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if it satisfies any of the following conditions:

a. $|f(z)|$ is constant.
b. $\Re(f(z))$ is constant.
c. $\arg(f(z))$ is constant.
d. $\overline{f(z)}$ is analytic.
:::

::: solution
**Goal:** Prove $f$ is constant in each case. Write $f = u + iv$.

<1>1. Case (a): $|f(z)| = c$ constant.
    *Proof:*
    <2>1. If $c = 0$, then $f \equiv 0$. Done.
    <2>2. If $c > 0$, then $u^2 + v^2 = c^2$ on the domain.
    <2>3. Differentiating: $u u_x + v v_x = 0$ and $u u_y + v v_y = 0$.
    <2>4. By Cauchy-Riemann ($u_x = v_y$, $u_y = -v_x$), substitute to get $u u_x - v u_y = 0$ and $u u_y + v u_x = 0$.
    <2>5. This is a linear system in $(u_x, u_y)$ with determinant $u^2 + v^2 = c^2 > 0$.
    <2>6. Thus $u_x = u_y = 0$, so $u$ is constant. Similarly $v$ is constant. Hence $f$ is constant.

<1>2. Case (b): $\Re(f) = u = c$ constant.
    *Proof:*
    <2>1. $u_x = 0$ and $u_y = 0$ everywhere.
    <2>2. By Cauchy-Riemann: $v_y = u_x = 0$ and $v_x = -u_y = 0$.
    <2>3. Thus $v$ is constant, so $f = c + iv_0$ is constant.

<1>3. Case (c): $\arg(f) = \theta_0$ constant.
    *Proof:*
    <2>1. Assume $f$ is never zero on the domain (if $f(z_0) = 0$ at some point, then $\arg f$ is undefined there).
    <2>2. Constant argument means $f(z) = |f(z)| e^{i\theta_0}$, so $v/u = \tan\theta_0$ is constant, i.e. $v = (\tan\theta_0) u$.
    <2>3. Then $v_x = (\tan\theta_0) u_x$ and $v_y = (\tan\theta_0) u_y$.
    <2>4. Cauchy-Riemann gives $u_x = v_y = (\tan\theta_0) u_y$ and $u_y = -v_x = -(\tan\theta_0) u_x$.
    <2>5. Substituting: $u_x = (\tan\theta_0)(-(\tan\theta_0) u_x) = -\tan^2\theta_0 \cdot u_x$.
    <2>6. Thus $(1 + \tan^2\theta_0) u_x = 0$, so $u_x = 0$. Similarly $u_y = 0$, and $f$ is constant.

<1>4. Case (d): $\overline{f}$ is analytic.
    *Proof:*
    <2>1. $\overline{f} = u - iv$ is analytic, so it satisfies Cauchy-Riemann: $u_x = (-v)_y = -v_y$ and $u_y = -(-v)_x = v_x$.
    <2>2. But $f = u + iv$ is also analytic: $u_x = v_y$ and $u_y = -v_x$.
    <2>3. From $u_x = v_y$ and $u_x = -v_y$: $2v_y = 0$, so $v_y = 0$.
    <2>4. From $u_y = -v_x$ and $u_y = v_x$: $2v_x = 0$, so $v_x = 0$.
    <2>5. Thus $v$ is constant, and by Cauchy-Riemann $u$ is constant. Hence $f$ is constant.

<1>5. Generalization of (a) and (b):
    If any non-constant real-valued function $\phi(u, v)$ satisfying $\nabla\phi \neq 0$ is constant on $f$'s image, then $f$ is constant. This follows because $\phi \circ f$ is a real harmonic function satisfying a constraint that forces $f'= 0$.

<1>6. Conclusion:
    In each case, $f$ is constant on the domain. Q.E.D.
:::
