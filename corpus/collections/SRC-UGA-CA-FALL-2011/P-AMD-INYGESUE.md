---
schema: qual/card@1
id: P-AMD-INYGESUE
kind: problem
title: Uniform continuity of $z^2$ and Hadamard's example for Laplace's equation
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Harmonic Functions
  - PDEs
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that $f(z) = z^2$ is uniformly continuous in any open disk $|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on $\mathbb C$.

```
(1) Show that the function $u=u(x,y)$ given by
    $$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
    is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
    the Laplace equation
    $$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
    u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$
(2) Show that there exist points $(x,y)\in D$ such that
    $\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.
```
:::

::: {.solution}
**Goal:**

1. Prove that $f(z) = z^2$ is uniformly continuous on the open disk $D(0, R) = \{z \in \mathbb{C} : |z| < R\}$ for any fixed $R > 0$, but is not uniformly continuous on $\mathbb{C}$.

2. For the function $u_n(x,y) = \frac{e^{ny}-e^{-ny}}{2n^2}\sin(nx) = \frac{\sinh(ny)}{n^2}\sin(nx)$ on $D = \{(x,y) \in \mathbb{R}^2 : x^2+y^2 < 1\}$, verify it solves the Laplace equation with Cauchy initial data $u_n(x,0) = 0$ and $\frac{\partial u_n}{\partial y}(x,0) = \frac{\sin(nx)}{n}$.

3. Show that there exist points $(x,y) \in D$ where $\limsup_{n\to\infty} |u_n(x,y)| = \infty$.

* * *

### Part 1: Uniform Continuity of $f(z) = z^2$

::: pf

::: pf-step
**$f(z) = z^2$ is uniformly continuous on $D(0, R) = \{z \in \mathbb{C} : |z| < R\}$.**

::: pf-proof

::: {.pf-step #s1-1}
For any $z_1, z_2 \in D(0, R)$, $|f(z_1) - f(z_2)| = |z_1^2 - z_2^2| = |z_1 + z_2| |z_1 - z_2|$.

::: pf-proof
By the algebraic factorization of difference of squares and multiplicativity of the complex modulus.
:::

:::

::: {.pf-step #s1-2}
For any $z_1, z_2 \in D(0, R)$, $|z_1 + z_2| \leq |z_1| + |z_2| < R + R = 2R$.

::: pf-proof
By the triangle inequality and the condition $|z_1| < R, |z_2| < R$.
:::

:::

::: {.pf-step #s1-3}
Thus, for any $z_1, z_2 \in D(0, R)$, $|f(z_1) - f(z_2)| \leq 2R |z_1 - z_2|$, so $f$ is Lipschitz continuous on $D(0,R)$ with Lipschitz constant $2R$.

::: pf-proof
Follows directly from steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.
:::

:::

::: pf-step
For every $\varepsilon > 0$, choosing $\delta = \frac{\varepsilon}{2R} > 0$, if $|z_1 - z_2| < \delta$ with $z_1, z_2 \in D(0, R)$, then $|f(z_1) - f(z_2)| \leq 2R |z_1 - z_2| < 2R \delta = \varepsilon$.

::: pf-proof
Direct substitution of $\delta = \frac{\varepsilon}{2R}$ into step [](#s1-3){.pf-ref}.
:::

:::

:::

:::

::: pf-step
**$f(z) = z^2$ is not uniformly continuous on $\mathbb{C}$.**

::: pf-proof

::: pf-step
A function $f: \mathbb{C} \to \mathbb{C}$ is uniformly continuous if and only if $\forall \varepsilon > 0, \exists \delta > 0, \forall z_1, z_2 \in \mathbb{C}, |z_1 - z_2| < \delta \implies |f(z_1) - f(z_2)| < \varepsilon$.
The negation is: $\exists \varepsilon_0 > 0, \forall \delta > 0, \exists z_1, z_2 \in \mathbb{C}$ such that $|z_1 - z_2| < \delta$ and $|f(z_1) - f(z_2)| \geq \varepsilon_0$.

::: pf-proof
Standard logical negation of uniform continuity.
:::

:::

::: pf-step
Set $\varepsilon_0 = 1$.
For any given $\delta > 0$, choose $z_1 = \frac{1}{\delta} \in \mathbb{R} \subset \mathbb{C}$ and $z_2 = \frac{1}{\delta} + \frac{\delta}{2} \in \mathbb{R} \subset \mathbb{C}$.

::: pf-proof
Explicit construction of test points.
:::

:::

::: pf-step
$|z_1 - z_2| = \frac{\delta}{2} < \delta$.

::: pf-proof
By definition of $z_1$ and $z_2$.
:::

:::

::: pf-step
$|f(z_2) - f(z_1)| = |z_2^2 - z_1^2| = |(z_2 - z_1)(z_2 + z_1)| = \frac{\delta}{2} \cdot \left(\frac{2}{\delta} + \frac{\delta}{2}\right) = 1 + \frac{\delta^2}{4} > 1 = \varepsilon_0$.

::: pf-proof
By direct calculation since $z_1, z_2$ are positive real numbers.
:::

:::

:::

:::

:::

* * *

### Part 2: Cauchy Problem for the Laplace Equation

::: pf

::: pf-step
**$u(x,y) = \frac{\sinh(ny)}{n^2} \sin(nx)$ satisfies the Laplace equation $\Delta u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ on $D$.**

::: pf-proof

::: {.pf-step #s3-1}
$\frac{\partial u}{\partial x} = \frac{\sinh(ny)}{n} \cos(nx)$ and $\frac{\partial^2 u}{\partial x^2} = -\sinh(ny)\sin(nx)$.

::: pf-proof
Differentiating $\sin(nx)$ with respect to $x$ gives $n\cos(nx)$, and differentiating again gives $-n^2\sin(nx)$.
Dividing by $n^2$ gives $-\sinh(ny)\sin(nx)$.
:::

:::

::: {.pf-step #s3-2}
$\frac{\partial u}{\partial y} = \frac{\cosh(ny)}{n} \sin(nx)$ and $\frac{\partial^2 u}{\partial y^2} = \sinh(ny)\sin(nx)$.

::: pf-proof
Differentiating $\sinh(ny) = \frac{e^{ny}-e^{-ny}}{2}$ with respect to $y$ gives $n\cosh(ny)$, and differentiating again gives $n^2\sinh(ny)$.
Dividing by $n^2$ gives $\sinh(ny)\sin(nx)$.
:::

:::

::: pf-step
$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = -\sinh(ny)\sin(nx) + \sinh(ny)\sin(nx) = 0$.

::: pf-proof
Sum of steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
**$u(x,y)$ satisfies the initial conditions $u(x,0) = 0$ and $\frac{\partial u}{\partial y}(x,0) = \frac{\sin(nx)}{n}$.**

::: pf-proof

::: pf-step
At $y=0$, $\sinh(0) = \frac{e^0 - e^0}{2} = 0$, so $u(x,0) = \frac{0}{n^2}\sin(nx) = 0$.

::: pf-proof
Direct evaluation at $y=0$.
:::

:::

::: pf-step
At $y=0$, $\cosh(0) = \frac{e^0 + e^0}{2} = 1$, so from step [](#s3-2){.pf-ref}, $\frac{\partial u}{\partial y}(x,0) = \frac{\cosh(0)}{n}\sin(nx) = \frac{\sin(nx)}{n}$.

::: pf-proof
Direct evaluation at $y=0$.
:::

:::

:::

:::

:::

* * *

### Part 3: Instability / Blowup of the Solution (Hadamard Example)

::: pf

::: pf-step
**There exist points $(x,y) \in D$ such that $\limsup_{n\to\infty} |u_n(x,y)| = \infty$.**

::: pf-proof

::: pf-step
Choose $(x_0, y_0) = \left(\frac{1}{2}, \frac{1}{2}\right) \in D$, since $x_0^2 + y_0^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} < 1$.

::: pf-proof
Point belongs to $D$ as its distance to origin is $\frac{1}{\sqrt{2}} < 1$.
:::

:::

::: {.pf-step #s5-2}
For any $y > 0$, $|u_n(x,y)| = \frac{e^{ny} - e^{-ny}}{2n^2} |\sin(nx)| \geq \frac{e^{ny} - 1}{2n^2} |\sin(nx)|$.

::: pf-proof
For $y > 0, n \geq 1$, $e^{-ny} \leq 1$.
:::

:::

::: {.pf-step #s5-3}
By Dirichlet's approximation theorem / equidistribution modulo $2\pi$, there exists a subsequence $n_k \to \infty$ such that $|\sin(n_k x_0)| = |\sin(n_k / 2)| \geq \frac{1}{2}$.

::: pf-proof
The fractional parts of $\frac{n}{2\pi}$ are dense in $[0,1]$ (since $\frac{1}{2\pi}$ is irrational), so $n/2 \pmod \pi$ visits the interval $[\pi/6, 5\pi/6]$ infinitely often, where $\sin \geq 1/2$.
:::

:::

::: pf-step
Along this subsequence $n_k$, $|u_{n_k}(x_0, y_0)| \geq \frac{e^{n_k / 2} - 1}{2n_k^2} \cdot \frac{1}{2} = \frac{e^{n_k/2} - 1}{4n_k^2}$.

::: pf-proof
Follows from steps [](#s5-2){.pf-ref} and [](#s5-3){.pf-ref}.
:::

:::

::: pf-step
Since $\lim_{k\to\infty} \frac{e^{n_k/2} - 1}{4n_k^2} = \infty$ (exponential growth dominates polynomial growth), $\limsup_{n\to\infty} |u_n(x_0, y_0)| = \infty$.

::: pf-proof
Limit of $e^{t}/t^2$ as $t \to \infty$ is $\infty$.
:::

:::

:::

:::

:::
:::
