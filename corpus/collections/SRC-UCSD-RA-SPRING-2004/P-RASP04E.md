---
schema: qual/card@1
id: P-RASP04E
kind: problem
title: "Uniform boundedness from weak sequential boundedness in L^p"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Suppose that $\{f_n\}_{n=1}^{\infty} \subset L^3(\mu)$ such that $\lim_{n \to \infty} \int_X f_n \varphi\,d\mu$ exists in $\mathbb{C}$ for all $\varphi \in L^{3/2}(\mu)$.
Show $M := \sup_n \|f_n\|_{L^3(\mu)} < \infty$.
:::

::: {.solution}
<1>1. Define the linear functional $\Lambda_n: L^{3/2}(\mu) \to \CC$ by $\Lambda_n(\varphi) = \int_X f_n \varphi\, d\mu$.
::: {.proof}
definition.
:::

<1>2. Each $\Lambda_n$ is bounded, with $\|\Lambda_n\| = \|f_n\|_{L^3}$.
::: {.proof}
by Hölder's inequality, $|\Lambda_n(\varphi)| \le \|f_n\|_{L^3}\|\varphi\|_{L^{3/2}}$, and the dual of $L^{3/2}$ is $L^3$ (since $3/2$ and $3$ are conjugate exponents), so $\|\Lambda_n\| = \|f_n\|_{L^3}$.
:::

<1>3. For each $\varphi \in L^{3/2}$, $\sup_n |\Lambda_n(\varphi)| < \infty$.
::: {.proof}
the limit $\lim_n \Lambda_n(\varphi)$ exists (by hypothesis), so the sequence $\{\Lambda_n(\varphi)\}$ is bounded.
:::

<1>4. By the uniform boundedness principle (Banach–Steinhaus), $\sup_n \|\Lambda_n\| < \infty$.
::: {.proof}
<1>3 and the uniform boundedness principle applied to the family $\{\Lambda_n\}$ of bounded linear functionals on the Banach space $L^{3/2}$.
:::

<1>5. Hence $M = \sup_n \|f_n\|_{L^3} = \sup_n \|\Lambda_n\| < \infty$.
::: {.proof}
<1>2 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
