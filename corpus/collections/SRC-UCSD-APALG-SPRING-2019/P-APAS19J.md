---
schema: qual/card@1
id: P-APAS19J
kind: problem
title: Multiplicity-free isotypic decomposition iff $\mathrm{End}_A V$ is commutative
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $A$ be a finite-dimensional algebra over $\mathbb{C}$ and let $(V,\rho)$ be a finite-dimensional representation of $A$.
Show that the isotypic decomposition of $(V,\rho)$ is multiplicity free if and only if $\mathrm{End}_A V$ is commutative.
:::

::: {.solution}
Write the isotypic decomposition as
\[
V\cong \bigoplus_{i=1}^r S_i^{\oplus m_i},
\]
where the \(S_i\) are pairwise nonisomorphic irreducible \(A\)-modules and \(m_i\ge1\). By Schur's lemma,
\[
\operatorname{Hom}_A(S_i,S_j)=0\quad(i\ne j),
\qquad
\operatorname{End}_A(S_i)\cong\mathbb C.
\]
Therefore an \(A\)-endomorphism of \(V\) preserves each isotypic summand, and on \(S_i^{\oplus m_i}\) it is given by an arbitrary \(m_i\times m_i\) matrix of scalar maps. Hence
\[
\operatorname{End}_A(V)
\cong \prod_{i=1}^r M_{m_i}(\mathbb C).
\]

If the isotypic decomposition is multiplicity free, then every \(m_i=1\), so
\[
\operatorname{End}_A(V)\cong\mathbb C^r,
\]
which is commutative.

Conversely, if some \(m_i\ge2\), then \(M_{m_i}(\mathbb C)\) is noncommutative; for instance the matrix units \(E_{12}\) and \(E_{21}\) do not commute. Thus the product algebra \(\operatorname{End}_A(V)\) is noncommutative. Therefore \(\operatorname{End}_A(V)\) is commutative if and only if every multiplicity \(m_i\) equals \(1\), i.e. if and only if the isotypic decomposition of \(V\) is multiplicity free.
:::
