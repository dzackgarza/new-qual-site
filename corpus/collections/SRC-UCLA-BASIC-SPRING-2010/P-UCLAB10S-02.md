---
schema: qual/card@1
id: P-UCLAB10S-02
kind: problem
title: Courant-Fischer characterization of ordered eigenvalues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 2. Let $A$ be an $n\times n$ real symmetric matrix with eigenvalues $\lambda_1\ge\cdots\ge\lambda_n$. Prove that
\[
\lambda_k=
\max_{\substack{U\subseteq\mathbb R^n\\ \dim U=k}}
\min_{\substack{x\in U\\ \|x\|=1}}
\langle Ax,x\rangle.
\]
:::
