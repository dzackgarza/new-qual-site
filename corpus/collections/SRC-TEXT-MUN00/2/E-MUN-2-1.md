---
schema: qual/card@1
id: E-MUN-2-1
kind: problem
title: Preimage and image under injective and surjective maps
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $f: A \to B$ . Let $A_0 \subset A$ and $B_0 \subset B$ .

(a) Show that $A_0 \subset f^{-1}(f(A_0))$ and that equality holds if $f$ is injective.

(b) Show that $f(f^{-1}(B_0)) \subset B_0$ and that equality holds if $f$ is surjective.
:::

::: {.solution}
(a) If \(a\in A_0\), then \(f(a)\in f(A_0)\), hence
\[
a\in f^{-1}(f(A_0)).
\]
Thus
\[
A_0\subset f^{-1}(f(A_0)).
\]
If \(f\) is injective and \(a\in f^{-1}(f(A_0))\), then \(f(a)=f(a_0)\) for some \(a_0\in A_0\). Injectivity gives \(a=a_0\in A_0\), so equality holds.

(b) If \(b\in f(f^{-1}(B_0))\), then \(b=f(a)\) for some \(a\) with \(f(a)\in B_0\). Hence \(b\in B_0\), so
\[
f(f^{-1}(B_0))\subset B_0.
\]
If \(f\) is surjective and \(b\in B_0\), choose \(a\in A\) with \(f(a)=b\). Then \(a\in f^{-1}(B_0)\), hence \(b\in f(f^{-1}(B_0))\). Thus equality holds.
:::
