---
schema: qual/card@1
id: P-UCLAB07S-06
kind: problem
title: Uniqueness for a Lipschitz integral equation
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Consider
$$
y(t)=y_0+\int_0^t f(s,y(s))\,ds,
$$
where $f$ is continuous on $[0,T]\times\RR$ and Lipschitz in its second variable with constant $K$.
Assume the Picard iterates
$$
y^n(t)=y_0+\int_0^t f(s,y^{n-1}(s))\,ds,
\qquad y^0(t)\equiv y_0,
$$
converge uniformly to a solution $y$.
Show that if $Y$ is another solution satisfying $\abs{Y(t)-y_0}\le C$ on $[0,T]$, then $Y(t)=y(t)$ for all $t\in[0,T]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The solution $y$ is bounded on $[0,T]$.


::: pf-proof

The Picard iterates
$$
y^n
$$
converge uniformly to $y$ by hypothesis.
In particular, choose $N$ such that
$$
\norm{y-y^N}_\infty<1.
$$
The function $y^N$ is continuous on the compact interval $[0,T]$, hence bounded:
$$
\abs{y^N(t)}\le M_N.
$$
Therefore
$$
\abs{y(t)}
\le
\abs{y(t)-y^N(t)}+\abs{y^N(t)}
<
1+M_N
$$
for every $t\in[0,T]$.

:::

:::

::: {.pf-step #s1-2}

There exists $M>0$ such that
$$
\abs{Y(t)-y(t)}\le M
$$
for every $t\in[0,T]$.


::: pf-proof

By hypothesis,
$$
\abs{Y(t)-y_0}\le C.
$$
By step [](#s1-1){.pf-ref}, $y$ is bounded; hence
$$
\abs{y(t)-y_0}
$$
is bounded by some constant $C'$.
Thus
$$
\abs{Y(t)-y(t)}
\le
\abs{Y(t)-y_0}
+
\abs{y(t)-y_0}
\le
C+C'.
$$
Take
$$
M=C+C'.
$$

:::

:::

::: {.pf-step #s1-3}

For every $t\in[0,T]$,
$$
\abs{Y(t)-y(t)}
\le
K\int_0^t\abs{Y(s)-y(s)}\,ds.
$$


::: pf-proof

Both $Y$ and $y$ satisfy the integral equation:
$$
Y(t)
=
y_0
+
\int_0^t f(s,Y(s))\,ds,
$$
$$
y(t)
=
y_0
+
\int_0^t f(s,y(s))\,ds.
$$
Subtracting gives
$$
Y(t)-y(t)
=
\int_0^t
\bigl(
f(s,Y(s))-f(s,y(s))
\bigr)\,ds.
$$
Taking absolute values and using the Lipschitz estimate in the second variable,
$$
\begin{aligned}
\abs{Y(t)-y(t)}
&\le
\int_0^t
\abs{f(s,Y(s))-f(s,y(s))}
\,ds\\
&\le
K\int_0^t
\abs{Y(s)-y(s)}
\,ds.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For every integer $n\ge0$ and every $t\in[0,T]$,
$$
\boxed{
\abs{Y(t)-y(t)}
\le
M\frac{(Kt)^n}{n!}
}.
$$


::: pf-proof

Proceed by induction on $n$.

For $n=0$, the claim is
$$
\abs{Y(t)-y(t)}\le M,
$$
which is step [](#s1-2){.pf-ref}.

Assume the estimate holds for some $n$.
Then step [](#s1-3){.pf-ref} gives
$$
\begin{aligned}
\abs{Y(t)-y(t)}
&\le
K\int_0^t
\abs{Y(s)-y(s)}
\,ds\\
&\le
K\int_0^t
M\frac{(Ks)^n}{n!}
\,ds\\
&=
M\frac{K^{n+1}}{n!}
\frac{t^{n+1}}{n+1}\\
&=
M\frac{(Kt)^{n+1}}{(n+1)!}.
\end{aligned}
$$
Thus the induction closes.

:::

:::

::: {.pf-step #s1-5}

For fixed $t\in[0,T]$,
$$
\frac{(Kt)^n}{n!}
\longrightarrow0.
$$


::: pf-proof

The exponential series
$$
\sum_{n=0}^{\infty}\frac{(Kt)^n}{n!}
$$
converges.
Hence its terms tend to $0$.

:::

:::

::: {.pf-step #s1-6}

For every $t\in[0,T]$,
$$
Y(t)=y(t).
$$


::: pf-proof

Fix $t$.
By step [](#s1-4){.pf-ref},
$$
0
\le
\abs{Y(t)-y(t)}
\le
M\frac{(Kt)^n}{n!}
$$
for every $n$.
By step [](#s1-5){.pf-ref}, the right-hand side tends to $0$ as $n\to\infty$.
Therefore
$$
\abs{Y(t)-y(t)}=0.
$$
Thus
$$
Y(t)=y(t).
$$
Since $t$ was arbitrary, the equality holds on all of $[0,T]$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves uniqueness of the solution within the stated bounded class.

:::

:::

:::
