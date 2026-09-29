---
schema: qual/card@1
id: P-BERK90S-09
kind: problem
title: Intermediate-value property plus closed level sets forces continuity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared both hypotheses and the conclusion of Problem 9 with the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Constructed an epsilon-delta neighborhood by excluding two closed level sets and applying the intermediate-value property on segments.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked relative closedness, both inequality cases, containment of each segment in the neighborhood, and continuity at the endpoints.
---

::: {.problem}
Let $f:[0,1]\to\RR$ satisfy:

1. for every interval $[a,b]\subset[0,1]$, the set $f([a,b])$ contains the interval with endpoints $f(a)$ and $f(b)$;
2. for every $c\in\RR$, the level set $f^{-1}(c)$ is closed.

Prove that $f$ is continuous.
:::

::: {.hint}
Fix $x_0\in[0,1]$ and $\varepsilon>0$, and put
$c_-\coloneqq f(x_0)-\varepsilon$ and
$c_+\coloneqq f(x_0)+\varepsilon$.
The two closed level sets $f^{-1}(c_-)$ and $f^{-1}(c_+)$ omit $x_0$,
so some interval neighborhood of $x_0$ in $[0,1]$ avoids both sets.
Apply the intermediate-value property on the segment joining $x_0$
to any point of this neighborhood. A value outside $(c_-,c_+)$ would
force one of the excluded levels on that segment.
:::

::: {.solution}
Fix $x_0\in[0,1]$ and $\varepsilon>0$. Put
$c_-\coloneqq f(x_0)-\varepsilon$ and
$c_+\coloneqq f(x_0)+\varepsilon$.

::: pf

::: {.pf-step #s1}

There exists $\delta>0$ such that the relative neighborhood
$$
U\coloneqq(x_0-\delta,x_0+\delta)\cap[0,1]
$$
meets neither $f^{-1}(c_-)$ nor $f^{-1}(c_+)$.

::: pf-proof

Both level sets are closed in $[0,1]$ by hypothesis. Their union is
closed and omits $x_0$, since $c_-<f(x_0)<c_+$. Its complement is
therefore a relatively open set containing $x_0$, so it contains $U$
for some $\delta>0$.

:::

:::

::: {.pf-step #s2}

Every $x\in U$ satisfies
$\abs{f(x)-f(x_0)}<\varepsilon$.

::: pf-proof

Fix $x\in U$. The segment with endpoints $x_0$ and $x$ is contained
in $U$, because each point on it lies in $[0,1]$ and has distance
at most $\abs{x-x_0}<\delta$ from $x_0$.
If $f(x)\geq c_+$, the intermediate-value hypothesis on this segment
gives a point $y$ on the segment with $f(y)=c_+$. This contradicts
step [](#s1){.pf-ref}. If $f(x)\leq c_-$, the same hypothesis gives a point
$y$ on the segment with $f(y)=c_-$, again contradicting step [](#s1){.pf-ref}.
Consequently $c_-<f(x)<c_+$, which is the asserted inequality.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that for every $\varepsilon>0$ there is
$\delta>0$ such that $x\in[0,1]$ and $\abs{x-x_0}<\delta$ imply
$\abs{f(x)-f(x_0)}<\varepsilon$. Thus $f$ is continuous at $x_0$.
Since $x_0$ was arbitrary, $f$ is continuous on $[0,1]$.

:::

:::

:::
