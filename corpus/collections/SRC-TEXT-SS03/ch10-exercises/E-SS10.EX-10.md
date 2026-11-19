---
schema: qual/card@1
id: E-SS10.EX-10
kind: problem
title: Irregular growth of $r_2(n)$ and $r_4(n)$
classification:
  areas:
  - complex-analysis
  topics:
  - Number Theory
  - Theta Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a statement or hint transcription defect before solving.
---

::: {.exercise}
Observe the following irregularities of the functions $r_2(n)$ and $r_4(n)$ as $n$ becomes large:

(a) $r_2(n) = 0$ for infinitely many $n$, while $\limsup_{n \to \infty} r_2(n) = \infty$,

(b) $r_4(n) = 24$ for infinitely many $n$ while $\limsup_{n \to \infty} r_4(n)/n = \infty$.

[Hint: For (a) consider $n = 5^k$; for (b) consider alternatively $n = 2^k$, and $n = q^k$ where $q$ is odd and large.]
:::

::: {.remark}
The hint's second family does not give the $\limsup$: for an odd prime $q$, $r_4(q^k)/q^k = 8(1 + q^{-1} + \cdots + q^{-k}) < 8q/(q-1) \le 12$. The solution uses products of the first $k$ odd primes.
:::

::: {.solution}
By the two-squares and four-squares theorems,
$$
r_2(n)=4\bigl(d_1(n)-d_3(n)\bigr),
\qquad
r_4(n)=8\sum_{\substack{d\mid n\\4\nmid d}}d,
\tag{1}
$$
where $d_j(n)$ counts divisors congruent to $j\pmod4$.

For part (a), if $n=3^{2k+1}$, the divisors are $1,3,3^2,\ldots,3^{2k+1}$; exactly $k+1$ are $1\pmod4$ and $k+1$ are $3\pmod4$. Hence $r_2(3^{2k+1})=0$, giving infinitely many zeros.

On the other hand, for $n=5^k$, every divisor is $1\pmod4$, so
$$
r_2(5^k)=4(k+1)\longrightarrow\infty.
$$
Thus $\limsup r_2(n)=\infty$.

For part (b), if $n=2^k$ with $k\ge1$, the only divisors not divisible by $4$ are $1$ and $2$. Therefore
$$
r_4(2^k)=8(1+2)=24,
$$
so the value $24$ occurs infinitely often.

To make $r_4(n)/n$ arbitrarily large, let
$$
n_k=p_1p_2\cdots p_k
$$
be the product of the first $k$ odd primes. Since $n_k$ is odd and squarefree, (1) gives
$$
\frac{r_4(n_k)}{n_k}
=8\frac{\prod_{j=1}^k(1+p_j)}{\prod_{j=1}^kp_j}
=8\prod_{j=1}^k\left(1+\frac1{p_j}\right).
$$
The product diverges: indeed $\log(1+1/p)\ge 1/(2p)$ for $p\ge2$, and Euler's theorem $\sum_p1/p=\infty$ implies
$$
\sum_j\log\left(1+\frac1{p_j}\right)=\infty.
$$
Hence
$$
\limsup_{n\to\infty}\frac{r_4(n)}n=\infty.
$$
:::
::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. The cited input is the pair of classical formulae
$$
r_2(n)=4\bigl(d_1(n)-d_3(n)\bigr),\qquad r_4(n)=8\sum_{\substack{d\mid n\\ 4\nmid d}}d,
\tag{1}
$$
where $d_1(n)$ and $d_3(n)$ count the divisors of $n$ congruent to $1$ and to $3$ modulo $4$; these are the two-squares and four-squares theorems.

::: pf

::: {.pf-step #formulae}
Both identities in (1) hold for every $n\ge1$.

::: pf-proof
The two-squares theorem states that $r_2(n)=4(d_1(n)-d_3(n))$, the number of representations of $n$ as a sum of two squares being four times the excess of the divisors $1\bmod4$ over the divisors $3\bmod4$. Jacobi's four-squares theorem states $r_4(n)=8\sum_{d\mid n,4\nmid d}d$. Both are cited as the classical theorems; the exercise asks for consequences of them.
:::

:::

::: {.pf-step #zero}
(a) $r_2(n)=0$ for infinitely many $n$.

::: pf-proof
Take $n=3^{2k+1}$, whose divisors are $3^j$ with $0\le j\le2k+1$. Such a power is $\equiv1\pmod4$ exactly when $j$ is even, so among the $2k+2$ divisors exactly $k+1$ are $1\bmod4$ and $k+1$ are $3\bmod4$; the difference vanishes and (1) gives $r_2(3^{2k+1})=0$. The numbers $3^{2k+1}$ are distinct for distinct $k$, so this happens infinitely often.
:::

:::

::: {.pf-step #unbounded}
(a) $\limsup_{n\to\infty}r_2(n)=\infty$.

::: pf-proof
Take $n=5^k$. Every divisor $5^j$ is $\equiv1\pmod4$, so $d_1(5^k)=k+1$ and $d_3(5^k)=0$, giving $r_2(5^k)=4(k+1)$. This tends to infinity along the sequence $n=5^k$, which is exactly what makes the limit superior infinite.
:::

:::

::: {.pf-step #twentyfour}
(b) $r_4(n)=24$ for infinitely many $n$.

::: pf-proof
Take $n=2^k$ with $k\ge2$. The divisors of $2^k$ not divisible by $4$ are $1$ and $2$, so the sum in (1) is $3$ and $r_4(2^k)=24$ for every $k\ge2$; there are infinitely many such $k$.
:::

:::

::: {.pf-step #ratio}
(b) $\limsup_{n\to\infty}r_4(n)/n=\infty$.

::: pf-proof
Let $n_k=p_1\cdots p_k$ be the product of the first $k$ odd primes, which is odd and squarefree. Since $n_k$ is odd, no divisor is divisible by $4$, so the sum in (1) is $\sigma(n_k)=\prod_{j\le k}(1+p_j)$, and
$$
\frac{r_4(n_k)}{n_k}=8\prod_{j=1}^{k}\frac{1+p_j}{p_j}=8\prod_{j=1}^{k}\Bigl(1+\frac1{p_j}\Bigr).
$$
The product diverges: $\log(1+1/p)\ge\frac1{2p}$ for $p\ge2$, so the logarithm of the product is at least $\frac12\sum_{j\le k}1/p_j$, and Euler's theorem that $\sum_p1/p$ diverges makes this tend to infinity. Hence $r_4(n_k)/n_k\to\infty$ along this sequence and the limit superior is infinite. This is exactly why the card's remark replaces the hint's second family $q^k$: there the ratio stays bounded by $8q/(q-1)$.
:::

:::

:::

:::
