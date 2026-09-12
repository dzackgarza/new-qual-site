---
schema: qual/card@1
id: E-PER08-3.5
kind: problem
title: Rectangular subdivision lemma for a homotopy
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 3.5 and Lemma 3.7 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
---

::: {.problem}
Suppose $X=U\cup V$, where $U$ and $V$ are open, and let
\[
\Gamma=\{\gamma_t\}_{t\in[0,1]}:I\times I\to X
\]
be a homotopy of based paths $(I,\partial I)\to(X,x)$.

Prove that there are increasing sequences
\[
0=t_0<t_1<\cdots<t_m=1,
\qquad
0=s_0<s_1<\cdots<s_n=1,
\]
such that $\Gamma$ maps every rectangle
\[
[t_i,t_{i+1}]\times[s_j,s_{j+1}]
\]
entirely into $U$ or entirely into $V$.
Moreover, show that the sequence $(s_j)$ can be chosen to refine prescribed subdivisions of $\gamma_0$ and $\gamma_1$.
:::
