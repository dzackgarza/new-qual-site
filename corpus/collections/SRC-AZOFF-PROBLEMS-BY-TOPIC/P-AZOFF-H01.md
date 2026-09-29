---
schema: qual/card@1
id: P-AZOFF-H01
kind: problem
title: Partial sums of the exponential series have no zeros in the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash mangles the summand in the exponential partial sum. The same deterministic packet prints $1+z+z^2/2!+\cdots+z^n/n!$ explicitly in H8, which resolves this local extraction defect.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Multiplied f_n by 1-z and rewrote the result as 1-H_n, where the positive
    coefficients of H_n sum to one. On every circle |z|=r<1 this gives
    |H_n(z)|<1, so Rouché shows (1-z)f_n has no zeros in |z|<r. Since r is
    arbitrary and 1-z is nonzero in the unit disk, f_n has no zeros there.
---

::: {.problem}
For each nonnegative integer $n$, define
\[
f_n(z)=\sum_{k=0}^n\frac{z^k}{k!}.
\]
Prove that $f_n$ has no roots in the open unit disk.
(Hint: check $n=1$ and $n=2$ directly.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The case $n=0$ has no roots.

::: pf-proof

Here
$$
f_0(z)=1.
$$

:::

:::

::: {.pf-step #s2}

For every integer $n\geq1$,
$$
(1-z)f_n(z)
=
1-H_n(z),
$$
where
$$
H_n(z)
=
\sum_{k=2}^{n}
\frac{k-1}{k!}z^k
+
\frac{z^{n+1}}{n!}.
$$

::: pf-proof

Starting from
$$
f_n(z)=\sum_{k=0}^n\frac{z^k}{k!},
$$
one has
$$
\begin{aligned}
(1-z)f_n(z)
&=
\sum_{k=0}^n\frac{z^k}{k!}
-\sum_{k=0}^n\frac{z^{k+1}}{k!}\\
&=
1
+\sum_{k=1}^{n}
\left(
\frac1{k!}-\frac1{(k-1)!}
\right)z^k
-\frac{z^{n+1}}{n!}.
\end{aligned}
$$
The coefficient of $z$ is zero, and for $k\geq2$,
$$
\frac1{k!}-\frac1{(k-1)!}
=
-\frac{k-1}{k!}.
$$
This is the stated identity.

:::

:::

::: {.pf-step #s3}

The coefficients occurring in $H_n$ satisfy
$$
\sum_{k=2}^{n}\frac{k-1}{k!}
+\frac1{n!}
=
1.
$$

::: pf-proof

For $k\geq2$,
$$
\frac{k-1}{k!}
=
\frac1{(k-1)!}-\frac1{k!}.
$$
Hence the sum telescopes:
$$
\begin{aligned}
\sum_{k=2}^{n}\frac{k-1}{k!}
+\frac1{n!}
&=
\sum_{k=2}^{n}
\left(
\frac1{(k-1)!}-\frac1{k!}
\right)
+\frac1{n!}\\
&=
1.
\end{aligned}
$$
For $n=1$, the sum from $k=2$ to $1$ is empty and the same identity reads
$1/1!=1$.

:::

:::

::: {.pf-step #s4}

Fix $0<r<1$. On the circle $\abs{z}=r$,
$$
\abs{H_n(z)}<1.
$$

::: pf-proof

By step [](#s3){.pf-ref} and the positivity of the coefficients,
$$
\begin{aligned}
\abs{H_n(z)}
&\leq
\sum_{k=2}^{n}
\frac{k-1}{k!}r^k
+
\frac{r^{n+1}}{n!}\\
&<
\sum_{k=2}^{n}
\frac{k-1}{k!}
+
\frac1{n!}\\
&=
1.
\end{aligned}
$$
The inequality is strict because $0<r<1$.

:::

:::

::: {.pf-step #s5}

For every $0<r<1$, the polynomial $(1-z)f_n(z)$ has no zeros in
$\abs{z}<r$.

::: pf-proof

By step [](#s2){.pf-ref},
$$
(1-z)f_n(z)=1-H_n(z).
$$
On $\abs{z}=r$, step [](#s4){.pf-ref} gives
$$
\abs{-H_n(z)}<\abs{1}.
$$
Rouché's theorem therefore implies that $1-H_n(z)$ and the constant
function $1$ have the same number of zeros in $\abs{z}<r$, namely zero.

:::

:::

::: {.pf-step #s6}

For every $n\geq1$, the polynomial $f_n$ has no roots in the open
unit disk.

::: pf-proof

Suppose $f_n(z_0)=0$ with $\abs{z_0}<1$. Choose $r$ such that
$$
\abs{z_0}<r<1.
$$
Then
$$
(1-z_0)f_n(z_0)=0,
$$
contradicting step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

For every nonnegative integer $n$, the polynomial $f_n$ has no roots
in the open unit disk.

::: pf-proof

Step [](#s1){.pf-ref} handles $n=0$, and step [](#s6){.pf-ref} handles every $n\geq1$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
