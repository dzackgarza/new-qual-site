---
schema: qual/card@1
id: E-JY5OT
kind: problem
title: Reverse triangle inequality, $\sup$ and $\inf$, and the Archimedean property
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Derive the reverse triangle inequality from the triangle inequality.

- Let $E\subseteq \RR$.
  Define $\sup E$ and $\inf E$.

- What is the **Archimedean** property?
:::

::: {.solution}
(a) In a normed space, $\big||x| - |y|\big| \le |x - y|$.

::: pf

::: {.pf-step #s1}
$|x| - |y| \le |x - y|$.

::: pf-proof
The triangle inequality applied to $x = (x - y) + y$ gives $|x| \le |x - y| + |y|$.
:::

:::

::: {.pf-step #s2}
$|y| - |x| \le |x - y|$.

::: pf-proof
The triangle inequality applied to $y = (y - x) + x$ gives $|y| \le |y - x| + |x|$, and $|y - x| = |x - y|$.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} bound both $|x| - |y|$ and its negative by $|x - y|$.
:::

:::

(b) Let $E \subseteq \RR$ be nonempty. If $E$ is bounded above, $\sup E$ is the real number $s$ such that $x \le s$ for all $x \in E$, and $s \le t$ for every $t$ with $x \le t$ for all $x \in E$; equivalently, $s$ is an upper bound and for every $\eps > 0$ there is $x \in E$ with $x > s - \eps$. By completeness of $\RR$ it exists. If $E$ is not bounded above, $\sup E = +\infty$. Similarly $\inf E$ is the greatest lower bound of $E$, or $-\infty$ if $E$ is not bounded below, and $\inf E = -\sup(-E)$.

(c) The Archimedean property: for every $x \in \RR$ there is $n \in \NN$ with $n > x$. Equivalently, for every $\eps > 0$ there is $n \in \NN$ with $1/n < \eps$.

::: {.proof}
Suppose no $n \in \NN$ exceeds $x$. Then $\NN$ is bounded above, so by completeness it has a least upper bound $s$. Since $s - 1$ is not an upper bound, some $n \in \NN$ has $n > s - 1$, so $n + 1 > s$ with $n + 1 \in \NN$, contradicting that $s$ is an upper bound.
:::
:::
