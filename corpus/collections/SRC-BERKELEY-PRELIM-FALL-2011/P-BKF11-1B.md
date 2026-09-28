---
schema: qual/card@1
id: P-BKF11-1B
kind: problem
title: Convergence of $\sum n^a(\log n)^b$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked eventual monotonicity where the integral test is used and reduced
    the comparison integral by u=log x to its exponential/power threshold.
---

::: {.problem}
For which pairs of real numbers $(a,b)$ does the series
$$
\sum_{n=3}^{\infty}n^a(\log n)^b
$$
converge?
:::

::: {.solution}
Let
$$
u_n\coloneqq n^a(\log n)^b.
$$

<1>1. In every case in which $u_n\to0$, the function
$$
\phi(x)\coloneqq x^a(\log x)^b
$$
is eventually decreasing, so the convergence of
$\sum_{n=3}^{\infty}u_n$ is equivalent to the convergence of
$$
\int_3^\infty x^a(\log x)^b\,dx.
$$

::: {.proof}
For $x>1$,
$$
\frac{\phi'(x)}{\phi(x)}
=\frac1x\left(a+\frac{b}{\log x}\right).
$$
If $a<0$, the expression in parentheses is negative for all
sufficiently large $x$, so $\phi$ is eventually decreasing. If
$a=0$ and $u_n\to0$, then necessarily $b<0$, in which case
$\phi'(x)<0$ for every $x>1$.

If $a>0$, then $u_n\not\to0$; if $a=0$ and $b\ge0$, again
$u_n\not\to0$. Those cases already diverge by the term test. Thus
the integral test applies in every remaining case.
:::

<1>2. With the substitution $u=\log x$,
$$
\int_3^\infty x^a(\log x)^b\,dx
=\int_{\log3}^\infty e^{(a+1)u}u^b\,du.
$$

::: {.proof}
The substitution gives $x=e^u$ and $dx=e^u\,du$. Hence
$$
x^a(\log x)^b\,dx
=e^{au}u^b e^u\,du
=e^{(a+1)u}u^b\,du,
$$
with the stated limits.
:::

<1>3. If $a<-1$, then the integral in step <1>2 converges for every
$b\in\RR$; if $a>-1$, it diverges for every $b\in\RR$.

::: {.proof}
Suppose first that $a<-1$ and put $c=-(a+1)>0$. The integrand is
$e^{-cu}u^b$. If $b\le0$, it is bounded above for large $u$ by
$e^{-cu}$. If $b>0$, the standard limit
$$
u^b e^{-cu/2}\longrightarrow0
$$
shows that $u^b\le e^{cu/2}$ for all sufficiently large $u$.
Thus
$$
e^{-cu}u^b\le e^{-cu/2}
$$
eventually. In either case the integral converges.

Now suppose $a>-1$ and put $c=a+1>0$. If $b\ge0$, the integrand
$e^{cu}u^b$ is eventually at least $1$. If $b<0$, then
$$
e^{cu}u^b=\frac{e^{cu}}{u^{-b}}\longrightarrow\infty,
$$
since exponential growth dominates every power. Thus the integrand
does not even tend to $0$, and the integral diverges.
:::

<1>4. If $a=-1$, then the integral converges exactly when $b<-1$.

::: {.proof}
For $a=-1$, step <1>2 reduces the integral to
$$
\int_{\log3}^{\infty}u^b\,du.
$$
This power integral converges exactly for $b<-1$. For $b=-1$, its
antiderivative is $\log u$ and it diverges; for $b\ne-1$, its
antiderivative is $u^{b+1}/(b+1)$, which has a finite limit at
infinity exactly when $b+1<0$.
:::

<1>5. Therefore the series converges exactly for
$$
\boxed{
\{(a,b)\in\RR^2:a<-1\}
\;\cup\;
\{(-1,b):b<-1\}
}.
$$

::: {.proof}
Step <1>1 reduces every nontrivial case to the integral, and
steps <1>3 and <1>4 give its complete convergence classification.
The cases excluded in step <1>1 diverge by the term test and lie
outside the displayed set.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives all and only the requested pairs.
:::
:::
