---
schema: qual/card@1
id: P-AGFS15-03
kind: problem
title: Finite subsets of quasi-projective varieties lie in affine opens
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the projective-closure argument, the finite-hyperplane avoidance step, and affineness of the resulting principal projective open.
---

::: {.problem}
Let $S$ be a finite set of points of a quasi-projective variety $X$.
Show that $S$ is contained in an affine open subset of $X$.
:::


::: {.solution}
Embed \(X\) as a locally closed subvariety of some projective space and let
\[
\overline X\subseteq\mathbf P^N
\]
be its projective closure. Since \(X\) is open in \(\overline X\), put
\[
Z:=\overline X\setminus X.
\]
We will find a homogeneous polynomial \(F\) which vanishes on \(Z\) and is nonzero at every point of \(S\). Then
\[
U:=\overline X\cap D_+(F)
\]
is the required affine open subset.

<1>1. There is a homogeneous polynomial \(F\) vanishing on \(Z\) and on no point of \(S\).
::: {.proof}
Write
\[
S=\{p_1,\dots,p_r\}.
\]
For every \(i\), the point \(p_i\) does not lie in \(Z\). Hence the homogeneous ideal \(I(Z)\) is not contained in the homogeneous maximal ideal of \(p_i\). Therefore there is a homogeneous polynomial
\[
f_i\in I(Z)
\]
with \(f_i(p_i)\ne0\).

Choose a degree \(d\) at least as large as all \(\deg f_i\). For each \(i\), choose a linear form \(\ell_i\) with \(\ell_i(p_i)\ne0\), and replace \(f_i\) by
\[
g_i=f_i\ell_i^{\,d-\deg f_i}\in I(Z)_d.
\]
Then \(g_i(p_i)\ne0\). Thus, for each \(i\), the condition
\[
F(p_i)=0
\]
defines a proper linear subspace of the finite-dimensional vector space \(I(Z)_d\).

Because \(k\) is algebraically closed, it is infinite. A finite union of proper linear subspaces of a finite-dimensional vector space over an infinite field cannot equal the whole space. Hence we may choose
\[
F\in I(Z)_d
\]
outside all these evaluation kernels. Then \(F|_Z=0\) and \(F(p_i)\ne0\) for every \(i\).
:::

<1>2. The principal open \(U=\overline X\cap D_+(F)\) is affine, lies in \(X\), and contains \(S\).
::: {.proof}
Let \(A\) be the homogeneous coordinate ring of \(\overline X\), so that
\[
\overline X=\operatorname{Proj}A.
\]
The standard principal open determined by \(F\) is
\[
D_+(F)=\operatorname{Spec}(A_F)_0,
\]
so \(U=\overline X\cap D_+(F)\) is affine.

Since \(F\) vanishes on \(Z\), no point of \(Z\) belongs to \(D_+(F)\). Hence
\[
U\subseteq\overline X\setminus Z=X.
\]
On the other hand, \(F(p_i)\ne0\) for every \(p_i\in S\), so
\[
S\subseteq U.
\]
Thus \(U\) is an affine open subset of \(X\) containing \(S\).
:::
:::
