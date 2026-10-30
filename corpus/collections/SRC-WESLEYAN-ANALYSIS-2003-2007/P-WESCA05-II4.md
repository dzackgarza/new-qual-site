---
schema: qual/card@1
id: P-WESCA05-II4
kind: problem
title: "Polynomial growth forces an entire function to be a polynomial"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 4 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f$ be entire.
Suppose there are a constant $M$ and a fixed positive integer $n$ such that
$$
\abs{f(z)}\le M\abs{z}^n
\qquad(z\in\CC).
$$
Prove that $f$ is a polynomial of degree at most $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $R>0$,
$$
\max_{\abs{z}=R}\abs{f(z)}\le MR^n.
$$


::: pf-proof

This is the given growth estimate restricted to the circle $\abs{z}=R$.

:::

:::

::: {.pf-step #s1-2}

For every integer $k\ge0$ and every $R>0$,
$$
\abs{f^{(k)}(0)}
\le
k!MR^{n-k}.
$$


::: pf-proof

By Cauchy's formula for derivatives on the circle $\abs{z}=R$,
$$
f^{(k)}(0)
=
\frac{k!}{2\pi i}
\int_{\abs{z}=R}\frac{f(z)}{z^{k+1}}\,dz.
$$
Taking absolute values and using the ML estimate together with step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
\abs{f^{(k)}(0)}
&\le
\frac{k!}{2\pi}
(2\pi R)
\frac{MR^n}{R^{k+1}}\\
&=
k!MR^{n-k}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

If $k>n$, then
$$
f^{(k)}(0)=0.
$$


::: pf-proof

For $k>n$, step [](#s1-2){.pf-ref} gives
$$
\abs{f^{(k)}(0)}
\le
k!M R^{n-k}
$$
for every $R>0$. Since $n-k<0$, the right-hand side tends to $0$ as $R\to\infty$. Hence $\abs{f^{(k)}(0)}=0$.

:::

:::

::: {.pf-step #s1-4}

The Taylor series of $f$ about $0$ terminates after degree $n$:
$$
f(z)
=
\sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}z^k.
$$


::: pf-proof

Because $f$ is entire, its Taylor series about $0$ converges to $f$ for every $z\in\CC$:
$$
f(z)
=
\sum_{k=0}^{\infty}\frac{f^{(k)}(0)}{k!}z^k.
$$
Step [](#s1-3){.pf-ref} shows that every coefficient with $k>n$ is zero, so only the terms through degree $n$ remain.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{f\text{ is a polynomial of degree at most }n.}
$$


::: pf-proof

The expression in step [](#s1-4){.pf-ref} is a polynomial with no term of degree greater than $n$, and it equals $f$ everywhere.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
