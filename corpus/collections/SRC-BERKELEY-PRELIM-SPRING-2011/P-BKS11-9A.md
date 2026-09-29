---
schema: qual/card@1
id: P-BKS11-9A
kind: problem
title: Generating function of the Catalan numbers
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
  note: Compared the authored statement with page 3 of the retained Spring 2011 solution PDF and independently reviewed the generating-function and binomial-series argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the formal power-series quadratic equation, branch selection, coefficient extraction, and radius of convergence.
---

::: {.problem}
The Catalan numbers $C ( n )$ satisfy $C ( 0 ) = 1 , C ( n ) = C ( 0 ) C ( n - 1 ) + C ( 1 ) C ( n - 2 ) + \cdots +$ $C ( n - 1 ) C ( 0 )$ if $n > 0$ . Find the function $\textstyle \sum _ { n = 0 } ^ { \infty } C ( n ) x ^ { n }$ and use this to evaluate $C ( n )$
:::

::: {.solution}
Let
$$
F(x)\coloneqq\sum_{n=0}^{\infty}C(n)x^n
$$
initially as a formal power series.

::: pf

::: {.pf-step #quadratic-relation}
The recurrence is equivalent to
$$
F(x)=1+xF(x)^2.
$$

::: pf-proof
The coefficient of $x^n$ in $F(x)^2$ is
$$
\sum_{j=0}^n C(j)C(n-j).
$$
Therefore the coefficient of $x^n$ in $xF(x)^2$, for $n\geq1$, is
$$
\sum_{j=0}^{n-1}C(j)C(n-1-j)
=
C(n)
$$
by the given recurrence. The constant term of $xF(x)^2$ is $0$, while
$C(0)=1$. Hence
$$
F(x)-1=xF(x)^2.
$$
:::

:::

::: {.pf-step #formal-solution}
The unique formal power-series solution of step [](#quadratic-relation){.pf-ref} with constant
term $1$ is
$$
F(x)
=
\frac{1-\sqrt{1-4x}}{2x},
$$
where $\sqrt{1-4x}$ denotes the formal square root with constant term
$1$.

::: pf-proof
The quadratic equation in step [](#quadratic-relation){.pf-ref} is
$$
xF(x)^2-F(x)+1=0.
$$
Formally solving this quadratic gives
$$
F(x)
=
\frac{1\pm\sqrt{1-4x}}{2x}.
$$
There is a unique formal series
$$
S(x)\in\QQ[[x]]
$$
with constant term $1$ and
$$
S(x)^2=1-4x,
$$
namely the binomial series
$$
S(x)
=
\sum_{j=0}^{\infty}
\binom{1/2}{j}(-4x)^j.
$$
The numerator
$$
1+S(x)
$$
has constant term $2$, so
$$
\frac{1+S(x)}{2x}
$$
is not a formal power series. By contrast,
$$
1-S(x)
$$
has zero constant term, so division by $x$ is valid in
$\QQ[[x]]$. Thus the minus sign is forced.
:::

:::

::: {.pf-step #closed-form-catalan}
For every $n\geq0$,
$$
\boxed{
C(n)
=
\frac{1}{n+1}\binom{2n}{n}
=
\frac{(2n)!}{n!(n+1)!}
}.
$$

::: pf-proof
For $n=0$, the formula gives $1$, agreeing with the defining value
$C(0)=1$. Assume now that $n\geq1$.

From step [](#formal-solution){.pf-ref} and the binomial expansion,
$$
\begin{aligned}
F(x)
&=
-\frac{1}{2x}
\sum_{j=1}^{\infty}
\binom{1/2}{j}(-4x)^j.
\end{aligned}
$$
Hence the coefficient of $x^n$ is
$$
C(n)
=
-\frac12
\binom{1/2}{n+1}
(-4)^{n+1}.
$$
Now
$$
\binom{1/2}{n+1}
=
\frac{
(1/2)(-1/2)(-3/2)\cdots(1/2-n)
}{(n+1)!}
=
\frac{
(-1)^n(2n-1)!!
}{
2^{n+1}(n+1)!
}.
$$
Therefore
$$
\begin{aligned}
C(n)
&=
2^n
\frac{(2n-1)!!}{(n+1)!}\\
&=
\frac{(2n)!}{n!(n+1)!},
\end{aligned}
$$
because
$$
(2n)!
=
2^n n!(2n-1)!!.
$$
The equivalent binomial-coefficient form follows immediately.
:::

:::

::: {.pf-step #radius-of-convergence}
The ordinary power series $F(x)$ has radius of convergence
$$
\frac14.
$$

::: pf-proof
Using the formula in step [](#closed-form-catalan){.pf-ref},
$$
\frac{C(n+1)}{C(n)}
=
\frac{2(2n+1)}{n+2}.
$$
Thus
$$
\lim_{n\to\infty}
\frac{C(n+1)}{C(n)}
=
4.
$$
The ratio test therefore gives radius of convergence $1/4$.
:::

:::

::: {.pf-step #analytic-identity}
Consequently, for $\abs{x}<1/4$,
$$
\boxed{
\sum_{n=0}^{\infty}C(n)x^n
=
\frac{1-\sqrt{1-4x}}{2x}
},
$$
with the value at $x=0$ understood as $1$.

::: pf-proof
By step [](#radius-of-convergence){.pf-ref}, the Catalan generating series converges for
$\abs{x}<1/4$. In that disk the ordinary binomial series for
$\sqrt{1-4x}$ converges, so the formal identity of step [](#formal-solution){.pf-ref} is an
analytic identity there. At $x=0$, the apparent singularity is removable;
equivalently,
$$
\frac{1-\sqrt{1-4x}}{2x}
=
\frac{2}{1+\sqrt{1-4x}},
$$
whose value at $0$ is $1$.
:::

:::

::: pf-qed
Step [](#analytic-identity){.pf-ref} gives the generating function, and step [](#closed-form-catalan){.pf-ref} gives the explicit
formula for $C(n)$.
:::

:::

:::
