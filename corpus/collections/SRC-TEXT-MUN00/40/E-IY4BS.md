---
schema: qual/card@1
id: E-IY4BS
kind: problem
title: F-sigma and G-delta sets
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

A subset $W$ of $X$ is said to be an "$F_\sigma$ set" in $X$ if $W$ equals a countable union of closed sets of $X$.
Show that $W$ is an $F_\sigma$ set in $X$ if and only if $X - W$ is a $G_\delta$ set in $X$.

[The terminology comes from the French. The "F" stands for "fermé," which means "closed," and the "σ" for "somme," which means "union."]
:::

::: {.solution}
Suppose first that
\[
W=\bigcup_{n=1}^{\infty}F_n
\]
with each \(F_n\) closed. By De Morgan's law,
\[
X-W
 =X-\bigcup_nF_n
 =\bigcap_n(X-F_n).
\]
Each \(X-F_n\) is open, so \(X-W\) is a \(G_\delta\) set.

Conversely, suppose
\[
X-W=\bigcap_{n=1}^{\infty}U_n
\]
with each \(U_n\) open. Again by De Morgan's law,
\[
W
=X-\bigcap_nU_n
=\bigcup_n(X-U_n).
\]
Each \(X-U_n\) is closed, so \(W\) is \(F_\sigma\).

Therefore
\[
\boxed{W\text{ is }F_\sigma\iff X-W\text{ is }G_\delta.}
\]
:::
