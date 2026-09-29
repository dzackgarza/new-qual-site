---
schema: qual/card@1
id: P-RASP16G
kind: problem
title: "Weak convergence in $C_0(X)$ is uniform boundedness plus pointwise convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - C0 Spaces
  - Locally Compact Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the recorded UCSD source appearance for this C_0 weak-convergence problem.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing Riesz-Markov and dominated-convergence proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $X$ be a locally compact Hausdorff topological vector space.
Let $f \in C_0(X)$ and $f_k \in C_0(X)$ ($k = 1, 2, \ldots$). Prove that $f_k \to f$ weakly in $C_0(X)$ if and only if $\sup_{k \geq 1} \|f_k\|_u < \infty$ and $f_k \to f$ pointwise on $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$f_k \to f$ weakly in $C_0(X)$ if and only if $\int_X f_k\,d\mu \to \int_X f\,d\mu$ for every $\mu \in M(X)$.

::: pf-proof

::: {.pf-step #s1-1}

By the Riesz–Markov–Kakutani Representation Theorem, the continuous dual space $C_0(X)^*$ is isometrically isomorphic to $M(X)$, the Banach space of regular complex Borel measures on $X$ equipped with the total variation norm $\|\mu\| = |\mu|(X)$.

::: pf-proof

This is the Riesz–Markov–Kakutani representation theorem for a locally compact Hausdorff space $X$.

:::

:::

::: pf-qed

By definition, $f_k\to f$ weakly if and only if $\Lambda(f_k)\to\Lambda(f)$ for every $\Lambda\in C_0(X)^*$; by step [](#s1-1){.pf-ref} these functionals are exactly $g\mapsto\int_X g\,d\mu$ for $\mu\in M(X)$.

:::

:::

:::

::: {.pf-step #s2}

If $f_k \to f$ weakly, then $\sup_k\|f_k\|_u<\infty$ and $f_k\to f$ pointwise.

::: pf-proof

::: pf-step

$\sup_{k \ge 1} \|f_k\|_u < \infty$.

::: pf-proof

Regard each $f_k$ as a bounded linear functional on the Banach space $C_0(X)^*$, with norm $\sup_{\|\mu\|\le1}\abs{\int_X f_k\,d\mu}=\|f_k\|_u$. Weak convergence makes $\sup_k\abs{\int_X f_k\,d\mu}$ finite for each $\mu\in M(X)$, so the uniform boundedness principle gives
\[
\sup_{k \ge 1} \|f_k\|_u = \sup_{k \ge 1} \sup_{\|\mu\| \le 1} \left|\int_X f_k\,d\mu\right| < \infty.
\]

:::

:::

::: pf-step

$f_k(x) \to f(x)$ for every $x \in X$.

::: pf-proof

For $x\in X$, the Dirac measure $\delta_x$ lies in $M(X)$ with $\|\delta_x\| = 1$. Step [](#s1){.pf-ref} applied to $\mu=\delta_x$ gives
\[
f_k(x) = \int_X f_k\,d\delta_x \xrightarrow{k \to \infty} \int_X f\,d\delta_x = f(x).
\]

:::

:::

:::

:::

::: {.pf-step #s3}

If $\sup_{k \ge 1} \|f_k\|_u \le M < \infty$ and $f_k \to f$ pointwise, then $f_k \to f$ weakly.

::: pf-proof

Let $\mu \in M(X)$. Then $|\mu|(X) < \infty$, so the constant function $M$ lies in $L^1(X, |\mu|)$ and dominates every $|f_k|$. By the dominated convergence theorem,
\[
\lim_{k \to \infty} \int_X f_k\,d\mu = \int_X f\,d\mu.
\]
Since $\mu \in M(X)$ was arbitrary, step [](#s1){.pf-ref} gives $f_k \to f$ weakly in $C_0(X)$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the two implications.

:::

:::

:::
