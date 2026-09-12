---
schema: qual/card@1
id: E-K8RRE
kind: problem
title: Closure of an interval in the order topology
classification:
  areas:
  - topology
  topics:
  - Closure
  - Order Topology
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

Let $X$ be an ordered set in the order topology.
Show that $\overline{(a, b)} \subset [a, b]$.
Under what conditions does equality hold?
:::

::: {.solution}
The set $[a,b]$ is closed in the order topology: its complement is the union of the open rays
\[
(-\infty,a)\cup(b,\infty).
\]
Since $(a,b)\subseteq[a,b]$, minimality of closure gives
\[
\overline{(a,b)}\subseteq[a,b].
\]
All points of $(a,b)$ are already in the closure, so equality is equivalent to having both endpoints $a,b$ in the closure.

The point $a$ lies in $\overline{(a,b)}$ exactly when $a$ has no immediate successor in $X$ (equivalently, every order-neighborhood of $a$ contains a point strictly between $a$ and $b$). If $a$ has an immediate successor $s$, then an order-neighborhood ending at $s$ contains $a$ but no point of $(a,b)$. Conversely, if there is no immediate successor, every neighborhood of $a$ contains some point $x$ with
\[
a<x<b.
\]
Similarly, $b\in\overline{(a,b)}$ exactly when $b$ has no immediate predecessor.

Hence
\[
\boxed{\overline{(a,b)}=[a,b]}
\]
if and only if $a$ has no immediate successor and $b$ has no immediate predecessor.
:::
