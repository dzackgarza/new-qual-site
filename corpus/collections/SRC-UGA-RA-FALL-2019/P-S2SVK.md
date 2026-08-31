---
schema: qual/card@1
id: P-S2SVK
kind: problem
title: $\bigl|\frac{d^n}{dx^n}\frac{\sin x}{x}\bigr|\le\frac1n$ for $x\neq 0$ and
  $n\ge 1$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Differentiation
relations: []
review: draft
---

::: problem
Prove that for all $x \ne 0$ and all positive integers $n \ge 1$:
$$
\left| \frac{d^{n}}{d x^{n}} \left(\frac{\sin x}{x}\right) \right| \le \frac{1}{n}.
$$
:::

::: solution
**Goal:** Express $\frac{\sin x}{x}$ as a parametric integral, justify differentiation under the integral sign, and bound the resulting integrand.

<1>1. Parametric integral representation of $\frac{\sin x}{x}$:
    *Proof:*
    <2>1. For $x \ne 0$, evaluate the integral of $\cos(tx)$ with respect to $t$:
    $$\int_0^1 \cos(tx) \, dt = \left[ \frac{\sin(tx)}{x} \right]_{t=0}^{t=1} = \frac{\sin x}{x} - \frac{\sin(0)}{x} = \frac{\sin x}{x}.$$

<1>2. Partial derivatives of the integrand:
    *Proof:*
    <2>1. Let $g(x, t) = \cos(tx)$ for $(x, t) \in \mathbb{R} \times [0, 1]$.
    <2>2. For every $n \ge 1$, compute the $n$-th partial derivative with respect to $x$:
    $$\frac{\partial^n}{\partial x^n} \cos(tx) = t^n \cos\left(tx + \frac{n\pi}{2}\right).$$
    <2>3. In particular:
        - When $n = 4k$, $\frac{\partial^n g}{\partial x^n} = t^n \cos(tx)$.
        - When $n = 4k+1$, $\frac{\partial^n g}{\partial x^n} = -t^n \sin(tx)$.
        - When $n = 4k+2$, $\frac{\partial^n g}{\partial x^n} = -t^n \cos(tx)$.
        - When $n = 4k+3$, $\frac{\partial^n g}{\partial x^n} = t^n \sin(tx)$.

<1>3. Justification of differentiation under the integral sign:
    *Proof:*
    <2>1. The function $g(x, t)$ and all its partial derivatives $\frac{\partial^k g}{\partial x^k}(x, t)$ are continuous on $\mathbb{R} \times [0, 1]$.
    <2>2. On any compact interval $x \in [a, b]$, the derivative is dominated by
    $$\left| \frac{\partial^n g}{\partial x^n}(x, t) \right| = t^n \left| \cos\left(tx + \frac{n\pi}{2}\right) \right| \le t^n \le 1 \in L^1([0, 1]).$$
    <2>3. By Leibniz's Integral Rule (or the Dominated Convergence Theorem applied inductively), we may differentiate under the integral sign $n$ times:
    $$\frac{d^n}{dx^n} \left(\frac{\sin x}{x}\right) = \frac{d^n}{dx^n} \int_0^1 \cos(tx) \, dt = \int_0^1 \frac{\partial^n}{\partial x^n} \cos(tx) \, dt = \int_0^1 t^n \cos\left(tx + \frac{n\pi}{2}\right) \, dt.$$

<1>4. Bounding the derivative:
    *Proof:*
    <2>1. Apply the triangle inequality for integrals:
    $$\left| \frac{d^n}{dx^n} \left(\frac{\sin x}{x}\right) \right| = \left| \int_0^1 t^n \cos\left(tx + \frac{n\pi}{2}\right) \, dt \right| \le \int_0^1 t^n \left| \cos\left(tx + \frac{n\pi}{2}\right) \right| \, dt.$$
    <2>2. Since $|\cos(\theta)| \le 1$ for all $\theta \in \mathbb{R}$ and $t \ge 0$:
    $$\int_0^1 t^n \left| \cos\left(tx + \frac{n\pi}{2}\right) \right| \, dt \le \int_0^1 t^n \, dt = \left[ \frac{t^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}.$$
    <2>3. Since $n \ge 1$, $\frac{1}{n+1} < \frac{1}{n} \le \frac{1}{n}$.

<1>5. Conclusion:
    *Proof:*
    For all $x \ne 0$ and $n \ge 1$, $\left| \frac{d^n}{dx^n} \left(\frac{\sin x}{x}\right) \right| \le \frac{1}{n+1} \le \frac{1}{n}$.
:::

