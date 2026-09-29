---
schema: qual/card@1
id: P-RASP13G
kind: problem
title: "sin(kx) converges weakly but not strongly to zero in L^p"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
  - Riemann-Lebesgue Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 7 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Removed an invalid density argument for the p=1 case and used Riemann-Lebesgue directly on every dual test function.
---

::: {.problem}
Let $X = [-\pi, \pi]$ with Lebesgue measure.
Let $p$ be a real number with $1 \leq p < \infty$.
Define for each integer $k \geq 1$ that $f_k(x) = \sin(kx)$ ($x \in X$).

(a) Prove that the sequence $\{f_k\}$ converges weakly to $0$ in $L^p(X)$.

(b) Prove that the sequence $\{f_k\}$ does not converge to $0$ strongly in $L^p(X)$.
:::

::: {.solution}
**Part (a).**

::: pf

::: pf-step
Test directly against an arbitrary element of the dual.

::: pf-proof
Let $q$ be conjugate to $p$, with $q=\infty$ when $p=1$. Since $X=[-\pi,\pi]$ has finite measure, every $g\in L^q(X)$ belongs to $L^1(X)$. Therefore the Riemann--Lebesgue lemma gives
\[
\int_{-\pi}^{\pi} g(x)e^{ikx}\,dx\longrightarrow0.
\]
Taking imaginary parts yields
\[
\int_{-\pi}^{\pi} g(x)\sin(kx)\,dx\longrightarrow0.
\]
:::

:::

::: {.pf-step #p1-s2}
Hence $f_k \rightharpoonup 0$ in $L^p(X)$.

::: pf-proof
For $1<p<\infty$, $(L^p)^*=L^q$, so Step 1 is exactly weak convergence. For $p=1$, the dual is $L^\infty$, and Step 1 also covers every $L^\infty$ test function because $L^\infty(X)\subset L^1(X)$ on this finite-measure interval.
:::

:::

:::

**Part (b).**

::: pf

::: {.pf-step #p2-s1}
$\|f_k\|_{L^p}^p = \int_{-\pi}^{\pi} |\sin(kx)|^p\, dx$ is constant in $k$ and nonzero.

::: pf-proof
by periodicity, $\int_{-\pi}^{\pi} |\sin(kx)|^p\, dx = \int_{-\pi}^{\pi} |\sin(x)|^p\, dx > 0$ (substitute $u = kx$ and use $2\pi$-periodicity).
:::

:::

::: {.pf-step #p2-s2}
Hence $\|f_k\|_{L^p} \not\to 0$.

::: pf-proof
step [](#p2-s1){.pf-ref} shows the norm is a fixed positive constant.
:::

:::

::: {.pf-step #p2-s3}
Therefore $f_k$ does not converge strongly to $0$ in $L^p(X)$.

::: pf-proof
strong convergence to $0$ would force $\|f_k\|_{L^p} \to 0$, contradicting step [](#p2-s2){.pf-ref}.
:::

:::

::: pf-qed
step [](#p1-s2){.pf-ref} (part (a)) and step [](#p2-s3){.pf-ref} (part (b)).
:::

:::
:::
