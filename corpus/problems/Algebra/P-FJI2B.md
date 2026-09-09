---
schema: qual/card@1
id: P-FJI2B
kind: problem
title: Classification of finitely generated modules over $\mathbb{Z}$, PIDs, and Dedekind
  rings
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Classify finitely-generated modules over $\ZZ$, over PIDs, and over Dedekind rings.
:::


::: {.solution}
Let all modules be finitely generated.

<1>1. Over $\ZZ$, every module is a finitely generated abelian group and has a unique invariant-factor decomposition
\[
M\cong \ZZ^r\oplus \ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_t\ZZ,
\qquad
1<d_1\mid d_2\mid\cdots\mid d_t.
\]
Equivalently, its torsion part has a unique elementary-divisor decomposition into cyclic groups of prime-power order.
::: {.proof}
This is the structure theorem for finitely generated modules over the PID $\ZZ$.
:::

<1>2. More generally, if $R$ is a PID, then
\[
M\cong R^r\oplus R/(a_1)\oplus\cdots\oplus R/(a_t),
\qquad
0\ne a_1\mid a_2\mid\cdots\mid a_t,
\]
with the nonunit invariant factors unique up to associates.
::: {.proof}
This is the structure theorem for finitely generated modules over a PID. The free rank $r$ and the invariant factors determine the isomorphism class. Factoring the $a_i$ into prime powers gives the equivalent elementary-divisor form.
:::

<1>3. Let $R$ be a Dedekind domain. Then every finitely generated module decomposes as
\[
M\cong P\oplus T,
\]
where $T$ is the torsion submodule and $P$ is finitely generated projective.
::: {.proof}
Over a Dedekind domain, finitely generated torsion-free modules are projective. The quotient $M/T$ is torsion-free, hence projective, so the exact sequence
\[
0\to T\to M\to M/T\to0
\]
splits. Put $P=M/T$.
:::

<1>4. If $P$ has positive rank $r$, then
\[
P\cong R^{r-1}\oplus I
\]
for a nonzero fractional ideal $I$, and the ideal class $[I]\in\operatorname{Cl}(R)$ is uniquely determined by $P$.
::: {.proof}
This is the Steinitz classification of finitely generated projective modules over a Dedekind domain. Two modules $R^{r-1}\oplus I$ and $R^{r-1}\oplus J$ are isomorphic iff $I$ and $J$ represent the same ideal class.
:::

<1>5. The torsion part has a unique primary decomposition
\[
T\cong
\bigoplus_{\mathfrak p}
\bigoplus_j R/\mathfrak p^{e_{\mathfrak p,j}},
\]
where only finitely many nonzero prime ideals $\mathfrak p$ occur and, for each $\mathfrak p$, the exponents may be ordered increasingly.
::: {.proof}
A finitely generated torsion module over a Dedekind domain has finite support. Localizing at a nonzero prime $\mathfrak p$ gives a finite-length module over the DVR $R_{\mathfrak p}$, hence a direct sum of cyclic modules $R_{\mathfrak p}/\mathfrak p^{e}R_{\mathfrak p}$. Gluing the primary pieces recovers the displayed global decomposition, with uniqueness inherited from the local DVR classifications.
:::

Thus the PID theorem is recovered from the Dedekind classification exactly when the class group is trivial: then every ideal $I$ is principal and every projective module is free.
:::
