---
schema: qual/card@1
id: E-SS4.EX-1
kind: problem
title: A continuous function of moderate decrease with $\hat f=0$ vanishes
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
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

::: pf

::: pf-step
(a) $A(\xi) = B(\xi)$ for all $\xi \in \RR$.

::: pf-proof

::: pf-step
$A(\xi) = \int_{-\infty}^t f(x) e^{-2\pi i \xi(x-t)}\,dx$ and $B(\xi) = -\int_t^\infty f(x) e^{-2\pi i \xi(x-t)}\,dx$.

::: pf-proof
definitions.
:::

:::

::: {.pf-step #s1-2}
$A(\xi) - B(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi i \xi(x-t)}\,dx = e^{2\pi i \xi t}\hat f(\xi) = 0$.

::: pf-proof
$A - B$ is the full Fourier transform of $f$ (with a phase), and $\hat f(\xi) = 0$ by hypothesis.
:::

:::

::: {.pf-step #s1-3}
Hence $A(\xi) = B(\xi)$.

::: pf-proof
step [](#s1-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
(b) $F$ (equal to $A$ on the closed upper half-plane and $B$ on the lower half-plane) is entire, bounded, hence constant, and in fact $F = 0$.

::: pf-proof

::: pf-step
$A$ and $B$ agree on the real axis (by (a)), so $F$ is well-defined and continuous.

::: pf-proof
step [](#s1-3){.pf-ref}.
:::

:::

::: pf-step
$A$ is holomorphic on the upper half-plane and $B$ on the lower half-plane.

::: pf-proof
each is an integral of a holomorphic function in $z$ (the integrand $e^{-2\pi i z(x-t)}$ is entire in $z$), and the integrals converge uniformly (moderate decrease).
:::

:::

::: pf-step
$F$ is entire.

::: pf-proof
$A$ and $B$ agree on $\RR$ and are holomorphic on their respective half-planes, so $F$ is holomorphic across the real axis (Morera's theorem).
:::

:::

::: pf-step
$F$ is bounded.

::: pf-proof
$|A(z)| \le \int_{-\infty}^t |f(x)| e^{2\pi \Im(z)(x-t)}\,dx$, which is bounded for $\Im z \ge 0$ (moderate decrease of $f$); similarly for $B$ on the lower half-plane.
:::

:::

::: pf-step
Hence $F$ is constant (Liouville's theorem).

::: pf-proof
a bounded entire function is constant.
:::

:::

::: pf-step
$F = 0$.

::: pf-proof
$F(\xi) = A(\xi) = 0$ for all real $\xi$ (since $A(\xi) = B(\xi)$ and $A(\xi) - B(\xi) = 0$... more directly, $A(\xi) = \int_{-\infty}^t f(x)e^{-2\pi i\xi(x-t)}dx$, and as $\xi \to \infty$ this tends to $0$ by Riemann–Lebesgue, so the constant $F$ is $0$).
:::

:::

:::

:::

::: pf-step
(c) $f = 0$.

::: pf-proof

::: {.pf-step #s3-1}
$F(0) = A(0) = \int_{-\infty}^t f(x)\,dx = 0$.

::: pf-proof
$F = 0$, and $A(0) = \int_{-\infty}^t f(x) e^0\,dx = \int_{-\infty}^t f(x)\,dx$.
:::

:::

::: pf-step
Hence $\int_{-\infty}^t f(x)\,dx = 0$ for all $t$.

::: pf-proof
step [](#s3-1){.pf-ref} holds for every $t$.
:::

:::

::: {.pf-step #s3-3}
Differentiating in $t$ gives $f(t) = 0$ for all $t$.

::: pf-proof
the fundamental theorem of calculus: $\frac{d}{dt}\int_{-\infty}^t f(x)\,dx = f(t) = 0$.
:::

:::

:::

:::

::: pf-qed
step [](#s3-3){.pf-ref} shows $f = 0$.
:::

:::
:::
