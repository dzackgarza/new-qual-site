---
schema: qual/card@1
id: P-AGAFFINETEST
kind: problem
title: Recognising an affine scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Serre Criterion
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Ogus's question immediately preceding the Serre-affineness follow-ups.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
How can you tell if a scheme is affine?
:::

::: {.solution}
There are three standard answers, depending on what information about the scheme is available.

<1>1. The intrinsic recognition map is
\[
\eta_X:X\longrightarrow\operatorname{Spec}\Gamma(X,\mathcal O_X).
\]
Then
\[
\boxed{
X\text{ is affine}
\iff
\eta_X\text{ is an isomorphism}.
}
\]
::: {.proof}
For every scheme $X$ and ring $A$ there is a natural bijection
\[
\operatorname{Hom}_{\mathrm{Sch}}(X,\operatorname{Spec}A)
\cong
\operatorname{Hom}_{\mathrm{Ring}}(A,\Gamma(X,\mathcal O_X)).
\]
Taking $A=\Gamma(X,\mathcal O_X)$ and the identity ring map produces the canonical morphism $\eta_X$.

If $X=\operatorname{Spec}B$ is affine, then
\[
\Gamma(X,\mathcal O_X)=B,
\]
and $\eta_X$ is the identity after this identification.  Conversely, if $\eta_X$ is an isomorphism, then $X$ is isomorphic to the spectrum of a ring and hence is affine.
:::

<1>2. For a Noetherian scheme, Serre's cohomological criterion says
\[
\boxed{
X\text{ affine}
\iff
H^i(X,\mathcal F)=0
\text{ for every quasicoherent }\mathcal F\text{ and every }i>0.
}
\]
It is enough to test
\[
\boxed{
H^1(X,\mathcal I)=0
}
\]
for every coherent ideal sheaf $\mathcal I\subseteq\mathcal O_X$.
::: {.proof}
This is Serre's criterion for affineness.  The forward direction is affine vanishing for quasicoherent sheaves.  The converse is the criterion proper; in the ideal-sheaf form it produces enough global functions to cover $X$ by affine global-principal opens and then shows those functions generate the unit ideal.
:::

<1>3. A concrete version of the same argument is the following.  Suppose $X$ is Noetherian and there are global functions
\[
f_1,\ldots,f_r\in A:=\Gamma(X,\mathcal O_X)
\]
such that
\[
\sum_i a_if_i=1
\]
for some $a_i\in A$ and every open
\[
X_{f_i}=\{x\in X:(f_i)_x\in\mathcal O_{X,x}^{\times}\}
\]
is affine.  Then $X$ is affine.
::: {.proof}
The equation $\sum_i a_if_i=1$ implies that the $X_{f_i}$ cover $X$.

Because $X$ is Noetherian, it is quasicompact and quasiseparated, so restriction gives
\[
\Gamma(X,\mathcal O_X)_{f_i}
\cong
\Gamma(X_{f_i},\mathcal O_X).
\]
Hence the canonical map
\[
\eta_X:X\longrightarrow\operatorname{Spec}A
\]
restricts to an isomorphism
\[
X_{f_i}\xrightarrow{\sim}D(f_i).
\]
The equation $\sum_i a_if_i=1$ also says that the distinguished opens $D(f_i)$ cover $\operatorname{Spec}A$.  Thus $\eta_X$ is an isomorphism on open covers of source and target, hence globally.  Apply <1>1.
:::

<1>4. These criteria distinguish affineness from merely having many global functions.
::: {.proof}
For example,
\[
\Gamma(\mathbb P^1_k,\mathcal O)=k,
\]
so the canonical map in <1>1 is
\[
\mathbb P^1_k\longrightarrow\operatorname{Spec}k,
\]
which is not an isomorphism.  Thus $\mathbb P^1$ is not affine.

Likewise, having a ring of global functions that happens to be an affine coordinate ring is not enough: the comparison morphism itself must recover the scheme.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>1 is the formal recognition criterion, step <1>2 is Serre's cohomological criterion, and step <1>3 is the global-principal version used in its proof.
:::
:::
