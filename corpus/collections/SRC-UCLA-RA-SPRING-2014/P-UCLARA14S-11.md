---
schema: qual/card@1
id: P-UCLARA14S-11
kind: problem
title: Improper integral of x to a power over one plus x squared
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
For each $p\in(-1,1)$, compute
$$
\int_0^\infty \frac{x^p}{x^2+1}\,dx.
$$
:::

::: {.solution}

::: pf

::: pf-step

The improper integral
$$
I_p
\coloneqq
\int_0^\infty\frac{x^p}{1+x^2}\,dx
$$
converges for every $p\in(-1,1)$.


::: pf-proof

As $x\downarrow0$,
$$
\frac{x^p}{1+x^2}
\sim
x^p,
$$
and
$$
\int_0^1x^p\,dx<\infty
$$
exactly when $p>-1$.

As $x\to\infty$,
$$
\frac{x^p}{1+x^2}
\sim
x^{p-2},
$$
and
$$
\int_1^\infty x^{p-2}\,dx<\infty
$$
exactly when $p<1$. Thus the given range of $p$ guarantees convergence at both endpoints.

:::

:::

::: {.pf-step #s1-2}

With
$$
a
\coloneqq
\frac{p+1}{2},
$$
one has $a\in(0,1)$ and
$$
I_p
=
\frac12
\int_0^\infty
\frac{t^{a-1}}{1+t}\,dt.
$$


::: pf-proof

Make the substitution
$$
t=x^2,
\qquad
dx=\frac12t^{-1/2}\,dt.
$$
Then
$$
x^p\,dx
=
t^{p/2}\frac12t^{-1/2}\,dt
=
\frac12
t^{(p-1)/2}\,dt
=
\frac12
t^{a-1}\,dt.
$$
The denominator becomes $1+t$, giving the formula.

:::

:::

::: {.pf-step #s1-3}

For $0<a<1$,
$$
\int_0^\infty
\frac{t^{a-1}}{1+t}\,dt
=
\Gamma(a)\Gamma(1-a)
=
\frac{\pi}{\sin(\pi a)}.
$$


::: pf-proof

The substitution
$$
s=\frac{t}{1+t},
\qquad
t=\frac{s}{1-s},
\qquad
dt=\frac{ds}{(1-s)^2},
$$
gives
$$
\int_0^\infty
\frac{t^{a-1}}{1+t}\,dt
=
\int_0^1
s^{a-1}(1-s)^{-a}\,ds
=
B(a,1-a).
$$
The beta--gamma identity gives
$$
B(a,1-a)
=
\Gamma(a)\Gamma(1-a),
$$
and Euler's reflection formula gives
$$
\Gamma(a)\Gamma(1-a)
=
\frac{\pi}{\sin(\pi a)}.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\int_0^\infty
\frac{x^p}{1+x^2}\,dx
=
\frac{\pi}
{2\cos(\pi p/2)}
}.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
I_p
=
\frac\pi{2\sin(\pi a)}.
$$
Since
$$
a=\frac{p+1}{2},
$$
one has
$$
\sin(\pi a)
=
\sin\left(\frac\pi2+\frac{\pi p}{2}\right)
=
\cos\left(\frac{\pi p}{2}\right).
$$
Substitution gives the boxed value.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the value of the convergent improper integral for every $p\in(-1,1)$.

:::

:::

:::
