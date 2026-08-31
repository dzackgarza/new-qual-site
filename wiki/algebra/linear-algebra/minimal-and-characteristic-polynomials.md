---
title: Minimal and characteristic polynomials
order: 20
problems:
  topics:
  - Minimal and Characteristic Polynomials
---

# Minimal and characteristic polynomials

The two invariants every canonical-form question is asked in terms of.
Viewing $V$ as an $F[t]\dash$module through $p(t)\actson v \da p(A)v$ is what makes them the same object seen twice, and it is the reason the structure theorem for modules over a PID answers questions about matrices.

[[PR-EDD7U]]

:::{.remark title="Notation"}
\[
\min_A(x): \quad & \text{the minimal polynomial of } A \\
\chi_A(x): \quad & \text{the characteristic polynomial of } A
.\]

:::

[[D-GK5SF]]

[[D-QFYAC]]

[[FD-GOB47]]

## How they constrain each other

[[T-SJCF7]]

:::{.proof}
By minimality $\min_A$ divides $\chi_A$.
Every eigenvalue is a root of $\min_A$: for a nontrivial eigenpair $(\vector v_i, \lambda_i)$, linearity gives
$$
\min_A(\lambda_i)\vector v_i = \min_A(A)\vector v_i = \vector 0
,$$
forcing $\min_A(\lambda_i) = 0$.

:::

:::{.remark title="What this leaves free"}
$\min_A$ and $\chi_A$ have the same irreducible factors and $\min_A \divides \chi_A$, so all that is undetermined is the exponents.
That is exactly the data the Jordan blocks encode, and it is why a problem can hand you both polynomials and still not determine the matrix.

:::

## Finding the minimal polynomial

[[PR-UFVPY]]

:::{.remark title="In practice"}
Factor $\chi_A$, then test the divisors in increasing degree: the first monic $p$ with $p(A) = 0$ is $\min_A$.
The search is short because the only candidates are products of the known irreducible factors with exponents between one and their multiplicity in $\chi_A$.

:::

:::{.example title="Polynomial long division"}
For $f(x) \da x^3-6x^2+12x-8$, the rational root theorem leaves $\ts{\pm 8, \pm 4, \pm 2, \pm 1}$.
Since $f(2) = 0$, divide by $x-2$:

![](../../../../assets/assets/figures/2021-07-24_18-32-38.png)

and the remaining quadratic factor is $x^2-4x+4 = (x-2)^2$ (a perfect square), so $f(x) = (x-2)(x^2-4x+4) = (x-2)^3$.

:::

## Using the forms

[[L-VDLNM]]

[[L-Y5KNM]]

[[PR-OF7ZW]]
