---
schema: qual/card@1
id: P-BERK86S-02
kind: problem
title: A continuous function with periods $1$ and $\sqrt2$ is constant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used pigeonhole approximation of multiples of sqrt(2) modulo one to
    produce nonzero periods tending to zero. Integer multiples of these
    periods approximate every real translation, and continuity forces all
    function values to agree.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous and suppose
\[
f(x)=f(x+1)=f(x+\sqrt2)
\]
for every $x\in\mathbb R$. Prove that $f$ is constant.
:::

::: {.solution}
Let
$$
H\coloneqq\{m+n\sqrt2:m,n\in\ZZ\}.
$$

<1>1. Every element of $H$ is a period of $f$:
$$
f(x+h)=f(x)
$$
for all $x\in\RR$ and $h\in H$.

::: {.proof}
The hypotheses say that $1$ and $\sqrt2$ are periods. If $p$ is a
period, then so is $-p$, because replacing $x$ by $x-p$ in
$$
f(x+p)=f(x)
$$
gives $f(x)=f(x-p)$. Integer multiples and sums of periods are again
periods by repeated substitution. Hence every
$$
m+n\sqrt2
$$
with $m,n\in\ZZ$ is a period.
:::

<1>2. For every positive integer $N$, there exists
$$
h_N\in H
$$
such that
$$
0<h_N<\frac1N.
$$

::: {.proof}
Consider the $N+1$ fractional parts
$$
\{j\sqrt2\},
\qquad
j=0,1,\ldots,N,
$$
in $[0,1)$. Partition $[0,1)$ into $N$ half-open intervals of length
$1/N$. By the pigeonhole principle, two distinct fractional parts,
say those for $0\leq i<j\leq N$, lie in the same interval. Therefore
their difference has absolute value less than $1/N$.

Writing
$$
j\sqrt2=\lfloor j\sqrt2\rfloor+\{j\sqrt2\}
$$
and similarly for $i$, this difference equals
$$
(j-i)\sqrt2-m
$$
for some $m\in\ZZ$. It is nonzero because $\sqrt2$ is irrational.
Thus $H$ contains a nonzero element of absolute value less than $1/N$.
Replacing it by its negative if necessary gives the required positive
$h_N$.
:::

<1>3. The subgroup $H$ is dense in $\RR$.

::: {.proof}
Fix $t\in\RR$. For each $N$, choose $h_N$ as in step <1>2 and let
$q_N\in\ZZ$ be an integer nearest to $t/h_N$. Then
$$
\abs{q_Nh_N-t}
\leq
\frac{h_N}{2}
<
\frac{1}{2N}.
$$
Since $q_Nh_N\in H$, the sequence $(q_Nh_N)$ consists of elements of
$H$ and converges to $t$. Thus every real number lies in the closure of
$H$.
:::

<1>4. For arbitrary $x,y\in\RR$,
$$
f(y)=f(x).
$$

::: {.proof}
Apply step <1>3 to
$$
t=y-x.
$$
There is a sequence $p_N\in H$ with
$$
p_N\longrightarrow y-x.
$$
Hence
$$
x+p_N\longrightarrow y.
$$
By step <1>1,
$$
f(x+p_N)=f(x)
$$
for every $N$. Continuity of $f$ gives
$$
f(y)
=
\lim_{N\to\infty}f(x+p_N)
=
f(x).
$$
:::

<1>5. Therefore
$$
\boxed{f\text{ is constant on }\RR}.
$$

::: {.proof}
Step <1>4 shows that any two values of $f$ are equal.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
