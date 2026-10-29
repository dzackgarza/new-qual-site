---
schema: qual/card@1
id: P-WESRA10-II2
kind: problem
title: 'Rational translation invariance extends to all real translations'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $\mu$ be a Borel measure on $\RR$ such that every bounded interval has finite measure and
\[
\mu(I)=\mu(I+r)
\]
for every bounded interval $I$ and rational $r$.

(a) Prove $\mu(\{x\})=0$ for every $x\in\RR$.

(b) Prove $\mu(I)=\mu(I+a)$ for every bounded interval $I$ and every real $a$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $x\in\RR$ and every rational $r$,
\[
\mu(\{x\})=\mu(\{x+r\}).
\]


::: pf-proof

For $n\ge1$, let
\[
I_n=(x-1/n,x+1/n).
\]
Then $(I_n)$ decreases to $\{x\}$ and $\mu(I_1)<\infty$. By continuity from
above,
\[
\mu(\{x\})=\lim_{n\to\infty}\mu(I_n).
\]
By rational translation invariance,
\[
\mu(I_n)=\mu(I_n+r).
\]
The intervals $(I_n+r)$ decrease to $\{x+r\}$, so another application of
continuity from above gives
\[
\mu(\{x+r\})=\lim_{n\to\infty}\mu(I_n+r)
=\lim_{n\to\infty}\mu(I_n)
=\mu(\{x\}).
\]

:::

:::

::: {.pf-step #s1-2}

For every $x\in\RR$,
\[
\boxed{\mu(\{x\})=0}.
\]


::: pf-proof

Fix $x$ and set
\[
c=\mu(\{x\}).
\]
Choose distinct rational numbers
\[
r_1,r_2,\dots\in[0,1].
\]
By step [](#s1-1){.pf-ref},
\[
\mu(\{x+r_k\})=c
\]
for every $k$. These singleton sets are pairwise disjoint and all lie in the
bounded interval $[x,x+1]$. Hence for every $N$,
\[
\mu([x,x+1])
\ge
\sum_{k=1}^N\mu(\{x+r_k\})
=Nc.
\]
The left-hand side is finite, so $c=0$.

:::

:::

::: {.pf-step #s1-3}

For every $y\in\RR$,
\[
\lim_{\delta\downarrow0}\mu((y-\delta,y+\delta))=0.
\]


::: pf-proof

For any sequence $\delta_n\downarrow0$, the intervals
\[
(y-\delta_n,y+\delta_n)
\]
decrease to $\{y\}$ and the first has finite measure. Continuity from above
and step [](#s1-2){.pf-ref} give
\[
\lim_{n\to\infty}\mu((y-\delta_n,y+\delta_n))
=\mu(\{y\})
=0.
\]
Since this holds for every sequence $\delta_n\downarrow0$, the displayed
one-sided limit is $0$.

:::

:::

::: {.pf-step #s1-4}

Let $I$ be a bounded interval and let $r_n\in\QQ$ satisfy
\[
r_n\to a\in\RR.
\]
Then
\[
\mu(I+r_n)\to\mu(I+a).
\]


::: pf-proof

Write the endpoints of $I$ as $u<v$. Because singletons have measure zero by
step [](#s1-2){.pf-ref}, the measure of an interval is unchanged by adding or removing its
endpoints. Thus it is enough to compare the open intervals
\[
(u+r_n,v+r_n)
\qquad\text{and}\qquad
(u+a,v+a).
\]
Their symmetric difference is contained in the union of two intervals whose
lengths are at most $|r_n-a|$, one near $u+a$ and one near $v+a$.
By step [](#s1-3){.pf-ref}, the measures of those two endpoint intervals tend to $0$.
Therefore
\[
\mu\bigl((I+r_n)\triangle(I+a)\bigr)\to0.
\]
Since
\[
|\mu(I+r_n)-\mu(I+a)|
\le
\mu\bigl((I+r_n)\triangle(I+a)\bigr),
\]
the desired convergence follows.

:::

:::

::: {.pf-step #s1-5}

For every bounded interval $I$ and every real $a$,
\[
\boxed{\mu(I)=\mu(I+a)}.
\]


::: pf-proof

Choose rationals $r_n\to a$. By hypothesis,
\[
\mu(I+r_n)=\mu(I)
\]
for every $n$. Step [](#s1-4){.pf-ref} gives
\[
\mu(I+a)
=\lim_{n\to\infty}\mu(I+r_n)
=\mu(I).
\]

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
