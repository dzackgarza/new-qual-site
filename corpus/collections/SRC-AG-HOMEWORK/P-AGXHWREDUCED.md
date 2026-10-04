---
schema: qual/card@1
id: P-AGXHWREDUCED
kind: problem
title: Reducedness on stalks and the universal property of the reduction of a scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Reduced Schemes
  - Nilpotents
  - Sheafification
relations: []
review: draft
---

::: {.problem}
Call $(X, \OO_X)\in \Sch$ **reduced** iff $\OO_X(U)$ has no nilpotents for every open $U$, and for $A\in \Ring$ define $A^{\red}\da A/\sqrt{0}$ to be $A$ modulo its ideal of nilpotents.

a. Show that $X$ is reduced iff for every $p\in X$, the local ring $\OO_{X, p}$ has no nilpotents.

b. Let $\OO_X^{\red}$ be the sheafification of $U \mapsto \OO_X(U)^{\red}$.
Show that $X_{\red}\da (X, \OO_X^{\red})$ is a scheme, and that there is a morphism of schemes $X_{\red}\xrightarrow{\red} X$ inducing a homeomorphism $\abs{X_{\red}}\to \abs{X}$ on underlying topological spaces.

c. Let $X \xrightarrow{f} Y\in \Sch$ with $X$ reduced.
Show that there is a unique morphism $X \xrightarrow{g} Y_{\red}$ such that $f$ is the composition

\begin{tikzcd}
	X && Y \\
	\\
	&& {Y_{\red}}
	\arrow["f", from=1-1, to=1-3]
	\arrow["{\exists ! g}"', from=1-1, to=3-3]
	\arrow["\red"', from=3-3, to=1-3]
\end{tikzcd}
:::

::: {.remark}
Strategy for part a: zero in every stalk implies zero by the sheaf axiom.

Strategy for part b:

- Cover by affines.

- $\sqrt{0_{R}} \leq \mfp$ for every $\mfp\in \Spec R$.

- $R_{\red}\da R/\sqrt{0_{R}}$ is a quotient, and localization commutes with quotients.

- Maps $R\to S$ with $S$ reduced factor through $R_{\red}$.

- Sheafification has the same stalks, and an isomorphism on stalks is an isomorphism of sheaves.

- Pushforwards of reduced sheaves are reduced.
:::

::: {.solution}
<1>1. If $X$ is reduced, then every local ring $\OO_{X,p}$ is reduced.

::: {.proof}
Fix $p\in X$ and let $\sigma\in\OO_{X,p}$ satisfy $\sigma^n=0$ for some $n\geq1$.
Choose an open neighborhood $U$ of $p$ and a section $s\in\OO_X(U)$ representing
$\sigma$.  The equality $\sigma^n=0$ means that, after shrinking to some open
neighborhood $V\subseteq U$ of $p$,
$$
(s|_V)^n=0\in\OO_X(V).
$$
Since $X$ is reduced, $\OO_X(V)$ has no nonzero nilpotents, so $s|_V=0$.
Hence $\sigma=0$ in the stalk.  Thus $\OO_{X,p}$ is reduced.
:::

<1>2. If every local ring $\OO_{X,p}$ is reduced, then $X$ is reduced.

::: {.proof}
Let $U\subseteq X$ be open and let $s\in\OO_X(U)$ satisfy $s^n=0$.
For every $p\in U$,
$$
(s_p)^n=(s^n)_p=0
$$
in the reduced ring $\OO_{X,p}$, hence $s_p=0$.
Therefore, for each $p\in U$, there is an open neighborhood $V_p\subseteq U$
on which $s|_{V_p}=0$.  The sets $V_p$ cover $U$, so the uniqueness axiom for
the sheaf $\OO_X$ gives $s=0$.  Thus every ring $\OO_X(U)$ is reduced.
:::

<1>3. Part (a) follows.

::: {.proof}
Steps <1>1 and <1>2 prove the two implications.
:::

<1>4. For every ring $A$ and every $f\in A$, there is a canonical isomorphism
$$
(A_f)^{\red}\cong (A^{\red})_{\bar f},
$$
where $\bar f$ denotes the image of $f$ in $A^{\red}$.

::: {.proof}
It suffices to show that the nilradical commutes with localization:
$$
\sqrt{0_{A_f}}=(\sqrt{0_A})_f.
$$
The inclusion from right to left is immediate.  Conversely, suppose
$a/f^m\in A_f$ is nilpotent.  Then for some $n\geq1$,
$$
\frac{a^n}{f^{mn}}=0.
$$
Hence there exists $r\geq0$ such that $f^r a^n=0$ in $A$.  Then
$(f^r a)^n=0$, so $f^r a\in\sqrt{0_A}$, while
$$
\frac{a}{f^m}=\frac{f^r a}{f^{m+r}}.
$$
Thus $a/f^m\in(\sqrt{0_A})_f$.  Quotienting by this localized nilradical gives
the claimed isomorphism.
:::

<1>5. If $U=\Spec A\subseteq X$ is affine, then the restriction of
$\OO_X^{\red}$ to $U$ is canonically the structure sheaf of
$\Spec(A^{\red})$ under the canonical homeomorphism
$$
\Spec(A^{\red})\xrightarrow{\sim}\Spec A.
$$

::: {.proof}
Every prime ideal of $A$ contains $\sqrt{0_A}$, so contraction along
$A\twoheadrightarrow A^{\red}$ gives a bijection
$$
\Spec(A^{\red})\longrightarrow\Spec A.
$$
For an ideal $I\subseteq A$, the inverse image of $V(I)$ is
$V((I+\sqrt{0_A})/\sqrt{0_A})$, so this bijection is a homeomorphism.

Now let $D(f)\subseteq\Spec A$ be distinguished.  The presheaf
$V\mapsto\OO_X(V)^{\red}$ has value
$$
\OO_X(D(f))^{\red}
=(A_f)^{\red}
\cong
(A^{\red})_{\bar f}
$$
by step <1>4.  The right-hand side is exactly
$\OO_{\Spec(A^{\red})}(D(\bar f))$.
These isomorphisms commute with restriction maps because they are the canonical
localization maps.  Distinguished opens form a basis, so after sheafification
they identify
$$
\ro{\OO_X^{\red}}{U}
\cong
\OO_{\Spec(A^{\red})}
$$
under the displayed homeomorphism.
:::

<1>6. The locally ringed space
$$
X_{\red}\coloneqq (X,\OO_X^{\red})
$$
is a scheme.

::: {.proof}
Choose an affine open cover $X=\bigcup_i U_i$ with
$U_i\cong\Spec A_i$.  By step <1>5,
$$
(U_i,\ro{\OO_X^{\red}}{U_i})
\cong
\Spec(A_i^{\red})
$$
as locally ringed spaces.  Hence $X_{\red}$ is covered by affine schemes and is
therefore a scheme.
:::

<1>7. There is a canonical morphism of schemes
$$
\red:X_{\red}\longrightarrow X
$$
whose underlying map is the identity on $X$.

::: {.proof}
For every open $U\subseteq X$, the quotient homomorphism
$$
\OO_X(U)\longrightarrow \OO_X(U)^{\red}
$$
is compatible with restrictions.  Hence it defines a morphism from $\OO_X$ to
the presheaf $U\mapsto\OO_X(U)^{\red}$, and by the universal property of
sheafification it induces a sheaf morphism
$$
\OO_X\longrightarrow\OO_X^{\red}.
$$
Together with the identity map on the underlying space this gives a morphism of
ringed spaces $X_{\red}\to X$.

On an affine neighborhood $\Spec A$, step <1>5 identifies this morphism with
the morphism
$$
\Spec(A^{\red})\longrightarrow\Spec A
$$
induced by $A\twoheadrightarrow A^{\red}$.  Its maps on stalks are quotient
maps by nilpotent ideals and are local homomorphisms.  Thus the ringed-space
morphism is a morphism of schemes.
:::

<1>8. The morphism $\red:X_{\red}\to X$ induces a homeomorphism on
underlying spaces.

::: {.proof}
By construction its underlying map is the identity map of the topological space
$X$.  Equivalently, on every affine open this is the homeomorphism from step
<1>5.
:::

<1>9. Part (b) follows.

::: {.proof}
Step <1>6 proves that $X_{\red}$ is a scheme, and steps <1>7 and <1>8 give the
required morphism and homeomorphism.
:::

<1>10. Let $f:X\to Y$ be a morphism of schemes with $X$ reduced.  For every
open $V\subseteq Y$, the map
$$
f_V^\#:\OO_Y(V)\longrightarrow\OO_X(f^{-1}(V))
$$
kills every nilpotent element of $\OO_Y(V)$.

::: {.proof}
If $a\in\OO_Y(V)$ satisfies $a^n=0$, then
$$
f_V^\#(a)^n=f_V^\#(a^n)=0.
$$
Because $X$ is reduced, the ring $\OO_X(f^{-1}(V))$ is reduced.  Therefore
$f_V^\#(a)=0$.
:::

<1>11. The sheaf morphism $f^\#:\OO_Y\to f_*\OO_X$ factors uniquely through
$\OO_Y^{\red}$:
$$
\OO_Y\longrightarrow\OO_Y^{\red}
\xrightarrow{g^\#}
f_*\OO_X.
$$

::: {.proof}
By step <1>10, for every open $V\subseteq Y$, the homomorphism $f_V^\#$ factors
uniquely through
$$
\OO_Y(V)\twoheadrightarrow\OO_Y(V)^{\red}.
$$
These factorizations commute with restriction maps because the maps $f_V^\#$
do.  Hence they give a morphism from the presheaf
$V\mapsto\OO_Y(V)^{\red}$ to $f_*\OO_X$.  Since $f_*\OO_X$ is a sheaf, the
universal property of sheafification gives a unique sheaf morphism
$$
g^\#:\OO_Y^{\red}\longrightarrow f_*\OO_X
$$
with the stated factorization.
:::

<1>12. With the same underlying continuous map as $f$, the morphism $g^\#$
defines a morphism of schemes
$$
g:X\longrightarrow Y_{\red}.
$$

::: {.proof}
The spaces underlying $Y$ and $Y_{\red}$ are identical, so use the continuous
map underlying $f$.  It remains to check that the induced homomorphism on each
stalk is local.

For $x\in X$ and $y=f(x)$, the stalk map of $f$ is a local homomorphism
$$
f_x^\#:\OO_{Y,y}\longrightarrow\OO_{X,x}.
$$
By step <1>10 it kills the nilradical and hence factors as
$$
\OO_{Y,y}\twoheadrightarrow
\OO_{Y,y}^{\red}
\xrightarrow{g_x^\#}
\OO_{X,x}.
$$
If $\mathfrak m_x$ and $\mathfrak m_y$ are the maximal ideals, locality of
$f_x^\#$ gives
$$
(g_x^\#)^{-1}(\mathfrak m_x)
=\mathfrak m_y/\sqrt{0_{\OO_{Y,y}}},
$$
which is the maximal ideal of $\OO_{Y,y}^{\red}$.  Thus $g_x^\#$ is local,
so $g$ is a morphism of schemes.
:::

<1>13. The morphism $g$ satisfies
$$
f=\red\circ g.
$$

::: {.proof}
The two morphisms have the same underlying continuous map.  On structure
sheaves, the equality is exactly the factorization constructed in step <1>11.
:::

<1>14. The morphism $g$ is unique with this property.

::: {.proof}
Any factorization $f=\red\circ h$ must have the same underlying continuous map
as $f$, because $\red:Y_{\red}\to Y$ is the identity on underlying spaces.
On sheaves, the map $h^\#$ must factor $f^\#$ through the quotient presheaf
$V\mapsto\OO_Y(V)^{\red}$ and then through its sheafification.  The quotient
factorization and the sheafification factorization are both unique, so
$h^\#=g^\#$.  Hence $h=g$.
:::

<1>15. Part (c) follows.

::: {.proof}
Steps <1>12--<1>14 give existence, the required factorization, and uniqueness.
:::

<1>16. Q.E.D.

::: {.proof}
Steps <1>3, <1>9, and <1>15 establish parts (a), (b), and (c), respectively.
:::
:::
