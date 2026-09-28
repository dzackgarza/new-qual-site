---
schema: qual/card@1
id: P-AGH2218RINGMAPSPEC
kind: problem
title: Injectivity and surjectivity of a ring map read off from the induced morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Ring Homomorphisms
  - Closed Immersions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.18 statement and its hint factoring through Spec(A/ker phi).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Compare properties of a ring homomorphism to the induced morphism on spectra.

a. Let $A$ be a ring, $X = \Spec A$, and $f \in A$.
Show that $f$ is nilpotent if and only if $D(f)$ is empty.

b. Let $\phi: A \to B$ be a homomorphism of rings and let $f: Y = \Spec B \to X = \Spec A$ be the induced morphism of affine schemes.
Show that $\phi$ is injective if and only if the map of sheaves $f^{\sharp}: \OO_X \to f_* \OO_Y$ is injective.
Show furthermore that in that case $f$ is dominant, that is, $f(Y)$ is dense in $X$.

c. With the same notation, show that if $\phi$ is surjective then $f$ is a homeomorphism of $Y$ onto a closed subset of $X$, and $f^{\sharp}: \OO_X \to f_* \OO_Y$ is surjective.

d. Prove the converse to (c): if $f: Y \to X$ is a homeomorphism onto a closed subset and $f^{\sharp}: \OO_X \to f_* \OO_Y$ is surjective, then $\phi$ is surjective.
:::

::: {.remark}
For part (d), consider $X' = \Spec\qty{A/\ker \phi}$ and apply parts (b) and (c).
:::

::: {.solution}
<1>1. For $f\in A$,
\[
D(f)=\varnothing
\iff
f\text{ is nilpotent}.
\]
::: {.proof}
By definition,
\[
D(f)=\{\mathfrak p\in\Spec A:f\notin\mathfrak p\}.
\]
Thus $D(f)=\varnothing$ exactly when $f$ lies in every prime ideal of $A$.  The intersection of all prime ideals is the nilradical $\sqrt{(0)}$, so this is equivalent to $f$ being nilpotent.
:::

<1>2. Let $\phi:A\to B$ be injective.  Then
\[
f^\sharp:\mathcal O_X\longrightarrow f_*\mathcal O_Y
\]
is injective.
::: {.proof}
The distinguished opens $D(a)$ form a basis of $X$.  Their inverse images are
\[
f^{-1}(D(a))=D(\phi(a))\subseteq\Spec B,
\]
and the map on sections is
\[
A_a\longrightarrow B_{\phi(a)}.
\]
Suppose $x/a^n$ maps to zero.  Then for some $m\ge0$,
\[
\phi(a)^m\phi(x)=0.
\]
Injectivity of $\phi$ gives $a^mx=0$ in $A$, hence $x/a^n=0$ in $A_a$.  Thus the map is injective on every distinguished basic open, and therefore $f^\sharp$ is injective as a map of sheaves.
:::

<1>3. Conversely, if $f^\sharp$ is injective, then $\phi$ is injective.
::: {.proof}
On global sections the sheaf map is exactly
\[
\Gamma(X,\mathcal O_X)=A
\longrightarrow
\Gamma(Y,\mathcal O_Y)=B,
\]
namely $\phi$.  An injective sheaf morphism is injective on sections over every open set, in particular over $X$.  Hence $\phi$ is injective.
:::

<1>4. If $\phi$ is injective, then $f:Y\to X$ is dominant.
::: {.proof}
It is enough to show that every nonempty distinguished open $D(a)\subseteq X$ meets $f(Y)$.  By <1>1, nonemptiness of $D(a)$ means that $a$ is not nilpotent.  Since $\phi$ is injective, $\phi(a)$ is not nilpotent in $B$.  Again by <1>1,
\[
D(\phi(a))\ne\varnothing.
\]
Choose $\mathfrak q\in D(\phi(a))$.  Then
\[
f(\mathfrak q)=\phi^{-1}(\mathfrak q)\in D(a).
\]
Thus the image meets every nonempty basic open, so it is dense.
:::

<1>5. If $\phi$ is surjective and $I=\ker\phi$, then
\[
Y\cong\Spec(A/I)
\]
and $f$ is a homeomorphism onto the closed subset $V(I)\subseteq X$.
::: {.proof}
The first isomorphism theorem gives
\[
B\cong A/I.
\]
Prime ideals of $A/I$ correspond bijectively to prime ideals of $A$ containing $I$, and this correspondence is a homeomorphism
\[
\Spec(A/I)\xrightarrow{\sim}V(I).
\]
Under the identification $B\cong A/I$, this is exactly the map $f$.
:::

<1>6. If $\phi$ is surjective, then $f^\sharp$ is surjective.
::: {.proof}
For a distinguished open $D(a)\subseteq X$, the map on sections is
\[
A_a\longrightarrow B_{\phi(a)}.
\]
Localization preserves surjections, so this map is surjective.  Since distinguished opens form a basis, $f^\sharp$ is surjective as a sheaf morphism.
:::

<1>7. Assume conversely that $f$ is a homeomorphism onto a closed subset of $X$ and that $f^\sharp$ is surjective.  Put
\[
I=\ker\phi,
\qquad
X'=\Spec(A/I),
\]
and factor
\[
Y\xrightarrow{g}X'\xrightarrow{h}X.
\]
Then $g$ is a homeomorphism.
::: {.proof}
The ring map
\[
A/I\longrightarrow B
\]
is injective.  By <1>4, $g(Y)$ is dense in $X'$.

By <1>5, $h$ is a homeomorphism of $X'$ onto $V(I)$.  Also
\[
f(Y)=h(g(Y)).
\]
The set $f(Y)$ is closed by hypothesis, so $g(Y)$ is closed in $X'$.  Since it is both closed and dense,
\[
g(Y)=X'.
\]
Finally $f$ and $h$ are homeomorphisms onto the same closed subset $V(I)=f(Y)$, and $f=h\circ g$.  Hence
\[
g=h^{-1}\circ f
\]
is a homeomorphism.
:::

<1>8. The sheaf map
\[
g^\sharp:\mathcal O_{X'}\longrightarrow g_*\mathcal O_Y
\]
is an isomorphism.
::: {.proof}
Because $A/I\to B$ is injective, <1>2 shows that $g^\sharp$ is injective.

For surjectivity, work on stalks.  At a point $y\in Y$, write $x'=g(y)$ and $x=h(x')$.  The map on stalks for $f=h\circ g$ factors as
\[
\mathcal O_{X,x}
\longrightarrow
\mathcal O_{X',x'}
\xrightarrow{g^\sharp_{x'}}
\mathcal O_{Y,y}.
\]
The composite is surjective because $f^\sharp$ is surjective.  Therefore the second arrow is surjective as well.  Thus $g^\sharp$ is both injective and surjective on every stalk, hence is an isomorphism of sheaves.
:::

<1>9. Under the hypotheses of <1>7, $\phi$ is surjective.
::: {.proof}
By <1>7, $g$ is a homeomorphism, and by <1>8 its map on structure sheaves is an isomorphism.  Hence $g$ is an isomorphism of schemes.

Taking global sections gives an isomorphism
\[
A/I\xrightarrow{\sim}B.
\]
Thus the original map
\[
A\longrightarrow B
\]
is the quotient map by $I=\ker\phi$, followed by an isomorphism, and is therefore surjective.
:::

<1>10. Q.E.D.
::: {.proof}
Step <1>1 proves part (a), steps <1>2--<1>4 prove part (b), steps <1>5--<1>6 prove part (c), and steps <1>7--<1>9 prove part (d).
:::
:::
