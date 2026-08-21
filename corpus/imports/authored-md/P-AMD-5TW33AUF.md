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
solved: true
---

::: {.problem}
Let $p(x) = \sum_i^na_ix^i$, view $p: \CC \union \infty \selfmap$ and determine its topological degree
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $p(z) = \sum_{j=0}^n a_j z^j$ with $a_n \neq 0$ and $n \ge 1$ be a polynomial with complex coefficients.
Extend $p$ to a continuous map on the Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\} \cong S^2$ by setting $p(\infty) = \infty$.
Determine the topological degree $\deg(p)$.
(If $n = 0$, $p(z) \equiv a_0$ is constant).

<1>1. Case $n = 0$ (constant polynomial $p(z) = a_0$). <2>1. If $p$ is constant, its image is a single point $\{a_0\}$ (or if extended as a constant map $\widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$). <2>2. Any continuous map into $S^2$ whose image is not surjective has degree 0. <2>3. Proof: A non-surjective map factors through $\mathbb{R}^2 \simeq S^2 \setminus \{q\}$, which is contractible, so the map induces the zero homomorphism on $H_2(S^2) \cong \mathbb{Z}$.
Thus $\deg(p) = 0$.
Q.E.D.

<1>2. Case $n \ge 1$ with $a_n \neq 0$.
<2>1. Extension to $\widehat{\mathbb{C}}$ is continuous: Since $a_n \neq 0$ and $n \ge 1$, $\lim_{|z| \to \infty} |p(z)| = \lim_{|z| \to \infty} |a_n z^n| \left|1 + \sum_{j=0}^{n-1} \frac{a_j}{a_n z^{n-j}}\right| = \infty$.
Setting $p(\infty) = \infty$ makes $p \colon \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$ a continuous map (in fact a holomorphic branched covering map).
<2>2. Construct a homotopy to $q(z) = a_n z^n$.
Define $H \colon \widehat{\mathbb{C}} \times [0, 1] \to \widehat{\mathbb{C}}$ by: $$H(z, t) = a_n z^n + (1-t)\sum_{j=0}^{n-1} a_j z^j \quad \text{for } z \in \mathbb{C}, \qquad H(\infty, t) = \infty.$$ <2>3. For any $t \in [0, 1]$, $H(z, t)$ is a polynomial in $z$ of degree $n$ with leading coefficient $a_n \neq 0$.
<2>4. Thus $\lim_{|z| \to \infty} |H(z, t)| = \infty$ uniformly for $t \in [0, 1]$, so $H$ is a continuous homotopy of maps $\widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$.
<2>5. Homotopic maps induce the same homomorphism on homology, so $\deg(p) = \deg(z \mapsto a_n z^n)$.
<2>6. Proof: By homotopy invariance of topological degree.
Q.E.D.

<1>3. Homotopy to the standard monomial $z \mapsto z^n$.
<2>1. Write $a_n = r e^{i\theta}$ with $r > 0$ and $\theta \in \mathbb{R}$.
<2>2. Define $K \colon \widehat{\mathbb{C}} \times [0, 1] \to \widehat{\mathbb{C}}$ by $K(z, t) = ((1-t)r + t) e^{i(1-t)\theta} z^n$ for $z \in \mathbb{C}$ and $K(\infty, t) = \infty$.
<2>3. Since $(1-t)r + t > 0$ for all $t \in [0, 1]$, the leading coefficient is non-zero for all $t$.
<2>4. Thus $K$ is a homotopy between $z \mapsto a_n z^n$ and $f_n(z) = z^n$.
<2>5. Therefore $\deg(z \mapsto a_n z^n) = \deg(f_n)$.
<2>6. Proof: Homotopy through non-zero leading coefficients.
Q.E.D.

<1>4. Compute the degree of $f_n(z) = z^n$ on $\widehat{\mathbb{C}} \cong S^2$.
<2>1. Method 1 (Local degree / Regular values): <3>1. Choose a regular value $w_0 \in \mathbb{C} \setminus \{0\}$, e.g. $w_0 = 1$.
<3>2. The preimage $f_n^{-1}(1)$ consists of the $n$ distinct $n$-th roots of unity: $$f_n^{-1}(1) = \{\zeta_k = e^{2\pi i k / n} \mid k = 0, 1, \dots, n-1\}.$$ <3>3. At each preimage $\zeta_k$, $f_n'(\zeta_k) = n \zeta_k^{n-1} \neq 0$.
<3>4. Since $f_n$ is complex holomorphic, its Jacobian determinant as a real map $\mathbb{R}^2 \to \mathbb{R}^2$ at each point is $|f_n'(z)|^2 > 0$.
<3>5. Thus each local degree is $\deg_{\zeta_k}(f_n) = +1$.
<3>6. Summing local degrees over all preimages of a regular value gives: $$\deg(f_n) = \sum_{k=0}^{n-1} \deg_{\zeta_k}(f_n) = \sum_{k=0}^{n-1} (+1) = n.$$ <3>7. Proof: By the regular value formula for topological degree of smooth/holomorphic maps between compact oriented manifolds.
Q.E.D. <2>2. Method 2 (Suspension / Winding number): <3>1. On the equator $S^1 \subset \mathbb{C}$, $f_n(e^{i\theta}) = e^{in\theta}$, which winds around $S^1$ exactly $n$ times (degree $n$ as a map $S^1 \to S^1$). <3>2. Viewing $\widehat{\mathbb{C}} \cong \Sigma S^1$, the suspension $\Sigma(S^1 \xrightarrow{\cdot n} S^1)$ has degree $n$.
<3>3. Proof: Degree is preserved under suspension.
Q.E.D.

<1>5. Conclusion.
<2>1. For $p(z) = \sum_{j=0}^n a_j z^j$ with $a_n \neq 0$: $$\deg(p) = n.$$ (If $p$ is constant, $\deg(p) = 0$). <2>2. Proof: By <1>1–<1>4. Q.E.D.
:::
