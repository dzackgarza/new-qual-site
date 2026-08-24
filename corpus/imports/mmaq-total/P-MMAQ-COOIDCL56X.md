---
schema: qual/card@1
id: P-MMAQ-COOIDCL56X
kind: problem
title: Uniform continuity of $z^2$ on disks but not on $\mathbb{C}$, and a Cauchy
  problem for Laplace's equation
classification:
  areas:
  - complex-analysis
  topics:
  - PDEs
relations: []
review: draft
---

::: problem
Show that $f(z) = z^2$ is uniformly continuous in any open disk
$|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on
$\mathbb C$.

(1) Show that the function $u=u(x,y)$ given by
    $$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
    is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
    the Laplace equation
    $$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
    u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. Prove that $f(z) = z^2$ is uniformly continuous on the open disk $D(0, R) = \{z \in \mathbb{C} : |z| < R\}$ for any fixed $R > 0$, but is not uniformly continuous on $\mathbb{C}$.
2. For $u_n(x,y) = \frac{e^{ny}-e^{-ny}}{2n^2}\sin(nx) = \frac{\sinh(ny)}{n^2}\sin(nx)$ on $D = \{(x,y) \in \mathbb{R}^2 : x^2+y^2 < 1\}$, verify it solves the Laplace equation with initial data $u_n(x,0) = 0$ and $\frac{\partial u_n}{\partial y}(x,0) = \frac{\sin(nx)}{n}$.

---

### Part 1: Uniform Continuity of $f(z) = z^2$

<1>1. **$f(z) = z^2$ is uniformly continuous on $D(0, R) = \{z \in \mathbb{C} : |z| < R\}$.**
  <2>1. For any $z_1, z_2 \in D(0, R)$, $|f(z_1) - f(z_2)| = |z_1^2 - z_2^2| = |z_1 + z_2| |z_1 - z_2|$.
    *Proof:* Algebraic factorization of difference of squares and multiplicativity of modulus.
  <2>2. For any $z_1, z_2 \in D(0, R)$, $|z_1 + z_2| \leq |z_1| + |z_2| < R + R = 2R$.
    *Proof:* Triangle inequality and $|z_1| < R, |z_2| < R$.
  <2>3. Thus $|f(z_1) - f(z_2)| \leq 2R |z_1 - z_2|$ on $D(0, R)$, which means $f$ is Lipschitz continuous on $D(0, R)$ with Lipschitz constant $2R$.
    *Proof:* Follows from <2>1 and <2>2.
  <2>4. Given any $\varepsilon > 0$, set $\delta = \frac{\varepsilon}{2R} > 0$. If $z_1, z_2 \in D(0, R)$ satisfy $|z_1 - z_2| < \delta$, then $|f(z_1) - f(z_2)| \leq 2R |z_1 - z_2| < 2R \delta = \varepsilon$.
    *Proof:* Substitution of $\delta = \varepsilon / (2R)$.
  <2>5. Q.E.D.

<1>2. **$f(z) = z^2$ is not uniformly continuous on $\mathbb{C}$.**
  <2>1. Uniform continuity on $\mathbb{C}$ requires: $\forall \varepsilon > 0, \exists \delta > 0, \forall z_1, z_2 \in \mathbb{C}, |z_1 - z_2| < \delta \implies |f(z_1) - f(z_2)| < \varepsilon$.
    *Proof:* Definition of uniform continuity.
  <2>2. Set $\varepsilon_0 = 1$. For any given $\delta > 0$, choose $z_1 = \frac{1}{\delta}$ and $z_2 = \frac{1}{\delta} + \frac{\delta}{2}$ in $\mathbb{R} \subset \mathbb{C}$.
    *Proof:* Explicit point construction.
  <2>3. Then $|z_1 - z_2| = \frac{\delta}{2} < \delta$.
    *Proof:* Definition of $z_1, z_2$.
  <2>4. $|f(z_2) - f(z_1)| = |z_2^2 - z_1^2| = (z_2 - z_1)(z_2 + z_1) = \frac{\delta}{2} \cdot \left(\frac{2}{\delta} + \frac{\delta}{2}\right) = 1 + \frac{\delta^2}{4} > 1 = \varepsilon_0$.
    *Proof:* Direct algebraic calculation.
  <2>5. Therefore, $f$ fails the definition of uniform continuity on $\mathbb{C}$.
    *Proof:* Negation of uniform continuity is satisfied with $\varepsilon_0 = 1$.
  <2>6. Q.E.D.

---

### Part 2: Verification of the Cauchy Problem for Laplace's Equation

<1>3. **$u(x,y) = \frac{\sinh(ny)}{n^2} \sin(nx)$ satisfies $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ on $D$.**
  <2>1. Compute partial derivatives with respect to $x$:
  $$\frac{\partial u}{\partial x} = \frac{\sinh(ny)}{n} \cos(nx), \qquad \frac{\partial^2 u}{\partial x^2} = -\sinh(ny)\sin(nx).$$
    *Proof:* $\frac{d}{dx}\sin(nx) = n\cos(nx)$ and $\frac{d^2}{dx^2}\sin(nx) = -n^2\sin(nx)$.
  <2>2. Compute partial derivatives with respect to $y$:
  $$\frac{\partial u}{\partial y} = \frac{\cosh(ny)}{n} \sin(nx), \qquad \frac{\partial^2 u}{\partial y^2} = \sinh(ny)\sin(nx).$$
    *Proof:* $\frac{d}{dy}\sinh(ny) = n\cosh(ny)$ and $\frac{d^2}{dy^2}\sinh(ny) = n^2\sinh(ny)$.
  <2>3. Adding the two second partial derivatives:
  $$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = -\sinh(ny)\sin(nx) + \sinh(ny)\sin(nx) = 0.$$
    *Proof:* Sum of <2>1 and <2>2.
  <2>4. Q.E.D.

<1>4. **$u(x,y)$ satisfies the initial conditions $u(x,0) = 0$ and $\frac{\partial u}{\partial y}(x,0) = \frac{\sin(nx)}{n}$.**
  <2>1. At $y = 0$, $\sinh(0) = \frac{e^0 - e^0}{2} = 0$, so $u(x,0) = \frac{0}{n^2}\sin(nx) = 0$.
    *Proof:* Evaluation of $u(x,y)$ at $y=0$.
  <2>2. At $y = 0$, $\cosh(0) = \frac{e^0 + e^0}{2} = 1$, so from <1>3.<2>2, $\frac{\partial u}{\partial y}(x,0) = \frac{\cosh(0)}{n}\sin(nx) = \frac{\sin(nx)}{n}$.
    *Proof:* Evaluation of $\frac{\partial u}{\partial y}$ at $y=0$.
  <2>3. Q.E.D.
:::
