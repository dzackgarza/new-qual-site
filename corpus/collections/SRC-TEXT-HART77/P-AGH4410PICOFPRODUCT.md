---
schema: qual/card@1
id: P-AGH4410PICOFPRODUCT
kind: problem
title: $\Pic(X \times X)$ is an extension of $\operatorname{End}(X, P_0)$ by the pullbacks of $\Pic X$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.10 together with the relative Picard/Jacobian
    construction and graph-line-bundle representative used in IV.4.7.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $X$ is an elliptic curve, show that there is an exact sequence
$$
0 \to p_1^* \Pic X \oplus p_2^* \Pic X \to \Pic(X \times X) \to R \to 0,
$$
where $R=\operatorname{End}(X, P_0)$.
In particular, we see that $\Pic(X \times X)$ is bigger than the sum of the Picard groups of the factors.
Cf.
(III, Ex.
12.6), (V, Ex.
1.6).
:::

::: {.solution}
Write $O=P_0$, and let
$$
p_1,p_2:X\times X\longrightarrow X
$$
be the projections.
We regard $R=\Endo(X,O)$ as an additive group.

::: pf

::: {.pf-step #s1}

The map
$$
\Pic X\oplus\Pic X
\longrightarrow
\Pic(X\times X),
\qquad
(\mca,\mcb)\longmapsto p_1^*\mca\tensor p_2^*\mcb
$$
is injective.

::: pf-proof

Suppose
$$
p_1^*\mca\tensor p_2^*\mcb\cong\OO_{X\times X}.
$$
Restricting to $X\times\{O\}$ gives $\mca\cong\OO_X$, because the second factor restricts to a constant one-dimensional vector space tensored with $\OO_X$.
Restricting to $\{O\}\times X$ then gives $\mcb\cong\OO_X$.
Thus the kernel is zero.

:::

:::

::: {.pf-step #s2}

Every line bundle $\mcl$ on $X\times X$ canonically determines an endomorphism $q(\mcl)\in\Endo(X,O)$.

::: pf-proof

Let
$$
i_2:X\longrightarrow X\times X,
\qquad
y\longmapsto(O,y),
$$
and put
$$
\mcm=i_2^*\mcl,
\qquad
\mcl^0=\mcl\tensor p_2^*\mcm^{-1}.
$$
Then $i_2^*\mcl^0\cong\OO_X$.

The degree of the restriction of a line bundle to the fibres of $p_1:X\times X\to X$ is constant on the connected base $X$.
Indeed, $\mcl^0$ is flat over $X$, and Theorem III.9.9 says that a flat projective family has constant Hilbert polynomial.
For an ample invertible sheaf $\mch$ on the second factor, Riemann--Roch on the genus-one fibre gives
$$
\chi(\mcl^0_x\tensor\mch^{\tensor n})
=
\deg\mcl^0_x+n\deg\mch,
$$
so constancy of the Hilbert polynomial forces $\deg\mcl^0_x$ to be constant.
Since the fibre over $O$ is trivial for $\mcl^0$, every fibre restriction has degree zero.
The relative Picard construction therefore gives a morphism
$$
\phi_{\mcl}:X\longrightarrow\Pic^0(X),
\qquad
x\longmapsto
\left[\mcl^0|_{\{x\}\times X}\right].
$$
It sends $O$ to the identity.
Under
$$
\alpha_X:X\overset\sim\longrightarrow\Pic^0(X),
\qquad
P\longmapsto\OO_X(P-O),
$$
define
$$
q(\mcl)=\alpha_X^{-1}\circ\phi_{\mcl}:X\longrightarrow X.
$$
This morphism sends $O$ to $O$, hence is an endomorphism of the elliptic curve.

:::

:::

::: {.pf-step #s3}

The assignment
$$
q:\Pic(X\times X)\longrightarrow R
$$
is a homomorphism, and every bundle of the form
$$
p_1^*\mca\tensor p_2^*\mcb
$$
lies in its kernel.

::: pf-proof

For line bundles $\mcl,\mcn$, normalization commutes with tensor product, and on every fibre of $p_1$,
$$
(\mcl\tensor\mcn)^0_x
\cong
\mcl^0_x\tensor\mcn^0_x.
$$
Tensor product in $\Pic^0(X)$ corresponds under $\alpha_X$ to addition on $X$.
Hence
$$
q(\mcl\tensor\mcn)=q(\mcl)+q(\mcn).
$$

If $\mcl=p_1^*\mca\tensor p_2^*\mcb$, then normalization by the fibre over $O$ removes the $p_2^*\mcb$ factor, up to a trivial constant factor.
The restriction of $p_1^*\mca$ to every fibre $\{x\}\times X$ is trivial.
Therefore $q(\mcl)=0$.

:::

:::

::: {.pf-step #s4}

Conversely,
$$
\ker q
=
p_1^*\Pic X\oplus p_2^*\Pic X.
$$

::: pf-proof

Let $q(\mcl)=0$, and use the notation $\mcm$ and $\mcl^0$ from step [](#s2){.pf-ref}. Then
$$
\left[\mcl^0|_{\{x\}\times X}\right]=0
\qquad
\text{in }\Pic^0(X)
$$
for every $x\in X$.
Thus $\mcl^0$ represents the zero element of the relative Picard group for $p_1:X\times X\to X$.

By the defining quotient in the relative Picard functor, a line bundle representing the zero relative class is pulled back from the base.
Hence there is $\mcn\in\Pic X$ such that
$$
\mcl^0\cong p_1^*\mcn.
$$
Undoing the normalization gives
$$
\mcl
\cong
p_1^*\mcn\tensor p_2^*\mcm.
$$
Step [](#s3){.pf-ref} gives the reverse inclusion, proving the equality.

:::

:::

::: {.pf-step #s5}

The homomorphism $q$ is surjective.

::: pf-proof

Let $f\in\Endo(X,O)$.
In the proof of [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(d)]], the normalized relative Picard bundle
$$
\mcm_f
=
\OO_{X\times X}\bigl(\Gamma_f-X\times\{O\}\bigr)
\tensor
p_1^*f^*\OO_X(O)^{-1}
$$
was constructed.
Its restriction to the fibre $\{x\}\times X$ is
$$
\OO_X(f(x)-O).
$$
Therefore the morphism to $\Pic^0(X)$ associated to $\mcm_f$ is precisely
$$
x\longmapsto\OO_X(f(x)-O)=\alpha_X(f(x)).
$$
By the definition of $q$ in step [](#s2){.pf-ref},
$$
q(\mcm_f)=f.
$$
Thus every element of $R$ is in the image.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives injectivity on the left, steps [](#s3){.pf-ref} and [](#s4){.pf-ref} identify the kernel of $q$ with the two pullback Picard groups, and step [](#s5){.pf-ref} proves surjectivity.
Hence
$$
0
\longrightarrow
p_1^*\Pic X\oplus p_2^*\Pic X
\longrightarrow
\Pic(X\times X)
\xrightarrow{q}
\Endo(X,O)
\longrightarrow
0
$$
is exact.
Since $R$ contains the nonzero identity endomorphism, the quotient of $\Pic(X\times X)$ by the two pullback Picard groups is nonzero.
Thus the pullback subgroup is proper, which is the stated final consequence.

:::

:::

:::
