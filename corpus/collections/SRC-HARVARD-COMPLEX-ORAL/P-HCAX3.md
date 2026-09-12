---
schema: qual/card@1
id: P-HCAX3
kind: problem
title: Mapping class group of the torus
classification:
  areas:
  - topology
  topics:
  - Mapping Class Groups
relations: []
review: draft
---

::: problem
Show that the orientation-preserving mapping class group of the torus is $\operatorname{SL}_2(\mathbb Z)$.
:::

::: solution
Write
\[
T^2=\mathbb R^2/\mathbb Z^2.
\]
Every orientation-preserving homeomorphism $f:T^2\to T^2$ induces an automorphism
\[
f_*:H_1(T^2;\mathbb Z)\longrightarrow H_1(T^2;\mathbb Z).
\]
Since
\[
H_1(T^2;\mathbb Z)\cong\mathbb Z^2,
\]
this gives a homomorphism
\[
\Phi:\operatorname{Mod}^+(T^2)
\longrightarrow GL_2(\mathbb Z).
\]
Preservation of orientation means preservation of the algebraic intersection form, whose matrix in the standard basis is
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
For a $2\times2$ integer matrix $A$ one has
\[
A^TJA=(\det A)J,
\]
so orientation preservation forces $\det A=1$. Hence $\Phi$ takes values in $SL_2(\mathbb Z)$.

The map is surjective. If
\[
A\in SL_2(\mathbb Z),
\]
then the linear map $x\mapsto Ax$ preserves $\mathbb Z^2$ and therefore descends to an orientation-preserving diffeomorphism
\[
f_A:T^2\to T^2
\]
whose action on $H_1$ is exactly $A$.

For injectivity, suppose an orientation-preserving homeomorphism $f$ acts trivially on $H_1(T^2;\mathbb Z)$. Since
\[
\pi_1(T^2)\cong\mathbb Z^2
\]
is already abelian, the induced map on $\pi_1$ is also the identity after the usual change of basepoint. The torus is a $K(\mathbb Z^2,1)$, so $f$ is homotopic to the identity. By the Baer theorem for closed oriented surfaces, homotopic orientation-preserving homeomorphisms are isotopic. Thus $f$ represents the identity mapping class.

Therefore $\Phi$ is an isomorphism:
\[
\boxed{
\operatorname{Mod}^+(T^2)\cong SL_2(\mathbb Z).}
\]
:::
