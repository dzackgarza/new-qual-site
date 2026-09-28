---
schema: qual/card@1
id: P-AGH2319CHEVALLEY
kind: problem
title: Images of constructible sets under a finite type morphism are constructible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Constructible Sets
  - Finite Type
  - Noetherian Induction
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.19 statement and the standard Chevalley constructibility theorem.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a morphism of finite type of noetherian schemes.
Then the image of any constructible subset of $X$ is a constructible subset of $Y$.
In particular $f(X)$, which need not be either open or closed, is a constructible subset of $Y$.

Prove this theorem in the following steps.

a. Reduce to showing that $f(X)$ itself is constructible, in the case where $X$ and $Y$ are affine, integral, noetherian schemes and $f$ is a dominant morphism.

b. In that case, show that $f(X)$ contains a nonempty open subset of $Y$ using the following result from commutative algebra.
Let $A \subseteq B$ be an inclusion of noetherian integral domains such that $B$ is a finitely generated $A$-algebra.
Then given a nonzero element $b \in B$, there is a nonzero element $a \in A$ with the following property: if $\phi: A \to K$ is any homomorphism of $A$ into an algebraically closed field $K$ with $\phi(a) \neq 0$, then $\phi$ extends to a homomorphism $\phi'$ of $B$ into $K$ with $\phi'(b) \neq 0$.

c. Now use noetherian induction on $Y$ to complete the proof.

d. Give some examples of morphisms $f: X \to Y$ of varieties over an algebraically closed field $k$ showing that $f(X)$ need not be either open or closed.
:::

::: {.remark}
Prove the algebraic result of (b) by induction on the number of generators of $B$ over $A$; for one generator prove it directly.
In the application, take $b = 1$.
This statement is Chevalley's theorem; see Cartan and Chevalley, exposé 7, and Matsumura.
:::

::: {.solution}
<1>1. It is enough to prove that the image of the whole source is constructible for finite type morphisms of noetherian schemes.
::: {.proof}
Let $E\subseteq X$ be constructible.  By Hartshorne II.3.18(a), write
\[
E=E_1\amalg\cdots\amalg E_r
\]
with each $E_i$ locally closed.

Give each $E_i$ its reduced induced locally closed subscheme structure.  Its inclusion
\[
E_i\hookrightarrow X
\]
is a composition of a closed immersion and an open immersion.  Since $X$ is noetherian, every open subset is quasi-compact, so Hartshorne II.3.13(a),(b),(c) shows that this inclusion is of finite type.  Hence
\[
E_i\longrightarrow Y
\]
is of finite type.

If images of whole sources under finite type morphisms are constructible, every
\[
f(E_i)
\]
is constructible, and then
\[
f(E)=\bigcup_{i=1}^r f(E_i)
\]
is constructible as a finite union.
:::

<1>2. To prove constructibility of $f(X)$, it is enough to treat the case in which $X$ and $Y$ are affine.
::: {.proof}
The noetherian scheme $Y$ is quasi-compact, so choose a finite affine cover
\[
Y=V_1\cup\cdots\cup V_m.
\]
Then
\[
f(X)\cap V_j
=
f\bigl(f^{-1}(V_j)\bigr).
\]
Since $f$ is finite type, each $f^{-1}(V_j)$ is quasi-compact and has a finite affine cover
\[
U_{j1},\ldots,U_{jr_j}.
\]
Therefore
\[
f(X)\cap V_j
=
\bigcup_\ell f(U_{j\ell}).
\]
If the affine-source/affine-target case is known, each $f(U_{j\ell})$ is constructible in $V_j$, hence locally a finite union of locally closed subsets of $Y$.  Thus $f(X)\cap V_j$ is constructible in $Y$.  Taking the finite union over $j$ proves constructibility of $f(X)$.
:::

<1>3. In the affine case it is enough to treat $X$ and $Y$ integral and $f$ dominant.
::: {.proof}
Write
\[
X=\Spec B,
\qquad
Y=\Spec A.
\]
Because $X$ is noetherian, it has finitely many irreducible components
\[
X_1,\ldots,X_n.
\]
Give each $X_i$ its reduced induced structure.  By Hartshorne II.3.11, each $X_i$ is a closed affine integral subscheme of $X$, and
\[
f(X)=\bigcup_i f(X_i).
\]

For each $i$, let
\[
Y_i=\overline{f(X_i)}
\]
with its reduced induced structure.  Then $Y_i$ is an integral closed affine subscheme of $Y$, and the morphism
\[
X_i\longrightarrow Y_i
\]
is dominant.  It is finite type: its composite with the closed immersion $Y_i\hookrightarrow Y$ is finite type, while $X_i\to Y_i$ is quasi-compact because $X_i$ is affine, so Hartshorne II.3.13(f) applies.

If the theorem is known for these affine integral dominant morphisms, each $f(X_i)$ is constructible in $Y_i$, hence constructible in $Y$ because $Y_i$ is closed.  Their finite union is $f(X)$.
:::

<1>4. This proves the reduction required in part (a).
::: {.proof}
Step <1>1 reduces from an arbitrary constructible subset to the image of the whole source, <1>2 reduces to affine source and target, and <1>3 reduces to the affine integral dominant case.
:::

<1>5. We prove the commutative-algebra lemma in part (b) first when
\[
B=A[x]
\]
is generated by one element over $A$.
::: {.proof}
Let $0\ne b\in B$.  There are two cases.

**Case 1: $x$ is transcendental over $K(A)$.**
Then
\[
B\cong A[T]
\]
and $b$ corresponds to a nonzero polynomial
\[
q(T)=q_0+q_1T+\cdots+q_mT^m\in A[T].
\]
Choose one nonzero coefficient
\[
a=q_j\in A.
\]
Let
\[
\phi:A\to K
\]
map into an algebraically closed field with $\phi(a)\ne0$.  Then the polynomial
\[
\phi(q)(T)\in K[T]
\]
is nonzero.  Since an algebraically closed field is infinite, choose $\lambda\in K$ with
\[
\phi(q)(\lambda)\ne0.
\]
Sending $x\mapsto\lambda$ extends $\phi$ to
\[
\phi':B\to K
\]
and gives $\phi'(b)\ne0$.

**Case 2: $x$ is algebraic over $K(A)$.**
Let
\[
F(T)\in K(A)[T]
\]
be the monic minimal polynomial of $x$.  Write
\[
b=q(x)
\]
for $q(T)\in A[T]$.  Since $b\ne0$, $F$ does not divide $q$ in $K(A)[T]$, so
\[
\gcd(F,q)=1.
\]
Hence there are polynomials $P,Q\in K(A)[T]$ with
\[
PF+Qq=1.
\]

Clear all denominators occurring in $F,P,Q$.  There exists $0\ne a\in A$ such that

- $F\in A_a[T]$ is still monic, and
- after multiplying the Bézout identity by a unit of $A_a$, it has the form
  \[
  P_0F+Q_0q=c
  \]
  with $P_0,Q_0\in A_a[T]$ and $c\in A$ nonzero and invertible in $A_a$.

Replace $a$ by $ac$.  If $\phi:A\to K$ satisfies $\phi(a)\ne0$, it extends to $A_a$.  The monic polynomial $\phi(F)$ has a root $\lambda\in K$.  Evaluating the Bézout identity at $\lambda$ gives
\[
\phi(Q_0)(\lambda)\phi(q)(\lambda)=\phi(c)\ne0.
\]
Thus $\phi(q)(\lambda)\ne0$.  Sending $x\mapsto\lambda$ defines the desired extension $B\to K$ with $b$ nonzero.

Indeed, this assignment respects every relation defining $A[x]$: if $r(T)\in A[T]$ satisfies $r(x)=0$, then the minimal polynomial $F$ divides $r$ in $K(A)[T]$.  After working in the localization $A_a$ chosen above, division by the monic polynomial $F$ shows that $r=FH$ for some $H\in A_a[T]$.  Hence
\[
\phi(r)(\lambda)=\phi(F)(\lambda)\phi(H)(\lambda)=0.
\]
:::

<1>6. The algebraic lemma holds for every finitely generated $A$-algebra domain
\[
B=A[x_1,\ldots,x_n].
\]
::: {.proof}
Induct on $n$.  The case $n=1$ is <1>5.

Put
\[
C=A[x_1,\ldots,x_{n-1}],
\qquad
B=C[x_n].
\]
Apply the one-generator case over the domain $C$ to the nonzero element $b\in B$.  It gives a nonzero element
\[
c\in C
\]
such that every homomorphism $C\to K$ to an algebraically closed field which does not kill $c$ extends to $B\to K$ without killing $b$.

Apply the induction hypothesis to
\[
A\subseteq C
\]
and the nonzero element $c$.  There is $0\ne a\in A$ such that every $\phi:A\to K$ with $\phi(a)\ne0$ extends to a map $C\to K$ with $c$ nonzero.  Applying the property of $c$ then extends further to $B$ with $b$ nonzero.  This proves the lemma.
:::

<1>7. Let
\[
f:\Spec B\longrightarrow\Spec A
\]
be dominant, with $A\subseteq B$ noetherian integral domains and $B$ finitely generated over $A$.  Then $f(\Spec B)$ contains a nonempty principal open subset of $\Spec A$.
::: {.proof}
Apply <1>6 with
\[
b=1.
\]
Obtain $0\ne a\in A$ with the extension property.

We claim
\[
D(a)\subseteq f(\Spec B).
\]
Let $\mathfrak p\in D(a)$.  Compose
\[
A\longrightarrow\kappa(\mathfrak p)
\hookrightarrow
\overline{\kappa(\mathfrak p)}.
\]
The image of $a$ is nonzero.  By the algebra lemma, this map extends to
\[
B\longrightarrow\overline{\kappa(\mathfrak p)}.
\]
Let $\mathfrak q$ be its kernel.  Since the extension agrees with the original map on $A$,
\[
\mathfrak q\cap A=\mathfrak p.
\]
Thus $f(\mathfrak q)=\mathfrak p$.

Because $a\ne0$ and $A$ is a domain, $D(a)$ contains the generic point and is nonempty.  Hence the image contains a nonempty open subset.
:::

<1>8. This proves part (b).
::: {.proof}
Steps <1>5--<1>6 prove the algebraic lemma requested in the exercise, and <1>7 applies it with $b=1$ to the affine integral dominant morphism.
:::

<1>9. We now prove constructibility of $f(X)$ for every finite type morphism of noetherian schemes by noetherian induction on the target.
::: {.proof}
For a closed subset $Y'\subseteq Y$, let $\mathcal P(Y')$ be the assertion:

> for every finite type morphism $h:W\to Y'$ of noetherian schemes, the image $h(W)$ is constructible in $Y'$.

Assume inductively that $\mathcal P$ holds for every proper closed subset of $Y$.  We prove $\mathcal P(Y)$.
:::

<1>10. In proving $\mathcal P(Y)$, we may first assume that $Y$ is irreducible.  Under that assumption, if no irreducible component of $X$ dominates $Y$, then $f(X)$ is constructible by the induction hypothesis.
::: {.proof}
If $Y$ is reducible, write it as the finite union of its irreducible components
\[
Y=Y_1\cup\cdots\cup Y_m.
\]
Each $Y_j$ is a proper closed subset of $Y$.  The morphism
\[
f^{-1}(Y_j)\to Y_j
\]
is finite type by base change, so the induction hypothesis makes
\[
f\bigl(f^{-1}(Y_j)\bigr)
\]
constructible in $Y_j$, hence in $Y$.  Their finite union is $f(X)$.  Thus only irreducible $Y$ remains.

Now give the finitely many irreducible components $X_i$ of $X$ their reduced induced structures, and let
\[
Y_i=\overline{f(X_i)}.
\]
If no $X_i$ dominates the now irreducible $Y$, then every $Y_i$ is a proper closed subset of $Y$.

The factor map
\[
X_i\to Y_i
\]
is finite type by the same argument as in <1>3.  The induction hypothesis gives $f(X_i)$ constructible in $Y_i$, hence in $Y$.  Their finite union is $f(X)$.
:::

<1>11. Suppose an irreducible component $X_0\subseteq X$ has dense image in an irreducible component $Y_0\subseteq Y$.  Then $f(X)$ contains a nonempty open subset of $Y_0$.
::: {.proof}
Replace $X_0,Y_0$ by their reduced induced structures.  The map
\[
X_0\to Y_0
\]
is dominant and finite type.

Let $\eta\in Y_0$ be the generic point.  Choose an affine neighborhood
\[
V\subseteq Y_0
\]
of $\eta$.  Since the map is dominant, the generic point of $X_0$ lies over $\eta$.  Choose an affine neighborhood $U$ of that generic point with
\[
U\subseteq f^{-1}(V).
\]
Then
\[
U\to V
\]
is an affine integral dominant finite type morphism.  By <1>7, its image contains a nonempty open subset
\[
O\subseteq V.
\]
Thus
\[
O\subseteq f(X_0)\subseteq f(X).
\]
Since $O$ contains the generic point of $Y_0$, it is dense in $Y_0$.
:::

<1>12. The noetherian induction in <1>9 proves that $f(X)$ is constructible.
::: {.proof}
By <1>10, the reducible-target case and the case in which no component of $X$ dominates the irreducible target are already handled.

Otherwise <1>11 gives a nonempty open
\[
O\subseteq Y
\]
with
\[
O\subseteq f(X).
\]
Put
\[
F=Y\setminus O,
\]
a proper closed subset.  Then
\[
f(X)
=
O\cup f\bigl(f^{-1}(F)\bigr).
\]
The base change
\[
f^{-1}(F)\to F
\]
is finite type, so the induction hypothesis gives its image constructible in $F$, hence in $Y$.  The open set $O$ is constructible, so their union is constructible.

Thus $\mathcal P(Y)$ follows from $\mathcal P$ for proper closed subsets.  Hartshorne II.3.16 gives $\mathcal P(Y)$ for every noetherian target $Y$.
:::

<1>13. Therefore the image of every constructible subset under a finite type morphism of noetherian schemes is constructible.
::: {.proof}
Step <1>12 proves constructibility for the image of the whole source.  Step <1>1 reduces the general constructible-subset statement to that case.
:::

<1>14. A finite type morphism can have image which is open but not closed.
::: {.proof}
The projection
\[
\pi:V(xy-1)\subseteq\mathbb A^2_k\longrightarrow\mathbb A^1_k,
\qquad
(x,y)\longmapsto x,
\]
has image
\[
\mathbb A^1_k\setminus\{0\}.
\]
Indeed, the equation $xy=1$ has a solution $y=x^{-1}$ exactly when $x\ne0$.  This image is open and not closed.
:::

<1>15. A finite type morphism can have image which is closed but not open.
::: {.proof}
The closed immersion
\[
\{0\}\hookrightarrow\mathbb A^1_k
\]
is finite type and has image the closed point $\{0\}$, which is not open.
:::

<1>16. A finite type morphism can have image which is neither open nor closed.
::: {.proof}
Consider
\[
F:\mathbb A^2_k\longrightarrow\mathbb A^2_k,
\qquad
(x,y)\longmapsto(x,xy).
\]
Its image is
\[
D(x)\cup\{(0,0)\}.
\]
For $x\ne0$, any second coordinate $v$ occurs by taking $y=v/x$.  For $x=0$, the second coordinate is forced to be $0$.

This subset is not closed because it contains the dense open $D(x)$ but is not all of $\mathbb A^2$.  It is not open because every Zariski-open neighborhood of $(0,0)$ meets the line $x=0$ away from the origin, while those points are not in the image.
Equivalently, its complement
\[
\{(0,v):v\ne0\}
\]
is not closed: its closure is the whole line $V(x)$, which also contains $(0,0)$.
:::

<1>17. Q.E.D.
::: {.proof}
Step <1>4 proves part (a), <1>8 proves part (b), <1>12--<1>13 prove part (c) and the theorem, and <1>14--<1>16 give the examples requested in part (d).
:::
:::
