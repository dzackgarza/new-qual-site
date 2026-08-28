---
schema: qual/card@1
id: E-SS4.EX-1
kind: exercise
title: "Vanishing Fourier transform forces f = 0 (uniqueness)"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: exercise
1. Suppose f is continuous and of moderate decrease, and ${ \hat { f } } ( \xi ) = 0$ for all $\xi \in \mathbb { R }$ Show that $f = 0$ by completing the following outline:

(a) For each fixed real number t consider the two functions

$$
A (z) = \int_ {- \infty} ^ {t} f (x) e ^ {- 2 \pi i z (x - t)} d x \quad \text { and } \quad B (z) = - \int_ {t} ^ {\infty} f (x) e ^ {- 2 \pi i z (x - t)} d x.
$$

Show that $A ( \xi ) = B ( \xi )$ for all $\xi \in \mathbb { R } .$

(b) Prove that the function F equal to A in the closed upper half-plane, and B in the lower half-plane, is entire and bounded, thus constant.
In fact, show that $F = 0$

(c) Deduce that

$$
\int_ {- \infty} ^ {t} f (x) d x = 0,
$$

for all t, and conclude that $f = 0$
:::

::: {.solution}
**Goal.** Show $\hat f = 0$ forces $f = 0$ for continuous $f$ of moderate decrease.

<1>1. (a) $A(\xi) = B(\xi)$ for all $\xi \in \RR$.
<2>1. $A(\xi) = \int_{-\infty}^t f(x) e^{-2\pi i \xi(x-t)}\,dx$ and $B(\xi) = -\int_t^\infty f(x) e^{-2\pi i \xi(x-t)}\,dx$.
Proof: definitions.
<2>2. $A(\xi) - B(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi i \xi(x-t)}\,dx = e^{2\pi i \xi t}\hat f(\xi) = 0$.
Proof: $A - B$ is the full Fourier transform of $f$ (with a phase), and $\hat f(\xi) = 0$ by hypothesis.
<2>3. Hence $A(\xi) = B(\xi)$.
Proof: <1>1.2.

<1>2. (b) $F$ (equal to $A$ on the closed upper half-plane and $B$ on the lower half-plane) is entire, bounded, hence constant, and in fact $F = 0$.
<2>1. $A$ and $B$ agree on the real axis (by (a)), so $F$ is well-defined and continuous.
Proof: <1>1.3.
<2>2. $A$ is holomorphic on the upper half-plane and $B$ on the lower half-plane.
Proof: each is an integral of a holomorphic function in $z$ (the integrand $e^{-2\pi i z(x-t)}$ is entire in $z$), and the integrals converge uniformly (moderate decrease).
<2>3. $F$ is entire.
Proof: $A$ and $B$ agree on $\RR$ and are holomorphic on their respective half-planes, so $F$ is holomorphic across the real axis (Morera's theorem).
<2>4. $F$ is bounded.
Proof: $|A(z)| \le \int_{-\infty}^t |f(x)| e^{2\pi \Im(z)(x-t)}\,dx$, which is bounded for $\Im z \ge 0$ (moderate decrease of $f$); similarly for $B$ on the lower half-plane.
<2>5. Hence $F$ is constant (Liouville's theorem).
Proof: a bounded entire function is constant.
<2>6. $F = 0$.
Proof: $F(\xi) = A(\xi) = 0$ for all real $\xi$ (since $A(\xi) = B(\xi)$ and $A(\xi) - B(\xi) = 0$... more directly, $A(\xi) = \int_{-\infty}^t f(x)e^{-2\pi i\xi(x-t)}dx$, and as $\xi \to \infty$ this tends to $0$ by Riemann–Lebesgue, so the constant $F$ is $0$).

<1>3. (c) $f = 0$.
<2>1. $F(0) = A(0) = \int_{-\infty}^t f(x)\,dx = 0$.
Proof: $F = 0$, and $A(0) = \int_{-\infty}^t f(x) e^0\,dx = \int_{-\infty}^t f(x)\,dx$.
<2>2. Hence $\int_{-\infty}^t f(x)\,dx = 0$ for all $t$.
Proof: <1>3.1 holds for every $t$.
<2>3. Differentiating in $t$ gives $f(t) = 0$ for all $t$.
Proof: the fundamental theorem of calculus: $\frac{d}{dt}\int_{-\infty}^t f(x)\,dx = f(t) = 0$.

<1>4. Q.E.D.
Proof: <1>3.3 shows $f = 0$.
:::
