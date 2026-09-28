---
schema: qual/card@1
id: P-UCLAB13S-07
kind: problem
title: Matrix exponential and logarithm from operator-norm series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
(a) Define the operator norm of a real $n\times n$ matrix, considered as a linear transformation from $\mathbb R^n$ to $\mathbb R^n$.

(b) Let $I$ be the $n\times n$ identity matrix. Show that
\[
\exp(A)=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots
\]
converges entrywise.

(c) Show that
\[
\ln(I+A)=A-\frac{A^2}{2}+\frac{A^3}{3}-\cdots+(-1)^{n+1}\frac{A^n}{n}+\cdots
\]
converges if the operator norm of $A$ is less than one.

(d) Show that $\exp(\ln(I+A))=I+A$ if the operator norm of $A$ is less than one.
:::
