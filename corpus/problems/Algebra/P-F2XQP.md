---
schema: qual/card@1
id: P-F2XQP
kind: problem
title: Polar decomposition of operators on a Hilbert space
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Consider the simple operator on C given by multiplication by a complex number.
It decomposes into a stretch and a rotation.
What is the generalisation of this to operators on a Hilbert space?
:::

::: {.solution}
<1>1. Statement of the Polar Decomposition Theorem:
<2>1. The generalisation of the polar form $z = e^{i\theta}|z|$ of complex numbers to bounded linear operators on a complex Hilbert space $H$ is the **Polar Decomposition**:
Every bounded linear operator $T \in B(H)$ can be uniquely factored as:
\[
T = U |T|,
\]
where:
- $|T| = \sqrt{T^* T} \in B(H)$ is the unique positive semidefinite self-adjoint operator ($\langle |T|x, x \rangle \ge 0$), representing the non-negative stretch factor.
- $U \in B(H)$ is a **partial isometry** satisfying $\ker(U) = \ker(T) = \ker(|T|)$, representing the rotation/unitary factor.
- The initial space of $U$ is $(\ker T)^\perp = \overline{\operatorname{im}(|T|)}$, and the final space of $U$ is $\overline{\operatorname{im}(T)}$.
Proof: functional analysis generalization of polar coordinates.

<1>2. Proof of Existence:
<2>1. For all $x \in H$, compute the norm of $|T|x$:
\[
\| |T|x \|^2 = \langle |T|x, |T|x \rangle = \langle |T|^2 x, x \rangle = \langle T^* T x, x \rangle = \langle Tx, Tx \rangle = \|Tx\|^2.
\]
Thus $\| |T|x \| = \|Tx\|$ for all $x \in H$.
Proof: definition of the positive square root $|T| = \sqrt{T^* T}$.
<2>2. In particular, $\ker(|T|) = \ker(T)$, and $\overline{\operatorname{im}(|T|)} = (\ker |T|)^\perp = (\ker T)^\perp$.
Proof: norm equality implies equal kernels.
<2>3. Define the linear map $U_0: \operatorname{im}(|T|) \to \operatorname{im}(T)$ by:
\[
U_0(|T|x) = Tx \quad \text{for all } x \in H.
\]
$U_0$ is well-defined and isometric because $\|U_0(|T|x)\| = \|Tx\| = \||T|x\|$.
Proof: <2>1.
<2>4. Since $U_0$ is an isometry on the dense subspace $\operatorname{im}(|T|)$ of $\overline{\operatorname{im}(|T|)}$, it extends uniquely to an isometry $U_1: \overline{\operatorname{im}(|T|)} \to \overline{\operatorname{im}(T)}$.
Proof: continuous extension of uniformly continuous maps.
<2>5. Define $U \in B(H)$ by:
\[
U(y + z) = U_1(y) \quad \text{for } y \in \overline{\operatorname{im}(|T|)}, \, z \in \ker(|T|).
\]
By construction, $U$ is a partial isometry with initial space $\overline{\operatorname{im}(|T|)}$ and $U|T|x = U_1(|T|x) = Tx$, so $T = U|T|$.
Proof: orthogonal decomposition $H = \overline{\operatorname{im}(|T|)} \oplus \ker(|T|)$.

<1>3. Uniqueness and the Invertible Case:
<2>1. If $T = U |T|$ is any polar decomposition with $\ker(U) = \ker(|T|)$, then $T^* T = |T| U^* U |T| = |T|^2$ (since $U^* U$ is the orthogonal projection onto $\overline{\operatorname{im}(|T|)}$).
Since $|T| \ge 0$, $|T| = \sqrt{T^* T}$ is unique by the uniqueness of positive square roots.
Proof: Spectral Theorem for positive operators.
<2>2. On $\operatorname{im}(|T|)$, $U(|T|x) = Tx$ is forced by $T = U|T|$, and $U = 0$ on $\ker(|T|)$ is forced by $\ker(U) = \ker(|T|)$, so $U$ is unique.
Proof: determination on an orthogonal decomposition of $H$.
<2>3. If $T$ is invertible, $\ker(T) = \{0\}$ and $\operatorname{im}(T) = H$, so $U$ is a **unitary operator** ($U^* U = U U^* = I$).
Proof: surjectivity and injectivity of isometric operators.

<1>4. Conclusion:
The generalization is the polar decomposition $T = U |T|$, decomposing $T$ into a positive stretch $|T| = \sqrt{T^* T}$ and a partial isometry $U$. Q.E.D.
Proof: <1>1 through <1>3.
:::
