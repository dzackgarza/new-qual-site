---
schema: qual/card@1
id: E-SS1.EX-24
kind: problem
title: "Reversing orientation negates a contour integral"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
24. Let $\gamma$ be a smooth curve in $\mathbb { C }$ parametrized by $z ( t ) : [ a , b ] \to \mathbb { C }$ . Let $\gamma ^ { - }$ denote the curve with the same image as $\gamma$ but with the reverse orientation.
    Prove that for any continuous function $f$ on γ

$$
\int_ {\gamma} f (z) d z = - \int_ {\gamma^ {-}} f (z) d z.
$$
:::

::: solution
If $\gamma$ is parametrized by $z:[a,b]\to\mathbb C$, then the reverse curve is parametrized by
\[
z^-(t)=z(a+b-t),\qquad a\le t\le b.
\]
Therefore $(z^-)'(t)=-z'(a+b-t)$, and
\[
\begin{aligned}
\int_{\gamma^-}f(z)\,dz
&=\int_a^b f(z(a+b-t))\,[-z'(a+b-t)]\,dt\\
&=-\int_a^b f(z(a+b-t))z'(a+b-t)\,dt.
\end{aligned}
\]
With the substitution $u=a+b-t$, the last integral becomes
\[
-\int_a^b f(z(u))z'(u)\,du=-\int_\gamma f(z)\,dz.
\]
Hence
\[
\int_\gamma f(z)\,dz=-\int_{\gamma^-}f(z)\,dz.
\]
:::
