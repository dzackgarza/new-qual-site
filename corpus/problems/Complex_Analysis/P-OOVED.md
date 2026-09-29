---
schema: qual/card@1
id: P-OOVED
kind: problem
title: Holomorphic functions of modulus one on the circle are finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $f$ is analytic in an open set containing the unit disc $\mathbb D$ and $|f(z)| =1$ when $|z|$=1. Show that either $f(z) = e^{i \theta}$ for some $\theta \in \mathbb R$ or there are
finite number of $z_k \in \mathbb D$, $k \leq n$ and
$\theta \in \mathbb R$ such that
\[
\displaystyle f(z) = e^{i\theta} \prod_{k=1}^n \frac{z-z_k}{1 - \bar{z}_k z } \, .
.\]

> Also cf. Stein et al, 1.4.7, 3.8.17

:::

::: {.solution}

::: pf

::: pf-step

Finiteness of zeros in $\mathbb{D}$:

::: pf-proof

::: pf-step

Since $f$ is analytic on an open set containing the compact closure $\overline{\mathbb{D}}$, and $|f(z)| = 1$ on the boundary $\partial\mathbb{D} = \{|z| = 1\}$, $f$ cannot be identically zero and has no zeros on $\partial\mathbb{D}$.

::: pf-proof

$|f(z)| = 1 > 0$ on $\partial\mathbb{D}$.

:::

:::

::: pf-step

By the Identity Theorem, the zeros of $f$ in $\overline{\mathbb{D}}$ are isolated.
Since $\overline{\mathbb{D}}$ is compact, $f$ has only finitely many zeros $z_1, z_2, \ldots, z_n \in \mathbb{D}$ (counted with multiplicity).
(If $f$ has no zeros in $\mathbb{D}$, we take $n = 0$ and the empty product to be $1$).

::: pf-proof

zeros of non-constant holomorphic functions in a compact domain are finite.

:::

:::

:::

:::

::: {.pf-step #s2}

Properties of the Blaschke product:

::: pf-proof

::: pf-step

For each $k \in \{1, \dots, n\}$, define the Blaschke factor:
\[
B_k(z) = \frac{z - z_k}{1 - \overline{z_k} z}.
\]
For $|z| = 1$, write $z = e^{i\phi}$:
\[
|B_k(e^{i\phi})| = \left| \frac{e^{i\phi} - z_k}{1 - \overline{z_k} e^{i\phi}} \right| = \left| e^{i\phi} \frac{1 - z_k e^{-i\phi}}{1 - \overline{z_k} e^{i\phi}} \right| = 1 \cdot \frac{|1 - z_k e^{-i\phi}|}{|\overline{1 - z_k e^{-i\phi}}|} = 1.
\]

::: pf-proof

$|w| = |\overline{w}|$ for all $w \in \mathbb{C}$.

:::

:::

::: pf-step

Define the finite Blaschke product $B(z) = \prod_{k=1}^n B_k(z)$.
$B(z)$ is holomorphic on a neighborhood of $\overline{\mathbb{D}}$, satisfies $|B(z)| = 1$ for all $|z| = 1$, and has exactly the zeros $z_1, \dots, z_n$ in $\mathbb{D}$ with the same multiplicities as $f$.

::: pf-proof

product of Blaschke factors.

:::

:::

:::

:::

::: {.pf-step #s3}

Quotient function and Maximum Modulus Principle:

::: pf-proof

::: pf-step

Define $g(z) = \frac{f(z)}{B(z)}$.
Since the zeros of $B(z)$ cancel with the zeros of $f(z)$ in $\mathbb{D}$, all singularities of $g$ in $\mathbb{D}$ are removable.
Thus $g$ extends to a holomorphic function on a neighborhood of $\overline{\mathbb{D}}$ with $g(z) \neq 0$ for all $z \in \overline{\mathbb{D}}$.

::: pf-proof

Riemann Removable Singularity Theorem.

:::

:::

::: pf-step

On the boundary circle $|z| = 1$:
\[
|g(z)| = \frac{|f(z)|}{|B(z)|} = \frac{1}{1} = 1.
\]

::: pf-proof

$|f| = 1$ and $|B| = 1$ on $\partial\mathbb{D}$.

:::

:::

::: pf-step

By the Maximum Modulus Principle applied to $g(z)$:
\[
|g(z)| \le 1 \quad \text{for all } z \in \mathbb{D}.
\]

::: pf-proof

Maximum Modulus Principle.

:::

:::

::: pf-step

Since $g(z)$ has no zeros in $\overline{\mathbb{D}}$, the function $\frac{1}{g(z)}$ is holomorphic on $\overline{\mathbb{D}}$ and satisfies $\left|\frac{1}{g(z)}\right| = 1$ on $\partial\mathbb{D}$.
Applying the Maximum Modulus Principle to $\frac{1}{g(z)}$ yields:
\[
\left| \frac{1}{g(z)} \right| \le 1 \implies |g(z)| \ge 1 \quad \text{for all } z \in \mathbb{D}.
\]

::: pf-proof

Maximum Modulus Principle for reciprocal.

:::

:::

::: pf-step

Thus $|g(z)| = 1$ for all $z \in \mathbb{D}$.
A holomorphic function of constant modulus on a connected domain is constant:
\[
g(z) = c = e^{i\theta} \quad \text{for some } \theta \in \mathbb{R}.
\]

::: pf-proof

Cauchy–Riemann equations for constant-modulus holomorphic functions.

:::

:::

:::

:::

::: pf-step

Conclusion:
$f(z) = e^{i\theta} B(z) = e^{i\theta} \prod_{k=1}^n \frac{z - z_k}{1 - \overline{z_k} z}$. Q.E.D.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
