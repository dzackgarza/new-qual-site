---
schema: qual/card@1
id: P-CAFA16F
kind: problem
title: "Infinite Blaschke product converges but cannot be extended past the boundary"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For $k \geq 1$, let $a_k = 1 - 1/k^2$.
For $n \geq 1$, define $f_n: \mathbb{D} \to \mathbb{D}$ by $f_n(z) = \prod_{k=1}^{n} \frac{a_k - z}{1 - a_k z}$.

(a) Prove that the sequence $\{f_n\}$ converges to an analytic function $f: \mathbb{D} \to \mathbb{D}$, uniformly on compact subsets of $\mathbb{D}$.

(b) Prove that there do not exist an open set $U \subset \mathbb{C}$ and an analytic function $g: U \to \mathbb{C}$ such that $\overline{\mathbb{D}} \subset U$ and $g(z) = f(z)$ for every $z \in \mathbb{D}$.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
Verify the Blaschke convergence condition:

::: pf-proof

::: pf-step
For $k = 1$, $a_1 = 1 - 1/1^2 = 0$.

::: pf-proof
definition.
:::

:::

::: pf-step
For $k \ge 2$, $0 < a_k = 1 - 1/k^2 < 1$.

::: pf-proof
$k \ge 2 \implies 0 < 1/k^2 \le 1/4$.
:::

:::

::: pf-step
$\sum_{k=1}^\infty (1 - a_k) = 1 + \sum_{k=2}^\infty \frac{1}{k^2} = 1 + \left(\frac{\pi^2}{6} - 1\right) = \frac{\pi^2}{6} < \infty$.

::: pf-proof
convergence of the $p$-series with $p = 2$.
:::

:::

:::

:::

::: pf-step
Show uniform convergence on compact subsets $K \subset \mathbb{D}$:

::: pf-proof

::: pf-step
Let $K \subset \mathbb{D}$ be a compact subset, and set $r = \sup_{z \in K} |z| < 1$.

::: pf-proof
compact subsets of the open unit disk are bounded away from the boundary.
:::

:::

::: pf-step
For each $k \ge 2$, write the Blaschke factor as $1 - u_k(z)$ where:
\[
u_k(z) = 1 - \frac{a_k - z}{1 - a_k z} = \frac{(1 - a_k z) - (a_k - z)}{1 - a_k z} = \frac{(1 - a_k)(1 + z)}{1 - a_k z}.
\]

::: pf-proof
algebraic identity.
:::

:::

::: {.pf-step #s2-3}
Bound $|u_k(z)|$ on $K$: for $z \in K$,
\[
|u_k(z)| \le \frac{(1 - a_k)(1 + |z|)}{1 - a_k |z|} \le \frac{1 - a_k}{1 - r} (1 + r) = \left(\frac{1+r}{1-r}\right) \frac{1}{k^2}.
\]

::: pf-proof
$|1 - a_k z| \ge 1 - a_k |z| \ge 1 - r$ and $|1+z| \le 1+|z| \le 1+r$.
:::

:::

::: pf-step
Since $\sum_{k=2}^\infty \frac{1}{k^2} < \infty$, the series $\sum_{k=2}^\infty |u_k(z)|$ converges uniformly on $K$ by the Weierstrass $M$-test.

::: pf-proof
step [](#s2-3){.pf-ref} and Weierstrass $M$-test.
:::

:::

::: pf-step
By the theorem on infinite products of analytic functions, the partial products $f_n(z) = -z \prod_{k=2}^n \frac{a_k - z}{1 - a_k z}$ converge uniformly on compact subsets of $\mathbb{D}$ to an analytic function $f: \mathbb{D} \to \mathbb{C}$.

::: pf-proof
uniform convergence of $\sum |u_k|$ implies uniform convergence of $\prod (1 - u_k)$.
:::

:::

:::

:::

::: {.pf-step #s3}
Show that $f(\mathbb{D}) \subset \mathbb{D}$:

::: pf-proof

::: pf-step
Each Blaschke factor $B_k(z) = \frac{a_k - z}{1 - a_k z}$ is a conformal automorphism of $\mathbb{D}$, so $|B_k(z)| < 1$ for all $z \in \mathbb{D}$.

::: pf-proof
properties of Möbius transformations of the disk.
:::

:::

::: pf-step
Thus $|f_n(z)| \le 1$ for all $z \in \mathbb{D}$ and all $n$, so $|f(z)| \le 1$ for all $z \in \mathbb{D}$.

::: pf-proof
limit of bounded functions.
:::

:::

::: pf-step
Since $f(a_k) = 0$ for each $k$, $f$ is not a constant unimodular function.

::: pf-proof
$f(0) = 0 \neq 1$.
:::

:::

::: pf-step
By the Maximum Modulus Principle, $|f(z)| < 1$ for all $z \in \mathbb{D}$, so $f: \mathbb{D} \to \mathbb{D}$.

::: pf-proof
open mapping theorem / maximum modulus principle for non-constant analytic functions.
:::

:::

:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #s4}
Assume for contradiction that there exist an open set $U \supset \overline{\mathbb{D}}$ and an analytic function $g: U \to \mathbb{C}$ such that $g(z) = f(z)$ for all $z \in \mathbb{D}$.

::: pf-proof
proof by contradiction assumption.
:::

:::

::: pf-step
Show that $z = 1$ is an accumulation point of zeros of $g$:

::: pf-proof

::: pf-step
For every $k \ge 1$, $a_k \in \mathbb{D}$, so $g(a_k) = f(a_k) = 0$.

::: pf-proof
step [](#s4){.pf-ref} and definition of $f$.
:::

:::

::: pf-step
The sequence of zeros $\{a_k\}_{k=1}^\infty$ satisfies $\lim_{k\to\infty} a_k = \lim_{k\to\infty} \left(1 - \frac{1}{k^2}\right) = 1$.

::: pf-proof
$\lim 1/k^2 = 0$.
:::

:::

::: pf-step
Since $1 \in \overline{\mathbb{D}} \subset U$, the point $z_0 = 1$ lies in $U$.

::: pf-proof
hypothesis $\overline{\mathbb{D}} \subset U$.
:::

:::

::: pf-step
$g$ is continuous at $z_0 = 1$, so $g(1) = \lim_{k\to\infty} g(a_k) = 0$.

::: pf-proof
continuity of analytic functions.
:::

:::

::: pf-step
The sequence of distinct zeros $\{a_k\}_{k=1}^\infty \subset U$ accumulates at $z_0 = 1 \in U$.

::: pf-proof
$a_k \neq 1$ for all $k$, and $a_k \to 1$.
:::

:::

:::

:::

::: {.pf-step #s6}
Apply the Identity Theorem:

::: pf-proof

::: pf-step
$U$ contains the connected open unit disk $\mathbb{D}$ and the point $1 \in \partial\mathbb{D}$.
Let $V \subseteq U$ be the connected component of $U$ containing $\mathbb{D}$.

::: pf-proof
$U$ is a neighborhood of the connected set $\overline{\mathbb{D}}$, so $\overline{\mathbb{D}}$ lies in a single connected component $V$.
:::

:::

::: pf-step
Since the zeros of $g$ in $V$ have an accumulation point $1 \in V$, the Identity Theorem implies $g(z) = 0$ identically on $V$.

::: pf-proof
Identity Theorem for analytic functions on a connected domain.
:::

:::

::: {.pf-step #s6-3}
Thus $f(z) = g(z) = 0$ for all $z \in \mathbb{D}$.

::: pf-proof
$\mathbb{D} \subset V$ and step [](#s4){.pf-ref}.
:::

:::

::: {.pf-step #s6-4}
However, the infinite Blaschke product $f(z)$ is not identically zero (it only vanishes at the isolated set $\{a_k\}$).

::: pf-proof
an infinite Blaschke product with convergent $\sum (1 - |a_k|)$ is non-trivial.
:::

:::

::: pf-step
This contradiction shows that no such analytic extension $g$ exists.

::: pf-proof
step [](#s6-3){.pf-ref} contradicts step [](#s6-4){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
step [](#s3){.pf-ref} (a) and step [](#s6){.pf-ref} (b).
:::

:::
:::
