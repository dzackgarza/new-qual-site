---
schema: qual/card@1
id: P-AGH2322FIBREDIM
kind: problem
title: Dimension of the fibres of a dominant morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Fibres
  - Constructible Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.22 statement, its stated hints, and the standard local dimension inequality for fibres.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $f: X \to Y$ be a dominant morphism of integral schemes of finite type over a field $k$.

a. Let $Y'$ be a closed irreducible subset of $Y$ whose generic point $\eta'$ is contained in $f(X)$.
   Let $Z$ be any irreducible component of $\inverseof{f}(Y')$ such that $\eta' \in f(Z)$, and show that $\codim(Z, X) \leq \codim(Y', Y)$.

b. Let $e = \krulldim X - \krulldim Y$ be the relative dimension of $X$ over $Y$.
   For any point $y \in f(X)$, show that every irreducible component of the fibre $X_y$ has dimension $\geq e$.

c. Show that there is a dense open subset $U \subseteq X$ such that for any $y \in f(U)$ one has $\krulldim U_y = e$.

d. Going back to the original morphism $f: X \to Y$, for any integer $h$ let $E_h$ be the set of points $x \in X$ such that, letting $y = f(x)$, there is an irreducible component $Z$ of the fibre $X_y$ containing $x$ with $\krulldim Z \geq h$.
   Show that $E_e = X$, that $E_h$ is not dense in $X$ when $h > e$, and that $E_h$ is closed for all $h$.

e. Prove the following theorem of Chevalley.
   For each integer $h$, let $C_h$ be the set of points $y \in Y$ such that $\krulldim X_y = h$.
   Then the subsets $C_h$ are constructible, and $C_e$ contains an open dense subset of $Y$.
:::

::: {.remark}
For (b), let $Y' = \cl\qty{\ts{y}}$ and use (a) together with II.3.20(b). For (c), first reduce to the case where $X = \Spec A$ and $Y = \Spec B$ are affine, so that $A$ is a finitely generated $B$-algebra.
Take $t_1, \ldots, t_e \in A$ forming a transcendence base of $K(X)$ over $K(Y)$, and let $X_1 = \Spec B[t_1, \ldots, t_e]$, which is affine $e$-space over $Y$; the morphism $X \to X_1$ is generically finite, so II.3.7 applies.
For (d), use (b), then (c), then induction on $\krulldim X$.
See Cartan and Chevalley, exposé 8.
:::

::: {.solution}
We use the standard local dimension inequality for a homomorphism of noetherian rings.
If a prime $\mathfrak q\subseteq S$ lies over $\mathfrak p\subseteq R$, then
\[
\dim S_{\mathfrak q}
\le
\dim R_{\mathfrak p}
+\dim\bigl(S_{\mathfrak q}/\mathfrak pS_{\mathfrak q}\bigr).
\]
This is Stacks Project, Tag 00OM.

<1>1. In part (a), the assertion is local around the generic points of $Y'$ and $Z$.
Choose affine neighborhoods
\[
Y_0=\Spec B\subseteq Y,
\qquad
X_0=\Spec A\subseteq X
\]
of $\eta'$ and the generic point $\zeta$ of $Z$, with
\[
X_0\subseteq f^{-1}(Y_0).
\]
Let $\mathfrak p\subseteq B$ and $\mathfrak q\subseteq A$ be the primes corresponding to $\eta'$ and $\zeta$.
Then
\[
\mathfrak q\cap B=\mathfrak p
\]
and $\mathfrak q$ is minimal over $\mathfrak pA$.
::: {.proof} The equality of contractions says exactly that $f(\zeta)=\eta'$.

The inverse image of $Y'$ in $X_0$ is cut out set-theoretically by $\mathfrak pA$.
Since $Z$ is an irreducible component of $f^{-1}(Y')$, its intersection with $X_0$ is an irreducible component of this inverse image.
Thus its generic prime $\mathfrak q$ is minimal over $\mathfrak pA$.
:::

<1>2. One has
\[
\dim\bigl(A_{\mathfrak q}/\mathfrak pA_{\mathfrak q}\bigr)=0.
\]
::: {.proof}
Primes of this quotient correspond to primes
\[
\mathfrak r\subseteq A
\]
with
\[
\mathfrak pA\subseteq\mathfrak r\subseteq\mathfrak q.
\]
Minimality of $\mathfrak q$ over $\mathfrak pA$ forces
\[
\mathfrak r=\mathfrak q.
\]
Hence the quotient has one prime ideal and dimension $0$.
:::

<1>3. Therefore
\[
\boxed{\codim(Z,X)\le\codim(Y',Y).}
\]
::: {.proof}
Apply the local dimension inequality to
\[
B_{\mathfrak p}\longrightarrow A_{\mathfrak q}.
\]
By <1>2,
\[
\dim A_{\mathfrak q}\le\dim B_{\mathfrak p}.
\]
Hartshorne II.3.20(c) identifies these local dimensions with the codimensions of the irreducible closed subsets whose generic points are $\zeta$ and $\eta'$:
\[
\dim A_{\mathfrak q}=\codim(Z,X),
\qquad
\dim B_{\mathfrak p}=\codim(Y',Y).
\]
This proves part (a).
:::

<1>4. Let $y\in f(X)$ and let $W$ be an irreducible component of the fibre $X_y$.
If
\[
Y'=\overline{\{y\}}
\]
and
\[
Z=\overline W\subseteq X,
\]
then $Z$ is an irreducible component of $f^{-1}(Y')$, and its generic point maps to $y$, the generic point of $Y'$.
::: {.proof} Work on affine neighborhoods
\[
Y_0=\Spec B\ni y,
\qquad
X_0=\Spec A
\]
meeting the generic point of $W$.
Let $\mathfrak p\subseteq B$ represent $y$.

By Hartshorne II.3.10, the fibre is
\[
\Spec\bigl(A\otimes_B\kappa(\mathfrak p)\bigr).
\]
An irreducible component $W$ corresponds to a prime $\mathfrak q\subseteq A$ minimal among primes containing $\mathfrak pA$ and disjoint from $B\setminus\mathfrak p$.
Such a prime satisfies
\[
\mathfrak q\cap B=\mathfrak p.
\]

If a prime $\mathfrak r\subsetneq\mathfrak q$ contained $\mathfrak pA$, then
\[
\mathfrak p\subseteq\mathfrak r\cap B\subseteq\mathfrak q\cap B=\mathfrak p,
\]
so $\mathfrak r\cap B=\mathfrak p$ and $\mathfrak r$ would define a smaller prime in the fibre, contradicting minimality.
Hence $\mathfrak q$ is minimal over $\mathfrak pA$.

Thus $V(\mathfrak q)$ is an irreducible component of the inverse image of $V(\mathfrak p)=Y'\cap Y_0$.  Taking its closure in $X$ gives the asserted component $Z$ of $f^{-1}(Y')$.  Its generic point is the same point represented by $\mathfrak q$, and its image is $y$.
:::

<1>5. With the notation of <1>4,
\[
\boxed{\dim W=\dim Z-\dim Y'.}
\]
::: {.proof} Let $w$ be the generic point of $W$, equivalently of $Z$.
Since $w$ maps to the generic point $y$ of $Y'$, there is an inclusion of function fields
\[
K(Y')=\kappa(y)\hookrightarrow\kappa(w)=K(Z).
\]

The fibre component $W$ is an integral scheme of finite type over the field $\kappa(y)$, with function field $\kappa(w)$.  Hartshorne II.3.20(b) gives
\[
\dim W
=
\operatorname{trdeg}_{\kappa(y)}\kappa(w).
\]
By additivity of transcendence degree,
\[
\operatorname{trdeg}_{\kappa(y)}\kappa(w)
=
\operatorname{trdeg}_k\kappa(w)
-
\operatorname{trdeg}_k\kappa(y).
\]
Applying II.3.20(b) to $Z$ and $Y'$ gives the displayed equality.
:::

<1>6. Every irreducible component of every nonempty fibre has dimension at least
\[
e=\dim X-\dim Y.
\]
::: {.proof}
Let $W,Z,Y'$ be as in <1>4.  Part (a) gives
\[
\codim(Z,X)\le\codim(Y',Y).
\]
By Hartshorne II.3.20(d),
\[
\dim X-\dim Z
\le
\dim Y-\dim Y'.
\]
Rearranging,
\[
\dim Z-\dim Y'
\ge
\dim X-\dim Y=e.
\]
Now apply <1>5:
\[
\dim W\ge e.
\]
This proves part (b).
:::

<1>7. For part (c), after replacing $X$ and $Y$ by dense affine opens, we may assume
\[
X=\Spec A,
\qquad
Y=\Spec B,
\]
with $B\hookrightarrow A$ a finitely generated inclusion of domains.
::: {.proof}
Choose an affine open neighborhood of the generic point of $Y$, and then an affine open neighborhood of the generic point of $X$ contained in its inverse image.  Both replacements are nonempty open subsets of integral finite-type schemes, so Hartshorne II.3.20(e) preserves their dimensions.  Their function fields are unchanged by II.3.6, so the relative dimension $e$ is unchanged as well.
:::

<1>8. There exist elements
\[
t_1,\ldots,t_e\in A
\]
which form a transcendence basis of
\[
K(X)/K(Y).
\]
The inclusion
\[
B[t_1,\ldots,t_e]\hookrightarrow A
\]
defines a dominant generically finite morphism
\[
g:X\longrightarrow X_1:=\Spec B[t_1,\ldots,t_e]\cong\mathbb A^e_Y.
\]
::: {.proof} By II.3.20(b),
\[
e
=
\operatorname{trdeg}_{K(Y)}K(X).
\]
Since $K(X)$ is generated as a field over $K(Y)$ by finitely many elements of the finitely generated $B$-algebra $A$, a maximal algebraically independent subset of algebra generators may be chosen inside $A$; call it $t_1,\ldots,t_e$.

Their algebraic independence over $K(Y)$ implies that
\[
B[t_1,\ldots,t_e]
\]
is a polynomial ring over $B$ and injects into $A$.
Hence $g$ is dominant.

The field extension
\[
K(X)/K(Y)(t_1,\ldots,t_e)
\]
is algebraic and finitely generated as a field extension, hence finite.  Thus the generic fibre of $g$ is finite, so $g$ is generically finite.
:::

<1>9. There is a dense open subset
\[
W\subseteq X_1
\]
such that
\[
U:=g^{-1}(W)\longrightarrow W
\]
is finite and surjective.
::: {.proof} Hartshorne II.3.7 applied to the generically finite morphism $g$ gives a dense open $W$ such that $U\to W$ is finite.

The restriction remains dominant because $U$ and $W$ contain the generic points.  A finite morphism is closed, so its image is both closed and dense in the irreducible space $W$.  Hence its image is all of $W$.
:::

<1>10. For every $y\in f(U)$,
\[
\boxed{\dim U_y=e.}
\]
::: {.proof} The morphism $X_1\to Y$ is affine $e$-space.
Its fibre at $y$ is
\[
(X_1)_y\cong\mathbb A^e_{\kappa(y)}.
\]
The open set $W_y$ is nonempty because $y\in f(U)$ and $U\to W$ is surjective.
Hence
\[
\dim W_y=e
\]
by Hartshorne II.3.20(e), applied over the field $\kappa(y)$.

Base changing the finite surjective map $U\to W$ to $\Spec\kappa(y)$ gives a finite surjective morphism
\[
U_y\longrightarrow W_y.
\]
Integral finite extensions preserve Krull dimension, so
\[
\dim U_y=\dim W_y=e.
\]
This proves part (c).
:::

<1>11. For the original morphism $f:X\to Y$, one has
\[
\boxed{E_e=X.}
\]
::: {.proof}
Given $x\in X$, put $y=f(x)$ and choose an irreducible component of $X_y$ containing $x$.  By part (b), every such component has dimension at least $e$.  Hence $x\in E_e$.
:::

<1>12. If $h>e$, then $E_h$ is not dense in $X$.
::: {.proof} Let $U\subseteq X$ be the dense open subset from part (c). We claim
\[
E_h\cap U=\varnothing.
\]

Let $x\in U$ and $y=f(x)$.
If $Z$ is an irreducible component of $X_y$ containing $x$, then
\[
Z\cap U_y
\]
is a nonempty open subset of $Z$.
Therefore
\[
\dim Z
=
\dim(Z\cap U_y)
\le
\dim U_y=e.
\]
Part (b) gives the reverse inequality, so in fact every fibre component through a point of $U$ has dimension exactly $e$.
Thus no point of $U$ lies in $E_h$ for $h>e$.

Since $U$ is nonempty open, $E_h$ cannot be dense.
:::

<1>13. We prove by induction on $\dim X$ that every $E_h$ is closed.
::: {.proof} If $\dim X=0$, every nonempty fibre component has dimension $0$, so each $E_h$ is either $X$ or $\varnothing$.

Assume the assertion for dominant morphisms whose integral source has dimension $<\dim X$.

For $h\le e$, part (b) gives
\[
E_h=X,
\]
which is closed.
Now suppose $h>e$.
Let $U$ be the dense open from part (c). By <1>12,
\[
E_h\subseteq F:=X\setminus U,
\]
a proper closed subset.

Let
\[
F_1,\ldots,F_r
\]
be the irreducible components of $F$, with their reduced induced structures, and let
\[
Y_i=\overline{f(F_i)}
\]
with reduced induced structures.  Each
\[
f_i:F_i\longrightarrow Y_i
\]
is a dominant finite type morphism of integral schemes.  Indeed, the composite $F_i\to Y$ is finite type, while $F_i\to Y_i$ is quasi-compact because $F_i$ is noetherian; Hartshorne II.3.13(f) therefore makes the factor map finite type.  Since $F_i$ is a proper closed irreducible subset of the integral finite-type scheme $X$, II.3.20(d) gives
\[
\dim F_i<\dim X.
\]
Thus the induction hypothesis applies to every $f_i$.
:::

<1>14. With the notation of <1>13,
\[
E_h(f)=\bigcup_{i=1}^r E_h(f_i).
\]
::: {.proof} Let $x\in E_h(f)$.
Choose an irreducible component
\[
Z\subseteq X_{f(x)}
\]
containing $x$ with $\dim Z\ge h$.

Every point of $Z$ belongs to $E_h(f)$ because the same component $Z$ witnesses the condition.
Hence
\[
Z\subseteq E_h(f)\subseteq F.
\]
As $Z$ is irreducible and $F$ is the finite union of the $F_i$, it lies in some $F_i$.
Then $Z$ is also an irreducible component of the fibre $(F_i)_{f(x)}$: any larger irreducible subset of that fibre would be a larger irreducible subset of $X_{f(x)}$, contradicting maximality of $Z$.
Thus
\[
x\in E_h(f_i).
\]

Conversely, if $x\in E_h(f_i)$, an irreducible component $W$ of $(F_i)_{f(x)}$ through $x$ has dimension at least $h$.  It lies in some irreducible component $Z$ of the full fibre $X_{f(x)}$, and
\[
\dim Z\ge\dim W\ge h.
\]
Hence $x\in E_h(f)$.
:::

<1>15. Every set $E_h$ is closed.
::: {.proof} For $h\le e$ this was already observed in <1>13. For $h>e$, the induction hypothesis makes each
\[
E_h(f_i)
\]
closed in $F_i$, hence closed in $X$.
Step <1>14 expresses $E_h(f)$ as their finite union, so it is closed.

This completes the induction and proves the closedness assertion in part (d), together with <1>11--<1>12.
:::

<1>16. For any integer $h\ge0$, let
\[
D_h=\{y\in Y:\dim X_y\ge h\}.
\]
Then
\[
\boxed{D_h=f(E_h).}
\]
::: {.proof} If $y\in D_h$, some irreducible component of $X_y$ has dimension at least $h$; any point on that component belongs to $E_h$ and maps to $y$.

Conversely, if $y=f(x)$ for some $x\in E_h$, the component witnessing $x\in E_h$ has dimension at least $h$, so $\dim X_y\ge h$.
:::

<1>17. Every $D_h$ is constructible.
::: {.proof}
By part (d), $E_h$ is closed in the noetherian finite-type scheme $X$.  Give it the reduced induced closed subscheme structure.  The restricted morphism
\[
E_h\longrightarrow Y
\]
is finite type.  Chevalley's theorem, Hartshorne II.3.19, therefore says that its image
\[
f(E_h)=D_h
\]
is constructible.
:::

<1>18. For every integer $h\ge0$,
\[
\boxed{C_h=D_h\setminus D_{h+1}}
\]
and hence $C_h$ is constructible.
::: {.proof} A nonempty fibre has dimension exactly $h$ if and only if its dimension is at least $h$ but not at least $h+1$.
For $h\ge0$, an empty fibre belongs to neither side.
Thus the displayed equality holds.

Constructible subsets form a Boolean algebra, so the difference of the constructible sets $D_h$ and $D_{h+1}$ is constructible.

With the standard convention $\dim\varnothing=-1$,
\[
C_{-1}=Y\setminus f(X),
\]
which is constructible because $f(X)$ is constructible by Hartshorne II.3.19.  For $h<-1$, $C_h=\varnothing$.  Hence $C_h$ is constructible for every integer $h$.
:::

<1>19. The generic fibre $X_\eta$, where $\eta$ is the generic point of $Y$, is integral and has dimension $e$.
::: {.proof} Work on affine neighborhoods
\[
Y_0=\Spec B,
\qquad
X_0=\Spec A
\]
of the generic points, with $B\hookrightarrow A$ an inclusion of domains.
The generic fibre has coordinate ring
\[
S^{-1}A,
\qquad
S=B\setminus\{0\},
\]
which is a domain.
Thus $X_\eta$ is integral.

Its function field is $K(X)$ and its ground field is
\[
\kappa(\eta)=K(Y).
\]
Hartshorne II.3.20(b) gives
\[
\dim X_\eta
=
\operatorname{trdeg}_{K(Y)}K(X).
\]
Additivity of transcendence degree and II.3.20(b) for $X$ and $Y$ give
\[
\operatorname{trdeg}_{K(Y)}K(X)
=
\dim X-\dim Y=e.
\]
:::

<1>20. The constructible subset $C_e\subseteq Y$ contains a dense open subset of $Y$.
::: {.proof} By <1>19, the generic point $\eta$ of the irreducible space $Y$ belongs to $C_e$.
Step <1>18 shows that $C_e$ is constructible.

Hartshorne II.3.18(b) says that a constructible subset of an irreducible Zariski space which contains the generic point is dense and contains a nonempty open subset.  Thus $C_e$ contains an open dense subset of $Y$.
:::

<1>21. Q.E.D.
::: {.proof}
Steps <1>1--<1>3 prove part (a), <1>4--<1>6 prove part (b), <1>7--<1>10 prove part (c), <1>11--<1>15 prove part (d), and <1>16--<1>20 prove part (e).
:::
:::
