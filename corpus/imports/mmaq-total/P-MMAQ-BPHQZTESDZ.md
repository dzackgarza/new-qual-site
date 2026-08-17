---
schema: qual/card@1
id: P-MMAQ-BPHQZTESDZ
kind: problem
title: (a) Show that in polar coordinates, the Cauchy-Riemann
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-riemann
relations: []
review: draft
solved: true
---

::: problem
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
1. (a) Derive the polar coordinate formulation of the Cauchy-Riemann equations: $\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$ and $\frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$.
2. (b) Verify that the principal branch of $\log z = \ln r + i\theta$ is holomorphic on $U = \{r e^{i\theta} : r > 0, -\pi < \theta < \pi\}$, and show that it cannot be extended continuously to the punctured plane $\mathbb{C}^* = \{z : |z| > 0\}$.

---

### Part (a): Polar Form of the Cauchy-Riemann Equations

<1>1. **Express polar partial derivatives via the multivariable chain rule.**
  <2>1. The change of coordinates is given by $x(r,\theta) = r\cos\theta$ and $y(r,\theta) = r\sin\theta$.
    *Proof:* Definition of polar coordinates in the plane.
  <2>2. The derivatives of the coordinate functions are:
  $$\frac{\partial x}{\partial r} = \cos\theta, \quad \frac{\partial y}{\partial r} = \sin\theta, \quad \frac{\partial x}{\partial \theta} = -r\sin\theta, \quad \frac{\partial y}{\partial \theta} = r\cos\theta.$$
    *Proof:* Direct differentiation with respect to $r$ and $\theta$.
  <2>3. By the multivariable chain rule for $u(r,\theta) = u(x(r,\theta), y(r,\theta))$ and $v(r,\theta) = v(x(r,\theta), y(r,\theta))$:
  $$\frac{\partial u}{\partial r} = u_x \cos\theta + u_y \sin\theta, \qquad \frac{\partial u}{\partial \theta} = -u_x r\sin\theta + u_y r\cos\theta,$$
  $$\frac{\partial v}{\partial r} = v_x \cos\theta + v_y \sin\theta, \qquad \frac{\partial v}{\partial \theta} = -v_x r\sin\theta + v_y r\cos\theta.$$
    *Proof:* Standard chain rule for $C^1$ functions.
  <2>4. Q.E.D.

<1>2. **Substitute Cartesian Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$.**
  <2>1. Substitute $u_x = v_y$ and $u_y = -v_x$ into $\frac{\partial v}{\partial \theta}$:
  $$\frac{\partial v}{\partial \theta} = -v_x r\sin\theta + v_y r\cos\theta = u_y r\sin\theta + u_x r\cos\theta = r(u_x \cos\theta + u_y \sin\theta) = r \frac{\partial u}{\partial r}.$$
    *Proof:* Direct substitution and factorization using <1>1.<2>3.
  <2>2. Dividing by $r > 0$ yields $\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$.
    *Proof:* Division by $r$.
  <2>3. Substitute $u_x = v_y$ and $u_y = -v_x$ into $\frac{\partial u}{\partial \theta}$:
  $$\frac{\partial u}{\partial \theta} = -u_x r\sin\theta + u_y r\cos\theta = -v_y r\sin\theta - v_x r\cos\theta = -r(v_x \cos\theta + v_y \sin\theta) = -r \frac{\partial v}{\partial r}.$$
    *Proof:* Direct substitution and factorization using <1>1.<2>3.
  <2>4. Dividing by $-r$ yields $\frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$.
    *Proof:* Division by $-r$.
  <2>5. Q.E.D.

---

### Part (b): Holomorphicity and Discontinuity of $\log z$

<1>3. **$\log z = \ln r + i\theta$ is holomorphic on $U = \{r e^{i\theta} : r > 0, -\pi < \theta < \pi\}$.**
  <2>1. The real and imaginary components are $u(r,\theta) = \ln r$ and $v(r,\theta) = \theta$.
    *Proof:* Definition of the principal logarithm.
  <2>2. The polar partial derivatives are:
  $$\frac{\partial u}{\partial r} = \frac{1}{r}, \quad \frac{\partial u}{\partial \theta} = 0, \quad \frac{\partial v}{\partial r} = 0, \quad \frac{\partial v}{\partial \theta} = 1.$$
    *Proof:* Direct differentiation of $\ln r$ and $\theta$.
  <2>3. Verifying the polar Cauchy-Riemann equations on $U$:
  $$\frac{\partial u}{\partial r} = \frac{1}{r} = \frac{1}{r}\cdot 1 = \frac{1}{r}\frac{\partial v}{\partial \theta}, \qquad \frac{\partial v}{\partial r} = 0 = -\frac{1}{r}\cdot 0 = -\frac{1}{r}\frac{\partial u}{\partial \theta}.$$
    *Proof:* Direct comparison of <2>2 with the formulas from <1>2.
  <2>4. Since $u, v$ have continuous partial derivatives on $U$ and satisfy the Cauchy-Riemann equations, $\log z$ is complex-differentiable (holomorphic) on $U$.
    *Proof:* Equivalence between real $C^1$ differentiability + Cauchy-Riemann equations and complex holomorphicity.
  <2>5. Q.E.D.

<1>4. **$\log z$ is not continuous on the punctured plane $\mathbb{C}^* = \{z : r > 0\}$.**
  <2>1. Consider the point $z_0 = -1 \in \mathbb{C}^*$ on the negative real axis.
    *Proof:* Negative real axis point where $\theta \to \pm \pi$.
  <2>2. Approach $z_0 = -1$ along the upper unit semicircle $z(\theta) = e^{i\theta}$ as $\theta \to \pi^-$:
  $$\lim_{\theta \to \pi^-} \log(e^{i\theta}) = \lim_{\theta \to \pi^-} (\ln 1 + i\theta) = i\pi.$$
    *Proof:* For $\theta \in (0, \pi)$, $\arg(e^{i\theta}) = \theta$.
  <2>3. Approach $z_0 = -1$ along the lower unit semicircle $z(\theta) = e^{i\theta}$ as $\theta \to (-\pi)^+$:
  $$\lim_{\theta \to (-\pi)^+} \log(e^{i\theta}) = \lim_{\theta \to (-\pi)^+} (\ln 1 + i\theta) = -i\pi.$$
    *Proof:* For $\theta \in (-\pi, 0)$, $\arg(e^{i\theta}) = \theta$.
  <2>4. Since $\lim_{\theta \to \pi^-} \log(e^{i\theta}) = i\pi \neq -i\pi = \lim_{\theta \to (-\pi)^+} \log(e^{i\theta})$, the limit $\lim_{z \to -1} \log z$ does not exist.
    *Proof:* Contradiction between directional limits along two continuous paths in the domain.
  <2>5. Therefore, $\log z$ is discontinuous across the negative real axis $(-\infty, 0)$, and cannot be continuous on the entire region $r > 0$.
    *Proof:* Non-existence of limit implies discontinuity.
  <2>6. Q.E.D.
:::
