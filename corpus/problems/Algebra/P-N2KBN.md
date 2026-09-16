---
schema: qual/card@1
id: P-N2KBN
kind: problem
title: Conjugacy of matrices over a field and over its algebraic closure
classification:
  areas:
  - algebra
  topics:
  - Canonical Forms
  - Structure Theorem
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
I give you two matrices over a field.
How would you tell if they are conjugate or not?
What theorem are you using?
State it.
How does it apply to this situation?
Why is $k[x]$ a PID? If two matrices are conjugate over the algebraic closure of a field, does that mean that they are conjugate over the base field too?
:::

::: {.solution}
For $A\in M_n(k)$, make $k^n$ a $k[x]$-module by $x\cdot v=Av$. Then $A$ and $B$ are similar over $k$ iff the corresponding $k[x]$-modules are isomorphic. Since $k[x]$ is Euclidean (degree is a Euclidean function), it is a PID, and the structure theorem for finitely generated modules over a PID gives the invariant factors. Equivalently, these give the rational canonical form, which is a complete similarity invariant.

Thus one tests similarity by comparing the invariant factors (or rational canonical forms) of $A$ and $B$.

Moreover, if $A,B\in M_n(k)$ become similar over an extension field $K/k$—in particular over $\bar k$—then they were already similar over $k$. One clean proof uses ranks: for every $f\in k[x]$ and every $r\ge1$, similarity over $K$ gives
\[
\operatorname{rank}_K f(A)^r=\operatorname{rank}_K f(B)^r.
\]
A matrix with entries in $k$ has the same rank after scalar extension, so the corresponding ranks over $k$ are equal. Applying this to powers of each irreducible factor recovers the elementary divisors, hence the invariant factors, of $A$ and $B$. Therefore their rational canonical forms over $k$ coincide.
:::
