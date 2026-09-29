---
schema: qual/card@1
id: P-AZOFF-F08
kind: problem
title: Partial fraction expansion of $\pi^2/\sin^2\pi z$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Established locally uniform convergence of the bilateral series away
    from the integers, identified the double-pole principal part 1/(z-k)^2
    for both functions, proved period one and uniform decay on a fundamental
    vertical strip, and applied Liouville to their entire difference.
---

::: {.problem}
Take $\begin{array} { r } { f ( z ) = \frac { \pi ^ { 2 } } { \sin ^ { 2 } \pi z } } \end{array}$ and $\begin{array} { r } { g ( z ) = \sum _ { n = - \infty } ^ { \infty } \frac { 1 } { ( z - n ) ^ { 2 } } } \end{array}$

a) Show these functions have the same singularities in $\mathbb { C }$

b) Show that $f$ and $g$ have the same singular parts at each of their singularities.

c) Note that $f$ and $g$ each have period one and that both approach zero uniformly on $0 \leq x \leq 1$ as $| y | \to \infty$ .

d) Conclude that $f = g$
:::

::: {.solution}
Write
$$
f(z)=\frac{\pi^2}{\sin^2(\pi z)}
$$
and
$$
g(z)=\sum_{n\in\ZZ}\frac1{(z-n)^2}.
$$

::: pf

::: {.pf-step #s1}

The series defining $g$ converges locally uniformly on
$\CC\sm\ZZ$ and therefore defines a holomorphic function there.

::: pf-proof

Let $K\subseteq\CC\sm\ZZ$ be compact and put
$$
M=\max_{z\in K}\abs{z}.
$$
For every integer $n$ with $\abs{n}>2M$ and every $z\in K$,
$$
\abs{z-n}
\geq
\abs{n}-\abs{z}
>
\frac{\abs{n}}{2}.
$$
Hence
$$
\abs{\frac1{(z-n)^2}}
\leq
\frac4{n^2}.
$$
The numerical series
$$
\sum_{n\in\ZZ\sm\{0\}}\frac1{n^2}
$$
converges. The Weierstrass M-test therefore gives uniform convergence of the
tail on $K$. Adding the finitely many remaining holomorphic terms proves
local uniform convergence on $\CC\sm\ZZ$, hence holomorphy there.

:::

:::

::: {.pf-step #s2}

The singularities of $g$ are exactly the integers, and each integer
$k$ is a double pole with singular part
$$
\frac1{(z-k)^2}.
$$

::: pf-proof

Fix $k\in\ZZ$ and choose $0<r<1/2$. On the disk
$$
\abs{z-k}<r,
$$
write
$$
g(z)
=
\frac1{(z-k)^2}
+
\sum_{n\in\ZZ\sm\{k\}}
\frac1{(z-n)^2}.
$$
The second series converges locally uniformly on this disk by the argument
of step [](#s1){.pf-ref} and is holomorphic there, since none of its denominators
vanishes. Thus the first term is the complete principal part at $k$, so $k$
is a double pole. Step [](#s1){.pf-ref} shows there are no other singularities.

:::

:::

::: {.pf-step #s3}

The singularities of $f$ are exactly the integers, and at every
$k\in\ZZ$ its singular part is also
$$
\frac1{(z-k)^2}.
$$

::: pf-proof

The zeros of $\sin(\pi z)$ are exactly the integers and are simple, so
$f$ has no singularities away from $\ZZ$ and has a double pole at each
integer.

For $z=k+w$,
$$
\sin(\pi z)
=
(-1)^k\sin(\pi w)
=
(-1)^k\pi w
\left(
1-\frac{\pi^2w^2}{6}+O(w^4)
\right).
$$
Therefore
$$
\begin{aligned}
f(k+w)
&=
\frac1{w^2}
\left(
1-\frac{\pi^2w^2}{6}+O(w^4)
\right)^{-2}\\
&=
\frac1{w^2}
+\frac{\pi^2}{3}
+O(w^2).
\end{aligned}
$$
Thus the entire principal part is $w^{-2}=(z-k)^{-2}$.

:::

:::

::: {.pf-step #s4}

Parts (a) and (b) hold: $f$ and $g$ have the same singularities and
the same singular parts at each one.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that both functions have exactly the integers as
double poles and that the principal part at every integer $k$ is
$(z-k)^{-2}$.

:::

:::

::: {.pf-step #s5}

Both $f$ and $g$ have period $1$.

::: pf-proof

Since
$$
\sin(\pi(z+1))=-\sin(\pi z),
$$
one has $f(z+1)=f(z)$.

For $g$, absolute convergence away from the integers allows reindexing:
$$
\begin{aligned}
g(z+1)
&=
\sum_{n\in\ZZ}\frac1{(z+1-n)^2}\\
&=
\sum_{m\in\ZZ}\frac1{(z-m)^2}\\
&=
g(z),
\end{aligned}
$$
where $m=n-1$.

:::

:::

::: {.pf-step #s6}

Uniformly for $0\leq x\leq1$,
$$
f(x+iy)\longrightarrow0
$$
as $\abs{y}\to\infty$.

::: pf-proof

For real $x,y$,
$$
\abs{\sin(\pi(x+iy))}^2
=
\sin^2(\pi x)+\sinh^2(\pi y).
$$
Hence
$$
\abs{f(x+iy)}
\leq
\frac{\pi^2}{\sinh^2(\pi y)}.
$$
The right-hand side is independent of $x$ and tends to $0$ as
$\abs{y}\to\infty$.

:::

:::

::: {.pf-step #s7}

Uniformly for $0\leq x\leq1$,
$$
g(x+iy)\longrightarrow0
$$
as $\abs{y}\to\infty$.

::: pf-proof

For $z=x+iy$ with $0\leq x\leq1$ and $y\neq0$,
$$
\abs{g(z)}
\leq
\sum_{n\in\ZZ}
\frac1{(x-n)^2+y^2}.
$$
The terms $n=0,1$ contribute at most $2/y^2$. For $n\geq2$,
$\abs{x-n}\geq n-1$, and for $n\leq-1$,
$\abs{x-n}\geq\abs{n}$. Therefore
$$
\abs{g(x+iy)}
\leq
\frac2{y^2}
+
2\sum_{m=1}^{\infty}\frac1{m^2+y^2}.
$$
Since $t\mapsto(t^2+y^2)^{-1}$ is decreasing on $[0,\infty)$,
$$
\sum_{m=1}^{\infty}\frac1{m^2+y^2}
\leq
\int_0^{\infty}\frac{dt}{t^2+y^2}
=
\frac{\pi}{2\abs{y}}.
$$
Consequently
$$
\abs{g(x+iy)}
\leq
\frac2{y^2}
+
\frac{\pi}{\abs{y}},
$$
uniformly in $x\in[0,1]$. This bound tends to $0$ as
$\abs{y}\to\infty$.

:::

:::

::: {.pf-step #s8}

The difference
$$
h=f-g
$$
extends to an entire, $1$-periodic function.

::: pf-proof

By step [](#s4){.pf-ref}, at each integer the principal parts of $f$ and $g$ cancel.
Thus every singularity of $h$ at an integer is removable. After filling in
those removable singularities, $h$ is entire. Step [](#s5){.pf-ref} gives
$h(z+1)=h(z)$.

:::

:::

::: {.pf-step #s9}

The entire function $h$ is bounded on $\CC$.

::: pf-proof

By steps [](#s6){.pf-ref} and [](#s7){.pf-ref},
$$
h(x+iy)\longrightarrow0
$$
uniformly for $0\leq x\leq1$ as $\abs{y}\to\infty$. Choose $Y>0$ so
that
$$
\abs{h(x+iy)}\leq1
$$
whenever $0\leq x\leq1$ and $\abs{y}\geq Y$.

On the compact rectangle
$$
0\leq x\leq1,
\qquad
\abs{y}\leq Y,
$$
the entire function $h$ is bounded. Hence $h$ is bounded on the whole
vertical strip $0\leq\operatorname{Re}z\leq1$. By $1$-periodicity, every
point of $\CC$ translates by an integer into this strip, so the same bound
holds on all of $\CC$.

:::

:::

::: {.pf-step #s10}

One has
$$
\boxed{
\frac{\pi^2}{\sin^2(\pi z)}
=
\sum_{n\in\ZZ}\frac1{(z-n)^2}.
}
$$

::: pf-proof

By step [](#s9){.pf-ref} and Liouville's theorem, $h$ is constant. Steps [](#s6){.pf-ref} and [](#s7){.pf-ref}
show that $h(z)\to0$ as $\abs{\operatorname{Im}z}\to\infty$ in a
fundamental strip. A constant function with this limit is zero. Therefore
$h\equiv0$, which is the displayed identity.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref} and [](#s10){.pf-ref} establish parts (a)--(d).

:::

:::

:::
