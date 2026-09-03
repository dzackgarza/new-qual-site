---
schema: qual/card@1
id: E-EG3W7
kind: problem
title: Isolated zeros of $f'$, and $f'=g'$ implies $f-g$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
  - Identity Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Let $\Omega \subseteq \mathbb{C}$ be a connected open region.
(1) Prove that if $f: \Omega \to \mathbb{C}$ is a non-constant holomorphic function, then $f'$ is holomorphic on $\Omega$ and the zeros of $f'$ are **isolated** in $\Omega$.
(2) Prove that if $f, g: \Omega \to \mathbb{C}$ are holomorphic functions satisfying $f'(z) = g'(z)$ for all $z \in \Omega$, then $f(z) - g(z) = C$ for some constant $C \in \mathbb{C}$.
:::

::: solution
**Goal:** Prove that derivatives of holomorphic functions are holomorphic, that non-zero holomorphic functions have isolated zeros, and that vanishing derivative on a connected domain implies constancy.

<1>1. Holomorphicity of $f'$:
    *Proof:*
    <2>1. By Cauchy's Integral Formula, any holomorphic function $f$ on an open set $\Omega$ is **infinitely complex differentiable** ($f \in C^\infty(\Omega)$).
    <2>2. In particular, $f'$ is itself a holomorphic function on $\Omega$.

<1>2. Proof that Zeros of $f'$ are Isolated:
    *Proof:*
    <2>1. Let $Z(f') = \{z \in \Omega \mid f'(z) = 0\}$ be the set of zeros of $f'$.
    <2>2. Suppose, for contradiction, that $Z(f')$ has an accumulation point $z_0 \in \Omega$.
    <2>3. By the **Identity Theorem for Holomorphic Functions**, since $f'$ is holomorphic on the connected region $\Omega$ and its zero set $Z(f')$ accumulates in $\Omega$, $f'$ must vanish identically on $\Omega$:
        $$f'(z) = 0 \quad \text{for all } z \in \Omega.$$
    <2>4. If $f'(z) = 0$ everywhere on connected $\Omega$, then for any two points $a, b \in \Omega$, connecting them by a smooth path $\gamma \subset \Omega$:
        $$f(b) - f(a) = \int_\gamma f'(z) \, dz = \int_\gamma 0 \, dz = 0 \implies f(b) = f(a).$$
    <2>5. Thus $f$ is a constant function on $\Omega$.
    <2>6. But this contradicts the hypothesis that $f$ is **non-constant**!
    <2>7. Therefore, the zero set $Z(f')$ cannot have any accumulation points in $\Omega$, meaning all zeros of $f'$ are **isolated**.

<1>3. Proof that $f' = g' \implies f - g$ is Constant:
    *Proof:*
    <2>1. Let $h(z) = f(z) - g(z)$.
    <2>2. Since $f$ and $g$ are holomorphic on $\Omega$, $h$ is holomorphic on $\Omega$, and:
        $$h'(z) = f'(z) - g'(z) = 0 \quad \text{for all } z \in \Omega.$$
    <2>3. Write $h(z) = u(x, y) + i v(x, y)$ in terms of real and imaginary parts.
    <2>4. The complex derivative satisfies:
        $$h'(z) = \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i \frac{\partial u}{\partial y} = 0.$$
    <2>5. Thus all first partial derivatives of $u$ and $v$ vanish identically on $\Omega$:
        $$\frac{\partial u}{\partial x} = \frac{\partial u}{\partial y} = \frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} = 0.$$
    <2>6. Since $\Omega$ is **connected** (and hence path-connected), any function with vanishing gradient is constant on $\Omega$.
    <2>7. Therefore, $u(x, y) = c_1$ and $v(x, y) = c_2$ are constant, so $h(z) = c_1 + i c_2 = C$ is constant.
    <2>8. Thus $f(z) - g(z) = C$ for all $z \in \Omega$.

<1>4. Conclusion:
    Derivatives of non-constant functions have isolated zeros by the Identity Theorem, and $f' = g'$ implies $f - g = C$ by path integration / gradient vanishing. Q.E.D.
:::
