---
schema: qual/card@1
id: PR-TC76W
kind: proposition
title: Counterexamples among uniform, pointwise, almost everywhere and $L^1$ convergence
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

(U) $f_n\to f$ [[D-YZC3C|uniformly]] on $\RR$;

(P) $f_n\to f$ [[D-IYDZU|pointwise]] on $\RR$, that is, $f_n(x)\to f(x)$ for every $x\in\RR$;

(AE) $f_n(x)\to f(x)$ for almost every $x\in\RR$;

(N) $f_n,f\in L^1(\RR)$ and $\norm{f_n-f}_1=\int_\RR\abs{f_n-f}\to0$.

Then (U) implies (P), and (P) implies (AE).
Neither implication reverses, none of (U), (P), (AE) implies (N), and (N) implies none of (U), (P), (AE).
:::

::: {.example}
The functions $f_n\coloneqq\frac1n\chi_{(0,n)}$ converge uniformly to $0$, but $\int_\RR f_n=1$ for all $n$, so they satisfy (U), (P), (AE) and not (N).

![image_2021-05-21-16-38-30](../../assets/figures/image_2021-05-21-16-38-30.png)
:::

::: {.example}
The functions $f_n\coloneqq\chi_{(n,n+1)}$ converge pointwise to $0$, but $\sup_\RR\abs{f_n}=1$ and $\norm{f_n}_1=1$ for all $n$, so they satisfy (P), (AE) and not (U), (N).

![image_2021-05-21-16-42-08](../../assets/figures/image_2021-05-21-16-42-08.png)
:::

::: {.example}
The functions $f_n\coloneqq n\chi_{[0,1/n]}$ converge to $0$ at every $x\neq0$ and diverge at $x=0$, and $\norm{f_n}_1=1$ for all $n$, so they satisfy (AE) and not (U), (P), (N).

![image_2021-05-21-16-54-38](../../assets/figures/image_2021-05-21-16-54-38.png)
:::

::: {.example}
For $k\geq1$ and $0\leq j<2^k$, let $I_{k,j}\coloneqq[j2^{-k},(j+1)2^{-k}]$, and enumerate the functions $\chi_{I_{k,j}}$ in the order of increasing $k$ and, for fixed $k$, increasing $j$, as $f_1,f_2,f_3,\ldots$, so $f_1=\chi_{[0,1/2]}$, $f_2=\chi_{[1/2,1]}$, $f_3=\chi_{[0,1/4]}$.
If $f_n=\chi_{I_{k,j}}$, then $\norm{f_n}_1=2^{-k}\to0$, so $f_n\to0$ in (N).
Every $x\in[0,1]$ lies in some $I_{k,j}$ and outside some $I_{k,j'}$ for each $k$, so $f_n(x)=1$ for infinitely many $n$ and $f_n(x)=0$ for infinitely many $n$; hence $(f_n)$ satisfies (N) and not (U), (P), (AE).

![image_2021-05-21-16-49-09](../../assets/figures/image_2021-05-21-16-49-09.png)
:::

::: {.example}
Almost everywhere convergence does not imply convergence in $L^p(\RR)$ for any $1\leq p\leq\infty$.
The functions $f_k\coloneqq\chi_{[k,k+1]}$ converge to $0$ at every point, but $\norm{f_k}_p=1$ for all $k$ and all $1\leq p\leq\infty$.
The functions $f_k\coloneqq k\chi_{[0,1/k]}$ converge to $0$ at every $x\neq0$, but $\norm{f_k}_p=k^{1-1/p}\geq1$ for $1\leq p<\infty$ and $\norm{f_k}_\infty=k$.
:::
