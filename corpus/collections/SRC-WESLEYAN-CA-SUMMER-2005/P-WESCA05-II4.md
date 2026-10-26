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
\[
|f(z)|\le M|z|^n
\qquad(z\in\mathbb C).
\]
Prove that $f$ is a polynomial of degree at most $n$.
:::

::: pf

::: pf-step

For every \(R>0\),
\[
\max_{|z|=R}|f(z)|\le MR^n.
\]


::: pf-proof

This is the given growth estimate restricted to the circle \(|z|=R\).

:::

:::

::: pf-step

For every integer \(k\ge0\) and every \(R>0\),
\[
|f^{(k)}(0)|
\le
k!MR^{n-k}.
\]


::: pf-proof

By Cauchy's formula for derivatives on the circle \(|z|=R\),
\[
f^{(k)}(0)
=
\frac{k!}{2\pi i}
\int_{|z|=R}\frac{f(z)}{z^{k+1}}\,dz.
\]
Taking absolute values and using the ML estimate together with step <1>1 gives
\[
\begin{aligned}
|f^{(k)}(0)|
&\le
\frac{k!}{2\pi}
(2\pi R)
\frac{MR^n}{R^{k+1}}\\
&=
k!MR^{n-k}.
\end{aligned}
\]

:::

:::

::: pf-step

If \(k>n\), then
\[
f^{(k)}(0)=0.
\]


::: pf-proof

For \(k>n\), step <1>2 gives
\[
|f^{(k)}(0)|
\le
k!M R^{n-k}
\]
for every \(R>0\). Since \(n-k<0\), the right-hand side tends to \(0\) as \(R\to\infty\). Hence \(|f^{(k)}(0)|=0\).

:::

:::

::: pf-step

The Taylor series of \(f\) about \(0\) terminates after degree \(n\):
\[
f(z)
=
\sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}z^k.
\]


::: pf-proof

Because \(f\) is entire, its Taylor series about \(0\) converges to \(f\) for every \(z\in\mathbb C\):
\[
f(z)
=
\sum_{k=0}^{\infty}\frac{f^{(k)}(0)}{k!}z^k.
\]
Step <1>3 shows that every coefficient with \(k>n\) is zero, so only the terms through degree \(n\) remain.

:::

:::

::: pf-step

Therefore
\[
\boxed{f\text{ is a polynomial of degree at most }n.}
\]


::: pf-proof

The expression in step <1>4 is a polynomial with no term of degree greater than \(n\), and it equals \(f\) everywhere.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
