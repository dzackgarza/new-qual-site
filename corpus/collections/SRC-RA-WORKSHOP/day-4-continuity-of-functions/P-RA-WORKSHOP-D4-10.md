---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-10
kind: problem
title: A continuous real function cannot take every value exactly twice
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
([KRD10, 5.6.H]) Show that a continuous function $f:\RR\to\RR$ cannot take on every real value exactly twice.
:::

::: {.solution}
Suppose for contradiction that a continuous $f:\RR\to\RR$ takes every real value exactly twice. Choose $a<b$ with $f(a)=f(b)=c$.

::: pf

::: {.pf-step #s1}

There exists $t\in(a,b)$ with $f(t)\ne c$.

::: pf-proof

Otherwise $f$ is constant with value $c$ on $[a,b]$, giving more than two preimages of $c$.

:::

:::

::: {.pf-step #s2}

If $f(t)>c$ for some $t\in(a,b)$, then $f$ is bounded above on $\RR$.

::: pf-proof

Choose $y$ with $c<y<f(t)$. By the intermediate value theorem on $[a,t]$ and $[t,b]$, the equation $f(x)=y$ has one solution in $(a,t)$ and another in $(t,b)$. By the assumption of exactly two preimages, it has no solution in $(-\infty,a]$ or $[b,\infty)$. Since $f(a)=f(b)=c<y$, continuity and the intermediate value theorem imply $f(x)<y$ throughout those two exterior rays: a value greater than $y$ would force another preimage of $y$. On the compact interval $[a,b]$, the continuous function $f$ is bounded above. Combining the interval bound with $f(x)<y$ on the exterior rays bounds $f$ above on all of $\RR$.

:::

:::

::: {.pf-step #s3}

If $f(t)<c$ for some $t\in(a,b)$, then $f$ is bounded below on $\RR$.

::: pf-proof

Apply step [](#s2){.pf-ref} to the continuous function $-f$. It also takes every real value exactly twice, and $(-f)(t)>-c$. Thus $-f$ is bounded above, equivalently $f$ is bounded below.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, one of steps [](#s2){.pf-ref} and [](#s3){.pf-ref} applies. Thus $f$ is bounded either above or below, contradicting the assumption that it attains every real value. Hence such a continuous function cannot exist.

:::

:::

:::
