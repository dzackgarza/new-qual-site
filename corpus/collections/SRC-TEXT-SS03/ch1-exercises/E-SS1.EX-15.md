---
schema: qual/card@1
id: E-SS1.EX-15
kind: problem
title: Abel's theorem for convergent series
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: exercise
Suppose $\sum_{n=1}^{\infty}a_n$ converges. Prove that
\[
\lim_{r\to1^-}\sum_{n=1}^{\infty}r^na_n
=
\sum_{n=1}^{\infty}a_n.
\]
In other words, a convergent series is Abel summable to its ordinary sum.
:::

::: {.solution}
<1>1. Let
\[
s_n=\sum_{k=1}^n a_k,
\qquad
s=\sum_{k=1}^{\infty}a_k.
\]
Then $(s_n)$ is bounded and $s_n\to s$.
::: {.proof}
Convergence of the series means exactly that its sequence of partial sums converges to $s$. Every convergent sequence is bounded.
:::

<1>2. For $0\le r<1$ and every $N\ge1$,
\[
\sum_{n=1}^N a_nr^n
=s_Nr^N+(1-r)\sum_{n=1}^{N-1}s_nr^n.
\]
::: {.proof}
Since $a_n=s_n-s_{n-1}$ with $s_0=0$,
\[
\begin{aligned}
\sum_{n=1}^N a_nr^n
&=\sum_{n=1}^N(s_n-s_{n-1})r^n\\
&=\sum_{n=1}^Ns_nr^n-r\sum_{n=0}^{N-1}s_nr^n\\
&=s_Nr^N+(1-r)\sum_{n=1}^{N-1}s_nr^n.
\end{aligned}
\]
This is the summation-by-parts identity specialized to $a_n=r^n$.
:::

<1>3. For every $0\le r<1$,
\[
\sum_{n=1}^{\infty}a_nr^n
=(1-r)\sum_{n=1}^{\infty}s_nr^n.
\]
::: {.proof}
By <1>1 there is $C$ with $|s_n|\le C$. Hence $|s_Nr^N|\le Cr^N\to0$ and the series $\sum s_nr^n$ converges absolutely. Letting $N\to\infty$ in <1>2 gives the identity.
:::

<1>4. For $0\le r<1$,
\[
(1-r)\sum_{n=1}^{\infty}s_nr^n
=sr+(1-r)\sum_{n=1}^{\infty}(s_n-s)r^n.
\]
::: {.proof}
Write $s_n=s+(s_n-s)$ and use
\[
(1-r)\sum_{n=1}^{\infty}r^n=r.
\]
:::

<1>5. One has
\[
\lim_{r\to1^-}(1-r)\sum_{n=1}^{\infty}(s_n-s)r^n=0.
\]
::: {.proof}
Fix $\varepsilon>0$. Choose $N$ so that $|s_n-s|<\varepsilon$ for every $n\ge N$. Then
\[
\begin{aligned}
(1-r)\sum_{n=1}^{\infty}|s_n-s|r^n
&\le
(1-r)\sum_{n=1}^{N-1}|s_n-s|r^n
+\varepsilon(1-r)\sum_{n=N}^{\infty}r^n\\
&\le
(1-r)\sum_{n=1}^{N-1}|s_n-s|
+\varepsilon.
\end{aligned}
\]
The first term tends to $0$ as $r\to1^-$ because it is $(1-r)$ times a fixed finite constant. Thus the limsup is at most $\varepsilon$. Since $\varepsilon$ is arbitrary, the asserted limit is $0$.
:::

<1>6. Therefore
\[
\lim_{r\to1^-}\sum_{n=1}^{\infty}a_nr^n=s.
\]
::: {.proof}
By <1>3 and <1>4,
\[
\sum_{n=1}^{\infty}a_nr^n
=sr+(1-r)\sum_{n=1}^{\infty}(s_n-s)r^n.
\]
The first term tends to $s$, and the second tends to $0$ by <1>5.
:::
:::
