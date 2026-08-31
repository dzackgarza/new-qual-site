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

::: problem
For $k \geq 1$, let $a_k = 1 - 1/k^2$.
For $n \geq 1$, define $f_n: \mathbb{D} \to \mathbb{D}$ by $f_n(z) = \prod_{k=1}^{n} \frac{a_k - z}{1 - a_k z}$.

(a) Prove that the sequence $\{f_n\}$ converges to an analytic function $f: \mathbb{D} \to \mathbb{D}$, uniformly on compact subsets of $\mathbb{D}$.

(b) Prove that there do not exist an open set $U \subset \mathbb{C}$ and an analytic function $g: U \to \mathbb{C}$ such that $\overline{\mathbb{D}} \subset U$ and $g(z) = f(z)$ for every $z \in \mathbb{D}$.
:::

::: {.solution}
**Part (a).**

<1>1. Verify the Blaschke convergence condition: <2>1. For $k = 1$, $a_1 = 1 - 1/1^2 = 0$.
::: {.proof}
definition.
:::
<2>2. For $k \ge 2$, $0 < a_k = 1 - 1/k^2 < 1$.
::: {.proof}
$k \ge 2 \implies 0 < 1/k^2 \le 1/4$.
:::
<2>3. $\sum_{k=1}^\infty (1 - a_k) = 1 + \sum_{k=2}^\infty \frac{1}{k^2} = 1 + \left(\frac{\pi^2}{6} - 1\right) = \frac{\pi^2}{6} < \infty$.
::: {.proof}
convergence of the $p$-series with $p = 2$.
:::

<1>2. Show uniform convergence on compact subsets $K \subset \mathbb{D}$: <2>1. Let $K \subset \mathbb{D}$ be a compact subset, and set $r = \sup_{z \in K} |z| < 1$.
::: {.proof}
compact subsets of the open unit disk are bounded away from the boundary.
:::
<2>2. For each $k \ge 2$, write the Blaschke factor as $1 - u_k(z)$ where:
\[
u_k(z) = 1 - \frac{a_k - z}{1 - a_k z} = \frac{(1 - a_k z) - (a_k - z)}{1 - a_k z} = \frac{(1 - a_k)(1 + z)}{1 - a_k z}.
\]
::: {.proof}
algebraic identity.
:::
<2>3. Bound $|u_k(z)|$ on $K$: for $z \in K$,
\[
|u_k(z)| \le \frac{(1 - a_k)(1 + |z|)}{1 - a_k |z|} \le \frac{1 - a_k}{1 - r} (1 + r) = \left(\frac{1+r}{1-r}\right) \frac{1}{k^2}.
\]
::: {.proof}
$|1 - a_k z| \ge 1 - a_k |z| \ge 1 - r$ and $|1+z| \le 1+|z| \le 1+r$.
:::
<2>4. Since $\sum_{k=2}^\infty \frac{1}{k^2} < \infty$, the series $\sum_{k=2}^\infty |u_k(z)|$ converges uniformly on $K$ by the Weierstrass $M$-test.
::: {.proof}
<2>3 and Weierstrass $M$-test.
:::
<2>5. By the theorem on infinite products of analytic functions, the partial products $f_n(z) = -z \prod_{k=2}^n \frac{a_k - z}{1 - a_k z}$ converge uniformly on compact subsets of $\mathbb{D}$ to an analytic function $f: \mathbb{D} \to \mathbb{C}$.
::: {.proof}
uniform convergence of $\sum |u_k|$ implies uniform convergence of $\prod (1 - u_k)$.
:::

<1>3. Show that $f(\mathbb{D}) \subset \mathbb{D}$: <2>1. Each Blaschke factor $B_k(z) = \frac{a_k - z}{1 - a_k z}$ is a conformal automorphism of $\mathbb{D}$, so $|B_k(z)| < 1$ for all $z \in \mathbb{D}$.
::: {.proof}
properties of Möbius transformations of the disk.
:::
<2>2. Thus $|f_n(z)| \le 1$ for all $z \in \mathbb{D}$ and all $n$, so $|f(z)| \le 1$ for all $z \in \mathbb{D}$.
::: {.proof}
limit of bounded functions.
:::
<2>3. Since $f(a_k) = 0$ for each $k$, $f$ is not a constant unimodular function.
::: {.proof}
$f(0) = 0 \neq 1$.
:::
<2>4. By the Maximum Modulus Principle, $|f(z)| < 1$ for all $z \in \mathbb{D}$, so $f: \mathbb{D} \to \mathbb{D}$.
::: {.proof}
open mapping theorem / maximum modulus principle for non-constant analytic functions.
:::

**Part (b).**

<1>4. Assume for contradiction that there exist an open set $U \supset \overline{\mathbb{D}}$ and an analytic function $g: U \to \mathbb{C}$ such that $g(z) = f(z)$ for all $z \in \mathbb{D}$.
::: {.proof}
proof by contradiction assumption.
:::

<1>5. Show that $z = 1$ is an accumulation point of zeros of $g$: <2>1. For every $k \ge 1$, $a_k \in \mathbb{D}$, so $g(a_k) = f(a_k) = 0$.
::: {.proof}
<1>4 and definition of $f$.
:::
<2>2. The sequence of zeros $\{a_k\}_{k=1}^\infty$ satisfies $\lim_{k\to\infty} a_k = \lim_{k\to\infty} \left(1 - \frac{1}{k^2}\right) = 1$.
::: {.proof}
$\lim 1/k^2 = 0$.
:::
<2>3. Since $1 \in \overline{\mathbb{D}} \subset U$, the point $z_0 = 1$ lies in $U$.
::: {.proof}
hypothesis $\overline{\mathbb{D}} \subset U$.
:::
<2>4. $g$ is continuous at $z_0 = 1$, so $g(1) = \lim_{k\to\infty} g(a_k) = 0$.
::: {.proof}
continuity of analytic functions.
:::
<2>5. The sequence of distinct zeros $\{a_k\}_{k=1}^\infty \subset U$ accumulates at $z_0 = 1 \in U$.
::: {.proof}
$a_k \neq 1$ for all $k$, and $a_k \to 1$.
:::

<1>6. Apply the Identity Theorem: <2>1. $U$ contains the connected open unit disk $\mathbb{D}$ and the point $1 \in \partial\mathbb{D}$.
Let $V \subseteq U$ be the connected component of $U$ containing $\mathbb{D}$.
::: {.proof}
$U$ is a neighborhood of the connected set $\overline{\mathbb{D}}$, so $\overline{\mathbb{D}}$ lies in a single connected component $V$.
:::
<2>2. Since the zeros of $g$ in $V$ have an accumulation point $1 \in V$, the Identity Theorem implies $g(z) = 0$ identically on $V$.
::: {.proof}
Identity Theorem for analytic functions on a connected domain.
:::
<2>3. Thus $f(z) = g(z) = 0$ for all $z \in \mathbb{D}$.
::: {.proof}
$\mathbb{D} \subset V$ and <1>4. <2>4. However, the infinite Blaschke product $f(z)$ is not identically zero (it only vanishes at the isolated set $\{a_k\}$).
::: {.proof}
an infinite Blaschke product with convergent $\sum (1 - |a_k|)$ is non-trivial.
:::
:::
<2>5. This contradiction shows that no such analytic extension $g$ exists.
::: {.proof}
<2>3 contradicts <2>4.
:::

<1>7. Q.E.D.
::: {.proof}
<1>3 (a) and <1>6 (b).
:::
:::
