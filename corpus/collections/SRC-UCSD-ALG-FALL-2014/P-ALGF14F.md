---
schema: qual/card@1
id: P-ALGF14F
kind: problem
title: Finitely generated projective or flat modules over a PID are free
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Projective Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2014; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified freeness of finitely generated projectives via split finite free presentations and freeness of finitely generated flats via torsion-freeness over a PID.
---

::: {.problem}
Let $A$ be a PID.

(i) Prove that a finitely generated projective $A$-module is free.

(ii) Prove that a finitely generated flat $A$-module is free.
:::


::: {.solution}
<1>1. Every finitely generated projective \(A\)-module is a direct summand of a finite-rank free module.
::: {.proof}
Let \(P\) be finitely generated and projective.
Choose generators \(p_1,\ldots,p_m\).
They define a surjection
\[
\pi:A^m\twoheadrightarrow P.
\]
Because \(P\) is projective, this surjection splits: there is an \(A\)-linear map
\[
s:P\to A^m
\]
with
\[
\pi s=\operatorname{id}_P.
\]
Therefore
\[
A^m=s(P)\oplus\ker\pi,
\]
so \(P\cong s(P)\) is a submodule, indeed a direct summand, of the finite free module \(A^m\).
:::

<1>2. Every finitely generated projective \(A\)-module is free.
::: {.proof}
A submodule of a free module over a PID is free.
By <1>1, a finitely generated projective module \(P\) is isomorphic to a submodule of the free module \(A^m\).
Hence \(P\) is free.
:::

<1>3. Every flat \(A\)-module is torsion-free.
::: {.proof}
Let \(M\) be flat and let \(0\neq a\in A\).
Because \(A\) is an integral domain, multiplication by \(a\) gives an injective map
\[
0\longrightarrow A
\overset{\cdot a}{\longrightarrow}A.
\]
Tensoring with the flat module \(M\) preserves injectivity, so
\[
0\longrightarrow A\otimes_A M
\overset{\cdot a\otimes1}{\longrightarrow}
A\otimes_A M
\]
is exact.
Under the canonical identification
\[
A\otimes_A M\cong M,
\]
this map is multiplication by \(a\):
\[
m\longmapsto am.
\]
Thus
\[
am=0
\quad\Longrightarrow\quad
m=0.
\]
Since this holds for every nonzero \(a\in A\), the module \(M\) is torsion-free.
:::

<1>4. Every finitely generated flat \(A\)-module is free.
::: {.proof}
Let \(M\) be finitely generated and flat.
By <1>3, \(M\) is torsion-free.
The structure theorem for finitely generated modules over a PID gives
\[
M\cong A^r\oplus T,
\]
where \(T\) is the torsion submodule.
Since \(M\) is torsion-free,
\[
T=0.
\]
Hence
\[
M\cong A^r,
\]
so \(M\) is free.
:::
:::
