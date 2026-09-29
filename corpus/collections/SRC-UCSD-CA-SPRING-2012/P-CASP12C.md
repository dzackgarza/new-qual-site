---
schema: qual/card@1
id: P-CASP12C
kind: problem
title: "Schwarz lemma type inequality for f(z) + f(-z)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $f: \mathbb{D} \to \mathbb{D}$ be an analytic function satisfying $f(0) = 0$.
Prove that $$|f(z) + f(-z)| \leq 2|z|^2$$ for all $z \in \mathbb{D}$.
Further, show that this inequality is strict for all $z \in \mathbb{D} \setminus \{0\}$ unless $f(z) + f(-z) = 2cz^2$ for some $c \in \mathbb{C}$ with $|c| = 1$.
:::

::: {.solution}
**Goal.** Prove $|f(z) + f(-z)| \le 2|z|^2$ and characterize equality.

::: pf

::: pf-step
Write $f(z) = \sum_{n=1}^\infty a_n z^n$ (since $f(0) = 0$).

::: pf-proof
Taylor expansion of $f$ at $0$.
:::

:::

::: pf-step
$f(z) + f(-z) = 2\sum_{k=1}^\infty a_{2k} z^{2k}$ (the odd terms cancel).

::: pf-proof
$f(-z) = \sum a_n (-z)^n$, so $f(z) + f(-z) = \sum a_n (1 + (-1)^n) z^n = 2\sum a_{2k} z^{2k}$.
:::

:::

::: {.pf-step #s3}
Define $g(z) = \frac{f(z) + f(-z)}{2z^2} = \sum_{k=1}^\infty a_{2k} z^{2k-2}$.

::: pf-proof
divide by $2z^2$; $g$ is holomorphic on $\DD$ (the series starts at $k=1$, so $g$ is well-defined at $0$).
:::

:::

::: pf-step
$g: \DD \to \DD$ (a holomorphic self-map of the disk).

::: pf-proof

::: pf-step
$g$ is holomorphic on $\DD$.

::: pf-proof
step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s4-2}
$|g(z)| \le 1$ for all $z \in \DD$.

::: pf-proof
for $|z| = r < 1$, $|g(z)| = \frac{|f(z)+f(-z)|}{2r^2} \le \frac{|f(z)|+|f(-z)|}{2r^2} < \frac{2}{2r^2} = \frac{1}{r^2}$; by the maximum modulus principle on $|z| \le r$ and letting $r \to 1^-$, $|g(z)| \le 1$.
:::

:::

:::

:::

::: {.pf-step #s5}
Hence $|f(z) + f(-z)| = 2|z|^2 |g(z)| \le 2|z|^2$.

::: pf-proof
step [](#s4-2){.pf-ref}.
:::

:::

::: {.pf-step #s6}
Equality case.

::: pf-proof

::: pf-step
If $|f(z) + f(-z)| = 2|z|^2$ for some $z \neq 0$, then $|g(z)| = 1$ for that $z$.

::: pf-proof
$|f(z)+f(-z)| = 2|z|^2|g(z)| = 2|z|^2$ forces $|g(z)| = 1$.
:::

:::

::: pf-step
By the maximum modulus principle, $|g(z)| = 1$ at an interior point forces $g$ to be constant of modulus $1$.

::: pf-proof
a holomorphic function attaining its maximum modulus at an interior point is constant.
:::

:::

::: pf-step
Hence $g \equiv c$ with $|c| = 1$, so $f(z) + f(-z) = 2cz^2$.

::: pf-proof
$f(z) + f(-z) = 2z^2 g(z) = 2cz^2$.
:::

:::

:::

:::

::: pf-qed
step [](#s5){.pf-ref} gives the inequality; step [](#s6){.pf-ref} gives the equality case.
:::

:::
:::
