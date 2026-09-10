---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P6
kind: problem
title: Apply Seifert--van Kampen to a wedge sum and identify a presentation complex as a wedge of familiar spaces
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2013)

(a) Explain in detail how the Seifert--van Kampen theorem may be used to calculate the fundamental group of a wedge sum $X\vee Y$ of two spaces under suitable assumptions on the spaces.
Clarify what assumptions on the spaces you are using and how you are using them.

(b) Describe the presentation complex $X_G$ of the group $G=\langle a,b,c:a^2=1\rangle$ as a wedge sum of familiar spaces.
Explain carefully what results you are using.
:::

::: {.solution}
(a) Assume \(X\) and \(Y\) are path connected CW complexes, wedged at \(0\)-cells \(x_0,y_0\). Small open neighborhoods of the wedge point can be chosen so that there are open sets \(U,V\subset X\vee Y\) with
\[
U\simeq X,
\qquad
V\simeq Y,
\qquad
U\cap V\simeq\{*\}.
\]
Seifert--van Kampen then gives
\[
\pi_1(X\vee Y)
\cong
\pi_1(X)*\pi_1(Y),
\]
since the amalgamated subgroup \(\pi_1(U\cap V)\) is trivial. More generally, the same argument works whenever the wedge point has neighborhoods allowing such a van Kampen cover.

(b) The presentation complex of
\[
G=\langle a,b,c\mid a^2=1\rangle
\]
has one vertex, three \(1\)-cells \(a,b,c\), and one \(2\)-cell attached along the degree-two loop \(a^2\). The subcomplex consisting of the vertex, the \(a\)-edge, and this \(2\)-cell is the standard CW structure on \(\mathbb{RP}^2\). The \(b\)- and \(c\)-edges are two additional circle summands attached only at the vertex. Hence
\[
X_G\cong\mathbb{RP}^2\vee S^1\vee S^1.
\]
By van Kampen,
\[
\pi_1(X_G)\cong(\mathbb Z/2)*\mathbb Z*\mathbb Z,
\]
which is precisely the presented group.
:::
