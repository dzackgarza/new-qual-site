---
schema: qual/card@1
id: P-R6CFM
kind: problem
title: Rational canonical forms of $6\times 6$ matrices over $\mathbb{Q}$ with minimal
  polynomial $(x+2)^2(x-1)$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared the dimension, minimal polynomial, and requested canonical form with page 5 of the original scan, Rings and modules 1."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: "Checked all degree partitions for the invariant-factor chain and the coefficients of every companion block."
---

::: {.problem}
There are finitely many $6 \times 6$ matrices over $\mathbb{Q}$, in rational canonical form, with minimal polynomial $(x + 2)^2(x - 1)$.
Find them.
:::

::: {.solution}
Put $p=x+2$, $q=x-1$, and $f=p^2q=x^3+3x^2-4$.
For a monic polynomial $h$, write $C(h)$ for the matrix of multiplication
by $x$ on $\mathbf Q[x]/(h)$ in the ordered basis
$1,x,\ldots,x^{\deg h-1}$. The answer consists of the following six
block diagonal matrices:
$$
\begin{gathered}
\operatorname{diag}(C(f),C(f)),\\
\operatorname{diag}(C(p),C(p^2),C(f)),\\
\operatorname{diag}(C(p),C(pq),C(f)),\\
\operatorname{diag}(C(q),C(pq),C(f)),\\
\operatorname{diag}(C(p),C(p),C(p),C(f)),\\
\operatorname{diag}(C(q),C(q),C(q),C(f)).
\end{gathered}
$$
The blocks are explicitly
$$
\begin{gathered}
C(p)=(-2),\qquad C(q)=(1),\\
C(p^2)=\begin{pmatrix}0&-4\\1&-4\end{pmatrix},\qquad
C(pq)=\begin{pmatrix}0&2\\1&-1\end{pmatrix},\qquad
C(f)=\begin{pmatrix}0&0&4\\1&0&0\\0&1&-3\end{pmatrix}.
\end{gathered}
$$

<1>1. The invariant factors form a chain of nonconstant monic polynomials
$$
d_1\mid d_2\mid\cdots\mid d_s=f,
\qquad \sum_{i=1}^s\deg d_i=6.
$$

::: {.proof}
Apply the rational canonical form theorem to $\mathbf Q^6$ as a
$\mathbf Q[x]$-module, with $x$ acting by the given matrix [@DF04].
Its invariant factors determine the companion blocks, their degrees
sum to the dimension, and their largest member is the minimal
polynomial. Since $\deg f=3$, all the earlier invariant factors have
total degree $3$ and divide $f$.
:::

<1>2. There are exactly six such chains.

::: {.proof}
The positive degrees before the final factor $f$ are nondecreasing and
sum to $3$. Their only possibilities are $(3)$, $(1,2)$, and $(1,1,1)$.

For $(3)$, a monic degree-$3$ divisor of $f$ is $f$ itself. This gives
$(f,f)$.

For $(1,2)$, the degree-$2$ factor is either $p^2$ or $pq$.
If it is $p^2$, the preceding linear factor must be $p$.
If it is $pq$, that factor can be either $p$ or $q$.
Thus the three chains are $(p,p^2,f)$, $(p,pq,f)$, and $(q,pq,f)$.

For $(1,1,1)$, divisibility forces the three monic linear factors to
coincide. They are all $p$ or all $q$, giving $(p,p,p,f)$ and
$(q,q,q,f)$. This exhausts the possible chains.
:::

<1>3. Every displayed matrix has the required minimal polynomial, and
no two are similar.

::: {.proof}
The minimal polynomial of $C(h)$ is $h$: a polynomial $g$ annihilates
multiplication by $x$ on $\mathbf Q[x]/(h)$ exactly when $h\mid g$,
as can be checked by applying it to $1$. A polynomial annihilates a
block diagonal matrix exactly when it annihilates every block, so its
minimal polynomial is the least common multiple of the block minimal
polynomials. For each displayed divisibility chain this is $f$, and
the block sizes sum to $6$. The chains are distinct, so uniqueness of
the invariant factors makes the six matrices pairwise nonsimilar
[@DF04]. Step <1>2 proves that no further rational canonical form is
possible.
:::
:::
