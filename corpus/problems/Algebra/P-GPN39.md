---
schema: qual/card@1
id: P-GPN39
kind: problem
title: A linear operator with $1\notin\spec(L)$ has unique fixed point $0$
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $V$ be a vector space over a field $F$, and let $L: V \to V$ be a linear operator.
Suppose that $1$ is not an eigenvalue of $L$ (that is, $1 \notin \operatorname{spec}(L)$). Prove that $x = 0$ is the unique fixed point of $L$ (i.e. $L(x) = x \implies x = 0$). Moreover, if $V$ is finite-dimensional, show that $I - L$ is an invertible linear operator on $V$.
:::

::: {.solution}
<1>1. Show that $x = 0$ is the unique fixed point of $L$: <2>1. Suppose $x \in V$ satisfies $L(x) = x$.
Proof: definition of a fixed point of $L$.
<2>2. Rewrite the equation in terms of the identity operator $I: V \to V$:
\[
(I - L)(x) = I(x) - L(x) = x - x = 0.
\]
Proof: linearity of operator subtraction.
<2>3. Thus $x \in \ker(I - L)$.
Proof: <2>2. <2>4. If $x \neq 0$, then $L(x) = 1 \cdot x$ would imply that $\lambda = 1$ is an eigenvalue of $L$ with eigenvector $x$.
Proof: definition of eigenvalue and eigenvector.
<2>5. By hypothesis, $1 \notin \operatorname{spec}(L)$, so no non-zero eigenvector with eigenvalue $1$ exists.
Proof: hypothesis.
<2>6. Therefore $x = 0$, so $\ker(I - L) = \{0\}$ and $x = 0$ is the unique fixed point of $L$.
Proof: <2>4 and <2>5.

<1>2. Show that $I - L$ is invertible when $\dim V < \infty$: <2>1. From <1>1, $\ker(I - L) = \{0\}$, so $I - L$ is injective.
Proof: a linear map is injective if and only if its kernel is trivial.
<2>2. By the Rank–Nullity Theorem for finite-dimensional vector spaces:
\[
\dim V = \dim \ker(I - L) + \dim \operatorname{im}(I - L) = 0 + \dim \operatorname{im}(I - L) = \dim \operatorname{im}(I - L).
\]
Proof: Rank–Nullity Theorem.
<2>3. Thus $\operatorname{im}(I - L) = V$, so $I - L$ is surjective.
Proof: a subspace of the same finite dimension as $V$ is all of $V$.
<2>4. Since $I - L$ is bijective, it is an invertible linear operator on $V$.
Proof: a bijective linear operator on a vector space is invertible.

<1>3. Conclusion: $0$ is the unique fixed point of $L$, and $I - L$ is invertible when $\dim V < \infty$.
Q.E.D. Proof: <1>1 and <1>2.
:::
