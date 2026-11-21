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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Twenty-six leaf steps asserted their claim with no justification and each now carries one: in part (a)
    the reduction to the open ball and the positivity of $c$, the kernel and codimension of
    $x_0^\perp$ with the Gram--Schmidt choice of $e_n$, the norm computation making $x_n$ a unit vector,
    the Riesz step, Bessel, the vanishing of the Fourier coefficients and the weak convergence; in part
    (b) the choice of $u$, the definition and linearity of $T_n$, the Cauchy--Schwarz bound, the value at
    the unit vector $e_n$ and the two-sided conclusion $\norm{T_n} = 1$, and the strong convergence.
    Checked while writing: $\norm{x_0 + ce_n}^2 = 1$ needs both $e_n \in x_0^\perp$ and
    $c^2 = 1 - \norm{x_0}^2$, and the operator norm $\norm{T_n} = 1$ needs the value at $e_n$, not only
    the upper bound. One repair: the closing step had "Conclusion:" as its claim and now states the two
    conclusions it proved. The statement is unchanged. The collection retains the UCLA real analysis
    Spring 2009 paper and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $H$ be an infinite dimensional real Hilbert space.

a. Prove that the unit sphere $S=\{x\in H: \norm{x}=1\}$ is weakly dense in the unit ball $B=\{x\in H: \norm{x}\le 1\}$.

b. Prove there is a sequence $T_n$ of bounded linear operators from $H$ to $H$ such that $\norm{T_n}=1$ for all $n$ but $\lim_{n\to\infty} T_n(x)=0$ for all $x\in H$.
:::

::: {.solution}
**Goal:** Prove that the unit sphere $S$ of an infinite-dimensional real Hilbert space $H$ is weakly dense in the closed unit ball $B$ in (a), and construct operators $T_n$ with $\norm{T_n} = 1$ converging strongly to 0 in (b).

::: pf

::: pf-step
Part (a): Reduction to the open unit ball.

::: pf-proof

::: pf-step
Let $x_0 \in B$, so $\norm{x_0} \le 1$.

::: pf-proof
$B$ is by definition the closed unit ball, so its points are exactly the vectors of norm at most $1$; that is the only property of $x_0$ used in this reduction.
:::

:::

::: pf-step
If $\norm{x_0} = 1$, then $x_0 \in S$, so the constant sequence $x_n = x_0 \in S$ converges strongly (and hence weakly) to $x_0$.

::: pf-proof
The sphere $S$ is the set of unit vectors, so $x_0$ lies in $S$; a constant sequence converges to its value in norm, and norm convergence implies weak convergence because $\abs{\langle x_n - x_0, v\rangle} \le \norm{x_n - x_0}\norm{v}$ tends to $0$ for every $v$.
:::

:::

::: pf-step
Thus we may assume $\norm{x_0} < 1$, which implies $c = \sqrt{1 - \norm{x_0}^2} > 0$.

::: pf-proof
A point of $B$ has norm exactly $1$, which is the previous case, or norm strictly less than $1$; in the second case $1 - \norm{x_0}^2 > 0$, so its square root $c$ is a positive real number.
:::

:::

:::

:::

::: pf-step
Part (a): Construction of an orthonormal sequence in $x_0^\perp$.

::: pf-proof

::: pf-step
The orthogonal complement $x_0^\perp = \{v \in H : \langle x_0, v \rangle = 0\}$ is the kernel of the continuous linear functional $\langle x_0, \cdot \rangle$.

::: pf-proof
The set is the preimage of $\{0\}$ under $v \mapsto \langle x_0, v\rangle$, a map that is linear in $v$ by linearity of the inner product in its second argument and continuous by Cauchy--Schwarz, with bound $\norm{x_0}$; a kernel of a linear map is a subspace, and a preimage of a closed set under a continuous map is closed.
:::

:::

::: pf-step
Since $x_0^\perp$ has codimension at most 1 in the infinite-dimensional space $H$, $x_0^\perp$ is infinite-dimensional.

::: pf-proof
The kernel of the functional $\langle x_0,\cdot\rangle$ has codimension $1$ when the functional is nonzero, and the whole space when it is zero, by the rank-nullity theorem; a subspace of finite codimension in an infinite-dimensional space is itself infinite-dimensional, because a finite-dimensional quotient plus a finite-dimensional complement would make the space finite-dimensional.
:::

:::

::: pf-step
Using the Gram–Schmidt process, choose a countable orthonormal sequence $\{e_n\}_{n=1}^\infty \subset x_0^\perp$, so $\langle e_n, e_m \rangle = \delta_{nm}$ and $\langle x_0, e_n \rangle = 0$ for all $n \ge 1$.

::: pf-proof
An infinite-dimensional Hilbert space contains a linearly independent sequence, and Gram--Schmidt turns it into an orthonormal sequence; applying the process to a sequence drawn from $x_0^\perp$ keeps every vector in that subspace, so $\langle e_n, e_m\rangle = \delta_{nm}$ and $\langle x_0, e_n\rangle = 0$ for all $n$.
:::

:::

:::

:::

::: pf-step
Part (a): Construction of the sequence on the unit sphere $S$.

::: pf-proof

::: pf-step
For each $n \ge 1$, define $x_n = x_0 + c e_n = x_0 + \sqrt{1 - \norm{x_0}^2} \, e_n$.

::: pf-proof
The formula assigns to each $n$ the vector $x_0 + c e_n$, a sum of two elements of $H$, so it defines a sequence in $H$; $c$ is the fixed positive number of the first part.
:::

:::

::: pf-step
Compute the norm squared of $x_n$ using orthogonality $\langle x_0, e_n \rangle = 0$:
$$\norm{x_n}^2 = \norm{x_0 + c e_n}^2 = \norm{x_0}^2 + 2c \langle x_0, e_n \rangle + c^2 \norm{e_n}^2 = \norm{x_0}^2 + 0 + (1 - \norm{x_0}^2)(1) = 1.$$

::: pf-proof
Expanding the square gives $\norm{x_0 + ce_n}^2 = \norm{x_0}^2 + 2c\operatorname{Re}\langle x_0,e_n\rangle + c^2\norm{e_n}^2$; the middle term vanishes because $e_n \in x_0^\perp$, and substituting $c^2 = 1 - \norm{x_0}^2$ and $\norm{e_n} = 1$ leaves $\norm{x_0}^2 + 1 - \norm{x_0}^2 = 1$.
:::

:::

::: pf-step
Therefore $\norm{x_n} = 1$, so $x_n \in S$ for all $n \ge 1$.

::: pf-proof
A nonnegative real number whose square is $1$ equals $1$, so $\norm{x_n} = 1$; the sphere $S$ is by definition the set of vectors of norm $1$, hence $x_n \in S$.
:::

:::

:::

:::

::: pf-step
Part (a): Weak convergence $x_n \rightharpoonup x_0$.

::: pf-proof

::: pf-step
By the Riesz Representation Theorem, every continuous linear functional $\phi \in H^*$ is of the form $\phi(y) = \langle y, v \rangle$ for some $v \in H$.

::: pf-proof
The Riesz representation theorem identifies the bounded functionals on a Hilbert space with the vectors, sending $v$ to $\langle\cdot, v\rangle$; so every $\phi \in H^*$ has the displayed form for some $v$, which is the only property of $H^*$ used below.
:::

:::

::: pf-step
For any fixed $v \in H$, Bessel's inequality for the orthonormal sequence $\{e_n\}$ gives
$$\sum_{n=1}^\infty \abs{\langle v, e_n \rangle}^2 \le \norm{v}^2 < \infty.$$

::: pf-proof
Bessel's inequality says that for any orthonormal sequence and any vector $v$ the sum of the squared moduli of the Fourier coefficients is at most $\norm{v}^2$, which is the displayed inequality; it is finite because $v \in H$ has finite norm.
:::

:::

::: pf-step
Since the series converges, its terms tend to zero: $\lim_{n \to \infty} \langle v, e_n \rangle = 0$.

::: pf-proof
The terms of a convergent series of nonnegative numbers tend to $0$, the partial sums being Cauchy; so $\abs{\langle v, e_n\rangle}^2 \to 0$, hence also $\langle v, e_n\rangle \to 0$.
:::

:::

::: pf-step
Evaluating $\phi(x_n)$:
$$\lim_{n \to \infty} \langle x_n, v \rangle = \lim_{n \to \infty} \left( \langle x_0, v \rangle + c \langle e_n, v \rangle \right) = \langle x_0, v \rangle + c \cdot 0 = \langle x_0, v \rangle.$$

::: pf-proof
The inner product is linear in its first argument, so $\langle x_n, v\rangle = \langle x_0, v\rangle + c\langle e_n, v\rangle$; the first term is constant in $n$ and the second tends to $c \cdot 0$ by the previous step.
:::

:::

::: pf-step
Since this holds for all $v \in H$, $x_n \rightharpoonup x_0$ weakly in $H$.

::: pf-proof
Weak convergence $x_n \rightharpoonup x_0$ means $\phi(x_n) \to \phi(x_0)$ for every bounded functional $\phi$, and by the Riesz step every such functional is $\langle\cdot, v\rangle$ for some $v$; the previous step gives the convergence for each $v$, which is exactly the definition.
:::

:::

::: pf-step
Thus every point of $B$ is in the weak closure of $S$, proving $S$ is weakly dense in $B$.

::: pf-proof
Every $x_n$ lies in $S$, so the sequence shows that each weakly open set containing the arbitrary point $x_0 \in B$ meets $S$; hence $S$ meets every weakly open set that meets $B$, that is, $B$ is contained in the weak closure of $S$.
:::

:::

:::

:::

::: pf-step
Part (b): Construction of rank-1 operators $T_n$.

::: pf-proof

::: pf-step
Choose an orthonormal sequence $\{e_n\}_{n=1}^\infty$ in $H$, and fix a unit vector $u \in H$ with $\norm{u} = 1$ (e.g. $u = e_1$).

::: pf-proof
The space is infinite-dimensional, so it contains a countable orthonormal sequence; its first vector is a unit vector, so $u = e_1$ is a legitimate choice of unit vector.
:::

:::

::: pf-step
Define $T_n: H \to H$ by $T_n(x) = \langle x, e_n \rangle u$ for all $x \in H$.

::: pf-proof
For each $x$ the scalar $\langle x, e_n\rangle$ is well defined and $u$ is a fixed vector, so the product is an element of $H$; the formula therefore defines a map from $H$ to $H$.
:::

:::

::: pf-step
Linearity of $T_n$ follows directly from linearity of the inner product in the first argument:
$$T_n(a x + b y) = \langle ax + by, e_n \rangle u = (a\langle x, e_n \rangle + b\langle y, e_n \rangle)u = a T_n(x) + b T_n(y).$$

::: pf-proof
The computation $T_n(ax+by) = \langle ax+by, e_n\rangle u = (a\langle x,e_n\rangle + b\langle y,e_n\rangle)u = aT_n(x) + bT_n(y)$ uses linearity of the inner product in its first argument and distributivity in $H$; additivity and homogeneity are what linearity of a map means.
:::

:::

:::

:::

::: pf-step
Part (b): Operator norm $\norm{T_n} = 1$.

::: pf-proof

::: pf-step
For any $x \in H$, by the Cauchy–Schwarz inequality:
$$\norm{T_n(x)} = \abs{\langle x, e_n \rangle} \norm{u} = \abs{\langle x, e_n \rangle} \le \norm{x} \norm{e_n} = \norm{x}.$$

::: pf-proof
Using $\norm{u} = 1$, $\norm{T_n(x)} = \norm{\langle x,e_n\rangle u} = \abs{\langle x,e_n\rangle}$; Cauchy--Schwarz gives $\abs{\langle x,e_n\rangle} \le \norm{x}\norm{e_n} = \norm{x}$ because $e_n$ is a unit vector.
:::

:::

::: pf-step
Thus $\norm{T_n} \le 1$.

::: pf-proof
The operator norm is the supremum of $\norm{T_n x}$ over the unit vectors; the previous bound says $\norm{T_n x} \le \norm{x}$, so the values on unit vectors are at most $1$ and the supremum is at most $1$.
:::

:::

::: pf-step
Evaluating at the unit vector $x = e_n$:
$$\norm{T_n(e_n)} = \abs{\langle e_n, e_n \rangle} \norm{u} = 1 \cdot 1 = 1 = \norm{e_n}.$$

::: pf-proof
The vector $e_n$ is a unit vector and $\abs{\langle e_n, e_n\rangle} = \norm{e_n}^2 = 1$, so $\norm{T_n(e_n)} = 1 \cdot \norm{u} = 1 = \norm{e_n}$.
:::

:::

::: pf-step
Therefore $\norm{T_n} = 1$ for all $n \ge 1$.

::: pf-proof
The operator norm is at most $1$ by the bound on unit vectors and at least $\norm{T_n(e_n)} = 1$ because it is the supremum of the values at unit vectors; hence it equals $1$ for every $n$.
:::

:::

:::

:::

::: pf-step
Part (b): Strong convergence $T_n(x) \to 0$ for all $x \in H$.

::: pf-proof

::: pf-step
For any fixed $x \in H$, Bessel's inequality gives $\sum_{n=1}^\infty \abs{\langle x, e_n \rangle}^2 \le \norm{x}^2 < \infty$.

::: pf-proof
Bessel's inequality applied to the fixed vector $x$ and the orthonormal sequence $\{e_n\}$ gives the displayed bound, whose right-hand side is finite because $x \in H$.
:::

:::

::: pf-step
Thus $\lim_{n \to \infty} \abs{\langle x, e_n \rangle} = 0$.

::: pf-proof
The terms of a convergent series of nonnegative numbers tend to $0$, so $\abs{\langle x, e_n\rangle}^2 \to 0$; taking square roots preserves the limit.
:::

:::

::: pf-step
Compute the norm of the operator value:
$$\lim_{n \to \infty} \norm{T_n(x)} = \lim_{n \to \infty} \abs{\langle x, e_n \rangle} = 0.$$

::: pf-proof
$\norm{T_n(x)} = \abs{\langle x,e_n\rangle}\norm{u} = \abs{\langle x,e_n\rangle}$ because $\norm{u} = 1$, and that sequence tends to $0$ by the previous step.
:::

:::

::: pf-step
Therefore $\lim_{n \to \infty} T_n(x) = 0$ in the norm topology of $H$ for every $x \in H$.

::: pf-proof
A sequence of vectors converges to $0$ in the norm topology exactly when its norms tend to $0$, which is the previous step; convergence for every $x \in H$ is strong convergence of the operators.
:::

:::

:::

:::

::: pf-step
$S$ is weakly dense in $B$, and $\norm{T_n} = 1$ for every $n$ while $T_n(x) \to 0$ for every $x \in H$.

::: pf-proof
$S$ is weakly dense in $B$, and the operators $T_n(x) = \langle x, e_n \rangle u$ satisfy $\norm{T_n} = 1$ for all $n$ while $T_n(x) \to 0$ for all $x \in H$.
:::

:::

:::

:::
