---
schema: qual/card@1
id: P-6QWZI
kind: problem
title: Almost uniform boundedness of an a.e. convergent sequence in $L^1$ on a finite
  measure space
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Measure Theory
  - L¹
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2021 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2021.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let \( (X, \mathcal{M}, \mu)  \) be a finite measure space and let \( \ts{ f_n}_{n=1}^{\infty } \subseteq L^1(X, \mu) \). Suppose $f\in L^1(X, \mu)$ such that $f_n(x) \converges{n\to \infty }\to f(x)$ for almost every $x \in X$.
Prove that for every \( \eps > 0 \) there exists $M>0$ and a set $E\subseteq X$ such that \( \mu(E) \leq \eps \) and \( \abs{f_n(x)}\leq M  \) for all $x\in X\sm E$ and all $n\in \NN$.
:::

::: {.solution}

::: pf

::: pf-step
Define $g(x) = \sup_{n \ge 1}|f_n(x)|$ (extended real-valued).

::: pf-proof
$g$ is measurable as the supremum of countably many measurable functions.
:::

:::

::: {.pf-step #g-finite-ae}
$g(x) < \infty$ for almost every $x$.

::: pf-proof
for a.e. $x$, $f_n(x) \to f(x) \in \RR$, so the sequence $(f_n(x))$ is bounded and $\sup_n|f_n(x)| < \infty$.
:::

:::

::: {.pf-step #measure-tail-vanishes}
$\mu\{g > M\} \to 0$ as $M \to \infty$.

::: pf-proof
the sets $\{g > M\}$ decrease to $\{g = \infty\}$ as $M \to \infty$, which has measure $0$ by step [](#g-finite-ae){.pf-ref}; since $\mu(X) < \infty$, continuity from above gives $\mu\{g > M\} \to \mu\{g = \infty\} = 0$.
:::

:::

::: {.pf-step #choose-m-and-e}
Given $\eps > 0$, choose $M$ with $\mu\{g > M\} < \eps$ and set $E = \{g > M\}$; then $\mu(E) \le \eps$ and $|f_n(x)| \le M$ for all $x \in X \setminus E$ and all $n$.

::: pf-proof
Step [](#measure-tail-vanishes){.pf-ref} gives $M$; for $x \notin E$: $g(x) \le M$, so $|f_n(x)| \le g(x) \le M$ for every $n$ by definition of $g$.
:::

:::

::: pf-qed
Step [](#choose-m-and-e){.pf-ref} is exactly the claim. (Only the a.e. convergence and finiteness of $\mu$ are used.)
:::

:::

:::
