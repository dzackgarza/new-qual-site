---
schema: qual/card@1
id: P-2HERP
kind: problem
title: Eigenvalues of skew-symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Matrices
  - Bilinear Forms
relations: []
review: draft
---

::: {.problem}
What can you say about the eigenvalues of a real skew-symmetric matrix?
:::

::: {.solution}
Let $A\in M_n(\RR)$ satisfy $A^t=-A$, regarded as a complex matrix. Write $\inner{v}{w}=\sum_i v_i\overline{w_i}$ for the standard Hermitian inner product on $\CC^n$; then $\inner{Av}{w}=\inner{v}{A^tw}=-\inner{v}{Aw}$ because $A$ is real.

::: pf

::: {.pf-step #imaginary}

Every complex eigenvalue of $A$ is purely imaginary (possibly $0$).

::: pf-proof

If $Av=\lambda v$ with $0\ne v\in\CC^n$, then
$$
\lambda\inner{v}{v}=\inner{Av}{v}=-\inner{v}{Av}=-\overline\lambda\inner{v}{v}.
$$
Since $\inner{v}{v}>0$, $\lambda=-\overline\lambda$, so $\operatorname{Re}\lambda=0$.

:::

:::

::: {.pf-step #pairs}

The nonzero eigenvalues occur in conjugate pairs $\pm i\mu$ with $\mu\in\RR$, $\mu\ne0$, of equal multiplicity; the only possible real eigenvalue is $0$.

::: pf-proof

The characteristic polynomial of $A$ has real coefficients, so its nonreal roots come in conjugate pairs with equal multiplicity. By step [](#imaginary){.pf-ref}, the conjugate of $i\mu$ is $-i\mu$, and a real purely imaginary number is $0$.

:::

:::

::: pf-step

If $n$ is odd, then $0$ is an eigenvalue of $A$, so $A$ is singular.

::: pf-proof

By step [](#pairs){.pf-ref}, the nonzero eigenvalues, counted with multiplicity, are even in number. Since $n$ is odd, at least one eigenvalue is $0$.

:::

:::

::: pf-step

$A$ is unitarily diagonalizable over $\CC$ with purely imaginary diagonal entries.

::: pf-proof

The matrix $iA$ satisfies $\overline{(iA)}^t=-iA^t=iA$, so it is Hermitian. The spectral theorem diagonalizes $iA$, hence $A$, by a unitary matrix, and the diagonal entries are eigenvalues of $A$, which are purely imaginary by step [](#imaginary){.pf-ref}.

:::

:::

:::

:::
