---
schema: qual/card@1
id: P-TIE-S15-07
kind: problem
title: Entire functions of polynomial growth are polynomials
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 7.
---

::: {.problem}
Suppose f is entire and there exist A, $R > 0$ and natural number N such that $| f ( z ) | \leq A | z | ^ { N }$ for $| z | \geq R .$ . Show that (i) f is a polynomial and (ii) the degree of f is at most N .
:::

::: pf

::: pf-step

For every integer $k\ge0$ and every $\rho\ge R$,
$$
\frac{\abs{f^{(k)}(0)}}{k!}
\le
A\rho^{N-k}.
$$


::: pf-proof

Since $f$ is entire, Cauchy's integral formula for derivatives on the circle $\abs{z}=\rho$ gives
$$
f^{(k)}(0)
=
\frac{k!}{2\pi i}
\int_{\abs{z}=\rho}
\frac{f(z)}{z^{k+1}}\,dz.
$$
Therefore
$$
\begin{aligned}
\frac{\abs{f^{(k)}(0)}}{k!}
&\le
\frac1{2\pi}
(2\pi\rho)
\frac{\max_{\abs{z}=\rho}\abs{f(z)}}{\rho^{k+1}}\\
&=
\frac{\max_{\abs{z}=\rho}\abs{f(z)}}{\rho^k}.
\end{aligned}
$$
For $\rho\ge R$, the hypothesis gives
$$
\max_{\abs{z}=\rho}\abs{f(z)}
\le
A\rho^N.
$$
Substitution yields the stated estimate.

:::

:::

::: pf-step

For every integer $k>N$,
$$
f^{(k)}(0)=0.
$$


::: pf-proof

Fix $k>N$. Step <1>1 gives
$$
\frac{\abs{f^{(k)}(0)}}{k!}
\le
A\rho^{N-k}
$$
for every $\rho\ge R$. Since $N-k<0$,
$$
A\rho^{N-k}\longrightarrow0
$$
as $\rho\to\infty$. Therefore
$$
f^{(k)}(0)=0.
$$

:::

:::

::: pf-step

The Taylor series of $f$ terminates after degree $N$:
$$
\boxed{
f(z)
=
\sum_{k=0}^{N}
\frac{f^{(k)}(0)}{k!}z^k.
}
$$


::: pf-proof

Because $f$ is entire, its Taylor series at $0$ converges to $f$ on all of $\CC$:
$$
f(z)
=
\sum_{k=0}^{\infty}
\frac{f^{(k)}(0)}{k!}z^k.
$$
By step <1>2, every coefficient with $k>N$ vanishes. Thus the series reduces to the finite sum displayed above.

:::

:::

::: pf-step

Hence $f$ is a polynomial of degree at most $N$.


::: pf-proof

Step <1>3 expresses $f$ as a finite polynomial whose highest possible power is $z^N$. Therefore $f$ is a polynomial and
$$
\boxed{\deg f\le N.}
$$

:::

:::

::: pf-qed

Step <1>4 proves both requested conclusions.

:::

:::
