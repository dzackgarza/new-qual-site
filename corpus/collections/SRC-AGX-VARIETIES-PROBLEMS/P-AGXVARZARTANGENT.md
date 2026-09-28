---
schema: qual/card@1
id: P-AGXVARZARTANGENT
kind: problem
title: The tangent space as the dual of $\mfm_p/\mfm_p^2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tangent Spaces
  - Local Rings
  - Cotangent Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Definitions 6.1 and the third clause of Exercises 6.2 in
    the recorded source. Over k=C it asks for the canonical identification
    T_pX = (m_p/m_p^2)^* for the local ring O(X,p).
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the affine-variety and complex-ground-field hypotheses explicit.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Identified the Jacobian-kernel tangent space with k-derivations of the
    local ring into the residue field, then proved directly that such
    derivations are the dual of m_p/m_p^2.
---

::: {.problem}
Let $X$ be an affine variety over $\CC$, let $p\in X$, and let
$$
\mco_{X,p}
$$
be the local ring with maximal ideal $\mfm_p$. Show canonically that
$$
T_pX
\cong
(\mfm_p/\mfm_p^2)\dual.
$$
:::

::: {.solution}
Put
$$
\mco=\mco_{X,p},
\qquad
\mfm=\mfm_p.
$$
Since $p$ is a complex point,
$$
\mco/\mfm\cong\CC.
$$
We regard $\CC$ as an $\mco$-module through evaluation at $p$.

<1>1. Every $\CC$-derivation
$$
D:\mco\longrightarrow\CC
$$
annihilates $\mfm^2$.

::: {.proof}
Let
$$
a,b\in\mfm.
$$
Their residues at $p$ are zero. The Leibniz rule for a derivation into the
residue-field module gives
$$
D(ab)
=
a(p)D(b)+b(p)D(a)
=
0.
$$
Thus $D$ vanishes on every product of two elements of $\mfm$, hence on the
ideal $\mfm^2$.
:::

<1>2. Restriction induces a linear map
$$
\Phi:
\Der_\CC(\mco,\CC)
\longrightarrow
\Hom_\CC(\mfm/\mfm^2,\CC).
$$

::: {.proof}
For a derivation $D$, define
$$
\Phi(D)([a])=D(a),
\qquad
a\in\mfm.
$$
Step <1>1 shows that this depends only on the class of $a$ modulo
$\mfm^2$. Additivity and $\CC$-linearity of $D$ make $\Phi(D)$ a
$\CC$-linear functional.
:::

<1>3. Every linear functional
$$
\lambda:\mfm/\mfm^2\longrightarrow\CC
$$
determines a derivation
$$
D_\lambda:\mco\longrightarrow\CC
$$
by
$$
D_\lambda(a)
=
\lambda\bigl([a-a(p)]\bigr).
$$

::: {.proof}
For every $a\in\mco$, the difference
$$
a-a(p)
$$
lies in $\mfm$, so the displayed formula is defined.

It is visibly additive and $\CC$-linear. For $a,b\in\mco$,
$$
\begin{aligned}
ab-a(p)b(p)
&=
a(p)(b-b(p))
+
b(p)(a-a(p))\\
&\qquad
+
(a-a(p))(b-b(p)).
\end{aligned}
$$
The last term lies in $\mfm^2$, so applying $\lambda$ modulo $\mfm^2$ gives
$$
D_\lambda(ab)
=
a(p)D_\lambda(b)
+
b(p)D_\lambda(a).
$$
Thus $D_\lambda$ satisfies the Leibniz rule and is a derivation into the
residue field.
:::

<1>4. The maps of steps <1>2--<1>3 are inverse isomorphisms:
$$
\boxed{
\Der_\CC(\mco,\CC)
\cong
(\mfm/\mfm^2)\dual.
}
$$

::: {.proof}
Let $D$ be a derivation. Since derivations kill constants,
$$
D(a)=D(a-a(p)).
$$
Hence the derivation reconstructed from $\Phi(D)$ is $D$ itself.

Conversely, if $\lambda$ is a functional and $a\in\mfm$, then $a(p)=0$, so
$$
\Phi(D_\lambda)([a])
=
D_\lambda(a)
=
\lambda([a]).
$$
Thus both composites are identities.
:::

<1>5. The Zariski tangent space $T_pX$ is canonically
$$
\Der_\CC(\mco_{X,p},\CC).
$$

::: {.proof}
Embed
$$
X\subseteq\AA^n_\CC
$$
and write
$$
p=(a_1,\ldots,a_n).
$$
Choose generators
$$
I(X)=(f_1,\ldots,f_m).
$$

A derivation
$$
D:\mco_{X,p}\longrightarrow\CC
$$
is determined by the values
$$
v_j=D(x_j-a_j).
$$
For every relation $f_i=0$ in the coordinate ring, the chain rule for
polynomials gives
$$
0
=
D(f_i)
=
\sum_{j=1}^n
\frac{\partial f_i}{\partial x_j}(p)v_j.
$$
Thus
$$
v=(v_1,\ldots,v_n)
$$
lies in the kernel of the Jacobian matrix, which is $T_pX$ by definition.

Conversely, if
$$
v\in\ker J(p),
$$
the directional derivative
$$
h\longmapsto
\sum_{j=1}^n
v_j\frac{\partial h}{\partial x_j}(p)
$$
is a derivation on $\CC[x_1,\ldots,x_n]$ that annihilates $I(X)$, because
the chosen generators and therefore the whole ideal have zero directional
derivative at $p$. It descends to the coordinate ring and extends uniquely
to the localization $\mco_{X,p}$. Hence every tangent vector gives a unique
derivation.

These constructions are inverse and independent of the chosen generators,
so
$$
T_pX
\cong
\Der_\CC(\mco_{X,p},\CC).
$$
:::

<1>6. Therefore
$$
\boxed{
T_pX
\cong
(\mfm_p/\mfm_p^2)\dual.
}
$$

::: {.proof}
Step <1>5 identifies $T_pX$ with the derivation space, and step <1>4
identifies that derivation space with the dual of the cotangent space
$\mfm_p/\mfm_p^2$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required canonical isomorphism.
:::
:::
