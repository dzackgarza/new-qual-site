---
schema: qual/card@1
id: P-UCLAB01F-07
kind: problem
title: Annihilator of an image and rank of the transpose
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Let $V$ be a real vector space and $X\subseteq V$ a subspace.
Write
\[
V^*=\{f:V\to\mathbb R:f\text{ is linear}\}
\]
and
\[
X^0=\{f\in V^*:f(x)=0\text{ for every }x\in X\}.
\]
Let $T:V\to W$ be a linear transformation of finite-dimensional real vector spaces, and let its transpose $T^t:W^*\to V^*$ be defined by $T^t(f)=f\circ T$.
Prove that
\[
(\operatorname{im}T)^0=\ker(T^t)
\]
and
\[
\dim\operatorname{im}T=\dim\operatorname{im}T^t.
\]
:::
