---
schema: qual/card@1
id: P-AGH223REDUCED
kind: problem
title: Reducedness is local, and every scheme has a reduction
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Reduced Schemes
  - Nilpotents
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.3 statement and source-order placement after II.2.2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
A scheme $(X, \OO_X)$ is **reduced** if for every open set $U \subseteq X$ the ring $\OO_X(U)$ has no nilpotent elements.

a. Show that $(X, \OO_X)$ is reduced if and only if for every $P \in X$ the local ring $\OO_{X, P}$ has no nilpotent elements.

b. Let $(X, \OO_X)$ be a scheme.
Let $(\OO_X)_{\mathrm{red}}$ be the sheaf associated to the presheaf $U \mapsto \OO_X(U)_{\mathrm{red}}$, where for any ring $A$ we denote by $A_{\mathrm{red}}$ the quotient of $A$ by its ideal of nilpotent elements.
Show that $\qty{X, (\OO_X)_{\mathrm{red}}}$ is a scheme.
We call it the **reduced scheme** associated to $X$ and denote it by $X_{\mathrm{red}}$.
Show that there is a morphism of schemes $X_{\mathrm{red}} \to X$ which is a homeomorphism on the underlying topological spaces.

c. Let $f: X \to Y$ be a morphism of schemes and assume that $X$ is reduced.
Show that there is a unique morphism $g: X \to Y_{\mathrm{red}}$ such that $f$ is obtained by composing $g$ with the natural map $Y_{\mathrm{red}} \to Y$.
:::

::: {.solution}
<1>1. If every ring of sections $\mathcal O_X(U)$ is reduced, then every local ring $\mathcal O_{X,P}$ is reduced.
::: {.proof}
Let
\[
\xi\in\mathcal O_{X,P}
\]
be nilpotent.
Choose an open neighborhood
\[
P\in U
\]
and a section
\[
s\in\mathcal O_X(U)
\]
representing $\xi$.

If
\[
\xi^n=0,
\]
then the germ of $s^n$ at $P$ is zero.
By the definition of equality in a stalk, after shrinking to some open
\[
P\in V\subseteq U
\]
one has
\[
(s|_V)^n=0
\]
in $\mathcal O_X(V)$.
This ring is reduced by hypothesis, so
\[
s|_V=0.
\]
Hence
\[
\xi=0.
\]
Thus the local ring has no nonzero nilpotents.
:::

<1>2. Conversely, if every local ring $\mathcal O_{X,P}$ is reduced, then every ring $\mathcal O_X(U)$ is reduced.
::: {.proof}
Let
\[
s\in\mathcal O_X(U)
\]
satisfy
\[
s^n=0.
\]
For every $P\in U$, the germ $s_P$ satisfies
\[
(s_P)^n=0
\]
in the reduced local ring $\mathcal O_{X,P}$.
Hence
\[
s_P=0
\]
for every $P$.

A section of a sheaf whose germ is zero at every point is itself zero: each point has a neighborhood on which the section vanishes, and the sheaf uniqueness axiom glues those local zeroes.
Therefore
\[
s=0.
\]
So $\mathcal O_X(U)$ is reduced.
:::

<1>3. Therefore
\[
\boxed{
X\text{ is reduced}
\iff
\mathcal O_{X,P}\text{ is reduced for every }P\in X.
}
\]
::: {.proof}
Combine <1>1 and <1>2.
:::

<1>4. Reduction commutes with localization.
For a ring $A$ and $f\in A$,
\[
\boxed{
(A_f)_{\mathrm{red}}
\cong
(A_{\mathrm{red}})_{\bar f},
}
\]
where
\[
A_{\mathrm{red}}=A/\sqrt{(0)}.
\]
::: {.proof}
The nilradical localizes:
\[
\sqrt{(0)}_{A_f}
=
(\sqrt{(0)}_A)_f.
\]
Indeed, if
\[
\frac a{f^m}
\]
is nilpotent in $A_f$, then for some $n$,
\[
\frac{a^n}{f^{mn}}=0.
\]
Thus some power $f^r a^n=0$ in $A$, so
\[
(f^ra)^n=0,
\]
and the fraction lies in the localization of the nilradical.
The reverse inclusion is immediate.

Therefore
\[
(A_f)_{\mathrm{red}}
=
A_f/(\sqrt0)_f
\cong
(A/\sqrt0)_{\bar f}.
\]
:::

<1>5. Let
\[
V=\operatorname{Spec}A\subseteq X
\]
be affine.
Then the restriction of $(\mathcal O_X)_{\mathrm{red}}$ to $V$ is the usual structure sheaf of
\[
\operatorname{Spec}A_{\mathrm{red}}.
\]
::: {.proof}
On the distinguished basis
\[
D(f)\subseteq V,
\]
the presheaf whose sheafification defines $(\mathcal O_X)_{\mathrm{red}}$ has values
\[
\mathcal O_X(D(f))_{\mathrm{red}}
=(A_f)_{\mathrm{red}}.
\]
By <1>4 this is
\[
(A_{\mathrm{red}})_{\bar f},
\]
which is exactly
\[
\mathcal O_{\operatorname{Spec}A_{\mathrm{red}}}(D(\bar f)).
\]
These identifications commute with restriction maps, so after sheafification the two structure sheaves agree on the affine chart.
:::

<1>6. The quotient map
\[
A\longrightarrow A_{\mathrm{red}}
\]
induces a homeomorphism
\[
\boxed{
\operatorname{Spec}A_{\mathrm{red}}
\xrightarrow{\sim}
\operatorname{Spec}A.
}
\]
::: {.proof}
Every prime ideal of $A$ contains the nilradical
\[
\sqrt{(0)}.
\]
Hence extension and contraction along
\[
A\to A/\sqrt0
\]
give a bijection
\[
\operatorname{Spec}(A/\sqrt0)
\longleftrightarrow
\operatorname{Spec}A.
\]

Closed sets correspond because an ideal $I\subseteq A$ and its image
\[
(I+\sqrt0)/\sqrt0
\]
define corresponding prime sets.
Thus the bijection is a homeomorphism.
:::

<1>7. The locally ringed space
\[
X_{\mathrm{red}}
:=
\left(X,(\mathcal O_X)_{\mathrm{red}}\right)
\]
is a scheme.
::: {.proof}
Choose an affine open cover
\[
X=\bigcup_iV_i,
\qquad
V_i\cong\operatorname{Spec}A_i.
\]
By <1>5--<1>6, on the same underlying open subset $V_i$ the reduced structure is isomorphic to
\[
\operatorname{Spec}(A_i)_{\mathrm{red}}.
\]
Thus $X_{\mathrm{red}}$ is covered by affine schemes and hence is a scheme.
:::

<1>8. The identity map of the underlying topological space, together with the quotient on structure sheaves, defines a morphism
\[
\boxed{
\iota:X_{\mathrm{red}}\longrightarrow X
}
\]
which is a homeomorphism on underlying spaces.
::: {.proof}
Sectionwise quotient gives a morphism of presheaves
\[
\mathcal O_X
\longrightarrow
\left(U\mapsto\mathcal O_X(U)_{\mathrm{red}}\right),
\]
and hence, after sheafification, a morphism
\[
\mathcal O_X
\longrightarrow
(\mathcal O_X)_{\mathrm{red}}.
\]
Together with the identity continuous map
\[
|X|\to|X|,
\]
this has the correct contravariant direction for a morphism
\[
X_{\mathrm{red}}\to X.
\]

Affinely it is the morphism
\[
\operatorname{Spec}A_{\mathrm{red}}
\longrightarrow
\operatorname{Spec}A
\]
from <1>6, so it is a homeomorphism locally and hence globally.

On a stalk it is the quotient
\[
\mathcal O_{X,P}
\longrightarrow
(\mathcal O_{X,P})_{\mathrm{red}}.
\]
The inverse image of the maximal ideal of the quotient is the maximal ideal of the original local ring, so this map is local.
Thus $\iota$ is a morphism of schemes.
:::

<1>9. Let
\[
f:X\longrightarrow Y
\]
be a morphism with $X$ reduced.
The sheaf map
\[
f^\sharp:\mathcal O_Y
\longrightarrow
f_*\mathcal O_X
\]
annihilates every nilpotent local section of $\mathcal O_Y$.
::: {.proof}
Let $V\subseteq Y$ be open and suppose
\[
s\in\mathcal O_Y(V)
\]
is nilpotent, say
\[
s^n=0.
\]
Then
\[
f^\sharp(s)^n
=f^\sharp(s^n)
=0
\]
in
\[
\mathcal O_X(f^{-1}V).
\]
Since $X$ is reduced, the ring of sections on every open set is reduced by definition.
Hence
\[
f^\sharp(s)=0.
\]
:::

<1>10. The morphism $f^\sharp$ factors uniquely through the reduced structure sheaf:
\[
\boxed{
\mathcal O_Y
\longrightarrow
(\mathcal O_Y)_{\mathrm{red}}
\xrightarrow{g^\sharp}
f_*\mathcal O_X.
}
\]
::: {.proof}
By <1>9, on each open set $V$ the ring map
\[
\mathcal O_Y(V)
\longrightarrow
\mathcal O_X(f^{-1}V)
\]
kills the nilradical.
Hence it factors uniquely through
\[
\mathcal O_Y(V)_{\mathrm{red}}.
\]
These factorizations commute with restrictions because the original maps do.
Thus they define a morphism from the presheaf
\[
V\longmapsto\mathcal O_Y(V)_{\mathrm{red}}
\]
to the sheaf $f_*\mathcal O_X$.
By the universal property of sheafification, it factors uniquely through
\[
(\mathcal O_Y)_{\mathrm{red}}.
\]
:::

<1>11. The continuous map underlying $g$ is the same as the map underlying $f$, and the morphism
\[
g:X\longrightarrow Y_{\mathrm{red}}
\]
defined by <1>10 is a morphism of schemes satisfying
\[
f=\iota_Y\circ g.
\]
::: {.proof}
The reduction morphism
\[
\iota_Y:Y_{\mathrm{red}}\to Y
\]
is the identity on the underlying topological space by <1>8, so any factorization of $f$ through it must use the same continuous map
\[
|X|\to|Y|=|Y_{\mathrm{red}}|.
\]

It remains to check that the induced maps on stalks are local.
At $P\in X$, put
\[
Q=f(P).
\]
The stalk map for $f$ factors as
\[
\mathcal O_{Y,Q}
\longrightarrow
(\mathcal O_{Y,Q})_{\mathrm{red}}
\xrightarrow{g_P^\sharp}
\mathcal O_{X,P}.
\]
Since $f_P^\sharp$ is local,
\[
(f_P^\sharp)^{-1}(\mathfrak m_{X,P})
=\mathfrak m_{Y,Q}.
\]
The maximal ideal of the reduced local ring is
\[
\mathfrak m_{Y,Q}/\sqrt0,
\]
so
\[
(g_P^\sharp)^{-1}(\mathfrak m_{X,P})
=\mathfrak m_{Y,Q}/\sqrt0.
\]
Thus $g_P^\sharp$ is local, and $g$ is a morphism of schemes.

The equality
\[
f=\iota_Y\circ g
\]
holds both on underlying spaces and on structure sheaves by the factorization in <1>10.
:::

<1>12. The factorization $g$ is unique.
::: {.proof}
Any such factorization must have the same underlying continuous map, because
\[
|Y_{\mathrm{red}}|\to|Y|
\]
is the identity.
On sheaves, its map
\[
(\mathcal O_Y)_{\mathrm{red}}
\longrightarrow
f_*\mathcal O_X
\]
must compose with
\[
\mathcal O_Y\to(\mathcal O_Y)_{\mathrm{red}}
\]
to give $f^\sharp$.
The uniqueness in <1>10 therefore forces the sheaf map to be $g^\sharp$.
Hence the scheme morphism is unique.
:::

<1>13. Thus reduction has the universal property
\[
\boxed{
\operatorname{Hom}(X,Y_{\mathrm{red}})
\xrightarrow{\sim}
\operatorname{Hom}(X,Y)
}
\]
for every reduced scheme $X$.
::: {.proof}
Existence and uniqueness are exactly <1>11 and <1>12.
:::

<1>14. Q.E.D.
::: {.proof}
Steps <1>1--<1>3 prove part (a), <1>4--<1>8 prove part (b), and <1>9--<1>13 prove part (c).
:::
:::
