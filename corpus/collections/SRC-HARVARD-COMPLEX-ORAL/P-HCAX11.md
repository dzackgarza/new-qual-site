---
schema: qual/card@1
id: P-HCAX11
kind: problem
title: The punctured disk is not conformally equivalent to an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Prove that the punctured unit disk is not conformally equivalent to an annulus.
:::

::: {.solution}
<1>1. Setup the biholomorphism and apply Riemann’s Removable Singularity Theorem: <2>1. Let $\mathbb{D}^* = \{z \in \mathbb{C} : 0 < |z| < 1\}$ and let $A = \{w \in \mathbb{C} : r < |w| < R\}$ with $0 < r < R < \infty$.
::: {.proof}
definition of the punctured disk and an annulus.
:::
<2>2. Suppose for contradiction that there exists a biholomorphic map $f: \mathbb{D}^* \to A$.
::: {.proof}
proof by contradiction setup.
:::
<2>3. For all $z \in \mathbb{D}^*$, $|f(z)| < R < \infty$, so $f$ is bounded on $\mathbb{D}^*$.
::: {.proof}
$f(\mathbb{D}^*) = A \subset B(0, R)$.
:::
<2>4. By Riemann’s Removable Singularity Theorem, $f$ extends to a holomorphic function $\tilde{f}: \mathbb{D} \to \mathbb{C}$ on the full unit disk $\mathbb{D}$, with $\tilde{f}(z) = f(z)$ for $z \neq 0$.
::: {.proof}
Riemann's Removable Singularity Theorem.
:::

<1>2. Analyze the value $w_0 = \tilde{f}(0)$: <2>1. By continuity, $w_0 = \lim_{z \to 0} f(z) \in \overline{A} = \{w \in \mathbb{C} : r \le |w| \le R\}$.
::: {.proof}
limits of sequences in $A$ lie in the closure $\overline{A}$.
:::
<2>2. **Case 1: $w_0 \in A$.** Since $f: \mathbb{D}^* \to A$ is a bijection, there exists $z_1 \in \mathbb{D}^*$ with $f(z_1) = w_0$.
Then $\tilde{f}(0) = \tilde{f}(z_1) = w_0$ with $0 \neq z_1 \in \mathbb{D}$.
By the Open Mapping Theorem and the local structure of holomorphic maps, $\tilde{f}$ is an open map, and every neighborhood of $0$ maps to a neighborhood of $w_0$.
Thus there exist distinct points $z', z'' \in \mathbb{D}^*$ with $f(z') = f(z'')$, contradicting the injectivity of $f$ on $\mathbb{D}^*$.
::: {.proof}
non-constant holomorphic maps are open and locally finite-to-one.
:::
<2>3. **Case 2: $w_0 \in \partial A$ (so $|w_0| = r$ or $|w_0| = R$).** By the Open Mapping Theorem, $\tilde{f}(\mathbb{D})$ is an open subset of $\mathbb{C}$.
Since $0 \in \mathbb{D}$, $\tilde{f}(\mathbb{D})$ contains an open neighborhood $U$ of $w_0 = \tilde{f}(0)$.
Since $w_0 \in \partial A$, the open neighborhood $U$ must contain points outside $\overline{A}$ (i.e. points with modulus $< r$ or $> R$). However, $\tilde{f}(\mathbb{D}) = \tilde{f}(\mathbb{D}^*) \cup \{\tilde{f}(0)\} = A \cup \{w_0\} \subseteq \overline{A}$, which contains no points outside $\overline{A}$.
This is a direct contradiction.
::: {.proof}
an open neighborhood of a boundary point contains points in the exterior.
:::

<1>3. Conclusion: Both cases lead to a contradiction, so $\mathbb{D}^*$ cannot be conformally equivalent to any annulus $A(r, R)$.
::: {.proof}
<1>1 and <1>2.
:::
Q.E.D.
:::
