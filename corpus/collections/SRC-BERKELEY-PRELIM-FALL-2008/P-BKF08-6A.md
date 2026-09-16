---
schema: qual/card@1
id: P-BKF08-6A
kind: problem
title: Young's inequality from integrals of a function and its inverse
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf. The packet explicitly corrects both inequality directions from the original exam.
---

::: {.problem}
Let $f$ be a continuous strictly increasing function with $f(0)=0$ and inverse $f^{-1}$.
Show that
\[
\int_0^a f(x)\,dx+\int_0^b f^{-1}(x)\,dx\ge ab
\]
for all positive real numbers $a,b$.
Use this to prove Young's inequality: if $p,q>0$ satisfy $1/p+1/q=1$, then for all $a,b>0$,
\[
\frac{a^p}{p}+\frac{b^q}{q}\ge ab.
\]

*Source note.* The retained Fall 2008 solution packet states that the exam originally printed both inequalities with the wrong direction; the inequalities above are the packet's explicit correction.
:::
