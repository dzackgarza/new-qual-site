---
schema: qual/card@1
id: P-UN3G3
kind: problem
title: The number and sizes of Jordan blocks
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $A \in M_n(\mathbb{C})$ (or an algebraically closed field).
How do you determine the **number** and **sizes** of the blocks in the Jordan Canonical Form of $A$?
:::

::: solution
Fix an eigenvalue $\lambda$ and set
\[
d_k=\dim\ker(A-\lambda I)^k,
\qquad d_0=0.
\]
If the Jordan blocks for $\lambda$ have sizes $m_1,\dots,m_r$, then
\[
d_k=\sum_{j=1}^r\min(k,m_j).
\]
Therefore
\[
d_k-d_{k-1}
\]
is exactly the number of Jordan blocks of size at least $k$.

Consequently:
\[
\#\{\text{blocks for }\lambda\}=d_1,
\]
\[
\#\{\text{blocks of size exactly }k\}
=(d_k-d_{k-1})-(d_{k+1}-d_k)
=2d_k-d_{k-1}-d_{k+1}.
\]
The largest block size is the least $m$ for which
\[
d_m=d_{m+1},
\]
and equivalently it is the exponent of $(x-\lambda)$ in the minimal polynomial of $A$.

Thus the nullities of the powers $(A-\lambda I)^k$, for each eigenvalue $\lambda$, determine all Jordan block numbers and sizes.
:::
