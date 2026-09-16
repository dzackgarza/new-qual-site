---
schema: qual/card@1
id: P-UCLARA15S-03
kind: problem
title: Refined weak-type bound for the Hardy--Littlewood maximal function
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$ and let
\[
Mf(x)=\sup_{r>0}\frac1{m(B(r,x))}\int_{B(r,x)}|f(y)|\,dy
\]
be the Hardy--Littlewood maximal function.

(a) Show that
\[
m(\{x:Mf(x)>s\})\le\frac{C_n}{s}\int_{|f(x)|>s/2}|f(x)|\,dx,\qquad s>0,
\]
where $C_n$ depends only on $n$.
The Hardy--Littlewood maximal theorem may be used.

(b) Prove that if $\phi\in C^1(\mathbb R)$, $\phi(0)=0$, and $\phi'>0$, then
\[
\int \phi(Mf(x))\,dx\le C_n\int |f(x)|\left(\int_{0<t<2|f(x)|}\frac{\phi'(t)}t\,dt\right)dx.
\]
:::
