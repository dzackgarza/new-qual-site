---
schema: qual/card@1
id: E-G4N4D
kind: exercise
title: A holomorphic function with a vanishing Taylor coefficient at every point is
  a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: exercise
Let $\Omega \subseteq \mathbb{C}$ be a connected open region, and let $f: \Omega \to \mathbb{C}$ be a holomorphic function.
Suppose that for every point $z_0 \in \Omega$, at least one coefficient in the Taylor series expansion:
$$f(z) = \sum_{n=0}^\infty c_n(z_0) (z - z_0)^n$$
is zero (i.e. for every $z_0 \in \Omega$, there exists some $n \in \mathbb{N}$ such that $f^{(n)}(z_0) = 0$).
Prove that $f$ is a polynomial.
:::

::: solution
**Goal:** Prove that if $\forall z \in \Omega, \; \exists n \ge 0$ such that $f^{(n)}(z) = 0$, then $f$ is a polynomial on the connected domain $\Omega$, using the Baire Category Theorem and the Identity Theorem.

<1>1. Decomposition into Closed Sets:
    *Proof:*
    <2>1. For each integer $n \ge 0$, define the set of points where the $n$-th derivative vanishes:
        $$E_n \coloneqq \{z \in \Omega \mid f^{(n)}(z) = 0\}.$$
    <2>2. Since $f$ is holomorphic on $\Omega$, each derivative $f^{(n)}$ is continuous on $\Omega$.
    <2>3. Therefore, each $E_n = (f^{(n)})^{-1}(\{0\})$ is a **closed subset** of $\Omega$ (relative to the subspace topology).
    <2>4. By the problem hypothesis, for every $z \in \Omega$, there is some $n \ge 0$ with $f^{(n)}(z) = 0$, which means:
        $$\Omega = \bigcup_{n=0}^\infty E_n.$$

<1>2. Application of the Baire Category Theorem:
    *Proof:*
    <2>1. The region $\Omega \subset \mathbb{C}$ is a locally compact, complete metric space.
    <2>2. By the **Baire Category Theorem**, a complete metric space (or open subset thereof) cannot be written as a countable union of nowhere dense closed sets.
    <2>3. Since $\Omega = \bigcup_{n=0}^\infty E_n$ is a countable union of closed sets, there must exist at least one index $N \ge 0$ such that $E_N$ has **non-empty interior**:
        $$\operatorname{int}(E_N) \ne \varnothing.$$
    <2>4. Thus, there exists an open disk $D = B_r(w) \subseteq \Omega$ on which:
        $$f^{(N)}(z) = 0 \quad \text{for all } z \in D.$$

<1>3. Local Form on the Open Disk $D$:
    *Proof:*
    <2>1. Since $f^{(N)}(z) = 0$ on the connected open disk $D$, integrating $N$ times shows that $f(z)$ is identically a polynomial of degree at most $N - 1$ on $D$:
        $$f(z) = P(z) = \sum_{k=0}^{N-1} a_k (z - w)^k \quad \text{for all } z \in D.$$

<1>4. Global Extension via the Identity Theorem:
    *Proof:*
    <2>1. Consider the function $g: \Omega \to \mathbb{C}$ defined by $g(z) = f(z) - P(z)$.
    <2>2. $g(z)$ is holomorphic on the connected domain $\Omega$.
    <2>3. On the open disk $D \subseteq \Omega$, $g(z) = 0$.
    <2>4. The zero set of $g$ has an accumulation point (in fact, it contains the entire open disk $D$).
    <2>5. By the **Identity Theorem for Holomorphic Functions**, $g(z)$ must vanish identically on the entire connected domain $\Omega$:
        $$g(z) = 0 \iff f(z) = P(z) \quad \text{for all } z \in \Omega.$$

<1>5. Conclusion:
    $f(z)$ is a polynomial of degree at most $N - 1$ on all of $\Omega$. Q.E.D.
:::
