---
schema: qual/card@1
id: P-AGH228DUALNUM
kind: problem
title: Dual numbers detect Zariski tangent vectors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Tangent Spaces
  - Dual Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.8 statement and source-order placement after II.2.7.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a scheme.
For any point $x \in X$, define the **Zariski tangent space** $T_x$ to $X$ at $x$ to be the dual of the $k(x)$-vector space $\mfm_x / \mfm_x^2$.

Now assume that $X$ is a scheme over a field $k$, and let $k[\eps]/\eps^2$ be the ring of dual numbers over $k$.
Show that to give a $k$-morphism $\Spec k[\eps]/\eps^2 \to X$ is equivalent to giving a point $x \in X$ rational over $k$, that is, with $k(x) = k$, together with an element of $T_x$.
:::

::: {.solution}
Put
\[
R=k[\varepsilon]/(\varepsilon^2),
\qquad
S=\operatorname{Spec}R.
\]

<1>1. The scheme $S$ has a single point, corresponding to the maximal ideal
\[
(\varepsilon),
\]
and its residue field is $k$.
::: {.proof}
Every prime ideal contains every nilpotent element, so any prime of $R$ contains $\varepsilon$.  Prime ideals of $R$ therefore correspond to prime ideals of
\[
R/(\varepsilon)\cong k.
\]
The field $k$ has the single prime ideal $(0)$, so $R$ has the single prime ideal $(\varepsilon)$.

The quotient by this maximal ideal is
\[
R/(\varepsilon)\cong k.
\]
:::

<1>2. A $k$-morphism
\[
f:S\longrightarrow X
\]
determines a point
\[
x=f((\varepsilon))\in X
\]
and a local $k$-algebra homomorphism
\[
\phi=f^\sharp_x:
\mathcal O_{X,x}
\longrightarrow
R.
\]
::: {.proof}
The source has one point, so the underlying continuous map chooses $x$.  The map on stalks at that point is local because $f$ is a morphism of schemes.  Since $f$ is a morphism over $\operatorname{Spec}k$, the stalk map commutes with the structure maps from $k$, so it is a $k$-algebra homomorphism.
:::

<1>3. The point $x$ in <1>2 is $k$-rational:
\[
\boxed{\kappa(x)=k.}
\]
::: {.proof}
Reduce the local homomorphism
\[
\phi:\mathcal O_{X,x}\to R
\]
modulo the maximal ideal $(\varepsilon)$ of $R$.  Since $\phi$ is local, its inverse image of $(\varepsilon)$ is the maximal ideal $\mathfrak m_x$.  Therefore reduction induces an injective $k$-algebra homomorphism
\[
\kappa(x)
=\mathcal O_{X,x}/\mathfrak m_x
\hookrightarrow
R/(\varepsilon)
=k.
\]

The structural map $k\to\kappa(x)$ followed by this injection is the identity because $f$ is a $k$-morphism.  Hence the inclusion $k\to\kappa(x)$ is an isomorphism: the image of $\kappa(x)$ in $k$ contains all of $k$ and is contained in $k$.  Thus $\kappa(x)=k$ as a $k$-algebra.
:::

<1>4. Under the identification $\kappa(x)=k$, every local $k$-algebra map
\[
\phi:\mathcal O_{X,x}\longrightarrow R
\]
whose reduction is the residue map has a unique form
\[
\boxed{
\phi(a)=\bar a+D(a)\varepsilon,
}
\]
where
\[
D:\mathcal O_{X,x}\longrightarrow k
\]
is a $k$-derivation and $\bar a$ is the residue class of $a$ in $k$.
::: {.proof}
Every element of $R$ has a unique expression
\[
c+d\varepsilon,
\qquad c,d\in k.
\]
Since reduction of $\phi(a)$ modulo $\varepsilon$ is the residue $\bar a$, there is a unique scalar $D(a)\in k$ with
\[
\phi(a)=\bar a+D(a)\varepsilon.
\]

Additivity of $\phi$ makes $D$ additive.  Because $\phi$ is a $k$-algebra map,
\[
D(c)=0
\qquad(c\in k).
\]
Finally,
\[
\begin{aligned}
\phi(ab)
&=\phi(a)\phi(b)\\
&=(\bar a+D(a)\varepsilon)
(\bar b+D(b)\varepsilon)\\
&=\bar a\bar b
+(\bar aD(b)+\bar bD(a))\varepsilon,
\end{aligned}
\]
because $\varepsilon^2=0$.  Comparing the $\varepsilon$-coefficients gives
\[
D(ab)=\bar aD(b)+\bar bD(a),
\]
which is the Leibniz rule for a derivation to the residue-field module $k$.

Conversely, any $k$-derivation $D$ makes the displayed formula additive, multiplicative, and unital, hence defines such a $k$-algebra homomorphism.
:::

<1>5. A $k$-derivation
\[
D:\mathcal O_{X,x}\longrightarrow k
\]
is equivalent to a $k$-linear functional
\[
\lambda:
\mathfrak m_x/\mathfrak m_x^2
\longrightarrow k.
\]
::: {.proof}
If
\[
a,b\in\mathfrak m_x,
\]
then
\[
\bar a=\bar b=0,
\]
so the Leibniz rule gives
\[
D(ab)=0.
\]
Hence $D$ vanishes on $\mathfrak m_x^2$.

Also $D$ vanishes on $k$.  Since the residue field is $k$, every
\[
a\in\mathcal O_{X,x}
\]
has a unique decomposition
\[
a=\bar a+m,
\qquad
\bar a\in k,
\quad
m\in\mathfrak m_x.
\]
Thus $D$ is completely determined by its restriction to $\mathfrak m_x$, and that restriction factors uniquely through a $k$-linear map
\[
\lambda:\mathfrak m_x/\mathfrak m_x^2\to k.
\]

Conversely, given such a linear functional $\lambda$, define
\[
D(a)=\lambda(a-\bar a\bmod\mathfrak m_x^2).
\]
For
\[
a=\bar a+m,
\qquad
b=\bar b+n,
\]
one has modulo $\mathfrak m_x^2$
\[
ab-\bar a\bar b
\equiv
\bar a n+\bar b m.
\]
Applying $\lambda$ gives
\[
D(ab)=\bar aD(b)+\bar bD(a),
\]
so $D$ is a $k$-derivation.
:::

<1>6. Therefore local $k$-algebra maps
\[
\mathcal O_{X,x}\longrightarrow k[\varepsilon]/(\varepsilon^2)
\]
reducing to the residue map are naturally parametrized by the Zariski tangent space
\[
\boxed{
T_xX
=
(\mathfrak m_x/\mathfrak m_x^2)^\vee.
}
\]
::: {.proof}
Step <1>4 identifies such local maps with $k$-derivations to $k$, and <1>5 identifies those derivations with the dual of $\mathfrak m_x/\mathfrak m_x^2$.
:::

<1>7. Conversely, let $x\in X$ be $k$-rational and let
\[
v\in T_xX.
\]
The corresponding derivation $D_v$ and formula
\[
\phi_v(a)=\bar a+D_v(a)\varepsilon
\]
define a local $k$-algebra homomorphism
\[
\phi_v:\mathcal O_{X,x}\longrightarrow R.
\]
::: {.proof}
By <1>5, $v$ corresponds to a $k$-derivation $D_v$.  Step <1>4 shows that $\phi_v$ is a $k$-algebra homomorphism.

Its reduction modulo $(\varepsilon)$ is the residue map
\[
\mathcal O_{X,x}\to k,
\]
so
\[
\phi_v^{-1}((\varepsilon))=\mathfrak m_x.
\]
Thus $\phi_v$ is local.
:::

<1>8. The local homomorphism $\phi_v$ defines a unique $k$-morphism
\[
f_v:\operatorname{Spec}R\longrightarrow X
\]
with underlying point $x$.
::: {.proof}
Send the unique point of $\operatorname{Spec}R$ to $x$.

For an open set $U\subseteq X$ containing $x$, define the pullback on sections as
\[
\mathcal O_X(U)
\longrightarrow
\mathcal O_{X,x}
\xrightarrow{\phi_v}
R,
\]
where the first map takes a germ at $x$.  If $x\notin U$, the inverse image in the one-point source is empty, so use the unique map to the zero ring.

These maps commute with restrictions and define a morphism of sheaves.  The only stalk map is $\phi_v$, which is local by <1>7, so this is a morphism of schemes.  It is a $k$-morphism because $\phi_v$ is a $k$-algebra map.

Uniqueness follows because any morphism with underlying point $x$ is determined by its local-ring map at that point, exactly as in Hartshorne II.2.7.
:::

<1>9. The two constructions are inverse.  Hence
\[
\boxed{
\operatorname{Hom}_k
\left(
\operatorname{Spec}k[\varepsilon]/(\varepsilon^2),X
\right)
\cong
\coprod_{x\in X(k)}T_xX.
}
\]
::: {.proof}
Starting with a morphism, steps <1>2--<1>6 extract its point $x$ and the coefficient derivation $D$, hence the tangent vector $v$.  Reconstructing from $v$ gives the same stalk homomorphism
\[
a\mapsto\bar a+D(a)\varepsilon,
\]
and therefore the same morphism by <1>8.

Starting from $(x,v)$, the constructed morphism has stalk map $\phi_v$, whose $\varepsilon$-coefficient is exactly $D_v$ and hence recovers the original tangent vector.
:::

<1>10. Q.E.D.
::: {.proof}
Step <1>9 is the equivalence requested by the exercise.
:::
:::
