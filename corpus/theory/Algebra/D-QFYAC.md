---
schema: qual/card@1
id: D-QFYAC
kind: definition
title: Characteristic polynomial
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Matrices
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $A\in\Mat_{n\times n}(k)$.
The \dfn{characteristic polynomial} of $A$ is
$$
\chi_A(x) \coloneqq \det(xI - A)\in k[x].
$$
It is monic of degree $n$; some texts use $\det(A-xI)=(-1)^n\chi_A(x)$ instead.
:::

::: {.remark}
If $\SNF(xI-A)=\diag(d_1,\ldots,d_n)$ is the Smith normal form of $xI-A$ over $k[x]$, with monic invariant factors $d_i$, then $\det(xI-A)$ and $d_1\cdots d_n$ are monic and differ by a unit of $k[x]$, hence are equal, and
$$
\chi_A(x)=\det(xI-A)=\det\SNF(xI-A).
$$
:::
