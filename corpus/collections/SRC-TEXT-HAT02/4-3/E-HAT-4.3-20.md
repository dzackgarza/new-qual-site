---
schema: qual/card@1
id: E-HAT-4.3-20
kind: problem
title: "Postnikov towers for $\\Omega X$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that by applying the loop space functor to a Postnikov tower for $X$ one obtains a Postnikov tower of principal fibrations for $\Omega X$.

::: {.solution}
Let
\[
\cdots\to X_n\to X_{n-1}\to\cdots
\]
be a Postnikov tower for \(X\). Looping preserves fibrations, so
\[
\cdots\to\Omega X_n\to\Omega X_{n-1}\to\cdots
\]
is a tower of fibrations. Since
\[
\pi_i(\Omega X_n)=\pi_{i+1}(X_n),
\]
the space \(\Omega X_n\) has the correct truncated homotopy groups to be the corresponding Postnikov stage of \(\Omega X\).

The successive Postnikov fibration is classified by a \(k\)-invariant. Looping its classifying map expresses
\[
\Omega X_{n+1}\to\Omega X_n
\]
as a pullback of a path-space fibration. Equivalently, the three-term sequence
\[
\Omega X_{n+1}\longrightarrow\Omega X_n\longrightarrow\Omega X_{n-1}
\]
is a principal fibration, with fiber an Eilenberg--MacLane loop space. Thus
\[
\boxed{\text{looping a Postnikov tower for }X\text{ gives a Postnikov tower of principal fibrations for }\Omega X.}
\]
:::
