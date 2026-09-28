---
schema: qual/card@1
id: P-BKS05-9B
kind: problem
title: Square roots of $x$ modulo $x^n-1$ in $\RR[x]$
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
    Independently checked both parity cases using evaluation on the distinct nth roots
    of unity and conjugation-compatible Lagrange interpolation.
---

::: {.problem}
(a) Prove that if $n > 0$ is even, there does not exist $f ( x ) \in \mathbb { R } [ x ]$ such that $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$

(b) For odd $n > 0$ , find the number of $f ( x ) \in \mathbb { R } [ x ]$ of degree $< n$ such that $f ( x ) ^ { 2 } - x$ is divisible by $x ^ { n } - 1$
:::

::: {.solution}
Let
$$
\mu_n\coloneqq\{\zeta\in\CC:\zeta^n=1\}.
$$

<1>1. If $n$ is even, no polynomial $f\in\RR[x]$ satisfies the divisibility
condition.

::: {.proof}
When $n$ is even, $-1\in\mu_n$, so $x+1$ divides $x^n-1$. If
$x^n-1$ divided $f(x)^2-x$, then evaluation at $x=-1$ would give
$$
f(-1)^2+1=0.
$$
This is impossible because $f(-1)\in\RR$.
:::

<1>2. Suppose $n$ is odd. A polynomial $f\in\RR[x]$ of degree $<n$
satisfies
$$
x^n-1\mid f(x)^2-x
$$
exactly when, for every $\zeta\in\mu_n$, its value $f(\zeta)$ is a square
root of $\zeta$, with the choices on conjugate roots related by complex
conjugation.

::: {.proof}
The roots in $\mu_n$ are distinct, since the derivative of $x^n-1$ is
$nx^{n-1}$ and no element of $\mu_n$ is zero. Hence
$$
x^n-1\mid f(x)^2-x
$$
if and only if
$$
f(\zeta)^2=\zeta
$$
for every $\zeta\in\mu_n$.

A polynomial with real coefficients satisfies
$$
f(\overline\zeta)=\overline{f(\zeta)}.
$$
Conversely, prescribe values $c_\zeta$ on the $n$ distinct roots in
$\mu_n$ such that
$$
c_{\overline\zeta}=\overline{c_\zeta}.
$$
Lagrange interpolation gives a unique polynomial $F\in\CC[x]$ of degree
$<n$ with $F(\zeta)=c_\zeta$ for all $\zeta\in\mu_n$. The polynomial
$$
\overline{F(\overline x)}
$$
has the same degree bound and takes the same prescribed values on every
$\zeta\in\mu_n$. By uniqueness of interpolation, it equals $F$, so all
coefficients of $F$ are real. Thus the stated conjugation compatibility is
exactly the condition for the interpolating polynomial to lie in $\RR[x]$.
:::

<1>3. For odd $n$, the number of such polynomials is
$$
\boxed{2^{(n+1)/2}}.
$$

::: {.proof}
Because $n$ is odd, the only real element of $\mu_n$ is $1$; the remaining
$n-1$ roots form $(n-1)/2$ conjugate pairs.

At $\zeta=1$, the equation
$$
f(1)^2=1
$$
gives two choices, $f(1)=1$ or $f(1)=-1$.

For each conjugate pair $\{\zeta,\overline\zeta\}$, choose one square root
$s$ of $\zeta$. There are exactly two choices for $s$, and then realness
forces
$$
f(\overline\zeta)=\overline s,
$$
which is automatically a square root of $\overline\zeta$. These choices are
independent from pair to pair. Step <1>2 shows that every such compatible
set of choices gives exactly one polynomial in $\RR[x]$ of degree $<n$,
and every desired polynomial arises this way. Therefore the number is
$$
2\cdot2^{(n-1)/2}=2^{(n+1)/2}.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>3 proves part (b).
:::
:::
