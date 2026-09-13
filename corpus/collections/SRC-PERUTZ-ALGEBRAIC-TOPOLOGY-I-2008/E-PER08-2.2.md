---
schema: qual/card@1
id: E-PER08-2.2
kind: problem
title: Polar decomposition and the topology of SL_2(C)
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 2.2 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the SU(2)-sphere parametrization, determinant-one positive-Hermitian coordinates, and continuity of the polar inverse via the explicit 2-by-2 square-root formula.
---

::: {.problem}
Assume that every matrix $A\in\operatorname{SL}_2(\mathbb C)$ can be written uniquely as a product $UP$, with $U\in\operatorname{SU}(2)$ and $P$ positive-definite Hermitian.

Deduce a homeomorphism
\[
S^3\times(0,\infty)\times\mathbb C\longrightarrow \operatorname{SL}_2(\mathbb C).
\]
:::

::: {.solution}
We identify separately the unitary factor and the positive-Hermitian factor.

<1>1. There is a homeomorphism $S^3\cong\operatorname{SU}(2)$.
::: {.proof}
Regard
\[
S^3=\{(\alpha,\beta)\in\mathbb C^2:|\alpha|^2+|\beta|^2=1\}.
\]
Define
\[
\Theta(\alpha,\beta)=
\begin{pmatrix}
\alpha&\beta\\
-\overline\beta&\overline\alpha
\end{pmatrix}.
\]
The columns are orthonormal and
\[
\det\Theta(\alpha,\beta)=|\alpha|^2+|\beta|^2=1,
\]
so $\Theta(\alpha,\beta)\in\operatorname{SU}(2)$.

Conversely, if
\[
U=\begin{pmatrix}u_{11}&u_{12}\\u_{21}&u_{22}\end{pmatrix}\in\operatorname{SU}(2),
\]
then the second row is forced by unitarity and determinant one to be
\[
(-\overline{u_{12}},\overline{u_{11}}).
\]
Thus $U=\Theta(u_{11},u_{12})$, with
\[
|u_{11}|^2+|u_{12}|^2=1.
\]
Hence $\Theta$ is bijective. Both $\Theta$ and its inverse, obtained by taking the first row, are continuous, so $\Theta$ is a homeomorphism.
:::

<1>2. The positive-definite Hermitian matrices of determinant one are homeomorphic to $(0,\infty)\times\mathbb C$.
::: {.proof}
A Hermitian matrix has the form
\[
P=\begin{pmatrix}r&z\\\overline z&s\end{pmatrix},
\qquad r,s\in\mathbb R,\ z\in\mathbb C.
\]
If $P$ is positive definite, then $r>0$. The condition $\det P=1$ gives
\[
rs-|z|^2=1,
\]
so necessarily
\[
s=\frac{1+|z|^2}{r}.
\]
Therefore every such $P$ is uniquely of the form
\[
P(r,z)=
\begin{pmatrix}
r&z\\[1mm]
\overline z&\dfrac{1+|z|^2}{r}
\end{pmatrix},
\qquad r>0,\ z\in\mathbb C.
\]
Conversely, $P(r,z)$ has positive upper-left entry and determinant $1>0$, so Sylvester's criterion makes it positive definite.

Thus
\[
\Psi:(0,\infty)\times\mathbb C\to\mathcal P,
\qquad
(r,z)\mapsto P(r,z),
\]
where $\mathcal P$ denotes the positive-definite Hermitian determinant-one matrices, is bijective. It is continuous, and its inverse is
\[
P\longmapsto(P_{11},P_{12}),
\]
which is continuous. Hence $\Psi$ is a homeomorphism.
:::

<1>3. Polar multiplication is a homeomorphism
\[
\operatorname{SU}(2)\times\mathcal P
\xrightarrow{\cong}
\operatorname{SL}_2(\mathbb C).
\]
::: {.proof}
Define
\[
\Phi(U,P)=UP.
\]
It is continuous. By the assumed polar decomposition, $\Phi$ is bijective. It remains to verify that the inverse factors depend continuously on $A$.

Let
\[
H=A^*A.
\]
Then $H$ is positive-definite Hermitian and
\[
\det H=|\det A|^2=1.
\]
By Cayley--Hamilton,
\[
H^2-(\operatorname{tr}H)H+I=0.
\]
Hence
\[
(H+I)^2
=H^2+2H+I
=(\operatorname{tr}H+2)H.
\]
Since $H$ is positive definite, $\operatorname{tr}H+2>0$, and therefore
\[
P=H^{1/2}
=\frac{H+I}{\sqrt{\operatorname{tr}H+2}}.
\]
This formula is continuous in $A$. Then
\[
U=AP^{-1}
\]
is also continuous in $A$, since inversion is continuous on invertible matrices.

Thus
\[
A\longmapsto(U,P)
\]
is continuous, so $\Phi$ is a homeomorphism.
:::

<1>4. Compose the three homeomorphisms.
::: {.proof}
By <1>1, <1>2, and <1>3, the map
\[
S^3\times(0,\infty)\times\mathbb C
\longrightarrow
\operatorname{SL}_2(\mathbb C)
\]
defined by
\[
((\alpha,\beta),r,z)
\longmapsto
\Theta(\alpha,\beta)P(r,z)
\]
is a composition of homeomorphisms. Therefore it is a homeomorphism, as required.
:::
:::
