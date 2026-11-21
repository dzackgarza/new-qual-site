---
schema: qual/card@1
id: P-PSIBT
kind: problem
title: $\int_0^\infty\frac{\log x}{1+x^3}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the substitution
    u = x^3 giving (1/3)u^{s/3-1}/(1+u), the beta integral by the Gamma reflection formula
    with a = s/3 in (0,1), the closed form (pi/3)csc(pi s/3), the differentiation under the
    integral sign with an explicit dominating function (x^{a-1}|log x| near 0 and
    x^{b-4}|log x| at infinity on [a,b] in (0,3)), and the value -2 pi^2/27 at s = 1. The
    prose asserted that domination "justifies" the differentiation without producing the
    dominating function; that is now a step. The value was confirmed numerically
    (-0.7310789 against the closed form's -0.7310818). The collection's provenance is the
    examination paper only, so no retained solution set covers the exercise and the argument
    is the card's own.
---

::: {.problem}
Compute the following integral carefully justifying each step:

$$
\int_{0}^{\infty} \frac{\log x}{1+x^{3}}\,dx.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
For $0<s<3$ put $I(s)\coloneqq\int_0^\infty\frac{x^{s-1}}{1+x^3}dx$.

::: pf

::: {.pf-step #substitution}
$\displaystyle I(s)=\frac13\int_0^\infty\frac{u^{s/3-1}}{1+u}\,du$ for $0<s<3$.

::: pf-proof
Substitute $u=x^3$, so $x=u^{1/3}$ and $dx=\frac13u^{-2/3}du$; then $x^{s-1}dx=u^{(s-1)/3}\frac13u^{-2/3}du=\frac13u^{s/3-1}du$, and $x$ runs over $(0,\infty)$ as $u$ does.
:::

:::

::: {.pf-step #beta}
$\displaystyle\int_0^\infty\frac{u^{a-1}}{1+u}\,du=\frac{\pi}{\sin \pi a}$ for $0<a<1$.

::: pf-proof
This is Euler's beta integral in the form $B(a,1-a)=\int_0^\infty\frac{u^{a-1}}{1+u}du=\Gamma(a)\Gamma(1-a)=\frac{\pi}{\sin\pi a}$, by the reflection formula for $\Gamma$; both hypotheses $0<a<1$ hold, since $a=\frac{s}{3}$ with $0<s<3$.
:::

:::

::: {.pf-step #closed-form}
$I(s)=\frac{\pi}{3}\csc\left(\frac{\pi s}{3}\right)$ for $0<s<3$.

::: pf-proof
Steps [](#substitution){.pf-ref} and [](#beta){.pf-ref} with $a=\frac s3\in(0,1)$ give $I(s)=\frac13\cdot\frac{\pi}{\sin(\pi s/3)}$.
:::

:::

::: {.pf-step #differentiation}
On every compact subinterval $[a,b]\subset(0,3)$,
$$
I'(s)=\int_0^\infty\frac{x^{s-1}\log x}{1+x^3}\,dx
$$
for $s\in[a,b]$, in particular at $s=1$.

::: pf-proof
The integrand and its $s$-derivative $\frac{x^{s-1}\log x}{1+x^3}$ are continuous in $(s,x)$ on $[a,b]\times(0,\infty)$. On that range the derivative is dominated by an integrable function of $x$ alone: for $0<x\le1$ it is at most $\frac{x^{a-1}\abs{\log x}}{1}$ and for $x\ge1$ at most $x^{b-4}\abs{\log x}$, and $x^{p-1}\abs{\log x}$ is integrable on $(0,1]$ for $p>0$ and $x^{-1-q}\abs{\log x}$ is integrable on $[1,\infty)$ for $q>0$; here $a>0$ and $4-b>1$. Leibniz's rule for differentiating under the integral sign therefore applies on $[a,b]$. Since $1$ lies in the interior of $(0,3)$ and $[a,b]$ was arbitrary, the identity holds at $s=1$.
:::

:::

::: {.pf-step #derivative}
$I'(s)=-\frac{\pi^2}{9}\csc\left(\frac{\pi s}{3}\right)\cot\left(\frac{\pi s}{3}\right)$.

::: pf-proof
Differentiate step [](#closed-form){.pf-ref}: $\frac{d}{ds}\csc\left(\frac{\pi s}{3}\right)=-\frac{\pi}{3}\csc\left(\frac{\pi s}{3}\right)\cot\left(\frac{\pi s}{3}\right)$, so $I'(s)=-\frac{\pi^2}{9}\csc\left(\frac{\pi s}{3}\right)\cot\left(\frac{\pi s}{3}\right)$.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^\infty\frac{\log x}{1+x^3}\,dx=\boxed{-\frac{2\pi^2}{27}}$.

::: pf-proof
By step [](#differentiation){.pf-ref} the desired integral is $I'(1)$, and step [](#derivative){.pf-ref} gives $I'(1)=-\frac{\pi^2}{9}\csc\left(\frac{\pi}{3}\right)\cot\left(\frac{\pi}{3}\right)=-\frac{\pi^2}{9}\cdot\frac{2}{\sqrt3}\cdot\frac{1}{\sqrt3}=-\frac{2\pi^2}{27}$, since $\sin\frac\pi3=\frac{\sqrt3}{2}$ and $\tan\frac\pi3=\sqrt3$. The value is $-0.73108\ldots$, which a numerical quadrature of the integral confirms.
:::

:::

:::
:::
