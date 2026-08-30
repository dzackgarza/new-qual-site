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

::: {.solution}
**Part (a).**

<1>1. Let $x_0 \in B$, so $\|x_0\| \le 1$.
We construct a sequence $\{x_n\} \subset S$ such that $x_n \rightharpoonup x_0$ weakly.
Proof: setup.

<1>2. If $\|x_0\| = 1$, then $x_0 \in S$, so the constant sequence $x_n = x_0$ lies in $S$ and converges weakly to $x_0$.
Proof: constant sequence is in $S$.

<1>3. Suppose $\|x_0\| < 1$.
Let $c = \sqrt{1 - \|x_0\|^2} > 0$.
Proof: $\|x_0\| < 1 \implies 1 - \|x_0\|^2 > 0$.

<1>4. Construct an orthonormal sequence $\{e_n\}_{n=1}^\infty$ in $x_0^\perp$: <2>1. The orthogonal complement $x_0^\perp = \{v \in H : \langle x_0, v \rangle = 0\}$ is a closed subspace of codimension at most 1. Proof: kernel of the continuous linear functional $\langle x_0, \cdot \rangle$.
<2>2. Since $H$ is infinite-dimensional, $x_0^\perp$ is infinite-dimensional.
Proof: codimension $\le 1$ in an infinite-dimensional space.
<2>3. Choose a countably infinite orthonormal sequence $\{e_n\}_{n=1}^\infty \subset x_0^\perp$ by the Gram–Schmidt process.
Proof: existence of infinite orthonormal sequences in infinite-dimensional inner product spaces.

<1>5. Define $x_n = x_0 + c e_n$ for each $n \ge 1$.
<2>1. Compute the norm of $x_n$:
\[
\|x_n\|^2 = \langle x_0 + c e_n, x_0 + c e_n \rangle = \|x_0\|^2 + 2c \langle x_0, e_n \rangle + c^2 \|e_n\|^2.
\]
Proof: expansion of the inner product norm.
<2>2. Since $e_n \in x_0^\perp$ and $\|e_n\| = 1$:
\[
\|x_n\|^2 = \|x_0\|^2 + 0 + c^2 = \|x_0\|^2 + (1 - \|x_0\|^2) = 1.
\]
Proof: <1>3 and <1>4. <2>3. Thus $x_n \in S$ for all $n \ge 1$.
Proof: <2>2.

<1>6. The sequence $x_n \rightharpoonup x_0$ weakly: <2>1. By the Riesz Representation Theorem, any continuous linear functional on $H$ is of the form $y \mapsto \langle y, v \rangle$ for some $v \in H$.
Proof: Riesz Representation Theorem for Hilbert spaces.
<2>2. For any $v \in H$, by Bessel's inequality:
\[
\sum_{n=1}^\infty |\langle v, e_n \rangle|^2 \le \|v\|^2 < \infty.
\]
Proof: Bessel's inequality for orthonormal sequences.
<2>3. Hence $\lim_{n\to\infty} \langle v, e_n \rangle = 0$.
Proof: terms of a convergent series tend to zero.
<2>4. Compute the inner product with $v$:
\[
\lim_{n\to\infty} \langle x_n, v \rangle = \lim_{n\to\infty} \bigl(\langle x_0, v \rangle + c \langle e_n, v \rangle\bigr) = \langle x_0, v \rangle + c \cdot 0 = \langle x_0, v \rangle.
\]
Proof: linearity of inner product and <2>3. <2>5. Thus $x_n \rightharpoonup x_0$ weakly in $H$.
Proof: definition of weak convergence.

<1>7. Hence every point of $B$ is in the weak closure of $S$, so $S$ is weakly dense in $B$.
Proof: <1>2 and <1>6.

**Part (b).**

<1>8. Choose an orthonormal sequence $\{e_n\}_{n=1}^\infty$ in $H$, and fix a unit vector $u = e_1 \in H$.
Proof: $H$ is infinite-dimensional.

<1>9. Define the operators $T_n: H \to H$ by $T_n(x) = \langle x, e_n \rangle u$ for all $x \in H$.
<2>1. $T_n$ is linear: $T_n(ax + by) = \langle ax + by, e_n \rangle u = (a\langle x, e_n \rangle + b\langle y, e_n \rangle)u = a T_n(x) + b T_n(y)$.
Proof: linearity of the inner product in the first slot.
<2>2. Bound the operator norm: for any $x \in H$,
\[
\|T_n(x)\| = |\langle x, e_n \rangle| \|u\| = |\langle x, e_n \rangle| \le \|x\| \|e_n\| = \|x\|.
\]
Proof: Cauchy–Schwarz inequality and $\|u\| = \|e_n\| = 1$.
<2>3. For $x = e_n$, $\|T_n(e_n)\| = |\langle e_n, e_n \rangle| \|u\| = 1 = \|e_n\|$.
Proof: $\langle e_n, e_n \rangle = 1$.
<2>4. Hence $\|T_n\| = 1$ for all $n \ge 1$.
Proof: <2>2 and <2>3.

<1>10. Show strong convergence $T_n(x) \to 0$ for all $x \in H$: <2>1. For any fixed $x \in H$, by Bessel's inequality $\sum_{n=1}^\infty |\langle x, e_n \rangle|^2 \le \|x\|^2 < \infty$.
Proof: Bessel's inequality.
<2>2. Thus $\lim_{n\to\infty} |\langle x, e_n \rangle| = 0$.
Proof: convergence of the series.
<2>3. Therefore $\|T_n(x)\| = |\langle x, e_n \rangle| \to 0$ as $n \to \infty$, so $\lim_{n\to\infty} T_n(x) = 0$ in $H$.
Proof: <1>9 and <2>2.

<1>11. Q.E.D. Proof: <1>7 (a) and <1>10 (b).
:::
