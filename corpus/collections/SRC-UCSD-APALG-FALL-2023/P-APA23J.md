---
schema: qual/card@1
id: P-APA23J
kind: problem
title: 'Monomial ideal $\langle x_2^2,\dots,x_n^2\rangle$: basis, Hilbert function, and variety'
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
---

::: problem
Consider the monomial ideal $I = \langle x_2^2, \dots, x_n^2 \rangle$ in $\mathbb{C}[x_1, \dots, x_n]$.

(a) Give a basis of the vector space $\mathbb{C}[x_1, \dots, x_n]/I$.

(b) Compute the Hilbert function of the ideal $I$.

(c) Determine the affine variety $V(I)$, and explain whether or not it is reducible.
:::

::: {.solution}
Let
\[
R=\mathbb C[x_1,\ldots,x_n],
\qquad
I=(x_2^2,\ldots,x_n^2).
\]

<1>1. A $\mathbb C$-basis of $R/I$ is
\[
\boxed{\left\{
 x_1^a x_2^{\varepsilon_2}\cdots x_n^{\varepsilon_n}
 :a\ge0,\ \varepsilon_i\in\{0,1\}
\right\}.}
\]
::: {.proof}
Because $I$ is a monomial ideal, the residue classes of monomials not contained in $I$ form a basis of the quotient.
A monomial lies in $I$ exactly when it is divisible by $x_i^2$ for some $i\ge2$. Therefore the monomials outside $I$ are precisely those in which every exponent of $x_2,\ldots,x_n$ is at most $1$, while the exponent of $x_1$ is arbitrary. This gives the displayed basis.
:::

<1>2. The Hilbert series of the quotient is
\[
\operatorname{Hilb}_{R/I}(t)
=\frac{(1+t)^{n-1}}{1-t}.
\]
::: {.proof}
For the basis in <1>1, the powers of $x_1$ contribute
\[
1+t+t^2+\cdots=\frac1{1-t},
\]
while each variable $x_i$ for $i\ge2$ may occur with exponent $0$ or $1$, contributing a factor $1+t$. Multiplying these independent contributions gives the formula.
:::

<1>3. Hence the degree-$d$ Hilbert function of the quotient is
\[
\boxed{
H_{R/I}(d)
=\sum_{j=0}^{\min(d,n-1)}\binom{n-1}{j}.}
\]
::: {.proof}
A basis monomial of total degree $d$ is determined by choosing a subset of $\{x_2,\ldots,x_n\}$ of size $j\le d$ to occur to exponent $1$, after which the exponent of $x_1$ is forced to be $d-j$. There are $\binom{n-1}{j}$ such choices. Summing over all possible $j$ gives the formula.
:::

<1>4. If “the Hilbert function of the ideal $I$” is interpreted literally as
\[
H_I(d)=\dim_{\mathbb C} I_d,
\]
then
\[
\boxed{
H_I(d)
=\binom{n+d-1}{n-1}
-\sum_{j=0}^{\min(d,n-1)}\binom{n-1}{j}.}
\]
::: {.proof}
The degree-$d$ component of
\[
0\longrightarrow I\longrightarrow R\longrightarrow R/I\longrightarrow0
\]
is exact, so
\[
\dim I_d=\dim R_d-\dim(R/I)_d.
\]
The number of degree-$d$ monomials in $n$ variables is
\[
\dim R_d=\binom{n+d-1}{n-1}.
\]
Subtract the quotient Hilbert function from <1>3.
This also records the answer if the source intended the more common convention of asking for the Hilbert function of the quotient.
:::

<1>5. The affine variety is
\[
\boxed{V(I)=\{(a,0,\ldots,0):a\in\mathbb C\}.}
\]
::: {.proof}
A point $(a_1,\ldots,a_n)$ belongs to $V(I)$ exactly when
\[
a_i^2=0\qquad(2\le i\le n).
\]
Over the field $\mathbb C$, this is equivalent to $a_i=0$ for every $i\ge2$, while $a_1$ is unrestricted.
:::

<1>6. The variety $V(I)$ is irreducible.
::: {.proof}
The map
\[
\mathbb A^1_{\mathbb C}\longrightarrow V(I),
\qquad
a\longmapsto(a,0,\ldots,0)
\]
is an isomorphism of affine varieties. Equivalently,
\[
\sqrt I=(x_2,\ldots,x_n),
\]
and
\[
R/\sqrt I\cong\mathbb C[x_1]
\]
is an integral domain. Hence $V(I)$ is irreducible.
:::
:::
