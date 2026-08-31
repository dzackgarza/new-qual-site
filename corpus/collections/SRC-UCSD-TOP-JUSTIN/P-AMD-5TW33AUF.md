---
schema: qual/card@1
id: P-AMD-5TW33AUF
kind: problem
title: Topological degree of a polynomial on the Riemann sphere
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $p(z) = \sum_{j=0}^n a_j z^j$ be a polynomial of degree $n \ge 1$ with $a_n \neq 0$. Extend $p$ to a continuous self-map of the Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\} \cong S^2$ by setting $p(\infty) = \infty$. Determine the topological degree $\deg(p)$.
:::

::: {.solution}
**Goal:** Let $p(z) = \sum_{j=0}^n a_j z^j$ with $a_n \neq 0$ and $n \ge 1$ be a polynomial with complex coefficients.
Extend $p$ to a continuous map on the Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\} \cong S^2$ by setting $p(\infty) = \infty$.
Determine the topological degree $\deg(p)$.
(If $n = 0$, $p(z) \equiv a_0$ is constant).

<1>1. Case $n = 0$ (constant polynomial $p(z) = a_0$). Then $\deg(p) = 0$.
::: {.proof}
<2>1. If $p$ is constant, its image is the single point $\{a_0\}$.
<2>2. A non-surjective map $g \colon S^2 \to S^2$ factors through $S^2 \setminus \{q\} \simeq \mathbb{R}^2$ for some $q \notin g(S^2)$.
<2>3. Since $\mathbb{R}^2$ is contractible, $H_2(\mathbb{R}^2) = 0$, so the induced map $g_* \colon H_2(S^2) \to H_2(S^2)$ factors through the zero group and is the zero homomorphism.
<2>4. Hence $\deg(g) = 0$.
:::

<1>2. Case $n \ge 1$ with $a_n \neq 0$. Then $\deg(p) = n$.
::: {.proof}
<2>1. The extension to $\widehat{\mathbb{C}}$ is continuous: Since $a_n \neq 0$ and $n \ge 1$, $\lim_{|z| \to \infty} |p(z)| = \lim_{|z| \to \infty} |a_n z^n| \left|1 + \sum_{j=0}^{n-1} \frac{a_j}{a_n z^{n-j}}\right| = \infty$, so setting $p(\infty) = \infty$ makes $p \colon \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$ continuous.
<2>2. Construct a homotopy to $q(z) = a_n z^n$: Define $H \colon \widehat{\mathbb{C}} \times [0, 1] \to \widehat{\mathbb{C}}$ by $$H(z, t) = a_n z^n + (1-t)\sum_{j=0}^{n-1} a_j z^j \quad \text{for } z \in \mathbb{C}, \qquad H(\infty, t) = \infty.$$
<2>3. For each $t \in [0, 1]$, $H(z, t)$ is a polynomial of degree $n$ with leading coefficient $a_n \neq 0$, so $\lim_{|z| \to \infty} |H(z, t)| = \infty$ uniformly for $t$. Thus $H$ is a continuous homotopy of maps $\widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$.
<2>4. The degree of a map $S^2 \to S^2$ is determined by its induced map on $H_2(S^2) \cong \mathbb{Z}$. Since homotopic maps induce the same homomorphism on homology, $\deg(p) = \deg(z \mapsto a_n z^n)$.
:::

<1>3. Homotopy to the standard monomial $z \mapsto z^n$.
::: {.proof}
<2>1. Write $a_n = r e^{i\theta}$ with $r > 0$ and $\theta \in \mathbb{R}$.
<2>2. Define $K \colon \widehat{\mathbb{C}} \times [0, 1] \to \widehat{\mathbb{C}}$ by $K(z, t) = ((1-t)r + t) e^{i(1-t)\theta} z^n$ for $z \in \mathbb{C}$ and $K(\infty, t) = \infty$.
<2>3. Since $(1-t)r + t > 0$ for all $t \in [0, 1]$, the leading coefficient is non-zero for all $t$, so each $K(\cdot, t)$ is a polynomial of degree $n$ extending continuously to $\widehat{\mathbb{C}}$.
<2>4. Moreover $K(z, 0) = r e^{i\theta} z^n = a_n z^n$ and $K(z, 1) = z^n$, so $K$ is a homotopy from $z \mapsto a_n z^n$ to $f_n(z) = z^n$.
<2>5. Homotopic maps have the same degree, so $\deg(z \mapsto a_n z^n) = \deg(f_n)$.
:::

<1>4. Compute the degree of $f_n(z) = z^n$ on $\widehat{\mathbb{C}} \cong S^2$.
::: {.proof}
<2>1. Method 1 (Local degree / Regular values): Choose the regular value $w_0 = 1 \in \mathbb{C} \setminus \{0\}$. The preimage $f_n^{-1}(1) = \{\zeta_k = e^{2\pi i k / n} \mid k = 0, 1, \dots, n-1\}$ consists of $n$ distinct roots of unity.
<2>2. At each preimage $\zeta_k$, $f_n'(\zeta_k) = n \zeta_k^{n-1} \neq 0$. Since $f_n$ is complex holomorphic, its Jacobian determinant as a real map $\mathbb{R}^2 \to \mathbb{R}^2$ is $|f_n'(z)|^2 > 0$, so each local degree is $\deg_{\zeta_k}(f_n) = +1$.
<2>3. By the regular value formula, the degree equals the sum of local degrees over the preimage of any regular value: $\deg(f_n) = \sum_{k=0}^{n-1} (+1) = n$.

<2>4. Method 2 (Suspension / Winding number): On the equator $S^1 \subset \mathbb{C}$, $f_n(e^{i\theta}) = e^{in\theta}$ winds $n$ times, so $\deg(f_n|_{S^1}) = n$. Viewing $\widehat{\mathbb{C}} \cong \Sigma S^1$, the suspension isomorphism $\widetilde{H}_{k+1}(\Sigma X) \cong \widetilde{H}_k(X)$ is natural, hence $\deg(\Sigma g) = \deg(g) = n$.
:::

<1>5. Conclusion.
<2>1. For $p(z) = \sum_{j=0}^n a_j z^j$ with $a_n \neq 0$: $$\deg(p) = n.$$ (If $p$ is constant, $\deg(p) = 0$).
::: {.proof}
<2>2. By <1>2 and <1>3, $\deg(p) = \deg(f_n)$; by <1>4, $\deg(f_n) = n$; and by <1>1, the constant case has degree $0$.
:::
:::
