---
schema: qual/card@1
id: P-UW7CE
kind: problem
title: A complex matrix with $A^2=A$ is similar to a diagonal matrix
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $A\in M_n(\CC)$ with $A^2 = A$.
Show that $A$ is similar to a diagonal matrix, and exhibit an explicit diagonal matrix similar to $A$.
:::


::: {.solution}
<1>1. One has
\[
\mathbb C^n=\operatorname{im}A\oplus\ker A.
\]
::: {.proof}
For any \(v\in\mathbb C^n\), write
\[
v=Av+(v-Av).
\]
The first term lies in \(\operatorname{im}A\), while
\[
A(v-Av)=Av-A^2v=0,
\]
so the second lies in \(\ker A\). Thus the sum is all of \(\mathbb C^n\). If \(w\in\operatorname{im}A\cap\ker A\), write \(w=Au\). Then
\[
w=Au=A^2u=Aw=0,
\]
so the intersection is zero.
:::

<1>2. The matrix \(A\) acts as the identity on \(\operatorname{im}A\) and as zero on \(\ker A\).
::: {.proof}
If \(w=Av\in\operatorname{im}A\), then
\[
Aw=A^2v=Av=w.
\]
If \(w\in\ker A\), then \(Aw=0\) by definition.
:::

<1>3. Let \(r=\operatorname{rank}A=\dim\operatorname{im}A\). Choose a basis \(u_1,\dots,u_r\) of \(\operatorname{im}A\) and a basis \(v_1,\dots,v_{n-r}\) of \(\ker A\). In the combined basis, the matrix of \(A\) is
\[
\operatorname{diag}(I_r,0_{n-r}).
\]
::: {.proof}
By <1>1 the two bases concatenate to a basis of \(\mathbb C^n\). By <1>2, \(A u_i=u_i\) and \(A v_j=0\), so the matrix in that basis is exactly the displayed diagonal matrix.
:::

<1>4. Hence \(A\) is similar to a diagonal matrix, explicitly
\[
A\sim\operatorname{diag}(\underbrace{1,\dots,1}_{r},\underbrace{0,\dots,0}_{n-r}).
\]
::: {.proof}
Changing from the standard basis to the basis in <1>3 gives the required similarity.
:::
:::
