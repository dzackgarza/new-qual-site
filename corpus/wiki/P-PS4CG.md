---
schema: qual/card@1
id: P-PS4CG
kind: problem
title: "Since $n_p \\neq 1$ by assumption, we must have $n_p = q$. Now conside\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

Since $n_p \neq 1$ by assumption, we must have $n_p = q$.
Now consider sub-cases for $n_q$:

- $n_q = p$: If $n_q = p = 1 \mod q$ and $p < q$, this forces $p=1$.

- $n_q = p^2$: We will reach a contradiction by showing that this forces
  $$
  \abs{P \definedas \union_{S_p \in \mathrm{Syl}(p, G)} S_p\setminus\theset{e}} + \abs{ Q \definedas \union_{S_q \in \mathrm{Syl}(q, G)} S_q\setminus\theset{e}} + \abs{\theset{e}} > \abs{G}.
  $$
  We have
  \[
  \begin{align*}
  \abs{P} + \abs{Q} + \abs{\theset{e}} &= n_p(q-1) + n_q(p^2 - 1) + 1 \\
  &= p^2(q-1) + q(p^2 - 1) + 1 \\
  &= p^2(q-1) + 1(p^2 - 1) + (q-1)(p^2-1) + 1 \quad\quad \text{(since $q > 1$) } \\
  &= (p^2q - p^2) + (p^2 - 1)  + (q-1)(p^2-1) + 1\\
  &= p^2q + (q-1)(p^2-1) \\
  &\geq p^2 q + (2-1)(2^2-1) \quad\quad\text{(since $p, q \geq 2$)} \\
  &= p^2 q + 3  \\
  &> p^2q = \abs{G}
  ,\end{align*}
  \]
  which is a contradiction.
  $\qed$
