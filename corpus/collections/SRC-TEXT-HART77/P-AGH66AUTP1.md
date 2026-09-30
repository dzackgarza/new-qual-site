---
schema: qual/card@1
id: P-AGH66AUTP1
kind: problem
title: $\Aut \PP^1$ is the group of fractional linear transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Automorphisms
  - Function Fields
  - Projective Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.6.6 and Corollary I.6.12 in the Hartshorne source. The proof identifies curve automorphisms with function-field automorphisms through the category equivalence and reduces an automorphism fixing infinity to an automorphism of k[x], hence to an affine linear map.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Think of $\PP^1$ as $\AA^1 \union \theset{\infty}$.
Define a *fractional linear transformation* of $\PP^1$ by sending
$$
x \mapsto \frac{ax + b}{cx + d}, \qquad a,b,c,d \in k, \quad ad - bc \neq 0.
$$

(a) Show that a fractional linear transformation induces an automorphism of $\PP^1$, that is, an isomorphism of $\PP^1$ with itself.
   Denote the group of all these fractional linear transformations by $\PGL(1)$.

(b) Let $\Aut \PP^1$ denote the group of all automorphisms of $\PP^1$.
   Show that $\Aut \PP^1 \cong \Aut k(x)$, the group of $k$-automorphisms of the field $k(x)$.

(c) Show that every automorphism of $k(x)$ is a fractional linear transformation, and deduce that $\PGL(1) \to \Aut \PP^1$ is an isomorphism.

Note: a similar result holds for $\PP^n$ (II, 7.1.1): every automorphism is given by a linear transformation of the homogeneous coordinates.
:::

::: {.solution}
Use homogeneous coordinates $[X:Z]$ on $\PP^1$, with affine coordinate $x=X/Z$ on $Z\ne0$ and $\infty=[1:0]$.

::: pf

::: {.pf-step #matrix-gives-automorphism}
Every matrix
$$
M=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in\operatorname{GL}_2(k)
$$
defines an automorphism
$$
T_M([X:Z])=[aX+bZ:cX+dZ]
$$
of $\PP^1$.

::: pf-proof
The two homogeneous linear forms $aX+bZ$ and $cX+dZ$ have no common nonzero zero because $M$ is invertible.
Hence they define a morphism $T_M:\PP^1\to\PP^1$.
The inverse matrix $M^{-1}$ gives a morphism $T_{M^{-1}}$ satisfying
$$
T_{M^{-1}}T_M=T_MT_{M^{-1}}=\operatorname{id}_{\PP^1}.
$$
Thus $T_M$ is an automorphism.
On the affine chart it sends
$$
x\longmapsto\frac{ax+b}{cx+d},
$$
with the usual value $\infty$ when the denominator vanishes.

Multiplying $M$ by a nonzero scalar does not change $T_M$, and two matrices inducing the same projective transformation differ by such a scalar.
Thus these transformations form the projective linear group $\operatorname{PGL}_2(k)$, denoted $\PGL(1)$ in the source.
This proves part (a).
:::

:::

::: {.pf-step #aut-p1-iso-aut-kx}
Pullback of rational functions gives an isomorphism
$$
\Aut(\PP^1)\xrightarrow{\cong}\Aut_k k(x).
$$

::: pf-proof
An automorphism $\phi:\PP^1\to\PP^1$ induces the $k$-automorphism
$$
\phi^*:K(\PP^1)=k(x)\longrightarrow k(x),
\qquad h\longmapsto h\circ\phi.
$$
Composition of maps reverses under pullback, so if one uses ordinary composition on both groups the assignment $\phi\mapsto(\phi^{-1})^*$ is a group homomorphism.

Corollary I.6.12 identifies nonsingular projective curves with their function fields contravariantly: every $k$-homomorphism of function fields is induced by a unique dominant morphism of the corresponding nonsingular projective curves.
Apply this with both fields equal to $k(x)$.
An automorphism of $k(x)$ therefore induces a unique dominant morphism $\psi:\PP^1\to\PP^1$, and its inverse field automorphism induces a morphism inverse to $\psi$ by uniqueness in the category equivalence.
Hence $\psi$ is an automorphism.

Thus the pullback construction is bijective, and after the harmless inverse convention just noted it is an isomorphism of groups.
This proves part (b).
:::

:::

::: {.pf-step #fixing-infinity-is-affine}
Every automorphism of $\PP^1$ fixing $\infty$ has the affine form $x\mapsto ax+b$ with $a\ne0$.

::: pf-proof
Let $\phi\in\Aut(\PP^1)$ satisfy $\phi(\infty)=\infty$.
Then
$$
\phi(\AA^1)=\phi(\PP^1\setminus\{\infty\})
=\PP^1\setminus\{\infty\}=\AA^1,
$$
so $\phi$ restricts to an automorphism of the affine line.
On coordinate rings this gives a $k$-algebra automorphism
$$
k[x]\longrightarrow k[x].
$$
If $p(x)$ is the image of $x$, surjectivity provides $q(x)$ with $q(p(x))=x$.
For nonconstant polynomials degrees multiply under composition, so
$$
1=\deg x=\deg(q\circ p)=(\deg q)(\deg p).
$$
Hence $\deg p=1$ and
$$
p(x)=ax+b,\qquad a\in k^\times,\ b\in k.
$$
Therefore $\phi$ is the fractional linear transformation represented by
$\begin{pmatrix}a&b\\0&1\end{pmatrix}$.
:::

:::

::: {.pf-step #every-automorphism-fractional-linear}
Every automorphism of $\PP^1$ is fractional linear.

::: pf-proof
Let $\phi\in\Aut(\PP^1)$ and put $P=\phi(\infty)$.
By step [](#matrix-gives-automorphism){.pf-ref} there is a fractional linear transformation $T$ with $T(P)=\infty$.
Then $T\circ\phi$ fixes $\infty$, so step [](#fixing-infinity-is-affine){.pf-ref} shows that $T\circ\phi$ is fractional linear.
Since $T^{-1}$ is fractional linear as well, so is
$$
\phi=T^{-1}\circ(T\circ\phi).
$$
Thus every automorphism of $\PP^1$ lies in $\PGL(1)$.
:::

:::

::: {.pf-step #field-automorphism-fractional-linear}
Every $k$-automorphism of $k(x)$ is fractional linear, and
$$
\boxed{\PGL(1)\cong\Aut(\PP^1)\cong\Aut_k k(x)}.
$$

::: pf-proof
By step [](#aut-p1-iso-aut-kx){.pf-ref}, a field automorphism corresponds to a unique automorphism of $\PP^1$.
Step [](#every-automorphism-fractional-linear){.pf-ref} makes that curve automorphism fractional linear, so its action on the affine coordinate is
$$
x\longmapsto\frac{ax+b}{cx+d},
\qquad ad-bc\ne0.
$$
Conversely step [](#matrix-gives-automorphism){.pf-ref} shows that every such formula is induced by an automorphism of $\PP^1$ and therefore of $k(x)$.
This proves part (c) and both asserted isomorphisms.
:::

:::

::: pf-qed
Step [](#matrix-gives-automorphism){.pf-ref} proves part (a), step [](#aut-p1-iso-aut-kx){.pf-ref} proves part (b), and steps [](#fixing-infinity-is-affine){.pf-ref}, [](#every-automorphism-fractional-linear){.pf-ref} and [](#field-automorphism-fractional-linear){.pf-ref} prove part (c).
:::

:::
:::
