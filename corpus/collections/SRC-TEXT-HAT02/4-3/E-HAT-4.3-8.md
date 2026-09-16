---
schema: qual/card@1
id: E-HAT-4.3-8
kind: problem
title: "Fibrations from sections of $E^I \\to E_p$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 8; corrected the stored one-way implication to Hatcher's if-and-only-if statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that a map $p: E \to B$ is a fibration if and only if the map $\pi: E^I \to E_p$, $\pi(\gamma) = (\gamma(0), p\gamma)$ has a section, that is, a map $s: E_p \to E^I$ such that $\pi s = \mathbb{1}$.
:::

::: {.solution}
Write
\[
E_p=\{(e,\alpha)\in E\times B^I:p(e)=\alpha(0)\},
\qquad
\pi:E^I\to E_p,
\quad
\pi(\gamma)=(\gamma(0),p\gamma).
\]

Suppose first that \(\pi\) has a section \(s\). Given a lifting problem
\[
f:X\to E,
\qquad
H:X\times I\to B,
\qquad
H(x,0)=pf(x),
\]
let \(H_x(t)=H(x,t)\). Then
\[
x\longmapsto(f(x),H_x)
\]
is a map \(X\to E_p\), and
\[
\widetilde H(x,t)=s(f(x),H_x)(t)
\]
satisfies
\[
\widetilde H(x,0)=f(x),
\qquad
p\widetilde H(x,t)=H(x,t).
\]
Thus \(p\) has the homotopy lifting property and is a fibration.

Conversely, suppose \(p\) is a fibration. Over \(E_p\), consider the map
\[
q:E_p\to E,
\qquad q(e,\alpha)=e,
\]
and the homotopy
\[
K:E_p\times I\to B,
\qquad K((e,\alpha),t)=\alpha(t).
\]
At time \(0\),
\[
K(-,0)=pq.
\]
By the homotopy lifting property there is
\[
\widetilde K:E_p\times I\to E
\]
with \(\widetilde K(-,0)=q\) and \(p\widetilde K=K\). Define
\[
s(e,\alpha)(t)=\widetilde K((e,\alpha),t).
\]
Then
\[
s(e,\alpha)(0)=e,
\qquad
p\,s(e,\alpha)=\alpha,
\]
so \(\pi s=\operatorname{id}_{E_p}\). Hence
\[
\boxed{p\text{ is a fibration iff }\pi\text{ has a section}.}
\]
:::
