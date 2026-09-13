---
schema: qual/card@1
id: P-UCLAB13F-03
kind: problem
title: Length of graphs of monotone functions
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
Let $\gamma:[0,1]\to\mathbb R^2$ be continuous and one-to-one, and define
\[
L(\gamma)=\sup\left\{\sum_{j=1}^{n-1}|\gamma(t_{j+1})-\gamma(t_j)|:0\le t_1<\cdots<t_n\le1,\ n<\infty\right\}.
\]

(a) If $f$ is continuous and nondecreasing on $[0,1]$ and $\gamma(t)=(t,f(t))$, prove
\[
L(\gamma)\le 1+f(1)-f(0).
\]

(b) Show that there exists continuous nondecreasing $f$ on $[0,1]$ with $f(0)=0$, $f(1)=1$, and $L(\gamma)=2$ for $\gamma(t)=(t,f(t))$.
:::
