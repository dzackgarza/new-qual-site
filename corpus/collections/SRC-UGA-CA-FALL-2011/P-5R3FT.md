---
schema: qual/card@1
id: P-5R3FT
kind: problem
title: Unique fixed point of $ce^z$ on $\{\operatorname{Re} z<1\}$ when $|c|<1/3$
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Rouché
  - Zeros
relations: []
review: draft
---

::: problem
Let $c \in \mathbb{C}$ with $|c| < \frac{1}{3}$. Show that on the open half-plane
$$
\Omega = \{z \in \mathbb{C} \mid \operatorname{Re}(z) < 1\},
$$
the function $f(z) = c e^z$ has exactly one fixed point.
:::

::: solution
**Goal:** Prove that $f(z) = c e^z$ has a unique fixed point in $\Omega = \{\operatorname{Re} z < 1\}$ by applying Rouché's Theorem on bounded truncated domains $\Omega_R$.

<1>1. Reformulation as a root-finding problem:
::: {.proof}
    <2>1. A point $z \in \Omega$ is a fixed point of $f$ if and only if $f(z) = z$, which is equivalent to $g(z) = 0$, where
    $$g(z) = c e^z - z.$$
    <2>2. Decompose $g(z) = F(z) + G(z)$, where $F(z) = -z$ and $G(z) = c e^z$.

:::

<1>2. Bounded domain $\Omega_R$ and its boundary:
::: {.proof}
    <2>1. For $R > 1$, define the bounded domain
    $$\Omega_R = \{z \in \mathbb{C} \mid |z| < R, \, \operatorname{Re}(z) < 1\}.$$
    <2>2. The boundary $\partial \Omega_R$ consists of two parts:
        - The vertical line segment $L_R = \{1 + i t \mid -\sqrt{R^2 - 1} \le t \le \sqrt{R^2 - 1}\}$.
        - The circular arc $C_R = \{R e^{i\theta} \mid \cos\theta \le 1/R\}$.

:::

<1>3. Rouché estimate on $\partial \Omega_R$:
::: {.proof}
    <2>1. Estimate on the vertical segment $L_R$:
        - For $z = 1 + i t \in L_R$, $\operatorname{Re}(z) = 1$.
        - $|G(z)| = |c e^{1 + i t}| = |c| e^1 < \frac{1}{3} \cdot e = \frac{e}{3}$.
        - Since $e < 3$, $\frac{e}{3} < 1$.
        - $|F(z)| = |z| = |1 + i t| = \sqrt{1 + t^2} \ge 1$.
        - Thus $|G(z)| < \frac{e}{3} < 1 \le |F(z)|$ on $L_R$.
    <2>2. Estimate on the circular arc $C_R$:
        - For $z \in C_R$, $|z| = R$ and $\operatorname{Re}(z) \le 1$.
        - $|G(z)| = |c e^z| = |c| e^{\operatorname{Re}(z)} \le |c| e^1 < \frac{e}{3} < 1$.
        - $|F(z)| = |z| = R > 1$.
        - Thus $|G(z)| < \frac{e}{3} < 1 < R = |F(z)|$ on $C_R$.
    <2>3. Therefore, $|G(z)| < |F(z)|$ holds strictly at every point $z \in \partial \Omega_R$.

:::

<1>4. Counting zeros:
::: {.proof}
    <2>1. Both $F(z) = -z$ and $G(z) = c e^z$ are holomorphic on and inside the bounded domain $\Omega_R$.
    <2>2. By Rouché's Theorem, $g(z) = F(z) + G(z) = c e^z - z$ and $F(z) = -z$ have the same number of zeros inside $\Omega_R$, counted with multiplicity.
    <2>3. $F(z) = -z$ has exactly one simple zero inside $\Omega_R$ (at $z = 0$, since $|0| = 0 < R$ and $\operatorname{Re}(0) = 0 < 1$).
    <2>4. Thus $g(z)$ has exactly one zero inside $\Omega_R$.

:::

<1>5. Extension to the full half-plane $\Omega$:
::: {.proof}
    <2>1. If $z_0 \in \Omega$ is any zero of $g(z) = c e^z - z$, then $|z_0| = |c e^{z_0}| = |c| e^{\operatorname{Re}(z_0)} < \frac{e}{3} < 1$.
    <2>2. Thus any zero $z_0 \in \Omega$ must satisfy $|z_0| < 1$, and therefore $z_0 \in \Omega_R$ for every $R > 1$.
    <2>3. Since $g(z)$ has exactly one zero in $\Omega_R$ for any $R > 1$, that single zero is the unique zero of $g(z)$ in all of $\Omega = \{\operatorname{Re}(z) < 1\}$.
    <2>4. Hence $f(z) = c e^z$ has exactly one fixed point in $\Omega$.

:::

<1>6. Conclusion:
::: {.proof}
    $f(z) = c e^z$ has a unique fixed point in $\{\operatorname{Re}(z) < 1\}$.
:::
:::

