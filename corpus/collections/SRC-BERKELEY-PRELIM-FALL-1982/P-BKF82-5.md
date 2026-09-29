---
schema: qual/card@1
id: P-BKF82-5
kind: problem
title: Moment convergence implies convergence against continuous functions
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used bounded total masses from the k=0 moment, Weierstrass approximation, and convergence for polynomials to prove the continuous test integrals are Cauchy."
---

::: {.problem}
Let $\varphi_n\ge0$ be continuous on $[0,1]$ and suppose
\[
\lim_{n\to\infty}\int_0^1x^k\varphi_n(x)\,dx
\]
exists for every $k\ge0$. Show that
\[
\lim_{n\to\infty}\int_0^1f(x)\varphi_n(x)\,dx
\]
exists for every continuous $f$ on $[0,1]$.
:::

::: {.solution}
Put
$$
I_n(g)=\int_0^1 g(x)\varphi_n(x)\,dx.
$$

::: pf

::: {.pf-step #s1}

The total masses $I_n(1)$ are uniformly bounded.

::: pf-proof

The hypothesis for $k=0$ says that
$$
I_n(1)=\int_0^1\varphi_n(x)\,dx
$$
converges. Hence there is a constant $M>0$ such that
$$
I_n(1)\le M
$$
for every $n$. Since $\varphi_n\ge0$, for every continuous $g$,
$$
|I_n(g)|
\le \|g\|_\infty I_n(1)
\le M\|g\|_\infty.
$$

:::

:::

::: {.pf-step #s2}

The sequence $I_n(p)$ converges for every polynomial $p$.

::: pf-proof

If
$$
p(x)=\sum_{k=0}^d c_kx^k,
$$
then
$$
I_n(p)=\sum_{k=0}^d c_k I_n(x^k).
$$
Each moment on the right converges by hypothesis, and the sum is finite.
Therefore $I_n(p)$ converges.

:::

:::

::: pf-step

For every continuous $f$, the sequence $I_n(f)$ is Cauchy.

::: pf-proof

Let $\varepsilon>0$. By the Weierstrass approximation theorem, choose a
polynomial $p$ such that
$$
\|f-p\|_\infty<\frac{\varepsilon}{3M}.
$$
By step [](#s2){.pf-ref}, $I_n(p)$ converges, so there is $N$ such that for
$m,n\ge N$,
$$
|I_n(p)-I_m(p)|<\frac\varepsilon3.
$$
Then step [](#s1){.pf-ref} gives
$$
\begin{aligned}
|I_n(f)-I_m(f)|
&\le |I_n(f-p)|+|I_n(p)-I_m(p)|+|I_m(p-f)|\\
&\le M\|f-p\|_\infty+\frac\varepsilon3+M\|f-p\|_\infty\\
&<\varepsilon.
\end{aligned}
$$
Thus $(I_n(f))$ is Cauchy in $\mathbb R$.

:::

:::

::: pf-step

Conclude convergence.

::: pf-proof

The real numbers are complete, so the Cauchy sequence $I_n(f)$ converges.
Hence for every $f\in C([0,1])$,
$$
\boxed{
\lim_{n\to\infty}\int_0^1 f(x)\varphi_n(x)\,dx
\text{ exists}.}
$$

:::

:::

:::

:::
