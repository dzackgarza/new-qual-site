---
schema: qual/card@1
id: P-AGH447DUALOFAMORPHISM
kind: problem
title: The dual isogeny $\hat f$ satisfies $f \circ \hat f = n$ and $\deg \hat f = \deg f$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.7 together with the preceding identification
    X = Pic^0(X), the relative Picard/Jacobian construction, and the
    graph-line-bundle hint for starred part (d). The proof treats separable
    and purely inseparable maps separately in part (c), then proves
    additivity of the dual by the normalized family attached to a graph.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ and $X'$ be elliptic curves over $k$, with base points $P_0, P_0'$.

a. If $f: X \to X'$ is any morphism, use (4.11) to show that $f^*: \Pic X' \to \Pic X$ induces a homomorphism $\hat{f}: (X', P_0') \to (X, P_0)$. We call this the **dual** of $f$.

b. If $f: X \to X'$ and $g: X' \to X''$ are two morphisms, then $\widehat{g \circ f} = \hat{f} \circ \hat{g}$.

c. Assume $f(P_0)=P_0'$, and let $n=\deg f$. Show that if $Q \in X$ is any point, and $f(Q)=Q'$, then $\hat{f}(Q')=n_X(Q)$. (Do the separable and purely inseparable cases separately, then combine.) Conclude that $f \circ \hat{f}=n_{X'}$ and $\hat{f} \circ f=n_X$.

d. \* If $f, g: X \to X'$ are two morphisms preserving the base points $P_0, P_0'$, then $\widehat{f+g} = \hat{f}+\hat{g}$.

    Hints: It is enough to show for any $\mcl \in \Pic X'$, that $(f+g)^* \mcl \cong f^* \mcl \tensor g^* \mcl$. For any $f$, let $\Gamma_f: X \to X \times X'$ be the graph morphism. Then it is enough to show (for $\mcl'=p_2^* \mcl$) that
$$
\Gamma_{f+g}^*(\mcl')=\Gamma_f^* \mcl' \tensor \Gamma_g^* \mcl' .
$$
    Let $\sigma: X \to X \times X'$ be the section $x \mapsto (x, P_0')$. Define a subgroup $\Pic_\sigma$ of $\Pic(X\times X')$ consisting of those $\mcl$ which have degree 0 along each fibre of $p_1$ and satisfy $\sigma^* \mcl = 0 \in \Pic(X)$. Note that this subgroup is isomorphic to the group $\Pic^{\circ}(X'/X)$ used in the definition of the Jacobian variety. Hence there is a 1-1 correspondence between morphisms $f: X \to X'$ and elements $\mcl_f \in \Pic_\sigma$ (this defines $\mcl_f$). Now compute explicitly to show that $\Gamma_g^*(\mcl_f)=\Gamma_f^*(\mcl_g)$ for any $f, g$. Use the fact that $\mcl_{f+g}=\mcl_f \tensor \mcl_g$, and the fact that for any $\mcl$ on $X'$, $p_2^* \mcl \in \Pic_\sigma^{\circ}$ to prove the result.

e. Using (d), show that for any $n \in \ZZ$, $\hat{n}_X=n_X$. Conclude that $\deg n_X=n^2$.

f. Show for any $f$ that $\deg \hat{f}=\deg f$.
:::

::: {.solution}
For an elliptic curve $(E,O)$ write
$$
\alpha_E:E\longrightarrow\Pic^0(E),
\qquad
P\longmapsto\OO_E(P-O).
$$
The preceding results identify $\alpha_E$ as an isomorphism of group
varieties.

<1>1. For every morphism
$$
f:X\longrightarrow X'
$$
the pullback on line bundles induces a homomorphism
$$
\boxed{
\hat f
=
\alpha_X^{-1}\circ f^*\circ\alpha_{X'}
:
(X',P_0')\longrightarrow(X,P_0).
}
$$

::: {.proof}
If $f$ is nonconstant of degree $m$, then
$$
\deg f^*\mcl=m\deg\mcl,
$$
so pullback carries $\Pic^0(X')$ into $\Pic^0(X)$.  If $f$ is constant,
the pullback of every degree-zero line bundle is trivial, so the same
conclusion holds.

The relative Picard construction used in (4.11) shows that pullback is not
merely a homomorphism on $k$-points: it is a morphism of the represented
Picard varieties.  Moreover
$$
f^*(\mcl\tensor\mcn)
\cong
f^*\mcl\tensor f^*\mcn,
$$
so it is a group homomorphism.  Conjugating by the group-variety
isomorphisms $\alpha_{X'}$ and $\alpha_X$ gives the asserted homomorphism
$\hat f$.  Since
$$
f^*\OO_{X'}\cong\OO_X,
$$
it sends $P_0'$ to $P_0$.
:::

<1>2. If
$$
X\xrightarrow{f}X'\xrightarrow{g}X''
$$
are morphisms, then
$$
\boxed{
\widehat{g\circ f}
=
\hat f\circ\hat g.
}
$$

::: {.proof}
Pullback of line bundles is contravariantly functorial:
$$
(g\circ f)^*=f^*\circ g^*.
$$
Therefore
$$
\begin{aligned}
\widehat{g\circ f}
&=
\alpha_X^{-1}(g\circ f)^*\alpha_{X''}\\
&=
\alpha_X^{-1}f^*g^*\alpha_{X''}\\
&=
(\alpha_X^{-1}f^*\alpha_{X'})
(\alpha_{X'}^{-1}g^*\alpha_{X''})\\
&=
\hat f\circ\hat g.
\end{aligned}
$$
Here the middle juxtaposition denotes composition of the displayed
morphisms.
:::

<1>3. Assume now that
$$
f(P_0)=P_0',
\qquad
n=\deg f>0.
$$
If $f$ is separable and
$$
f(Q)=Q',
$$
then
$$
\boxed{\hat f(Q')=[n]Q.}
$$

::: {.proof}
Because $f$ carries origin to origin, it is a homomorphism of elliptic
curves.  A separable morphism between genus-one curves is unramified by
Riemann--Hurwitz.  Hence
$$
K=\ker f
$$
has exactly $n$ points and
$$
f^{-1}(Q')=Q+K
$$
with every point occurring with multiplicity one.  Thus
$$
\begin{aligned}
f^*\OO_{X'}(Q'-P_0')
&\cong
\OO_X\left(
\sum_{T\in K}(Q+T)-\sum_{T\in K}T
\right).
\end{aligned}
$$
Under the identification
$$
\Pic^0(X)\cong X,
$$
the class of a degree-zero divisor
$$
\sum_i P_i-\sum_i R_i
$$
corresponds to
$$
\sum_iP_i-\sum_iR_i
$$
in the group law.  The displayed divisor therefore corresponds to
$$
\sum_{T\in K}(Q+T)-\sum_{T\in K}T
=
nQ.
$$
By the definition in step <1>1 this point is $\hat f(Q')$.
:::

<1>4. Under the same hypotheses, if $f$ is purely inseparable, then again
$$
\boxed{\hat f(Q')=[n]Q.}
$$

::: {.proof}
A finite purely inseparable morphism of degree $n$ between smooth curves is
radicial.  Over the algebraically closed field, each fibre therefore has a
single point, with scheme-theoretic multiplicity $n$.  Hence
$$
f^*(Q')=nQ,
\qquad
f^*(P_0')=nP_0.
$$
Consequently
$$
f^*\OO_{X'}(Q'-P_0')
\cong
\OO_X\bigl(nQ-nP_0\bigr),
$$
whose class corresponds to $[n]Q$.
:::

<1>5. For an arbitrary nonconstant $f$ preserving the origins, one still has
$$
\boxed{
\hat f(f(Q))=[n]Q
}
$$
for every $Q\in X$.

::: {.proof}
Factor the finite extension of function fields into its inseparable and
separable parts.  On smooth projective models this gives
$$
X\xrightarrow{f_i}Y\xrightarrow{f_s}X',
$$
where $f_i$ is purely inseparable of degree $i$, $f_s$ is separable of
degree $s$, and
$$
n=is.
$$
The intermediate curve inherits the image of $P_0$ as origin, and both maps
preserve origins.

Put
$$
R=f_i(Q).
$$
Steps <1>3--<1>4 and contravariance from step <1>2 give
$$
\begin{aligned}
\hat f(f(Q))
&=
\widehat{f_s\circ f_i}(f_s(R))\\
&=
\hat f_i\bigl(\hat f_s(f_s(R))\bigr)\\
&=
\hat f_i([s]R)\\
&=
[s]\hat f_i(R)\\
&=
[s][i]Q\\
&=
[n]Q.
\end{aligned}
$$
:::

<1>6. Consequently
$$
\boxed{
\hat f\circ f=[n]_X,
\qquad
f\circ\hat f=[n]_{X'}.
}
$$

::: {.proof}
The first equality is exactly step <1>5.

Since a nonconstant morphism of projective curves is surjective, every
$Q'\in X'$ is $f(Q)$ for some $Q\in X$.  Then
$$
\begin{aligned}
f(\hat f(Q'))
&=
f([n]Q)\\
&=
[n]f(Q)\\
&=
[n]Q',
\end{aligned}
$$
because $f$ is a group homomorphism.  Hence
$$
f\circ\hat f=[n]_{X'}.
$$
This proves part (c).
:::

<1>7. Let
$$
p_1:X\times X'\longrightarrow X,
\qquad
p_2:X\times X'\longrightarrow X'
$$
be the projections and let
$$
\sigma:X\longrightarrow X\times X',
\qquad
x\longmapsto(x,P_0').
$$
For a morphism $h:X\to X'$ define
$$
\mcm_h
=
\OO_{X\times X'}\bigl(\Gamma_h-X\times\{P_0'\}\bigr)
\tensor
p_1^*h^*\OO_{X'}(P_0')^{-1}.
$$
Then $\mcm_h$ represents $h$ in the normalized relative Picard group
$\Pic_\sigma$ occurring in the hint.

::: {.proof}
On the fibre $\{x\}\times X'$ the graph $\Gamma_h$ cuts out the point
$h(x)$, while $X\times\{P_0'\}$ cuts out $P_0'$.  Therefore
$$
\mcm_h|_{\{x\}\times X'}
\cong
\OO_{X'}(h(x)-P_0').
$$
The last factor is pulled back from $X$ and hence does not change this fibre
class.

It remains to check the normalization along $\sigma$.  The graph is the
inverse image of the diagonal under
$$
(h\circ p_1,p_2):X\times X'\longrightarrow X'\times X'.
$$
Restricting the diagonal bundle to $X'\times\{P_0'\}$ gives
$\OO_{X'}(P_0')$.  Hence
$$
\sigma^*\OO(\Gamma_h)
\cong
h^*\OO_{X'}(P_0').
$$
The restriction of
$\OO(X\times\{P_0'\})$ along the constant section is trivial as a line
bundle on $X$.  Consequently
$$
\sigma^*\mcm_h\cong\OO_X.
$$
Thus $\mcm_h$ has degree zero on every $p_1$-fibre and is normalized along
$\sigma$.  Its fibre class is exactly
$$
x\longmapsto\OO_{X'}(h(x)-P_0'),
$$
so representability of $\Pic^0(X'/X)$ identifies it with the morphism $h$.
:::

<1>8. For any two morphisms $f,g:X\to X'$ one has the symmetric identity
$$
\boxed{
\Gamma_g^*\mcm_f
\cong
\Gamma_f^*\mcm_g.
}
$$

::: {.proof}
Pulling the graph divisor $\Gamma_f$ back along $\Gamma_g$ gives the
zero divisor of the difference morphism
$$
g-f:X\longrightarrow X'.
$$
Therefore
$$
\Gamma_g^*\OO(\Gamma_f)
\cong
(g-f)^*\OO_{X'}(P_0').
$$
Also
$$
\Gamma_g^*\OO(X\times\{P_0'\})
\cong
g^*\OO_{X'}(P_0'),
$$
and
$$
\Gamma_g^*p_1^*f^*\OO_{X'}(P_0')
\cong
f^*\OO_{X'}(P_0').
$$
Thus
$$
\Gamma_g^*\mcm_f
\cong
(g-f)^*\OO(P_0')
\tensor
g^*\OO(P_0')^{-1}
\tensor
f^*\OO(P_0')^{-1}.
$$
Since inversion fixes $P_0'$,
$$
[-1]^*\OO_{X'}(P_0')\cong\OO_{X'}(P_0'),
$$
so
$$
(g-f)^*\OO(P_0')
\cong
(f-g)^*\OO(P_0').
$$
The resulting expression is symmetric in $f$ and $g$, proving the claim.
:::

<1>9. If $f,g:X\to X'$ preserve the base points, then
$$
\boxed{
\widehat{f+g}=\hat f+\hat g.
}
$$

::: {.proof}
The group law on the relative Jacobian is tensor product, so step <1>7 gives
$$
\mcm_{f+g}
\cong
\mcm_f\tensor\mcm_g.
$$

Let $\mcl\in\Pic^0(X')$.  There is a unique point $A\in X'$ such that
$$
\mcl\cong\OO_{X'}(A-P_0').
$$
Let
$$
h:X\longrightarrow X'
$$
be the constant morphism with value $A$.  By step <1>7,
$$
\mcm_h\cong p_2^*\mcl;
$$
the possible normalization factor pulled back from $X$ is trivial because
$h$ is constant.

Using step <1>8 three times,
$$
\begin{aligned}
(f+g)^*\mcl
&=
\Gamma_{f+g}^*\mcm_h\\
&\cong
\Gamma_h^*\mcm_{f+g}\\
&\cong
\Gamma_h^*\mcm_f
\tensor
\Gamma_h^*\mcm_g\\
&\cong
\Gamma_f^*\mcm_h
\tensor
\Gamma_g^*\mcm_h\\
&=
f^*\mcl\tensor g^*\mcl.
\end{aligned}
$$
Under
$$
\alpha_X:X\overset\sim\longrightarrow\Pic^0(X),
$$
tensor product is addition.  Applying the definition of the dual from
step <1>1 to the last identity yields
$$
\widehat{f+g}(A)
=
\hat f(A)+\hat g(A).
$$
This holds for every $A\in X'$, so the two morphisms are equal.  This proves
the starred part (d).
:::

<1>10. For every $r\in\ZZ$,
$$
\boxed{\widehat{[r]_X}=[r]_X.}
$$

::: {.proof}
The identity morphism pulls every line bundle back to itself, so step <1>1 gives
$$
\widehat{[1]_X}=[1]_X.
$$
By step <1>9, dualization is additive on endomorphisms. Hence it sends zero to
zero, sends negatives to negatives, and sends the sum of $r$ copies of the
identity to the sum of $r$ copies of its dual. Therefore
$$
\widehat{[r]_X}=[r]_X
$$
for every integer $r$.
:::

<1>11. For every $r\in\ZZ$,
$$
\boxed{\deg [r]_X=r^2.}
$$

::: {.proof}
For $r=0$ this is the convention that a constant morphism has degree $0$.
Let $r\ne0$ and put
$$
d=\deg[r]_X.
$$
Applying step <1>6 to $[r]_X$ and using step <1>10 gives
$$
[d]_X
=
\widehat{[r]_X}\circ[r]_X
=
[r^2]_X.
$$
The standard embedding $\ZZ\to\Endo(X)$, $m\mapsto[m]_X$, is injective, so
$d=r^2$. This proves part (e).
:::

<1>12. For every morphism $f:X\to X'$,
$$
\boxed{\deg\hat f=\deg f.}
$$

::: {.proof}
If $f$ is constant, step <1>1 shows that $\hat f$ is the zero morphism, so
both degrees are $0$. Suppose that $f$ is nonconstant and put
$$
n=\deg f>0.
$$
Step <1>6 gives
$$
f\circ\hat f=[n]_{X'}.
$$
Degrees of finite morphisms of curves multiply under composition. Hence step
<1>11 gives
$$
n^2
=
\deg[n]_{X'}
=
\deg(f\circ\hat f)
=
n\deg\hat f.
$$
Since $n>0$, we obtain
$$
\deg\hat f=n=\deg f.
$$
This proves part (f).
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove parts (a)--(b), steps <1>3--<1>6 prove part (c),
steps <1>7--<1>9 prove part (d), steps <1>10--<1>11 prove part (e), and
step <1>12 proves part (f).
:::
:::
