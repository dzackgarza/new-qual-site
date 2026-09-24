---
schema: qual/card@1
id: P-BKF08-6B
kind: problem
title: The identity $\int_0^1 x^{-x}\,dx=\sum_{n\ge1} n^{-n}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the logarithmic-moment integral by induction and the
    termwise integration by monotone convergence of nonnegative terms.
---

::: {.problem}
Show that
$$
\int_0^1\frac{1}{x^x}\,dx=\sum_{n=1}^{\infty}\frac1{n^n}.
$$
:::

::: {.hint}
Write $x^x$ in terms of the exponential and logarithm functions, and evaluate
$$
\int_0^1x^s\log(x)^n\,dx.
$$
:::

::: {.solution}
<1>1. For every real $s>-1$ and integer $n\ge0$,
$$
\int_0^1x^s\log(x)^n\,dx
=\frac{(-1)^n n!}{(s+1)^{n+1}}.
$$

::: {.proof}
For $n=0$,
$$
\int_0^1x^s\,dx=\frac1{s+1}.
$$
For $n\ge1$, integration by parts with
$$
u=\log(x)^n,
\qquad
dv=x^s\,dx
$$
gives
$$
\int_0^1x^s\log(x)^n\,dx
=-\frac{n}{s+1}
\int_0^1x^s\log(x)^{n-1}\,dx.
$$
The boundary term vanishes: it is zero at $x=1$, and
$x^{s+1}\abs{\log x}^n\to0$ as $x\to0^+$ because $s+1>0$.
Induction on $n$ now yields the displayed formula.
:::

<1>2. For $0<x\le1$,
$$
x^{-x}
=\sum_{n=0}^{\infty}\frac{(-x\log x)^n}{n!},
$$
and every term in this series is nonnegative.

::: {.proof}
Since $x^{-x}=e^{-x\log x}$, the exponential power series gives the
identity. On $(0,1]$ one has $\log x\le0$, hence
$-x\log x\ge0$, so every summand is nonnegative.
:::

<1>3. The series in step <1>2 may be integrated term by term on
$(0,1)$.

::: {.proof}
The partial sums
$$
S_N(x)=\sum_{n=0}^N\frac{(-x\log x)^n}{n!}
$$
are nonnegative and increase pointwise to $x^{-x}$ by step <1>2.
Therefore the monotone convergence theorem gives
$$
\int_0^1x^{-x}\,dx
=\sum_{n=0}^{\infty}\frac1{n!}
  \int_0^1x^n(-\log x)^n\,dx.
$$
:::

<1>4. For every integer $n\ge0$,
$$
\frac1{n!}\int_0^1x^n(-\log x)^n\,dx
=\frac1{(n+1)^{n+1}}.
$$

::: {.proof}
Applying step <1>1 with $s=n$ gives
$$
\int_0^1x^n\log(x)^n\,dx
=\frac{(-1)^n n!}{(n+1)^{n+1}}.
$$
Multiplying the integrand by $(-1)^n$ and dividing by $n!$ yields the
claim.
:::

<1>5. Hence
$$
\boxed{
\int_0^1x^{-x}\,dx
=\sum_{m=1}^{\infty}\frac1{m^m}
}.
$$

::: {.proof}
Combining steps <1>3 and <1>4 gives
$$
\int_0^1x^{-x}\,dx
=\sum_{n=0}^{\infty}\frac1{(n+1)^{n+1}}.
$$
Relabeling $m=n+1$ gives the displayed identity.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is exactly the required identity.
:::
:::
