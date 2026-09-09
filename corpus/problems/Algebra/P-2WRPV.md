---
schema: qual/card@1
id: P-2WRPV
kind: problem
title: Cokernel of a map $\ZZ^4\to\ZZ^3$
classification:
  areas:
  - algebra
  topics:
  - Smith Normal Form
  - Structure Theorem
  - Modules
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
Let $\phi:\ZZ^4\to\ZZ^3$ be represented in the standard bases by
\[
A=
\begin{pmatrix}
1&2&0&3\\
0&-3&3&1\\
-1&1&1&5
\end{pmatrix}.
\]
Compute $\operatorname{coker}(\phi)=\ZZ^3/\operatorname{im}(A)$ using Smith normal form.
:::

::: {.solution}
<1>1. The first determinantal divisor is $\Delta_1=1$.
::: {.proof}
The gcd of all entries of $A$ is $1$, since $A$ contains the entry $1$.
:::

<1>2. The second determinantal divisor is $\Delta_2=1$.
::: {.proof}
Among the $2\times2$ minors is
\[
\det
\begin{pmatrix}
1&3\\
0&1
\end{pmatrix}=1,
\]
using rows $1,2$ and columns $1,4$. Hence the gcd of all $2\times2$ minors is $1$.
:::

<1>3. The third determinantal divisor is $\Delta_3=1$.
::: {.proof}
The four $3\times3$ minors obtained by deleting one column are
\[
-12,\qquad -27,\qquad 23,\qquad 10.
\]
Their gcd is $1$; for instance
\[
\gcd(12,27,23,10)=1.
\]
Therefore $\Delta_3=1$.
:::

<1>4. The Smith invariant factors are
\[
d_1=1,\qquad d_2=1,\qquad d_3=1.
\]
::: {.proof}
For a full-rank integer matrix, the Smith invariant factors satisfy
\[
d_1=\Delta_1,\qquad
 d_1d_2=\Delta_2,\qquad
 d_1d_2d_3=\Delta_3.
\]
Using <1>1--<1>3 gives $d_1=d_2=d_3=1$.
:::

<1>5. Hence $\phi$ is surjective and
\[
\operatorname{coker}(\phi)=0.
\]
::: {.proof}
The Smith normal form is
\[
\operatorname{diag}(1,1,1)
\]
as a $3\times4$ matrix, with one additional zero column. Therefore
\[
\ZZ^3/\operatorname{im}(A)
\cong
\ZZ/1\ZZ\oplus\ZZ/1\ZZ\oplus\ZZ/1\ZZ
=0.
\]
:::
:::
