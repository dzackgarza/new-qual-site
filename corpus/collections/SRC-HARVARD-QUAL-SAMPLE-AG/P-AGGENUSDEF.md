---
schema: qual/card@1
id: P-AGGENUSDEF
kind: problem
title: The genus of a curve, and its independence of the embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Curves
  - Invariance
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Hartshorne's question on the genus of a curve and whether it depends on an embedding.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What is the genus of a curve?

Does the genus of a curve depend on the embedding?
:::

::: {.solution}
<1>1. For a connected projective curve $C$, the arithmetic genus is
\[
\boxed{p_a(C)=1-\chi(C,\mathcal O_C).}
\]
::: {.proof}
For a projective curve,
\[
\chi(C,\mathcal O_C)
=h^0(C,\mathcal O_C)-h^1(C,\mathcal O_C).
\]
The arithmetic genus is defined intrinsically by
\[
p_a(C)=1-\chi(C,\mathcal O_C).
\]
Equivalently, if an embedding is used to form the Hilbert polynomial, its constant term is $\chi(\mathcal O_C)=1-p_a(C)$.
:::

<1>2. If $C$ is smooth, projective, and geometrically connected, then the usual genus is
\[
\boxed{
g(C)=h^1(C,\mathcal O_C)=h^0(C,\omega_C).
}
\]
::: {.proof}
For a geometrically connected proper curve,
\[
h^0(C,\mathcal O_C)=1.
\]
Hence
\[
p_a(C)
=1-(1-h^1(C,\mathcal O_C))
=h^1(C,\mathcal O_C).
\]
Serre duality on the smooth projective curve gives
\[
H^1(C,\mathcal O_C)^\vee
\cong
H^0(C,\omega_C),
\]
so the two dimensions agree.
:::

<1>3. Over an algebraically closed field, for a possibly singular integral projective curve $C$, the geometric genus is
\[
\boxed{
p_g(C)=h^0(\widetilde C,\omega_{\widetilde C}),
}
\]
where
\[
\nu:\widetilde C\longrightarrow C
\]
is the normalization.
::: {.proof}
The normalization $\widetilde C$ is normal and one-dimensional, hence regular; over an algebraically closed field it is therefore smooth.  It is the smooth projective model of the function field obtained by resolving the curve singularities.  Its ordinary smooth genus is therefore the intrinsic genus of the function field, and this is by definition the geometric genus of $C$.
:::

<1>4. For a smooth projective curve,
\[
\boxed{p_a(C)=p_g(C)=g(C).}
\]
::: {.proof}
If $C$ is smooth, it is already normal, so
\[
\widetilde C=C.
\]
Then <1>2 computes both the arithmetic genus and the geometric genus as
\[
h^1(C,\mathcal O_C)=h^0(C,\omega_C).
\]
:::

<1>5. Over $\mathbb C$, this same integer is the topological genus: the underlying compact Riemann surface has Euler characteristic
\[
\boxed{\chi_{\mathrm{top}}(C)=2-2g(C).}
\]
::: {.proof}
For a compact Riemann surface, Hodge theory identifies
\[
\dim_{\mathbb C}H^0(C,\Omega_C^1)=g
\]
with half the first Betti number.  Hence
\[
b_0=1,
\qquad
b_1=2g,
\qquad
b_2=1,
\]
and therefore
\[
\chi_{\mathrm{top}}=1-2g+1=2-2g.
\]
:::

<1>6. The genus does not depend on a projective embedding of the curve.
::: {.proof}
The quantities
\[
\chi(C,\mathcal O_C),
\qquad
h^1(C,\mathcal O_C),
\qquad
h^0(C,\omega_C),
\]
are invariants of the abstract curve itself.  Likewise the normalization is intrinsic, so $p_g(C)$ is intrinsic for a singular curve.

Thus changing an embedding
\[
C\hookrightarrow\mathbb P^N
\]
can change the degree and the full Hilbert polynomial presentation, but it cannot change $p_a$, $p_g$, or the smooth genus $g$.
:::

<1>7. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 give the standard meanings of genus, and step <1>6 proves the requested embedding independence.
:::
:::
