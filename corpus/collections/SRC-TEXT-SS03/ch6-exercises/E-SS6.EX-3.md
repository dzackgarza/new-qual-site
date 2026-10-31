---
schema: qual/card@1
id: E-SS6.EX-3
kind: problem
title: Wallis's product and the duplication formula for $\Gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Infinite Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
Show that Wallis’s product formula can be written as

$$
\sqrt{\frac{\pi}{2}} = \lim_{n \to \infty} \frac{2^{2n} (n!)^{2}}{(2n + 1)!} (2n + 1)^{1/2}.
$$

As a result, prove the following identity:

$$
\Gamma(s) \Gamma(s + 1/2) = \sqrt{\pi}\, 2^{1 - 2s} \Gamma(2s).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Wallis's product is $\frac{\pi}{2} = \prod_{k=1}^{\infty} \frac{4k^2}{4k^2 - 1} = \lim_{n \to \infty} \frac{2^{4n}(n!)^4}{((2n)!)^2 (2n+1)}$.

::: pf-proof

The $n$-th partial product is $\prod_{k=1}^{n} \frac{(2k)^2}{(2k-1)(2k+1)} = \frac{(2^n n!)^4}{((2n)!)^2(2n+1)}$, since $\prod_{k=1}^n 2k = 2^n n!$ and $\prod_{k=1}^n (2k-1) = (2n)!/(2^n n!)$.

:::

:::

::: {.pf-step #s2}

$\sqrt{\frac{\pi}{2}} = \lim_{n \to \infty} \frac{2^{2n}(n!)^2}{(2n+1)!}(2n+1)^{1/2}$.

::: pf-proof

Take square roots in Step [](#s1){.pf-ref} and use $(2n)!\,(2n+1)^{1/2} = (2n+1)!\,(2n+1)^{-1/2}$.

:::

:::

::: {.pf-step #s3}

For $s \notin \{0, -1, -2, \ldots\}$, $\Gamma(s) = \lim_{n\to\infty} \frac{n^s (n-1)!}{s(s+1)\cdots(s+n-1)}$.

::: pf-proof

Exercise 1 gives $\Gamma(s) = \lim_n \frac{n^s n!}{s(s+1)\cdots(s+n)}$, and that expression is the one above times $\frac{n}{s+n} \to 1$.

:::

:::

::: {.pf-step #s4}

Let $2s \notin \{0, -1, -2, \ldots\}$. Then $\frac{\Gamma(s)\Gamma(s+1/2)}{\Gamma(2s)} = 2^{-2s} L$, where $L = \lim_{n\to\infty} \frac{2^{2n}((n-1)!)^2\, n^{1/2}}{(2n-1)!}$ exists.

::: pf-proof

Apply Step [](#s3){.pf-ref} to $s$ and to $s + 1/2$ with $n$ factors, and to $2s$ with $2n$ factors. The denominators satisfy
$$
2s(2s+1)\cdots(2s+2n-1) = 2^{2n} \prod_{k=0}^{n-1} (s+k)\left(s+k+\tfrac12\right),
$$
so the quotient of the three approximants is
$$
\frac{n^{s}\, n^{s+1/2} ((n-1)!)^2\, 2^{2n}}{(2n)^{2s} (2n-1)!} = 2^{-2s}\, \frac{2^{2n}((n-1)!)^2 n^{1/2}}{(2n-1)!}.
$$
The left side converges because each approximant converges and $\Gamma(2s) \ne 0$, so the right side converges.

:::

:::

::: {.pf-step #s5}

$L = 2\sqrt{\pi}$.

::: pf-proof

With $(n-1)! = n!/n$ and $(2n-1)! = (2n+1)!/(2n(2n+1))$,
$$
\frac{2^{2n}((n-1)!)^2 n^{1/2}}{(2n-1)!} = \left[\frac{2^{2n}(n!)^2}{(2n+1)!}(2n+1)^{1/2}\right] \cdot \frac{2(2n+1)^{1/2}}{n^{1/2}}.
$$
By Step [](#s2){.pf-ref} the bracket tends to $\sqrt{\pi/2}$, and the last factor tends to $2\sqrt2$.

:::

:::

::: {.pf-step #s6}

$\Gamma(s)\Gamma(s+1/2) = \sqrt{\pi}\, 2^{1-2s}\, \Gamma(2s)$ as meromorphic functions on $\CC$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the identity on the connected open set where $2s \notin \{0,-1,-2,\ldots\}$. Both sides are meromorphic on $\CC$, so the identity theorem extends it.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

:::
