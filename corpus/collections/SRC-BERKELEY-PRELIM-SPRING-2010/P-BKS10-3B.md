---
schema: qual/card@1
id: P-BKS10-3B
kind: problem
title: Zeros of $z^7+e^z$ in the upper half of the disk $\abs{z}<2$
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the Rouche count, uniqueness of the real zero, absence of multiple zeros, and conjugate-pair count.
---

::: {.problem}
How many complex numbers $z$ satisfy
$$
|z|<2,\qquad \operatorname{Im}(z)>0,\qquad z^7+e^z=0?
$$
:::

::: {.solution}
Set
$$
F(z)\coloneqq z^7+e^z.
$$

::: pf

::: {.pf-step #seven-zeros}
The function $F$ has exactly seven zeros in the disk
$$
\abs{z}<2,
$$
counted with multiplicity.

::: pf-proof
On the circle $\abs{z}=2$,
$$
\abs{z^7}=2^7=128,
$$
while
$$
\abs{e^z}
=
e^{\operatorname{Re}z}
\leq
e^2
<
128.
$$
Rouché's theorem therefore shows that $F(z)=z^7+e^z$ and $z^7$ have the
same number of zeros inside the circle. The latter has seven zeros counted
with multiplicity, all at $0$.
:::

:::

::: {.pf-step #real-zero}
The function $F$ has exactly one real zero, and it lies in
$(-1,0)$.

::: pf-proof
For real $x$,
$$
F'(x)=7x^6+e^x>0,
$$
so $F$ is strictly increasing on $\RR$. Also
$$
F(-1)=-1+e^{-1}<0
$$
and
$$
F(0)=1>0.
$$
The intermediate value theorem gives a real zero in $(-1,0)$, and strict
monotonicity makes it unique.
:::

:::

::: {.pf-step #zeros-simple}
Every zero of $F$ is simple.

::: pf-proof
If $z$ were a multiple zero, then
$$
z^7+e^z=0
$$
and
$$
7z^6+e^z=0.
$$
Thus
$$
e^z=-z^7=-7z^6,
$$
so
$$
z^6(z-7)=0.
$$
Hence $z=0$ or $z=7$. But
$$
F(0)=1
$$
and
$$
F(7)=7^7+e^7\neq0.
$$
This contradiction proves simplicity.
:::

:::

::: {.pf-step #conjugate-pairs}
Besides the one real zero from step [](#real-zero){.pf-ref}, the disk
$\abs{z}<2$ contains six nonreal zeros, arranged in three conjugate pairs.

::: pf-proof
Steps [](#seven-zeros){.pf-ref} and [](#zeros-simple){.pf-ref} show that there are seven distinct zeros in the disk.
Step [](#real-zero){.pf-ref} accounts for exactly one of them on the real axis. Since
$$
\overline{F(z)}
=
F(\overline z),
$$
every nonreal zero occurs together with its complex conjugate. Thus the
remaining six zeros form three conjugate pairs.
:::

:::

::: {.pf-step #solution-count}
The number of solutions satisfying all three conditions is
$$
\boxed{3}.
$$

::: pf-proof
Each conjugate pair in step [](#conjugate-pairs){.pf-ref} contains exactly one zero with positive
imaginary part and one with negative imaginary part. There are three such
pairs.
:::

:::

::: pf-qed
Step [](#solution-count){.pf-ref} gives the requested number.
:::

:::

:::
