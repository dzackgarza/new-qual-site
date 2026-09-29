---
schema: qual/card@1
id: P-BERK98S-08
kind: problem
title: Integrality of divided-power coefficients under powers
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $m\ge0$ be an integer, let $a_1,\dots,a_m\in\mathbb Z$, and set
\[
f(x)=\sum_{i=1}^m\frac{a_ix^i}{i!}.
\]
Show that for every integer $d\ge0$ there are integers $b_0,\dots,b_{md}$ such that
\[
\frac{f(x)^d}{d!}
=\sum_{i=0}^{md}\frac{b_ix^i}{i!}.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The claim is immediate when $d=0$, and also when $m=0$.

::: pf-proof

If $d=0$, then
$$
\frac{f(x)^0}{0!}=1,
$$
so take $b_0=1$. If $m=0$ and $d>0$, then $f=0$, so take $b_0=0$.
Thus it remains to consider $m,d\geq1$.

:::

:::

::: {.pf-step #s2}

For $0\leq n\leq md$, the coefficient of $x^n/n!$ in
$f(x)^d/d!$ is
$$
b_n
=
\sum_{\substack{c_1,\ldots,c_m\geq0\\
c_1+\cdots+c_m=d\\
c_1+2c_2+\cdots+mc_m=n}}
\frac{n!}{\prod_{i=1}^m c_i!(i!)^{c_i}}
\prod_{i=1}^m a_i^{c_i}.
$$

::: pf-proof

By the multinomial theorem,
$$
f(x)^d
=
\sum_{c_1+\cdots+c_m=d}
\frac{d!}{c_1!\cdots c_m!}
\prod_{i=1}^m
\left(\frac{a_i x^i}{i!}\right)^{c_i}.
$$
After division by $d!$, a term indexed by $(c_1,\ldots,c_m)$ has degree
$$
n=c_1+2c_2+\cdots+mc_m
$$
and coefficient
$$
\frac{\prod_{i=1}^m a_i^{c_i}}
{\prod_{i=1}^m c_i!(i!)^{c_i}}.
$$
Multiplying the coefficient of $x^n$ by $n!$ gives the displayed formula
for the coefficient $b_n$ of $x^n/n!$.

:::

:::

::: {.pf-step #s3}

For every tuple $(c_1,\ldots,c_m)$ occurring in step [](#s2){.pf-ref},
$$
\frac{n!}{\prod_{i=1}^m c_i!(i!)^{c_i}}
$$
is an integer.

::: pf-proof

Let $S$ be an $n$-element set. The displayed number counts partitions of
$S$ into exactly $c_i$ unlabeled blocks of size $i$ for each
$1\leq i\leq m$.

Indeed, ordering the elements of $S$ gives $n!$ lists. Cutting such a list
into $c_i$ blocks of size $i$ for each $i$ overcounts by a factor $i!$ for
the internal ordering of each size-$i$ block, and by a factor $c_i!$ for
the ordering of the $c_i$ blocks of the same size. Hence the number of such
set partitions is exactly
$$
\frac{n!}{\prod_{i=1}^m c_i!(i!)^{c_i}},
$$
which is therefore an integer.

:::

:::

::: {.pf-step #s4}

Every coefficient $b_n$ in step [](#s2){.pf-ref} is an integer.

::: pf-proof

Each $a_i$ is an integer by hypothesis, and step [](#s3){.pf-ref} shows that every
other factor in every summand defining $b_n$ is an integer. Hence
$b_n\in\ZZ$.

:::

:::

::: {.pf-step #s5}

One has
$$
\boxed{
\frac{f(x)^d}{d!}
=
\sum_{n=0}^{md}\frac{b_nx^n}{n!}
}
$$
with every $b_n\in\ZZ$.

::: pf-proof

The degree of $f^d$ is at most $md$. Step [](#s2){.pf-ref} identifies the divided-power
coefficient $b_n$ for every degree $0\leq n\leq md$, and step [](#s4){.pf-ref} proves
that each is an integer.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s5){.pf-ref} cover all cases.

:::

:::

:::
