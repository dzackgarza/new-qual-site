---
schema: qual/card@1
id: E-HAT-4.1-11
kind: problem
title: "Contractibility from nullhomotopic inclusions"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that a CW complex is contractible if it is the union of an increasing sequence of subcomplexes $X_1 \subset X_2 \subset \cdots$ such that each inclusion $X_i \hookrightarrow X_{i+1}$ is nullhomotopic, a condition sometimes expressed by saying $X_i$ is contractible in $X_{i+1}$.
An example is $S^\infty$, or more generally the infinite suspension $S^\infty X$ of any CW complex $X$, the union of the iterated suspensions $S^n X$.
:::

::: {.solution}
First, \(X\) is path-connected. Given \(x,y\in X\), both lie in some \(X_i\); the nullhomotopy of \(X_i\hookrightarrow X_{i+1}\) supplies paths from their images to the same point of \(X_{i+1}\).

Now let
\[
f:S^n\to X
\]
be any based map, \(n\ge1\). Since \(S^n\) is compact and \(X\) is a CW complex, \(f(S^n)\) is contained in a finite subcomplex of \(X\). Because the \(X_i\)'s are increasing and have union \(X\), this finite subcomplex is contained in some \(X_i\). Thus \(f\) factors through \(X_i\).

But the inclusion
\[
X_i\hookrightarrow X_{i+1}
\]
is nullhomotopic, so the composite \(S^n\to X_i\to X_{i+1}\), and hence \(f:S^n\to X\), is nullhomotopic. Consequently
\[
\pi_n(X)=0\qquad(n\ge1).
\]
The map \(X\to *\) therefore induces isomorphisms on all homotopy groups (and on \(\pi_0\)). Since both spaces have CW type, Whitehead's theorem gives
\[
\boxed{X\simeq *}.
\]
Thus \(X\) is contractible. In particular this applies to \(S^\infty\) and to infinite suspensions \(S^\infty X\).
:::
