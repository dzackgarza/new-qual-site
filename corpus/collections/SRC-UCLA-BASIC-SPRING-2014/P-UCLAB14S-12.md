---
schema: qual/card@1
id: P-UCLAB14S-12
kind: problem
title: No countable partition of the unit interval into nonempty closed intervals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 12. Assume
\[
[0,1]=\bigcup_{n=1}^\infty I_n,
\qquad I_n=[a_n,b_n]\neq\varnothing,
\]
and
\[
I_n\cap I_m=\varnothing
\]
whenever $n\neq m$.

(a) Let
\[
E=\{a_n:n\geq1\}\cup\{b_n:n\geq1\}
\]
be the set of endpoints of the intervals above.
Prove that $E$ is closed.

(b) Prove that no such family of intervals $\{I_n\}$ can exist.
:::

::: {.solution}

Assume throughout that the displayed family exists.

::: pf

::: {.pf-step #s1-1}

If $x\in[0,1]\setminus E$, then $x$ lies in the interior of the unique interval $I_k$ containing it.


::: pf-proof

The intervals cover $[0,1]$, so $x\in I_k=[a_k,b_k]$ for some $k$. Pairwise disjointness makes $k$ unique. Since $x\notin E$, it is neither $a_k$ nor $b_k$, hence
\[
a_k<x<b_k.
\]

:::

:::

::: {.pf-step #s1-2}

There exists $\varepsilon>0$ such that
\[
(x-\varepsilon,x+\varepsilon)\cap[0,1]\subset I_k.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, both $x-a_k$ and $b_k-x$ are positive. Take
\[
\varepsilon<\min\{x-a_k,b_k-x\}.
\]
Then every point of the indicated neighborhood lies strictly between $a_k$ and $b_k$.

:::

:::

::: {.pf-step #s1-3}

This neighborhood contains no point of $E$.


::: pf-proof

Suppose an endpoint $a_m$ or $b_m$ lay strictly inside $I_k$. It belongs to $I_m$ as well as $I_k$, so $I_m\cap I_k\ne\varnothing$. Pairwise disjointness forces $m=k$, but the endpoints of $I_k$ are outside the neighborhood chosen in step [](#s1-2){.pf-ref}. Contradiction.

:::

:::

::: {.pf-step #s1-4}

Therefore $[0,1]\setminus E$ is open in $[0,1]$, so
\[
\boxed{E\text{ is closed in }[0,1].}
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give every point of the complement a relative open neighborhood contained in the complement.

:::

:::

::: {.pf-step #s1-5}

The set $E$ is countable, closed, and nonempty, so it has an isolated point $e$.


::: pf-proof

It is countable by definition and closed by step [](#s1-4){.pf-ref}. A nonempty countable closed subset of $\RR$ cannot be perfect: every nonempty perfect subset of $\RR$ is uncountable (construct a binary tree of nested disjoint intervals meeting the set). Hence $E$ has an isolated point.

:::

:::

::: {.pf-step #s1-6}

An isolated endpoint $e\in(0,1)$ is impossible.


::: pf-proof

Choose $\delta>0$ with
\[
E\cap(e-\delta,e+\delta)=\{e\}.
\]
Take $x\in(e-\delta,e)$ and let $I_j$ contain $x$. Since $x\notin E$, step [](#s1-1){.pf-ref} says $x$ lies in the interior of $I_j$. No endpoint lies between $x$ and $e$, so the interval property and the covering force $I_j$ to extend to $e$; because $I_j$ is closed, $e\in I_j$. The same argument with $y\in(e,e+\delta)$ produces an interval $I_k$ containing $e$. These intervals are distinct because one contains points below $e$ and the other points above $e$ while neither can cross $e$ without containing both sides. Thus $I_j\cap I_k$ contains $e$, contradicting pairwise disjointness.

:::

:::

::: {.pf-step #s1-7}

Neither $0$ nor $1$ can be an isolated point of $E$.


::: pf-proof

Suppose $0$ were isolated. Choose $\delta>0$ with $E\cap[0,\delta)=\{0\}$. For any $x\in(0,\delta)$, the interval containing $x$ has no endpoint between $0$ and $x$, so closedness and the interval property force it to contain $0$. Hence it is the same interval as the one containing $0$, and it contains $[0,\delta)$. Its right endpoint is then a point of $E$ different from $0$, so it cannot lie in $[0,\delta)$; consequently this one interval extends past $\delta$. Repeating the same argument up to its right endpoint shows that if that endpoint were $<1$, points immediately to its right would force a second interval to meet it, contradicting disjointness. Thus the interval is $[0,1]$, leaving no room for the other nonempty $I_n$. Contradiction. The argument at $1$ is symmetric.

:::

:::

::: {.pf-step #s1-8}

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} contradict each other. Therefore no such countably infinite family exists.


::: pf-proof

Step [](#s1-5){.pf-ref} produces an isolated point of $E$. Steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} exclude every possible location for such a point in $[0,1]$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
