---
schema: qual/card@1
id: P-UCLARA17S-09
kind: problem
title: UCLA analysis Spring 2017, Problem 9
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f(z)$ be entire and assume $f(0)\ne0$. Let $\{a_n\}$ be the zeros of $f$, repeated according to multiplicity.

(a) Let $R>0$ be such that $|f(z)|>0$ on $|z|=R$. Prove
\[
\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta
=\log|f(0)|+\sum_{|a_n|<R}\log\frac{R}{|a_n|}.
\]

(b) Prove that if there are constants $C$ and $\lambda$ such that $|f(z)|\le Ce^{|z|^\lambda}$ for all $z$, then
\[
\sum_n\left(\frac1{|a_n|}\right)^{\lambda+\varepsilon}<\infty
\]
for all $\varepsilon>0$. Hint: estimate $\#\{n:|a_n|<R\}$ using (a) on $|z|\sim2R$.
:::
