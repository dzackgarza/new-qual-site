---
schema: qual/card@1
id: P-AGH4310NOTEVERYSECANTMULTISECANT
kind: problem
title: A general $(n-2)$-plane spanned by points of $X$ meets $X$ in no further point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Linear Systems
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.10 and checked the characteristic-zero input against
    Harris's Uniform Position Lemma (Duke Math. J. 46 (1979), 685--724,
    DOI 10.1215/S0012-7094-79-04635-0) and modern curve notes. The proof
    below applies uniform position only to a general hyperplane section, then
    proves openness of the desired (n-1)-tuple condition by a finite incidence
    family over the Grassmannian.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Generalize the statement that "not every secant is a multisecant" as follows.
If $X$ is a curve in $\PP^n$, not contained in any $\PP^{n-1}$, and if $\characteristic k=0$, show that for almost all choices of $n-1$ points $P_1, \ldots, P_{n-1}$ on $X$, the linear space $L^{n-2}$ spanned by the $P_i$ does not contain any further points of $X$.
:::

::: {.solution}
Put
$$
d=\deg X.
$$
The curve is nondegenerate by hypothesis.

<1>1. One has
$$
d\ge n.
$$

::: {.proof}
If $d\le n$, then
[[P-AGH434RATIONALNORMALCURVE|Exercise IV.3.4(b)]]
applied to the nondegenerate curve $X\subseteq\PP^n$ gives
$$
d=n.
$$
Thus in all cases $d\ge n$.
:::

<1>2. Choose a general hyperplane
$$
H\subseteq\PP^n.
$$
Then
$$
\Gamma=X\cap H
$$
is a reduced set of $d$ points in uniform position in
$$
H\cong\PP^{n-1}.
$$

::: {.proof}
In characteristic zero, the Uniform Position Lemma says that a general
hyperplane section of an integral nondegenerate projective curve is reduced
and in uniform position: any two subsets of the same cardinality have the
same Hilbert function.
This is Harris's Uniform Position Lemma
([J. Harris, *Galois groups of enumerative problems*](https://doi.org/10.1215/S0012-7094-79-04635-0));
see also the
[curve-notes exposition, §16.1](https://people.math.harvard.edu/~landesman/assets/curves-notes.pdf).
The characteristic-zero hypothesis in the exercise is exactly the hypothesis
under which this monodromy statement is used.
:::

<1>3. The $d$ points of $\Gamma$ span the whole hyperplane $H$.

::: {.proof}
Suppose instead that
$$
\Gamma\subseteq L
$$
for some hyperplane
$$
L\subsetneq H.
$$
Since $L$ has codimension $2$ in $\PP^n$, choose a hyperplane
$$
H'\ne H
$$
with
$$
H\cap H'=L.
$$
Nondegeneracy of $X$ implies that neither $H$ nor $H'$ contains $X$.

The hyperplane divisor
$$
D_H=H|_X
$$
is the reduced divisor consisting of the $d$ points of $\Gamma$. Since every
point of $\Gamma$ lies in $H'$, one has
$$
D_{H'}\ge D_H.
$$
Both divisors have degree $d$, so
$$
D_{H'}=D_H.
$$

Let $s,s'$ be the two corresponding nonzero sections of $\mco_X(1)$. Their
zero divisors agree, so
$$
\frac{s'}s
$$
is a nowhere-vanishing regular function on the integral projective curve
$X$. It is therefore a scalar
$$
c\in k^\times.
$$
Thus
$$
s'-cs=0
$$
on $X$. But $s'-cs$ is a nonzero linear form because $H'\ne H$, so this
would place $X$ in a hyperplane, a contradiction.
Hence $\Gamma$ spans $H$.
:::

<1>4. Every set of $n$ distinct points of $\Gamma$ spans $H$.

::: {.proof}
By step <1>3, the finite set $\Gamma$ spans the $(n-1)$-dimensional
projective space $H$. Hence some $n$ points of $\Gamma$ form a projective
basis of $H$.

For a finite set
$$
Z\subseteq H,
$$
the value of its Hilbert function in degree $1$ is the rank of the
evaluation map
$$
H^0(H,\mco_H(1))
\longrightarrow
H^0(Z,\mco_Z).
$$
For $n$ points this rank is $n$ exactly when no hyperplane of $H$ contains
all of them, equivalently exactly when they span $H$.

Step <1>2 says that all $n$-point subsets of $\Gamma$ have the same Hilbert
function. Since one such subset spans $H$, every such subset has degree-one
Hilbert function equal to $n$ and therefore spans $H$.
:::

<1>5. Every set of $n-1$ distinct points
$$
P_1,\ldots,P_{n-1}\in\Gamma
$$
is linearly independent and spans an $(n-2)$-plane
$$
L=\langle P_1,\ldots,P_{n-1}\rangle.
$$

::: {.proof}
If the $n-1$ points were linearly dependent, adjoining any further point
$$
Q\in\Gamma\setminus\{P_1,\ldots,P_{n-1}\}
$$
would give $n$ points spanning a projective space of dimension at most
$n-2$. This would contradict step <1>4, since $d\ge n$ by step <1>1.
Therefore the $n-1$ points are linearly independent and their span has
dimension $n-2$.
:::

<1>6. For the points in step <1>5,
$$
L\cap X
=
\{P_1,\ldots,P_{n-1}\}
$$
scheme-theoretically.

::: {.proof}
Because
$$
L\subseteq H,
$$
any point
$$
Q\in L\cap X
$$
also belongs to
$$
H\cap X=\Gamma.
$$
If $Q$ were distinct from the chosen $P_i$, then the $n$ points
$$
P_1,\ldots,P_{n-1},Q
$$
would all lie in the $(n-2)$-plane $L$, contradicting step <1>4.
Thus there is no additional set-theoretic intersection point.

Moreover the hyperplane section $\Gamma=X\cap H$ is reduced by step <1>2.
At each $P_i$, a local equation of $H$ is therefore a uniformizer in the
regular local ring $\mco_{X,P_i}$. Since the ideal of
$$
L\cap X
$$
contains that local equation, its local intersection length at $P_i$ is at
most $1$, and it is nonzero because $P_i\in L$. Hence that length is exactly
$1$.
Therefore the scheme-theoretic intersection consists exactly of the
$n-1$ reduced chosen points.
:::

<1>7. Let
$$
U\subseteq X^{n-1}
$$
be the open set of ordered tuples of distinct linearly independent points.
There is a finite morphism
$$
q:\mathcal Z\longrightarrow U
$$
whose fibre over
$$
\mathbf P=(P_1,\ldots,P_{n-1})
$$
is
$$
X\cap\langle P_1,\ldots,P_{n-1}\rangle.
$$

::: {.proof}
Linear independence is an open rank condition, and pairwise distinctness is
the complement of the diagonals, so $U$ is open. It is nonempty by step
<1>5.

On $U$, taking the linear span defines a morphism
$$
\lambda:
U
\longrightarrow
\operatorname{Gr}(n-2,n),
$$
where the Grassmannian parametrizes $(n-2)$-planes in $\PP^n$.
Pull back the universal $(n-2)$-plane and intersect it with
$$
U\times X.
$$
This gives a closed subscheme
$$
\mathcal Z
\subseteq
U\times X
$$
with the stated fibres.

The projection
$$
q:\mathcal Z\to U
$$
is projective. Every fibre is finite: if an $(n-2)$-plane contained the
integral curve $X$, then $X$ would lie in a hyperplane, contrary to
nondegeneracy. Hence $q$ is projective and quasi-finite, therefore finite.
:::

<1>8. The locus
$$
B
=
\left\{
\mathbf P\in U:
\operatorname{length}
\bigl(
X\cap\langle P_1,\ldots,P_{n-1}\rangle
\bigr)
\ge n
\right\}
$$
is a proper closed subset of $U$.

::: {.proof}
Since $q$ is finite, the coherent sheaf
$$
q_*\mco_{\mathcal Z}
$$
has fibre dimension
$$
\dim_{\kappa(\mathbf P)}
\left(
q_*\mco_{\mathcal Z}\otimes\kappa(\mathbf P)
\right)
=
\operatorname{length}(\mathcal Z_{\mathbf P}).
$$
Upper semicontinuity of fibre dimension for a coherent sheaf makes the
locus where this number is at least $n$ closed.

Step <1>6 gives a tuple for which the fibre consists of exactly
$n-1$ reduced points, hence has length $n-1$. Therefore that tuple is not in
$B$, so $B$ is proper.
:::

<1>9. For every tuple
$$
\mathbf P\in U\setminus B,
$$
the span
$$
\langle P_1,\ldots,P_{n-1}\rangle
$$
contains no further point of $X$.

::: {.proof}
The fibre in step <1>7 always contains the $n-1$ distinct chosen points, so
its length is at least $n-1$.
For
$$
\mathbf P\notin B,
$$
step <1>8 gives length at most $n-1$. Hence the length is exactly $n-1$.
There can therefore be no additional point of $X$ in the span.
:::

<1>10. Q.E.D.

::: {.proof}
The variety $X^{n-1}$ is irreducible. The set $U$ in step <1>7 is nonempty
open, and $U\setminus B$ is nonempty open in $U$ by step <1>8. Hence it is a
dense open subset of $X^{n-1}$.

By step <1>9, every tuple in this dense open set has the required property.
Thus for almost all choices of
$$
P_1,\ldots,P_{n-1}\in X,
$$
their $(n-2)$-plane contains no further point of $X$.
:::
:::
