---
schema: qual/card@1
id: P-BKS14-2A
kind: problem
title: Boundedness on rationals versus irrational translates
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the interpolation nodes are distinct and that the resulting polynomial sequence is eventually zero on rationals and grows linearly on their sqrt(2)-translates.
---

::: {.problem}
Prove or disprove that there is a sequence $\{f_n\}$ of continuous functions on $\RR$ such that for every rational $x$, the sequence $f_n(x)$ is bounded, but the sequence $f_n(x+\sqrt2)$ is unbounded.
:::

::: {.solution}
Enumerate the rational numbers as
$$
\QQ=\{r_1,r_2,r_3,\ldots\}.
$$

::: pf

::: {.pf-step #s1}

For every $n\geq1$, the $2n$ real numbers
$$
r_1,\ldots,r_n,
\qquad
r_1+\sqrt2,\ldots,r_n+\sqrt2
$$
are pairwise distinct.

::: pf-proof

The rationals $r_1,\ldots,r_n$ are distinct by construction. Their
$\sqrt2$-translates are also distinct.

Moreover, no rational $r_i$ can equal a translated point
$$
r_j+\sqrt2,
$$
because that would imply
$$
\sqrt2=r_i-r_j\in\QQ,
$$
a contradiction.

:::

:::

::: {.pf-step #s2}

For every $n\geq1$, there is a polynomial
$$
f_n\in\RR[x]
$$
such that
$$
f_n(r_j)=0
$$
and
$$
f_n(r_j+\sqrt2)=n
$$
for every $1\leq j\leq n$.

::: pf-proof

By step [](#s1){.pf-ref}, these are prescribed values at $2n$ distinct real points.
Lagrange interpolation therefore gives a real polynomial satisfying all
the conditions simultaneously.

:::

:::

::: {.pf-step #s3}

Every function $f_n$ from step [](#s2){.pf-ref} is continuous on $\RR$.

::: pf-proof

Every real polynomial is continuous.

:::

:::

::: {.pf-step #s4}

For every rational number $x$, the sequence
$$
\{f_n(x)\}_{n\geq1}
$$
is bounded.

::: pf-proof

Write
$$
x=r_j
$$
for some $j$. By step [](#s2){.pf-ref},
$$
f_n(x)=f_n(r_j)=0
$$
for every $n\geq j$. Thus the sequence is eventually zero. Its finitely
many earlier terms have a finite maximum in absolute value, so the whole
sequence is bounded.

:::

:::

::: {.pf-step #s5}

For every rational number $x$, the sequence
$$
\{f_n(x+\sqrt2)\}_{n\geq1}
$$
is unbounded.

::: pf-proof

Again write
$$
x=r_j.
$$
For every $n\geq j$, step [](#s2){.pf-ref} gives
$$
f_n(x+\sqrt2)
=
f_n(r_j+\sqrt2)
=
n.
$$
Hence this sequence tends to $+\infty$ along its tail and is unbounded.

:::

:::

::: {.pf-step #s6}

Therefore the requested sequence of continuous functions
$$
\boxed{\{f_n\}_{n\geq1}}
$$
exists.

::: pf-proof

Step [](#s3){.pf-ref} gives continuity, step [](#s4){.pf-ref} gives boundedness at every rational
argument, and step [](#s5){.pf-ref} gives unboundedness at every corresponding
$\sqrt2$-translate.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} proves the assertion.

:::

:::

:::
