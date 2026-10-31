---
schema: qual/card@1
id: P-PRACT20-W6-11
kind: problem
title: Open, closed and uncountable sets containing $\QQ$
classification:
  areas:
  - prelim
  topics:
  - Topology of the Real Line
  - Lebesgue Measure
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray figure caption from another page and separated the choices, checked against Week6_solns.pdf page 5 (Problem 11).
---

::: {.problem}
Which of the following necessarily holds for $\QQ \subseteq A \subseteq \RR$?

(A) If $A$ is open, then $A = \RR$.

(B) If $A$ is closed, then $A = \RR$.

(C) If $A$ is uncountable, then $A = \RR$.

(D) If $A$ is uncountable, then $A$ is open.

(E) If $A$ is countable, then $A$ is closed.
:::

::: {.solution}
Only (B) necessarily holds.

(A) is false. Enumerate $\QQ=\{q_n\}_{n=1}^\infty$ and let

$$
A=\bigcup_{n=1}^\infty\left(q_n-\frac{1}{2^{n+1}},q_n+\frac{1}{2^{n+1}}\right).
$$

Then $A$ is open and $\QQ\subset A$, but the Lebesgue measure of $A$ satisfies

$$
m(A)\leq\sum_{n=1}^\infty m\left(\left(q_n-\frac{1}{2^{n+1}},q_n+\frac{1}{2^{n+1}}\right)\right)=\sum_{n=1}^\infty\frac{1}{2^n}=1,
$$

whereas $m(\RR)=+\infty$. Thus $A\neq\RR$. Replacing $1/2^{n+1}$ by $\varepsilon/2^{n+1}$ shows that $\QQ$, and any countable set, has Lebesgue measure zero.

(B) is true: a closed set containing $\QQ$ contains its closure $\RR$.

(C) is false: take $A=(0,1)\cup\QQ$.

(D) is false: the same $A=(0,1)\cup\QQ$ is not open, since $2\in A$ but no interval around $2$ lies in $A$.

(E) is false: take $A=\QQ$, which is not closed.
:::
