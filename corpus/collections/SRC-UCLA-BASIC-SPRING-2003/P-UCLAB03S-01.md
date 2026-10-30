---
schema: qual/card@1
id: P-UCLAB03S-01
kind: problem
title: Extending a uniformly continuous function to the closed interval
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Examination, May 2003 PDF.
---

::: {.problem}
(a) Suppose $f:(0,1)\to\RR$ is continuous.
Define what it means for $f$ to be uniformly continuous.

(b) Show that if $f:(0,1)\to\RR$ is uniformly continuous, then there exists a continuous function $F:[0,1]\to\RR$ such that
$$
F(x)=f(x)
$$
for every $x\in(0,1)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f:(0,1)\to\RR$ is uniformly continuous if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $x,y\in(0,1)$,
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\varepsilon.
$$


::: pf-proof

This is the definition of uniform continuity. The essential point is that the same $\delta$ works simultaneously for all $x,y$ in the domain.

:::

:::

::: {.pf-step #s1-2}

If $f$ is uniformly continuous, then the sequence
$$
\left(f\left(\frac1n\right)\right)_{n\ge2}
$$
is Cauchy in $\RR$.


::: pf-proof

Let $\varepsilon>0$. By uniform continuity, choose $\delta>0$ such that
$$
\abs{x-y}<\delta
\Longrightarrow
\abs{f(x)-f(y)}<\varepsilon.
$$
Choose $N$ with $1/N<\delta/2$. If $m,n\ge N$, then
$$
\abs{\frac1m-\frac1n}
\le\frac1m+\frac1n
\le\frac2N
<\delta.
$$
Hence
$$
\abs{f\left(\frac1m\right)-f\left(\frac1n\right)}<\varepsilon.
$$
Thus the sequence is Cauchy.

:::

:::

::: {.pf-step #s1-3}

There exists $L_0\in\RR$ such that
$$
\lim_{x\to0^+}f(x)=L_0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref} and completeness of $\RR$, there is
$$
L_0=\lim_{n\to\infty}f(1/n).
$$
Let $\varepsilon>0$. Choose $\delta>0$ from uniform continuity for $\varepsilon/2$. Then choose $N$ such that
$$
\frac1N<\frac\delta2
\qquad\text{and}\qquad
\abs{f\left(\frac1N\right)-L_0}<\frac\varepsilon2.
$$
If $0<x<\delta/2$, then
$$
\abs{x-\frac1N}
<
\delta,
$$
so
$$
\abs{f(x)-f\left(\frac1N\right)}<\frac\varepsilon2.
$$
Therefore
$$
\abs{f(x)-L_0}
\le
\abs{f(x)-f\left(\frac1N\right)}
+
\abs{f\left(\frac1N\right)-L_0}
<\varepsilon.
$$
Thus $f(x)\to L_0$ as $x\to0^+$.

:::

:::

::: {.pf-step #s1-4}

There exists $L_1\in\RR$ such that
$$
\lim_{x\to1^-}f(x)=L_1.
$$


::: pf-proof

Apply the argument of steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} to the sequence
$$
1-\frac1n.
$$
Uniform continuity makes
$$
\left(f\left(1-\frac1n\right)\right)_{n\ge2}
$$
Cauchy, hence convergent in $\RR$; comparison with a sufficiently late term then proves that $f(x)$ approaches the same limit as $x\to1^-$.

:::

:::

::: {.pf-step #s1-5}

Define
$$
\boxed{
F(x)=
\begin{cases}
L_0,&x=0,\\
f(x),&0<x<1,\\
L_1,&x=1.
\end{cases}}
$$
Then $F:[0,1]\to\RR$ is continuous.


::: pf-proof

On $(0,1)$, the function $F$ agrees with the continuous function $f$. At $0$, step [](#s1-3){.pf-ref} gives
$$
\lim_{x\to0^+}F(x)
=
\lim_{x\to0^+}f(x)
=L_0
=F(0),
$$
so $F$ is continuous at $0$. Likewise, step [](#s1-4){.pf-ref} gives
$$
\lim_{x\to1^-}F(x)
=L_1
=F(1),
$$
so $F$ is continuous at $1$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-5){.pf-ref} constructs the continuous extension required in part (b).

:::

:::

:::
