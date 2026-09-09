---
schema: qual/card@1
id: P-ALGS05B
kind: problem
title: "A triangular matrix is normal if and only if it is diagonal"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Prove that a triangular matrix is normal if and only if it is diagonal.
:::


::: {.solution}
<1>1. It suffices to treat upper triangular matrices.
::: {.proof}
If \(A\) is lower triangular and normal, then \(A^*\) is upper triangular and normal. If \(A^*\) is diagonal, then so is \(A\). Thus we assume that \(A\) is upper triangular.
:::

<1>2. If \(A\) is upper triangular and normal, then every off-diagonal entry in its first row is zero.
::: {.proof}
Write \(A=(a_{ij})\) and let \(e_1\) be the first standard basis vector. Since \(A\) is upper triangular,
\[
Ae_1=a_{11}e_1,
\]
so \(\|Ae_1\|^2=|a_{11}|^2\). On the other hand,
\[
A^*e_1=\overline{a_{11}}e_1+\overline{a_{12}}e_2+\cdots+\overline{a_{1n}}e_n,
\]
so
\[
\|A^*e_1\|^2=|a_{11}|^2+\sum_{j=2}^n |a_{1j}|^2.
\]
Normality gives \(A^*A=AA^*\), hence
\[
\|Av\|^2=\langle A^*Av,v\rangle=\langle AA^*v,v\rangle=\|A^*v\|^2
\]
for every \(v\). Taking \(v=e_1\) gives \(\sum_{j=2}^n|a_{1j}|^2=0\), hence \(a_{1j}=0\) for all \(j>1\).
:::

<1>3. Therefore \(A\) has block form
\[
A=\begin{pmatrix}a_{11}&0\\0&B\end{pmatrix},
\]
where \(B\) is upper triangular and normal.
::: {.proof}
Upper triangularity already makes the entries below \(a_{11}\) in the first column zero, and <1>2 makes the entries to its right in the first row zero. Thus \(A=a_{11}\oplus B\). From
\[
A^*A=AA^*
\]
one obtains blockwise \(B^*B=BB^*\), so \(B\) is normal.
:::

<1>4. By induction on the size, every upper triangular normal matrix is diagonal.
::: {.proof}
The assertion is trivial in size \(1\). For size \(n\), <1>3 reduces the problem to the upper triangular normal \((n-1)\times(n-1)\) block \(B\), which is diagonal by induction. Hence \(A\) is diagonal.
:::

<1>5. Conversely, every diagonal matrix is normal.
::: {.proof}
If \(D\) is diagonal, then \(D^*\) is diagonal and \(D^*D=DD^*\) entrywise. Therefore \(D\) is normal.
:::
:::
