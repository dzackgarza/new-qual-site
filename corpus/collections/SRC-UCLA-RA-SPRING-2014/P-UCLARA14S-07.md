---
schema: qual/card@1
id: P-UCLARA14S-07
kind: problem
title: Entire functions with linear logarithmic growth and finitely many zeros
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Characterize all entire functions $f$ such that $\abs{f(z)}>0$ for all sufficiently large $\abs{z}$ and
$$
\limsup_{\abs{z}\to\infty}\frac{\abs{\log\abs{f(z)}}}{\abs{z}}<\infty.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Such a function $f$ has only finitely many zeros in $\CC$.


::: pf-proof

By hypothesis, there is $R_0>0$ such that
$$
f(z)\ne0
\qquad
(\abs{z}\ge R_0).
$$
Thus every zero lies in the compact disk $\abs{z}\le R_0$. Since $f$ is not identically zero and zeros of a nonzero entire function are isolated, there can be only finitely many zeros in that compact disk.

:::

:::

::: {.pf-step #s1-2}

There is a polynomial $p$ and an entire function $h$ such that
$$
f(z)=p(z)e^{h(z)},
$$
where $p$ has exactly the zeros of $f$, with the same multiplicities.


::: pf-proof

Let $a_1,\dots,a_N$ be the zeros of $f$, listed with multiplicity, and set
$$
p(z)
\coloneqq
\prod_{j=1}^N(z-a_j),
$$
with $p\equiv1$ if $N=0$. Then
$$
g(z)
\coloneqq
\frac{f(z)}{p(z)}
$$
extends to an entire function with no zeros.

Since $\CC$ is simply connected and $g$ is nonvanishing, the logarithmic derivative
$$
\frac{g'}g
$$
has an entire primitive $H$. Then
$$
\frac{d}{dz}\left(g e^{-H}\right)=0,
$$
so
$$
g(z)=Ce^{H(z)}
$$
for some nonzero constant $C$. Choosing a logarithm of $C$ and absorbing it into $H$ gives
$$
g=e^h
$$
for an entire function $h$.

:::

:::

::: {.pf-step #s1-3}

There are constants $A>0$ and $R_1>0$ such that
$$
\abs{\operatorname{Re}h(z)}
\le
A\abs{z}
\qquad
(\abs{z}\ge R_1).
$$


::: pf-proof

The limsup hypothesis gives constants $C>0$ and $R_1$ such that
$$
\abs{\log\abs{f(z)}}\le C\abs{z}
\qquad
(\abs{z}\ge R_1).
$$
Increase $R_1$ if necessary so that $p(z)\ne0$ there. Since
$$
f=pe^h,
$$
one has
$$
\log\abs{f(z)}
=
\log\abs{p(z)}
+
\operatorname{Re}h(z).
$$
If $d=\deg p$, then for sufficiently large $\abs{z}$,
$$
\abs{\log\abs{p(z)}}\le C_p+d\log\abs{z}
\le C_p'\abs{z}
$$
for suitable constants $C_p,C_p'$. Hence
$$
\abs{\operatorname{Re}h(z)}
\le
\abs{\log\abs{f(z)}}+\abs{\log\abs{p(z)}}
\le
(C+C_p')\abs{z}.
$$
Take $A=C+C_p'$.

:::

:::

::: {.pf-step #s1-4}

Write
$$
h(z)=\sum_{n=0}^\infty c_n z^n.
$$
For every integer $k\ge1$ and every sufficiently large $R$,
$$
\pi c_kR^k
=
\int_0^{2\pi}
\operatorname{Re}h(Re^{i\theta})e^{-ik\theta}\,d\theta.
$$


::: pf-proof

For fixed $R$, the power series for $h$ converges uniformly on the circle $\abs{z}=R$. Thus
$$
\operatorname{Re}h(Re^{i\theta})
=
\frac12
\left(
\sum_{n=0}^\infty c_nR^ne^{in\theta}
+
\sum_{n=0}^\infty \overline{c_n}R^ne^{-in\theta}
\right).
$$
Multiply by $e^{-ik\theta}$ and integrate term-by-term over $[0,2\pi]$. Orthogonality of the exponentials kills every term except the $n=k$ term in the first sum, yielding
$$
\int_0^{2\pi}
\operatorname{Re}h(Re^{i\theta})e^{-ik\theta}\,d\theta
=
\pi c_kR^k.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
c_k=0
\qquad
(k\ge2).
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, for sufficiently large $R$,
$$
\begin{aligned}
\pi\abs{c_k}R^k
&\le
\int_0^{2\pi}
\abs{\operatorname{Re}h(Re^{i\theta})}\,d\theta\\
&\le
2\pi AR.
\end{aligned}
$$
Therefore
$$
\abs{c_k}
\le
2A R^{1-k}.
$$
If $k\ge2$, letting $R\to\infty$ gives $c_k=0$.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
h(z)=az+b
$$
for some $a,b\in\CC$, and every function satisfying the hypotheses has the form
$$
\boxed{
f(z)=p(z)e^{az+b}
}
$$
with $p$ a polynomial.


::: pf-proof

Step [](#s1-5){.pf-ref} shows that the Taylor series of $h$ has no terms of degree at least $2$. Thus
$$
h(z)=c_1z+c_0.
$$
Rename $a=c_1$ and $b=c_0$, and substitute into the factorization from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Conversely, every function
$$
f(z)=p(z)e^{az+b},
$$
with $p$ a nonzero polynomial and $a,b\in\CC$, satisfies the two hypotheses.


::: pf-proof

Such a function is entire. Its zeros are exactly the finitely many zeros of $p$, so
$$
\abs{f(z)}>0
$$
for all sufficiently large $\abs{z}$.

For large $\abs{z}$ beyond all zeros of $p$,
$$
\log\abs{f(z)}
=
\log\abs{p(z)}
+
\operatorname{Re}(az+b).
$$
Hence
$$
\abs{\log\abs{f(z)}}\le C_1\log\abs{z}+\abs{a}\abs{z}+C_2
$$
for suitable constants $C_1,C_2$. Dividing by $\abs{z}$ shows that
$$
\limsup_{\abs{z}\to\infty}
\frac{\abs{\log\abs{f(z)}}}{\abs{z}}
<
\infty.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} prove necessity, and step [](#s1-7){.pf-ref} proves sufficiency.

:::

:::

:::
