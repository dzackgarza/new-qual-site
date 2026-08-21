---
schema: qual/card@1
id: P-AMD-YDNWHPDM
kind: problem
title: $2^{n-1}\prod_{k=1}^{n-1}\sin(k\pi/n)=n$, polar Cauchy–Riemann equations, and
  holomorphy of $\log z$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
  - Cauchy-Riemann
  - Complex Logarithm
relations: []
review: draft
solved: true
---

::: {.problem}
Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
    that
    $$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
    = n
    \; .$$ 
    
    > Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.

    (a) Show that in polar coordinates, the Cauchy-Riemann
    equations take the form

    $$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
    \; \; \; \text{and} \; \; \;
    \frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$

    (b) Use these equations to show that the logarithm function
    defined by $$\log z = \log r + i \theta \; \;
    \mbox{where} \; z = r e^{i \theta } \; \mbox{with} \; - \pi < \theta < \pi$$
    is a holomorphic function in the region
    $r>0, \; - \pi < \theta < \pi$. Also show that $\log z$ defined
    above is not continuous in $r>0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. Prove using $n$-th roots of unity that $2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = n$ for any integer $n \geq 2$.
2. (a) Derive the polar form of the Cauchy-Riemann equations: $\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$ and $\frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$.
3. (b) Verify that the principal branch of $\log z = \ln r + i\theta$ on $U = \{r e^{i\theta} : r > 0, -\pi < \theta < \pi\}$ is holomorphic, and prove it cannot be extended continuously to the punctured plane $\mathbb{C}^* = \{z \in \mathbb{C} : r > 0\}$.

---

### Part 1: Product of Sines via Roots of Unity

<1>1. **Factorization of the cyclotomic polynomial.**
  <2>1. The polynomial $z^n - 1$ factors as $(z - 1)\sum_{k=0}^{n-1} z^k = (z-1)(z^{n-1} + z^{n-2} + \dots + z + 1)$.
    *Proof:* Standard algebraic identity for geometric series / difference of powers.
  <2>2. The roots of $z^n - 1 = 0$ are $\omega_k = e^{i 2\pi k/n}$ for $k = 0, 1, \dots, n-1$.
    *Proof:* $(e^{i 2\pi k/n})^n = e^{i 2\pi k} = 1$.
  <2>3. Since $\omega_0 = 1$, the remaining $n-1$ roots of unity $\omega_1, \dots, \omega_{n-1}$ are the roots of $P(z) = z^{n-1} + z^{n-2} + \dots + z + 1 = \prod_{k=1}^{n-1} (z - \omega_k)$.
    *Proof:* A monic polynomial of degree $n-1$ with $n-1$ distinct roots is uniquely factored as the product of its linear factors.
  <2>4. Evaluating $P(z)$ at $z=1$:
  $$\prod_{k=1}^{n-1} (1 - e^{i 2\pi k/n}) = P(1) = \underbrace{1 + 1 + \dots + 1}_{n \text{ terms}} = n.$$
    *Proof:* Direct substitution of $z=1$ into $P(z)$.
  <2>5. Q.E.D.

<1>2. **Compute $|1 - e^{i 2\pi k/n}|$.**
  <2>1. For any real $\phi$, $|1 - e^{i\phi}|^2 = (1 - \cos\phi)^2 + (\sin\phi)^2 = 1 - 2\cos\phi + \cos^2\phi + \sin^2\phi = 2 - 2\cos\phi = 2(1 - \cos\phi)$.
    *Proof:* Expansion of complex modulus squared.
  <2>2. Using the half-angle identity $1 - \cos\phi = 2\sin^2(\phi/2)$, $|1 - e^{i\phi}|^2 = 4\sin^2(\phi/2)$, so $|1 - e^{i\phi}| = 2\left|\sin\left(\frac{\phi}{2}\right)\right|$.
    *Proof:* Taking the principal square root.
  <2>3. For $\phi = \frac{2\pi k}{n}$ with $1 \leq k \leq n-1$, $\frac{\phi}{2} = \frac{\pi k}{n} \in (0, \pi)$, so $\sin\left(\frac{\pi k}{n}\right) > 0$.
    *Proof:* The sine function is strictly positive on $(0, \pi)$.
  <2>4. Thus, $|1 - e^{i 2\pi k/n}| = 2\sin\left(\frac{\pi k}{n}\right)$ for every $1 \leq k \leq n-1$.
    *Proof:* Follows from <2>2 and <2>3.
  <2>5. Q.E.D.

<1>3. **Take the modulus of the product.**
  <2>1. Taking the absolute value of both sides of <1>1.<2>4:
  $$\left|\prod_{k=1}^{n-1} (1 - e^{i 2\pi k/n})\right| = |n| = n \implies \prod_{k=1}^{n-1} |1 - e^{i 2\pi k/n}| = n.$$
    *Proof:* Multiplicativity of the complex modulus.
  <2>2. Substituting <1>2.<2>4 into the product:
  $$\prod_{k=1}^{n-1} \left( 2\sin\left(\frac{k\pi}{n}\right) \right) = 2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = n.$$
    *Proof:* Factoring out the $n-1$ factors of $2$.
  <2>3. Q.E.D.

---

### Part 2: (a) Cauchy-Riemann Equations in Polar Coordinates

<1>4. **Express partial derivatives with respect to $r$ and $\theta$ in terms of $x$ and $y$.**
  <2>1. The coordinate transformation is $x(r,\theta) = r\cos\theta$ and $y(r,\theta) = r\sin\theta$.
    *Proof:* Definition of polar coordinates.
  <2>2. The partial derivatives are:
  $$\frac{\partial x}{\partial r} = \cos\theta, \quad \frac{\partial y}{\partial r} = \sin\theta, \quad \frac{\partial x}{\partial \theta} = -r\sin\theta, \quad \frac{\partial y}{\partial \theta} = r\cos\theta.$$
    *Proof:* Differentiating $x$ and $y$ with respect to $r$ and $\theta$.
  <2>3. By the multivariable chain rule for $u(r,\theta) = u(x(r,\theta), y(r,\theta))$:
  $$\frac{\partial u}{\partial r} = u_x \cos\theta + u_y \sin\theta, \qquad \frac{\partial u}{\partial \theta} = -u_x r\sin\theta + u_y r\cos\theta.$$
  $$\frac{\partial v}{\partial r} = v_x \cos\theta + v_y \sin\theta, \qquad \frac{\partial v}{\partial \theta} = -v_x r\sin\theta + v_y r\cos\theta.$$
    *Proof:* Chain rule for compositions of $C^1$ functions.
  <2>4. Q.E.D.

<1>5. **Substitute Cartesian Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$.**
  <2>1. Substitute $u_x = v_y$ and $u_y = -v_x$ into the expression for $\frac{\partial v}{\partial \theta}$:
  $$\frac{\partial v}{\partial \theta} = -v_x r\sin\theta + v_y r\cos\theta = u_y r\sin\theta + u_x r\cos\theta = r(u_x \cos\theta + u_y \sin\theta) = r \frac{\partial u}{\partial r}.$$
    *Proof:* Direct substitution and grouping by <1>4.<2>3.
  <2>2. Dividing by $r > 0$ yields $\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$.
    *Proof:* Division by $r$.
  <2>3. Substitute $u_x = v_y$ and $u_y = -v_x$ into the expression for $\frac{\partial u}{\partial \theta}$:
  $$\frac{\partial u}{\partial \theta} = -u_x r\sin\theta + u_y r\cos\theta = -v_y r\sin\theta - v_x r\cos\theta = -r(v_x \cos\theta + v_y \sin\theta) = -r \frac{\partial v}{\partial r}.$$
    *Proof:* Direct substitution and grouping by <1>4.<2>3.
  <2>4. Dividing by $-r$ yields $\frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$.
    *Proof:* Division by $-r$.
  <2>5. Q.E.D.

---

### Part 3: (b) Holomorphicity and Discontinuity of $\log z$

<1>6. **$\log z = \ln r + i\theta$ is holomorphic on $U = \{r e^{i\theta} : r > 0, -\pi < \theta < \pi\}$.**
  <2>1. For $\log z$, the real and imaginary parts are $u(r,\theta) = \ln r$ and $v(r,\theta) = \theta$.
    *Proof:* By definition of $\log z$.
  <2>2. Compute the polar partial derivatives:
  $$\frac{\partial u}{\partial r} = \frac{1}{r}, \quad \frac{\partial u}{\partial \theta} = 0, \quad \frac{\partial v}{\partial r} = 0, \quad \frac{\partial v}{\partial \theta} = 1.$$
    *Proof:* Differentiation of $\ln r$ and $\theta$.
  <2>3. Check the polar Cauchy-Riemann equations on $U$:
  $$\frac{\partial u}{\partial r} = \frac{1}{r} = \frac{1}{r}\cdot 1 = \frac{1}{r}\frac{\partial v}{\partial \theta}, \qquad \frac{\partial v}{\partial r} = 0 = -\frac{1}{r}\cdot 0 = -\frac{1}{r}\frac{\partial u}{\partial \theta}.$$
    *Proof:* Direct comparison of <2>2 with the polar CR equations.
  <2>4. Since $u, v \in C^1(U)$ and satisfy the Cauchy-Riemann equations, $\log z$ is holomorphic on $U$.
    *Proof:* Equivalence of real differentiability + CR equations with complex differentiability (holomorphicity).
  <2>5. Q.E.D.

<1>7. **$\log z$ cannot be continuous on the punctured plane $\mathbb{C}^* = \{z : r > 0\}$.**
  <2>1. Consider the point $z_0 = -1 \in \mathbb{C}^*$ (which has $r = 1$, $\theta = \pm \pi$).
    *Proof:* Test point on the branch cut $(-\infty, 0)$.
  <2>2. Approach $z_0 = -1$ from the upper half-plane along the unit circle $z(\theta) = e^{i\theta}$ as $\theta \to \pi^-$:
  $$\lim_{\theta \to \pi^-} \log(e^{i\theta}) = \lim_{\theta \to \pi^-} (\ln 1 + i\theta) = i\pi.$$
    *Proof:* Since $-\pi < \theta < \pi$, $\log(e^{i\theta}) = i\theta$.
  <2>3. Approach $z_0 = -1$ from the lower half-plane along the unit circle $z(\theta) = e^{i\theta}$ as $\theta \to (-\pi)^+$:
  $$\lim_{\theta \to (-\pi)^+} \log(e^{i\theta}) = \lim_{\theta \to (-\pi)^+} (\ln 1 + i\theta) = -i\pi.$$
    *Proof:* In the lower half-plane, $-\pi < \theta < 0$, so $\log(e^{i\theta}) = i\theta$.
  <2>4. Since the two directional limits $i\pi$ and $-i\pi$ do not agree ($i\pi \neq -i\pi$), the limit $\lim_{z \to -1} \log z$ does not exist.
    *Proof:* Failure of two path limits to coincide.
  <2>5. Therefore, $\log z$ is discontinuous at every point on the negative real axis $(-\infty, 0]$, and is not continuous on $r > 0$.
    *Proof:* A function lacking a limit at a point is not continuous at that point.
  <2>6. Q.E.D.
:::
