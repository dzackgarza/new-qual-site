---
schema: qual/card@1
id: P-DGE5I
kind: problem
title: 'Cesàro means: convergence, divergent examples, and Tauberian converses'
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Series of Numbers
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-30
  note: 'Split from P-4FH62, where it was part (n).'
---

::: {.problem}
If $\theset{s_n}$ is a complex sequence, define its arithmetic means $\sigma_n$ by
$$
\sigma_n = \frac{s_0 + s_1 + \cdots + s_n}{n+1} \qquad (n = 0, 1, 2, \ldots).
$$

(a) If $\lim s_n = s$, prove that $\lim \sigma_n = s$.

(b) Construct a sequence $\theset{s_n}$ which does not converge, although $\lim \sigma_n = 0$.

(c) Can it happen that $s_n > 0$ for all $n$ and that $\limsup s_n = \infty$, although $\lim \sigma_n = 0$?

(d) Put $a_n = s_n - s_{n-1}$ for $n \geq 1$. Show that
$$
s_n - \sigma_n = \frac{1}{n+1}\sum_{k=1}^n ka_k.
$$
Assume that $\lim(na_n) = 0$ and that $\theset{\sigma_n}$ converges. Prove that $\theset{s_n}$ converges. This gives a converse of part (a), under the additional assumption that $na_n \to 0$.

(e) Derive the last conclusion from a weaker hypothesis: assume $M < \infty$, $\abs{na_n} \leq M$ for all $n$, and $\lim \sigma_n = \sigma$. Prove that $\lim s_n = \sigma$.
:::

::: {.solution}

::: pf

::: pf-step

The five claims about Cesàro means hold, and the answer to part (c) is $\boxed{\text{yes}}$.

::: pf-proof

::: pf-step

Part (a): If $s_n\to s$, then $\sigma_n\to s$.

::: pf-proof

Given $\varepsilon > 0$, choose $K$ with $\abs{s_k - s} < \varepsilon$ for $k > K$. Then $\abs{\sigma_n - s} \leq \frac{1}{n+1}\sum_{k \leq K}\abs{s_k - s} + \varepsilon$, and the first term tends to $0$.

:::

:::

::: pf-step

Part (b): $s_n=(-1)^n$ does not converge, while $\sigma_n\to0$.

::: pf-proof

$\abs{s_0 + \cdots + s_n} \leq 1$, so $\abs{\sigma_n} \leq 1/(n+1)$.

:::

:::

::: pf-step

Part (c): $s_{2^k}=k$ for $k \geq 1$ and $s_n=1/(n+1)$ for all other $n$ gives $s_n>0$, $\limsup s_n=\infty$ and $\sigma_n\to0$.

::: pf-proof

For $2^m\le n<2^{m+1}$,
$$
0<\sigma_n\le\frac{(1+2+\cdots+m) + \sum_{j=0}^n \frac{1}{j+1}}{n+1}\le\frac{m(m+1)/2 + 1 + \log(n+1)}{2^m}\to0.
$$

:::

:::

::: pf-step

Part (d): $s_n-\sigma_n=\frac1{n+1}\sum_{k=1}^nka_k$, and if $na_n\to0$ and $\sigma_n$ converges, then $s_n$ converges to the same limit.

::: pf-proof

$$
\sum_{k=1}^nka_k
=ns_n-\sum_{k=0}^{n-1}s_k
=(n+1)s_n-\sum_{k=0}^{n}s_k
=(n+1)(s_n-\sigma_n).
$$
If $na_n\to0$, then the averages $\frac1{n+1}\sum_{k=1}^nka_k$ tend to $0$ by part (a), so $s_n-\sigma_n\to0$.

:::

:::

::: pf-step

Part (e): If $\abs{na_n}\le M$ for all $n$ and $\sigma_n\to\sigma$, then $s_n\to\sigma$.

::: pf-proof

For $0 \leq m<n$, $(n+1)\sigma_n-(m+1)\sigma_m=\sum_{i=m+1}^n s_i$, and therefore
$$
s_n-\sigma_n=\frac{m+1}{n-m}(\sigma_n-\sigma_m)+\frac1{n-m}\sum_{i=m+1}^n(s_n-s_i).
$$
For $m<i\le n$, $\abs{s_n-s_i}\le\sum_{k=i+1}^n\abs{a_k}\le M\frac{n-i}{i+1}\le M\frac{n-m-1}{m+2}$. Fix $\varepsilon\in(0,1)$ and, for $n$ large, let $m$ be the integer with $m\le\frac{n-\varepsilon}{1+\varepsilon}<m+1$. The first inequality gives $\varepsilon(m+1)\le n-m$, so $\frac{m+1}{n-m}\le\frac1\varepsilon$; the second gives $n-m-1<\varepsilon(m+2)$, so $\frac{n-m-1}{m+2}<\varepsilon$. Hence
$$
\abs{s_n-\sigma_n}\le\frac1\varepsilon\abs{\sigma_n-\sigma_m}+M\varepsilon.
$$
As $n\to\infty$, $m\to\infty$ and $\sigma_n-\sigma_m\to0$, so $\limsup_n\abs{s_n-\sigma}\le M\varepsilon$. Since $\varepsilon$ is arbitrary, $s_n\to\sigma$.

:::

:::

:::

:::

:::

:::
