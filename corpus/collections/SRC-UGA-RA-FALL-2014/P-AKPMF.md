---
schema: qual/card@1
id: P-AKPMF
kind: problem
title: $\norm{f}_p=\sup_{\norm{g}_q=1}\abs{\int fg}$ for $f\in L^p(\RR^n)$ and conjugate exponents
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the UGA Fall 2014 real-analysis qualifying exam recorded by the collection source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $1 \leq p,q \leq \infty$ be conjugate exponents, and show that
$$
f \in L^p(\RR^n) \implies \norm{f}_{p} = \sup _{\norm{g}_{q}=1}\abs{\int f(x) g(x) d x}
$$
:::
::: {.solution}

::: pf

::: pf-step

Hölder gives the upper bound.

::: pf-proof

For every $g\in L^q(\RR^n)$ with $\norm{g}_q=1$, Hölder's inequality gives
$$
\abs{\int_{\RR^n}f(x)g(x)\,dx}
\le \norm{f}_p\norm{g}_q
=\norm{f}_p.
$$
Hence
$$
\sup_{\norm{g}_q=1}\abs{\int fg}\le\norm{f}_p.
$$

:::

:::

::: pf-step

Prove equality when $1<p<\infty$.

::: pf-proof

If $f=0$, the result is immediate. Otherwise define
$$
g(x)=\frac{\overline{f(x)}\abs{f(x)}^{p-2}}{\norm{f}_p^{p-1}},
$$
with $g=0$ where $f=0$. Since $q=p/(p-1)$,
$$
\norm{g}_q^q
=\frac{\int \abs{f}^{(p-1)q}}{\norm{f}_p^{(p-1)q}}
=\frac{\int \abs{f}^p}{\norm{f}_p^p}=1.
$$
Moreover,
$$
\int fg
=\frac{\int \abs{f}^p}{\norm{f}_p^{p-1}}
=\norm{f}_p.
$$
Thus the supremum is at least $\norm{f}_p$, and Step 1 gives equality.

:::

:::

::: pf-step

Prove equality when $p=1$ and $q=\infty$.

::: pf-proof

If $f=0$, there is nothing to prove. Define the phase
$$
\theta(x)=
\begin{cases}
\overline{f(x)}/\abs{f(x)},&f(x)\ne0,\\
0,&f(x)=0.
\end{cases}
$$
Then $\norm{\theta}_\infty=1$ and
$$
\int f\theta=\int \abs{f}=\norm{f}_1.
$$
Hence the supremum equals $\norm{f}_1$.

:::

:::

::: pf-step

Prove equality when $p=\infty$ and $q=1$.

::: pf-proof

Let $M=\norm{f}_\infty$. If $M=0$, the result is immediate. Fix $\varepsilon\in(0,M)$. By the definition of essential supremum,
$$
A_\varepsilon:=\{x:\abs{f(x)}>M-\varepsilon\}
$$
has positive measure. Since Lebesgue measure on $\RR^n$ is sigma-finite, there is a measurable set
$$
E\subseteq A_\varepsilon,
\qquad
0<m(E)<\infty.
$$
Define
$$
g(x)=\frac{\theta(x)\mathbf1_E(x)}{m(E)},
\qquad
\theta(x)=
\begin{cases}
\overline{f(x)}/\abs{f(x)},&f(x)\ne0,\\
0,&f(x)=0.
\end{cases}
$$
Then $\norm{g}_1=1$ and
$$
\abs{\int fg}
=\frac1{m(E)}\int_E\abs{f(x)}\,dx
\ge M-\varepsilon.
$$
Letting $\varepsilon\downarrow0$ shows that the supremum is at least $M$. Step 1 gives the reverse inequality, hence equality.

:::

:::

::: pf-step

Conclude.

::: pf-proof

All conjugate pairs $1\le p,q\le\infty$ have been covered, so
$$
\boxed{
\norm{f}_p
=\sup_{\norm{g}_q=1}
\abs{\int_{\RR^n}f(x)g(x)\,dx}.}
$$

:::

:::

:::

:::
