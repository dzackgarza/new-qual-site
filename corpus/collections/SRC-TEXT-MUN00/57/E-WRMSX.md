---
schema: qual/card@1
id: E-WRMSX
kind: problem
title: Antipode-separating maps of the sphere are surjective
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that if $g: S^2 \to S^2$ is continuous and $g(x) \neq g(-x)$ for all $x$, then $g$ is surjective.
[Hint: If $p \in S^2$, then $S^2 - \ts{p}$ is homeomorphic to $\mathbb{R}^2$.]
:::

::: {.solution}
Suppose, toward a contradiction, that \(g\) is not surjective. Choose
\[
p\in S^2-g(S^2).
\]
Since \(S^2-\{p\}\) is homeomorphic to \(\mathbb R^2\), choose a homeomorphism
\[
\phi:S^2-\{p\}\longrightarrow\mathbb R^2.
\]
Then
\[
F=\phi\circ g:S^2\to\mathbb R^2
\]
is continuous. By the Borsuk--Ulam theorem there exists \(x\in S^2\) with
\[
F(x)=F(-x).
\]
Since \(\phi\) is injective, this implies
\[
g(x)=g(-x),
\]
contrary to the hypothesis. Therefore \(g\) must be surjective.
:::
