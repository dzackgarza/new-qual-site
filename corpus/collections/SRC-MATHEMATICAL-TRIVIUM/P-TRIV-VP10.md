---
schema: qual/card@1
id: P-TRIV-VP10
kind: problem
title: Natural boundary conditions from a boundary term in the functional
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned Variational Principle Problem 10 against page 20 of the source PDF and added a remark on the stray plus sign printed in its boundary condition.
---

::: problem
Consider the following problem
$$
\begin{cases}
F_f - \dfrac{\partial}{\partial x} F_{f_x} - \dfrac{\partial}{\partial y} F_{f_y} = 0, & (x, y) \in D \\
F_{f_x} n_x + F_{f_y} n_y + = g(s), & x \in \partial D,
\end{cases}
\tag{16}
$$
where $f = f(x, y) \in C^2(\bar{D})$, $F = F[f, f_x, f_y](x, y) \in C^2(\mathbb{R}^3 \times \bar{D})$, $g \in C^1(\partial D)$, $\partial/\partial n$ denotes a normal derivative on $\partial D$, $f_x \equiv \frac{\partial f}{\partial x}$ and $F_f \equiv \frac{\partial F}{\partial f}$.

(a) Show that the solutions to this equation are given by extrema of the functional
$$
J[f] = \iint_D dx\,dy\,F - \int_{\partial D} ds\,f g.
\tag{17}
$$

(b) How must the functional above be modified to give the mixed boundary conditions on the function $f$:
$$
F_{f_x} n_x + F_{f_y} n_y + h(s) f = g(s), \quad h \in C^1(\partial D)
\tag{18}
$$
:::

::: {.remark}
Erratum: the boundary condition in (16) is printed in the source as "$F_{f_x} n_x + F_{f_y} n_y + = g(s)$, $x \in \partial D$", with a dangling plus sign.
The condition that makes part (a) true, and that (18) reduces to for $h = 0$, is $F_{f_x} n_x + F_{f_y} n_y = g(s)$ on $\partial D$, where $(n_x, n_y)$ is the outward unit normal and $s$ is arc length along $\partial D$.
:::
