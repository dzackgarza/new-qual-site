---
schema: qual/card@1
id: P-CASP12B
kind: problem
title: "Normal families characterized by coefficient bounds"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP12_220_Complex_Analysis_Qual.pdf,
    Section 2, Problem 1: "Let F subset H(D). Prove that F is normal if and only if there exists a
    sequence of nonnegative constants {M_n} such that limsup M_n^(1/n) <= 1 and
    sup_{f in F} |f^(n)(0)/n!| <= M_n". The problem and both displayed conditions are as the card
    now has them.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Statement repaired: the card printed the hypothesis as lim M_n^(1/n) <= 1, and the paper prints
    limsup. The difference matters in the converse direction, which yields only the limsup bound,
    so the statement now follows the paper. The solution is the card's own, structured into Lamport
    steps. Checked: that limsup M_n^(1/n) < 1/rho gives M_n <= rho^-n eventually, so the Taylor
    series is dominated by a geometric series on the closed disc of radius r < rho; that a normal
    family is locally bounded, by the subsequence argument; Cauchy's estimate coefficient by
    coefficient; and the passage from the bound limsup M_n^(1/n) <= 1/r for every r < 1 to the bound
    with 1. No retained published solution covers this problem.
---

::: {.problem}
Let $\mathcal{F} \subseteq H(\DD)$.
Prove that $\mathcal{F}$ is normal if and only if there exists a sequence of nonnegative constants $\{M_n\}$ such that $\limsup_{n \to \infty} M_n^{1/n} \leq 1$ and $\sup_{f \in \mathcal{F}} \abs{\frac{f^{(n)}(0)}{n!}} \leq M_n$ for each $n \geq 0$.
:::

::: {.solution}
This is Problem 1 of Section 2 of the UCSD complex-analysis qualifying exam of Spring 2012 (`assets/attachments/SP12_220_Complex_Analysis_Qual.pdf`). No published solution set is transcribed: the argument is the card's own, and it is the standard coefficient characterization of normal families through Montel's theorem and Cauchy's estimates.

The statement was corrected against the printed paper, which writes $\limsup_{n\to\infty}M_{n}^{1/n}\leq1$; the card had written $\lim$. The two differ, and the converse direction below produces only the $\limsup$ bound, so the printed hypothesis is the one stated.

::: pf

::: {.pf-step #forward}
Assume there are $M_{n}\geq0$ with $\limsup_{n}M_{n}^{1/n}\leq1$ and $\sup_{f\in\mathcal{F}}\abs{a_{n}(f)}\leq M_{n}$ for every $n$, where $a_{n}(f)=f^{(n)}(0)/n!$. Then $\mathcal{F}$ is locally bounded.

::: pf-proof
Fix $0<r<1$ and choose $\rho$ with $r<\rho<1$. Since $\limsup M_{n}^{1/n}\leq1<1/\rho$, there is $N$ with $M_{n}^{1/n}\leq1/\rho$, that is $M_{n}\leq\rho^{-n}$, for all $n\geq N$. Then for $\abs{z}\leq r$ and $f\in\mathcal{F}$,
$$\abs{f(z)}\leq\sum_{n=0}^{\infty}\abs{a_{n}(f)}r^{n}\leq\sum_{n=0}^{N-1}M_{n}r^{n}+\sum_{n\geq N}\left(\frac{r}{\rho}\right)^{n}<\infty,$$
which does not depend on $f$ or on $z$ in the disc.
:::
:::

::: {.pf-step #montel}
$\mathcal{F}$ is normal.

::: pf-proof
A locally bounded family of holomorphic functions on a domain is normal: this is Montel's theorem. Step [](#forward){.pf-ref} gives the local bound on every disc $\abs{z}\leq r$ with $r<1$, and these discs cover $\DD$.
:::
:::

::: {.pf-step #converse-bounded}
Assume $\mathcal{F}$ is normal; then $\mathcal{F}$ is locally bounded.

::: pf-proof
If it were not, there would be a compact $K\subset\DD$ and $f_{j}\in\mathcal{F}$ with $\sup_{K}\abs{f_{j}}\to\infty$. Normality gives a subsequence converging uniformly on $K$ to a function holomorphic on a neighbourhood of $K$, which is bounded on the compact set $K$; eventually the subsequence is within $1$ of that bound, contradicting the divergence.
:::
:::

::: {.pf-step #cauchy}
With $C_{r}=\sup_{f\in\mathcal{F}}\max_{\abs{z}=r}\abs{f(z)}$ for $0<r<1$, one has $\abs{a_{n}(f)}\leq C_{r}r^{-n}$, so $M_{n}=\sup_{f\in\mathcal{F}}\abs{a_{n}(f)}$ is finite for every $n$.

::: pf-proof
$C_{r}<\infty$ by step [](#converse-bounded){.pf-ref}, since the circle $\abs{z}=r$ is compact. Each $f\in\mathcal{F}$ is holomorphic on the disc of radius $r$, and Cauchy's estimate for the $n$-th coefficient gives $\abs{a_{n}(f)}\leq\max_{\abs{z}=r}\abs{f(z)}\,r^{-n}\leq C_{r}r^{-n}$. Taking the supremum over $f$ gives $M_{n}\leq C_{r}r^{-n}<\infty$, and $M_{n}\geq0$.
:::
:::

::: {.pf-step #limsup}
$\limsup_{n}M_{n}^{1/n}\leq1$.

::: pf-proof
From step [](#cauchy){.pf-ref}, $M_{n}^{1/n}\leq C_{r}^{1/n}r^{-1}$ for every $n$, so $\limsup_{n}M_{n}^{1/n}\leq r^{-1}$ for every $0<r<1$; letting $r\uparrow1$ gives the bound.
:::
:::
:::

:::
