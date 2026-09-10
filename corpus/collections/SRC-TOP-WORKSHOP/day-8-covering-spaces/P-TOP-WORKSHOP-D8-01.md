---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-01
kind: problem
title: Uniqueness of lifts into a covering space
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Wisconsin Jan ’98) Let $p:\widetilde X\to X$ be a cover.
Suppose that $f,g:Y\to\widetilde X$ are maps such that $p\circ f$ and $p\circ g$ are equal and assume that $f$ and $g$ agree at $y_0\in Y$.
Show that if $Y$ is connected, then $f=g$.
:::

::: {.solution}
Put \(h=p\circ f=p\circ g\), and let
\[
A=\{y\in Y:f(y)=g(y)\}.
\]
By assumption \(y_0\in A\), so \(A\ne\varnothing\).

We show that \(A\) and its complement are open. Fix \(y\in Y\), and choose an evenly covered neighborhood \(U\) of \(h(y)\):
\[
p^{-1}(U)=\bigsqcup_{\lambda}V_\lambda,
\]
with each \(p|_{V_\lambda}:V_\lambda\to U\) a homeomorphism. By continuity of \(h,f,g\), after shrinking to a neighborhood \(W\ni y\) we may assume \(h(W)\subset U\), while \(f(W)\) and \(g(W)\) lie in the sheets containing \(f(y)\) and \(g(y)\), respectively.

If \(f(y)=g(y)\), these are the same sheet. Since \(p\) is injective on that sheet and \(pf=pg\), we have \(f=g\) on \(W\). Hence \(A\) is open.

If \(f(y)\ne g(y)\), then the two points lie in distinct sheets over \(U\). The corresponding neighborhoods \(f(W)\) and \(g(W)\) remain in distinct sheets, so \(f(w)\ne g(w)\) for every \(w\in W\). Hence \(Y\setminus A\) is open.

Thus \(A\) is a nonempty clopen subset of connected \(Y\). Therefore \(A=Y\), so \(f=g\).
:::
