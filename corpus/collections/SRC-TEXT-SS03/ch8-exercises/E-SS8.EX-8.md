---
schema: qual/card@1
id: E-SS8.EX-8
kind: problem
title: A harmonic function on the first quadrant with piecewise constant boundary values
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Ten of the card's fourteen steps, every leaf of the three parts, asserted their claim with
    no proof body; each now carries a `pf-proof`, and the `**Goal.**` paragraph that restated
    the statement is replaced by a plan sentence. No claim was changed and the construction is
    the same. Checked: that $z\mapsto z^2$ is a biholomorphism of the quadrant onto the upper
    half-plane with the inverse given by the principal square root; that the image of each
    boundary piece is the one the card states; that $v$ is the real part of a holomorphic
    function, hence harmonic; and the three boundary limits, recomputed on the three intervals
    $(-\infty,0)$, $(0,1)$ and $(1,\infty)$. Not checked: the printed page of Stein and
    Shakarchi's Chapter 8, Exercise 8, the retained source being an extraction; no published
    solution set for the exercise is in the checkout.
---

::: {.exercise}
Find a harmonic function $u$ in the open first quadrant that extends continuously up to the boundary except at the points 0 and 1, and that takes on the following boundary values: $u(x, y) = 1$ on the half-lines $\{y = 0, x > 1\}$ and $\{x = 0, y > 0\}$, and $u(x, y) = 0$ on the segment $\{0 < x < 1, y = 0\}$.

[Hint: Find conformal maps $F_1, F_2, \ldots, F_5$ indicated in Figure 11. Note that $\frac{1}{\pi}\arg(z)$ is harmonic on the upper half-plane, equals 0 on the positive real axis, and 1 on the negative real axis.]
:::

::: {.solution}

The map $z\mapsto z^2$ carries the quadrant onto the upper half-plane and its two boundary rays onto the negative axis and the ray $(1,\infty)$; there the function $1-\frac1\pi(\arg(w-1)-\arg(w))$ is harmonic and takes the values $1,0,1$ on $(-\infty,0)$, $(0,1)$ and $(1,\infty)$.

::: pf

::: {.pf-step #s1}

Conformal mapping of the quadrant to the upper half-plane:

::: pf-proof

Steps 1.1--1.3 identify the image of the quadrant and of each of its boundary pieces under $z\mapsto z^2$.

::: pf-step

Let $Q = \{z \in \CC : \Re z > 0, \Im z > 0\}$. Every $z \in Q$ has polar representation $z = r e^{i\theta}$ with $r > 0$ and $\theta \in (0, \pi/2)$.

::: pf-proof

For $z=x+iy$ with $x,y>0$ set $r=\sqrt{x^2+y^2}>0$ and $\theta=\arctan(y/x)$, which lies in $(0,\pi/2)$ because $y/x>0$; then $x=r\cos\theta$ and $y=r\sin\theta$, that is $z=re^{i\theta}$. This is the polar form of a nonzero complex number, and $z\ne0$ because $x>0$.

:::

:::

::: pf-step

Define $F(z) = z^2$. For $z \in Q$, $F(z) = r^2 e^{i 2\theta}$ with $2\theta \in (0, \pi)$, so $F$ maps $Q$ biholomorphically onto the upper half-plane $\halfplane = \{w \in \CC : \Im w > 0\}$.

::: pf-proof

$(re^{i\theta})^2=r^2e^{2i\theta}$ and $2\theta\in(0,\pi)$, so $F(Q)\subseteq\halfplane$. $F$ is injective on $Q$: $z_1^2=z_2^2$ gives $z_1=\pm z_2$, and two points of $Q$ are never negatives of one another since their real parts are both positive. $F$ is surjective onto $\halfplane$: a point $w=\rho e^{i\varphi}$ with $\varphi\in(0,\pi)$ is the square of $z=\sqrt\rho\,e^{i\varphi/2}$, and $\varphi/2\in(0,\pi/2)$ puts $z$ in $Q$. Finally $F$ is holomorphic with $F'(z)=2z\ne0$ on $Q$, and its inverse $w\mapsto\sqrt\rho\,e^{i\varphi/2}$ is the principal square root, holomorphic on $\halfplane$; so $F$ is biholomorphic onto $\halfplane$.

:::

:::

::: pf-step

The boundary components of $Q$ map under $z \mapsto z^2$ as follows:
- The positive imaginary axis $\{x = 0, y > 0\}$ maps to the negative real axis $(-\infty, 0)$ via $(iy)^2 = -y^2 < 0$.
- The segment $\{0 < x < 1, y = 0\}$ maps to the segment $(0, 1)$ on the real axis via $x^2 \in (0, 1)$.
- The ray $\{x > 1, y = 0\}$ maps to the ray $(1, \infty)$ on the real axis via $x^2 \in (1, \infty)$.

::: pf-proof

These are three substitutions. On the imaginary axis $z=iy$ with $y>0$, so $z^2=-y^2$, a negative real number, and $y\mapsto-y^2$ is a bijection of $(0,\infty)$ onto $(-\infty,0)$. On the real axis $z=x$ with $x>0$, so $z^2=x^2$, and $x\mapsto x^2$ is a bijection of $(0,1)$ onto $(0,1)$ and of $(1,\infty)$ onto $(1,\infty)$. The two remaining boundary points are $0$ and $1$, the images of $0$ and $1$.

:::

:::

:::

:::

::: {.pf-step #s2}

Construction of the harmonic profile on the upper half-plane $\halfplane$:

::: pf-proof

Steps 2.1--2.4 build $v$ and compute its boundary values; the only analytic input is that $\arg$ is the imaginary part of a branch of $\log$.

::: pf-step

For $w \in \halfplane$, let $\arg(w) = \operatorname{Im}(\log w) \in (0, \pi)$ and $\arg(w - 1) = \operatorname{Im}(\log(w - 1)) \in (0, \pi)$, where $\log$ denotes the principal branch of logarithm holomorphic on $\CC \setminus (-\infty, 0]$.

::: pf-proof

For $w\in\halfplane$ the principal argument lies in $(0,\pi)$, and $\log w=\ln\abs{w}+i\arg w$ with $\ln\abs{w}$ real, so $\arg w=\operatorname{Im}\log w$. The principal branch is holomorphic on $\CC\setminus(-\infty,0]$, and $\halfplane$ misses that cut. The set $\halfplane-1=\{w-1:w\in\halfplane\}$ is the upper half-plane shifted by $-1$, so it also misses $(-\infty,0]$; hence $\log(w-1)$ is defined on $\halfplane$ and its imaginary part, the principal argument of $w-1$, again lies in $(0,\pi)$.

:::

:::

::: pf-step

Both $\arg(w)$ and $\arg(w - 1)$ are real parts of holomorphic functions (namely $\operatorname{Re}(-i \log w)$), so they are harmonic on $\halfplane$.

::: pf-proof

$\arg w=\operatorname{Im}\log w=\operatorname{Re}(-i\log w)$, and likewise $\arg(w-1)=\operatorname{Re}(-i\log(w-1))$. By step 2.1 both $-i\log w$ and $-i\log(w-1)$ are holomorphic on $\halfplane$, and the real part of a holomorphic function is harmonic there.

:::

:::

::: pf-step

Define $v: \halfplane \to \RR$ by
$$v(w) = 1 - \frac{1}{\pi}\Big(\arg(w - 1) - \arg(w)\Big).$$
As a linear combination of harmonic functions, $v$ is harmonic on $\halfplane$.

::: pf-proof

$v$ is $1-\frac1\pi\arg(w-1)+\frac1\pi\arg w$, a real linear combination of the constant function $1$ and the two harmonic functions of step 2.2. Harmonic functions on an open set form a real vector space, since differentiation is linear, so $v$ is harmonic.

:::

:::

::: pf-step

Boundary limits of $v(u + iv)$ as $v \to 0^+$:
- For $u > 1$: $u > 0$ and $u - 1 > 0$, so $\arg(w) \to 0$ and $\arg(w - 1) \to 0$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(0 - 0) = 1$.
- For $0 < u < 1$: $u > 0$ and $u - 1 < 0$, so $\arg(w) \to 0$ and $\arg(w - 1) \to \pi$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(\pi - 0) = 0$.
- For $u < 0$: $u < 0$ and $u - 1 < 0$, so $\arg(w) \to \pi$ and $\arg(w - 1) \to \pi$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(\pi - \pi) = 1$.

::: pf-proof

The principal argument is continuous on $\CC\setminus(-\infty,0]$, and tends to $\pi$ at a point of $(-\infty,0)$ approached from the upper half-plane. So as $t\to0^+$ with $w=u+it$: for $u>1$ both $w$ and $w-1$ tend to points of the positive axis, where the principal argument is $0$; for $0<u<1$, $w\to u>0$ gives $\arg w\to0$ while $w-1\to u-1<0$ gives $\arg(w-1)\to\pi$; for $u<0$ both limits are negative reals, so both arguments tend to $\pi$. Substituting these three pairs into the formula of step 2.3 gives $1$, $0$ and $1$.

:::

:::

:::

:::

::: pf-step

Pullback to the quadrant $Q$:

::: pf-proof

Steps 3.1--3.2 place $u=v\circ F$ on the quadrant and show it is harmonic; step 3.3 reads off the boundary values from steps 1.3 and 2.4.

::: pf-step

Define $u: Q \to \RR$ by $u(z) = v(F(z)) = v(z^2)$.

::: pf-proof

By step 1.2 the map $F$ carries $Q$ into $\halfplane$, where $v$ is defined (step 2.3), so the composition $v\circ F$ is a real-valued function on $Q$.

:::

:::

::: pf-step

Since $F(z) = z^2$ is holomorphic on $Q$ and $v$ is harmonic on $\halfplane$, the composition $u = v \circ F$ is harmonic on $Q$.

::: pf-proof

By steps 2.1--2.3, $v=\operatorname{Re}g$ with $g=1-\frac1\pi(-i\log(w-1)+i\log w)$ holomorphic on $\halfplane$. Then $u=\operatorname{Re}(g\circ F)$, and $g\circ F$ is holomorphic on $Q$ as a composition of holomorphic maps (step 1.2); the real part of a holomorphic function is harmonic, so $u$ is harmonic.

:::

:::

::: pf-step

By the boundary correspondence established in step [](#s1){.pf-ref} and the boundary values of $v$ from step [](#s2){.pf-ref}:
- For $z = x \in (1, \infty)$, $z^2 = x^2 \in (1, \infty)$, so $u(x, 0) = 1$.
- For $z = x \in (0, 1)$, $z^2 = x^2 \in (0, 1)$, so $u(x, 0) = 0$.
- For $z = iy$ with $y > 0$, $z^2 = -y^2 \in (-\infty, 0)$, so $u(0, y) = 1$.

::: pf-proof

Step 1.3 sends $x>1$ to $x^2>1$, $x\in(0,1)$ to $x^2\in(0,1)$ and $iy$ to $-y^2<0$; step 2.4 gives the limits $1$, $0$, $1$ of $v$ at points of $(1,\infty)$, $(0,1)$ and $(-\infty,0)$. Since $z\mapsto z^2$ is continuous up to the boundary and $v$ is continuous on $\halfplane$ with those boundary limits, $u$ has the stated boundary values, and it is continuous up to $\partial Q\setminus\{0,1\}$.

:::

:::

:::

:::

::: pf-step

Conclusion:

::: pf-proof

The function
$$u(z) = 1 - \frac{1}{\pi}\Big(\arg(z^2 - 1) - \arg(z^2)\Big)$$
is harmonic in the first quadrant $Q$, extends continuously to $\partial Q \setminus \{0, 1\}$, and takes the required boundary values $1, 0, 1$.

:::

:::

:::
:::