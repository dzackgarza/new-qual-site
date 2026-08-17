---
schema: qual/card@1
id: P-MMAQ-CEXDT22XWE
kind: problem
title: Harmonic conjugate of a $C^3$ harmonic function on a disk
classification:
  areas:
  - complex-analysis
  topics:
  - harmonic-functions
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Let $u(x,y)$ be harmonic and have continuous partial derivatives of
order three in an open disc of radius $R>0$.

(a) Let two points $(a,b), (x,y)$ in this disk be given. Show that
    the following integral is independent of the path in this disk
    joining these points:
    $$v(x,y) = \int_{a,b}^{x,y} ( -\frac{\partial u}{\partial y}dx +  \frac{\partial u}{\partial x}dy).$$\

(b) \hfill

    (i) Prove that $u(x,y)+i v(x,y)$ is an analytic function in this disc.

    (ii) Prove that $v(x,y)$ is harmonic in this disc.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $D = D((x_0, y_0), R) \subset \mathbb{R}^2$ be an open disk, and let $u \in C^3(D)$ be a real-valued harmonic function ($\Delta u = u_{xx} + u_{yy} = 0$).
1. (a) Prove that the differential 1-form $\omega = -u_y \, dx + u_x \, dy$ is closed, and that the line integral $\int_{(a,b)}^{(x,y)} \omega$ is independent of the path in $D$.
2. (b)(i) Prove that $f(z) = u(x,y) + i v(x,y)$ is analytic (holomorphic) in $D$.
3. (b)(ii) Prove that $v(x,y)$ is harmonic in $D$.

---

### Part (a): Path Independence of the Line Integral

<1>1. **The differential form $\omega = P\,dx + Q\,dy$ with $P = -u_y$ and $Q = u_x$ is $C^1$ and closed on $D$.**
  <2>1. Since $u \in C^3(D)$, the partial derivatives $P = -u_y$ and $Q = u_x$ are in $C^2(D)$, hence $C^1(D)$.
    *Proof:* Continuous differentiability of orders up to 3.
  <2>2. Compute the curl / exterior derivative:
  $$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \frac{\partial}{\partial x}(u_x) - \frac{\partial}{\partial y}(-u_y) = u_{xx} + u_{yy} = \Delta u.$$
    *Proof:* Clairaut's theorem on equality of mixed partials and direct differentiation.
  <2>3. Since $u$ is harmonic on $D$, $\Delta u = 0$, which implies $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$ everywhere in $D$.
    *Proof:* Hypothesis that $u$ is harmonic.
  <2>4. Q.E.D.

<1>2. **Closed 1-forms on simply connected domains are exact, hence path independent.**
  <2>1. An open disk $D$ in $\mathbb{R}^2$ is convex, hence simply connected.
    *Proof:* Standard geometric property of open disks.
  <2>2. By Green's Theorem (or Poincaré's Lemma), the line integral of a $C^1$ closed 1-form along any closed piecewise smooth curve $\gamma$ contained in $D$ is zero: $\oint_\gamma \omega = 0$.
    *Proof:* $\oint_\gamma P\,dx+Q\,dy = \iint_{\text{Int}(\gamma)} (Q_x - P_y)\,dA = \iint_{\text{Int}(\gamma)} 0\,dA = 0$.
  <2>3. If $\gamma_1, \gamma_2$ are any two piecewise smooth paths in $D$ from $(a,b)$ to $(x,y)$, then $\gamma_1 - \gamma_2$ is a closed loop, so $\int_{\gamma_1} \omega - \int_{\gamma_2} \omega = \oint_{\gamma_1 - \gamma_2} \omega = 0 \implies \int_{\gamma_1} \omega = \int_{\gamma_2} \omega$.
    *Proof:* Additivity of path integrals.
  <2>4. Therefore, the function $v(x,y) = \int_{(a,b)}^{(x,y)} (-u_y\,dx + u_x\,dy)$ is well-defined and independent of path in $D$.
    *Proof:* Follows from <2>3.
  <2>5. Q.E.D.

---

### Part (b)(i): Holomorphicity of $u(x,y) + i v(x,y)$

<1>3. **Compute the partial derivatives of $v(x,y)$.**
  <2>1. By the Fundamental Theorem of Calculus for line integrals of exact forms, $\nabla v(x,y) = (P(x,y), Q(x,y)) = (-u_y(x,y), u_x(x,y))$.
    *Proof:* Differentiating $v(x,y) = \int_{(a,b)}^{(x,y)} (P\,dx + Q\,dy)$ with respect to $x$ and $y$ along axis-parallel segments.
  <2>2. Explicitly, $v_x = -u_y$ and $v_y = u_x$.
    *Proof:* Extracting components from <2>1.
  <2>3. Q.E.D.

<1>4. **$f(z) = u(x,y) + i v(x,y)$ satisfies the Cauchy-Riemann equations in $D$.**
  <2>1. The Cauchy-Riemann equations are $u_x = v_y$ and $u_y = -v_x$.
    *Proof:* Standard definition.
  <2>2. From <1>3.<2>2, $v_y = u_x$ and $v_x = -u_y \iff u_y = -v_x$.
    *Proof:* Direct comparison with <1>3.<2>2.
  <2>3. Since $u \in C^3(D)$, its partial derivatives $u_x, u_y, v_x, v_y$ are in $C^1(D)$ and are continuous.
    *Proof:* Real differentiability follows from continuity of first partial derivatives.
  <2>4. A complex function $f = u+iv$ whose real and imaginary parts are $C^1$ and satisfy the Cauchy-Riemann equations is analytic (holomorphic) on $D$.
    *Proof:* Standard characterization of complex differentiability.
  <2>5. Q.E.D.

---

### Part (b)(ii): Harmonicity of $v(x,y)$

<1>5. **$v(x,y)$ satisfies the Laplace equation $\Delta v = 0$ on $D$.**
  <2>1. Since $v \in C^2(D)$, compute its second partial derivatives using <1>3.<2>2:
  $$v_{xx} = \frac{\partial}{\partial x}(v_x) = \frac{\partial}{\partial x}(-u_y) = -u_{yx}.$$
  $$v_{yy} = \frac{\partial}{\partial y}(v_y) = \frac{\partial}{\partial y}(u_x) = u_{xy}.$$
    *Proof:* Differentiating <1>3.<2>2 with respect to $x$ and $y$.
  <2>2. Since $u \in C^3(D) \subseteq C^2(D)$, Clairaut's theorem guarantees $u_{yx} = u_{xy}$.
    *Proof:* Equality of mixed partials for $C^2$ functions.
  <2>3. Therefore, $\Delta v = v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0$.
    *Proof:* Substitution of <2>2 into <2>1.
  <2>4. Thus, $v(x,y)$ is harmonic in $D$.
    *Proof:* Definition of harmonic function.
  <2>5. Q.E.D.
:::
