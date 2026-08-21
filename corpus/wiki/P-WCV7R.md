---
schema: qual/card@1
id: P-WCV7R
kind: problem
title: $\CC[x,y]$ is not a PID
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Polynomials
  - Ideals
relations: []
review: draft
solved: true
---

Give a careful proof that $\CC[x, y]$ is not a PID.

::: {.concept}
\envlist

- If $R[x]$ is a PID, then $R$ is a field (not explicitly used).

- In $P \da R[x_1, \cdots, x_n]$, there are degree functions $\deg_{x_n}: P\to \ZZ_{\geq 0}$.
:::

::: {.solution}
\envlist

- The claim is that $I \da \gens{x, y}$ is not principal.

- Toward a contradiction, if so, then $\gens{x, y} = \gens{f}$.

- So write $x = fg$ for some $g\in \CC[x, y]$, then

  - $\deg_x(x) = 1$, so $\deg_x(fg) = 1$ which forces $\deg_x(f) \leq 1$.

  - $\deg_y(y) = 1$, so $\deg_y(fg) = 1$ which forces $\deg_y(f) \leq 1$.

  - So $f(x, y) = ax + by + c$ for some $a,b,c\in \CC$.

  - $\deg_x(y) = 0$ and thus $\deg_x(fg) = 0$, forcing $a=0$

  - $\deg_y(x) = 0$ and thus $\deg_y(fg) = 0$, forcing $b=0$

  - So $f(x, y) = c \in \CC$.

- But $\CC[x]$ is a field, so $c$ is a unit in $\CC$ and thus $\CC[x, y]$, so $\gens{f} = \gens{c} = \CC[x, y]$.

- This is a contradiction, since $1\not\in \gens{x, y}$:

  - Every element in $\alpha(x, y) \in\gens{x, y}$ is of the form $\alpha(x, y) = xp(x, y) + yq(x, y)$.

  - But $\deg_x(\alpha) \geq 1, \deg_y(\alpha)\geq 1$, while $\deg_x(1) = \deg_y(1) = 0$.

  - So $\gens{x, y} \neq \CC[x, y]$.

- Alternatively, $\gens{x, y}$ is proper since $\CC[x, y] / \gens{x, y} \cong \CC \neq \CC[x, y]$.
:::
