---
schema: qual/card@1
id: E-MUN-2-2
kind: problem
title: Preimage preserves all set operations; image preserves unions only
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 2; restored parts (g) and (h) to the printed request for counterexamples where equality fails.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $f: A \to B$ and let $A_i \subset A$ and $B_i \subset B$ for $i = 0$ and $i = 1$ . Show that $f^-$

preserves inclusions, unions, intersections, and differences of sets:

(a) $B_0 \subset B_1 \Rightarrow f^{-1}(B_0) \subset f^{-1}(B_1)$ .

(b) $f^{-1}(B_{0} \cup B_{1}) = f^{-1}(B_{0}) \cup f^{-1}(B_{1}).$

(c) $f^{-1}(B_{0} \cap B_{1}) = f^{-1}(B_{0}) \cap f^{-1}(B_{1}).$

(d) $f^{-1}(B_0 - B_1) = f^{-1}(B_0) - f^{-1}(B_1)$ .

Show that $f$ preserves inclusions and unions only:

(e) $A_0 \subset A_1 \Rightarrow f(A_0) \subset f(A_1)$ .

(f) $f(A_{0} \cup A_{1}) = f(A_{0}) \cup f(A_{1}).$

(g) $f(A_0 \cap A_1) \subset f(A_0) \cap f(A_1)$ ; give an example where equality fails.

(h) $f(A_0 - A_1) \supset f(A_0) - f(A_1)$ ; give an example where equality fails.
:::

::: {.solution}
For preimages, all four assertions follow directly from the equivalence
\[
x\in f^{-1}(S)\iff f(x)\in S.
\]
Thus:

(a) If \(B_0\subset B_1\) and \(x\in f^{-1}(B_0)\), then \(f(x)\in B_1\), so \(x\in f^{-1}(B_1)\).

(b)
\[
x\in f^{-1}(B_0\cup B_1)
\iff f(x)\in B_0\text{ or }f(x)\in B_1
\iff x\in f^{-1}(B_0)\cup f^{-1}(B_1).
\]

(c) The same argument with ``and'' gives
\[
f^{-1}(B_0\cap B_1)=f^{-1}(B_0)\cap f^{-1}(B_1).
\]

(d) Likewise,
\[
f^{-1}(B_0-B_1)=f^{-1}(B_0)-f^{-1}(B_1).
\]

For images:

(e) If \(A_0\subset A_1\), every value attained on \(A_0\) is attained on \(A_1\), so \(f(A_0)\subset f(A_1)\).

(f) A value is attained on \(A_0\cup A_1\) exactly when it is attained on at least one of \(A_0,A_1\), hence
\[
f(A_0\cup A_1)=f(A_0)\cup f(A_1).
\]

(g) If \(y=f(x)\) for some \(x\in A_0\cap A_1\), then \(y\in f(A_0)\cap f(A_1)\), so
\[
f(A_0\cap A_1)\subset f(A_0)\cap f(A_1).
\]
Equality can fail: let \(f:\{0,1\}\to\{*\}\) be constant, \(A_0=\{0\}\), and \(A_1=\{1\}\). Then the left side is empty and the right side is \(\{*\}\). If \(f\) is injective, equality does hold, since equal image values then come from the same point.

(h) If \(y\in f(A_0)-f(A_1)\), write \(y=f(x)\) with \(x\in A_0\). Since \(y\notin f(A_1)\), necessarily \(x\notin A_1\), so \(x\in A_0-A_1\). Thus
\[
f(A_0-A_1)\supset f(A_0)-f(A_1).
\]
Equality can fail for the same constant map with \(A_0=\{0,1\}\), \(A_1=\{1\}\): the left side is \(\{*\}\), while the right side is empty. If \(f\) is injective, equality holds.
:::
