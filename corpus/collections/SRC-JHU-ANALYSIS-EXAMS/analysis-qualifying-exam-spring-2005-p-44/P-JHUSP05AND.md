---
schema: qual/card@1
id: P-JHUSP05AND
kind: problem
title: "Weak and strong convergence of an orthonormal basis and its Cesàro means"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Weak Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\{e_n\}$ be an orthonormal basis for a Hilbert space $H$.

a) Show that $e_n \to 0$ weakly.
(Explain what weak convergence means.)

b) Show that $e_n$ does not tend to zero strongly.
(Explain what strong convergence means.)

c) Let $v_n = \frac{1}{n} \sum_{j=1}^{n} e_j$.
Show that $v_n \to 0$ strongly.
:::

::: {.solution}
A sequence $x_n$ in $H$ converges weakly to $x$ if $\phi(x_n)\to\phi(x)$ for every bounded linear functional $\phi$ on $H$; by the Riesz representation theorem, if and only if $\langle x_n,y\rangle\to\langle x,y\rangle$ for every $y\in H$. It converges strongly to $x$ if $\norm{x_n-x}\to0$.

::: pf

::: {.pf-step #s1}

(a) $e_n\to0$ weakly.

::: pf-proof

For $y\in H$, Bessel's inequality gives $\sum_n\abs{\langle y,e_n\rangle}^2\le\norm y^2<\infty$, so the terms $\abs{\langle e_n,y\rangle}$ tend to $0$.

:::

:::

::: {.pf-step #s2}

(b) $e_n$ does not tend to $0$ strongly.

::: pf-proof

$\norm{e_n-0}=\norm{e_n}=1$ for every $n$.

:::

:::

::: {.pf-step #s3}

(c) $\norm{v_n}=1/\sqrt n$, so $v_n\to0$ strongly.

::: pf-proof

By orthonormality, $\norm{v_n}^2=\frac1{n^2}\sum_{j,k=1}^n\langle e_j,e_k\rangle=\frac{n}{n^2}=\frac1n$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} answer parts (a), (b) and (c).

:::

:::

:::
