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

<1>1. If $x\in[0,1]\setminus E$, then $x$ lies in the interior of the unique interval $I_k$ containing it.

::: {.proof}
The intervals cover $[0,1]$, so $x\in I_k=[a_k,b_k]$ for some $k$. Pairwise disjointness makes $k$ unique. Since $x\notin E$, it is neither $a_k$ nor $b_k$, hence
\[
a_k<x<b_k.
\]
:::

<1>2. There exists $\varepsilon>0$ such that
\[
(x-\varepsilon,x+\varepsilon)\cap[0,1]\subset I_k.
\]

::: {.proof}
By step <1>1, both $x-a_k$ and $b_k-x$ are positive. Take
\[
\varepsilon<\min\{x-a_k,b_k-x\}.
\]
Then every point of the indicated neighborhood lies strictly between $a_k$ and $b_k$.
:::

<1>3. This neighborhood contains no point of $E$.

::: {.proof}
Suppose an endpoint $a_m$ or $b_m$ lay strictly inside $I_k$. It belongs to $I_m$ as well as $I_k$, so $I_m\cap I_k\ne\varnothing$. Pairwise disjointness forces $m=k$, but the endpoints of $I_k$ are outside the neighborhood chosen in step <1>2. Contradiction.
:::

<1>4. Therefore $[0,1]\setminus E$ is open in $[0,1]$, so
\[
\boxed{E\text{ is closed in }[0,1].}
\]

::: {.proof}
Steps <1>1--<1>3 give every point of the complement a relative open neighborhood contained in the complement.
:::

<1>5. The set $E$ is countable, closed, and nonempty, so it has an isolated point $e$.

::: {.proof}
It is countable by definition and closed by step <1>4. A nonempty countable closed subset of $\mathbb R$ cannot be perfect: every nonempty perfect subset of $\mathbb R$ is uncountable (construct a binary tree of nested disjoint intervals meeting the set). Hence $E$ has an isolated point.
:::

<1>6. An isolated endpoint $e\in(0,1)$ is impossible.

::: {.proof}
Choose $\delta>0$ with
\[
E\cap(e-\delta,e+\delta)=\{e\}.
\]
Take $x\in(e-\delta,e)$ and let $I_j$ contain $x$. Since $x\notin E$, step <1>1 says $x$ lies in the interior of $I_j$. No endpoint lies between $x$ and $e$, so the interval property and the covering force $I_j$ to extend to $e$; because $I_j$ is closed, $e\in I_j$. The same argument with $y\in(e,e+\delta)$ produces an interval $I_k$ containing $e$. These intervals are distinct because one contains points below $e$ and the other points above $e$ while neither can cross $e$ without containing both sides. Thus $I_j\cap I_k$ contains $e$, contradicting pairwise disjointness.
:::

<1>7. Neither $0$ nor $1$ can be an isolated point of $E$.

::: {.proof}
Suppose $0$ were isolated. Choose $\delta>0$ with $E\cap[0,\delta)=\{0\}$. For any $x\in(0,\delta)$, the interval containing $x$ has no endpoint between $0$ and $x$, so closedness and the interval property force it to contain $0$. Hence it is the same interval as the one containing $0$, and it contains $[0,\delta)$. Its right endpoint is then a point of $E$ different from $0$, so it cannot lie in $[0,\delta)$; consequently this one interval extends past $\delta$. Repeating the same argument up to its right endpoint shows that if that endpoint were $<1$, points immediately to its right would force a second interval to meet it, contradicting disjointness. Thus the interval is $[0,1]$, leaving no room for the other nonempty $I_n$. Contradiction. The argument at $1$ is symmetric.
:::

<1>8. Steps <1>5--<1>7 contradict each other. Therefore no such countably infinite family exists.

::: {.proof}
Step <1>5 produces an isolated point of $E$. Steps <1>6 and <1>7 exclude every possible location for such a point in $[0,1]$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>4 proves part (a), and step <1>8 proves part (b).
:::
:::
