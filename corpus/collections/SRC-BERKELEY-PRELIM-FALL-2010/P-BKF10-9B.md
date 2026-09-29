---
schema: qual/card@1
id: P-BKF10-9B
kind: problem
title: The divergent asymptotic series $\sum(-1)^n n!/x^{n+1}$ for $\int_0^\infty e^{-tx}/(1+t)\,dt$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked divergence by the term test, the exact finite-geometric
    remainder identity, the first-omitted-term bound, and the numerical
    error estimate at x=100.
---

::: {.problem}
(a) Prove that the series
$$
\frac{0!}{x}-\frac{1!}{x^2}+\frac{2!}{x^3}-\frac{3!}{x^4}+\cdots
$$
diverges for every nonzero $x$.

(b) If $x>0$ and
$$
G(x)=\int_0^{\infty}\frac{e^{-tx}}{1+t}\,dt,
$$
show that the absolute difference between $G(x)$ and the sum of the first $n$ terms of the series in (a) is at most the absolute value of the first omitted term.

(c) If $x=100$, prove that the sum of the first ten terms of the divergent series in (a) gives $G(x)$ correctly to more than ten decimal places.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every fixed $x\ne0$, the terms
$$
a_n(x)\coloneqq\frac{(-1)^n n!}{x^{n+1}}
$$
do not tend to $0$.

::: pf-proof

Their absolute values satisfy
$$
\frac{\abs{a_{n+1}(x)}}{\abs{a_n(x)}}
=\frac{n+1}{\abs{x}}.
$$
For all sufficiently large $n$, this ratio is at least $2$. Hence
$\abs{a_n(x)}$ eventually grows at least geometrically and in particular
does not tend to $0$.

:::

:::

::: {.pf-step #s2}

The series in part (a) diverges for every nonzero $x$.

::: pf-proof

A necessary condition for convergence of a series is that its terms tend
to $0$. Step [](#s1){.pf-ref} shows that this condition fails.

:::

:::

::: {.pf-step #s3}

For every integer $n\ge1$ and every $t\ge0$,
$$
\frac1{1+t}
=\sum_{k=0}^{n-1}(-1)^k t^k
+\frac{(-1)^n t^n}{1+t}.
$$

::: pf-proof

Multiplying the right-hand side by $1+t$ gives the finite geometric
identity
$$
(1+t)\sum_{k=0}^{n-1}(-t)^k+(-t)^n=1.
$$
Dividing by $1+t$ gives the claim.

:::

:::

::: {.pf-step #s4}

For $x>0$ and every integer $k\ge0$,
$$
\int_0^\infty e^{-tx}t^k\,dt
=\frac{k!}{x^{k+1}}.
$$

::: pf-proof

With the substitution $u=tx$,
$$
\int_0^\infty e^{-tx}t^k\,dt
=\frac1{x^{k+1}}
\int_0^\infty e^{-u}u^k\,du.
$$
Repeated integration by parts gives
$$
\int_0^\infty e^{-u}u^k\,du=k!,
$$
so the displayed formula follows.

:::

:::

::: {.pf-step #s5}

For $x>0$, if
$$
S_n(x)\coloneqq
\sum_{k=0}^{n-1}\frac{(-1)^k k!}{x^{k+1}},
$$
then
$$
G(x)-S_n(x)
=(-1)^n
\int_0^\infty\frac{e^{-tx}t^n}{1+t}\,dt.
$$

::: pf-proof

Multiply the identity from step [](#s3){.pf-ref} by $e^{-tx}$ and integrate over
$[0,\infty)$. The finite sum may be integrated term by term, and step
[](#s4){.pf-ref} evaluates its terms. This gives
$$
G(x)
=S_n(x)
+(-1)^n\int_0^\infty\frac{e^{-tx}t^n}{1+t}\,dt.
$$

:::

:::

::: {.pf-step #s6}

The error after the first $n$ terms satisfies
$$
\boxed{
\abs{G(x)-S_n(x)}
\le\frac{n!}{x^{n+1}}
}.
$$

::: pf-proof

Since $t\ge0$ implies $(1+t)^{-1}\le1$, step [](#s5){.pf-ref} gives
$$
\begin{aligned}
\abs{G(x)-S_n(x)}
&=\int_0^\infty\frac{e^{-tx}t^n}{1+t}\,dt\\
&\le\int_0^\infty e^{-tx}t^n\,dt\\
&=\frac{n!}{x^{n+1}}
\end{aligned}
$$
by step [](#s4){.pf-ref}. The right-hand side is exactly the absolute value of the
first omitted term, whose index is $n$.

:::

:::

::: pf-step

At $x=100$, the first ten terms approximate $G(100)$ with error
less than $10^{-15}$.

::: pf-proof

Take $n=10$ in step [](#s6){.pf-ref}. Then
$$
\abs{G(100)-S_{10}(100)}
\le\frac{10!}{100^{11}}
=\frac{3{,}628{,}800}{10^{22}}
=3.6288\times10^{-16}
<10^{-15}.
$$

:::

:::

::: {.pf-step #s8}

Therefore the first ten terms give $G(100)$ correctly to more
than ten decimal places.

::: pf-proof

An absolute error smaller than $10^{-15}$ is, in particular, smaller
than $10^{-11}$. Thus the approximation determines more than ten digits
after the decimal point correctly, as required.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), step [](#s6){.pf-ref} proves part (b), and step [](#s8){.pf-ref} proves
part (c).

:::

:::

:::
