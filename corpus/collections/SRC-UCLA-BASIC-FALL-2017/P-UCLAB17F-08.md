---
schema: qual/card@1
id: P-UCLAB17F-08
kind: problem
title: Functions with limits at every point
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $a<b$ and let $f:[a,b]\to\RR$ be such that
$$
L(x)=\lim_{y\to x}f(y)
$$
exists for every $x\in[a,b]$, using one-sided limits at the endpoints.

(a) Prove that $L$ is continuous.

(b) Prove that $\{x:f(x)\ne L(x)\}$ is countable.

(c) Prove that $f$ is Riemann integrable.
:::

::: {.solution}

All limits below are taken relative to $[a,b]$, so at the endpoints they are one-sided.

::: pf

::: {.pf-step #s1-1}

Fix $x_0\in[a,b]$ and $\varepsilon>0$.
There exists $\delta>0$ such that
$$
0<|y-x_0|<\delta
$$
implies
$$
|f(y)-L(x_0)|<\frac{\varepsilon}{2}.
$$


::: pf-proof

This is exactly the definition of
$$
L(x_0)=\lim_{y\to x_0}f(y).
$$

:::

:::

::: {.pf-step #s1-2}

If
$$
0<|x-x_0|<\frac{\delta}{2},
$$
then
$$
|L(x)-L(x_0)|
\le
\frac{\varepsilon}{2}.
$$


::: pf-proof

Fix such an $x$.
Choose a sequence
$$
y_k\to x
$$
with
$$
y_k\ne x
$$
and, for all sufficiently large $k$,
$$
|y_k-x|<\frac12\min\{|x-x_0|,\delta-|x-x_0|\}.
$$
Then for large $k$,
$$
y_k\ne x_0
$$
and
$$
|y_k-x_0|<\delta.
$$
By step [](#s1-1){.pf-ref},
$$
|f(y_k)-L(x_0)|
<
\frac{\varepsilon}{2}.
$$
Letting $k\to\infty$ and using
$$
f(y_k)\to L(x)
$$
gives
$$
|L(x)-L(x_0)|
\le
\frac{\varepsilon}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

The function $L$ is continuous on $[a,b]$.


::: pf-proof

At $x=x_0$,
$$
|L(x)-L(x_0)|=0.
$$
For
$$
0<|x-x_0|<\delta/2,
$$
step [](#s1-2){.pf-ref} gives
$$
|L(x)-L(x_0)|
\le
\frac{\varepsilon}{2}
<
\varepsilon.
$$
Thus $L$ is continuous at the arbitrary point $x_0$.
This proves part (a).

:::

:::

::: {.pf-step #s1-4}

Define
$$
h(x)=f(x)-L(x).
$$
Then for every $x_0\in[a,b]$,
$$
\lim_{\substack{x\to x_0\\x\ne x_0}}h(x)=0.
$$


::: pf-proof

As $x\to x_0$ with $x\ne x_0$,
$$
f(x)\to L(x_0)
$$
by definition of $L(x_0)$.
Also
$$
L(x)\to L(x_0)
$$
by continuity from step [](#s1-3){.pf-ref}.
Therefore
$$
h(x)
=
f(x)-L(x)
\to
0.
$$

:::

:::

::: {.pf-step #s1-5}

For each positive integer $m$, define
$$
E_m
=
\left\{
x\in[a,b]:
|h(x)|\ge\frac1m
\right\}.
$$
Then $E_m$ is finite.


::: pf-proof

Suppose $E_m$ were infinite.
Since $[a,b]$ is compact, the Bolzano--Weierstrass theorem gives an accumulation point
$$
x_0\in[a,b].
$$
Thus there is a sequence of distinct points
$$
x_k\in E_m\setminus\{x_0\}
$$
with
$$
x_k\to x_0.
$$
By step [](#s1-4){.pf-ref},
$$
h(x_k)\to0.
$$
But
$$
|h(x_k)|
\ge
\frac1m
$$
for every $k$, a contradiction.
Thus $E_m$ is finite.

:::

:::

::: {.pf-step #s1-6}

The set
$$
D=\{x\in[a,b]:f(x)\ne L(x)\}
$$
is countable.


::: pf-proof

Since
$$
f(x)\ne L(x)
$$
if and only if
$$
h(x)\ne0,
$$
one has
$$
D
=
\bigcup_{m=1}^{\infty}E_m.
$$
Indeed, if $h(x)\ne0$, choose $m$ so large that
$$
1/m\le |h(x)|.
$$
Each $E_m$ is finite by step [](#s1-5){.pf-ref}.
A countable union of finite sets is countable.
This proves part (b).

:::

:::

::: {.pf-step #s1-7}

The function $f$ is bounded on $[a,b]$.


::: pf-proof

For each $x\in[a,b]$, the existence of the finite limit
$$
L(x)
$$
gives a neighborhood $U_x$ in which
$$
|f(y)|
\le
|L(x)|+1
$$
for all
$$
y\in U_x\setminus\{x\}.
$$
Including the single value $f(x)$ gives a finite bound for $f$ on $U_x$.

The neighborhoods $U_x$ cover the compact interval $[a,b]$.
Choose a finite subcover.
Taking the maximum of the finitely many local bounds gives a global bound
$$
|f|\le M
$$
on $[a,b]$.

:::

:::

::: pf-step

The function $h=f-L$ is bounded.


::: pf-proof

The function $f$ is bounded by step [](#s1-7){.pf-ref}.
The function $L$ is continuous on the compact interval $[a,b]$ by step [](#s1-3){.pf-ref}, hence bounded.
Therefore their difference $h$ is bounded.
Choose
$$
|h(x)|\le M
$$
for all $x$.

:::

:::

::: {.pf-step #s1-9}

The function $h$ is Riemann integrable and
$$
\int_a^b h(x)\,dx=0.
$$


::: pf-proof

Fix $\varepsilon>0$.
Choose $m$ so large that
$$
\frac{2(b-a)}{m}
<
\frac{\varepsilon}{2}.
$$
By step [](#s1-5){.pf-ref}, the set
$$
E_m
$$
is finite.
Cover its finitely many points by finitely many intervals whose total length is less than
$$
\frac{\varepsilon}{4M}
$$
if $M>0$.
If $M=0$, then $h\equiv0$ and there is nothing to prove.

Choose a partition $P$ containing all endpoints of these covering intervals.
On every partition subinterval not contained in the exceptional cover, no point belongs to $E_m$, so
$$
|h(x)|<\frac1m.
$$
Hence the oscillation of $h$ there is less than
$$
\frac2m.
$$
On the exceptional intervals, the oscillation is at most
$$
2M.
$$
Therefore
$$
\begin{aligned}
U(h,P)-L(h,P)
&<
\frac2m(b-a)
+
2M\cdot\frac{\varepsilon}{4M}\\
&<
\frac{\varepsilon}{2}
+
\frac{\varepsilon}{2}\\
&=
\varepsilon.
\end{aligned}
$$
Thus $h$ is Riemann integrable.

Moreover, outside the countable set $D$ from step [](#s1-6){.pf-ref},
$$
h=0.
$$
The same partition estimate, applied to upper and lower sums of $h$, shows that its integral has absolute value at most arbitrarily small $\varepsilon$.
Equivalently, one may use the above construction with the nonexceptional contribution bounded by $(b-a)/m$ and the exceptional contribution made arbitrarily small.
Hence
$$
\int_a^b h=0.
$$

:::

:::

::: {.pf-step #s1-10}

The function $f$ is Riemann integrable.


::: pf-proof

By step [](#s1-3){.pf-ref}, $L$ is continuous on $[a,b]$, hence Riemann integrable.
By step [](#s1-9){.pf-ref}, $h=f-L$ is Riemann integrable.
Therefore
$$
f=L+h
$$
is Riemann integrable.
This proves part (c).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), step [](#s1-6){.pf-ref} proves part (b), and step [](#s1-10){.pf-ref} proves part (c).

:::

:::

:::
