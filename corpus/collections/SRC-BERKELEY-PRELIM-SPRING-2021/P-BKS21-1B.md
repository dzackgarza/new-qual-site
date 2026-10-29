---
schema: qual/card@1
id: P-BKS21-1B
kind: problem
title: Convergence of $\sum n^a(\log n)^b$
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
For which pairs $(a,b)\in\RR^2$ does
$$
\sum_{n=3}^{\infty}n^a(\log n)^b
$$
converge?
:::

::: {.solution}

For $x\geq3$, set
$$
f(x)\coloneqq x^a(\log x)^b.
$$

::: pf

::: {.pf-step #s1-1}

If $a>0$, or if $a=0$ and $b\geq0$, then the series diverges.


::: pf-proof

If $a>0$, then
$$
n^a(\log n)^b\not\longrightarrow0,
$$
because the polynomial factor $n^a$ dominates any fixed power of $\log n$; equivalently,
$$
\log\!\bigl(n^a(\log n)^b\bigr)
=
a\log n+b\log\log n
\longrightarrow+\infty.
$$
If $a=0$ and $b>0$, then $(\log n)^b\to\infty$, while if $a=b=0$ the terms are identically $1$. In every case the terms fail to tend to $0$, so the series diverges.

:::

:::

::: {.pf-step #s1-2}

In all remaining cases, $f$ is eventually decreasing, so the integral test applies.


::: pf-proof

For $x>1$,
$$
\frac{f'(x)}{f(x)}
=
\frac{1}{x}\left(a+\frac{b}{\log x}\right).
$$
If $a<0$, the parenthesized quantity tends to $a<0$, so it is negative for all sufficiently large $x$. If $a=0$ and $b<0$, it is negative for every $x>1$. Hence $f$ is eventually decreasing in every case not covered by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The improper integral
$$
\int_3^\infty x^a(\log x)^b\,dx
$$
equals
$$
\int_{\log3}^{\infty}e^{(a+1)t}t^b\,dt
$$
after the substitution $t=\log x$.


::: pf-proof

With $x=e^t$ one has $dx=e^t\,dt$, and therefore
$$
x^a(\log x)^b\,dx
=
e^{at}t^b e^t\,dt
=
e^{(a+1)t}t^b\,dt.
$$

:::

:::

::: {.pf-step #s1-4}

If $a<-1$, then the integral in step [](#s1-3){.pf-ref} converges for every $b\in\RR$.


::: pf-proof

Set $c\coloneqq-(a+1)>0$. The integrand is
$$
e^{-ct}t^b.
$$
Since
$$
\frac{b\log t}{t}\longrightarrow0,
$$
there is $T$ such that
$$
t^b=e^{b\log t}\leq e^{ct/2}
$$
for $t\geq T$. Hence
$$
0\leq e^{-ct}t^b\leq e^{-ct/2}
$$
eventually, and the latter function is integrable on $[T,\infty)$.

:::

:::

::: {.pf-step #s1-5}

If $a>-1$, then the series diverges for every $b\in\RR$.


::: pf-proof

The cases $a\geq0$ covered by step [](#s1-1){.pf-ref} already diverge. Suppose $-1<a<0$. Then $c\coloneqq a+1>0$, and step [](#s1-3){.pf-ref} gives the integrand
$$
e^{ct}t^b.
$$
Since $b\log t/t\to0$, for all sufficiently large $t$ one has
$$
t^b\geq e^{-ct/2}.
$$
Thus
$$
e^{ct}t^b\geq e^{ct/2},
$$
so the improper integral diverges. By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} and the integral test, the series diverges.

:::

:::

::: {.pf-step #s1-6}

If $a=-1$, then the series converges exactly when $b<-1$.


::: pf-proof

When $a=-1$, step [](#s1-3){.pf-ref} reduces the integral to
$$
\int_{\log3}^{\infty}t^b\,dt.
$$
This converges exactly for $b<-1$: if $b\neq-1$, an antiderivative is
$$
\frac{t^{b+1}}{b+1},
$$
which has a finite limit at infinity exactly when $b+1<0$; for $b=-1$, the antiderivative is $\log t$, which diverges. The integral test applies by step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore the series converges exactly for
$$
\boxed{
a<-1
\quad\text{or}\quad
\bigl(a=-1\ \text{and}\ b<-1\bigr)
}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives convergence for $a<-1$, step [](#s1-5){.pf-ref} gives divergence for $a>-1$, and step [](#s1-6){.pf-ref} settles the boundary $a=-1$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the complete classification.

:::

:::

:::
