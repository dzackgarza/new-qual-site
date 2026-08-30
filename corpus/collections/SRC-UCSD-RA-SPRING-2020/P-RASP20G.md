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
---

::: problem
Let $H$ be a real Hilbert space.
Recall: If $K$ is a nonempty, closed, and convex subset of $H$, and $x \in H \setminus K$, then there exists a unique $y \in K$ such that $\|x - y\| = \min_{z \in K} \|x - z\|$.
Moreover, $\langle x - y, z - y \rangle \leq 0$ for all $z \in K$.

(1) Let $K$ be a nonempty, closed, and convex subset of $H$.
Prove that $K$ is weakly sequentially closed, i.e., if $u_n \in K$ ($n = 1, 2, \ldots$) and $u \in H$ satisfy that $u_n \to u$ weakly, then $u \in K$.

(2) Let $K_n$ ($n = 1, 2, \ldots$) be a decreasing sequence of nonempty, closed, and convex subsets of $H$ (i.e., $K_{n+1} \subseteq K_n$ for all $n$). Prove that $\bigcap_{n=1}^{\infty} K_n \neq \emptyset$.
:::

::: {.solution}
**Part (1).**

<1>1. Let $u_n \in K$ ($n = 1, 2, \ldots$) with $u_n \rightharpoonup u$ weakly in $H$.
Proof: setup.

<1>2. Assume for contradiction that $u \notin K$.
Proof: proof by contradiction assumption.

<1>3. Since $K$ is non-empty, closed, and convex, let $y = P_K(u) \in K$ be the unique closest point projection of $u$ onto $K$.
Proof: Hilbert projection theorem for closed convex sets.

<1>4. By the characterization of the projection:
\[
\langle u - y, z - y \rangle \le 0 \quad \text{for all } z \in K.
\]
Proof: recall statement in the problem.

<1>5. Setting $z = u_n \in K$ yields:
\[
\langle u - y, u_n - y \rangle \le 0 \quad \text{for all } n \ge 1.
\]
Proof: <1>4 with $z = u_n$.

<1>6. Take the limit as $n \to \infty$:
<2>1. The vector $u - y \in H$ defines a continuous linear functional $\langle u - y, \cdot \rangle$ on $H$.
Proof: Riesz representation / inner product properties.
<2>2. Since $u_n \rightharpoonup u$ weakly, $u_n - y \rightharpoonup u - y$ weakly in $H$.
Proof: weak convergence is preserved under translation.
<2>3. Thus $\lim_{n\to\infty} \langle u - y, u_n - y \rangle = \langle u - y, u - y \rangle = \|u - y\|^2$.
Proof: definition of weak convergence.
<2>4. Since every term in the sequence is non-positive by <1>5, the limit satisfies $\|u - y\|^2 \le 0$.
Proof: limits preserve non-strict inequalities.

<1>7. Hence $\|u - y\| = 0 \implies u = y \in K$, contradicting $u \notin K$.
Proof: positive definiteness of the norm and <1>2.

<1>8. Therefore $u \in K$, proving that $K$ is weakly sequentially closed.
Proof: <1>2 and <1>7.

**Part (2).**

<1>9. For each $n \ge 1$, let $x_n = P_{K_n}(0) \in K_n$ be the unique element of minimal norm in $K_n$.
Proof: Hilbert projection theorem applied to the closed convex set $K_n$ and $x = 0$.

<1>10. The characterization $\langle 0 - x_n, z - x_n \rangle \le 0$ for all $z \in K_n$ gives:
\[
\langle x_n, z \rangle \ge \|x_n\|^2 \quad \text{for all } z \in K_n.
\]
Proof: expanding the inner product $\langle -x_n, z - x_n \rangle = - \langle x_n, z \rangle + \|x_n\|^2 \le 0$.

<1>11. The sequence of norms $\{\|x_n\|\}$ is monotonically non-decreasing:
<2>1. For any $m \ge n$, $K_m \subseteq K_n$, so $x_m \in K_n$.
Proof: hypothesis that $\{K_n\}$ is a decreasing sequence.
<2>2. Setting $z = x_m$ in <1>10 gives $\langle x_n, x_m \rangle \ge \|x_n\|^2$.
Proof: <1>10 applied to $z = x_m \in K_n$.
<2>3. By the Cauchy–Schwarz inequality:
\[
\|x_n\|^2 \le \langle x_n, x_m \rangle \le \|x_n\| \|x_m\| \implies \|x_n\| \le \|x_m\|.
\]
Proof: Cauchy–Schwarz inequality in $H$.

<1>12. Bound the distance $\|x_m - x_n\|^2$ for $m \ge n$:
\[
\|x_m - x_n\|^2 = \|x_m\|^2 - 2\langle x_n, x_m \rangle + \|x_n\|^2 \le \|x_m\|^2 - 2\|x_n\|^2 + \|x_n\|^2 = \|x_m\|^2 - \|x_n\|^2.
\]
Proof: expanding the norm squared and using $\langle x_n, x_m \rangle \ge \|x_n\|^2$ from <2>2.

<1>13. $\{x_n\}$ is a Cauchy sequence in $H$:
<2>1. Since $\{\|x_n\|\}$ is non-decreasing and bounded above (by $\operatorname{dist}(0, \bigcap K_n) < \infty$), $L = \lim_{n\to\infty} \|x_n\| < \infty$ exists.
Proof: monotone convergence theorem for bounded sequences in $\mathbb{R}$.
<2>2. For $m \ge n$, $\|x_m - x_n\|^2 \le \|x_m\|^2 - \|x_n\|^2 \to L^2 - L^2 = 0$ as $n, m \to \infty$.
Proof: <1>12 and <2>1.
<2>3. Thus $\{x_n\}$ is a Cauchy sequence.
Proof: <2>2.

<1>14. Since $H$ is a complete Hilbert space, there exists $x^* \in H$ such that $\lim_{n\to\infty} x_n = x^*$ in norm.
Proof: completeness of Hilbert spaces.

<1>15. Show that $x^* \in \bigcap_{n=1}^\infty K_n$:
<2>1. Fix any integer $k \ge 1$.
Proof: arbitrary choice of index.
<2>2. For all $n \ge k$, $x_n \in K_n \subseteq K_k$.
Proof: nesting $K_{n+1} \subseteq K_n$.
<2>3. Since $K_k$ is closed in $H$, the limit of the tail sequence satisfies $x^* = \lim_{n\to\infty} x_n \in K_k$.
Proof: closed sets contain all their limit points.
<2>4. Since this holds for all $k \ge 1$, $x^* \in \bigcap_{k=1}^\infty K_k$.
Proof: <2>3 for all $k$.

<1>16. Conclusion:
$\bigcap_{n=1}^\infty K_n \neq \emptyset$. Q.E.D.
Proof: <1>8 (1) and <1>15 (2).
:::
