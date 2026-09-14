---
schema: qual/card@1
id: P-WESTOP06-B5
kind: problem
title: Naturality of induced fundamental-group maps under a homotopy
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let
\[
F:X\times I\to Y
\]
be continuous, choose $x_0\in X$, and define
\[
\alpha(t)=F(x_0,t).
\]
Prove that the diagram
\[
\begin{CD}
\pi_1(X,x_0) @>{F(-,1)_*}>> \pi_1(Y,F(x_0,1))\\
@V{F(-,0)_*}VV @VV{\widehat\alpha}V\\
\pi_1(Y,F(x_0,0)) @= \pi_1(Y,F(x_0,0))
\end{CD}
\]
commutes, where $\widehat\alpha$ is the change-of-basepoint map induced by the path $\alpha$.
:::
