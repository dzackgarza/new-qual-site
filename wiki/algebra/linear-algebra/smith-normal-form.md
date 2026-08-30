---
title: Smith normal form
order: 50
problems:
  topics:
  - Smith Normal Form
  - Modules over PIDs
---

# Smith normal form

The form for a matrix over a PID rather than a field, and therefore the form that classifies finitely generated modules rather than linear maps.

::: {.fact}
For $A\in \Mat(m\times n; R)$ with $R$ a PID, $\SNF(A)$ is diagonal and its entries are the invariant factors.

To compute it: $\SNF(A) = \diag(a_i)$ where $a_i = d_i/d_{i-1}$ and $d_i$ is the $\gcd$ of the determinants of all $i\times i$ minors of $A$.

Two matrices are equivalent exactly when they have the same Smith normal form.
:::

::: {.remark}
The algorithm by row and column operations is in Dummit and Foote, page 479. The minors formula above is usually faster on an exam, since it needs no bookkeeping: each $d_i$ is one gcd computation.
:::

::: {.remark title="What it is for"}
Two questions, and they are the same question:

- **Classify a finitely generated module over a PID.** Present it as the cokernel of a matrix, take the Smith form, and read the invariant factors off the diagonal.
  This is how [[Algebra/modules/classify-this-module|Classify this module]] is carried out in practice.

- **Classify a finitely generated abelian group.** The same computation over $\ZZ$, where the invariant factors are the orders of the cyclic summands.

The reason both work is that the structure theorem is a statement about matrices over a PID, and Smith form is its normal form -- the same theorem that gives the [[Algebra/linear-algebra/rational-canonical-form|rational canonical form]] over $k[x]$.
:::
