---
schema: qual/card@1
id: E-FB9OZ
kind: problem
title: Closure of the eventually-zero sequences in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Closure
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 5, printed p. 127, with the uniform
    metric of printed p. 124; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.5, PDF p. 19. The closure of the eventually-
    zero sequences in the uniform topology is the set of sequences converging to 0: a
    sequence not converging to 0 has infinitely many entries bounded away from 0, no
    eventually-zero sequence can come within epsilon of it, and a sequence converging to 0
    is approximated by its truncation. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $\RR^\infty$ be the subset of $\RR^\omega$ consisting of all sequences that are eventually zero.
What is the closure of $\RR^\infty$ in $\RR^\omega$ in the uniform topology?
Justify your answer.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.5, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the answer and both inclusions are theirs.

**The closure of $\RR^{\infty}$ in the uniform topology is the set of all sequences that converge to $0$.**

Let $\mathbf{x}\in\RR^{\omega}$ and recall $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i}\min\{\abs{x_{i}-y_{i}},1\}$.

*If $\mathbf{x}$ is a limit of eventually-zero sequences, then $x_{i}\to0$.* Suppose not: then there are $\delta>0$ and indices $i_{1}<i_{2}<\cdots$ with $\abs{x_{i_{n}}}>\delta$. Taking $\varepsilon=\min\{1,\delta\}/2$, no eventually-zero $\mathbf{y}$ can satisfy $\bar\rho(\mathbf{x},\mathbf{y})<\varepsilon$: at each of the infinitely many indices $i_{n}$ one has either $y_{i_{n}}=0$ and $\min\{\abs{x_{i_{n}}},1\}>\varepsilon$, or $y_{i_{n}}\ne0$ for infinitely many $n$, which contradicts $\mathbf{y}$ being eventually zero. So the ball of radius $\varepsilon$ around $\mathbf{x}$ misses $\RR^{\infty}$ and $\mathbf{x}$ is not in its closure.

*If $x_{i}\to0$, then $\mathbf{x}$ is in the closure.* Let $0<\varepsilon<1$; choose $N$ with $\abs{x_{i}}<\varepsilon$ for $i\ge N$, and define $\mathbf{y}$ by $y_{i}=x_{i}$ for $i<N$ and $y_{i}=0$ for $i\ge N$. Then $\mathbf{y}\in\RR^{\infty}$ and $\bar\rho(\mathbf{x},\mathbf{y})=\sup_{i\ge N}\abs{x_{i}}\le\varepsilon$. So every ball around $\mathbf{x}$ meets $\RR^{\infty}$, as required.
:::
