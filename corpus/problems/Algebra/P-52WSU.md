---
schema: qual/card@1
id: P-52WSU
kind: problem
title: Toeplitz operator
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is a Toeplitz operator? Define the Hardy space $H^2(\mathbb{T})$, the Toeplitz operator $T_\varphi$ associated with a symbol $\varphi \in L^\infty(\mathbb{T})$, and describe its matrix representation.
:::

::: {.solution}
<1>1. Setting: Hardy Space $H^2(\mathbb{T})$ and the Szegő Projection:
<2>1. Let $\mathbb{T} = \{z \in \mathbb{C} \mid |z| = 1\}$ be the unit circle with normalized Lebesgue measure $\frac{d\theta}{2\pi}$.
The Hilbert space $L^2(\mathbb{T})$ has standard orthonormal basis $\{e_n(z) = z^n\}_{n=-\infty}^\infty$.
Proof: Fourier analysis on the torus $\mathbb{T}$.
<2>2. The **Hardy space** $H^2(\mathbb{T})$ is the closed subspace spanned by the non-negative Fourier modes:
\[
H^2(\mathbb{T}) = \overline{\operatorname{span}}\{z^n \mid n \ge 0\} = \left\{ f(z) = \sum_{n=0}^\infty c_n z^n \in L^2(\mathbb{T}) \;\middle|\; \sum_{n=0}^\infty |c_n|^2 < \infty \right\}.
\]
Proof: definition of Hardy space $H^2(\mathbb{T})$.
<2>3. The **Szegő projection** $P: L^2(\mathbb{T}) \to H^2(\mathbb{T})$ is the orthogonal projection onto $H^2(\mathbb{T})$:
\[
P\left(\sum_{n=-\infty}^\infty c_n z^n\right) = \sum_{n=0}^\infty c_n z^n.
\]
Proof: orthogonal projection in Hilbert spaces.

<1>2. Definition of the Toeplitz Operator:
<2>1. Given a symbol $\varphi \in L^\infty(\mathbb{T})$, the multiplication operator $M_\varphi: L^2(\mathbb{T}) \to L^2(\mathbb{T})$ is defined by $M_\varphi(f) = \varphi \cdot f$.
Proof: definition of multiplication operator.
<2>2. The **Toeplitz operator** with symbol $\varphi$, denoted $T_\varphi: H^2(\mathbb{T}) \to H^2(\mathbb{T})$, is defined by:
\[
T_\varphi(f) = P(\varphi \cdot f) \quad \text{for } f \in H^2(\mathbb{T}).
\]
Proof: definition of Toeplitz operator.
<2>3. Because $\|P\| = 1$ and $\|M_\varphi\| = \|\varphi\|_\infty$, $T_\varphi$ is a bounded linear operator on $H^2(\mathbb{T})$ with operator norm $\|T_\varphi\| = \|\varphi\|_\infty$.
Proof: boundedness of composition of bounded operators.

<1>3. Matrix Representation of $T_\varphi$:
<2>1. Let $\varphi(z) \sim \sum_{k=-\infty}^\infty a_k z^k$ be the Fourier series of $\varphi$, so $a_k = \frac{1}{2\pi}\int_0^{2\pi}\varphi(e^{i\theta})e^{-ik\theta}d\theta$.
Proof: Fourier coefficients of $L^\infty$ functions.
<2>2. Apply $T_\varphi$ to the orthonormal basis vector $e_j(z) = z^j$ for $j \ge 0$:
\[
T_\varphi(z^j) = P\left( \sum_{k=-\infty}^\infty a_k z^{j+k} \right) = \sum_{j+k \ge 0} a_k z^{j+k} = \sum_{i=0}^\infty a_{i-j} z^i.
\]
Proof: applying projection $P$ to Fourier series.
<2>3. Thus, the $(i, j)$-entry of the matrix of $T_\varphi$ with respect to the basis $\{1, z, z^2, \dots\}$ is:
\[
\langle T_\varphi(z^j), z^i \rangle = a_{i-j}.
\]
This produces a semi-infinite **Toeplitz matrix** (constant along diagonals):
\[
[T_\varphi] = \begin{pmatrix}
a_0 & a_{-1} & a_{-2} & a_{-3} & \cdots \\
a_1 & a_0 & a_{-1} & a_{-2} & \cdots \\
a_2 & a_1 & a_0 & a_{-1} & \cdots \\
a_3 & a_2 & a_1 & a_0 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}.
\]
Proof: matrix entry calculation $\langle T_\varphi e_j, e_i \rangle = a_{i-j}$.

<1>4. Key Algebraic Properties:
<2>1. Linearity in symbol: $T_{\alpha \varphi + \beta \psi} = \alpha T_\varphi + \beta T_\psi$.
<2>2. Adjoint: $T_\varphi^* = T_{\overline{\varphi}}$.
<2>3. Shift operator: For $\varphi(z) = z$, $T_z = S$ is the unilateral forward shift $S(z^n) = z^{n+1}$.
<2>4. Characterization (Brown–Halmos Theorem): A bounded linear operator $T$ on $H^2(\mathbb{T})$ is a Toeplitz operator if and only if $S^* T S = T$, where $S = T_z$.
Proof: Brown–Halmos algebraic characterization of Toeplitz operators.

<1>5. Conclusion:
A Toeplitz operator is $T_\varphi = P M_\varphi|_{H^2(\mathbb{T})}$, represented by the semi-infinite constant-diagonal matrix $(a_{i-j})_{i,j \ge 0}$. Q.E.D.
Proof: <1>1 through <1>4.
:::
