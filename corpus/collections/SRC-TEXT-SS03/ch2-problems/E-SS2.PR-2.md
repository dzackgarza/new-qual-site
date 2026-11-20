---
schema: qual/card@1
id: E-SS2.PR-2
kind: problem
title: Growth of $\sum d(n)z^n$ along rational rays
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against the printed item (Chapter 2, Problem 2, printed p. 68, PDF p. 88 of the retained
    scan): the statement is the print's, and the asterisk the print sets before "2." is recorded in
    the remark. The four steps were read. One repair was made in step s3: the terms with $q\nmid n$
    were bounded in modulus and then subtracted from a lower bound for $|F|$, which is only valid
    through $|F|\ge\operatorname{Re}F$; the step now says so and fixes
    $\delta_q=\min_{m\not\equiv0}\abs{1-e^{2\pi im/q}}$, so that the estimate is uniform in $n$ and
    not merely pointwise for each $n$. Not checked: nothing in the item beyond these four claims.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s3 on the reader's report. The bound $\abs{1-z^n}\ge\delta_q$ recorded there held
    only in the limit $r\to1^-$: for $r<1$ the infimum of $\abs{1-re^{i\theta_n}}$ is $\sin\theta_n$,
    which is below $\abs{1-e^{i\theta_n}}$, and the minimum defining $\delta_q$ was taken over the
    empty set when $q=1$. The step now derives $\abs{1-z^n}\ge\delta_q-(1-r)$, gives $\delta_q/2$ for
    $r\ge1-\delta_q/2$ when $q\ge2$, states the case $q=1$ to be vacuous, and bounds the real part of
    the corresponding terms by $-2r^n/\delta_q$. The other three steps are unchanged. Not checked in
    this pass: the identity of step 1 and the convergence argument of step 4 beyond reading them.
---

::: {.exercise}
Let
$$
F(z) = \sum_{n=1}^{\infty} d(n) z^n \quad \text{for } \abs{z} < 1
$$
where $d(n)$ denotes the number of divisors of $n$. Observe that the radius of convergence of this series is $1$. Verify the identity
$$
\sum_{n=1}^{\infty} d(n) z^n = \sum_{n=1}^{\infty} \frac{z^n}{1 - z^n}.
$$
Using this identity, show that if $z = r$ with $0 < r < 1$, then
$$
\abs{F(r)} \geq c \frac{1}{1 - r} \log(1/(1 - r))
$$
as $r \to 1$. Similarly, if $\theta = 2\pi p/q$ where $p$ and $q$ are positive integers and $z = re^{i\theta}$, then
$$
\abs{F(re^{i\theta})} \geq c_{p/q} \frac{1}{1 - r} \log(1/(1 - r))
$$
as $r \to 1$. Conclude that $F$ cannot be continued analytically past the unit disc.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 2, Problem 2, printed p. 68).
:::

::: {.solution}
No published solution set covers the end-of-chapter Problems of Stein--Shakarchi: the set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, and no other set was located. The argument is the card's own, with the book's numbered results cited where used.

::: pf

::: pf-step

$\sum_{n\ge1} d(n) z^n = \sum_{n\ge1} \frac{z^n}{1 - z^n}$ for $\abs z<1$.

::: pf-proof

By the geometric series, $\frac{z^n}{1 - z^n} = \sum_{k\ge1} z^{kn}$. The double series converges absolutely, and the coefficient of $z^m$ in $\sum_n\sum_k z^{kn}$ is the number of pairs $(n,k)$ with $kn = m$, which is $d(m)$.

:::

:::

::: {.pf-step #s2}

$F(r) \ge c \frac{1}{1-r}\log\frac{1}{1-r}$ as $r \to 1^-$.

::: pf-proof

All terms of $F(r) = \sum_{n} \frac{r^n}{1-r^n}$ are positive. Using $1 - r^n \le n(1-r)$ and keeping the terms with $n \le N$, where $N$ is the integer part of $\frac{1}{1-r}$, gives $F(r)\ge\frac{r^N}{1-r}\sum_{n\le N}\frac1n$. Since $r^N$ is bounded below by a positive constant as $r\to1^-$ and $\sum_{n\le N}\frac1n\ge\log N$, this is at least $c \frac{1}{1-r}\log\frac{1}{1-r}$.

:::

:::

::: pf-step

For $\theta = 2\pi p/q$, $\abs{F(re^{i\theta})} \ge c_{p/q}\frac{1}{1-r}\log\frac{1}{1-r}$ as $r\to1^-$.

::: pf-proof

Assume $p/q$ is in lowest terms and put $z=re^{i\theta}$. For $q\mid n$, $z^n = r^n$, and the terms with $n=qj$ contribute $\sum_j\frac{r^{qj}}{1-r^{qj}}=F(r^q)$, which by step [](#s2){.pf-ref} is at least $c\frac{1}{1-r^q}\log\frac{1}{1-r^q}\ge \frac cq\frac{1}{1-r}\log\frac{1}{q(1-r)}$ since $1-r^q\le q(1-r)$. For $q\nmid n$ put $\theta_n=2\pi np/q$. Then $e^{i\theta_n}$ is a $q$th root of unity different from $1$ and $\abs{1-z^n}=\abs{1-r^ne^{i\theta_n}}\ge\abs{1-e^{i\theta_n}}-(1-r^n)\ge\delta_q-(1-r)$, where $\delta_q=\min_{1\le m\le q-1}\abs{1-e^{2\pi im/q}}>0$ depends only on $n$ modulo $q$, so one $\delta_q$ serves every such $n$; for $q\ge2$ and $r\ge1-\delta_q/2$ this is at least $\delta_q/2$, and for $q=1$ there is no such $n$ and the estimate is vacuous. These terms have real part at least $-2r^n/\delta_q$ and so contribute at least $-2\sum_n r^n/\delta_q=-O\bigl(\frac1{1-r}\bigr)$ to $\operatorname{Re}F(re^{i\theta})$, and $\abs{F}\ge\operatorname{Re}F$. The logarithmic factor dominates, which gives the bound with a smaller constant $c_{p/q}$.

:::

:::

::: pf-step

$F$ cannot be continued analytically past the unit circle.

::: pf-proof

If $w\in C$ were regular for $F$, then $F$ would agree on $\DD\cap U$ with a function analytic on a neighborhood $U$ of $w$, so $F$ would be bounded on $\DD\cap U'$ for a smaller neighborhood $U'$ of $w$. The points $e^{2\pi ip/q}$ are dense in $C$, so $U'$ contains one of them, and by the previous step $\abs{F(re^{2\pi ip/q})}\to\infty$ as $r\to1^-$. This is a contradiction, so no point of $C$ is regular.

:::

:::

:::

:::
