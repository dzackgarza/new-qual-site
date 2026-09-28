---
schema: qual/card@1
id: P-AMH-ALG-SG16-31
kind: problem
title: Reducibility of $x^2+3$ over $\mathbb F_7$ and an intermediate ideal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(March 2008) Let $g(x)=x^2+3\in\mathbb{F}_7[x]$, where $\mathbb{F}_7=\{0,1,2,3,4,5,6\}$ is the field of seven elements.
(a) Prove that $g$ is reducible in $\mathbb{F}_7[x]$.
(b) Let $\langle g\rangle\subseteq\mathbb{F}_7[x]$ denote the principal ideal $\{gh\mid h\in\mathbb{F}_7[x]\}$.
Find an ideal $I\subseteq\mathbb{F}_7[x]$ such that $\langle g\rangle\subsetneq I\subsetneq\mathbb{F}_7[x]$.
:::

::: {.solution}
(a) Evaluating $g$ at the elements of $\FF_7$ gives $g(2)=7=0$, so $x-2$ divides $g$. Long division gives $g(x)=(x-2)(x+2)$, so $g$ is reducible.

(b) Let $I=\langle x-2\rangle\subseteq\FF_7[x]$. Every element of $\langle g\rangle$ has the form $hg$ with $h\in\FF_7[x]$, and $hg=\bigl((x+2)h\bigr)(x-2)\in I$. Thus $\langle g\rangle\subseteq I\subseteq\FF_7[x]$. Moreover $x-2\notin\langle g\rangle$, because a multiple $hg$ of $g$ is either $0$ or has degree $\deg(hg)\ge\deg g=2$, whereas $\deg(x-2)=1$. Finally $1\notin I$, because a multiple $h\cdot(x-2)$ is either $0$ or has degree at least $1$, whereas $\deg 1=0$. Hence $\langle g\rangle\subsetneq I\subsetneq\FF_7[x]$.
:::
