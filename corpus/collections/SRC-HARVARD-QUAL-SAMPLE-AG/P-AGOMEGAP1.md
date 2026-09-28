---
schema: qual/card@1
id: P-AGOMEGAP1
kind: problem
title: $H^0(\PP^1, \Omega^1)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Differentials
  - Cohomology
  - Projective Line
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the Harvard sample qualifying-exam algebraic-geometry PDF; this is Poonen's question asking for H^0(P^1, Omega^1).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Calculate $H^0(\PP^1, \Omega^1)$.
:::

::: {.solution}
\[
\boxed{H^0(\mathbb P^1_k,\Omega^1_{\mathbb P^1/k})=0.}
\]

<1>1. On the standard affine chart
\[
U_0=\{X_0\ne0\}\cong\mathbb A^1_k
\]
with coordinate
\[
x=X_1/X_0,
\]
every regular differential has the form
\[
\omega=f(x)\,dx
\]
for a polynomial $f(x)\in k[x]$.
::: {.proof}
On $U_0\cong\operatorname{Spec}k[x]$,
\[
\Omega^1_{k[x]/k}\cong k[x]\,dx.
\]
Thus a section of $\Omega^1$ over $U_0$ is uniquely $f(x)dx$ with $f\in k[x]$.
:::

<1>2. On the other standard chart
\[
U_1=\{X_1\ne0\}
\]
put
\[
u=X_0/X_1=1/x.
\]
Then
\[
dx=-u^{-2}\,du.
\]
::: {.proof}
Since $x=u^{-1}$ on $U_0\cap U_1$,
\[
dx=d(u^{-1})=-u^{-2}du.
\]
:::

<1>3. If
\[
f(x)=a_0+a_1x+\cdots+a_dx^d
\]
is nonzero, then $f(x)dx$ has a pole at $u=0$, the point at infinity.
::: {.proof}
Using <1>2,
\[
\begin{aligned}
f(x)dx
&=f(u^{-1})(-u^{-2}du)\\
&=-\left(a_0u^{-2}+a_1u^{-3}+\cdots+a_du^{-d-2}\right)du.
\end{aligned}
\]
If $f\ne0$, at least one coefficient is nonzero, and every displayed exponent of $u$ is negative.  Hence the coefficient of $du$ is not regular at $u=0$.
:::

<1>4. Therefore a global regular differential on $\mathbb P^1$ must vanish identically.
::: {.proof}
A global differential restricts on $U_0$ to some $f(x)dx$ by <1>1.  It must also be regular on $U_1$, in particular at $u=0$.  Step <1>3 shows this is possible only if
\[
f=0.
\]
Thus the global section is zero.
:::

<1>5. Equivalently,
\[
\Omega^1_{\mathbb P^1/k}\cong\mathcal O_{\mathbb P^1}(-2),
\]
so the calculation is the identity
\[
H^0(\mathbb P^1,\mathcal O(-2))=0.
\]
::: {.proof}
On the overlap, <1>2 says the local generators transform by
\[
dx=-u^{-2}du.
\]
This is the transition function of $\mathcal O(-2)$ up to the invertible constant $-1$.  Hence the two line bundles are isomorphic.  A negative-degree line bundle on $\mathbb P^1$ has no nonzero global section, agreeing with <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>4 proves the required calculation.
:::
:::
