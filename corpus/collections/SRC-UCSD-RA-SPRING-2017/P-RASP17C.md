---
schema: qual/card@1
id: P-RASP17C
kind: problem
title: "Diagonal operators on Hilbert space: boundedness and compactness criterion"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Compact Operators
  - Orthonormal Bases
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Spring 2017 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing diagonal-operator proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $(H, \langle \cdot | \cdot \rangle)$ be a Hilbert space, $\{e_n\}_{n=1}^\infty$ and $\{u_n\}_{n=1}^\infty$ be orthonormal bases for $H$, and $\{\lambda_n\}_{n=1}^\infty \subset \mathbb{C}$ with $M := \sup_n |\lambda_n| < \infty$.

1. Show $Th := \sum_{n=1}^\infty \lambda_n \langle h | e_n \rangle u_n$ exists in $H$ for all $h \in H$.

2. Show $\|T\|_{op} \leq M < \infty$, where $\|T\|_{op}$ is the operator norm of $T$.

3. Show $T$ is a compact operator if $\lim_{n \to \infty} \lambda_n = 0$.
:::

::: {.solution}
**Part 1.**

::: pf

::: {.pf-step #p1-s1}
For $h \in H$, $\sum_n |\langle h | e_n \rangle|^2 = \|h\|^2 < \infty$ (Parseval).

::: pf-proof
$\{e_n\}$ is an orthonormal basis.
:::

:::

::: {.pf-step #p1-s2}
The series $\sum_n \lambda_n \langle h | e_n \rangle u_n$ converges in $H$ iff $\sum_n |\lambda_n \langle h | e_n \rangle|^2 < \infty$.

::: pf-proof
$\{u_n\}$ is orthonormal, so the series converges iff the sum of squares of coefficients converges.
:::

:::

::: {.pf-step #p1-s3}
$\sum_n |\lambda_n \langle h | e_n \rangle|^2 \le M^2 \sum_n |\langle h | e_n \rangle|^2 = M^2 \|h\|^2 < \infty$.

::: pf-proof
step [](#p1-s1){.pf-ref} and $|\lambda_n| \le M$.
:::

:::

::: {.pf-step #p1-s4}
Hence $Th = \sum_n \lambda_n \langle h | e_n \rangle u_n$ exists in $H$ for all $h$.

::: pf-proof
step [](#p1-s2){.pf-ref} and step [](#p1-s3){.pf-ref}.
:::

:::

:::

**Part 2.**

::: pf

::: {.pf-step #p2-s1}
$\|Th\|^2 = \sum_n |\lambda_n \langle h | e_n \rangle|^2 \le M^2 \sum_n |\langle h | e_n \rangle|^2 = M^2 \|h\|^2$.

::: pf-proof
step [](#p1-s3){.pf-ref} (part 1) and Parseval.
:::

:::

::: {.pf-step #p2-s2}
Hence $\|T\|_{op} \le M < \infty$.

::: pf-proof
step [](#p2-s1){.pf-ref}.
:::

:::

:::

**Part 3.**

::: pf

::: {.pf-step #p3-s1}
Define $T_N h = \sum_{n=1}^{N} \lambda_n \langle h | e_n \rangle u_n$.

::: pf-proof
the finite-rank truncation.
:::

:::

::: pf-step
$T_N$ is a finite-rank operator (its range is spanned by $u_1, \ldots, u_N$).

::: pf-proof
step [](#p3-s1){.pf-ref}.
:::

:::

::: {.pf-step #p3-s3}
$\|T - T_N\|_{op} \le \sup_{n > N} |\lambda_n|$.

::: pf-proof
$T - T_N$ is the diagonal operator with coefficients $\lambda_n$ for $n > N$ and $0$ for $n \le N$, so its operator norm is $\sup_{n > N} |\lambda_n|$ (by part 2).
:::

:::

::: {.pf-step #p3-s4}
Since $\lambda_n \to 0$, $\sup_{n > N} |\lambda_n| \to 0$ as $N \to \infty$.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #p3-s5}
Hence $\|T - T_N\|_{op} \to 0$, so $T$ is the norm limit of finite-rank operators.

::: pf-proof
step [](#p3-s3){.pf-ref} and step [](#p3-s4){.pf-ref}.
:::

:::

::: {.pf-step #p3-s6}
Therefore $T$ is compact.

::: pf-proof
step [](#p3-s5){.pf-ref} (a norm limit of finite-rank operators is compact).
:::

:::

::: pf-qed
step [](#p1-s4){.pf-ref} (1), step [](#p2-s2){.pf-ref} (2), step [](#p3-s6){.pf-ref} (3).
:::

:::
:::
