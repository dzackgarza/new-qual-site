---
schema: qual/card@1
id: P-RHDT6
kind: problem
title: A summable family of positive terms has countable index set; $f(x)=\sum_{q\le
  x}a(q)$ is continuous precisely at irrationals
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the UGA Fall 2014 real-analysis qualifying exam source recorded by this collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $I$ be an index set and let $a:I\to(0,\infty)$.

(a) Show that
\[
\sum_{i\in I}a(i)
:=\sup_{\substack{J\subset I\\J\text{ finite}}}\sum_{i\in J}a(i)<\infty
\quad\Longrightarrow\quad
I\text{ is countable}.
\]

(b) Suppose $I=\mathbb Q$ and $\sum_{q\in\mathbb Q}a(q)<\infty$. Define
\[
f(x):=\sum_{\substack{q\in\mathbb Q\\q\le x}}a(q).
\]
Show that $f$ is continuous at $x$ if and only if $x\notin\mathbb Q$.
:::

::: solution
<1>1. Prove that the index set in part (a) is countable.
::: proof
Put
\[
S:=\sum_{i\in I}a(i)<\infty
\]
and, for $n\ge1$, define
\[
I_n:=\{i\in I:a(i)\ge 1/n\}.
\]
If $J\subset I_n$ is finite, then
\[
\frac{|J|}{n}
\le \sum_{i\in J}a(i)
\le S.
\]
Thus every finite subset of $I_n$ has cardinality at most $nS$, which forces $I_n$ itself to be finite.

Since every $a(i)>0$, for each $i\in I$ there is some $n$ with $a(i)\ge1/n$. Hence
\[
I=\bigcup_{n=1}^\infty I_n.
\]
This is a countable union of finite sets, so $I$ is countable.
:::

<1>2. Show that $f$ is discontinuous at every rational point.
::: proof
Fix $r\in\mathbb Q$. Since $a(r)>0$, for every $y<r$,
\[
f(r)-f(y)
=\sum_{y<q\le r}a(q)
\ge a(r).
\]
Therefore values approaching $r$ from the left remain at least $a(r)$ below $f(r)$. Hence $f$ is not continuous at $r$.
:::

<1>3. Show that $f$ is continuous at every irrational point.
::: proof
Fix $x\notin\mathbb Q$ and $\varepsilon>0$. Since the nonnegative family $(a(q))_{q\in\mathbb Q}$ is summable, there is a finite set $F\subset\mathbb Q$ such that
\[
\sum_{q\in\mathbb Q\setminus F}a(q)<\varepsilon.
\]
Because $x\notin F$ and $F$ is finite, choose $\delta>0$ such that
\[
(x-\delta,x+\delta)\cap F=\varnothing.
\]
If $|y-x|<\delta$, then the rational numbers whose terms contribute to the difference between $f(y)$ and $f(x)$ all lie in $\mathbb Q\setminus F$. Therefore
\[
|f(y)-f(x)|
\le\sum_{q\in\mathbb Q\setminus F}a(q)
<\varepsilon.
\]
Thus $f$ is continuous at $x$.

Combining Steps 2 and 3,
\[
\boxed{f\text{ is continuous at }x\iff x\notin\mathbb Q.}
\]
:::
:::
