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
---

::: problem
I give you two matrices over a field.
How would you tell if they are conjugate or not?
What theorem are you using?
State it.
How does it apply to this situation?
Why is $k[x]$ a PID? If two matrices are conjugate over the algebraic closure of a field, does that mean that they are conjugate over the base field too?
:::

::: {.solution}
**Goal.** Explain how to test conjugacy of matrices, the theorem used, and answer the algebraic-closure question.

<1>1. Two matrices $A, B \in M_n(k)$ are conjugate iff they have the same rational canonical form.
Proof: the rational canonical form is a complete invariant of conjugacy (similarity) over $k$.

<1>2. The theorem is the structure theorem for finitely generated modules over a PID.
<2>1. $k[x]$ is a PID.
Proof: $k[x]$ is a Euclidean domain (polynomial division), and every Euclidean domain is a PID.
<2>2. $M_n(k)$-conjugacy of $A$ and $B$ is equivalent to $k[x]$-module isomorphism of $k^n$ with $x$ acting as $A$ and as $B$.
Proof: a matrix $A$ makes $k^n$ into a $k[x]$-module via $x \cdot v = Av$; two matrices are conjugate iff the corresponding modules are isomorphic.
<2>3. The structure theorem decomposes a finitely generated $k[x]$-module into invariant factors, which determine the rational canonical form.
Proof: the invariant factors are the elementary divisors, giving the rational canonical form.

<1>3. Conjugacy over $\bar k$ implies conjugacy over $k$.
<2>1. The rational canonical form of a matrix is computed from the invariant factors of $xI - A$ in $k[x]$.
Proof: the invariant factors are the diagonal entries of the Smith normal form of $xI - A$ over $k[x]$.
<2>2. These invariant factors are polynomials in $k[x]$, and computing them over $\bar k[x]$ gives the same polynomials.
Proof: the Smith normal form of $xI - A$ is the same whether computed over $k[x]$ or $\bar k[x]$ (the invariant factors are monic polynomials in $k[x]$, and the computation is field-independent).
<2>3. Hence if $A$ and $B$ are conjugate over $\bar k$, they have the same rational canonical form, so they are conjugate over $k$.
Proof: conjugacy over $\bar k$ forces the same invariant factors, hence the same rational canonical form, hence conjugacy over $k$.

<1>4. Q.E.D.
Proof: <1>1 and <1>2 explain the test; <1>3 answers the algebraic-closure question (yes).
:::
