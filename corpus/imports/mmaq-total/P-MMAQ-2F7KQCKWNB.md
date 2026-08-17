---
schema: qual/card@1
id: P-MMAQ-2F7KQCKWNB
kind: problem
title: Non-integrability of $\frac{xy}{(x^2+y^2)^2}$ on $[-1,1]^2$
classification:
  areas:
  - real-analysis
  topics:
  - l1
relations: []
review: draft
solved: true
---

::: problem
Let $f(x, y)$ on $[-1, 1]^2$ be defined by
$$
f(x, y) = \begin{cases}
\frac{x y}{\left(x^{2}+y^{2}\right)^{2}} & (x, y) \neq (0, 0) \\
0 & (x, y) = (0, 0)
\end{cases}
$$
Determine if $f$ is integrable.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Determine whether the function $f(x, y) = \frac{xy}{(x^2+y^2)^2}$ (with $f(0, 0)=0$) is Lebesgue integrable on $Q = [-1, 1]^2$.

<1>1. **Definition of Lebesgue Integrability.**
  <2>1. By definition, a measurable function $f: Q \to \RR$ is Lebesgue integrable ($f \in L^1(Q)$) if and only if $\int_Q |f(x, y)|\,d(x, y) < \infty$.
    Proof: This is the standard definition of Lebesgue integrability for real-valued functions on a measure space.

<1>2. **Lower bound on $\int_Q |f|\,d(x, y)$ via polar coordinates on the unit disk.**
  <2>1. The closed unit disk $D = \{(x, y) \in \RR^2 : x^2 + y^2 \leq 1\}$ is a measurable subset of $Q = [-1, 1]^2$.
    Proof: For every $(x, y) \in D$, $x^2 \leq x^2+y^2 \leq 1 \implies |x| \leq 1$, and similarly $|y| \leq 1$. Thus $D \subseteq Q$.
  <2>2. $\int_Q |f(x, y)|\,d(x, y) \geq \int_D |f(x, y)|\,d(x, y)$.
    Proof: By monotonicity of the Lebesgue integral for non-negative functions, since $|f| \geq 0$ and $D \subseteq Q$.
  <2>3. In polar coordinates $x = r\cos\theta, y = r\sin\theta$ on $D \setminus \{(0, 0)\}$:
    $$
    |f(r\cos\theta, r\sin\theta)| = \frac{|r^2\cos\theta\sin\theta|}{r^4} = \frac{|\sin(2\theta)|}{2r^2}.
    $$
    Proof: $x^2+y^2 = r^2$, and $xy = r^2\cos\theta\sin\theta = \frac{1}{2}r^2\sin(2\theta)$.
  <2>4. Compute the integral over $D$:
    $$
    \int_D |f(x, y)|\,d(x, y) = \int_0^{2\pi} \int_0^1 \frac{|\sin(2\theta)|}{2r^2} \cdot r\,dr\,d\theta = \left(\int_0^{2\pi} \frac{|\sin(2\theta)|}{2}\,d\theta\right) \left(\int_0^1 \frac{1}{r}\,dr\right).
    $$
    Proof: By Tonelli's Theorem for non-negative measurable functions under the smooth polar coordinate transformation (valid off the measure-zero origin).
  <2>5. The angular integral is strictly positive:
    $$
    \int_0^{2\pi} \frac{|\sin(2\theta)|}{2}\,d\theta = 4 \int_0^{\pi/2} \frac{\sin(2\theta)}{2}\,d\theta = 4 \left[ -\frac{\cos(2\theta)}{4} \right]_0^{\pi/2} = 4 \left( \frac{1}{4} + \frac{1}{4} \right) = 2.
    $$
  <2>6. The radial integral diverges:
    $$
    \int_0^1 \frac{1}{r}\,dr = \lim_{\eps \to 0^+} \int_\eps^1 \frac{1}{r}\,dr = \lim_{\eps \to 0^+} (-\ln\eps) = \infty.
    $$
  <2>7. $\int_D |f(x, y)|\,d(x, y) = 2 \cdot \infty = \infty$.
    Proof: Product of a positive constant and an infinite integral.

<1>3. **Conclusion.**
  Since $\int_{[-1, 1]^2} |f(x, y)|\,d(x, y) \geq \int_D |f(x, y)|\,d(x, y) = \infty$, the function $f$ is **not integrable** on $[-1, 1]^2$. Q.E.D.
:::
