---
schema: qual/card@1
id: P-HXUGN
kind: problem
title: Euclidean domains and PIDs
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
What is the relation between Euclidean domains and PIDs?
:::

::: solution
Every Euclidean domain is a PID. Indeed, let $R$ be Euclidean with Euclidean function $\delta$, and let $0\ne I\triangleleft R$. Choose $0\ne a\in I$ with $\delta(a)$ minimal. For any $b\in I$, Euclidean division gives
\[
b=qa+r,
\]
with either $r=0$ or $\delta(r)<\delta(a)$. Since $r=b-qa\in I$, minimality forces $r=0$. Hence every $b\in I$ lies in $(a)$, so $I=(a)$.

Thus
\[
\text{Euclidean domain}\Longrightarrow\text{PID}\Longrightarrow\text{UFD}.
\]
Neither implication reverses in general.

For UFD $\not\Rightarrow$ PID, take $k[x,y]$. It is a UFD by Gauss's theorem, but the ideal $(x,y)$ is not principal: if $(x,y)=(d)$, then $d$ divides both $x$ and $y$, so $d$ is a unit, contradicting $(x,y)\ne k[x,y]$.

For PID $\not\Rightarrow$ Euclidean, take
\[
R=\mathbb Z\!\left[\frac{1+\sqrt{-19}}2\right].
\]
Its discriminant is $-19$, so Minkowski's bound is $(2/\pi)\sqrt{19}<3$. Thus every ideal class contains an integral ideal of norm $1$ or $2$. The polynomial $x^2-x+5$ is irreducible modulo $2$, so $2$ is inert and there is no ideal of norm $2$. Hence every ideal class is trivial, so $R$ is a PID.

It is not Euclidean for any Euclidean function. If $R$ were Euclidean, choose a nonzero nonunit $b$ of minimal Euclidean value. Division by $b$ would show that every residue class modulo $(b)$ is represented by $0$ or a unit. The norm is
\[
N(a+c\theta)=a^2+ac+5c^2,
\qquad \theta=\frac{1+\sqrt{-19}}2,
\]
and the only units are $\pm1$, so $|R/(b)|=|N(b)|$ would be at most $3$ and greater than $1$, hence $2$ or $3$. But
\[
a^2+ac+5c^2=\left(a+\frac c2\right)^2+\frac{19}{4}c^2
\]
never equals $2$ or $3$ for integers $a,c$. This contradiction shows that $R$ is not Euclidean.
:::
