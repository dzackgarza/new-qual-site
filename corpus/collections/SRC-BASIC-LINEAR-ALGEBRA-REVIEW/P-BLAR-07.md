---
schema: qual/card@1
id: P-BLAR-07
kind: problem
title: Decide linearity and find transformation matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md. In part (d), the deterministic source declares a map from R^3 to R^2 but writes the input as T(x,y); the card preserves this mismatch explicitly rather than silently inventing a third argument.
---

::: problem
Decide which of the following transformations are linear.
For those that are linear, find the matrix of the transformation using the standard bases.

1. \(T:\mathbb R^2\to\mathbb R^2\), \(T(x,y)=(2x,y)\).

2. \(T:\mathbb R^2\to\mathbb R^2\), \(T(x,y)=(x+1,y+2)\).

3. \(T:\mathbb R^2\to\mathbb R^2\) rotates an object through an angle of \(\pi/3\).

4. The source declares \(T:\mathbb R^3\to\mathbb R^2\) and then gives the formula
   \[
   T(x,y)=(x+2y,x+3y).
   \]
   Analyze the stated transformation, noting the source's domain/formula mismatch.
:::
