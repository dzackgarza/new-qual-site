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
Prove or disprove that there is a sequence \(\{f_n\}\) of continuous functions on \(\mathbb R\) such that for every rational \(x\), the sequence \(f_n(x)\) is bounded, but the sequence \(f_n(x+\sqrt2)\) is unbounded.
:::

::: {.solution}
Enumerate the rational numbers as
$$
\QQ=\{r_1,r_2,r_3,\ldots\}.
$$

<1>1. For every $n\geq1$, the $2n$ real numbers
$$
r_1,\ldots,r_n,
\qquad
r_1+\sqrt2,\ldots,r_n+\sqrt2
$$
are pairwise distinct.

::: {.proof}
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

<1>2. For every $n\geq1$, there is a polynomial
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

::: {.proof}
By step <1>1, these are prescribed values at $2n$ distinct real points.
Lagrange interpolation therefore gives a real polynomial satisfying all
the conditions simultaneously.
:::

<1>3. Every function $f_n$ from step <1>2 is continuous on $\RR$.

::: {.proof}
Every real polynomial is continuous.
:::

<1>4. For every rational number $x$, the sequence
$$
\{f_n(x)\}_{n\geq1}
$$
is bounded.

::: {.proof}
Write
$$
x=r_j
$$
for some $j$. By step <1>2,
$$
f_n(x)=f_n(r_j)=0
$$
for every $n\geq j$. Thus the sequence is eventually zero. Its finitely
many earlier terms have a finite maximum in absolute value, so the whole
sequence is bounded.
:::

<1>5. For every rational number $x$, the sequence
$$
\{f_n(x+\sqrt2)\}_{n\geq1}
$$
is unbounded.

::: {.proof}
Again write
$$
x=r_j.
$$
For every $n\geq j$, step <1>2 gives
$$
f_n(x+\sqrt2)
=
f_n(r_j+\sqrt2)
=
n.
$$
Hence this sequence tends to $+\infty$ along its tail and is unbounded.
:::

<1>6. Therefore the requested sequence of continuous functions
$$
\boxed{\{f_n\}_{n\geq1}}
$$
exists.

::: {.proof}
Step <1>3 gives continuity, step <1>4 gives boundedness at every rational
argument, and step <1>5 gives unboundedness at every corresponding
$\sqrt2$-translate.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the assertion.
:::
:::
