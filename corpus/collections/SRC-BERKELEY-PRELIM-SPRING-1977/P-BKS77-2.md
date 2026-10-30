---
schema: qual/card@1
id: P-BKS77-2
kind: problem
title: Existence of one-sided limits everywhere implies Riemann integrability
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $f$ be a real-valued function such that
$$
\lim_{x\to c}f(x)
$$
exists for every $c\in[a,b]$.
Show that $f$ is Riemann integrable on $[a,b]$.
:::

::: {.solution}
For $c\in[a,b]$, write
$$
L_c\coloneqq\lim_{x\to c}f(x),
$$
where at an endpoint the limit is taken relative to $[a,b]$.

::: pf

::: {.pf-step #boundedness}
The function $f$ is bounded on $[a,b]$.

::: pf-proof
For every $c\in[a,b]$, choose $\delta_c>0$ such that
$$
0<\abs{x-c}<\delta_c
\quad\Longrightarrow\quad
\abs{f(x)-L_c}<1.
$$
Thus on
$$
U_c\coloneqq(c-\delta_c,c+\delta_c)\cap[a,b]
$$
one has
$$
\abs{f(x)}
\leq
\max\{\abs{f(c)},\abs{L_c}+1\}.
$$
The sets $U_c$ form an open cover of the compact interval $[a,b]$. Choose a finite subcover
$$
U_{c_1},\ldots,U_{c_m}.
$$
Taking the maximum of $1$ and the finitely many bounds associated to $c_1,\ldots,c_m$ gives a constant $M\geq1$ such that
$$
\abs{f(x)}\leq M
$$
for all $x\in[a,b]$.
:::

:::

::: {.pf-step #finite-cover}
Let $\eta>0$. If $a<b$, there is a finite open cover
$$
U_1,\ldots,U_m
$$
of $[a,b]$, with distinguished points $c_i\in U_i$, such that
$$
x,y\in U_i\setminus\{c_i\}
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<
\frac{\eta}{2(b-a)}.
$$

::: pf-proof
For each $c\in[a,b]$, choose $\delta_c>0$ so that
$$
0<\abs{x-c}<\delta_c
\quad\Longrightarrow\quad
\abs{f(x)-L_c}<
\frac{\eta}{4(b-a)}.
$$
Let
$$
U_c\coloneqq
\left(c-\frac{\delta_c}{2},c+\frac{\delta_c}{2}\right)\cap[a,b].
$$
If $x,y\in U_c\setminus\{c\}$, then
$$
\abs{f(x)-f(y)}
\leq
\abs{f(x)-L_c}+\abs{f(y)-L_c}
<
\frac{\eta}{2(b-a)}.
$$
Compactness supplies a finite subcover; rename its members $U_1,\ldots,U_m$ and their centers $c_1,\ldots,c_m$.
:::

:::

::: {.pf-step #partition}
There is a partition $P$ of $[a,b]$ for which the total length of all subintervals of $P$ containing at least one of the points $c_1,\ldots,c_m$ is less than
$$
\frac{\eta}{4M}.
$$

::: pf-proof
Let $\lambda>0$ be a Lebesgue number for the finite cover from [](#finite-cover){.pf-ref}. Choose a partition $P$ whose mesh $h$ satisfies
$$
h<\lambda
\qquad\text{and}\qquad
h<\frac{\eta}{8Mm}.
$$
Each point $c_i$ belongs to at most two closed subintervals of $P$, so there are at most $2m$ subintervals containing one of the $c_i$. Their total length is therefore at most
$$
2mh
<
\frac{\eta}{4M}.
$$
:::

:::

::: {.pf-step #darboux-gap}
For the partition $P$ from [](#partition){.pf-ref},
$$
U(f,P)-L(f,P)<\eta.
$$

::: pf-proof
Call a subinterval of $P$ bad if it contains one of the distinguished points $c_i$, and good otherwise.

On any bad interval, [](#boundedness){.pf-ref} gives oscillation at most $2M$. By [](#partition){.pf-ref}, the total contribution of all bad intervals to
$$
U(f,P)-L(f,P)
$$
is less than
$$
2M\cdot\frac{\eta}{4M}
=
\frac{\eta}{2}.
$$

Now let $J$ be a good interval. Its length is less than the Lebesgue number $\lambda$, so $J\subseteq U_i$ for some $i$. Since $J$ contains no distinguished point, in particular $c_i\notin J$. [](#finite-cover){.pf-ref} therefore shows that the oscillation of $f$ on $J$ is less than
$$
\frac{\eta}{2(b-a)}.
$$
The total length of all good intervals is at most $b-a$, so their total contribution is less than $\eta/2$. Adding the two contributions gives the claim.
:::

:::

::: pf-step
The function $f$ is Riemann integrable on $[a,b]$.

::: pf-proof
If $a=b$, the assertion is immediate. Assume $a<b$. [](#boundedness){.pf-ref} gives boundedness, and [](#darboux-gap){.pf-ref} shows that for every $\eta>0$ there is a partition $P$ with
$$
U(f,P)-L(f,P)<\eta.
$$
By the Darboux criterion, $f$ is Riemann integrable.
:::

:::

:::

:::
