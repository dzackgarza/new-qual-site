---
schema: qual/card@1
id: E-MUN-9-5
kind: problem
title: Right inverses from surjections via the axiom of choice
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Use the choice axiom to show that if $f: A \to B$ is surjective, then $f$ has a right inverse $h: B \to A$ .

(b) Show that if $f: A \to B$ is injective and $A$ is not empty, then $f$ has a left inverse.
Is the axiom of choice needed?
:::

::: {.solution}
(a) Since \(f:A\to B\) is surjective, every fiber
\[
f^{-1}(\{b\})\qquad(b\in B)
\]
is nonempty. The axiom of choice applied to this family of nonempty sets gives a choice function selecting
\[
h(b)\in f^{-1}(\{b\})
\]
for every \(b\in B\). Then
\[
f(h(b))=b
\]
for every \(b\), hence
\[
f\circ h=i_B.
\]
Thus \(h\) is a right inverse of \(f\).

(b) Suppose \(f:A\to B\) is injective and \(A\ne\varnothing\). Choose one fixed point \(a_0\in A\). Define
\[
g:B\to A,
\qquad
g(b)=
\begin{cases}
f^{-1}(b),&b\in f(A),\\a_0,&b\notin f(A).
\end{cases}
\]
The inverse value in the first case is unique because \(f\) is injective. Hence, for every \(a\in A\),
\[
g(f(a))=a,
\]
so \(g\circ f=i_A\). Thus \(g\) is a left inverse.

No axiom of choice is needed in (b): only one element \(a_0\) is chosen from the single nonempty set \(A\), and all remaining values are uniquely determined.
:::
