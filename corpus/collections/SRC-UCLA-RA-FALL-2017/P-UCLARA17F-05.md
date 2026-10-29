---
schema: qual/card@1
id: P-UCLARA17F-05
kind: problem
title: Bounded functions invariant under $x\mapsto x+1$ and $x\mapsto 2x$ are constant
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 5. Suppose $f:\RR\to\RR$ is a bounded and measurable function satisfying
$$
f(x+1)=f(x)\qquad\text{and}\qquad f(2x)=f(x)
$$
for almost every $x\in\RR$. Show that there exists a constant $c\in\RR$ such that $f(x)=c$ for almost every $x\in\RR$.
:::

::: {.solution}

Since $f$ is bounded and measurable, its restriction to $[0,1]$ lies in
$$
L^2([0,1]).
$$

For each $n\in\ZZ$, define the Fourier coefficient
$$
\boxed{
\widehat f(n)
=
\int_0^1
f(x)e^{-2\pi i n x}\,dx}.
$$

::: pf

::: pf-step

For every $n\in\ZZ$,
$$
\widehat f(n)
=
\int_0^1
f(2x)e^{-2\pi i n x}\,dx.
$$


::: pf-proof

The relation
$$
f(2x)=f(x)
$$
holds for almost every $x$, so replacing $f(x)$ by $f(2x)$ does not change the integral.

:::

:::

::: {.pf-step #s1-2}

Split the integral at $1/2$:
$$
\widehat f(n)
=
\int_0^{1/2}
f(2x)e^{-2\pi i n x}\,dx
+
\int_{1/2}^{1}
f(2x)e^{-2\pi i n x}\,dx.
$$


::: pf-proof

This is additivity of the Lebesgue integral.

:::

:::

::: {.pf-step #s1-3}

In the first integral, the substitution
$$
u=2x
$$
gives
$$
\boxed{
\int_0^{1/2}
f(2x)e^{-2\pi i n x}\,dx
=
\frac12
\int_0^1
f(u)e^{-\pi i n u}\,du}.
$$


::: pf-proof

One has
$$
dx=\frac12\,du
$$
and
$$
e^{-2\pi i n x}
=
e^{-\pi i n u}.
$$

:::

:::

::: {.pf-step #s1-4}

In the second integral, set
$$
u=2x-1.
$$
Then
$$
\boxed{
\int_{1/2}^{1}
f(2x)e^{-2\pi i n x}\,dx
=
\frac{(-1)^n}{2}
\int_0^1
f(u)e^{-\pi i n u}\,du}.
$$


::: pf-proof

Here
$$
2x=u+1,
\qquad
dx=\frac12\,du.
$$
By the almost-everywhere periodicity,
$$
f(u+1)=f(u)
$$
for almost every $u$. Also,
$$
e^{-2\pi i n x}
=
e^{-\pi i n(u+1)}
=
(-1)^n e^{-\pi i n u}.
$$
Substitute these identities.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\widehat f(n)
=
\frac{1+(-1)^n}{2}
\int_0^1
f(u)e^{-\pi i n u}\,du}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

If $n$ is odd, then
$$
\boxed{
\widehat f(n)=0}.
$$


::: pf-proof

For odd $n$,
$$
1+(-1)^n=0.
$$
Apply step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

If $n=2m$ is even, then
$$
\boxed{
\widehat f(2m)=\widehat f(m)}.
$$


::: pf-proof

For $n=2m$,
$$
\frac{1+(-1)^n}{2}=1,
$$
and
$$
e^{-\pi i n u}
=
e^{-2\pi i m u}.
$$
Thus step [](#s1-5){.pf-ref} becomes
$$
\widehat f(2m)
=
\int_0^1
f(u)e^{-2\pi i m u}\,du
=
\widehat f(m).
$$

:::

:::

::: pf-step

Write
$$
\boxed{
n=2^k q}
$$
where $k\ge0$ and $q$ is odd.


::: pf-proof

Factor out the highest power of $2$ dividing the nonzero integer $n$.

:::

:::

::: {.pf-step #s1-9}

Iterating step [](#s1-7){.pf-ref} gives
$$
\boxed{
\widehat f(n)=\widehat f(q)}.
$$


::: pf-proof

Apply
$$
\widehat f(2m)=\widehat f(m)
$$
successively $k$ times.

:::

:::

::: {.pf-step #s1-10}

Since $q$ is odd,
$$
\boxed{
\widehat f(q)=0}.
$$


::: pf-proof

Apply step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence
$$
\boxed{
\widehat f(n)=0}
$$
for every
$$
n\ne0.
$$


::: pf-proof

Combine steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

The function
$$
g=f-c
$$
has all Fourier coefficients equal to $0$.


::: pf-proof

For $n\ne0$, use step [](#s1-11){.pf-ref}. For $n=0$,
$$
\widehat g(0)
=
\widehat f(0)-c
=
0.
$$

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
g=0}
$$
almost everywhere on $[0,1]$.


::: pf-proof

The trigonometric system
$$
\{e^{2\pi i n x}:n\in\ZZ\}
$$
is complete in $L^2([0,1])$. A function orthogonal to every basis vector must be $0$ in $L^2$, hence almost everywhere.

:::

:::

::: pf-step

Thus
$$
\boxed{
f(x)=c}
$$
for almost every $x\in[0,1]$.


::: pf-proof

This is step [](#s1-13){.pf-ref} with $g=f-c$.

:::

:::

::: {.pf-step #s1-15}

The same equality holds for almost every $x\in\RR$.


::: pf-proof

For each integer $m$, the relation
$$
f(x+m)=f(x)
$$
holds almost everywhere by iterating the given period-$1$ relation. Translating the null exceptional set from $[0,1]$ to each interval $[m,m+1]$ preserves nullity. Taking the countable union over $m\in\ZZ$ still gives a null set. Hence
$$
f=c
$$
almost everywhere on $\RR$.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} is the required conclusion.

:::

:::

:::
