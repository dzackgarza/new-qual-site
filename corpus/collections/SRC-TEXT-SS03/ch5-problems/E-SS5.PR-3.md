---
schema: qual/card@1
id: E-SS5.PR-3
kind: problem
title: Order of an entire function with coefficients $(n!)^{-\alpha}$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured both bounds into numbered steps and supplied the estimates that were quoted: the
    radius from the ratio 1/(n+1)^alpha, the Stirling lower bound n! >= (n/e)^n used to produce the
    term bound (eR/n)^{alpha n} with R = r^{1/alpha}, the one-variable maximisation of
    x(1 + log R - log x) at x = R with value R, the split at N = ceil(2eR) against the geometric
    tail, and for the lower bound the minimisation of A e^{B r^sigma} r^{-n} at
    r = (n/(B sigma))^{1/sigma} together with the two Stirling asymptotics that are compared.
    Every macro used is one the preamble defines. Not checked this session: the printed statement
    page.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The printed statement page is now read: Chapter 5, Problem 3 on printed p. 157 (PDF p. 176)
    reads "Show that $\sum z^n/(n!)^\alpha$ is an entire function of order $1/\alpha$", with the
    asterisk before "3.", and the card's block is that sentence. One repair in step s6: the
    minimisation of $Ae^{Br^\sigma}r^{-n}$ at $r_n=(n/(B\sigma))^{1/\sigma}$ gives $Br^\sigma=n/\sigma$,
    and the card printed $+n$ where the substitution yields $+n/\sigma$; for $\sigma<1$, which is the
    case the step is used in when $\alpha>1$, that is a stronger bound than the estimate delivers.
    The term is now $n/\sigma$, and the conclusion $\log(n!)^\alpha\ge(n/\sigma)\log n+O(n)$ is
    unchanged. The rest was read and holds: the ratio $1/(n+1)^\alpha$, the Stirling lower bound,
    the maximum of $x(1+\log R-\log x)$ at $x=R$, the split at $\lceil2eR\rceil$, and the upper
    bound $M_F(r)\le Ce^{C'r^{1/\alpha}}$.

---

::: {.exercise}
Show that

$$
\sum_{n=0}^{\infty}\frac{z^n}{(n!)^\alpha}
$$

is an entire function of order $1/\alpha$.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 5, Problem 3).
:::

::: {.solution}

The argument is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Let $\alpha>0$, $a_{n}=(n!)^{-\alpha}$ and $F(z)=\sum_{n\geq0}a_{n}z^{n}$. Recall that the order of an entire $F$ is $\rho=\limsup_{r\to\infty}\frac{\log\log M_{F}(r)}{\log r}$ with $M_{F}(r)=\max_{\abs{z}\leq r}\abs{F(z)}$; $\rho\leq\sigma$ holds exactly when $M_{F}(r)\leq Ae^{Br^{\sigma}}$ for some constants and all large $r$.

::: pf

::: {.pf-step #entire}
$F$ is entire.

::: pf-proof
$\abs{a_{n+1}/a_{n}}=\bigl(n!/(n+1)!\bigr)^{\alpha}=(n+1)^{-\alpha}\to0$, so the radius of convergence is infinite and $F$ is entire.
:::

:::

::: {.pf-step #term}
For $R=r^{1/\alpha}$ and every $n\geq1$, $\dfrac{r^{n}}{(n!)^{\alpha}}\leq\Bigl(\dfrac{eR}{n}\Bigr)^{\alpha n}$.

::: pf-proof
Stirling's lower bound $n!\geq(n/e)^{n}$ gives $(n!)^{\alpha}\geq(n/e)^{\alpha n}$, hence $\frac{r^{n}}{(n!)^{\alpha}}\leq\frac{r^{n}e^{\alpha n}}{n^{\alpha n}}=\bigl(\frac{r^{1/\alpha}e}{n}\bigr)^{\alpha n}$, which is the assertion with $R=r^{1/\alpha}$.
:::

:::

::: {.pf-step #maximise}
The function $h(x)=x(1+\log R-\log x)$ on $x>0$ has maximum $R$.

::: pf-proof
$h'(x)=1+\log R-\log x-1=\log(R/x)$, positive for $x<R$ and negative for $x>R$, so $h$ increases then decreases with its maximum at $x=R$, where $h(R)=R$.
:::

:::

::: {.pf-step #upper-term}
Every term of the series satisfies $\dfrac{r^{n}}{(n!)^{\alpha}}\leq e^{\alpha R}$.

::: pf-proof
$\bigl(\frac{eR}{n}\bigr)^{\alpha n}=\exp\bigl(\alpha n\log\frac{eR}{n}\bigr)=\exp\bigl(\alpha h(n)\bigr)\leq e^{\alpha R}$ by step [](#maximise){.pf-ref}, and step [](#term){.pf-ref} bounds the term by this quantity.
:::

:::

::: {.pf-step #tail}
With $N=\lceil2eR\rceil$, $\sum_{n>N}\frac{r^{n}}{(n!)^{\alpha}}\leq\sum_{n>N}2^{-\alpha n}<\infty$.

::: pf-proof
For $n>N\geq2eR$ we have $eR/n<1/2$, so step [](#term){.pf-ref} gives the term at most $(1/2)^{\alpha n}=2^{-\alpha n}$, and the geometric series with ratio $2^{-\alpha}<1$ converges.
:::

:::

::: {.pf-step #upper}
$M_{F}(r)\leq Ce^{C'r^{1/\alpha}}$ for constants $C,C'$, so the order is at most $1/\alpha$.

::: pf-proof
Since all coefficients are positive, $\abs{F(z)}\leq\sum_{n}\abs{a_{n}}\abs{z}^{n}=F(\abs{z})$, so $M_{F}(r)\leq F(r)$. Splitting the sum at $N$, the first $N+1$ terms are at most $e^{\alpha R}$ each by step [](#upper-term){.pf-ref} and the tail is bounded by a constant by step [](#tail){.pf-ref}, so $F(r)\leq(N+1)e^{\alpha R}+K\leq Ce^{C'R}$ for suitable constants, using $N+1\leq3eR$ for large $R$. With $R=r^{1/\alpha}$ this is $\log M_{F}(r)\leq C'r^{1/\alpha}+O(1)$, hence $\rho\leq1/\alpha$.
:::

:::

::: {.pf-step #cauchy}
If $M_{F}(r)\leq Ae^{Br^{\sigma}}$ for all large $r$, then $\alpha\geq1/\sigma$.

::: pf-proof
Cauchy's estimate for the Taylor coefficient gives $\frac{1}{(n!)^{\alpha}}=\abs{a_{n}}\leq\frac{M_{F}(r)}{r^{n}}\leq\frac{Ae^{Br^{\sigma}}}{r^{n}}$ for every $r>0$. The right side, as a function of $r$, has logarithmic derivative $B\sigma r^{\sigma-1}-n/r$, which vanishes at $r_{n}=(n/(B\sigma))^{1/\sigma}$ and changes sign from negative to positive there, so $r_{n}$ gives the minimum. Substituting,
$$
\log\frac{1}{(n!)^{\alpha}}\leq\log A+\frac{n}{\sigma}-\frac{n}{\sigma}\log n+\frac{n}{\sigma}\log(B\sigma),
$$
that is $\log(n!)^{\alpha}\geq\frac{n}{\sigma}\log n+O(n)$. Stirling's formula gives $\log(n!)^{\alpha}=\alpha n\log n+O(n)$, so
$$
\alpha n\log n+O(n)\geq\frac{n}{\sigma}\log n+O(n),
$$
which after dividing by $n\log n$ and letting $n\to\infty$ yields $\alpha\geq1/\sigma$.
:::

:::

::: {.pf-step #lower}
The order is not less than $1/\alpha$.

::: pf-proof
Suppose $\rho<1/\alpha$ and choose $\sigma$ with $\rho<\sigma<1/\alpha$. By the definition of order, $M_{F}(r)\leq Ae^{Br^{\sigma}}$ for all large $r$, so step [](#cauchy){.pf-ref} gives $\alpha\geq1/\sigma$. But $\sigma<1/\alpha$ is equivalent to $1/\sigma>\alpha$, and $\alpha\geq1/\sigma$ and $1/\sigma>\alpha$ cannot both hold. Hence no such $\sigma$ exists and $\rho\geq1/\alpha$.
:::

:::

::: {.pf-step}
$\rho=1/\alpha$: the series defines an entire function of order $1/\alpha$.

::: pf-proof
Steps [](#entire){.pf-ref}, [](#upper){.pf-ref} and [](#lower){.pf-ref}.
:::

:::

:::

:::
