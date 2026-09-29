---
schema: qual/card@1
id: P-BERK91S-03
kind: problem
title: The divisor-counting function is odd exactly on perfect squares
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the positive-integer hypothesis, positive divisor count, and perfect-square equivalence with Problem 3 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Paired positive divisors by the involution a maps to n/a and identified its unique possible fixed point.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked that the divisor set is finite, the map is a well-defined involution, its nonfixed elements form disjoint pairs, and the fixed-point count proves both implications including n equals one.
---

::: {.problem}
For a positive integer $n$, let $d(n)$ be the number of positive divisors of $n$. Prove that
$$
d(n)\text{ is odd}\iff n\text{ is a perfect square}.
$$
:::

::: {.hint}
Pair a positive divisor $a$ of $n$ with $n/a$. A divisor is
paired with itself precisely when $a^2=n$.
:::

::: {.solution}
Let
$$
D_n\coloneqq\{a\in\ZZ:a>0\text{ and }a\mid n\},
\qquad
\iota\colon D_n\longrightarrow D_n,
\quad a\longmapsto n/a.
$$

::: pf

::: {.pf-step #s1}

The map $\iota$ partitions $D_n$ into singleton sets
at its fixed points and pairs of distinct divisors elsewhere.

::: pf-proof

For $a\in D_n$, the quotient $n/a$ is a positive integer and
divides $n$, since $n=a(n/a)$. Thus $\iota$ is well defined,
and
$$
\iota(\iota(a))=\frac{n}{n/a}=a.
$$
Consequently $\{a,\iota(a)\}$ contains one element when
$\iota(a)=a$ and two elements otherwise. Any two such sets
that intersect coincide, by the displayed identity, so they
partition $D_n$. Every member of $D_n$ lies between $1$ and
$n$, so this is a finite partition.

:::

:::

::: {.pf-step #s2}

There is exactly one fixed point of $\iota$ when $n$
is a perfect square, and there are no fixed points otherwise.

::: pf-proof

For $a\in D_n$, the equality $\iota(a)=a$ is equivalent to
$a^2=n$. There is at most one positive integer with square
$n$: if $a,b>0$ and $a^2=b^2$, then
$(a-b)(a+b)=0$ and $a+b>0$, hence $a=b$.
If $n=b^2$ for a positive integer $b$, then $b\mid n$ and
$\iota(b)=b$, so that fixed point exists. If $n$ is not a
perfect square, no positive integer satisfies $a^2=n$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, every part of the partition away from the fixed
points contributes $2$ to $d(n)=\abs{D_n}$. Step [](#s2){.pf-ref} shows
that the fixed points contribute $1$ precisely when $n$ is
a perfect square, and contribute $0$ otherwise. Thus $d(n)$
is odd if and only if $n$ is a perfect square. This includes
$n=1$, for which $D_1=\{1\}$.

:::

:::

:::
