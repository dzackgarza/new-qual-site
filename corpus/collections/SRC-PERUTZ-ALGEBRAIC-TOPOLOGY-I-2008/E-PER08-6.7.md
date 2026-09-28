---
schema: qual/card@1
id: E-PER08-6.7
kind: problem
title: The doubled full rotation loop in $SO(3)$ is nullhomotopic
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 6.7 of the Perutz 2008 notes.
---

::: {.problem}
Rotation about a fixed axis, by angles increasing from $0$ up to $2\pi$, determines a loop $\gamma$ in $SO(3)$.
Show that $\gamma*\gamma$ is nullhomotopic.
:::

::: {.solution}
Use the double covering
\[
SU(2)\cong S^3\longrightarrow SO(3).
\]
A rotation through angles from $0$ to $2\pi$ about a fixed axis lifts to a path in $SU(2)$ beginning at $1$ and ending at $-1$.
Consequently the concatenated loop $\gamma*\gamma$ lifts to a closed loop beginning and ending at $1$ (the second traverse continues from $-1$ back to $1$).

Since $SU(2)\cong S^3$ is simply connected, that lifted loop is null-homotopic.
Projecting its null-homotopy to $SO(3)$ shows that
\[
\boxed{\gamma*\gamma\simeq *}.
\]
Equivalently, $[\gamma]$ is the nontrivial element of $\pi_1(SO(3))\cong\mathbb Z/2$.
:::
