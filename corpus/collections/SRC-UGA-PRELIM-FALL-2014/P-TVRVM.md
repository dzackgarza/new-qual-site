---
schema: qual/card@1
id: P-TVRVM
kind: problem
title: The sequence $a_{n+1}=\frac{a_n}{3}+5$ with $a_1=1$ is increasing, bounded
  by $10$, and converges to $\frac{15}{2}$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Sequences of Numbers
relations: []
review: draft
---

::: {.problem}
Let $(a_n)$ be a sequence defined recursively by $a_1 = 1$ and $a_{n+1} = \frac{a_n}{3} + 5$ for $n \geq 1$. Prove inductively that $a_n \leq a_{n+1} \leq 10$ for each positive integer $n$. Then explain why the sequence $(a_n)$ converges and find its limit.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own induction is replaced by the clean one, with the invariant $a_{n}\le 15/2$, the monotonicity, the convergence and the limit as separate steps.

Let $a_{1}=1$ and $a_{n+1}=\frac{a_{n}}{3}+5$.

::: pf

::: {.pf-step #fixed}
$L=\frac{15}{2}$ is the unique solution of $L=\frac{L}{3}+5$.

::: pf-proof
$L=\frac L3+5$ is equivalent to $\frac23L=5$, that is $L=\frac{15}{2}$.
:::

:::

::: {.pf-step #invariant}
$a_{n}\le\frac{15}{2}$ for every $n$, and hence $a_{n}\le10$.

::: pf-proof
Induction: $a_{1}=1\le\frac{15}{2}$. If $a_{n}\le\frac{15}{2}$ then $a_{n+1}-\frac{15}{2}=\frac{a_{n}}{3}+5-\frac{15}{2}=\frac{a_{n}}{3}-\frac52=\frac13\big(a_{n}-\frac{15}{2}\big)\le0$, so $a_{n+1}\le\frac{15}{2}$. Since $\frac{15}{2}\le10$, both bounds hold.
:::

:::

::: {.pf-step #monotone}
$a_{n}\le a_{n+1}$ for every $n$.

::: pf-proof
$a_{n+1}-a_{n}=5-\frac{2}{3}a_{n}=\frac23\big(\frac{15}{2}-a_{n}\big)\ge0$ by step [](#invariant){.pf-ref}.
:::

:::

::: {.pf-step #converges}
$(a_{n})$ converges, and its limit is $\frac{15}{2}$.

::: pf-proof
The sequence is nondecreasing by step [](#monotone){.pf-ref} and bounded above by $\frac{15}{2}$ by step [](#invariant){.pf-ref}, so it converges, by the monotone convergence theorem for real sequences (a nondecreasing sequence bounded above converges to its supremum). If $a_{n}\to L$ then the recursion and continuity of $x\mapsto\frac x3+5$ give $L=\frac L3+5$, so $L=\frac{15}{2}$ by step [](#fixed){.pf-ref}.
:::

:::

::: {.pf-qed}
For every positive integer $n$, $a_{n}\le a_{n+1}$ by step [](#monotone){.pf-ref} and $a_{n+1}\le10$ by step [](#invariant){.pf-ref}; the sequence converges to $\frac{15}{2}$ by step [](#converges){.pf-ref}.
:::

:::

:::
