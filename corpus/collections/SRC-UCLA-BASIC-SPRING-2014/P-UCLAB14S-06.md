---
schema: qual/card@1
id: P-UCLAB14S-06
kind: problem
title: Adjoint of a normal matrix as a polynomial
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 6. Show that if $A\in M_{n,n}(\mathbb C)$ is normal, then
\[
A^*=P(A)
\]
for some polynomial $P(x)$ with complex coefficients.
Here $A^*$ is the conjugate transpose of $A$.
:::

::: pf

::: pf-step

Since $A$ is normal, the spectral theorem gives a unitary matrix $U$ and distinct eigenvalues
\[
\lambda_1,\ldots,\lambda_r
\]
such that
\[
A=UDU^*,
\]
where $D$ is diagonal and every diagonal entry of $D$ is one of the $\lambda_i$.


::: pf-proof

The spectral theorem for normal complex matrices says precisely that a normal matrix is unitarily diagonalizable. Group the diagonal entries by their distinct values to obtain $\lambda_1,\ldots,\lambda_r$.

:::

:::

::: pf-step

There exists a polynomial $P\in\mathbb C[x]$ satisfying
\[
P(\lambda_i)=\overline{\lambda_i}
\qquad(i=1,\ldots,r).
\]


::: pf-proof

The points $\lambda_i$ are distinct, so Lagrange interpolation gives the explicit polynomial
\[
P(x)=\sum_{i=1}^r
\overline{\lambda_i}
\prod_{j\ne i}\frac{x-\lambda_j}{\lambda_i-\lambda_j}.
\]
Substituting $x=\lambda_i$ leaves only the $i$th summand and gives $P(\lambda_i)=\overline{\lambda_i}$.

:::

:::

::: pf-step

Applying $P$ to the diagonalization gives
\[
P(A)=UP(D)U^*.
\]


::: pf-proof

For every nonnegative integer $k$,
\[
A^k=(UDU^*)^k=UD^kU^*.
\]
Taking the same linear combination of powers prescribed by the polynomial $P$ yields the displayed identity.

:::

:::

::: pf-step

The interpolation property implies
\[
P(D)=D^*.
\]


::: pf-proof

If the $j$th diagonal entry of $D$ is $\lambda_i$, then the $j$th diagonal entry of $P(D)$ is $P(\lambda_i)=\overline{\lambda_i}$ by step <1>2. These are exactly the diagonal entries of $D^*$.

:::

:::

::: pf-step

Therefore
\[
P(A)=UD^*U^*=A^*.
\]


::: pf-proof

Steps <1>3--<1>4 give $P(A)=UD^*U^*$. On the other hand,
\[
A^*=(UDU^*)^*=UD^*U^*,
\]
because $U$ is unitary.

:::

:::

::: pf-step

Hence
\[
\boxed{A^*=P(A)}
\]
for the polynomial $P$ constructed in step <1>2.


::: pf-proof

This is exactly step <1>5.

:::

:::

::: pf-qed

Step <1>6 proves the assertion.

:::

:::
