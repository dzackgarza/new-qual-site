---
schema: qual/card@1
id: E-HAT-4.1-23
kind: problem
title: "Mapping cylinders and cones have CW type"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 23; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

If $f: X \to Y$ is a map with $X$ and $Y$ homotopy equivalent to CW complexes, show that the pair $(M_f, X)$ is homotopy equivalent to a CW pair, where $M_f$ is the mapping cylinder.
Deduce that the mapping cone $C_f$ has the homotopy type of a CW complex.

::: {.solution}
Choose CW complexes \(X'\) and \(Y'\) together with homotopy equivalences
\[
u:X'\xrightarrow{\simeq}X,
\qquad
v:Y'\xrightarrow{\simeq}Y,
\]
and homotopy inverses \(u^{-1}\) and \(v^{-1}\). Define
\[
f'=v^{-1}fu:X'\to Y'.
\]
By cellular approximation, replace \(f'\) by a cellular map without changing its homotopy class.

The homotopy-commutative square
\[
\begin{array}{ccc}
X'&\xrightarrow{f'}&Y'\\
\downarrow u&&\downarrow v\\
X&\xrightarrow{f}&Y
\end{array}
\]
has vertical homotopy equivalences. Mapping cylinders are homotopy pushouts, so homotopy invariance of homotopy pushouts gives a homotopy equivalence of pairs
\[
(M_{f'},X')\simeq(M_f,X).
\]
(Equivalently, one can write the maps explicitly using chosen homotopies making the square commute.)

Because \(f'\) is cellular, its mapping cylinder admits a CW structure for which \(X'\subset M_{f'}\) is a subcomplex. Hence
\[
\boxed{(M_f,X)\text{ is homotopy equivalent to a CW pair}.}
\]

The mapping cone is the quotient
\[
C_f=M_f/X.
\]
Passing to the homotopy-equivalent CW pair gives
\[
C_f\simeq M_{f'}/X'.
\]
The quotient of a CW complex by a subcomplex is again a CW complex. Therefore
\[
\boxed{C_f\text{ has the homotopy type of a CW complex}.}
\]
:::
