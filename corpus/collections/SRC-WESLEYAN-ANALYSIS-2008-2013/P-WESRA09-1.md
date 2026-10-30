---
schema: qual/card@1
id: P-WESRA09-1
kind: problem
title: 'Definitions in measure theory and normed spaces'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Give definitions of each of the following:

1. a Dynkin system in a set $\Omega$;

2. an outer measure on $\Omega$;

3. a $\mu^*$-measurable set when $\mu^*$ is an outer measure;

4. an integrable function on a measure space $(\Omega,\mathcal A,\mu)$;

5. absolute continuity of one measure with respect to another;

6. a normed vector space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A Dynkin system on $\Omega$ is a collection $\mathcal D\subseteq\mathcal P(\Omega)$ such that $\Omega\in\mathcal D$, whenever $A,B\in\mathcal D$ with $A\subseteq B$ one has $B\setminus A\in\mathcal D$, and whenever $(A_n)_{n\ge1}\subseteq\mathcal D$ are pairwise disjoint one has $\bigcup_{n=1}^\infty A_n\in\mathcal D$.

:::

::: pf-step

An outer measure on $\Omega$ is a function
$$
\mu^*:\mathcal P(\Omega)\longrightarrow[0,\infty]
$$
such that $\mu^*(\varnothing)=0$, $A\subseteq B$ implies $\mu^*(A)\le\mu^*(B)$, and
$$
\mu^*\!\left(\bigcup_{n=1}^\infty A_n\right)
\le \sum_{n=1}^\infty \mu^*(A_n)
$$
for every sequence $(A_n)_{n\ge1}\subseteq\mathcal P(\Omega)$.

:::

::: pf-step

If $\mu^*$ is an outer measure on $\Omega$, a set $E\subseteq\Omega$ is $\mu^*$-measurable when
$$
\mu^*(A)=\mu^*(A\cap E)+\mu^*(A\setminus E)
$$
for every $A\subseteq\Omega$.

:::

::: pf-step

A real- or complex-valued function $f$ on $(\Omega,\mathcal A,\mu)$ is integrable when it is $\mathcal A$-measurable and
$$
\int_\Omega \abs{f}\,d\mu<\infty.
$$

:::

::: pf-step

For measures $\mu$ and $\nu$ on the same measurable space, $\mu$ is absolutely continuous with respect to $\nu$, written $\mu\ll\nu$, when
$$
\nu(E)=0\quad\Longrightarrow\quad\mu(E)=0
$$
for every measurable set $E$.

:::

::: {.pf-step #s1-6}

A normed vector space is a vector space $V$ over $\RR$ or $\CC$ together with a function $\norm{\cdot}:V\to[0,\infty)$ such that, for all $x,y\in V$ and scalars $\lambda$,
$$
\norm{x}=0\Longleftrightarrow x=0,
\qquad
\norm{\lambda x}=\abs{\lambda}\,\norm{x},
\qquad
\norm{x+y}\le\norm{x}+\norm{y}.
$$

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} give the six requested definitions.

:::

:::

:::
