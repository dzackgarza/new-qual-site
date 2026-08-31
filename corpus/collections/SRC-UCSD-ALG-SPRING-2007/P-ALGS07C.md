---
schema: qual/card@1
id: P-ALGS07C
kind: problem
title: "All R[x]-module structures on a 3-dimensional real vector space"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Describe, up to isomorphism, all the $\mathbb{R}[x]$-module structures one might put on a 3-dimensional real vector space (extending the fixed $\mathbb{R}$-action).
:::

::: {.solution}
<1>1. Equivalence to similarity classes of linear operators on $\mathbb{R}^3$:
<2>1. An $\mathbb{R}[x]$-module structure on $V = \mathbb{R}^3$ extending the scalar multiplication of $\mathbb{R}$ is completely determined by the linear operator $T \in \operatorname{End}_\mathbb{R}(V)$ given by $T(v) = x \cdot v$.
Polynomials act by $p(x) \cdot v = p(T)(v)$.
<2>2. Two such $\mathbb{R}[x]$-modules $V_T$ and $V_{T'}$ are isomorphic if and only if the operators $T$ and $T'$ are similar, i.e. $T' = P T P^{-1}$ for some $P \in \operatorname{GL}_3(\mathbb{R})$.

<1>2. Classification via the Structure Theorem for modules over the PID $\mathbb{R}[x]$:
<2>1. Since $\mathbb{R}[x]$ is a PID and $\dim_\mathbb{R}(V) = 3$, $V$ is a finitely generated torsion $\mathbb{R}[x]$-module with $\sum \deg(p_i^{e_i}) = 3$.
By the Primary Decomposition Theorem, $V$ decomposes into a direct sum of cyclic modules:
\[
V \cong \bigoplus_{j=1}^k \mathbb{R}[x]/\langle p_j(x)^{r_j} \rangle,
\]
where each $p_j(x) \in \mathbb{R}[x]$ is an irreducible monic polynomial, and $\sum_{j=1}^k r_j \deg(p_j) = 3$.
<2>2. The irreducible monic polynomials in $\mathbb{R}[x]$ are:
- Linear polynomials: $x - \lambda$ for $\lambda \in \mathbb{R}$,
- Irreducible quadratic polynomials: $x^2 + ax + b$ with $a, b \in \mathbb{R}$ and $a^2 - 4b < 0$.

<1>3. Explicit list of isomorphism classes by elementary divisors:
<2>1. **Case I (Sum of degrees $1 + 1 + 1 = 3$):**
\[
V \cong \mathbb{R}[x]/\langle x - \lambda_1 \rangle \oplus \mathbb{R}[x]/\langle x - \lambda_2 \rangle \oplus \mathbb{R}[x]/\langle x - \lambda_3 \rangle,
\]
where $\lambda_1, \lambda_2, \lambda_3 \in \mathbb{R}$ (ordered $\lambda_1 \le \lambda_2 \le \lambda_3$).
The operator $T$ is diagonalizable over $\mathbb{R}$ with eigenvalues $\lambda_1, \lambda_2, \lambda_3$.
<2>2. **Case II (Sum of degrees $2 + 1 = 3$ with linear base):**
\[
V \cong \mathbb{R}[x]/\langle (x - \lambda_1)^2 \rangle \oplus \mathbb{R}[x]/\langle x - \lambda_2 \rangle,
\]
where $\lambda_1, \lambda_2 \in \mathbb{R}$.
The operator $T$ has a $2 \times 2$ Jordan block for $\lambda_1$ and a $1 \times 1$ block for $\lambda_2$.
<2>3. **Case III (Single cyclic factor of degree 3 with linear base):**
\[
V \cong \mathbb{R}[x]/\langle (x - \lambda)^3 \rangle,
\]
where $\lambda \in \mathbb{R}$.
The operator $T$ has a single $3 \times 3$ Jordan block for $\lambda$.
<2>4. **Case IV (Sum of degrees $2 + 1 = 3$ with irreducible quadratic):**
\[
V \cong \mathbb{R}[x]/\langle x^2 + ax + b \rangle \oplus \mathbb{R}[x]/\langle x - \lambda \rangle,
\]
where $\lambda, a, b \in \mathbb{R}$ with $a^2 - 4b < 0$.
The operator $T$ has a pair of complex conjugate eigenvalues $\frac{-a \pm i\sqrt{4b-a^2}}{2}$ and one real eigenvalue $\lambda$.

<1>4. Conclusion:
The $\mathbb{R}[x]$-module structures up to isomorphism are completely classified by the four families of elementary divisors above. Q.E.D.
:::
