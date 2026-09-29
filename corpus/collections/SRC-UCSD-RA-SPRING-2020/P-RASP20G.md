---
schema: qual/card@1
id: P-RASP20G
kind: problem
title: "Weakly sequentially closed convex sets and intersection properties"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 7 of the official UCSD Spring 2020 real-analysis qualifying exam. Restored the source's omitted boundedness hypothesis in part (2).
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Repaired the circular boundedness step in the projection argument and normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $H$ be a real Hilbert space.
Recall: If $K$ is a nonempty, closed, and convex subset of $H$, and $x \in H \setminus K$, then there exists a unique $y \in K$ such that $\|x - y\| = \min_{z \in K} \|x - z\|$.
Moreover, $\langle x - y, z - y \rangle \leq 0$ for all $z \in K$.

(1) Let $K$ be a nonempty, closed, and convex subset of $H$.
Prove that $K$ is weakly sequentially closed, i.e., if $u_n \in K$ ($n = 1, 2, \ldots$) and $u \in H$ satisfy that $u_n \to u$ weakly, then $u \in K$.

(2) Let $K_n$ ($n = 1, 2, \ldots$) be a decreasing sequence of nonempty, bounded, closed, and convex subsets of $H$ (i.e., $K_{n+1} \subseteq K_n$ for all $n$). Prove that $\bigcap_{n=1}^{\infty} K_n \neq \emptyset$.
:::

::: {.solution}
**Part (1).**

::: pf

::: pf-step
Let $u_n \in K$ ($n = 1, 2, \ldots$) with $u_n \rightharpoonup u$ weakly in $H$.

::: pf-proof
setup.
:::

:::

::: {.pf-step #s2}
Assume for contradiction that $u \notin K$.

::: pf-proof
proof by contradiction assumption.
:::

:::

::: pf-step
Since $K$ is non-empty, closed, and convex, let $y = P_K(u) \in K$ be the unique closest point projection of $u$ onto $K$.

::: pf-proof
Hilbert projection theorem for closed convex sets.
:::

:::

::: {.pf-step #s4}
By the characterization of the projection:
\[
\langle u - y, z - y \rangle \le 0 \quad \text{for all } z \in K.
\]

::: pf-proof
recall statement in the problem.
:::

:::

::: {.pf-step #s5}
Setting $z = u_n \in K$ yields:
\[
\langle u - y, u_n - y \rangle \le 0 \quad \text{for all } n \ge 1.
\]

::: pf-proof
step [](#s4){.pf-ref} with $z = u_n$.
:::

:::

::: pf-step
Take the limit as $n \to \infty$:

::: pf-proof

::: pf-step
The vector $u - y \in H$ defines a continuous linear functional $\langle u - y, \cdot \rangle$ on $H$.

::: pf-proof
Riesz representation / inner product properties.
:::

:::

::: pf-step
Since $u_n \rightharpoonup u$ weakly, $u_n - y \rightharpoonup u - y$ weakly in $H$.

::: pf-proof
weak convergence is preserved under translation.
:::

:::

::: pf-step
Thus $\lim_{n\to\infty} \langle u - y, u_n - y \rangle = \langle u - y, u - y \rangle = \|u - y\|^2$.

::: pf-proof
definition of weak convergence.
:::

:::

::: pf-step
Since every term in the sequence is non-positive by step [](#s5){.pf-ref}, the limit satisfies $\|u - y\|^2 \le 0$.

::: pf-proof
limits preserve non-strict inequalities.
:::

:::

:::

:::

::: {.pf-step #s7}
Hence $\|u - y\| = 0 \implies u = y \in K$, contradicting $u \notin K$.

::: pf-proof
positive definiteness of the norm and step [](#s2){.pf-ref}.
:::

:::

::: {.pf-step #s8}
Therefore $u \in K$, proving that $K$ is weakly sequentially closed.

::: pf-proof
step [](#s2){.pf-ref} and step [](#s7){.pf-ref}.
:::

:::

:::

**Part (2).**

::: pf

::: pf-step
For each $n \ge 1$, let $x_n = P_{K_n}(0) \in K_n$ be the unique element of minimal norm in $K_n$.

::: pf-proof
Hilbert projection theorem applied to the closed convex set $K_n$ and $x = 0$.
:::

:::

::: {.pf-step #s10}
The characterization $\langle 0 - x_n, z - x_n \rangle \le 0$ for all $z \in K_n$ gives:
\[
\langle x_n, z \rangle \ge \|x_n\|^2 \quad \text{for all } z \in K_n.
\]

::: pf-proof
expanding the inner product $\langle -x_n, z - x_n \rangle = - \langle x_n, z \rangle + \|x_n\|^2 \le 0$.
:::

:::

::: {.pf-step #s11}
The sequence of norms $\{\|x_n\|\}$ is monotonically non-decreasing:

::: pf-proof

::: pf-step
For any $m \ge n$, $K_m \subseteq K_n$, so $x_m \in K_n$.

::: pf-proof
hypothesis that $\{K_n\}$ is a decreasing sequence.
:::

:::

::: {.pf-step #s11-2}
Setting $z = x_m$ in step [](#s10){.pf-ref} gives $\langle x_n, x_m \rangle \ge \|x_n\|^2$.

::: pf-proof
step [](#s10){.pf-ref} applied to $z = x_m \in K_n$.
:::

:::

::: pf-step
By the Cauchy–Schwarz inequality:
\[
\|x_n\|^2 \le \langle x_n, x_m \rangle \le \|x_n\| \|x_m\| \implies \|x_n\| \le \|x_m\|.
\]

::: pf-proof
Cauchy–Schwarz inequality in $H$.
:::

:::

:::

:::

::: {.pf-step #s12}
Bound the distance $\|x_m - x_n\|^2$ for $m \ge n$:
\[
\|x_m - x_n\|^2 = \|x_m\|^2 - 2\langle x_n, x_m \rangle + \|x_n\|^2 \le \|x_m\|^2 - 2\|x_n\|^2 + \|x_n\|^2 = \|x_m\|^2 - \|x_n\|^2.
\]

::: pf-proof
expanding the norm squared and using $\langle x_n, x_m \rangle \ge \|x_n\|^2$ from step [](#s11-2){.pf-ref}.
:::

:::

::: pf-step
$\{x_n\}$ is a Cauchy sequence in $H$:

::: pf-proof

::: {.pf-step #s13-1}
Since $x_n\in K_n\subseteq K_1$ for every $n$ and $K_1$ is bounded, the non-decreasing sequence $\{\|x_n\|\}$ is bounded above. Hence $L = \lim_{n\to\infty} \|x_n\| < \infty$ exists.

::: pf-proof
boundedness of $K_1$ and monotone convergence for real sequences.
:::

:::

::: {.pf-step #s13-2}
For $m \ge n$, $\|x_m - x_n\|^2 \le \|x_m\|^2 - \|x_n\|^2 \to L^2 - L^2 = 0$ as $n, m \to \infty$.

::: pf-proof
step [](#s12){.pf-ref} and step [](#s13-1){.pf-ref}.
:::

:::

::: pf-step
Thus $\{x_n\}$ is a Cauchy sequence.

::: pf-proof
step [](#s13-2){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Since $H$ is a complete Hilbert space, there exists $x^* \in H$ such that $\lim_{n\to\infty} x_n = x^*$ in norm.

::: pf-proof
completeness of Hilbert spaces.
:::

:::

::: {.pf-step #s15}
Show that $x^* \in \bigcap_{n=1}^\infty K_n$:

::: pf-proof

::: pf-step
Fix any integer $k \ge 1$.

::: pf-proof
arbitrary choice of index.
:::

:::

::: pf-step
For all $n \ge k$, $x_n \in K_n \subseteq K_k$.

::: pf-proof
nesting $K_{n+1} \subseteq K_n$.
:::

:::

::: {.pf-step #s15-3}
Since $K_k$ is closed in $H$, the limit of the tail sequence satisfies $x^* = \lim_{n\to\infty} x_n \in K_k$.

::: pf-proof
closed sets contain all their limit points.
:::

:::

::: pf-step
Since this holds for all $k \ge 1$, $x^* \in \bigcap_{k=1}^\infty K_k$.

::: pf-proof
step [](#s15-3){.pf-ref} for all $k$.
:::

:::

:::

:::

::: pf-qed
step [](#s8){.pf-ref} (1) and step [](#s15){.pf-ref} (2).
:::

:::
:::
