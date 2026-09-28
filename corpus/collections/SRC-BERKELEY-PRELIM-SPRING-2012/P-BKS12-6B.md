---
schema: qual/card@1
id: P-BKS12-6B
kind: problem
title: Integer-valued rational polynomials determined by $n$ consecutive values
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 5 of the retained Spring 2012 solution PDF and independently reviewed the congruence argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the reduction of arbitrary integers to residues modulo n and polynomial evaluation modulo n.
---

::: {.problem}
Suppose $f ( x ) \in Q [ x ]$ is a polynomial with rational coefficient, n is a positive integer, $n f ( x ) \in$ $Z [ x ]$ has integer coefficients and $f ( m )$ is an integer for all integers m, $0 \leq m < n$ . Show $f ( m )$ is an integer for all integers m.
:::

::: {.solution}
Set
$$
g(x)\coloneqq nf(x)\in\ZZ[x].
$$

<1>1. If integers $a$ and $b$ satisfy
$$
a\equiv b\pmod n,
$$
then
$$
g(a)\equiv g(b)\pmod n.
$$

::: {.proof}
Write
$$
g(x)=\sum_{k=0}^d c_kx^k,
\qquad
c_k\in\ZZ.
$$
From
$$
a\equiv b\pmod n
$$
one gets
$$
a^k\equiv b^k\pmod n
$$
for every $k\geq0$. Multiplying by the integer coefficients $c_k$ and
summing yields the claim.
:::

<1>2. For every integer $m$, there are integers $q$ and $i$ such that
$$
m=i+qn,
\qquad
0\leq i<n.
$$

::: {.proof}
This is the division algorithm applied to $m$ by the positive integer
$n$. It applies equally to positive and negative integers $m$.
:::

<1>3. For $m,i$ as in step <1>2,
$$
\frac{g(m)-g(i)}n
\in
\ZZ.
$$

::: {.proof}
Step <1>2 gives
$$
m\equiv i\pmod n.
$$
By step <1>1,
$$
g(m)\equiv g(i)\pmod n.
$$
Thus $n$ divides $g(m)-g(i)$.
:::

<1>4. For every integer $m$,
$$
\boxed{f(m)\in\ZZ}.
$$

::: {.proof}
Choose $i$ as in step <1>2. Then
$$
\begin{aligned}
f(m)
&=
\frac{g(m)}n\\
&=
\frac{g(i)}n
+
\frac{g(m)-g(i)}n\\
&=
f(i)
+
\frac{g(m)-g(i)}n.
\end{aligned}
$$
The first term is an integer by the hypothesis because
$$
0\leq i<n,
$$
and the second is an integer by step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the required integer-valuedness at every integer.
:::
:::
