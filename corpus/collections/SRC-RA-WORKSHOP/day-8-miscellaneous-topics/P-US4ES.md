---
schema: qual/card@1
id: P-US4ES
kind: problem
title: Continuity equivalent to lower and upper semicontinuity, and sequential characterization
  of lower semicontinuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $(X,d)$ be a metric space.
A function $f \colon X \to \mathbb{R}$ is said to be lower semi-continuous (l.s.c) if $f^{-1}(a,\infty)  = \{x \in X \, \colon \,  f(x)> a\}$ is open in $X$ for every $a \in \mathbb{R}$.
Analogously, $f$ is upper semi-continuous (u.s.c) if $f^{-1}(-\infty, b) = \{x \in X \, \colon \,  f(x)<b\}$ is open in $X$ for every $b \in \mathbb{R}$.

Prove that a function $f \colon X \to \mathbb{R}$ is continuous if and only if $f$ is both l.s.c. and u.s.c.

Prove that $f$ is lower semi-continuous if and only if $\liminf_{n \to \infty} f(x_n) \geq f(x)$ whenever $\{x_n\}_{n=1}^\infty \subseteq X$ such that $x_n \to x$ in $X$.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ is continuous, then it is both lower and upper semicontinuous.

::: pf-proof

For every $a,b\in\mathbb R$, the intervals $(a,\infty)$ and $(-\infty,b)$ are open in $\mathbb R$. Continuity makes their inverse images under $f$ open in $X$, as required.

:::

:::

::: {.pf-step #s2}

If $f$ is both lower and upper semicontinuous, then it is continuous.

::: pf-proof

For every $a<b$, one has
\[
f^{-1}((a,b))=f^{-1}((a,\infty))\cap f^{-1}((-\infty,b)).
\]
Both factors are open by the respective semicontinuity hypotheses, so their intersection is open. Every open subset of $\mathbb R$ is a union of open intervals; inverse images preserve unions. Therefore inverse images of all open subsets of $\mathbb R$ are open in $X$.

:::

:::

::: {.pf-step #s3}

If $f$ is lower semicontinuous and $x_n\to x$, then $\liminf_{n\to\infty}f(x_n)\ge f(x)$.

::: pf-proof

Fix $a<f(x)$. The set $U=f^{-1}((a,\infty))$ is open and contains $x$. Convergence $x_n\to x$ implies $x_n\in U$ eventually, hence $f(x_n)>a$ eventually. Consequently $\liminf_n f(x_n)\ge a$. Since this holds for every $a<f(x)$, the desired inequality follows.

:::

:::

::: {.pf-step #s4}

If the sequential liminf inequality holds for every convergent sequence, then $f$ is lower semicontinuous.

::: pf-proof

Suppose otherwise. There is $a\in\mathbb R$ such that $U=f^{-1}((a,\infty))$ is not open. Choose $x\in U$ which is not an interior point. For every integer $n\ge1$, the ball $B(x,1/n)$ meets $X\setminus U$; choose $x_n$ in that intersection. Then $x_n\to x$, while $f(x_n)\le a$ for all $n$. Thus
\[
\liminf_{n\to\infty}f(x_n)\le a<f(x),
\]
contradicting the assumed sequential inequality.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} establish the continuity equivalence; steps [](#s3){.pf-ref} and [](#s4){.pf-ref} establish the sequential characterization of lower semicontinuity.

:::

:::
