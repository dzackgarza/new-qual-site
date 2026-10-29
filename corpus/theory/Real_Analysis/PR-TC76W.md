---
schema: qual/card@1
id: PR-TC76W
kind: proposition
title: Counterexamples among uniform, pointwise, almost everywhere and $L^1$ convergence
slogan: 'Uniform implies pointwise implies almost everywhere, but no other implication among these and $L^1$ convergence holds in general.'
prompts:
- Give a sequence that converges uniformly, pointwise, and a.e., but not in $L^1$.
- Give a sequence that converges pointwise and a.e. but not uniformly or in $L^1$.
- Give a sequence of functions that converges pointwise but not in $L^1$.
- Give a sequence that converges a.e. but not in $L^1$, uniformly, or pointwise.
- Show that almost everywhere convergence does not imply $L^p$ convergence.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - L¹
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
Let $f_n,f\colon\RR\to\RR$ be Lebesgue measurable for $n\geq1$, and consider the following modes of convergence of $(f_n)$ to $f$:

- **(U)** $f_n\to f$ [[D-YZC3C|uniformly]] on $\RR$;
- **(P)** $f_n\to f$ [[D-IYDZU|pointwise]] on $\RR$, that is, $f_n(x)\to f(x)$ for every $x\in\RR$;
- **(AE)** $f_n(x)\to f(x)$ for almost every $x\in\RR$;
- **(N)** $f_n,f\in L^1(\RR)$ and $\norm{f_n-f}_1=\int_\RR\abs{f_n-f}\to0$.

Then (U) implies (P), and (P) implies (AE).
Neither implication reverses, none of (U), (P), (AE) implies (N), and (N) implies none of (U), (P), (AE).
:::

::: {.example}
The functions $f_n\coloneqq\frac1n\chi_{(0,n)}$ converge uniformly to $0$, but $\int_\RR f_n=1$ for all $n$, so they satisfy (U), (P), (AE) and not (N).

![Graph of $f_n = \frac1n\chi_{(0,n)}$: a rectangle of height $1/n$ over $(0,n)$, of area $1$](../../assets/figures/image_2021-05-21-16-38-30.png)
:::

::: {.example}
The functions $f_n\coloneqq\chi_{(n,n+1)}$ converge pointwise to $0$, but $\sup_\RR\abs{f_n}=1$ and $\norm{f_n}_1=1$ for all $n$, so they satisfy (P), (AE) and not (U), (N).

![Graphs of $f_1, f_2, f_3, f_4$: unit-height rectangles over the adjacent intervals $(1,2), (2,3), (3,4), (4,5)$, each of area $1$, moving to the right](../../assets/figures/image_2021-05-21-16-42-08.png)
:::

::: {.example}
The functions $f_n\coloneqq n\chi_{[0,1/n]}$ converge to $0$ at every $x\neq0$ and diverge at $x=0$, and $\norm{f_n}_1=1$ for all $n$, so they satisfy (AE) and not (U), (P), (N).

![Graph of $f_n = n\chi_{[0,1/n]}$: a rectangle of height $n$ over $[0,1/n]$, of area $1$](../../assets/figures/image_2021-05-21-16-54-38.png)
:::

::: {.example}
For $k\geq1$ and $0\leq j<2^k$, let $I_{k,j}\coloneqq[j2^{-k},(j+1)2^{-k}]$, and enumerate the functions $\chi_{I_{k,j}}$ in the order of increasing $k$ and, for fixed $k$, increasing $j$, as $f_1,f_2,f_3,\ldots$, so $f_1=\chi_{[0,1/2]}$, $f_2=\chi_{[1/2,1]}$, $f_3=\chi_{[0,1/4]}$.
If $f_n=\chi_{I_{k,j}}$, then $\norm{f_n}_1=2^{-k}\to0$, so $f_n\to0$ in (N).
Every $x\in[0,1]$ lies in some $I_{k,j}$ and outside some $I_{k,j'}$ for each $k$, so $f_n(x)=1$ for infinitely many $n$ and $f_n(x)=0$ for infinitely many $n$; hence $(f_n)$ satisfies (N) and not (U), (P), (AE).

![Graphs of $f_1, \ldots, f_6$: unit-height indicators of $[0,1/2]$, $[1/2,1]$, then $[0,1/4]$, $[1/4,1/2]$, $[1/2,3/4]$, $[3/4,1]$, sweeping across $[0,1]$ with halving width](../../assets/figures/image_2021-05-21-16-49-09.png)
:::

::: {.remark title="Variations"}
Almost everywhere convergence does not imply $L^p$ convergence for any $1\le p\le\infty$: the sequence $\chi_{(n,n+1)}$ tends to $0$ everywhere with $\norm{\chi_{(n,n+1)}}_p=1$, and the spikes $n\chi_{[0,1/n]}$ tend to $0$ almost everywhere with $\norm{n\chi_{[0,1/n]}}_p=n^{1-1/p}\geq1$ for $1\le p<\infty$ and $\norm{n\chi_{[0,1/n]}}_\infty=n$.

Over the open interval, $n\chi_{(0,1/n)}$ converges to $0$ at every $x\in\RR$, including $x=0$, and still has integral $1$: it satisfies (P) and (AE) and not (U), (N).
:::
