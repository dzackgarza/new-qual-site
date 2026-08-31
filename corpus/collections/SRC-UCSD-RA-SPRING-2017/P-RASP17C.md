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
---

::: problem
Let $(H, \langle \cdot | \cdot \rangle)$ be a Hilbert space, $\{e_n\}_{n=1}^\infty$ and $\{u_n\}_{n=1}^\infty$ be orthonormal bases for $H$, and $\{\lambda_n\}_{n=1}^\infty \subset \mathbb{C}$ with $M := \sup_n |\lambda_n| < \infty$.

1. Show $Th := \sum_{n=1}^\infty \lambda_n \langle h | e_n \rangle u_n$ exists in $H$ for all $h \in H$.

2. Show $\|T\|_{op} \leq M < \infty$, where $\|T\|_{op}$ is the operator norm of $T$.

3. Show $T$ is a compact operator if $\lim_{n \to \infty} \lambda_n = 0$.
:::

::: {.solution}
**Part 1.**

<1>1. For $h \in H$, $\sum_n |\langle h | e_n \rangle|^2 = \|h\|^2 < \infty$ (Parseval).
::: {.proof}
$\{e_n\}$ is an orthonormal basis.
:::

<1>2. The series $\sum_n \lambda_n \langle h | e_n \rangle u_n$ converges in $H$ iff $\sum_n |\lambda_n \langle h | e_n \rangle|^2 < \infty$.
::: {.proof}
$\{u_n\}$ is orthonormal, so the series converges iff the sum of squares of coefficients converges.
:::

<1>3. $\sum_n |\lambda_n \langle h | e_n \rangle|^2 \le M^2 \sum_n |\langle h | e_n \rangle|^2 = M^2 \|h\|^2 < \infty$.
::: {.proof}
<1>1 and $|\lambda_n| \le M$.
:::

<1>4. Hence $Th = \sum_n \lambda_n \langle h | e_n \rangle u_n$ exists in $H$ for all $h$.
::: {.proof}
<1>2 and <1>3.
:::

**Part 2.**

<1>1. $\|Th\|^2 = \sum_n |\lambda_n \langle h | e_n \rangle|^2 \le M^2 \sum_n |\langle h | e_n \rangle|^2 = M^2 \|h\|^2$.
::: {.proof}
<1>3 (part 1) and Parseval.
:::

<1>2. Hence $\|T\|_{op} \le M < \infty$.
::: {.proof}
<1>1.
:::

**Part 3.**

<1>1. Define $T_N h = \sum_{n=1}^{N} \lambda_n \langle h | e_n \rangle u_n$.
::: {.proof}
the finite-rank truncation.
:::

<1>2. $T_N$ is a finite-rank operator (its range is spanned by $u_1, \ldots, u_N$).
::: {.proof}
<1>1.
:::

<1>3. $\|T - T_N\|_{op} \le \sup_{n > N} |\lambda_n|$.
::: {.proof}
$T - T_N$ is the diagonal operator with coefficients $\lambda_n$ for $n > N$ and $0$ for $n \le N$, so its operator norm is $\sup_{n > N} |\lambda_n|$ (by part 2).
:::

<1>4. Since $\lambda_n \to 0$, $\sup_{n > N} |\lambda_n| \to 0$ as $N \to \infty$.
::: {.proof}
hypothesis.
:::

<1>5. Hence $\|T - T_N\|_{op} \to 0$, so $T$ is the norm limit of finite-rank operators.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Therefore $T$ is compact.
::: {.proof}
<1>5 (a norm limit of finite-rank operators is compact).
:::

<1>7. Q.E.D.
::: {.proof}
<1>4 (1), <1>2 (2), <1>6 (3).
:::
:::
