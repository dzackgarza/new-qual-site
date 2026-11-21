---
schema: qual/card@1
id: P-RASP18D
kind: problem
title: "Riemann-Lebesgue lemma for derivatives of dilated functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing integration-by-parts and density proof reviewed as correct; normalized the legacy solution block.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight steps asserted their claim with no justification and the card is now two steps, one per part, each
    deriving its claim. Part 1: the integration by parts is written with $v = \lambda^{-1}\varphi(\lambda x)$,
    the boundary term is shown to vanish because $f$ has compact support while $\varphi$ is bounded, and the
    remaining integral is bounded by $M\lambda^{-1}\norm{f'}_{L^1}$. Part 2: the split into $f - g$ and $g$,
    the bound $\varepsilon/2$ on the first piece, the threshold $\Lambda = 2M\norm{g'}_{L^1}/\varepsilon$ from
    part 1 for the second, and the sum. One gap repaired: both parts divide by $M$, and the card nowhere
    treated $M = 0$; when $M = 0$ one has $\varphi \equiv 0$ and both conclusions hold trivially, which each
    step now says before assuming $M > 0$. The closing pf-qed, which only said both parts were proved, is
    gone. Sources are cited by numbered statement: integration by parts, the density of $C_c^1(\RR)$ in
    $L^1(\RR)$, and the definition of $M$ in the statement; no page reference is written in the body of this
    card or in the event above. The statement is unchanged. The collection retains the UCSD real analysis
    qualifying exam of Spring 2018 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $\varphi : \RR \to \RR$ be a $C^1$-function such that $M := \sup_{x \in \RR} [\abs{\varphi(x)} + \abs{\varphi'(x)}] < \infty$.

1. If $f \in C_c^1(\RR)$, show
$$
\abs{\int_{\RR} f(x) \varphi'(\lambda x)\,dx} \leq M \cdot \norm{f'}_{L^1(\RR, m)} \abs{\lambda}^{-1} \quad \text{for all } \lambda > 0.
$$

2. If $f \in L^1(\RR, m)$, show
$$
\lim_{\lambda \to \infty} \int_{\RR} f(x) \varphi'(\lambda x)\,dx = 0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #bound}
For $f \in C_c^1(\RR)$ and $\lambda > 0$, $\abs{\int_\RR f(x)\varphi'(\lambda x)\,dx} \le M\norm{f'}_{L^1}\lambda^{-1}$.

::: pf-proof
If $M = 0$ then $\abs{\varphi} + \abs{\varphi'} \le 0$ pointwise forces $\varphi \equiv 0$ and the integral vanishes, so assume $M > 0$. Since $f \in C_c^1$ both $f$ and $f'$ are supported in some $[-R,R]$. Integration by parts on that interval with $u = f$ and $dv = \varphi'(\lambda x)\,dx$, so that $v = \lambda^{-1}\varphi(\lambda x)$, gives
$$\int_{-\infty}^\infty f(x)\varphi'(\lambda x)\,dx = \left[\lambda^{-1}f(x)\varphi(\lambda x)\right]_{-\infty}^{\infty} - \lambda^{-1}\int_{-\infty}^\infty f'(x)\varphi(\lambda x)\,dx,$$
and the boundary term vanishes because $f$ vanishes outside $[-R,R]$ while $\varphi$ is bounded. Taking absolute values and using $\abs{\varphi(\lambda x)} \le M$ bounds the integral by $\lambda^{-1}\int\abs{f'}\abs{\varphi(\lambda x)}\,dx \le M\lambda^{-1}\norm{f'}_{L^1}$, which is the stated inequality for $\lambda > 0$.
:::

:::

::: {.pf-step #limit}
For $f \in L^1(\RR)$, $\lim_{\lambda\to\infty}\int_\RR f(x)\varphi'(\lambda x)\,dx = 0$.

::: pf-proof
If $M = 0$ the integrand vanishes identically and there is nothing to prove, so take $M > 0$ and let $\varepsilon > 0$. By density of $C_c^1(\RR)$ in $L^1(\RR)$ choose $g \in C_c^1(\RR)$ with $\norm{f-g}_{L^1} < \varepsilon/(2M)$. Writing the integral of $f$ as that of $f - g$ plus that of $g$, the first term is bounded by $\sup_y\abs{\varphi'(y)}\norm{f-g}_{L^1} \le M\cdot\varepsilon/(2M) = \varepsilon/2$, using $\abs{\varphi'} \le M$. By step [](#bound){.pf-ref} applied to $g$ the second term is at most $M\norm{g'}_{L^1}\lambda^{-1}$, which is below $\varepsilon/2$ for every $\lambda > \Lambda \coloneqq 2M\norm{g'}_{L^1}/\varepsilon$. For such $\lambda$ the sum of the two bounds is $\varepsilon$, and since $\varepsilon$ was arbitrary the limit is $0$.
:::

:::
:::
:::
