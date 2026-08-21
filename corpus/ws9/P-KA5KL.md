---
schema: qual/card@1
id: P-KA5KL
kind: problem
title: The space $A^2(U)$ of square-integrable holomorphic functions is a Hilbert
  space
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Hilbert Spaces
  - Completeness
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $U \subset \mathbb{C}$ be an open set and $$A^2(U) = \{f \text{ holomorphic on } U : \int_U |f(z)|^2 dxdy < \infty\}.$$ Define $$\langle f,g \rangle = \int_U f(z)\overline{g(z)}dxdy, \quad \forall f,g \in A^2(U).$$ Prove that $A^2(U)$ is a Hilbert space when equipped with this inner product.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For open $U \subseteq \CC$, show $A^2(U) = \{f \text{ holomorphic on } U : \int_U |f|^2 < \infty\}$ with $\langle f, g \rangle = \int_U f\bar g\, dxdy$ is a Hilbert space.

<1>1. $A^2(U)$ is an inner product space.
Proof: $A^2(U)$ is a subspace of $L^2(U)$ (pointwise operations preserve holomorphy and the $L^2$ norm is finite by definition), and the pairing is the restriction of the $L^2$ inner product, hence a positive-definite Hermitian form.

<1>2. It suffices to show $A^2(U)$ is closed in the complete space $L^2(U)$.
Proof: a closed subspace of a complete inner product space is complete.

<1>3. Mean-value estimate: for each compact $K \subset U$ there is $C_K$ with $\sup_K |f| \le C_K \|f\|_{L^2(U)}$ for all $f \in A^2(U)$.
Proof: by the mean value property $|f(a)| \le \frac{1}{\pi r^2}\int_{D(a,r)}|f| \le \frac{1}{\sqrt{\pi} r}\|f\|_{L^2(D(a,r))}$ for any disk $D(a,r) \subset U$; cover $K$ by finitely many disks with radius $r = \tfrac{1}{2}\dist(K, \bd U)$ (if $U = \CC$, take any fixed $r$).

<1>4. $A^2(U)$ is closed in $L^2(U)$.
<2>1. Let $(f_n) \subset A^2(U)$ with $f_n \to f$ in $L^2$; then $(f_n)$ is locally uniformly Cauchy.
Proof: <1>3 applied to $f_n - f_m$ gives $\sup_K |f_n - f_m| \le C_K \|f_n - f_m\|_2 \to 0$.
<2>2. $f_n \to g$ locally uniformly on $U$ for some holomorphic $g$.
Proof: local uniform Cauchy sequence (by <2>1) converges locally uniformly; the limit of holomorphic functions is holomorphic.
<2>3. $f = g$ a.e., so $f \in A^2(U)$.
Proof: $f_n \to f$ in $L^2$ gives a subsequence converging a.e. to $f$; <2>2 gives $f_n \to g$ pointwise; hence $f = g$ a.e. and $g \in L^2$ since $\int|g|^2 = \int|f|^2 < \infty$.

<1>5. Q.E.D. Proof: <1>1 and <1>4 show $A^2(U)$ is a closed subspace of the Hilbert space $L^2(U)$, hence a Hilbert space.
:::
