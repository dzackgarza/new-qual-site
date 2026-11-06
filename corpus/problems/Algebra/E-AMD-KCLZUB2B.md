---
schema: qual/card@1
id: E-AMD-KCLZUB2B
kind: problem
title: A linear operator is diagonalizable iff $V$ is the direct sum of its eigenspaces
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the equivalence to the eigenbasis/direct-sum argument.
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (an
    equivalence, no repair needed), and the existing prose against a fresh
    re-derivation: the forward direction takes a basis of eigenvectors, groups it by
    eigenvalue, and gets spanning from the partition, with directness from the
    independence of eigenvectors belonging to distinct eigenvalues; the reverse
    direction takes a basis of each eigenspace, whose union spans because the sum is
    V and is independent because the sum is direct, hence a basis of eigenvectors. All
    correct. What the prose had compressed and the proof now supplies: the linear
    independence argument for eigenvectors of distinct eigenvalues (minimal relation
    plus one application of T), which is what makes the sum direct rather than merely
    spanning. No source solution is retained for this card, so no source comparison
    was made. What was not checked: any printed source.
---

::: {.exercise}
Show that a linear map $T:V\to V$ is diagonalizable if and only if
$$
V=\bigoplus_\lambda \ker(T-\lambda I),
$$
where the sum runs over the eigenvalues of $T$ in the base field.
:::

::: {.solution}
Let $V$ be a finite-dimensional vector space over a field $k$, let $T\colon V\to V$ be linear, and let $E_\lambda=\ker(T-\lambda\Id)$ be the eigenspace of the eigenvalue $\lambda\in k$; a linear map is diagonalizable when $V$ has a basis of eigenvectors of $T$.

::: pf

::: {.pf-step #independent}
Vectors lying in eigenspaces of distinct eigenvalues are linearly independent: if $v_1,\ldots,v_m$ are nonzero with $Tv_i=\lambda_iv_i$ for pairwise distinct $\lambda_i$, then they are independent.

::: pf-proof
Suppose a relation $\sum_i c_iv_i=0$ holds with not all $c_i$ zero, and take one of minimal length $m$. Then $m\geq2$. Applying $T$ gives $\sum_ic_i\lambda_iv_i=0$, and subtracting $\lambda_1$ times the original relation gives $\sum_{i\geq2}c_i(\lambda_i-\lambda_1)v_i=0$. The coefficients $c_i(\lambda_i-\lambda_1)$ are nonzero for $i\geq2$ because the eigenvalues are distinct and $c_i\neq0$, so this is a shorter nontrivial relation, contradicting minimality. Hence no nontrivial relation exists.
:::

:::

::: {.pf-step #forward}
If $T$ is diagonalizable then $V=\bigoplus_\lambda E_\lambda$.

::: pf-proof
Diagonalizability gives a basis $v_1,\ldots,v_n$ of $V$ of eigenvectors; let $\lambda(i)$ be the eigenvalue of $v_i$ and group the basis vectors by that value. A vector with eigenvalue $\lambda$ lies in $E_\lambda$ by definition, so the $E_\lambda$ together span $V$; and if $\sum_\lambda w_\lambda=0$ with $w_\lambda\in E_\lambda$, then each nonzero $w_\lambda$ is an eigenvector for the distinct eigenvalues $\lambda$, so step [](#independent){.pf-ref} forces all $w_\lambda=0$. Together, spanning and independence of the summands are exactly the statement that the sum is direct and equals $V$.
:::

:::

::: {.pf-step #backward}
If $V=\bigoplus_\lambda E_\lambda$ then $T$ is diagonalizable.

::: pf-proof
For each eigenvalue $\lambda$ choose a basis of $E_\lambda$. The union of these bases is a set of eigenvectors of $T$; it spans $V$ because the sum of the $E_\lambda$ is $V$, and it is linearly independent because the sum is direct (an element of $E_\lambda$ that also lies in the sum of the others is $0$). So the union is a basis of $V$ consisting of eigenvectors, and the matrix of $T$ in this basis is diagonal, with the eigenvalue $\lambda$ repeated as often as $\dim E_\lambda$.
:::

:::

::: {.pf-step}
$T$ is diagonalizable if and only if $V=\bigoplus_\lambda\ker(T-\lambda\Id)$.

::: pf-proof
Step [](#forward){.pf-ref} gives one implication and step [](#backward){.pf-ref} the other.
:::

:::

:::
:::
