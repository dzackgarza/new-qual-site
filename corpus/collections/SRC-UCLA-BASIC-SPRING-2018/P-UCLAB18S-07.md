---
schema: qual/card@1
id: P-UCLAB18S-07
kind: problem
title: Convergence of $\sum_n \sin(\pi n/p)/n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Prove that for every $p\in\NN$, the series
$$
\sum_{n=1}^{\infty}\frac{\sin(\pi n/p)}{n}
$$
converges.
:::

::: {.solution}

Fix $p\in\NN$, and set $a_n=\sin(\pi n/p)$ and $A_N=\sum_{n=1}^N a_n$.

::: pf

::: {.pf-step #s1-1}

If $p=1$, then the series converges.


::: pf-proof

For every $n\ge 1$, $a_n=\sin(\pi n)=0$. Hence every partial sum of the given series is zero.

:::

:::

::: {.pf-step #s1-2}

Suppose $p\ge 2$. Then the partial sums $A_N$ are bounded independently of $N$.


::: pf-proof

Let $q=e^{i\pi/p}$. Since $p\ge 2$, $q\ne 1$. Therefore
$$
\sum_{n=1}^N q^n
=q\frac{1-q^N}{1-q}.
$$
Taking imaginary parts gives
$$
A_N=\operatorname{Im}\left(q\frac{1-q^N}{1-q}\right).
$$
Since $\abs{q}=1$ and $\abs{1-q^N}\le 2$,
$$
\abs{A_N}\le \frac{2}{\abs{1-q}}
$$
for every $N$. Thus there is a constant $M>0$, depending only on $p$, such that $\abs{A_N}\le M$ for all $N$.

:::

:::

::: {.pf-step #s1-3}

Suppose $p\ge 2$. For integers $N\ge m\ge 1$,
$$
\abs{\sum_{n=m}^N\frac{a_n}{n}}\le \frac{2M}{m},
$$
where $M$ is as in step [](#s1-2){.pf-ref}.


::: pf-proof

Abel summation gives
$$
\sum_{n=m}^N\frac{a_n}{n}
=\frac{A_N}{N}-\frac{A_{m-1}}{m}
+\sum_{n=m}^{N-1}A_n\left(\frac1n-\frac1{n+1}\right).
$$
Using $\abs{A_n}\le M$ from step [](#s1-2){.pf-ref} and the positivity of $1/n-1/(n+1)$,
$$
\begin{aligned}
\abs{\sum_{n=m}^N\frac{a_n}{n}}
&\le \frac{M}{N}+\frac{M}{m}
+M\sum_{n=m}^{N-1}\left(\frac1n-\frac1{n+1}\right)\\
&=\frac{M}{N}+\frac{M}{m}+M\left(\frac1m-\frac1N\right)\\
&=\frac{2M}{m}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For $p\ge 2$, the series $\sum_{n=1}^{\infty}\sin(\pi n/p)/n$ converges.


::: pf-proof

By step [](#s1-3){.pf-ref}, every tail from $m$ through $N$ has absolute value at most $2M/m$. This bound tends to zero as $m\to\infty$, uniformly in $N\ge m$. Hence the sequence of partial sums is Cauchy in $\RR$, so the series converges.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the claim for $p=1$, and step [](#s1-4){.pf-ref} proves it for every $p\ge 2$.

:::

:::

:::
