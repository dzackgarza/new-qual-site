---
schema: qual/card@1
id: P-CAF09C
kind: problem
title: 'The product $\prod_{n\geq 2}\qty{1-1/n^2}$ evaluated in two ways'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the factorisation 1 - 1/n^2 =
    ((n-1)/n)((n+1)/n), both telescoping products giving (N+1)/(2N) and the limit 1/2, the
    division of Euler's product by the n = 1 factor for z not equal to plus or minus 1, the
    limit at z = 1 computed with sin(pi z) = -sin(pi(z-1)) and 1 - z^2 = -(z-1)(z+1), and
    that the value at z = 1 of the product is its limit by continuity of the locally
    uniformly convergent product. The argument is the card's own; no retained set is cited.
    No repair needed.
---

::: {.problem}
Evaluate $\prod_{n=2}^{\infty}\left(1 - \frac{1}{n^2}\right)$ in two different ways.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. It gives the value twice, once by telescoping and once from Euler's product, as the exercise asks.

::: pf

::: {.pf-step #factor}
$1-\dfrac{1}{n^{2}}=\dfrac{n-1}{n}\cdot\dfrac{n+1}{n}$ for $n\ge2$.

::: pf-proof
$(n-1)(n+1)=n^{2}-1$, so $\frac{(n-1)(n+1)}{n^{2}}=\frac{n^{2}-1}{n^{2}}=1-\frac{1}{n^{2}}$.
:::

:::

::: {.pf-step #telescope}
$\displaystyle\prod_{n=2}^{N}\Big(1-\frac{1}{n^{2}}\Big)=\frac{N+1}{2N}$ for every $N\ge2$, so the infinite product converges to $\frac12$.

::: pf-proof
By step [](#factor){.pf-ref} the partial product is the product of $P_{N}=\prod_{n=2}^{N}\frac{n-1}{n}$ and $Q_{N}=\prod_{n=2}^{N}\frac{n+1}{n}$. Each telescopes:
$$
P_{N}=\frac{1}{2}\cdot\frac{2}{3}\cdots\frac{N-1}{N}=\frac1N,
\qquad
Q_{N}=\frac{3}{2}\cdot\frac{4}{3}\cdots\frac{N+1}{N}=\frac{N+1}{2}.
$$
Hence the partial product is $\frac1N\cdot\frac{N+1}{2}=\frac{N+1}{2N}$, whose limit as $N\to\infty$ is $\frac12$; the product converges because this limit exists and is nonzero.
:::

:::

::: {.pf-step #euler}
Euler's product $\dfrac{\sin\pi z}{\pi z}=\displaystyle\prod_{n=1}^{\infty}\Big(1-\frac{z^{2}}{n^{2}}\Big)$ holds for all $z$, and for $z\ne\pm1$
$$
\prod_{n=2}^{\infty}\Big(1-\frac{z^{2}}{n^{2}}\Big)=\frac{\sin\pi z}{\pi z\,(1-z^{2})}.
$$

::: pf-proof
Euler's product is an identity of entire functions, the product converging locally uniformly on $\CC$. Dividing both sides by the factor $1-z^{2}$ of the index $n=1$, which is nonzero for $z\ne\pm1$, gives the displayed identity for those $z$.
:::

:::

::: {.pf-step #limit}
$\displaystyle\lim_{z\to1}\frac{\sin\pi z}{\pi z\,(1-z^{2})}=\frac12$.

::: pf-proof
Write $z=1+\varepsilon$ with $\varepsilon\to0$. Then $\sin\pi z=\sin(\pi+\pi\varepsilon)=-\sin(\pi\varepsilon)=-\pi\varepsilon+O(\varepsilon^{3})$, and $1-z^{2}=-(z-1)(z+1)=-2\varepsilon+O(\varepsilon^{2})$, while $\pi z\to\pi$. Hence
$$
\frac{\sin\pi z}{\pi z\,(1-z^{2})}=\frac{-\pi\varepsilon+O(\varepsilon^{3})}{\pi(1+\varepsilon)\big(-2\varepsilon+O(\varepsilon^{2})\big)}\longrightarrow\frac{-\pi}{\pi\cdot(-2)}=\frac12.
$$
:::

:::

::: {.pf-step #second-value}
The value at $z=1$ of the product over $n\ge2$ is $\frac12$.

::: pf-proof
The product $\prod_{n\ge2}(1-z^{2}/n^{2})$ is an entire function of $z$, being a locally uniformly convergent product with factors $1-z^{2}/n^{2}$, hence continuous at $z=1$; so its value at $z=1$ is the limit computed in step [](#limit){.pf-ref} of the function of step [](#euler){.pf-ref}, which is $\frac12$.
:::

:::

::: {.pf-step}
$\displaystyle\prod_{n=2}^{\infty}\Big(1-\frac{1}{n^{2}}\Big)=\frac12$, obtained in two ways.

::: pf-proof
Step [](#telescope){.pf-ref} is the first evaluation and step [](#second-value){.pf-ref} the second, through Euler's product; both give $\frac12$.
:::

:::

:::
:::
