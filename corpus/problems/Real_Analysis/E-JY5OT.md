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
(a) Derive the reverse triangle inequality from the triangle inequality.

(b) Let $E\subseteq \RR$.
Define $\sup E$ and $\inf E$.

(c) What is the **Archimedean** property?
:::

::: {.solution}

::: pf

::: pf-step

(a) In a normed space, $\abs{\norm{x} - \norm{y}} \le \norm{x - y}$.

::: pf-proof

::: {.pf-step #s1}

$\norm{x} - \norm{y} \le \norm{x - y}$.

::: pf-proof

The triangle inequality applied to $x = (x - y) + y$ gives $\norm{x} \le \norm{x - y} + \norm{y}$.

:::

:::

::: {.pf-step #s2}

$\norm{y} - \norm{x} \le \norm{x - y}$.

::: pf-proof

The triangle inequality applied to $y = (y - x) + x$ gives $\norm{y} \le \norm{y - x} + \norm{x}$, and $\norm{y - x} = \norm{x - y}$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} bound both $\norm{x} - \norm{y}$ and its negative by $\norm{x - y}$.

:::

:::

:::

::: pf-step

(b) For nonempty $E \subseteq \RR$ bounded above, $\sup E$ is the real number $s$ such that $x \le s$ for all $x \in E$, and $s \le t$ for every $t$ with $x \le t$ for all $x \in E$; equivalently, $s$ is an upper bound of $E$ and for every $\varepsilon > 0$ there is $x \in E$ with $x > s - \varepsilon$. If $E$ is not bounded above, $\sup E = +\infty$. Dually, $\inf E$ is the greatest lower bound of $E$, or $-\infty$ if $E$ is not bounded below, and $\inf E = -\sup(-E)$.

::: pf-proof

The least upper bound exists by the completeness axiom of $\RR$. The two descriptions agree: if $s$ is the least upper bound and $\varepsilon > 0$, then $s - \varepsilon$ is not an upper bound, so some $x \in E$ exceeds it; conversely, if an upper bound $t$ satisfied $t < s$, taking $\varepsilon = s - t$ gives $x \in E$ with $x > t$. The identity $\inf E = -\sup(-E)$ holds because $x \mapsto -x$ reverses the order and exchanges upper and lower bounds.

:::

:::

::: pf-step

(c) The Archimedean property: for every $x \in \RR$ there is $n \in \NN$ with $n > x$; equivalently, for every $\varepsilon > 0$ there is $n \in \NN$ with $1/n < \varepsilon$. It holds in $\RR$.

::: pf-proof

Suppose no $n \in \NN$ exceeds $x$. Then $\NN$ is bounded above, so by completeness it has a least upper bound $s$. Since $s - 1$ is not an upper bound, some $n \in \NN$ has $n > s - 1$, so $n + 1 > s$ with $n + 1 \in \NN$, contradicting that $s$ is an upper bound. The second form follows by applying the first to $x = 1/\varepsilon$.

:::

:::

:::

:::
