---
schema: qual/card@1
id: P-QMPVS
kind: problem
title: Hölder's inequality, Minkowski's inequality, $L^\infty[0,1]$, and $\lim_{p\to\infty}\int_{[0,1]}f^p$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - L∞
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'Part (a) of the source printed the conclusion of Hölder''s inequality as ||fg||_p <= ||f||_p ||g||_q; the statement now bounds ||fg||_1.'
---

::: {.problem}
(a) Prove Hölder's inequality: let $f\in L^p, g\in L^q$ with $p, q$ conjugate, and show that
$$
\pnorm{fg}{1} \leq \pnorm{f}{p} \cdot \pnorm{g}{q}.
$$

(b) Prove Minkowski's inequality:
$$
1\leq p < \infty \implies \pnorm{f+g}{p} \leq \pnorm{f}{p}+ \pnorm{g}{p}.
$$
Conclude that if $f, g\in L^p(\RR^n)$ then so is $f+g$.

(c) Let $X = [0, 1] \subset \RR$.

(i) Give a definition of the Banach space $L^\infty(X)$ of essentially bounded functions on $X$.

(ii) Let $f$ be non-negative and measurable on $X$. Prove that, as $p\to\infty$, $\int_X f(x)^p \,dx$ converges either to $\infty$ or to $m\qty{f^{-1}(1)}$, and characterize the functions of each type.

:::

::: {.solution}

Part (c)(ii). Let $f \ge 0$ be measurable on $X = [0,1]$.

::: pf

::: {.pf-step #s1}

$\int_X f^p = \int_{\theset{f < 1}} f^p + m\theset{f = 1} + \int_{\theset{f > 1}} f^p$.

::: pf-proof

$X$ is the disjoint union of $\theset{f < 1}$, $\theset{f = 1}$ and $\theset{f > 1}$, and $f^p = 1$ on $\theset{f = 1}$.

:::

:::

::: {.pf-step #s2}

$\int_{\theset{f < 1}} f^p \to 0$ as $p \to \infty$.

::: pf-proof

On $\theset{f < 1}$, $f^p \to 0$ pointwise and $0 \le f^p \le 1$, and $m(X) = 1$, so dominated convergence applies.

:::

:::

::: {.pf-step #s3}

$\int_{\theset{f > 1}} f^p \to \infty$ if $m\theset{f > 1} > 0$, and it is $0$ if $m\theset{f > 1} = 0$.

::: pf-proof

If $m\theset{f > 1} > 0$, then $m\theset{f > 1 + 1/k} > 0$ for some $k$, and $\int_{\theset{f > 1}} f^p \ge (1 + 1/k)^p\, m\theset{f > 1 + 1/k} \to \infty$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\int_X f^p \to m\theset{f = 1} = m(f^{-1}(1))$ when $f \le 1$ a.e., and $\int_X f^p \to \infty$ when $m\theset{f > 1} > 0$.

:::

:::

:::
