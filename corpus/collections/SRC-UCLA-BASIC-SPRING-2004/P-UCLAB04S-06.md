---
schema: qual/card@1
id: P-UCLAB04S-06
kind: problem
title: Equivalence of norms and closedness of finite-dimensional subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Exam Spring 2004 PDF. In part (b), the source writes merely "there exists a constant c"; the accompanying sphere-minimum hint makes the intended positive constant explicit.
---

::: {.problem}
Let $\|\cdot\|$ be any norm on $\mathbb R^n$, and let $\|\cdot\|_2$ be the Euclidean norm.

(a) Prove that there exists $d>0$ such that
\[
\|x\|\leq d\|x\|_2
\]
for every $x\in\mathbb R^n$, and use this to show that $N(x)=\|x\|$ is continuous in the usual topology on $\mathbb R^n$.

(b) Prove that there exists $c>0$ such that
\[
\|x\|\geq c\|x\|_2
\]
for every $x\in\mathbb R^n$.

Hint: use continuity of $N$ on the sphere $\{x:\|x\|_2=1\}$.

(c) Show that if $L$ is an $n$-dimensional subspace of an arbitrary normed vector space $V$, then $L$ is closed.
:::
