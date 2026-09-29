---
schema: qual/card@1
id: P-AZOFF-A01
kind: problem
title: Limit of the averaging recurrence $x_n=(x_{n-1}+x_{n-2})/2$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Derived the first-difference recurrence d_n=-(1/2)d_{n-1}, summed it
    explicitly, and checked the resulting formula against the initial
    conditions and recurrence. The same formula gives a direct Cauchy estimate
    and the limit (a+2b)/3. The source compilation contains no worked solution
    for this problem.
---

::: {.problem}
Take $x_0 = a$, $x_1 = b$, and set $x_n \coloneqq \frac{x_{n-1} + x_{n-2}}{2}$ for $n \geq 2$. Prove that $(x_n)$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.
:::

::: {.solution}
For $n\geq1$, put
$$
d_n=x_n-x_{n-1}.
$$

::: pf

::: {.pf-step #s1}

For every $n\geq2$,
$$
d_n=-\frac12d_{n-1},
$$
and hence
$$
d_n=
\left(-\frac12\right)^{n-1}(b-a).
$$

::: pf-proof

Using the recurrence for $x_n$,
$$
\begin{aligned}
d_n
&=x_n-x_{n-1}\\
&=\frac{x_{n-1}+x_{n-2}}2-x_{n-1}\\
&=-\frac12(x_{n-1}-x_{n-2})\\
&=-\frac12d_{n-1}.
\end{aligned}
$$
Since
$$
d_1=x_1-x_0=b-a,
$$
iteration gives the stated formula.

:::

:::

::: {.pf-step #s2}

For every $n\geq0$,
$$
x_n
=
\frac{a+2b}{3}
+
\frac{2(a-b)}3
\left(-\frac12\right)^n.
$$

::: pf-proof

For $n\geq1$, telescoping and step [](#s1){.pf-ref} give
$$
\begin{aligned}
x_n
&=a+\sum_{k=1}^n d_k\\
&=a+(b-a)\sum_{k=1}^n\left(-\frac12\right)^{k-1}\\
&=a+\frac23(b-a)
\left(1-\left(-\frac12\right)^n\right)\\
&=\frac{a+2b}{3}
+\frac{2(a-b)}3
\left(-\frac12\right)^n.
\end{aligned}
$$
For $n=0$ the same expression equals $a$, so the formula holds for all
$n\geq0$.

:::

:::

::: {.pf-step #s3}

The sequence $(x_n)$ is Cauchy.

::: pf-proof

Put
$$
C=\frac{2(a-b)}3.
$$
By step [](#s2){.pf-ref}, for any $m,n\geq0$,
$$
\begin{aligned}
\abs{x_n-x_m}
&=
\abs{C}
\abs{
\left(-\frac12\right)^n
-
\left(-\frac12\right)^m
}\\
&\leq
\abs{C}
\left(2^{-n}+2^{-m}\right).
\end{aligned}
$$
Let $\varepsilon>0$. If $C=0$, then the sequence is constant. Otherwise
choose $N$ so large that
$$
2\abs{C}\,2^{-N}<\varepsilon.
$$
For $m,n\geq N$, the displayed estimate gives
$$
\abs{x_n-x_m}<\varepsilon.
$$
Thus $(x_n)$ is Cauchy.

:::

:::

::: {.pf-step #s4}

The limit is
$$
\boxed{
\lim_{n\to\infty}x_n
=
\frac{a+2b}{3}
}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
x_n-\frac{a+2b}{3}
=
\frac{2(a-b)}3
\left(-\frac12\right)^n.
$$
Since
$$
\left(-\frac12\right)^n\longrightarrow0,
$$
the displayed difference tends to zero.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the Cauchy property, and step [](#s4){.pf-ref} gives the requested
limit.

:::

:::

:::
