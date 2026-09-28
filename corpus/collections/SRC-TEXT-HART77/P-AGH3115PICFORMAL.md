---
schema: qual/card@1
id: P-AGH3115PICFORMAL
kind: problem
title: The Picard group of a formal completion along a hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Formal Schemes
  - Picard Group
  - Lefschetz Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.5 together with the three exercises named in its
    hint: II.9.6, III.4.6, and III.5.5. The proof identifies the square-zero
    kernel between successive infinitesimal neighbourhoods as O_Y(-nd), uses
    the complete-intersection vanishing in degrees 1 and 2 to make every
    Picard transition an isomorphism, and then applies the formal Picard
    inverse-limit theorem. The kernel identification and Picard exact sequence
    were cross-checked against Stacks Project Tag 0C6R.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a hypersurface in $X = \PP_k^N$ with $N \geq 4$.
Let $\hat{X}$ be the formal completion of $X$ along $Y$ (II, §9). Prove that the natural map
\[
\Pic \hat{X} \to \Pic Y
\]
is an isomorphism.

Hint: use (II, Ex.
9.6), and then study the maps $\Pic X_{n+1} \to \Pic X_n$ for each $n$ using (Ex.
4.6) and (Ex.
5.5).
:::

::: {.solution}
Let
$$
d=\deg Y
$$
and let
$$
\mci=\mci_Y\subseteq\mco_X
$$
be the ideal sheaf of $Y$. Since $Y$ is a hypersurface of degree $d$,
$$
\mci\cong\mco_X(-d).
$$
For $n\ge1$, put
$$
X_n=\bigl(Y,\mco_X/\mci^n\bigr).
$$
Thus $X_1=Y$, and the formal completion $\hat X$ is the inverse system of the
infinitesimal neighbourhoods $X_n$.

<1>1. The formal Picard group is the inverse limit
$$
\Pic\hat X\cong\varprojlim_n\Pic X_n.
$$

::: {.proof}
Each $X_n$ is the closed subscheme of the projective scheme $X=\PP_k^N$
defined by $\mci^n$, hence is projective over the common field $k$.
Therefore the Mittag--Leffler hypothesis in
[[P-AGH296PICFORMAL|Exercise II.9.6(d)]] holds for the inverse system
$$
\Gamma(X_n,\mco_{X_n}).
$$
Exercise II.9.6 then gives the canonical isomorphism
$$
\boxed{\Pic\hat X\cong\varprojlim_n\Pic X_n}.
$$
Under this isomorphism, restriction to $Y=X_1$ is the projection to the first
factor.
:::

<1>2. For every $n\ge1$, the closed immersion
$$
X_n\hookrightarrow X_{n+1}
$$
is a square-zero thickening with ideal
$$
\mci^n/\mci^{n+1}\cong\mco_Y(-nd).
$$

::: {.proof}
Its ideal in
$$
\mco_{X_{n+1}}=\mco_X/\mci^{n+1}
$$
is
$$
\mci^n/\mci^{n+1}.
$$
Its square is zero because
$$
\mci^{2n}\subseteq\mci^{n+1}
$$
for $n\ge1$.

Moreover multiplication by $\mci$ annihilates
$\mci^n/\mci^{n+1}$, so this ideal is naturally an $\mco_Y$-module. Since
$\mci$ is invertible,
$$
\mci^n/\mci^{n+1}
\cong
\mci^n\otimes_{\mco_X}\mco_Y.
$$
Using
$$
\mci^n\cong\mco_X(-nd)
$$
and restricting to $Y$ gives
$$
\boxed{\mci^n/\mci^{n+1}\cong\mco_Y(-nd)}.
$$
:::

<1>3. For every $n\ge1$,
$$
H^1\bigl(Y,\mco_Y(-nd)\bigr)
=
H^2\bigl(Y,\mco_Y(-nd)\bigr)
=0.
$$

::: {.proof}
The hypersurface $Y\subseteq\PP_k^N$ is a complete intersection of dimension
$$
\dim Y=N-1\ge3.
$$
By [[P-AGH355COMPINT|Exercise III.5.5(c)]],
$$
H^i(Y,\mco_Y(m))=0
$$
for every $m\in\ZZ$ and every
$$
0<i<\dim Y.
$$
Taking $m=-nd$, the values $i=1,2$ both lie in this range because
$\dim Y\ge3$. This proves the two vanishings.
:::

<1>4. For every $n\ge1$, restriction induces an isomorphism
$$
\Pic X_{n+1}\xrightarrow{\sim}\Pic X_n.
$$

::: {.proof}
Apply
[[P-AGH346SQUAREZEROPIC|Exercise III.4.6]]
to the square-zero thickening of step <1>2. The relevant part of its exact
sequence is
$$
H^1\bigl(Y,\mci^n/\mci^{n+1}\bigr)
\longrightarrow
\Pic X_{n+1}
\longrightarrow
\Pic X_n
\longrightarrow
H^2\bigl(Y,\mci^n/\mci^{n+1}\bigr).
$$
By steps <1>2--<1>3, both outer groups are zero. Hence the middle restriction
map is both injective and surjective:
$$
\boxed{\Pic X_{n+1}\xrightarrow{\sim}\Pic X_n}.
$$
Equivalently, every line bundle on $X_n$ has a unique isomorphism class of
lift to $X_{n+1}$.
:::

<1>5. Projection to the first term induces an isomorphism
$$
\varprojlim_n\Pic X_n\xrightarrow{\sim}\Pic Y.
$$

::: {.proof}
By step <1>4 every transition map in the inverse system
$$
\cdots\longrightarrow\Pic X_3
\longrightarrow\Pic X_2
\longrightarrow\Pic X_1
$$
is an isomorphism. Therefore a compatible sequence of classes is uniquely
determined by its first term, and every class in
$$
\Pic X_1=\Pic Y
$$
extends uniquely through all the inverse transitions. Hence the first
projection is an isomorphism.
:::

<1>6. Q.E.D.

::: {.proof}
Combining steps <1>1 and <1>5 gives
$$
\Pic\hat X
\xrightarrow{\sim}
\varprojlim_n\Pic X_n
\xrightarrow{\sim}
\Pic X_1
=
\Pic Y.
$$
The composite is precisely the natural restriction map in the statement.
Thus
$$
\boxed{\Pic\hat X\xrightarrow{\sim}\Pic Y}.
$$
:::
:::
