---
schema: qual/card@1
id: P-AE7QC
kind: problem
title: Weak $L^1$ and weak-$*$ $L^\infty$ convergence of $\exp(\sin(2\pi nx))$ on
  $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - L¹
  - L∞
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Checked part by part: periodicity and the bound e^{-1} <= f_n <= e; the exact period integral C = int_0^1 exp(sin 2 pi u) du; the computation on an interval via p = ceil(na), q = floor(nb), the identification of [a_n, b_n] as q - p periods, and the two remainder intervals of length below 1/n; the density family (finite linear combinations of interval indicators) and the three-term estimate with the constants e and e made explicit; and the order of the two limits (n -> infinity for fixed phi, then phi -> g). Two gaps filled: the interval computation did not say that [a_n, b_n] is a union of whole periods (it is, because a_n = p/n and b_n = q/n), and it did not handle a = b or note that half-open and open interval indicators differ from closed ones on null sets, which is what makes the stated dense family adequate. The answer C is the constant int_0^1 exp(sin 2 pi u) du in both parts. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Consider the following sequence of functions: $$f_n:[0,1]\to\RR \quad \text{by} \quad f_n(x) = \exp(\sin(2\pi n x)).$$

a. Prove that $f_n$ converges weakly in $L^1([0,1])$.

b. Prove that $f_n$ converges weak-$*$ in $L^\infty([0,1])$, viewed as the dual of $L^1([0,1])$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Put $f_n(x)=\exp\bigl(\sin(2\pi nx)\bigr)$ on $[0,1]$ and $C=\int_0^1\exp\bigl(\sin(2\pi u)\bigr)du$.

::: pf

::: {.pf-step #basic}
Each $f_n$ is $\frac1n$-periodic, measurable, and satisfies $e^{-1}\le f_n\le e$ pointwise.

::: pf-proof
$\sin\bigl(2\pi n(x+\frac1n)\bigr)=\sin(2\pi nx+2\pi)=\sin(2\pi nx)$, so $f_n$ is $\frac1n$-periodic. It is continuous, hence measurable, and $-1\le\sin\le1$ gives $e^{-1}\le f_n\le e$.
:::

:::

::: {.pf-step #constant}
$\displaystyle\int_0^1f_n(x)\,dx=C$ for every $n$.

::: pf-proof
Since $f_n$ is $\frac1n$-periodic, $\int_0^1f_n=n\int_0^{1/n}f_n$; substituting $u=nx$, $dx=du/n$, gives $n\int_0^{1/n}f_n(x)dx=n\cdot\frac1n\int_0^1\exp(\sin 2\pi u)du=C$.
:::

:::

::: {.pf-step #intervals}
For $0\le a\le b\le1$, $\displaystyle\int_a^bf_n\to C(b-a)$.

::: pf-proof
Let $g=\chi_{[a,b]}$; the case $a=b$ is trivial, so assume $a<b$. Put $p=\lceil na\rceil$, $q=\lfloor nb\rfloor$, $a_n=p/n$ and $b_n=q/n$; then $0\le a_n-a<\frac1n$ and $0\le b-b_n<\frac1n$, and for $n>\frac{2}{b-a}$ one has $b_n-a_n>(b-a)-\frac2n>0$.

::: {.pf-step #periods}
$\displaystyle\int_{a_n}^{b_n}f_n=(b_n-a_n)C$.

::: pf-proof
$a_n=p/n$ and $b_n=q/n$ with integers $p\le q$, so $[a_n,b_n]$ is the union of the $q-p$ intervals $[\frac kn,\frac{k+1}{n}]$, each of which is a period of $f_n$; each contributes $\int_k^{k+1\over n}f_n=\frac1n\int_0^1\exp(\sin2\pi u)du=C/n$ by the substitution of step [](#constant){.pf-ref}. Hence the integral is $(q-p)C/n=(b_n-a_n)C$.
:::

:::

::: {.pf-step #remainders}
$\abs{\displaystyle\int_a^{a_n}f_n}+\abs{\displaystyle\int_{b_n}^{b}f_n}\le\frac{2e}{n}$.

::: pf-proof
The two intervals have length less than $\frac1n$ each, and $\abs{f_n}\le e$ by step [](#basic){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #dense}
Finite linear combinations of characteristic functions of intervals $[a,b]\subseteq[0,1]$ are dense in $L^1([0,1])$.

::: pf-proof
Step functions are dense in $L^1([0,1])$, and a step function is a finite linear combination of characteristic functions of intervals whose endpoints may be taken in $[0,1]$; a uniform approximation of the endpoints is not needed: the indicator of $(a,b)$ differs from that of $[a,b]$ on a set of measure zero, and the indicator of a half-open interval differs from a closed one the same way. So the family named is dense.
:::

:::

::: {.pf-step #estimate}
For $g\in L^1([0,1])$, $\phi$ a finite linear combination of interval indicators, and every $n$,
$$
\abs{\int_0^1f_ng-C\int_0^1g}\le2e\norm{g-\phi}_{L^1}+\abs{\int_0^1f_n\phi-C\int_0^1\phi} .
$$

::: pf-proof
Insert $f_n\phi$ and $C\phi$:
$$
\int_0^1f_ng-C\int_0^1g=\int_0^1f_n(g-\phi)+\Bigl(\int_0^1f_n\phi-C\int_0^1\phi\Bigr)+C\int_0^1(\phi-g),
$$
and by the triangle inequality and $\abs{f_n}\le e$, $0<C\le e$ (steps [](#basic){.pf-ref}, [](#constant){.pf-ref}) the first and third terms are bounded by $e\norm{g-\phi}_1$ and $e\norm{\phi-g}_1$ respectively.
:::

:::

::: {.pf-step #partb}
$\displaystyle\int_0^1f_ng\to C\int_0^1g$ for every $g\in L^1([0,1])$; that is, $f_n\to C$ weak-$*$ in $L^\infty$ as the dual of $L^1$.

::: pf-proof
Fix $g\in L^1$ and $\varepsilon>0$. By step [](#dense){.pf-ref} choose a finite linear combination $\phi$ of interval indicators with $\norm{g-\phi}_1<\varepsilon/(4e)$; then the first term of step [](#estimate){.pf-ref} is below $\varepsilon/2$. By step [](#intervals){.pf-ref} and linearity, $\int f_n\phi\to C\int\phi$, so for all $n\ge N$ the second term is below $\varepsilon/2$. Hence $\abs{\int f_ng-C\int g}<\varepsilon$ for $n\ge N$. The constant $C$ lies in $L^\infty$ and $\int Cg=C\int g$ identifies it as the weak-$*$ limit.
:::

:::

::: {.pf-step #parta}
$f_n$ converges weakly in $L^1([0,1])$, with limit the constant $C$.

::: pf-proof
$L^\infty([0,1])\subseteq L^1([0,1])$ because the measure of $[0,1]$ is finite, and weak convergence in $L^1$ requires $\int f_ng\to\int Cg$ for all $g\in L^\infty$. Step [](#partb){.pf-ref} gives it for all $g\in L^1$, hence in particular for all $g\in L^\infty$; the limit $C$ is a constant, so it lies in $L^1$. That is part (a).
:::

:::

:::
:::
