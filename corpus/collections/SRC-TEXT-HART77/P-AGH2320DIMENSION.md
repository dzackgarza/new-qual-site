---
schema: qual/card@1
id: P-AGH2320DIMENSION
kind: problem
title: Dimension of an integral scheme of finite type over a field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Function Fields
  - Codimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.20 statement and the standard dimension formulas for finite-type algebras over fields.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be an integral scheme of finite type over a field $k$, not necessarily algebraically closed.
Prove the following, where for rings $\krulldim$ always means the Krull dimension.

a. For any closed point $P \in X$, $\krulldim X = \krulldim \OO_P$.

b. Let $K(X)$ be the function field of $X$.
Then
\[
\krulldim X = \trdeg\qty{K(X)/k}.
\]

c. If $Y$ is a closed subset of $X$, then
\[
\codim(Y, X) = \inf \ts{\krulldim \OO_{P, X} \st P \in Y}.
\]

d. If $Y$ is a closed subset of $X$, then
\[
\krulldim Y + \codim(Y, X) = \krulldim X.
\]

e. If $U$ is a nonempty open subset of $X$, then $\krulldim U = \krulldim X$.

f. If $k \subseteq k'$ is a field extension, then every irreducible component of $X' = \fiberprod{X}{k}{k'}$ has dimension equal to $\krulldim X$.
:::

::: {.solution}
We use the following standard affine dimension theorem.

If $A$ is a finitely generated integral $k$-algebra with fraction field $K$, then
\[
\dim A=\operatorname{trdeg}_kK,
\]
every maximal localization $A_{\mathfrak m}$ has this same dimension, and for every prime $\mathfrak p\subseteq A$,
\[
\boxed{
\dim A_{\mathfrak p}
+\operatorname{trdeg}_k\kappa(\mathfrak p)
=\operatorname{trdeg}_kK.}
\]
The first two assertions follow from Noether normalization and going up; the last is the dimension formula for finite-type algebras over a field.  These are Stacks Project, Tags 00P0 and 00P1.

<1>1. Every nonempty affine open
\[
U=\Spec A\subseteq X
\]
has
\[
\dim U
=
\operatorname{trdeg}_kK(X).
\]
::: {.proof}
Since $X$ is integral, $A$ is a domain.  Since $X$ is of finite type over $k$, Hartshorne II.3.3(c) shows that $A$ is a finitely generated $k$-algebra.

By Hartshorne II.3.6,
\[
\operatorname{Frac}(A)\cong K(X).
\]
The affine dimension theorem therefore gives
\[
\dim U=\dim A=\operatorname{trdeg}_kK(X).
\]
:::

<1>2. Put
\[
r=\operatorname{trdeg}_kK(X).
\]
Then
\[
\dim X\le r.
\]
::: {.proof}
Take any strict chain of irreducible closed subsets
\[
Z_0\subsetneq Z_1\subsetneq\cdots\subsetneq Z_n
\]
in $X$.

The closed subscheme $Z_0$ with its reduced induced structure is of finite type over $k$.  By Hartshorne II.3.14, it contains a closed point $P$.  Since $Z_0$ is closed in $X$, this point is closed in $X$ as well.

Choose an affine open neighborhood
\[
U\subseteq X
\]
of $P$.  Each intersection
\[
Z_i\cap U
\]
is nonempty and irreducible.  Moreover the inclusions remain strict.  Indeed, if
\[
Z_i\cap U=Z_{i+1}\cap U,
\]
then the nonempty open subset $Z_{i+1}\cap U$ of the irreducible space $Z_{i+1}$ would lie in the proper closed subset $Z_i$, impossible.

Thus
\[
Z_0\cap U\subsetneq\cdots\subsetneq Z_n\cap U
\]
is a chain of length $n$ in $U$.  By <1>1,
\[
n\le\dim U=r.
\]
Taking the supremum over all chains gives $\dim X\le r$.
:::

<1>3. One has
\[
\dim X\ge r.
\]
::: {.proof}
Any nonempty affine open $U\subseteq X$ is a subspace of $X$, so every chain of irreducible closed subsets in $U$ gives a chain of the same length in $X$ after taking closures in $X$.  Hence
\[
\dim U\le\dim X.
\]
By <1>1, $\dim U=r$.
:::

<1>4. Therefore
\[
\boxed{
\dim X=\operatorname{trdeg}_kK(X).}
\]
::: {.proof}
Combine <1>2 and <1>3.  This proves part (b).
:::

<1>5. Let $P\in X$ be a closed point.  Then
\[
\boxed{\dim\mathcal O_{X,P}=\dim X.}
\]
::: {.proof}
Choose an affine neighborhood
\[
U=\Spec A
\]
of $P$, and let $\mathfrak m\subseteq A$ be the corresponding maximal ideal.  Then
\[
\mathcal O_{X,P}=A_{\mathfrak m}.
\]
By <1>1, the fraction field of $A$ is $K(X)$ and
\[
\operatorname{trdeg}_kK(X)=\dim X.
\]
The maximal-localization part of the affine dimension theorem gives
\[
\dim A_{\mathfrak m}
=
\operatorname{trdeg}_kK(X)
=
\dim X.
\]
This proves part (a).
:::

<1>6. If $P\in X$ and
\[
Z=\overline{\{P\}},
\]
then
\[
\boxed{
\codim(Z,X)=\dim\mathcal O_{X,P}.}
\]
::: {.proof}
The point $P$ is the generic point of the irreducible closed subset $Z$.  By the definition of codimension in a scheme, chains of irreducible closed subsets from $Z$ up to an irreducible component of $X$ correspond in an affine neighborhood of $P$ to chains of prime ideals contained in the prime representing $P$.  Their supremal length is the height of that prime, namely
\[
\dim\mathcal O_{X,P}.
\]
Since $X$ is integral it has one irreducible component, so this is exactly $\codim(Z,X)$.
:::

<1>7. For every closed subset $Y\subseteq X$,
\[
\boxed{
\codim(Y,X)
=
\inf_{P\in Y}\dim\mathcal O_{X,P}.}
\]
::: {.proof}
By definition,
\[
\codim(Y,X)
\]
is the infimum of $\codim(Z,X)$ over irreducible closed subsets $Z\subseteq Y$.

Every point $P\in Y$ gives such an irreducible closed subset
\[
\overline{\{P\}}\subseteq Y,
\]
and <1>6 identifies its codimension with $\dim\mathcal O_{X,P}$.

Conversely every irreducible closed $Z\subseteq Y$ has a generic point $P\in Y$, and
\[
Z=\overline{\{P\}}.
\]
Thus the two sets of numbers over which the infima are taken are identical.  This proves part (c).
:::

<1>8. Let $Z\subseteq X$ be irreducible closed with generic point $\zeta$.  Then
\[
\boxed{
\dim Z+\codim(Z,X)=\dim X.}
\]
::: {.proof}
Give $Z$ its reduced induced structure.  It is an integral scheme of finite type over $k$, with function field
\[
K(Z)=\kappa(\zeta).
\]
By <1>4 applied to $Z$,
\[
\dim Z=\operatorname{trdeg}_k\kappa(\zeta).
\]
By <1>6,
\[
\codim(Z,X)=\dim\mathcal O_{X,\zeta}.
\]

Choose an affine neighborhood $\Spec A$ of $\zeta$, corresponding to a prime $\mathfrak p\subseteq A$.  The affine dimension formula gives
\[
\dim A_{\mathfrak p}
+\operatorname{trdeg}_k\kappa(\mathfrak p)
=\operatorname{trdeg}_kK(X).
\]
Using <1>4 for $X$ converts this exactly into the displayed identity.
:::

<1>9. For every closed subset $Y\subseteq X$,
\[
\boxed{
\dim Y+\codim(Y,X)=\dim X.}
\]
::: {.proof}
Let
\[
Y_1,\ldots,Y_m
\]
be the irreducible components of $Y$.  Then
\[
\dim Y=\max_i\dim Y_i.
\]

By <1>8,
\[
\codim(Y_i,X)=\dim X-\dim Y_i.
\]
Any irreducible closed subset of $Y$ is contained in some $Y_i$, and its dimension is at most $\dim Y_i$, so <1>8 shows that its codimension is at least $\codim(Y_i,X)$.  Hence
\[
\codim(Y,X)
=
\min_i\codim(Y_i,X)
=
\dim X-\max_i\dim Y_i.
\]
This proves part (d).
:::

<1>10. If $U\subseteq X$ is nonempty open, then
\[
\boxed{\dim U=\dim X.}
\]
::: {.proof}
Choose a nonempty affine open
\[
V\subseteq U.
\]
Since $V$ is also a nonempty affine open of $X$, <1>1 and <1>4 give
\[
\dim V=\dim X.
\]
As subspaces,
\[
V\subseteq U\subseteq X,
\]
so
\[
\dim V\le\dim U\le\dim X.
\]
Therefore all three dimensions are equal.  This proves part (e).
:::

<1>11. Let $k\subseteq k'$ be a field extension and put
\[
X'=X\times_k k'.
\]
Every irreducible component of $X'$ maps dominantly to $X$.
::: {.proof}
The projection
\[
\pi:X'\to X
\]
is flat, because it is obtained by base change from the flat field extension $k\to k'$.

Let $C$ be an irreducible component of $X'$ with generic point $\xi_C$.  Work in an affine neighborhood
\[
U=\Spec A\subseteq X
\]
of the image of $\xi_C$.  On the corresponding affine base change
\[
U'=\Spec(A\otimes_k k'),
\]
the generic point of $C$ is represented by a minimal prime $\mathfrak q$.  Flatness gives going down, so the contraction of the minimal prime $\mathfrak q$ is a minimal prime of the domain $A$, hence is $(0)$.

Thus $\xi_C$ maps to the generic point of $X$, and $C\to X$ is dominant.
:::

<1>12. Choose a nonempty affine open
\[
U=\Spec A\subseteq X
\]
and put
\[
d=\dim X.
\]
There is a finite injective Noether-normalization map
\[
k[t_1,\ldots,t_d]\hookrightarrow A.
\]
After base change,
\[
k'[t_1,\ldots,t_d]
\hookrightarrow
A'=A\otimes_k k'
\]
is again finite and injective.
::: {.proof}
By <1>4,
\[
d=\operatorname{trdeg}_kK(X)=\operatorname{trdeg}_k\operatorname{Frac}(A).
\]
Noether normalization gives algebraically independent elements $t_1,\ldots,t_d\in A$ such that $A$ is finite over the polynomial subring $k[t_1,\ldots,t_d]$.

Tensoring with the flat $k$-module $k'$ preserves injectivity, and tensoring a finite module with $k'$ remains finite.  This gives the asserted map.
:::

<1>13. Every irreducible component of
\[
U'=U\times_k k'=\Spec A'
\]
has dimension $d$.
::: {.proof}
Let $\mathfrak q$ be a minimal prime of $A'$.  The ring $A'$ is integral over
\[
R=k'[t_1,\ldots,t_d]
\]
by <1>12.  The contraction
\[
\mathfrak q\cap R
\]
is a minimal prime of $R$ under an integral extension.  Since $R$ is a domain,
\[
\mathfrak q\cap R=(0).
\]

Therefore
\[
R\hookrightarrow A'/\mathfrak q
\]
is an integral finite extension.  Integral extensions preserve Krull dimension, so
\[
\dim(A'/\mathfrak q)
=
\dim R
=d.
\]
This is the dimension of the irreducible component $V(\mathfrak q)$.
:::

<1>14. Every irreducible component $C$ of $X'$ has dimension $d=\dim X$.
::: {.proof}
By <1>11, $C$ contains a point mapping to the generic point of $X$, so it meets the inverse image $U'$ of every nonempty open $U\subseteq X$.  Hence
\[
C\cap U'
\]
is a nonempty open subset of $C$.  It is an irreducible component of $U'$: if it were properly contained in a larger irreducible closed subset of $U'$, its closure in $X'$ would be an irreducible closed subset properly containing the component $C$.

By <1>13,
\[
\dim(C\cap U')=d.
\]
Give $C$ its reduced induced structure.  It is an integral scheme of finite type over $k'$.  Part (e), already proved in <1>10, gives
\[
\dim C=\dim(C\cap U')=d.
\]
This proves part (f).
:::

<1>15. Q.E.D.
::: {.proof}
Step <1>5 proves part (a), <1>4 proves part (b), <1>7 proves part (c), <1>9 proves part (d), <1>10 proves part (e), and <1>14 proves part (f).
:::
:::
