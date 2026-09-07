---
schema: qual/card@1
id: P-ALGF09G
kind: problem
title: "Equivalent conditions for a finite-dimensional quotient of a polynomial ring"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 7 of the official UCSD Algebra Qualifying Examination, Fall 2009; all three conditions agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified (i) implies coordinate algebraicity by linear dependence, (ii) implies finite spanning by bounded coordinate exponents, and the equivalence with finite zero set using Hilbert's Nullstellensatz.
---

::: {.problem}
Let $I$ be an ideal in the polynomial ring $\mathbb{C}[x_1, \ldots, x_n]$ for some $n \geq 1$.
Prove that the following conditions on $I$ are all equivalent:

(i) $\mathbb{C}[x_1, \ldots, x_n]/I$ is a finite-dimensional $\mathbb{C}$-vector space;

(ii) $I \cap \mathbb{C}[x_i] \neq (0)$ for all $1 \leq i \leq n$;

(iii) The set of common zeroes in affine $n$-space $\mathbb{C}^n$ of all of the polynomials in $I$ is a finite (or empty) set.
:::

::: {.solution}
Write
\[
R:=\mathbb C[x_1,\ldots,x_n]
\]
and let
\[
V(I):=\{a\in\mathbb C^n:f(a)=0\text{ for all }f\in I\}.
\]

<1>1. Condition (i) implies condition (ii).
::: {.proof}
Assume
\[
R/I
\]
is finite-dimensional over $\mathbb C$.
Fix $i$ and let $\bar x_i$ be the image of $x_i$ in $R/I$.
The infinite sequence
\[
1,\bar x_i,\bar x_i^2,\ldots
\]
lies in a finite-dimensional vector space, so it is linearly dependent.
Hence there is a nonzero polynomial
\[
f_i(T)=c_0+c_1T+\cdots+c_dT^d\in\mathbb C[T]
\]
such that
\[
f_i(\bar x_i)=0
\]
in $R/I$.
Equivalently,
\[
f_i(x_i)\in I.
\]
Since $f_i(x_i)\neq0$ in the polynomial ring $\mathbb C[x_i]$,
\[
I\cap\mathbb C[x_i]\neq(0).
\]
This holds for every $i$.
:::

<1>2. Condition (ii) implies condition (i).
::: {.proof}
Assume that for each $i$ there is a nonzero polynomial
\[
f_i(x_i)\in I\cap\mathbb C[x_i].
\]
Multiplying by a nonzero scalar, take each $f_i$ monic, and write
\[
d_i:=\deg f_i\ge0.
\]
If some $d_i=0$, then $f_i$ is a nonzero constant, so $1\in I$ and $R/I=0$, which is finite-dimensional.
Thus suppose all $d_i\ge1$.

Modulo $I$, the relation $f_i(x_i)=0$ expresses
\[
x_i^{d_i}
\]
as a $\mathbb C$-linear combination of lower powers of $x_i$.
Repeated reduction therefore expresses every monomial in $R/I$ as a linear combination of monomials
\[
x_1^{e_1}\cdots x_n^{e_n}
\qquad
(0\le e_i<d_i).
\]
There are only
\[
d_1\cdots d_n
\]
such monomials.
Hence $R/I$ is spanned by finitely many vectors over $\mathbb C$, so it is finite-dimensional.
:::

<1>3. Condition (ii) implies condition (iii).
::: {.proof}
For each $i$, choose
\[
0\neq f_i(x_i)\in I\cap\mathbb C[x_i].
\]
If
\[
a=(a_1,\ldots,a_n)\in V(I),
\]
then
\[
f_i(a_i)=0
\]
for every $i$.
Thus $a_i$ must lie in the finite set of roots of $f_i$.
Consequently
\[
V(I)
\]
is contained in the finite Cartesian product of those root sets.
Therefore $V(I)$ is finite, possibly empty.
:::

<1>4. Condition (iii) implies condition (ii).
::: {.proof}
Assume first that
\[
V(I)=\{a^{(1)},\ldots,a^{(r)}\}
\]
is nonempty and finite, where
\[
a^{(j)}=(a_1^{(j)},\ldots,a_n^{(j)}).
\]
For each $i$, define the nonzero one-variable polynomial
\[
g_i(T):=\prod_{j=1}^r(T-a_i^{(j)})\in\mathbb C[T].
\]
Then
\[
g_i(x_i)
\]
vanishes at every point of $V(I)$.
By Hilbert's Nullstellensatz,
\[
I(V(I))=\sqrt I.
\]
Hence
\[
g_i(x_i)\in\sqrt I.
\]
Therefore some positive power satisfies
\[
g_i(x_i)^{N_i}\in I.
\]
This is a nonzero element of $\mathbb C[x_i]$, so
\[
I\cap\mathbb C[x_i]\neq(0).
\]

If $V(I)=\varnothing$, the Nullstellensatz gives
\[
\sqrt I=R.
\]
Hence $1\in\sqrt I$, so $1\in I$ and $I=R$.
Then
\[
1\in I\cap\mathbb C[x_i]
\]
for every $i$.
Thus (ii) holds in the empty case as well.
:::

<1>5. Therefore (i), (ii), and (iii) are equivalent.
::: {.proof}
By <1>1 and <1>2,
\[
\text{(i)}\Longleftrightarrow\text{(ii)}.
\]
By <1>3 and <1>4,
\[
\text{(ii)}\Longleftrightarrow\text{(iii)}.
\]
Hence all three conditions are equivalent.
:::
:::
