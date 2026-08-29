---
schema: qual/card@1
id: P-GSFRX
kind: problem
title: Minimal and characteristic polynomials of a $5\times 5$ real matrix with eigenvalues
  $0,1\pm i,1\pm 2i$
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $L \in M_5(\mathbb{R})$ be a $5 \times 5$ real matrix with eigenvalues $0, 1 + i, 1 + 2i$.
Find the characteristic polynomial $\chi_L(x)$ and the minimal polynomial $\mu_L(x)$ of $L$ over $\mathbb{R}$.
:::

::: solution
**Goal:** Determine the characteristic polynomial $\chi_L(x)$ and minimal polynomial $\mu_L(x)$ for the $5 \times 5$ matrix $L$.

<1>1. Complete Set of Complex Eigenvalues (Spectrum):
    *Proof:*
    <2>1. Because $L$ is a real matrix ($L \in M_5(\mathbb{R})$), all coefficients of its characteristic polynomial $\chi_L(x)$ are real: $\chi_L(x) \in \mathbb{R}[x]$.
    <2>2. By the Complex Conjugate Root Theorem, non-real eigenvalues of real matrices must occur in complex conjugate pairs:
        - $1 + i$ is an eigenvalue $\implies 1 - i$ is an eigenvalue.
        - $1 + 2i$ is an eigenvalue $\implies 1 - 2i$ is an eigenvalue.
    <2>3. Together with the real eigenvalue $0$, the distinct eigenvalues are:
        $$\operatorname{Spec}(L) = \{0, 1 + i, 1 - i, 1 + 2i, 1 - 2i\}.$$
    <2>4. Since $L$ is a $5 \times 5$ matrix, the total algebraic multiplicity of all eigenvalues is at most 5.
    <2>5. We have found 5 distinct eigenvalues in $\mathbb{C}$, so each eigenvalue has algebraic multiplicity exactly 1.

<1>2. Characteristic Polynomial $\chi_L(x)$:
    *Proof:*
    <2>1. The characteristic polynomial is the product of $(x - \lambda)$ over all eigenvalues:
        $$\chi_L(x) = (x - 0)(x - (1+i))(x - (1-i))(x - (1+2i))(x - (1-2i)).$$
    <2>2. Combining conjugate pairs into real irreducible quadratics:
        $$(x - (1+i))(x - (1-i)) = (x-1)^2 - i^2 = x^2 - 2x + 1 + 1 = x^2 - 2x + 2,$$
        $$(x - (1+2i))(x - (1-2i)) = (x-1)^2 - (2i)^2 = x^2 - 2x + 1 + 4 = x^2 - 2x + 5.$$
    <2>3. Therefore:
        $$\chi_L(x) = x(x^2 - 2x + 2)(x^2 - 2x + 5) = x(x^4 - 4x^3 + 11x^2 - 14x + 10) = x^5 - 4x^4 + 11x^3 - 14x^2 + 10x.$$

<1>3. Minimal Polynomial $\mu_L(x)$:
    *Proof:*
    <2>1. Every eigenvalue $\lambda \in \operatorname{Spec}(L)$ must be a root of the minimal polynomial $\mu_L(x)$.
    <2>2. Because all 5 eigenvalues are distinct, $\mu_L(x)$ must have at least 5 distinct roots in $\mathbb{C}$.
    <2>3. Thus $\deg(\mu_L) \ge 5$.
    <2>4. On the other hand, the Cayley–Hamilton Theorem guarantees that $\mu_L(x) \mid \chi_L(x)$, so $\deg(\mu_L) \le \deg(\chi_L) = 5$.
    <2>5. Since both polynomials are monic of degree 5 sharing the same roots:
        $$\mu_L(x) = \chi_L(x) = x(x^2 - 2x + 2)(x^2 - 2x + 5).$$

<1>4. Conclusion:
    $\chi_L(x) = \mu_L(x) = x(x^2 - 2x + 2)(x^2 - 2x + 5) = x^5 - 4x^4 + 11x^3 - 14x^2 + 10x$. Q.E.D.
:::
