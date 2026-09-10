---
schema: qual/card@1
id: E-CVDAJ
kind: problem
title: Consequences of an abstract degree theory on spheres
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Suppose that to every map $h: S^n \to S^n$ we have assigned an integer, denoted by $\deg h$ and called the degree of $h$, such that:

(i) Homotopic maps have the same degree.

(ii) $\deg(h \circ k) = (\deg h) \cdot (\deg k)$.

(iii) The identity map has degree 1, any constant map has degree 0, and the reflection map $\rho(x_1, \ldots, x_{n+1}) = (x_1, \ldots, x_n, -x_{n+1})$ has degree $-1$.

[One can construct such a function, using the tools of algebraic topology. Intuitively, $\deg h$ measures how many times $h$ wraps $S^n$ about itself; the sign tells you whether $h$ preserves orientation or not.] Prove the following:

(a) There is no retraction $r: B^{n+1} \to S^n$.

(b) If $h: S^n \to S^n$ has degree different from $(-1)^{n+1}$, then $h$ has a fixed point.
[Hint: Show that if $h$ has no fixed point, then $h$ is homotopic to the antipodal map $a(x) = -x$.]

(c) If $h: S^n \to S^n$ has degree different from 1, then $h$ maps some point $x$ to its antipode $-x$.

(d) If $S^n$ has a nonvanishing tangent vector field $v$, then $n$ is odd.
[Hint: If $v$ exists, show the identity map is homotopic to the antipodal map.]
:::

::: {.solution}
First note that the antipodal map \(a(x)=-x\) is the composite of \(n+1\) coordinate reflections, each conjugate to the given reflection \(\rho\). Hence
\[
\deg a=(-1)^{n+1}.
\]

(a) If \(r:B^{n+1}\to S^n\) were a retraction and \(i:S^n\hookrightarrow B^{n+1}\) the inclusion, then \(r\circ i=\operatorname{id}_{S^n}\). But \(i\) is nullhomotopic since the ball is contractible, so \(r\circ i\) is nullhomotopic. Thus
\[
1=\deg(\operatorname{id})=\deg(r\circ i)=0,
\]
a contradiction.

(b) Suppose \(h\) has no fixed point. Define
\[
H(x,t)=\frac{(1-t)h(x)-tx}{\|(1-t)h(x)-tx\|}.
\]
The denominator never vanishes: if it did, then \(h(x)=\frac{t}{1-t}x\); since both are unit vectors, this forces \(h(x)=x\), contrary to hypothesis. Thus \(H\) is a homotopy from \(h\) to the antipodal map. Hence a fixed-point-free map must satisfy
\[
\deg h=\deg a=(-1)^{n+1}.
\]
The contrapositive proves (b).

(c) Suppose \(h(x)\ne -x\) for every \(x\). Then
\[
K(x,t)=\frac{(1-t)h(x)+tx}{\|(1-t)h(x)+tx\|}
\]
is well defined: a zero would force \(h(x)=-x\). Thus \(h\simeq\operatorname{id}\), so \(\deg h=1\). Contrapositively, if \(\deg h\ne1\), some \(x\) satisfies \(h(x)=-x\).

(d) If \(v\) is a nonvanishing tangent vector field, normalize it so \(\|v(x)\|=1\). Since \(v(x)\perp x\),
\[
F(x,t)=\cos(\pi t)x+\sin(\pi t)v(x)
\]
lies on \(S^n\) for all \(t\), and is a homotopy from the identity to the antipodal map. Therefore
\[
1=(-1)^{n+1}.
\]
Hence \(n+1\) is even, so \(n\) is odd.
:::
