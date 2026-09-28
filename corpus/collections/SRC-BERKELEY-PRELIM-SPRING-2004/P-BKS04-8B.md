---
schema: qual/card@1
id: P-BKS04-8B
kind: problem
title: Limit of $n((1+x/n)^n-e^x)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
For each real number $x$, compute

$$
\lim_{n\to\infty}n\left(\left(1+\frac xn\right)^n-e^x\right).
$$
:::

::: {.solution}
We have

$$
\begin{aligned}
n\left(\left(1+\frac xn\right)^n-e^x\right)&=n\left(e^{n\log(1+x/n)}-e^x\right)\\
&=ne^x\left(e^{n\log(1+x/n)-x}-1\right).
\end{aligned}
$$

Taylor's theorem with remainder gives

$$
\log\left(1+\frac xn\right)=\frac xn-\frac12\left(\frac{x^2}{n^2}\right)+O\left(\frac1{n^3}\right)
$$

where the constant in the big-O depends on $x$, but not on $n$. Substituting, we get

$$
ne^x\left(e^{-\frac{x^2}{2n}+O\left(\frac1{n^2}\right)}-1\right).
$$

Since $e^y=1+y+O(y^2)$ as $y\to0$, this becomes

$$
ne^x\left(-\frac{x^2}{2n}+O\left(\frac1{n^2}\right)\right)=-\frac12x^2e^x+O\left(\frac1n\right),
$$

so the limit is $-\frac12x^2e^x$.
:::
