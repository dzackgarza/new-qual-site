---
schema: qual/card@1
id: P-P3GIM
kind: problem
title: 'Fitting''s lemma: $V=U\oplus W$ with $\phi\restrict_U$ nilpotent and $\phi\restrict_W$ nonsingular'
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
where $U$ and $W$ are $\phi$-invariant subspaces of $V$, $\phi\restrict_U$ is nilpotent, and $\phi\restrict_W$ is invertible (nonsingular).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For some $k\geq1$, the kernels of all powers $\phi^j$ with $j\geq k$ equal $\ker(\phi^k)$.

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

::: {.pf-step #s2}

The subspaces $U=\ker(\phi^k)$ and $W=\operatorname{im}(\phi^k)$ are $\phi$-invariant.

::: pf-proof

::: pf-step

For $u \in U = \ker(\phi^k)$:
    $$\phi^k(\phi(u)) = \phi(\phi^k(u)) = \phi(0) = 0,$$
    so $\phi(u) \in \ker(\phi^k) = U$.

:::

::: pf-step

For $w \in W = \operatorname{Im}(\phi^k)$, write $w = \phi^k(v)$ for some $v \in V$:

:::

$$\phi(w) = \phi(\phi^k(v)) = \phi^k(\phi(v)) \in \operatorname{Im}(\phi^k) = W.$$

:::

:::

::: {.pf-step #s3}

The vector space decomposes as $V=U\oplus W$.

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

:::

- By the Rank-Nullity Theorem applied to the linear map $\phi^k: V \to V$:
$$\dim_F \ker(\phi^k) + \dim_F \operatorname{Im}(\phi^k) = \dim_F V.$$
- Since $U \cap W = \{0\}$, $\dim_F(U \oplus W) = \dim_F U + \dim_F W = \dim_F V$.
- A subspace of $V$ with the same finite dimension as $V$ must be $V$ itself.
- Thus $V = U \oplus W$.

:::

:::

::: {.pf-step #s4}

The restriction $\phi\restrict_U$ is nilpotent, while $\phi\restrict_W$ is invertible.

::: pf-proof

::: pf-step

$\phi\restrict_U$ is nilpotent:
        - For every $u \in U = \ker(\phi^k)$, $(\phi\restrict_U)^k(u) = \phi^k(u) = 0$.
        - Thus $(\phi\restrict_U)^k = 0$, so $\phi\restrict_U$ is nilpotent.

:::

::: pf-step

$\phi\restrict_W$ is invertible:

:::

- Since $W$ is finite-dimensional, $\phi\restrict_W: W \to W$ is invertible if and only if $\ker(\phi\restrict_W) = \{0\}$.
- Let $w \in \ker(\phi\restrict_W)$. Then $w \in W$ and $\phi(w) = 0$.
- Then $\phi^k(w) = \phi^{k-1}(\phi(w)) = \phi^{k-1}(0) = 0$, so $w \in \ker(\phi^k) = U$.
- Thus $w \in U \cap W$.
- By step [](#s3){.pf-ref}, $U \cap W = \{0\}$, so $w = 0$.
- Therefore $\ker(\phi\restrict_W) = \{0\}$, which proves that $\phi\restrict_W$ is invertible.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}, using the stabilized kernels from step [](#s1){.pf-ref}, prove the required Fitting decomposition.

:::

:::

:::
