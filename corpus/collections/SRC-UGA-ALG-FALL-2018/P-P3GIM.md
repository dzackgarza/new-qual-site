---
schema: qual/card@1
id: P-P3GIM
kind: problem
title: 'Fitting''s lemma: $V=U\oplus W$ with $\phi|_U$ nilpotent and $\phi|_W$ nonsingular'
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$, and let $\phi: V \to V$ be a linear transformation.

Prove that there exists a direct sum decomposition
$$
V = U \oplus W,
$$
where $U$ and $W$ are $\phi$-invariant subspaces of $V$, $\phi|_U$ is nilpotent, and $\phi|_W$ is invertible (nonsingular).
:::

::: {.solution}
**Goal:** Prove Fitting's Lemma for linear operators on finite-dimensional vector spaces using the stabilization of kernels and images of powers of $\phi$.

::: pf

::: {.pf-step #s1}
Stabilization of kernel and image chains:

::: pf-proof

::: pf-step
Let $n = \dim_F V < \infty$.
:::

::: pf-step
Consider the ascending chain of kernels and the descending chain of images:
$$\ker(\phi) \subseteq \ker(\phi^2) \subseteq \ker(\phi^3) \subseteq \cdots \subseteq V,$$
$$V \supseteq \operatorname{Im}(\phi) \supseteq \operatorname{Im}(\phi^2) \supseteq \operatorname{Im}(\phi^3) \supseteq \cdots$$
:::

::: pf-step
Because $\dim_F V = n < \infty$, the sequence of dimensions $\dim_F \ker(\phi^m)$ is non-decreasing and bounded above by $n$.
:::

::: pf-step
Thus the chain of kernels must stabilize: there exists an integer $k \le n$ such that
$$\ker(\phi^k) = \ker(\phi^{k+1}) = \ker(\phi^{k+2}) = \cdots = \ker(\phi^{2k}).$$
:::

::: pf-step
Define $U = \ker(\phi^k)$ and $W = \operatorname{Im}(\phi^k)$.
:::

:::

:::

::: pf-step
$U$ and $W$ are $\phi$-invariant subspaces:

::: pf-proof

::: pf-step
For $u \in U = \ker(\phi^k)$:
$$\phi^k(\phi(u)) = \phi(\phi^k(u)) = \phi(0) = 0,$$
so $\phi(u) \in \ker(\phi^k) = U$.
:::

::: pf-step
For $w \in W = \operatorname{Im}(\phi^k)$, write $w = \phi^k(v)$ for some $v \in V$:
$$\phi(w) = \phi(\phi^k(v)) = \phi^k(\phi(v)) \in \operatorname{Im}(\phi^k) = W.$$
:::

:::

:::

::: {.pf-step #s3}
Direct sum decomposition $V = U \oplus W$:

::: pf-proof

::: pf-step
Intersection $U \cap W = \{0\}$:

- Let $v \in U \cap W$.
- Since $v \in W = \operatorname{Im}(\phi^k)$, there exists $x \in V$ such that $v = \phi^k(x)$.
- Since $v \in U = \ker(\phi^k)$, $\phi^k(v) = 0$, which gives $\phi^{2k}(x) = 0$.
- Thus $x \in \ker(\phi^{2k})$.
- By stabilization at index $k$ (step [](#s1){.pf-ref}), $\ker(\phi^{2k}) = \ker(\phi^k)$, so $x \in \ker(\phi^k)$.
- Therefore $v = \phi^k(x) = 0$.
- Hence $U \cap W = \{0\}$.
:::

::: pf-step
Sum $V = U + W$:

- By the Rank-Nullity Theorem applied to the linear map $\phi^k: V \to V$:
$$\dim_F \ker(\phi^k) + \dim_F \operatorname{Im}(\phi^k) = \dim_F V.$$
- Since $U \cap W = \{0\}$, $\dim_F(U \oplus W) = \dim_F U + \dim_F W = \dim_F V$.
- A subspace of $V$ with the same finite dimension as $V$ must be $V$ itself.
- Thus $V = U \oplus W$.
:::

:::

:::

::: pf-step
Properties of the restrictions $\phi|_U$ and $\phi|_W$:

::: pf-proof

::: pf-step
$\phi|_U$ is nilpotent:

- For every $u \in U = \ker(\phi^k)$, $(\phi|_U)^k(u) = \phi^k(u) = 0$.
- Thus $(\phi|_U)^k = 0$, so $\phi|_U$ is nilpotent.
:::

::: pf-step
$\phi|_W$ is invertible:

- Since $W$ is finite-dimensional, $\phi|_W: W \to W$ is invertible if and only if $\ker(\phi|_W) = \{0\}$.
- Let $w \in \ker(\phi|_W)$. Then $w \in W$ and $\phi(w) = 0$.
- Then $\phi^k(w) = \phi^{k-1}(\phi(w)) = \phi^{k-1}(0) = 0$, so $w \in \ker(\phi^k) = U$.
- Thus $w \in U \cap W$.
- By step [](#s3){.pf-ref}, $U \cap W = \{0\}$, so $w = 0$.
- Therefore $\ker(\phi|_W) = \{0\}$, which proves that $\phi|_W$ is invertible.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$V = U \oplus W$ with $U = \ker(\phi^k)$ and $W = \operatorname{Im}(\phi^k)$ is the required Fitting decomposition.
:::

:::

:::
:::
