---
schema: qual/card@1
id: P-SQUAL2-01
kind: problem
title: Closure of an arbitrary union versus the union of the closures
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\{A_\alpha\}$ be a collection of subsets of a topological space $X$.
Determine whether
$$\overline{\bigcup_\alpha A_\alpha}=\bigcup_\alpha\overline{A_\alpha}$$
must hold. If equality can fail, determine which inclusion, if either, always holds.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every index $\alpha$,
$$
A_\alpha
\subseteq
\bigcup_\beta A_\beta.
$$


::: pf-proof

This is the defining property of a union.

:::

:::

::: {.pf-step #s1-2}

Taking closures,
$$
\boxed{
\overline{A_\alpha}
\subseteq
\overline{\bigcup_\beta A_\beta}}
$$
for every $\alpha$.


::: pf-proof

Closure is monotone: if $A\subseteq B$, then $\overline A\subseteq\overline B$.
Apply this to step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\bigcup_\alpha\overline{A_\alpha}
\subseteq
\overline{\bigcup_\alpha A_\alpha}}.
$$


::: pf-proof

Every set $\overline{A_\alpha}$ is contained in the right-hand side by step [](#s1-2){.pf-ref}, so their union is also contained there.

:::

:::

::: pf-step

Each $A_n$ is closed.


::: pf-proof

Singletons are closed in the Hausdorff space $\RR$.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\overline{A_n}=A_n}.
$$


::: pf-proof

The closure of a closed set is itself.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\bigcup_{n=1}^{\infty}\overline{A_n}
=
\left\{\frac1n:n\ge1\right\}}.
$$


::: pf-proof

Use step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The point $0$ belongs to
$$
\overline{\bigcup_{n=1}^{\infty}A_n}.
$$


::: pf-proof

Every open interval around $0$ contains $1/n$ for all sufficiently large $n$, since $1/n\to0$.

:::

:::

::: {.pf-step #s1-8}

But
$$
0\notin
\bigcup_{n=1}^{\infty}\overline{A_n}.
$$


::: pf-proof

The right-hand side is exactly the set of positive numbers $1/n$ by step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Thus the inclusion in step [](#s1-3){.pf-ref} can be strict.


::: pf-proof

Steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} show that $0$ belongs to the right-hand side but not the left-hand side.

:::

:::

::: {.pf-step #s1-10}

Hence the correct general statement is
$$
\boxed{
\bigcup_\alpha\overline{A_\alpha}
\subseteq
\overline{\bigcup_\alpha A_\alpha},
}
$$
and equality need not hold.


::: pf-proof

The inclusion is step [](#s1-3){.pf-ref}, and strictness is step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} gives the complete answer.

:::

:::

:::
