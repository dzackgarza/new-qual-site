---
schema: qual/card@1
id: P-BKS09-3A
kind: problem
title: Polynomial growth forces a meromorphic function to be rational
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
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed its pole-clearing argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked that the growth bound excludes poles outside a compact disk,
    that only finitely many poles remain, and that Cauchy estimates force the pole-cleared entire function to be a polynomial.
---

::: {.problem}
Show that if $f : \mathbb { C } \to \hat { \mathbb { C } }$ is a meromorphic function in the plane, such that there exists $R , C > 0$ so that for $| z | > R , | f ( z ) | \leq C | z | ^ { n }$ , then f is a rational function.
:::

::: {.solution}

::: pf

::: {.pf-step #finitely-many-poles}
The function $f$ has only finitely many poles.

::: pf-proof
The bound
$$
\abs{f(z)}\leq C\abs z^n
$$
is finite for every $\abs z>R$, so $f$ has no pole outside the closed disk
$\abs z\leq R$. The poles of a meromorphic function are isolated. If there
were infinitely many poles in the compact disk $\abs z\leq R$, they would
have an accumulation point in that disk, contradicting isolatedness of the
poles. Hence there are only finitely many.
:::

:::

::: {.pf-step #pole-cleared-entire}
There is a polynomial $P$ such that
$$
g\coloneqq Pf
$$
is entire.

::: pf-proof
Let the distinct poles of $f$ be $a_1,\ldots,a_r$, with respective orders
$m_1,\ldots,m_r$, and set
$$
P(z)\coloneqq\prod_{j=1}^r(z-a_j)^{m_j}.
$$
At each $a_j$, multiplication by $(z-a_j)^{m_j}$ removes the pole of $f$,
while the remaining factors are holomorphic and nonzero there. Thus every
singularity of $Pf$ is removable. Away from the poles, $Pf$ is already
holomorphic, so after filling in the removable singularities, $g=Pf$ is
entire.
:::

:::

::: {.pf-step #g-is-polynomial}
The entire function $g$ is a polynomial.

::: pf-proof
Let
$$
m\coloneqq m_1+\cdots+m_r=\deg P.
$$
For sufficiently large $\abs z$, there is a constant $C_1>0$ such that
$$
\abs{P(z)}\leq C_1\abs z^m.
$$
Hence the assumed growth bound gives another constant $C_2>0$ such that
$$
\abs{g(z)}\leq C_2\abs z^{m+n}
$$
for all sufficiently large $\abs z$.

Choose an integer $k>m+n$. For all sufficiently large radii $\rho$, the
Cauchy estimate on the circle $\abs z=\rho$ gives
$$
\abs{g^{(k)}(0)}
\leq
\frac{k!}{\rho^k}
\max_{\abs z=\rho}\abs{g(z)}
\leq
k!C_2\rho^{m+n-k}.
$$
Because $m+n-k<0$, the right-hand side tends to $0$ as
$\rho\to\infty$. Therefore $g^{(k)}(0)=0$ for every sufficiently large
integer $k$. The Taylor series of the entire function $g$ consequently has
only finitely many nonzero coefficients, so $g$ is a polynomial.
:::

:::

::: {.pf-step #f-rational}
The function $f$ is rational.

::: pf-proof
By steps [](#pole-cleared-entire){.pf-ref} and [](#g-is-polynomial){.pf-ref}, both $P$ and $g=Pf$ are polynomials. Therefore
$$
f=\frac{g}{P}
$$
as meromorphic functions on $\CC$, so $f$ is rational.
:::

:::

::: pf-qed
Step [](#f-rational){.pf-ref} is the required conclusion.
:::

:::

:::
