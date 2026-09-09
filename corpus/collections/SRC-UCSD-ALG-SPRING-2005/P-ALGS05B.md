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
<1>1. Every diagonal matrix is normal.
::: {.proof}
If $D$ is diagonal, then $D^*$ is diagonal and
\[
DD^*=D^*D,
\]
entry by entry.
:::

<1>2. Let $A=(a_{ij})\in M_n(\mathbb C)$ be upper triangular and normal. Then
\[
a_{1j}=0\qquad(j>1).
\]
::: {.proof}
For every vector $v$, normality gives
\[
\|Av\|^2=\langle A^*Av,v\rangle
=\langle AA^*v,v\rangle
=\|A^*v\|^2.
\]
Take $v=e_1$. Since $A$ is upper triangular,
\[
Ae_1=a_{11}e_1,
\]
whereas
\[
A^*e_1=\overline{a_{11}}e_1+\overline{a_{12}}e_2+\cdots+\overline{a_{1n}}e_n.
\]
Hence
\[
|a_{11}|^2
=\|Ae_1\|^2
=\|A^*e_1\|^2
=|a_{11}|^2+\sum_{j=2}^n|a_{1j}|^2.
\]
Thus every $a_{1j}$ with $j>1$ is zero.
:::

<1>3. With the first row off the diagonal zero, $A$ has block form
\[
A=\begin{pmatrix}a_{11}&0\\0&B\end{pmatrix},
\]
where $B$ is upper triangular and normal.
::: {.proof}
Upper triangularity already gives $a_{i1}=0$ for $i>1$, and <1>2 gives $a_{1j}=0$ for $j>1$. Therefore $A$ is block diagonal as displayed. From
\[
AA^*=A^*A
\]
and block multiplication, the lower-right blocks satisfy
\[
BB^*=B^*B,
\]
so $B$ is normal.
:::

<1>4. Every upper-triangular normal matrix is diagonal.
::: {.proof}
Induct on $n$. The assertion is immediate for $n=1$. For $n>1$, <1>3 gives a normal upper-triangular $(n-1)\times(n-1)$ block $B$. By induction $B$ is diagonal, hence so is $A$.
:::

<1>5. Every lower-triangular normal matrix is diagonal as well.
::: {.proof}
If $A$ is lower triangular and normal, then $A^*$ is upper triangular and normal. By <1>4, $A^*$ is diagonal, hence $A$ is diagonal.
:::

<1>6. Therefore a triangular matrix is normal if and only if it is diagonal.
::: {.proof}
Combine <1>1, <1>4, and <1>5.
:::
:::
