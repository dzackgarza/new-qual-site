---
schema: qual/card@1
id: P-AGH427ETALEDEGREETWO
kind: problem
title: Étale double covers of $Y$ correspond to $2$-torsion elements of $\Pic Y$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Jacobians
  - Curves
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.7 under the book's standing convention that curves
    are over an algebraically closed field. The proof uses the trace splitting
    of a quadratic étale algebra, checks the converse locally as
    O[t]/(t^2-u), and verifies independence of the chosen trivialization of
    L^2 by rescaling with a square root of a global scalar.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Let $Y$ be a curve over a field $k$ of characteristic $\neq 2$.
We show there is a one-to-one correspondence between finite étale morphisms $f: X \to Y$ of degree 2, and 2-torsion elements of $\Pic Y$, i.e., invertible sheaves $\mcl$ on $Y$ with $\mcl^2 \cong \OO_Y$.

a. Given an étale morphism $f: X \to Y$ of degree 2, there is a natural map $\OO_Y \to f_* \OO_X$.
Let $\mcl$ be the cokernel.
Then $\mcl$ is an invertible sheaf on $Y$, $\mcl \cong \det f_* \OO_X$, and so $\mcl^2 \cong \OO_Y$ by (Ex.
2.6). Thus an étale cover of degree 2 determines a 2-torsion element in $\Pic Y$.

b. Conversely, given a 2-torsion element $\mcl$ in $\Pic Y$, define an $\OO_Y\dash$algebra structure on $\OO_Y \oplus \mcl$ by $\langle a, b\rangle \cdot\left\langle a', b'\right\rangle=\left\langle a a'+\varphi(b \tensor b'), a b'+a' b\right\rangle$, where $\varphi$ is an isomorphism of $\mcl \tensor \mcl \to \OO_Y$.
Then take $X=\Spec(\OO_Y \oplus \mcl)$ (II, Ex.
5.17). Show that $X$ is an étale cover of $Y$.

c. Show that these two processes are inverse to each other.
Hint: Let $\tau: X \to X$ be the involution which interchanges the points of each fibre of $f$.
Use the trace map $a \mapsto a+\tau(a)$ from $f_* \OO_X \to \OO_Y$ to show that the sequence of $\OO_Y\dash$modules in a. is split exact:
$$
0 \to \OO_Y \to f_* \OO_X \to \mcl \to 0
$$

Note.
This is a special case of the more general fact that for $(n, \characteristic k)=1$, the étale Galois covers of $Y$ with group $\ZZ/n\ZZ$ are classified by the étale cohomology group $H_{\text{et}}^1(Y, \ZZ/n\ZZ)$, which is equal to the group of $n$-torsion points of $\Pic Y$.
See Serre.
:::

::: {.solution}
The correspondence below is between isomorphism classes of degree-$2$
finite étale covers over $Y$ and $2$-torsion classes in $\Pic Y$.

::: pf

::: {.pf-step #s1}

Let
$$
f:X\longrightarrow Y
$$
be finite étale of degree $2$, and put
$$
A=f_*\OO_X.
$$
Then the unit inclusion
$$
\OO_Y\longrightarrow A
$$
is split as a map of $\OO_Y$-modules, and its cokernel $\mcl$ is invertible.

::: pf-proof

The finite étale algebra $A$ is locally free of rank $2$.  Its trace map
$$
\Tr_{A/\OO_Y}:A\longrightarrow\OO_Y
$$
satisfies
$$
\Tr(1)=2.
$$
Because $\operatorname{char}k\ne2$, multiplication by $1/2$ gives a
retraction
$$
\frac12\Tr:A\longrightarrow\OO_Y
$$
of the unit inclusion.  Hence
$$
A\cong\OO_Y\oplus M,
\qquad
M=\ker\Tr.
$$
Since $A$ has rank $2$, $M$ is locally free of rank $1$.  The quotient
$$
\mcl=A/\OO_Y
$$
is naturally isomorphic to $M$, and is therefore invertible.

:::

:::

::: {.pf-step #s2}

The invertible sheaf from step [](#s1){.pf-ref} satisfies
$$
\mcl\cong\det f_*\OO_X
\qquad\text{and}\qquad
\mcl^{\tensor2}\cong\OO_Y.
$$

::: pf-proof

The split exact sequence
$$
0
\longrightarrow
\OO_Y
\longrightarrow
A
\longrightarrow
\mcl
\longrightarrow0
$$
gives
$$
\det A
\cong
\det\OO_Y\tensor\det\mcl
\cong
\mcl.
$$

Because $f$ is étale, its ramification divisor and hence its branch divisor
are zero.  Applying [[P-AGH426PUSHFORWARDDIVISORS|Exercise IV.2.6]], part
(d), gives
$$
(\det A)^2\cong\OO_Y.
$$
Thus
$$
\mcl^{\tensor2}\cong\OO_Y.
$$
This proves part (a).

:::

:::

::: {.pf-step #s3}

Conversely, let $\mcl$ be invertible and choose an isomorphism
$$
\varphi:\mcl\tensor\mcl\xrightarrow{\sim}\OO_Y.
$$
The multiplication in the statement makes
$$
A_\varphi=\OO_Y\oplus\mcl
$$
into a commutative finite locally free $\OO_Y$-algebra of rank $2$.

::: pf-proof

The unit is $(1,0)$.  Commutativity is immediate from symmetry of the tensor
product of line bundles.  Associativity can be checked after locally
trivializing $\mcl$.  On an open set where $\mcl=\OO_Ye$, write
$$
\varphi(e\tensor e)=u\in\OO_Y^\times.
$$
Then the map sending a formal variable $t$ to $(0,e)$ identifies the algebra
with
$$
A_\varphi
\cong
\OO_Y[t]/(t^2-u).
$$
This is manifestly an associative commutative algebra, free with basis
$1,t$.  The local descriptions glue because they came from the globally
defined multiplication in the statement.

:::

:::

::: {.pf-step #s4}

The morphism
$$
f_\varphi:X_\varphi=\Spec_Y(A_\varphi)\longrightarrow Y
$$
is finite étale of degree $2$.

::: pf-proof

Finiteness and degree $2$ follow from the fact that $A_\varphi$ is locally
free of rank $2$.  In the local description of step [](#s3){.pf-ref},
$$
A_\varphi=R[t]/(t^2-u),
\qquad
u\in R^\times.
$$
The element $t$ is a unit because $t^2=u$, and $2$ is a unit because the
characteristic is not $2$.  Therefore
$$
2t\in A_\varphi^\times.
$$
The relative differentials are
$$
\Omega_{A_\varphi/R}
\cong
A_\varphi\,dt/(2t\,dt)
=0.
$$
Thus the finite flat morphism $f_\varphi$ is unramified, hence étale.  This
proves part (b).

:::

:::

::: {.pf-step #s5}

For a quadratic étale cover $f:X\to Y$, the trace-zero summand
$$
M=\ker\Tr\subseteq A=f_*\OO_X
$$
is the $(-1)$-eigensheaf for the nontrivial deck involution $\tau$, and
multiplication induces an isomorphism
$$
M\tensor M\xrightarrow{\sim}\OO_Y.
$$

::: pf-proof

The deck involution interchanges the two points of each geometric fibre.  On
the rank-$2$ algebra it satisfies
$$
\Tr(a)=a+\tau(a).
$$
Hence an element of $M$ obeys
$$
\tau(a)=-a,
$$
while $\OO_Y\cdot1$ is the $(+1)$-eigensheaf.  If $a,b\in M$, then
$$
\tau(ab)=\tau(a)\tau(b)=ab,
$$
so multiplication lands in the invariant summand $\OO_Y$ and gives a map
$$
M^{\tensor2}\longrightarrow\OO_Y.
$$

This map is an isomorphism fibrewise.  Indeed, over a geometric point the
étale quadratic algebra is
$$
k\times k,
$$
the involution swaps the two factors, and the trace-zero line consists of
$(a,-a)$.  Multiplication sends
$$
(a,-a)(b,-b)=(ab,ab),
$$
which is a nonzero perfect pairing on that one-dimensional line.  A map
between line bundles that is an isomorphism on every fibre is an isomorphism.

:::

:::

::: {.pf-step #s6}

Starting with a degree-$2$ finite étale cover, applying part (a) and
then the construction of part (b) recovers the original cover up to
isomorphism over $Y$ once the multiplication pairing is used as the chosen
trivialization.

::: pf-proof

By step [](#s1){.pf-ref} and step [](#s5){.pf-ref},
$$
A=f_*\OO_X
\cong
\OO_Y\oplus M
$$
as an $\OO_Y$-module, and the algebra multiplication is completely described
by
$$
M\tensor M\xrightarrow{\sim}\OO_Y:
$$
products involving the first summand are scalar multiplication, while the
product of two trace-zero elements is exactly this pairing.  Therefore the
algebra reconstructed in part (b) is isomorphic to $A$ as an
$\OO_Y$-algebra.  Relative Spec then recovers $X$ and its morphism to $Y$.

:::

:::

::: {.pf-step #s7}

Starting with a $2$-torsion line bundle $\mcl$, the cover constructed
in part (b) returns the same class $[\mcl]\in\Pic Y$ under part (a).

::: pf-proof

For
$$
A_\varphi=\OO_Y\oplus\mcl,
$$
the unit map is inclusion of the first summand.  Its cokernel is therefore
exactly $\mcl$.  Thus part (a) recovers the original line-bundle class.

:::

:::

::: {.pf-step #s8}

The isomorphism class of the cover constructed from $\mcl$ is
independent of the chosen trivialization
$$
\varphi:\mcl^{\tensor2}\xrightarrow{\sim}\OO_Y.
$$

::: pf-proof

Because $Y$ is a projective integral curve over the algebraically closed
field $k$,
$$
H^0(Y,\OO_Y)^\times=k^\times.
$$
Thus any two trivializations satisfy
$$
\varphi'=c\varphi
$$
for some $c\in k^\times$.  Choose $\lambda\in k^\times$ with
$$
\lambda^2c=1,
$$
which is possible because $k$ is algebraically closed.  Then
$$
\OO_Y\oplus\mcl
\longrightarrow
\OO_Y\oplus\mcl,
\qquad
(a,b)\longmapsto(a,\lambda b)
$$
is an isomorphism from the algebra defined by $\varphi$ to the algebra
defined by $\varphi'$.  Hence the associated covers are isomorphic over
$Y$.

The same argument shows that replacing $\mcl$ by an isomorphic line bundle
does not change the cover.  Therefore the construction depends only on the
class of $\mcl$ in $\Pic Y$.

:::

:::

::: {.pf-step #s9}

The two constructions give mutually inverse bijections
$$
\left\{
\begin{array}{c}
\text{degree-$2$ finite étale covers of $Y$}\\
\text{up to isomorphism over $Y$}
\end{array}
\right\}
\longleftrightarrow
\Pic(Y)[2].
$$

::: pf-proof

Step [](#s6){.pf-ref} proves that cover $\to$ line bundle $\to$ cover is the identity on
isomorphism classes.  Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove that line bundle $\to$ cover
$\to$ line bundle is the identity on $2$-torsion classes and that the cover
does not depend on auxiliary choices.  Thus the two maps are inverse.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (b), and steps
[](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref} and [](#s9){.pf-ref} prove part (c).

:::

:::

:::
