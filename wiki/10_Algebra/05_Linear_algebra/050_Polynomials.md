---
order: 50
---

# Polynomials in Linear Algebra

## Using Canonical Forms

[[L-VDLNM]]

[[L-Y5KNM]]

[[PR-OF7ZW]]

## Minimal / Characteristic Polynomials

[[PR-FYXFF]]

:::{.remark}
Fix some notation:
\[
\min_A(x): \quad & \text{The minimal polynomial of } A \\
\chi_A(x): \quad & \text{The characteristic polynomial of } A
.\]

:::

[[D-GK5SF]]

[[D-QFYAC]]

:::{.fact}
If $A$ is upper triangular, then $\det(A) = \prod_{i} a_{ii}$

:::

[[T-SJCF7]]

:::{.proof title="?"}
By minimality, $\min_A$ divides $\chi_A$. 
Every $\lambda_i$ is a root of $\min_A(x)$: 
Let $(\vector v_i, \lambda_i)$ be a nontrivial eigenpair. 
Then by linearity,
$$
\min_A(\lambda_i)\vector v_i = \min_A(A)\vector v_i = \vector 0
,$$ 
which forces $\min_A(\lambda_i) = 0$.

:::

## Finding Minimal Polynomials

[[PR-UFVPY]]

