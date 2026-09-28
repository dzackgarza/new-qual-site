---
schema: qual/card@1
id: P-AGPERFECTFIELD
kind: problem
title: Curves over a perfect field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Perfect Fields
  - Curves
  - Smoothness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Coleman's question on curves over perfect fields.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
What can you say about curves over perfect fields?
:::

::: {.solution}
Let $k$ be a perfect field and let $C$ be a curve of finite type over $k$.

<1>1. For a scheme locally of finite type over a perfect field,
\[
\boxed{
C\text{ is regular}
\quad\Longleftrightarrow\quad
C\to\operatorname{Spec}k\text{ is smooth}.
}
\]
::: {.proof}
Smoothness over a field means geometric regularity: after every field extension, the fibres remain regular.  Smooth schemes are therefore regular over any field.

Conversely, if $k$ is perfect, every finite extension of $k$ is separable.  For a finite-type $k$-scheme this removes the purely inseparable residue-field obstruction, so a regular local ring remains geometrically regular over $k$.  Thus a regular finite-type $k$-scheme is smooth over $k$.
:::

<1>2. In particular, a normal curve over a perfect field is smooth.
::: {.proof}
Let $p$ be a point of a normal Noetherian integral curve $C$.

At the generic point, the local ring is a field and is regular.  At a closed point, $\mathcal O_{C,p}$ is a one-dimensional Noetherian normal local domain.  Such a ring is a discrete valuation ring, hence a regular local ring of dimension one.  Therefore every local ring of $C$ is regular, so $C$ is regular.  Apply <1>1.
:::

<1>3. Consequently, normalization resolves the singularities of an integral curve over a perfect field.
::: {.proof}
Let
\[
\nu:\widetilde C\longrightarrow C
\]
be the normalization.  The scheme $\widetilde C$ is normal by definition.  Since normalization of a finite-type curve over a field is again a finite-type curve, <1>2 shows that $\widetilde C$ is smooth over $k$.

Thus in dimension one the normalization itself is a resolution of singularities: it is a finite birational morphism from a smooth curve.
:::

<1>4. Over an imperfect field, a regular scheme of finite type need not be smooth.
::: {.proof}
Let
\[
k=\mathbb F_p(t),
\]
which is imperfect, and consider
\[
X=\operatorname{Spec}k[x]/(x^p-t).
\]
The polynomial $x^p-t$ is irreducible over $k$, so the coordinate ring is a field.  Hence $X$ is regular.

After adjoining $t^{1/p}$,
\[
k(t^{1/p})\otimes_k k[x]/(x^p-t)
\cong
k(t^{1/p})[x]/(x-t^{1/p})^p,
\]
which is nonreduced.  Thus $X$ is not geometrically regular and hence is not smooth over $k$.

The same phenomenon is what perfectness excludes for curves: over a perfect base, regularity cannot be destroyed by a purely inseparable residue-field extension.
:::

<1>5. Hence
\[
\boxed{
\text{over a perfect field, normal }\Longleftrightarrow
\text{ regular }\Longleftrightarrow\text{ smooth}
}
\]
for an integral curve, and the normalization of any integral curve is smooth.
::: {.proof}
For curves, normality is equivalent to regularity by the DVR characterization in <1>2, and regularity is equivalent to smoothness by <1>1.  Step <1>3 gives the normalization statement.
:::

<1>6. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 give the regularity, smoothness, and normalization consequences that distinguish curves over perfect fields.
:::
:::
