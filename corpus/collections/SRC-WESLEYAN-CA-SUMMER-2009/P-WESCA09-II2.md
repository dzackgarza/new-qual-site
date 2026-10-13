---
schema: qual/card@1
id: P-WESCA09-II2
kind: problem
title: 'If every analytic function has a primitive, the domain is simply connected'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section II, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $D\subset\mathbb C$ be a domain.
If every function analytic in $D$ has a primitive in $D$, prove that $D$ is simply connected, where simply connected means that every cycle in $D$ is homologous to zero.
:::

::: {.solution}
<1>1. Let $\sigma$ be any cycle in $D$ and let $a\in\mathbb C\setminus D$.
Then
\[
\int_\sigma \frac{dz}{z-a}=0.
\]

::: {.proof}
Because $a\notin D$, the function
\[
z\longmapsto \frac1{z-a}
\]
is analytic on $D$. By hypothesis it has a primitive $F$ on $D$. The integral
of a derivative over every closed path is zero, and by linearity the same is
true over every cycle. Therefore
\[
\int_\sigma \frac{dz}{z-a}
=\int_\sigma F'(z)\,dz
=0.
\]
:::

<1>2. Every cycle $\sigma$ in $D$ is homologous to zero in $D$.

::: {.proof}
Let $a\in\mathbb C\setminus D$. By the definition of the winding number and
step <1>1,
\[
n(\sigma,a)
=\frac1{2\pi i}\int_\sigma\frac{dz}{z-a}
=0.
\]
Since this holds for every $a\notin D$, the defining criterion for $\sigma$ to
be homologous to zero in $D$ is satisfied.
:::

<1>3. Hence $D$ is simply connected.

::: {.proof}
The cycle $\sigma$ in step <1>1 was arbitrary. Step <1>2 therefore shows that
every cycle in $D$ is homologous to zero, which is the stated definition of
simple connectedness.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the required conclusion.
:::
:::
