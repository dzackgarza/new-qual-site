---
schema: qual/card@1
id: P-BKS15-9B
kind: problem
title: Legendre's formula and the base-$p$ digit sum of $n$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the valuation count, the floor calculation from the base-p digits, and the resulting relation n=(p-1)a(n)+b(n).
---

::: {.problem}
Let $p$ be a prime.
Let $p^{a(n)}$ be the largest power of $p$ dividing $n!$, and let $b(n)$ be the sum of the digits of $n$ in base $p$.

(a) Show that
\[
a(n)=\left\lfloor\frac np\right\rfloor+\left\lfloor\frac n{p^2}\right\rfloor+\left\lfloor\frac n{p^3}\right\rfloor+\cdots.
\]

(b) Express $a(n)$ in terms of the digits $d_k$ in the base-$p$ expansion
\[
n=\sum_k d_kp^k,
\qquad 0\le d_k<p.
\]

(c) Find a nontrivial linear relation between $n$, $a(n)$, and $b(n)$, with coefficients allowed to depend on $p$ but not on $n$.
:::

::: {.solution}
<1>1. The exponent $a(n)$ satisfies
$$
a(n)
=
\sum_{r=1}^{n}v_p(r),
$$
where $v_p(r)$ is the exponent of $p$ in the prime factorization of $r$.

::: {.proof}
Since
$$
n!=\prod_{r=1}^n r,
$$
the exponent of $p$ in $n!$ is the sum of the exponents of $p$ in its factors.
:::

<1>2. One has
$$
a(n)
=
\sum_{k\geq1}
\left\lfloor\frac{n}{p^k}\right\rfloor.
$$

::: {.proof}
For each positive integer $r$,
$$
v_p(r)
=
\sum_{k\geq1}\mathbf 1_{p^k\mid r}.
$$
Therefore step <1>1 gives
$$
\begin{aligned}
a(n)
&=
\sum_{r=1}^n\sum_{k\geq1}\mathbf 1_{p^k\mid r}\\
&=
\sum_{k\geq1}
\#\{1\leq r\leq n:p^k\mid r\}\\
&=
\sum_{k\geq1}
\left\lfloor\frac{n}{p^k}\right\rfloor.
\end{aligned}
$$
Only finitely many terms are nonzero. This proves part (a).
:::

<1>3. If
$$
n=\sum_{j\geq0}d_jp^j,
\qquad
0\leq d_j<p,
$$
then for every $k\geq1$,
$$
\left\lfloor\frac{n}{p^k}\right\rfloor
=
\sum_{j\geq k}d_jp^{j-k}.
$$

::: {.proof}
Divide the base-$p$ expansion by $p^k$:
$$
\frac{n}{p^k}
=
\sum_{j\geq k}d_jp^{j-k}
+
\sum_{0\leq j<k}d_jp^{j-k}.
$$
The first sum is an integer. The second is nonnegative and strictly less than $1$, since
$$
0
\leq
\sum_{0\leq j<k}d_jp^j
<
p^k.
$$
Taking the floor gives the displayed formula.
:::

<1>4. In terms of the base-$p$ digits,
$$
\boxed{
a(n)
=
\sum_{j\geq1}d_j(1+p+\cdots+p^{j-1})
}.
$$

::: {.proof}
Substitute step <1>3 into step <1>2 and interchange the finite sums:
$$
\begin{aligned}
a(n)
&=
\sum_{k\geq1}\sum_{j\geq k}d_jp^{j-k}\\
&=
\sum_{j\geq1}d_j\sum_{k=1}^{j}p^{j-k}\\
&=
\sum_{j\geq1}d_j(1+p+\cdots+p^{j-1}).
\end{aligned}
$$
This proves part (b).
:::

<1>5. The quantities $n$, $a(n)$, and $b(n)$ satisfy
$$
\boxed{n=(p-1)a(n)+b(n)}.
$$

::: {.proof}
By step <1>4,
$$
\begin{aligned}
(p-1)a(n)
&=
\sum_{j\geq1}d_j(p^j-1)\\
&=
\sum_{j\geq1}d_jp^j
-
\sum_{j\geq1}d_j.
\end{aligned}
$$
Since
$$
n=\sum_{j\geq0}d_jp^j
$$
and
$$
b(n)=\sum_{j\geq0}d_j,
$$
adding $b(n)$ to the preceding identity gives
$$
(p-1)a(n)+b(n)=n.
$$
This proves part (c).
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), step <1>4 proves part (b), and step <1>5 proves part (c).
:::
:::
