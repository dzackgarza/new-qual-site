---
schema: qual/card@1
id: P-DUKEBA14-12
kind: problem
title: Characterization of continuity for a linear map between normed spaces
classification:
  areas: [real-analysis]
  topics: [Normed Spaces, Bounded Linear Operators]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 6 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $L:V_1\to V_2$ be a linear map between normed vector spaces. Prove that $L$ is continuous if and only if there exists $c>0$ such that
\[
\|L(v)\|_{V_2}\le c\|v\|_{V_1}
\qquad\text{for every }v\in V_1.
\]
:::

::: solution
<1>1. A global linear bound implies continuity.
::: proof
If
\[
\|L(v)\|\le c\|v\|
\]
for all $v$, then for $u,v\in V_1$,
\[
\|L(u)-L(v)\|
=\|L(u-v)\|
\le c\|u-v\|.
\]
Thus $L$ is Lipschitz, hence continuous.
:::

<1>2. Continuity at the origin implies a global bound.
::: proof
Assume $L$ is continuous. By continuity at $0$, there exists $\delta>0$ such that
\[
\|w\|<\delta
\quad\Longrightarrow\quad
\|L(w)\|<1.
\]
Let $v\ne0$ and set
\[
w=\frac{\delta}{2\|v\|}v.
\]
Then $\|w\|=\delta/2<\delta$, so $\|L(w)\|<1$. By linearity,
\[
\frac{\delta}{2\|v\|}\|L(v)\|<1,
\]
and therefore
\[
\|L(v)\|<\frac2\delta\|v\|.
\]
The same inequality is trivial for $v=0$. Hence the required estimate holds with $c=2/\delta$.
:::
:::
