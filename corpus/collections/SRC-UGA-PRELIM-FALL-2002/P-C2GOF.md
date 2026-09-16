---
schema: qual/card@1
id: P-C2GOF
kind: problem
title: Continuity of a composition $g\circ f$ at a point
classification:
  areas:
  - prelim
  topics:
  - Continuity
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
For a function $f: \mathbb{R} \to \mathbb{R}$, give the definition of continuity of $f$ at a point $a$.
For functions $f$ and $g$ from $\mathbb{R}$ to $\mathbb{R}$, prove that if $f$ is continuous at $a$ and $g$ is continuous at $b = f(a)$, then $g \circ f$ is continuous at $a$.
[The composition $g \circ f$ is defined by $(g \circ f)(x) = g(f(x))$ for $x \in \mathbb{R}$.]
:::

::: {.solution}
A function $f:\mathbb R\to\mathbb R$ is continuous at $a$ if for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
|x-a|<\delta\quad\Longrightarrow\quad |f(x)-f(a)|<\varepsilon.
\]

Assume $f$ is continuous at $a$ and $g$ is continuous at $b=f(a)$. Let $\varepsilon>0$. By continuity of $g$ at $b$, choose $\eta>0$ such that
\[
|y-b|<\eta\quad\Longrightarrow\quad |g(y)-g(b)|<\varepsilon.
\]
By continuity of $f$ at $a$, choose $\delta>0$ such that
\[
|x-a|<\delta\quad\Longrightarrow\quad |f(x)-f(a)|<\eta.
\]
Hence, if $|x-a|<\delta$, then
\[
|g(f(x))-g(f(a))|<\varepsilon.
\]
Therefore $g\circ f$ is continuous at $a$.
:::
