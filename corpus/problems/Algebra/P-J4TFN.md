---
schema: qual/card@1
id: P-J4TFN
kind: problem
title: Eigenvalues of a linear map preserving a nondegenerate alternating form come
  in pairs $k,1/k$
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Eigenvalues and Eigenvectors
  - Matrix Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $V$ be a finite-dimensional vector space over a field $F$, and let $\omega: V \times V \to F$ be a **nondegenerate alternating bilinear form** on $V$.
Suppose $T: V \to V$ is a linear transformation that preserves $\omega$, i.e.
$$\omega(T(u), T(v)) = \omega(u, v) \quad \text{for all } u, v \in V.$$
Prove that if $\lambda \in F$ (or in an algebraic closure $\bar{F}$) is an eigenvalue of $T$, then $\lambda \ne 0$ and $\lambda^{-1} = 1/\lambda$ is also an eigenvalue of $T$ (with the same algebraic and geometric multiplicity).
:::

::: solution
**Goal:** Prove that symplectic operators have eigenvalues coming in reciprocal pairs $\lambda, \lambda^{-1}$ using matrix congruence and characteristic polynomials.

<1>1. Matrix Representation of Symplectic Transformation:
    *Proof:*
    <2>1. Choose an arbitrary basis of $V$, and let $J$ be the matrix of the alternating form $\omega$ with respect to this basis.
    <2>2. Since $\omega$ is alternating, $J^T = -J$.
    <2>3. Since $\omega$ is **nondegenerate**, the matrix $J$ is invertible:
        $$\det(J) \ne 0 \implies J^{-1} \text{ exists and } (J^{-1})^T = (J^T)^{-1} = -J^{-1}.$$
    <2>4. Let $M$ be the matrix of the linear transformation $T$ in this basis.
    <2>5. The preservation condition $\omega(Tu, Tv) = \omega(u, v)$ in matrix form is:
        $$M^T J M = J.$$

<1>2. Invertibility of $M$ and $\lambda \ne 0$:
    *Proof:*
    <2>1. Taking determinants of both sides:
        $$\det(M^T) \det(J) \det(M) = \det(J) \implies (\det M)^2 \det(J) = \det(J).$$
    <2>2. Since $\det(J) \ne 0$, we can cancel $\det(J)$ to get:
        $$(\det M)^2 = 1 \implies \det(M) = \pm 1 \ne 0 \quad (\text{in fact } \det M = 1 \text{ for symplectic matrices}).$$
    <2>3. Since $\det(M) \ne 0$, $M$ is invertible, so $\lambda = 0$ cannot be an eigenvalue of $T$.

<1>3. Similarity Between $M$ and $M^{-1}$:
    *Proof:*
    <2>1. From $M^T J M = J$, multiplying on the left by $J^{-1}$ and on the right by $M^{-1}$:
        $$J^{-1} M^T J = M^{-1}.$$
    <2>2. Taking transposes of both sides:
        $$(J^{-1} M^T J)^T = (M^{-1})^T \implies J^T M (J^{-1})^T = (M^{-1})^T.$$
    <2>3. Using $J^T = -J$ and $(J^{-1})^T = -J^{-1}$:
        $$(-J) M (-J^{-1}) = (M^{-1})^T \implies J M J^{-1} = (M^{-1})^T.$$
    <2>4. Thus $(M^{-1})^T$ is **similar** to $M$ via the change-of-basis matrix $J$.
    <2>5. Furthermore, any square matrix is similar to its transpose ($M^{-1} \sim (M^{-1})^T$).
    <2>6. Therefore, $M$ is **similar to $M^{-1}$**:
        $$M \sim M^{-1}.$$

<1>4. Eigenvalue Reciprocal Pairing:
    *Proof:*
    <2>1. Since $M$ and $M^{-1}$ are similar, they share the **exact same characteristic polynomial**:
        $$p_M(t) = p_{M^{-1}}(t).$$
    <2>2. If $\lambda$ is an eigenvalue of $M$ with eigenvector $v$ ($M v = \lambda v$), then:
        $$M^{-1} v = \lambda^{-1} v.$$
    <2>3. Thus $\lambda^{-1} = 1/\lambda$ is an eigenvalue of $M^{-1}$.
    <2>4. Since $M \sim M^{-1}$, the spectrum of $M$ equals the spectrum of $M^{-1}$.
    <2>5. Therefore, $\lambda^{-1} = 1/\lambda$ is also an eigenvalue of $M$ (with identical algebraic and geometric multiplicities).

<1>5. Conclusion:
    Symplectic transformations satisfy $M \sim M^{-1}$, so eigenvalues occur in inverse pairs $\lambda$ and $1/\lambda$. Q.E.D.
:::
