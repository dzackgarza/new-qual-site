---
schema: qual/card@1
id: P-QGCXS
kind: problem
title: $\sum_{k=1}^{n-1}\cos\frac{2\pi k}{n}=-1$ and $\sum_{k=1}^{n-1}\sin\frac{2\pi
  k}{n}=0$, via roots of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source omitted sin before the last summand 2(n-1)pi/n of the sine identity; it now reads sin 2(n-1)pi/n. The stray + before =-1 in the cosine identity is removed.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source states the identities for every n. For n=1 both sums are empty and the cosine identity reads 0=-1, so the statement now assumes n>=2. The source hint about Vieta formulas is moved to a hint block.'
---

::: {.problem}
Let $n\geq2$ be an integer.
Use $n$-th roots of unity (i.e. solutions of $z^{n}-1=0$ ) to show that

$$
\begin{aligned}
&\cos \frac{2 \pi}{n}+\cos \frac{4 \pi}{n}+\cos \frac{6 \pi}{n}+\cdots+\cos \frac{2(n-1) \pi}{n}=-1 \text { and } \\
&\sin \frac{2 \pi}{n}+\sin \frac{4 \pi}{n}+\sin \frac{6 \pi}{n}+\cdots+\sin \frac{2(n-1) \pi}{n}=0
\end{aligned}
$$
:::

::: {.hint}
If $z^{n}+c_{1} z^{n-1}+\cdots+c_{n-1} z+c_{n}=0$ has roots $z_{1}, z_{2}, \ldots, z_{n}$, then $z_{1}+z_{2}+\cdots+z_{n}=-c_{1}$.
:::

::: {.solution}
Let $\omega=e^{2\pi i/n}$, so the roots of $z^n-1$ are $1,\omega,\ldots,\omega^{n-1}$.

::: pf

::: {.pf-step #vieta}

$\sum_{k=1}^{n-1}\omega^k=-1$.

::: pf-proof

Since $n\ge2$, the coefficient of $z^{n-1}$ in $z^n-1$ is $0$, so the roots sum to $0$: $1+\omega+\cdots+\omega^{n-1}=0$.

:::

:::

::: pf-step

$$
\boxed{\sum_{k=1}^{n-1}\cos\frac{2\pi k}{n}=-1},
\qquad
\boxed{\sum_{k=1}^{n-1}\sin\frac{2\pi k}{n}=0}.
$$

::: pf-proof

Take real and imaginary parts in step [](#vieta){.pf-ref}, using $\omega^k=\cos\frac{2\pi k}n+i\sin\frac{2\pi k}n$.

:::

:::

:::

:::
