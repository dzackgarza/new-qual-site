---
schema: qual/card@1
id: P-S4PJP
kind: problem
title: Convolution $L^p\to L^q$ bounds for compactly supported continuous $\phi$,
  and failure for $p>q$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 11 of the UCLA Analysis Qualifying Exam, Spring 2010, from the collection provenance PDF and independently reviewed the supplied UCLA solution compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Corrected the prior/source bound ||phi||_alpha <= ||phi||_infinity, which omits the support-measure factor and does not give the required single constant over all p<=q. Proved Young's inequality including the L-infinity endpoint, obtained a uniform bound ||phi||_alpha <= ||phi||_infinity max(1, |supp phi|), and made the p>q counterexample exponent condition explicit.
---

::: {.problem}
Let $\phi:\mathbb{R}\to\mathbb{R}$ be a continuous function with compact support.

a. Prove there is a constant $A$ such that $$||f*\phi||_{L^q} \le A||f||_{L^p} \quad \text{for all } 1\le p\le q\le\infty \quad \text{and all } f\in L^p.$$ If you use Young's convolution inequality you should prove it.

b. Show by example that such a general inequality cannot hold for $p>q$.
:::

::: {.solution}
We first prove the form of Young's convolution inequality needed below.

<1>1. Let $1\le p,a,r\le\infty$ satisfy
\[
1+\frac1r=\frac1p+\frac1a.
\]
Then
\[
\|f*g\|_{L^r}\le\|f\|_{L^p}\|g\|_{L^a}.
\]
::: {.proof}
First suppose $r<\infty$.
Then necessarily $p,a<\infty$, and the exponent relation implies
\[
r\ge p,
\qquad
r\ge a.
\]
For fixed $x$, write
\[
|f(x-y)g(y)|
=
|f(x-y)|^{1-p/r}
|g(y)|^{1-a/r}
\bigl(|f(x-y)|^p|g(y)|^a\bigr)^{1/r}.
\]
Apply Hölder's inequality with exponents
\[
\frac{pr}{r-p},
\qquad
\frac{ar}{r-a},
\qquad
r,
\]
using the convention that a quotient with zero denominator is $\infty$.
Their reciprocal exponents add to
\[
\left(\frac1p-\frac1r\right)
+
\left(\frac1a-\frac1r\right)
+
\frac1r
=1.
\]
Thus
\[
|f*g(x)|
\le
\|f\|_p^{1-p/r}
\|g\|_a^{1-a/r}
\left(
\int_{\mathbb R}|f(x-y)|^p|g(y)|^a\,dy
\right)^{1/r}.
\]
Raise to the $r$th power and integrate in $x$.
Tonelli's theorem gives
\[
\begin{aligned}
\|f*g\|_r^r
&\le
\|f\|_p^{r-p}
\|g\|_a^{r-a}
\int_{\mathbb R}\int_{\mathbb R}
|f(x-y)|^p|g(y)|^a\,dy\,dx\\
&=
\|f\|_p^{r-p}
\|g\|_a^{r-a}
\left(\int_{\mathbb R}|f(t)|^p\,dt\right)
\left(\int_{\mathbb R}|g(y)|^a\,dy\right)\\
&=
\|f\|_p^r\|g\|_a^r.
\end{aligned}
\]
Taking $r$th roots proves the finite-$r$ case.

Now suppose $r=\infty$.
Then
\[
\frac1p+\frac1a=1.
\]
For every $x$, Hölder's inequality directly gives
\[
\begin{aligned}
|f*g(x)|
&\le\int_{\mathbb R}|f(x-y)||g(y)|\,dy\\
&\le\|f(x-\cdot)\|_p\|g\|_a\\
&=\|f\|_p\|g\|_a.
\end{aligned}
\]
Taking the essential supremum over $x$ proves the endpoint case.
:::

<1>2. There is one finite constant $A_\phi$ such that
\[
\|\phi\|_{L^a}\le A_\phi
\qquad
\text{for every }1\le a\le\infty.
\]
::: {.proof}
Let
\[
M=\|\phi\|_{L^\infty},
\qquad
L=m(\operatorname{supp}\phi)<\infty.
\]
For $1\le a<\infty$,
\[
\|\phi\|_a^a
=\int_{\operatorname{supp}\phi}|\phi|^a
\le M^aL,
\]
so
\[
\|\phi\|_a\le ML^{1/a}\le M\max\{1,L\}.
\]
For $a=\infty$,
\[
\|\phi\|_\infty=M\le M\max\{1,L\}.
\]
Hence one may take
\[
A_\phi=M\max\{1,L\}.
\]
:::

<1>3. If $1\le p\le q\le\infty$, then
\[
\|f*\phi\|_{L^q}\le A_\phi\|f\|_{L^p}.
\]
::: {.proof}
Define $a\in[1,\infty]$ by
\[
\frac1a=1+\frac1q-\frac1p.
\]
Because $p\le q$,
\[
0\le\frac1a\le1,
\]
so such an $a$ exists in $[1,\infty]$.
The exponent identity is exactly
\[
1+\frac1q=\frac1p+\frac1a.
\]
Applying <1>1 with $g=\phi$ and then <1>2 gives
\[
\|f*\phi\|_q
\le\|f\|_p\|\phi\|_a
\le A_\phi\|f\|_p.
\]
The constant $A_\phi$ depends only on the fixed function $\phi$, not on $p,q$, or $f$.
This proves part (a).
:::

<1>4. For every pair $1\le q<p\le\infty$, there are a compactly supported continuous $\phi$ and an $f\in L^p$ such that
\[
f*\phi\notin L^q.
\]
::: {.proof}
First suppose $p<\infty$.
Choose a number $\alpha$ satisfying
\[
\frac1p<\alpha<\frac1q.
\]
Choose a continuous function $\phi$ such that
\[
0\le\phi\le1,
\qquad
\phi=1\text{ on }[0,1],
\qquad
\operatorname{supp}\phi\subseteq[-1,2].
\]
Define
\[
f(y)=
\begin{cases}
y^{-\alpha},&y\ge10,\\
0,&y<10.
\end{cases}
\]
Since $\alpha p>1$,
\[
f\in L^p(\mathbb R).
\]
For every $x>100$,
\[
\begin{aligned}
(f*\phi)(x)
&=\int_{\mathbb R}f(x-y)\phi(y)\,dy\\
&\ge\int_0^1f(x-y)\,dy\\
&=\int_{x-1}^x t^{-\alpha}\,dt\\
&\ge x^{-\alpha}.
\end{aligned}
\]
But $\alpha q<1$, so
\[
\int_{100}^{\infty}x^{-\alpha q}\,dx=\infty.
\]
Therefore $f*\phi\notin L^q$.

If $p=\infty$ and $q<\infty$, take the same $\phi$ and simply let
\[
f\equiv1.
\]
Then $f\in L^\infty$ and
\[
(f*\phi)(x)=\int_{\mathbb R}\phi(y)\,dy=:c>0
\]
for every $x$.
Thus $f*\phi$ is a nonzero constant and hence does not belong to $L^q(\mathbb R)$.
This proves that no analogous general estimate can hold for $p>q$.
:::
:::
