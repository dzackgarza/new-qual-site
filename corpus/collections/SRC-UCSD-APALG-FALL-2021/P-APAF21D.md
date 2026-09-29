---
schema: qual/card@1
id: P-APAF21D
kind: problem
title: Matrix $p$- and Frobenius norms; identities; rank-one norms; unitary invariance
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(a) Define the $p$-norm $\|A\|_p$ and Frobenius norm $\|A\|_F$ of a matrix $A\in M_{m,n}$.

(b) For every $A\in M_{m,n}$, establish the following identities:

(i) $\|A^H\|_2=\|A\|_2$.

(ii) $\|A^HA\|_2=\|A^H\|_2\|A\|_2$.

(c) Given two $n$-vectors $x$ and $y$ and the matrix $Z=xy^H$, show that
\[
\|Z\|_2=\|Z\|_F=\|x\|_2\|y\|_2.
\]

(d) Prove that the Frobenius norm and the matrix two-norm are invariant under unitary transformations, i.e., show that if $P$ and $Q$ are unitary matrices of suitable dimension, then
\[
\|A\|_2=\|PAQ\|_2
\quad\text{and}\quad
\|A\|_F=\|PAQ\|_F.
\]
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
The $p$-norm of $A$ is $\|A\|_p = \sup_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$ (the operator norm induced by the vector $p$-norm).

::: pf-proof
definition.
:::

:::

::: {.pf-step #frobenius-def}
The Frobenius norm is $\|A\|_F = \left(\sum_{i,j} |a_{ij}|^2\right)^{1/2} = \sqrt{\operatorname{tr}(A^H A)}$.

::: pf-proof
definition.
:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #norm-AH-eq-A}
(i) $\|A^H\|_2 = \|A\|_2$.

::: pf-proof
$\|A\|_2 = \sigma_{\max}(A)$ (the largest singular value), and $A^H$ has the same singular values as $A$, so $\|A^H\|_2 = \sigma_{\max}(A^H) = \sigma_{\max}(A) = \|A\|_2$.
:::

:::

::: {.pf-step #norm-AHA}
(ii) $\|A^H A\|_2 = \|A^H\|_2 \|A\|_2$.

::: pf-proof
$\|A^H A\|_2 = \sigma_{\max}(A^H A) = \sigma_{\max}(A)^2 = \|A\|_2^2 = \|A^H\|_2 \|A\|_2$ (using step [](#norm-AH-eq-A){.pf-ref} and the fact that the singular values of $A^H A$ are the squares of the singular values of $A$).
:::

:::

:::

**Part (c).**

::: pf

::: {.pf-step #Z-two-norm}
$\|Z\|_2 = \|x\|_2 \|y\|_2$.

::: pf-proof
$Z = xy^H$ has rank $1$, and its single nonzero singular value is $\|x\|_2 \|y\|_2$ (since $Z^H Z = y x^H x y^H = \|x\|_2^2 y y^H$, whose nonzero eigenvalue is $\|x\|_2^2 \|y\|_2^2$), so $\|Z\|_2 = \|x\|_2 \|y\|_2$.
:::

:::

::: {.pf-step #Z-frobenius-norm}
$\|Z\|_F = \|x\|_2 \|y\|_2$.

::: pf-proof
$\|Z\|_F^2 = \sum_{i,j} |x_i \bar y_j|^2 = \left(\sum_i |x_i|^2\right)\left(\sum_j |y_j|^2\right) = \|x\|_2^2 \|y\|_2^2$.
:::

:::

::: {.pf-step #Z-norms-equal}
Hence $\|Z\|_2 = \|Z\|_F = \|x\|_2 \|y\|_2$.

::: pf-proof
Steps [](#Z-two-norm){.pf-ref} and [](#Z-frobenius-norm){.pf-ref}.
:::

:::

:::

**Part (d).**

::: pf

::: {.pf-step #unitary-two-norm}
$\|A\|_2 = \|PAQ\|_2$.

::: pf-proof
$\|PAQ\|_2 = \sigma_{\max}(PAQ) = \sigma_{\max}(A) = \|A\|_2$, since multiplication by unitary matrices does not change the singular values.
:::

:::

::: {.pf-step #unitary-frobenius-norm}
$\|A\|_F = \|PAQ\|_F$.

::: pf-proof
$\|PAQ\|_F^2 = \operatorname{tr}((PAQ)^H (PAQ)) = \operatorname{tr}(Q^H A^H P^H P A Q) = \operatorname{tr}(Q^H A^H A Q) = \operatorname{tr}(A^H A) = \|A\|_F^2$ (using $P^H P = I$ and the cyclicity of the trace).
:::

:::

::: pf-qed
Step [](#frobenius-def){.pf-ref} (a), steps [](#norm-AH-eq-A){.pf-ref}–[](#norm-AHA){.pf-ref} (b), step [](#Z-norms-equal){.pf-ref} (c), and steps [](#unitary-two-norm){.pf-ref}–[](#unitary-frobenius-norm){.pf-ref} (d).
:::

:::
:::
