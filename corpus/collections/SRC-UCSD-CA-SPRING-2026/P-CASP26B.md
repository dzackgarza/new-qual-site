---
schema: qual/card@1
id: P-CASP26B
kind: problem
title: '$\abs{f(z)}\leq 2000\abs z^2$ for an even holomorphic $f$ on $\DD$ with $f(0)=0$ and $\abs f<2000$'
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic such that (i) $f(0) = 0$, (ii) $\abs{f(z)} < 2000$ for all $z \in \DD$, (iii) $f(z) = f(-z)$ for all $z \in \DD$.

Show that $\abs{f(z)} \leq 2000\abs{z}^2$ for all $z \in \DD$, and determine when equality holds.
:::

::: {.solution}

::: pf

::: pf-step

Power series expansion and order of zero at the origin:

::: pf-proof

::: pf-step

Since $f: \DD \to \CC$ is holomorphic, it admits a power series expansion around 0:
$$
f(z) = \sum_{n=0}^\infty a_n z^n.
$$

::: pf-proof

Taylor expansion for holomorphic functions on the unit disk.

:::

:::

::: pf-step

Condition (i) gives $a_0 = f(0) = 0$.
Condition (iii) $f(z) = f(-z)$ means $f$ is an even function, so $a_n = 0$ for all odd $n$.
In particular, $a_1 = 0$.

::: pf-proof

uniqueness of power series coefficients for even functions.

:::

:::

::: pf-step

Therefore $f(z) = z^2 g(z)$, where $g(z) = \sum_{k=0}^\infty a_{2k+2} z^{2k}$ is holomorphic on $\DD$.

::: pf-proof

dividing by $z^2$.

:::

:::

:::

:::

::: {.pf-step #s2}

Proof of the bound $\abs{f(z)} \le 2000 \abs{z}^2$:

::: pf-proof

::: pf-step

For any $0 < r < 1$ and any $z$ with $\abs{z} = r$:
$$
\abs{g(z)} = \frac{\abs{f(z)}}{\abs{z}^2} = \frac{\abs{f(z)}}{r^2} < \frac{2000}{r^2}.
$$

::: pf-proof

condition (ii) $\abs{f(z)} < 2000$.

:::

:::

::: pf-step

By the Maximum Modulus Principle applied to $g$ on the closed disk $\overline{D}(0, r)$, for all $z \in D(0, r)$:
$$
\abs{g(z)} \le \max_{\abs{w} = r} \abs{g(w)} \le \frac{2000}{r^2}.
$$

::: pf-proof

Maximum Modulus Principle.

:::

:::

::: {.pf-step #s2-3}

Taking the limit as $r \to 1^-$ yields:
$$
\abs{g(z)} \le 2000 \quad \text{for all } z \in \DD.
$$

::: pf-proof

limit of upper bounds as $r \to 1^-$.

:::

:::

::: pf-step

Multiplying by $\abs{z}^2$:
$$
\abs{f(z)} = \abs{z^2 g(z)} = \abs{z}^2 \abs{g(z)} \le 2000 \abs{z}^2 \quad \text{for all } z \in \DD.
$$

::: pf-proof

Step [](#s2-3){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s3}

Characterization of equality:

::: pf-proof

::: pf-step

Suppose equality $\abs{f(z_0)} = 2000 \abs{z_0}^2$ holds for some non-zero $z_0 \in \DD \setminus \{0\}$.
Then $\abs{g(z_0)} = 2000$.

::: pf-proof

$\abs{f(z_0)} = \abs{z_0}^2 \abs{g(z_0)}$.

:::

:::

::: pf-step

Since $\abs{g(z)} \le 2000$ throughout $\DD$, the modulus $\abs{g}$ attains its global maximum at the interior point $z_0 \in \DD$.
By the Maximum Modulus Principle, $g(z)$ must be constant:
$$
g(z) = 2000 e^{i\theta} \quad \text{for some constant } \theta \in \RR.
$$

::: pf-proof

Maximum Modulus Principle forces constant functions.

:::

:::

::: pf-step

Consequently, $f(z) = 2000 e^{i\theta} z^2$.
Notice that for this function, $\abs{f(z)} = 2000 \abs{z}^2 < 2000$ holds strictly for all $z \in \DD$, and $f(z) = f(-z)$ and $f(0) = 0$ are satisfied.

::: pf-proof

$\abs{z} < 1 \implies 2000\abs{z}^2 < 2000$.

:::

:::

:::

:::

::: pf-step

Conclusion:
$\abs{f(z)} \le 2000 \abs{z}^2$ for all $z \in \DD$, with equality at any non-zero point if and only if $f(z) = 2000 e^{i\theta} z^2$ for some $\theta \in [0, 2\pi)$. Q.E.D.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
