---
schema: qual/card@1
id: P-BDFPC
kind: problem
title: Riemann–Stieltjes integral against a jump, and vanishing of $g$ against $x^{3k+2}$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Stone-Weierstrass
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 6 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: "Corrected the Stieltjes partition argument: because alpha(0)=-1 and alpha(x)=1 for x>0, the nonzero increment is on the interval beginning at 0."
---

::: {.problem}
1. Suppose $f:[-1,1]\to\mathbb R$ is bounded and continuous at $0$. Let
\[
\alpha(x)=
\begin{cases}
-1,&x\in[-1,0],\\
1,&x\in(0,1].
\end{cases}
\]
Prove that $f\in\mathcal R(\alpha)[-1,1]$ and
\[
\int_{-1}^1 f\,d\alpha=2f(0).
\]

2. Let $g:[0,1]\to\mathbb R$ be continuous and suppose
\[
\int_0^1 g(x)x^{3k+2}\,dx=0
\qquad(k=0,1,2,\ldots).
\]
Prove that $g\equiv0$.
:::

::: {.solution}
<1>1. Prove the Riemann--Stieltjes assertion.
::: {.proof}
The integrator $\alpha$ is nondecreasing and has a single jump of size $2$ immediately to the right of $0$.

Fix $\varepsilon>0$. By continuity of $f$ at $0$, choose $r\in(0,1)$ such that
\[
|f(x)-f(0)|<\frac{\varepsilon}{4}
\qquad(0\le x\le r).
\]
Take any partition containing the points
\[
-1<0<r<1.
\]
All increments of $\alpha$ are zero except the one on the subinterval $[0,r]$, where
\[
\alpha(r)-\alpha(0)=1-(-1)=2.
\]
Consequently, if $M$ and $m$ are the supremum and infimum of $f$ on $[0,r]$, then
\[
U(f,P,\alpha)-L(f,P,\alpha)=2(M-m).
\]
Since $|f(x)-f(0)|<\varepsilon/4$ on $[0,r]$,
\[
M-m<\frac{\varepsilon}{2},
\]
and hence
\[
U(f,P,\alpha)-L(f,P,\alpha)<\varepsilon.
\]
Thus $f\in\mathcal R(\alpha)[-1,1]$.

Moreover,
\[
2m\le \int_{-1}^1f\,d\alpha\le2M,
\]
and both $m$ and $M$ can be made arbitrarily close to $f(0)$ by shrinking $r$. Therefore
\[
\boxed{\int_{-1}^1f\,d\alpha=2f(0)}.
\]
:::

<1>2. Extend the moment identities from monomials to polynomials in $x^3$.
::: {.proof}
For every polynomial $p$,
\[
x^2p(x^3)
\]
is a finite linear combination of the functions $x^{3k+2}$. Hence the hypothesis gives
\[
\int_0^1 g(x)x^2p(x^3)\,dx=0.
\]
:::

<1>3. Approximate $g$ by polynomials in $x^3$.
::: {.proof}
Define
\[
h(t):=g(t^{1/3}),\qquad t\in[0,1].
\]
Then $h$ is continuous. By the Weierstrass approximation theorem there are polynomials $p_n$ such that
\[
p_n\to h
\]
uniformly on $[0,1]$. Substituting $t=x^3$ gives
\[
p_n(x^3)\to g(x)
\]
uniformly on $[0,1]$.

Since $x^2g(x)$ is bounded, we may pass to the limit in the identities from Step 2:
\[
0
=\lim_{n\to\infty}\int_0^1 g(x)x^2p_n(x^3)\,dx
=\int_0^1x^2g(x)^2\,dx.
\]
The integrand is continuous and nonnegative, so it vanishes identically. Thus $g(x)=0$ for every $x\in(0,1]$, and continuity gives $g(0)=0$. Hence
\[
\boxed{g\equiv0}.
\]
:::
:::
