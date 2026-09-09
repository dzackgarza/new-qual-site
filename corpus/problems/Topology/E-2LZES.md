---
schema: qual/card@1
id: E-2LZES
kind: problem
title: Compactness, limit point compactness, and sequential compactness are equivalent for metrizable spaces
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that for $X$ metrizable, the following are equivalent:

- $X$ is compact;

- $X$ is limit point compact;

- $X$ is sequentially compact.
:::

::: {.remark}
The original exercise read "Show that if $X$ is metrizable, then $X$ is compact", which is false ($\RR$ is metrizable and not compact).
The equivalence above repairs it; the neighbouring exercises suggest the intended statement.
:::

::: solution
Fix a metric $d$ inducing the topology of $X$.

<1>1. Compactness implies limit-point compactness.
::: proof
Let $A\subseteq X$ be infinite. If $A$ had no limit point, then for each $x\in X$ there would be an open neighborhood $U_x$ with
$$
U_x\cap A\subseteq\{x\}.
$$
A finite subcover $U_{x_1},\dots,U_{x_r}$ would then give
$$
A\subseteq\{x_1,\dots,x_r\},
$$
a contradiction.
:::

<1>2. Limit-point compactness implies sequential compactness.
::: proof
Let $(x_n)$ be a sequence. If its range is finite, one value occurs infinitely often and gives a constant subsequence. If its range is infinite, let $x$ be a limit point of the range.

Every ball about $x$ contains infinitely many terms of the sequence: otherwise a smaller ball would meet the range in only finitely many points, contradicting that $x$ is a limit point. Inductively choose
$$
n_1<n_2<\cdots,
\qquad d(x_{n_k},x)<1/k.
$$
Then $x_{n_k}\to x$.
:::

<1>3. Sequential compactness implies total boundedness.
::: proof
If some $\varepsilon>0$ admitted no finite cover by $\varepsilon$-balls, choose inductively $x_{n+1}$ outside
$$
\bigcup_{j=1}^n B(x_j,\varepsilon).
$$
Then $d(x_i,x_j)\ge\varepsilon$ for $i\ne j$, so the sequence has no convergent subsequence, a contradiction.
:::

<1>4. Sequential compactness implies the Lebesgue-number property: every open cover $\mathcal U$ has some $\delta>0$ such that every ball $B(x,\delta)$ lies in a member of $\mathcal U$.
::: proof
If not, for each $n$ choose $x_n$ such that $B(x_n,1/n)$ is contained in no member of $\mathcal U$. Pass to a subsequence $x_{n_k}\to x$. Choose $U\in\mathcal U$ and $r>0$ with $B(x,r)\subseteq U$. For large $k$,
$$
d(x_{n_k},x)<r/2,
\qquad 1/n_k<r/2,
$$
so $B(x_{n_k},1/n_k)\subseteq B(x,r)\subseteq U$, a contradiction.
:::

<1>5. Sequential compactness implies compactness.
::: proof
Let $\mathcal U$ be an open cover and choose a Lebesgue number $\delta>0$. By total boundedness, finitely many balls
$$
B(x_1,\delta),\dots,B(x_m,\delta)
$$
cover $X$. Each such ball lies in some member of $\mathcal U$, so those finitely many members form a finite subcover.
:::

<1>6. Hence compactness, limit-point compactness, and sequential compactness are equivalent for metrizable spaces.
:::
