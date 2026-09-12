---
schema: qual/card@1
id: E-C0ZWV
kind: problem
title: Homotopy classes into an interval and out of a path-connected space
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Given spaces $X$ and $Y$, let $[X, Y]$ denote the set of homotopy classes of maps of $X$ into $Y$.

(a) Let $I = [0, 1]$.
Show that for any $X$, the set $[X, I]$ has a single element.

(b) Show that if $Y$ is path connected, the set $[I, Y]$ has a single element.
:::

::: {.solution}
(a) Let \(f,g:X\to I\) be arbitrary. Since \(I=[0,1]\) is convex, define
\[
H(x,t)=(1-t)f(x)+tg(x).
\]
Then \(H:X\times I\to I\) is continuous, \(H(x,0)=f(x)\), and \(H(x,1)=g(x)\). Thus every two maps \(X\to I\) are homotopic, so \([X,I]\) has one element.

(b) Let \(f,g:I\to Y\). Since \(Y\) is path connected, choose a path \(\alpha:I\to Y\) from \(f(0)\) to \(g(0)\). Every map from an interval is homotopic to the constant map at its initial value: for \(f\),
\[
F(s,t)=f((1-t)s)
\]
is a homotopy from \(f\) to the constant map \(c_{f(0)}\), and similarly \(g\simeq c_{g(0)}\). The constants \(c_{f(0)}\) and \(c_{g(0)}\) are homotopic by
\[
A(s,t)=\alpha(t),
\]
independent of \(s\). Hence
\[
f\simeq c_{f(0)}\simeq c_{g(0)}\simeq g.
\]
Therefore \([I,Y]\) also has a single element.
:::
