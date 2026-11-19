---
schema: qual/card@1
id: P-BKS04-4B
kind: problem
title: Unique maximum of $\log\prod x_i$ on the simplex $\sum a_ix_i=1$, $x_i>0$
classification:
  areas: [prelim]
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Spring
    2004, solutions, assets/attachments/s04solution.pdf, Problem 4B on PDF p. 7 — and
    restructured into steps; the card's prose was that sheet's two arguments. Both routes are
    kept. Added: the check that the candidate point lies in Delta and that Delta is bounded in
    each coordinate, and the explicit statement that equality in AM-GM characterises the
    maximiser, which the sheet stated in one sentence.
---

::: {.problem}
Let $a_1,\ldots,a_n$ be positive real numbers.
Let $\Delta$ be the set of points $\mathbf x\in\RR^n$ satisfying the conditions

$$
\sum_{i=1}^na_ix_i=1,\quad x_i>0\text{ for all }i.
$$

Prove that the function $\log\left(\prod_{i=1}^nx_i\right)$ has a unique maximum on $\Delta$ and find the point where it occurs.
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Spring 2004, solutions** (`assets/attachments/s04solution.pdf`), Problem 4B, PDF p. 7, which gives both a Lagrange-multiplier and an AM-GM route. Throughout $a_{1},\ldots,a_{n} > 0$, $\Delta = \theset{\mathbf{x} \in \RR^{n} \mid \sum_{i}a_{i}x_{i} = 1,\ x_{i} > 0}$ and $F(\mathbf{x}) \coloneqq \log\bigl(\prod_{i}x_{i}\bigr) = \sum_{i}\log x_{i}$.

::: pf

::: {.pf-step #inside}
The point $\mathbf{p} \coloneqq (1/(na_{1}), \ldots, 1/(na_{n}))$ lies in $\Delta$, and every $\mathbf{x} \in \Delta$ has $x_{i} \le 1/a_{i}$ for all $i$.

::: pf-proof
$\sum_{i}a_{i}p_{i} = \sum_{i}\frac{1}{n} = 1$ and each $p_{i} > 0$, so $\mathbf{p} \in \Delta$. For $\mathbf{x} \in \Delta$ the term $a_{i}x_{i}$ is at most the whole sum $1$, since all terms are positive, so $x_{i} \le 1/a_{i}$.

:::

:::

::: {.pf-step #amgm}
For every $\mathbf{x} \in \Delta$ one has $\prod_{i}x_{i} \le \frac{1}{n^{n}\prod_{i}a_{i}}$, with equality exactly when $a_{i}x_{i} = 1/n$ for all $i$, that is exactly at $\mathbf{x} = \mathbf{p}$.

::: pf-proof
The arithmetic-mean--geometric-mean inequality applied to the $n$ positive numbers $a_{1}x_{1},\ldots,a_{n}x_{n}$ gives $\bigl(\prod_{i}a_{i}x_{i}\bigr)^{1/n} \le \frac{1}{n}\sum_{i}a_{i}x_{i} = \frac{1}{n}$, since $\mathbf{x} \in \Delta$. Raising to the $n$-th power gives $\bigl(\prod_{i}a_{i}\bigr)\bigl(\prod_{i}x_{i}\bigr) \le n^{-n}$, which is the displayed bound. Equality in AM-GM holds exactly when the $n$ numbers are equal, that is when $a_{i}x_{i} = 1/n$ for every $i$, which says $x_{i} = 1/(na_{i})$ for every $i$, and this is the point $\mathbf{p}$ of step [](#inside){.pf-ref}.

:::

:::

::: {.pf-step #log}
For every $\mathbf{x} \in \Delta$ one has $F(\mathbf{x}) \le -n\log n - \sum_{i}\log a_{i}$, with equality exactly at $\mathbf{x} = \mathbf{p}$.

::: pf-proof
$\log$ is strictly increasing and the bound of step [](#amgm){.pf-ref} holds, so $F(\mathbf{x}) = \log\prod_{i}x_{i} \le \log\bigl(1/(n^{n}\prod_{i}a_{i})\bigr) = -n\log n - \sum_{i}\log a_{i}$; strict increase makes the equality cases of the two statements coincide.

:::

:::

::: {.pf-step #lagrange}
A critical point of $F$ on the smooth constraint surface $\Delta$ is $\mathbf{p}$, and $F$ is strictly concave on the convex set $\Delta$.

::: pf-proof
At a constrained critical point $dF = \lambda\\, d\bigl(\sum_{i}a_{i}x_{i}\bigr)$ for some $\lambda$, that is $\sum_{i}\frac{dx_{i}}{x_{i}} = \lambda\sum_{i}a_{i}\\,dx_{i}$ for all $(dx_{i})$, which forces $a_{i} = 1/(\lambda x_{i})$ and so $x_{i} = 1/(\lambda a_{i})$; imposing $\sum_{i}a_{i}x_{i} = 1$ gives $n/\lambda = 1$, that is $\lambda = n$ and $\mathbf{x} = \mathbf{p}$. The Hessian of $F$ is the diagonal matrix with entries $-1/x_{i}^{2}$, negative definite, so $F$ is strictly concave on the convex set $\Delta$.

:::

:::

::: pf-step
$F$ has a unique maximum on $\Delta$, attained at $\boxed{\mathbf{x} = \mathbf{p} = \bigl(1/(na_{1}),\ldots,1/(na_{n})\bigr)}$.

::: pf-proof
Step [](#log){.pf-ref} bounds $F$ on $\Delta$ by a constant and shows the bound is attained exactly at $\mathbf{p}$, which is in $\Delta$ by step [](#inside){.pf-ref}; that is a maximum, and it is unique because equality forces $\mathbf{x} = \mathbf{p}$. Step [](#lagrange){.pf-ref} is the sheet's other route: strict concavity makes any critical point the unique maximiser, and the only critical point is $\mathbf{p}$.

:::

:::

:::
:::
