---
schema: qual/card@1
id: P-7UIYI
kind: problem
title: $\lim|a_{n+1}/a_n|=L$ implies $\lim|a_n|^{1/n}=L$, and the ratio test for the
  radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Power Series
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $a_n\neq 0$ and show that
\[
\lim_{n\to \infty} {\abs{a_{n+1}} \over \abs{a_n}} = L \implies \lim_{n\to\infty} \abs{a_n}^{1\over n} = L
.\]
In particular, this shows that when applicable, the ratio test can be used to calculate the radius of convergence of a power series.
:::

::: {.solution}
<1>1. Put $r_n = \abs{a_{n+1}}/\abs{a_n}$. Then $r_n>0$ and $r_n \to L$.

::: {.proof}
The quotient is defined and positive because every $a_n\neq0$; its limit is $L$ by hypothesis.
:::

<1>2. For any $\varepsilon > 0$, put $\ell=\max\{L-\varepsilon,0\}$. There is $N$ such that $\ell \le r_n < L + \varepsilon$ for all $n \ge N$.

::: {.proof}
Since $r_n\to L$, there is $N$ with $L-\varepsilon<r_n<L+\varepsilon$ for $n\ge N$. Together with $r_n>0$ from step <1>1, this gives $\ell\le r_n$.
:::

<1>3. For $n > N$,
$$\abs{a_N}\,\ell^{n-N} \le \abs{a_n} < \abs{a_N}(L + \varepsilon)^{n-N}.$$

::: {.proof}
The product telescopes: $\abs{a_n} = \abs{a_N} \prod_{k=N}^{n-1} r_k$. Bound each factor $r_k$ by step <1>2.
:::

<1>4. One has
$$L - \varepsilon \le \ell \le \liminf_{n\to\infty} \abs{a_n}^{1/n} \le \limsup_{n\to\infty} \abs{a_n}^{1/n} \le L + \varepsilon.$$

::: {.proof}
Take $n$th roots in step <1>3 and let $n\to\infty$. Since $a_N\neq0$, $\abs{a_N}^{1/n} \to 1$, and $c^{(n-N)/n} \to c$ for every $c>0$. If $\ell=0$, the lower bound is $0\le\liminf\abs{a_n}^{1/n}$.
:::

<1>5. One has $\lim_{n\to\infty} \abs{a_n}^{1/n} = \boxed{L}$.

::: {.proof}
Step <1>4 holds for every $\varepsilon > 0$. Letting $\varepsilon\to0$ gives $L\le\liminf\abs{a_n}^{1/n}\le\limsup\abs{a_n}^{1/n}\le L$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required limit.
:::
:::
