---
schema: qual/card@1
id: P-6ATGL
kind: problem
title: $H_0(X,A)=0$ if and only if $A$ meets every path-component of $X$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 8 of the official UGA Fall 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the relative long exact sequence argument using the canonical basis of H_0 by path components.
---

::: problem
Let $A\subset X$.
Prove that the relative homology group $H_0(X,A)$ is trivial if and only if $A$ intersects every path component of $X$.
:::

::: {.solution}
Let
\[
i:A\hookrightarrow X
\]
be the inclusion.

<1>1. The relative long exact sequence identifies $H_0(X,A)$ with the cokernel of
\[
i_*:H_0(A;\ZZ)\longrightarrow H_0(X;\ZZ).
\]
::: {.proof}
The degree-zero part of the long exact sequence of the pair $(X,A)$ is
\[
H_0(A;\ZZ)
\xrightarrow{i_*}
H_0(X;\ZZ)
\longrightarrow
H_0(X,A;\ZZ)
\longrightarrow 0.
\]
Exactness therefore gives
\[
H_0(X,A;\ZZ)
\cong
H_0(X;\ZZ)/\operatorname{im}i_*.
\]
Thus
\[
H_0(X,A;\ZZ)=0
\quad\Longleftrightarrow\quad
i_*\text{ is surjective}.
\]
:::

<1>2. The map $i_*$ is surjective if and only if $A$ meets every path component of $X$.
::: {.proof}
For any space $Y$, its zeroth singular homology is canonically the free abelian group on its path components:
\[
H_0(Y;\ZZ)
\cong
\bigoplus_{C\in\pi_0^{\mathrm{path}}(Y)}\ZZ[C].
\]
If $D$ is a path component of $A$, then $D$ lies in a unique path component $C$ of $X$, and the inclusion induces
\[
i_*([D])=[C].
\]
Hence the image of $i_*$ is generated precisely by those basis elements $[C]$ for which $C\cap A\neq\varnothing$.
Therefore $i_*$ is surjective exactly when
\[
C\cap A\neq\varnothing
\]
for every path component $C$ of $X$.
:::

<1>3. Consequently,
\[
H_0(X,A;\ZZ)=0
\]
if and only if $A$ intersects every path component of $X$.
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
