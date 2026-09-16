---
schema: qual/card@1
id: P-NORI-GT-3-04
kind: problem
title: Towers of quadratic extensions of $\mathbb F_p$ for $p\equiv 3 \pmod 4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.4 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of Problem 3.3, on which this problem depends, from p. 1-2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
Problem 3.3 reads: Let $p$ be a prime which is $\equiv 1 \bmod 2^k$, but not congruent to $1$ modulo a higher power of $2$.
Assume $k \geq 2$.
Assume that $u_0 \in \mathbb{F}_p$ is not a square.
Construct a sequence of pairs $(E_n, u_n)$ where $E_n$ is a field and $u_n \in E_n$ as follows.
Define $(E_0, u_0) = (\mathbb{F}_p, u_0)$.
Assume that $(E_n, u_n)$ has been defined.
Let $E_{n+1}$ be a field extension of $E_n$ obtaing by adjoining a square-root $u_{n+1}$ of $u_n \in E_n$.
Show that $\deg(E_n/E_{n-1}) = 2$ for all $n > 0$.

Explain how you would construct a sequence of quadratic extensions when $k = 1$ in the previous problem.
:::
