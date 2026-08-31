---
schema: qual/card@1
id: P-7Q5AM
kind: problem
title: The unit sphere of an infinite-dimensional Hilbert space is weakly dense in
  the unit ball, and operators of norm $1$ converging strongly to $0$
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $H$ be an infinite dimensional real Hilbert space.

a. Prove that the unit sphere $S=\{x\in H: ||x||=1\}$ is weakly dense in the unit ball $B=\{x\in H: ||x||\le 1\}$.

b. Prove there is a sequence $T_n$ of bounded linear operators from $H$ to $H$ such that $||T_n||=1$ for all $n$ but $\lim_{n\to\infty} T_n(x)=0$ for all $x\in H$.
:::

::: solution
**Goal:** Prove that the unit sphere $S$ of an infinite-dimensional real Hilbert space $H$ is weakly dense in the closed unit ball $B$ in (a), and construct operators $T_n$ with $\|T_n\| = 1$ converging strongly to 0 in (b).

<1>1. Part (a): Reduction to the open unit ball.
::: {.proof}
    <2>1. Let $x_0 \in B$, so $\|x_0\| \le 1$.
    <2>2. If $\|x_0\| = 1$, then $x_0 \in S$, so the constant sequence $x_n = x_0 \in S$ converges strongly (and hence weakly) to $x_0$.
    <2>3. Thus we may assume $\|x_0\| < 1$, which implies $c = \sqrt{1 - \|x_0\|^2} > 0$.

:::

<1>2. Part (a): Construction of an orthonormal sequence in $x_0^\perp$.
::: {.proof}
    <2>1. The orthogonal complement $x_0^\perp = \{v \in H : \langle x_0, v \rangle = 0\}$ is the kernel of the continuous linear functional $\langle x_0, \cdot \rangle$.
    <2>2. Since $x_0^\perp$ has codimension at most 1 in the infinite-dimensional space $H$, $x_0^\perp$ is infinite-dimensional.
    <2>3. Using the Gram–Schmidt process, choose a countable orthonormal sequence $\{e_n\}_{n=1}^\infty \subset x_0^\perp$, so $\langle e_n, e_m \rangle = \delta_{nm}$ and $\langle x_0, e_n \rangle = 0$ for all $n \ge 1$.

:::

<1>3. Part (a): Construction of the sequence on the unit sphere $S$.
::: {.proof}
    <2>1. For each $n \ge 1$, define $x_n = x_0 + c e_n = x_0 + \sqrt{1 - \|x_0\|^2} \, e_n$.
    <2>2. Compute the norm squared of $x_n$ using orthogonality $\langle x_0, e_n \rangle = 0$:
    $$\|x_n\|^2 = \|x_0 + c e_n\|^2 = \|x_0\|^2 + 2c \langle x_0, e_n \rangle + c^2 \|e_n\|^2 = \|x_0\|^2 + 0 + (1 - \|x_0\|^2)(1) = 1.$$
    <2>3. Therefore $\|x_n\| = 1$, so $x_n \in S$ for all $n \ge 1$.

:::

<1>4. Part (a): Weak convergence $x_n \rightharpoonup x_0$.
::: {.proof}
    <2>1. By the Riesz Representation Theorem, every continuous linear functional $\phi \in H^*$ is of the form $\phi(y) = \langle y, v \rangle$ for some $v \in H$.
    <2>2. For any fixed $v \in H$, Bessel's inequality for the orthonormal sequence $\{e_n\}$ gives
    $$\sum_{n=1}^\infty |\langle v, e_n \rangle|^2 \le \|v\|^2 < \infty.$$
    <2>3. Since the series converges, its terms tend to zero: $\lim_{n \to \infty} \langle v, e_n \rangle = 0$.
    <2>4. Evaluating $\phi(x_n)$:
    $$\lim_{n \to \infty} \langle x_n, v \rangle = \lim_{n \to \infty} \left( \langle x_0, v \rangle + c \langle e_n, v \rangle \right) = \langle x_0, v \rangle + c \cdot 0 = \langle x_0, v \rangle.$$
    <2>5. Since this holds for all $v \in H$, $x_n \rightharpoonup x_0$ weakly in $H$.
    <2>6. Thus every point of $B$ is in the weak closure of $S$, proving $S$ is weakly dense in $B$.

:::

<1>5. Part (b): Construction of rank-1 operators $T_n$.
::: {.proof}
    <2>1. Choose an orthonormal sequence $\{e_n\}_{n=1}^\infty$ in $H$, and fix a unit vector $u \in H$ with $\|u\| = 1$ (e.g. $u = e_1$).
    <2>2. Define $T_n: H \to H$ by $T_n(x) = \langle x, e_n \rangle u$ for all $x \in H$.
    <2>3. Linearity of $T_n$ follows directly from linearity of the inner product in the first argument:
    $$T_n(a x + b y) = \langle ax + by, e_n \rangle u = (a\langle x, e_n \rangle + b\langle y, e_n \rangle)u = a T_n(x) + b T_n(y).$$

:::

<1>6. Part (b): Operator norm $\|T_n\| = 1$.
::: {.proof}
    <2>1. For any $x \in H$, by the Cauchy–Schwarz inequality:
    $$\|T_n(x)\| = |\langle x, e_n \rangle| \|u\| = |\langle x, e_n \rangle| \le \|x\| \|e_n\| = \|x\|.$$
    <2>2. Thus $\|T_n\| \le 1$.
    <2>3. Evaluating at the unit vector $x = e_n$:
    $$\|T_n(e_n)\| = |\langle e_n, e_n \rangle| \|u\| = 1 \cdot 1 = 1 = \|e_n\|.$$
    <2>4. Therefore $\|T_n\| = 1$ for all $n \ge 1$.

:::

<1>7. Part (b): Strong convergence $T_n(x) \to 0$ for all $x \in H$.
::: {.proof}
    <2>1. For any fixed $x \in H$, Bessel's inequality gives $\sum_{n=1}^\infty |\langle x, e_n \rangle|^2 \le \|x\|^2 < \infty$.
    <2>2. Thus $\lim_{n \to \infty} |\langle x, e_n \rangle| = 0$.
    <2>3. Compute the norm of the operator value:
    $$\lim_{n \to \infty} \|T_n(x)\| = \lim_{n \to \infty} |\langle x, e_n \rangle| = 0.$$
    <2>4. Therefore $\lim_{n \to \infty} T_n(x) = 0$ in the norm topology of $H$ for every $x \in H$.

:::

<1>8. Conclusion:
::: {.proof}
    $S$ is weakly dense in $B$, and the operators $T_n(x) = \langle x, e_n \rangle u$ satisfy $\|T_n\| = 1$ for all $n$ while $T_n(x) \to 0$ for all $x \in H$.
:::
:::
