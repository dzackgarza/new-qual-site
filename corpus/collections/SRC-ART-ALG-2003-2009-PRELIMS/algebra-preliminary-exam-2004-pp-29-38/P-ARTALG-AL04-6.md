---
schema: qual/card@1
id: P-ARTALG-AL04-6
kind: problem
title: 'A cyclic $2\times2$ matrix and canonical forms with characteristic polynomial $(x^2+1)(x+1)^2$'
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked PDF page 32 (printed page 4), Rings 2. Restored omitted part (a), whose matrix has rows (2,3) and (7,1), and verified every factor and the coefficient field in part (b)."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked AP=PC for the 2-by-2 matrix, exhausted the invariant-factor chains in part (b), and checked the coefficients and distinct minimal polynomials of both displayed forms."
---

::: {.problem}
(a) Find the rational canonical form of
$$
\begin{pmatrix}2&3\\7&1\end{pmatrix}.
$$

(b) Find all possible rational canonical forms for 4-by-4 matrices over the complex numbers whose characteristic polynomial is $(x^2+1)(x+1)^2$.
:::

::: {.solution}
For a monic polynomial $f=x^d+c_{d-1}x^{d-1}+\cdots+c_0$,
write $C(f)$ for its companion matrix with ones on the subdiagonal
and last column $(-c_0,\ldots,-c_{d-1})^{\mathsf T}$.

<1>1. The answer to part (a) is
$$
C(x^2-3x-19)=\begin{pmatrix}0&19\\1&3\end{pmatrix}.
$$

::: {.proof}
Let $A$ be the given matrix. Its characteristic polynomial is
$$
\det(xI-A)=(x-2)(x-1)-21=x^2-3x-19.
$$
For $v=(1,0)^{\mathsf T}$, the columns $v,Av$ form the matrix
$$
P=\begin{pmatrix}1&2\\0&7\end{pmatrix},\qquad \det P=7\ne0.
$$
Writing $C=\left(\begin{smallmatrix}0&19\\1&3\end{smallmatrix}\right)$,
direct multiplication gives
$$
AP=PC=\begin{pmatrix}2&25\\7&21\end{pmatrix}.
$$
Thus $P^{-1}AP=C$. The cyclic basis $v,Av$ gives the single
invariant factor $x^2-3x-19$, so this companion matrix is the
rational canonical form over $\mathbb Q$ [@DF04].
:::

<1>2. There are exactly two invariant-factor chains in part (b):
$$
\bigl((x^2+1)(x+1)^2\bigr),\qquad
\bigl(x+1,\ (x^2+1)(x+1)\bigr).
$$

::: {.proof}
Over $\mathbb C$, the characteristic polynomial is
$(x-i)(x+i)(x+1)^2$. Let $f_1\mid\cdots\mid f_r$ be the
nonconstant monic invariant factors. Their product is the
characteristic polynomial [@DF04]. If $x-i$ or $x+i$ divided
some $f_j$ with $j<r$, it would also divide $f_r$, contradicting
its multiplicity one in the product. Hence both of those factors
occur only in $f_r$.

Every earlier $f_j$ is consequently a positive power of $x+1$.
If there is an earlier factor, divisibility forces $x+1$ into
$f_r$ as well. Its total multiplicity is only two, so $r=2$,
$f_1=x+1$, and $f_2=(x^2+1)(x+1)$. If there is no earlier
factor, $r=1$ and $f_1$ is the whole characteristic polynomial.
This proves that the two chains exhaust all possibilities.
:::

<1>3. The two rational canonical forms are
$$
\begin{pmatrix}
0&0&0&-1\\
1&0&0&-2\\
0&1&0&-2\\
0&0&1&-2
\end{pmatrix},\qquad
\begin{pmatrix}
-1&0&0&0\\
0&0&0&-1\\
0&1&0&-1\\
0&0&1&-1
\end{pmatrix}.
$$

::: {.proof}
The products expand to
$$
(x^2+1)(x+1)^2=x^4+2x^3+2x^2+2x+1,
\qquad
(x^2+1)(x+1)=x^3+x^2+x+1.
$$
The first displayed matrix is the companion matrix of the quartic.
The second is $C(x+1)\oplus C(x^3+x^2+x+1)$. Their block
polynomials form the two divisibility chains in step <1>2, so
both are rational canonical forms with the required characteristic
polynomial. Their minimal polynomials are their largest invariant
factors, of degrees four and three respectively [@DF04]. They are
therefore not similar, and step <1>2 proves completeness.
:::
:::
