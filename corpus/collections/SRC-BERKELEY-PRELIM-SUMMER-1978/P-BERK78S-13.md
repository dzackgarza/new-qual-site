---
schema: qual/card@1
id: P-BERK78S-13
kind: problem
title: A row over $F[x]$ is the first row of a determinant-one matrix exactly when its gcd is $1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The source does not restrict n. With the standard monic-gcd convention
    the statement fails for n=1: over Q[x], p_1=2 has gcd 1 but the only
    1-by-1 matrix with first row (2) has determinant 2. The card adds the
    intended hypothesis n>=2.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For the forward direction, reduced the unimodular row to
    (1,0,...,0) by determinant-one column transformations built from Bezout
    identities for successive pairs; the inverse transformation completes
    the original row to an SL_n matrix. Conversely, expanding a
    determinant-one completion along its first row gives a Bezout identity
    for the p_i.
---

::: {.problem}
Let $R=F[x]$ be the polynomial ring over a field $F$, let $n\geq2$, and
let $p_1,\dots,p_n\in R$. Prove that
\[
\gcd(p_1,\dots,p_n)=1
\]
if and only if there is an $n\times n$ matrix over $R$ with determinant $1$ whose first row is
\[
(p_1,\dots,p_n).
\]
:::

::: {.solution}
All greatest common divisors below are chosen monic.

::: pf

::: {.pf-step #s1}

Let $a,b\in R$ be not both zero, and let
$$
d=\gcd(a,b).
$$
There is a matrix
$$
Q(a,b)\in\operatorname{SL}_2(R)
$$
such that
$$
(a,b)Q(a,b)=(d,0).
$$

::: pf-proof

Since $R=F[x]$ is a Euclidean domain, Bezout's identity gives
$u,v\in R$ such that
$$
ua+vb=d.
$$
Write
$$
a=da',
\qquad
b=db'.
$$
Set
$$
Q(a,b)
=
\begin{pmatrix}
u&-b'\\
v&a'
\end{pmatrix}.
$$
Then
$$
(a,b)Q(a,b)
=
(ua+vb,-ab'+ba')
=
(d,0).
$$
Moreover,
$$
\det Q(a,b)
=
ua'+vb'
=
\frac{ua+vb}{d}
=
1.
$$
Thus $Q(a,b)\in\operatorname{SL}_2(R)$.

:::

:::

::: {.pf-step #s2}

For distinct indices $r,s$, the matrix which acts on coordinates
$r,s$ by
$$
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
$$
and fixes all other coordinates lies in $\operatorname{SL}_n(R)$.

::: pf-proof

The displayed $2\times2$ block has determinant $1$. The full matrix is
block diagonal after a simultaneous reordering of rows and columns, with
this block and identity blocks, so its determinant is $1$.

:::

:::

::: {.pf-step #s3}

Suppose
$$
\gcd(p_1,\ldots,p_n)=1.
$$
There is a matrix
$$
U\in\operatorname{SL}_n(R)
$$
such that
$$
(p_1,\ldots,p_n)U=(1,0,\ldots,0).
$$

::: pf-proof

Because the gcd is $1$, the row is not the zero row. If $p_1=0$, choose
$k\geq2$ with $p_k\neq0$ and apply the determinant-one coordinate
transformation from step [](#s2){.pf-ref} to coordinates $1$ and $k$. After this
operation the first coordinate is nonzero.

Now process coordinates
$$
j=2,3,\ldots,n
$$
in order. At a given stage let the current first and $j$th entries be
$$
a,\ b.
$$
The first entry is nonzero, so the pair is not $(0,0)$. Embed the matrix
$Q(a,b)$ from step [](#s1){.pf-ref} into coordinates $1$ and $j$, fixing all other
coordinates. Right multiplication by this embedded matrix replaces the
pair $(a,b)$ by
$$
(\gcd(a,b),0)
$$
and has determinant $1$.

After processing the first $j$ coordinates, the first entry is the monic
gcd of the original entries
$$
p_1,\ldots,p_j,
$$
and coordinates $2,\ldots,j$ are zero. Thus after the final stage the row
is
$$
(\gcd(p_1,\ldots,p_n),0,\ldots,0)
=(1,0,\ldots,0).
$$
The product $U$ of all the determinant-one transformations lies in
$\operatorname{SL}_n(R)$.

:::

:::

::: {.pf-step #s4}

Under the hypothesis
$$
\gcd(p_1,\ldots,p_n)=1,
$$
there is an $n\times n$ matrix over $R$ with determinant $1$ and first row
$(p_1,\ldots,p_n)$.

::: pf-proof

Let $U$ be the matrix from step [](#s3){.pf-ref} and set
$$
A=U^{-1}.
$$
Since $\det U=1$,
$$
\det A=1.
$$
Step [](#s3){.pf-ref} gives
$$
(p_1,\ldots,p_n)U=e_1^T.
$$
Right multiplication by $U^{-1}$ yields
$$
(p_1,\ldots,p_n)
=
e_1^TU^{-1}
=
e_1^TA.
$$
But $e_1^TA$ is the first row of $A$. Hence $A$ is the required
completion.

:::

:::

::: {.pf-step #s5}

Conversely, suppose there is a matrix
$$
A\in M_n(R)
$$
with determinant $1$ and first row
$$
(p_1,\ldots,p_n).
$$
Then there exist $c_1,\ldots,c_n\in R$ such that
$$
\sum_{j=1}^n p_jc_j=1.
$$

::: pf-proof

Expand $\det A$ along the first row:
$$
\det A
=
\sum_{j=1}^n p_jC_{1j},
$$
where $C_{1j}\in R$ is the $(1,j)$ cofactor of $A$. Since
$$
\det A=1,
$$
take
$$
c_j=C_{1j}.
$$

:::

:::

::: {.pf-step #s6}

Under the hypothesis of step [](#s5){.pf-ref},
$$
\gcd(p_1,\ldots,p_n)=1.
$$

::: pf-proof

Let
$$
d=\gcd(p_1,\ldots,p_n).
$$
Then $d$ divides every $p_j$, so it divides every $R$-linear combination
of the $p_j$. By step [](#s5){.pf-ref} it therefore divides $1$. Thus $d$ is a unit in
$F[x]$. Since the gcd is chosen monic, the only monic unit is $1$, and
hence
$$
d=1.
$$

:::

:::

::: {.pf-step #s7}

The equivalence holds:
$$
\boxed{
\gcd(p_1,\ldots,p_n)=1
\iff
\text{the row }(p_1,\ldots,p_n)
\text{ extends to a matrix in }\operatorname{SL}_n(R).
}
$$

::: pf-proof

Step [](#s4){.pf-ref} proves the forward implication, and step [](#s6){.pf-ref} proves the reverse
implication.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required equivalence.

:::

:::

:::

::: {.remark}
Erratum: the source does not state $n\geq2$. With the standard convention
that polynomial gcds are monic, the assertion is false for $n=1$. For
example, in $\QQ[x]$ the polynomial $p_1=2$ has monic gcd $1$, but the
only $1\times1$ matrix with first row $(2)$ is $(2)$, whose determinant is
$2$, not $1$.
:::
