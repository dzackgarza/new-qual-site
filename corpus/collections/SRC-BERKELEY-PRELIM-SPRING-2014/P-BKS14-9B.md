---
schema: qual/card@1
id: P-BKS14-9B
kind: problem
title: Burnside counting for a transitive action
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
---

::: {.problem}
Let a finite group \(G\) act transitively on a finite set \(X\). For \(g\in G\), let
\[
\operatorname{Fix}_g(X)=\{x\in X:g(x)=x\}.
\]

(a) Show that
\[
|G|=\sum_{g\in G}|\operatorname{Fix}_g(X)|.
\]
Hint: count \(\{(x,g)\in X\times G:gx=x\}\) in two ways.

(b) Show that if \(|X|>1\), then some \(g\in G\) fixes no point of \(X\).
:::
