---
schema: qual/card@1
id: P-WESRA15-3
kind: problem
title: 'A one-neighborhood of a measurable subset of the line is measurable'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $A\subset\mathbb R$ be Lebesgue measurable.
Prove that
\[
B=\bigcup_{x\in A}[x-1,x+1]
\]
is Lebesgue measurable.
:::

::: {.solution}
For each $q\in\QQ$, define
$$
B_q
=
\bigcup_{\substack{x\in A\\ q\in(x-1,x+1)}}[x-1,x+1].
$$
If there is no such $x$, set $B_q=\varnothing$.

<1>1. For every $q\in\QQ$, the set $B_q$ is an interval, or is empty.

::: {.proof}
Every interval appearing in the union defining $B_q$ contains the common point $q$. Let $u<v$ belong to $B_q$, and let $w\in(u,v)$. Choose contributing intervals $I_u,I_v$ with
$$
u,q\in I_u,
\qquad
q,v\in I_v.
$$
If $w\le q$, then $u\le w\le q$, so $w\in I_u$. If $w\ge q$, then $q\le w\le v$, so $w\in I_v$. Thus every point between two points of $B_q$ also lies in $B_q$, and $B_q$ is an interval whenever it is nonempty.
:::

<1>2. Each $B_q$ is a Borel subset of $\RR$.

::: {.proof}
Every interval in $\RR$—bounded or unbounded, with any choice of included endpoints—is Borel. The empty set is also Borel. Apply step <1>1.
:::

<1>3. One has
$$
B=\bigcup_{q\in\QQ}B_q.
$$

::: {.proof}
If $y\in B_q$ for some rational $q$, then by definition $y$ belongs to an interval $[x-1,x+1]$ with $x\in A$, so $y\in B$. Hence
$$
\bigcup_{q\in\QQ}B_q\subseteq B.
$$

Conversely, let $y\in B$. Then there is $x\in A$ such that
$$
y\in[x-1,x+1].
$$
The open interval $(x-1,x+1)$ is nonempty, so it contains some rational number $q$. For this $q$, the interval $[x-1,x+1]$ occurs in the union defining $B_q$. Hence $y\in B_q$, proving the reverse inclusion.
:::

<1>4. The set $B$ is Lebesgue measurable.

::: {.proof}
The rationals are countable. By steps <1>2--<1>3, $B$ is a countable union of Borel sets, hence is Borel. Every Borel subset of $\RR$ is Lebesgue measurable.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion. The argument actually does not require the hypothesis that $A$ itself is measurable.
:::
:::
