---
schema: qual/card@1
id: P-AGGEOMGENUS
kind: problem
title: Geometric genus, and what it becomes for a singular curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Singularities
  - Normalization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Poonen's question on geometric genus and singular curves.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Define the geometric genus.

What might the geometric genus of a singular curve be?
:::

::: {.solution}
Let $C$ be an integral projective curve over an algebraically closed field, and let
\[
\nu:\widetilde C\longrightarrow C
\]
be its normalization.

<1>1. The geometric genus of $C$ is
\[
\boxed{
p_g(C)
=g(\widetilde C)
=h^1(\widetilde C,\mathcal O_{\widetilde C})
=h^0(\widetilde C,\omega_{\widetilde C}).
}
\]
::: {.proof}
The normalization $\widetilde C$ is a normal one-dimensional Noetherian scheme, hence regular, and over an algebraically closed field it is smooth.  Thus it has the ordinary genus of a smooth projective curve.  The geometric genus of $C$ is defined to be that genus.

For the smooth projective curve $\widetilde C$, Serre duality identifies
\[
H^1(\widetilde C,\mathcal O_{\widetilde C})^\vee
\cong
H^0(\widetilde C,\omega_{\widetilde C}),
\]
giving the last equality of dimensions.
:::

<1>2. The normalization exact sequence is
\[
0\longrightarrow\mathcal O_C
\longrightarrow\nu_*\mathcal O_{\widetilde C}
\longrightarrow\mathcal Q
\longrightarrow0,
\]
where $\mathcal Q$ is a finite-length sheaf supported at the singular points.
::: {.proof}
Because $C$ is integral, the normalization map induces an injection
\[
\mathcal O_C\hookrightarrow\nu_*\mathcal O_{\widetilde C}.
\]
It is an isomorphism over the normal locus.  For a curve, every regular point is normal, so the cokernel is supported only at the finitely many singular points; hence it has finite length.
:::

<1>3. For each singular point $p$, define
\[
\delta_p
=\length_{\mathcal O_{C,p}}
\left(
(\nu_*\mathcal O_{\widetilde C}/\mathcal O_C)_p
\right).
\]
Then
\[
\boxed{
p_a(C)-p_g(C)=\sum_{p\in\operatorname{Sing}C}\delta_p.
}
\]
::: {.proof}
Take Euler characteristics in the exact sequence of <1>2.  Since $\nu$ is finite,
\[
H^i(C,\nu_*\mathcal O_{\widetilde C})
\cong
H^i(\widetilde C,\mathcal O_{\widetilde C}),
\]
and since $\mathcal Q$ has finite support,
\[
\chi(\mathcal Q)=h^0(\mathcal Q)=\sum_p\delta_p.
\]
Thus
\[
\chi(\mathcal O_{\widetilde C})
=\chi(\mathcal O_C)+\sum_p\delta_p.
\]
Using
\[
p_a(C)=1-\chi(\mathcal O_C)
\]
and
\[
p_g(C)=g(\widetilde C)
=1-\chi(\mathcal O_{\widetilde C}),
\]
gives the displayed formula.
:::

<1>4. Hence a singular curve can have geometric genus strictly smaller than its arithmetic genus, with
\[
\boxed{0\le p_g(C)\le p_a(C).}
\]
::: {.proof}
Each $\delta_p$ in <1>3 is a nonnegative integer, so
\[
p_g(C)=p_a(C)-\sum_p\delta_p\le p_a(C).
\]
The geometric genus is the genus of a smooth projective curve and is therefore nonnegative.
:::

<1>5. For a plane curve of degree $d$,
\[
\boxed{
p_g(C)
=\frac{(d-1)(d-2)}2
-\sum_p\delta_p.
}
\]
::: {.proof}
The arithmetic genus of every plane curve of degree $d$ is
\[
p_a(C)=\frac{(d-1)(d-2)}2.
\]
Substitute this into <1>3.
:::

<1>6. For example, the cuspidal cubic
\[
C=V(y^3-x^2z)\subseteq\mathbb P^2
\]
has
\[
p_a(C)=1,
\qquad
p_g(C)=0.
\]
::: {.proof}
The preceding arithmetic-genus computation gives $p_a(C)=1$.  The cusp has
\[
\delta=1,
\]
so <1>3 gives
\[
p_g(C)=1-1=0.
\]
Equivalently, the normalization is $\mathbb P^1$, which has genus $0$.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>1 defines geometric genus, and steps <1>3--<1>6 explain exactly what it can become in the presence of singularities.
:::
:::
