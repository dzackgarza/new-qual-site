---
schema: qual/card@1
id: P-BKS05-5A
kind: problem
title: Higher derivative test for local extrema
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked and sharpened the retained argument. The sign of
    f^{(n-1)} near a follows directly from the existence and positivity of
    f^{(n)}(a); Taylor's theorem of order n-2 then gives the required strict
    one-sided inequalities. The n=1 case is handled separately.
---

::: {.problem}
Let I be an open interval and let $f \colon I \to \mathbb { R }$ have continuous k-th derivatives everywhere on I for all $k \leq n - 1$ . Let $a \in I$ be such that $f ^ { ( k ) } ( a ) = 0$ for $1 \leq k \leq n - 1$ , and assume that $f ^ { ( n ) } ( a )$ is defined and $f ^ { ( n ) } ( a ) > 0$ . Prove that if n is even, then f has a local minimum at a, and if n is odd, then f has no local extremum at a.
:::

::: {.solution}

::: pf

::: {.pf-step #n1-no-extremum}
If $n=1$, then $f$ has no local extremum at $a$.

::: pf-proof
Since
$$
f'(a)
=
\lim_{x\to a}\frac{f(x)-f(a)}{x-a}
>0,
$$
there is $\delta>0$ such that
$$
\frac{f(x)-f(a)}{x-a}>0
$$
whenever $0<|x-a|<\delta$. Shrinking $\delta$ if necessary, assume
$(a-\delta,a+\delta)\subseteq I$. Thus $f(x)<f(a)$ for
$a-\delta<x<a$, while $f(x)>f(a)$ for
$a<x<a+\delta$. Hence $a$ is neither a local maximum nor a local
minimum.
:::

:::

::: {.pf-step #derivative-sign-matches}
Assume $n\geq2$. Then there is $\delta>0$ such that
$f^{(n-1)}(x)$ has the same sign as $x-a$ whenever
$0<|x-a|<\delta$.

::: pf-proof
The hypothesis $f^{(n-1)}(a)=0$ and the existence of $f^{(n)}(a)$ give
$$
\lim_{x\to a}
\frac{f^{(n-1)}(x)}{x-a}
=
f^{(n)}(a)
>0.
$$
Therefore the displayed quotient is positive for all sufficiently
small nonzero $x-a$. Its numerator consequently has the same sign as
its denominator. Shrinking $\delta$ if necessary, also assume
$(a-\delta,a+\delta)\subseteq I$.
:::

:::

::: {.pf-step #taylor-remainder}
Assume $n\geq2$ and $0<|x-a|<\delta$. There is a point $c$
strictly between $a$ and $x$ such that
$$
f(x)-f(a)
=
\frac{f^{(n-1)}(c)}{(n-1)!}(x-a)^{n-1}.
$$

::: pf-proof
Apply Taylor's theorem with Lagrange remainder through order $n-2$ at
$a$. The hypotheses give
$$
f^{(k)}(a)=0
$$
for $1\leq k\leq n-2$, so all nonconstant Taylor terms vanish. The
remainder has the stated form for some $c$ strictly between $a$ and
$x$.
:::

:::

::: {.pf-step #even-n-local-min}
If $n$ is even, then $f$ has a strict local minimum at $a$.

::: pf-proof
Take $0<|x-a|<\delta$ and let $c$ be as in step [](#taylor-remainder){.pf-ref}. If $x>a$, then
$c>a$, so step [](#derivative-sign-matches){.pf-ref} gives
$$
f^{(n-1)}(c)>0.
$$
Since $(x-a)^{n-1}>0$, step [](#taylor-remainder){.pf-ref} gives $f(x)>f(a)$.

If $x<a$, then $c<a$, so $f^{(n-1)}(c)<0$. Because $n$ is even,
$n-1$ is odd and $(x-a)^{n-1}<0$. Step [](#taylor-remainder){.pf-ref} again gives
$f(x)>f(a)$. Thus every sufficiently close $x\neq a$ satisfies
$f(x)>f(a)$.
:::

:::

::: {.pf-step #odd-n-no-extremum}
If $n$ is odd, then $f$ has no local extremum at $a$.

::: pf-proof
For $n=1$ this is step [](#n1-no-extremum){.pf-ref}. Suppose $n\geq3$. If
$a<x<a+\delta$, then the argument in step [](#even-n-local-min){.pf-ref} gives
$f(x)>f(a)$. If $a-\delta<x<a$, then step [](#derivative-sign-matches){.pf-ref} gives
$f^{(n-1)}(c)<0$, while $n-1$ is even and hence
$(x-a)^{n-1}>0$. By step [](#taylor-remainder){.pf-ref},
$$
f(x)<f(a).
$$
There are therefore arbitrarily close points on one side with values
below $f(a)$ and on the other side with values above $f(a)$, so $a$
is neither a local maximum nor a local minimum.
:::

:::

::: pf-qed
Step [](#even-n-local-min){.pf-ref} proves the assertion for even $n$, and step [](#odd-n-no-extremum){.pf-ref} proves it
for odd $n$.
:::

:::

:::
