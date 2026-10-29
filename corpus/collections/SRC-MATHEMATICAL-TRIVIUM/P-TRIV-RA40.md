---
schema: qual/card@1
id: P-TRIV-RA40
kind: problem
title: Volumes of high-dimensional balls and concentration near the boundary
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 40, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
" 20-dimensional watermelon"

(a) Find the surface area of the unit n-dimensional sphere $S ^ { n }$ Indication: Use the notion of Gamma function $\Gamma ( a ) \equiv \int _ { 0 } ^ { \infty } e ^ { - x } x ^ { a - 1 } d x$

(b) Find the volume $V _ { n }$ of the unit n-dimensional ball $B ^ { n }$

(c) Denote by $V _ { n , a }$ the volume of a layer of depth a adjacent to the surface of $B ^ { n } , 0 < a < 1$ . Compute the ratio $\frac { V _ { n , a } } { V _ { n } }$ and investigate the limit $n \to \infty$

(d) Assuming the watermelon rind has a thickness 0.1 of its radius, find what fraction of the total volume of the 20-dimensional watermelon would be occupied by its rind.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The one-dimensional Gaussian integral satisfies
$$
\int_{-\infty}^{\infty}e^{-x^2}\,dx
=
\sqrt\pi.
$$


::: pf-proof

This is the standard Gaussian integral.

:::

:::

::: pf-step

Therefore, in $\RR^{n+1}$,
$$
\int_{\RR^{n+1}}
e^{-\|x\|^2}
\,dx
=
\pi^{(n+1)/2}.
$$


::: pf-proof

By Fubini's theorem, the integral factors into $n+1$ copies of the
one-dimensional integral from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Let
$$
A_n=\operatorname{Area}(S^n)
$$
for the unit $n$-sphere in $\RR^{n+1}$. Polar coordinates give
$$
\pi^{(n+1)/2}
=
A_n
\int_0^\infty
e^{-r^2}r^n
\,dr.
$$


::: pf-proof

In radial coordinates on $\RR^{n+1}$, the volume element is
$$
r^n\,dr\,d\omega,
$$
where $d\omega$ is surface measure on $S^n$. Integrating over the angular
variables gives the factor $A_n$.

:::

:::

::: {.pf-step #s1-4}

The radial integral equals
$$
\int_0^\infty
e^{-r^2}r^n
\,dr
=
\frac12
\Gamma\left(\frac{n+1}{2}\right).
$$


::: pf-proof

Set
$$
u=r^2.
$$
Then
$$
dr=\frac{du}{2\sqrt u},
$$
and
$$
r^n\,dr
=
\frac12u^{(n-1)/2}\,du.
$$
Thus the integral becomes
$$
\frac12
\int_0^\infty
e^{-u}u^{(n-1)/2}
\,du,
$$
which is the displayed Gamma value.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\operatorname{Area}(S^n)
=
\frac{2\pi^{(n+1)/2}}
{\Gamma((n+1)/2)}.
}
$$


::: pf-proof

Solve the identity in step [](#s1-3){.pf-ref} for $A_n$ using step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Part (a) follows.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Let $V_n(R)$ be the volume of the radius-$R$ ball in $\RR^n$.
Then
$$
V_n(R)=V_n(1)R^n.
$$


::: pf-proof

The dilation $x\mapsto Rx$ multiplies every $n$-dimensional volume by $R^n$.

:::

:::

::: {.pf-step #s1-8}

Differentiating step [](#s1-7){.pf-ref} with respect to $R$ at $R=1$ gives
$$
\operatorname{Area}(S^{n-1})
=
nV_n(1).
$$


::: pf-proof

The derivative of ball volume with respect to radius is the surface area of
the boundary sphere. Differentiating
$$
V_n(1)R^n
$$
at $R=1$ gives $nV_n(1)$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
V_n
\coloneqq
V_n(1)
=
\frac1n
\operatorname{Area}(S^{n-1}).
$$


::: pf-proof

Rearrange step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Using step [](#s1-5){.pf-ref} with $n-1$ in place of $n$,
$$
\boxed{
V_n
=
\frac{\pi^{n/2}}
{\Gamma(n/2+1)}.
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives
$$
\operatorname{Area}(S^{n-1})
=
\frac{2\pi^{n/2}}
{\Gamma(n/2)}.
$$
Hence by step [](#s1-9){.pf-ref},
$$
V_n
=
\frac{2\pi^{n/2}}
{n\Gamma(n/2)}.
$$
Using
$$
\Gamma\left(\frac n2+1\right)
=
\frac n2\Gamma\left(\frac n2\right)
$$
gives the formula.

:::

:::

::: {.pf-step #s1-11}

Part (b) follows.


::: pf-proof

This is step [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

The inner ball obtained by removing a boundary layer of depth $a$ has
radius
$$
1-a.
$$


::: pf-proof

The original ball has radius $1$, so removing an outer layer of radial
thickness $a$ leaves the concentric ball of radius $1-a$.

:::

:::

::: pf-step

Its volume is
$$
V_n(1-a)^n.
$$


::: pf-proof

Apply the scaling relation from step [](#s1-7){.pf-ref} with $R=1-a$.

:::

:::

::: {.pf-step #s1-14}

Therefore the shell volume is
$$
V_{n,a}
=
V_n
\left[
1-(1-a)^n
\right].
$$


::: pf-proof

Subtract the inner-ball volume from the total volume:
$$
V_{n,a}
=
V_n-V_n(1-a)^n.
$$

:::

:::

::: {.pf-step #s1-15}

Hence
$$
\boxed{
\frac{V_{n,a}}{V_n}
=
1-(1-a)^n.
}
$$


::: pf-proof

Divide step [](#s1-14){.pf-ref} by $V_n>0$.

:::

:::

::: {.pf-step #s1-16}

For fixed $0<a<1$,
$$
\boxed{
\lim_{n\to\infty}
\frac{V_{n,a}}{V_n}
=1.
}
$$


::: pf-proof

Since
$$
0<1-a<1,
$$
one has
$$
(1-a)^n\to0.
$$
Apply step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-17}

Part (c) follows.


::: pf-proof

Steps [](#s1-15){.pf-ref} through [](#s1-16){.pf-ref} give the ratio and its high-dimensional limit.

:::

:::

::: {.pf-step #s1-18}

For a $20$-dimensional ball with rind thickness $0.1$ of its radius,
$$
\frac{V_{20,0.1}}{V_{20}}
=
1-0.9^{20}.
$$


::: pf-proof

Substitute
$$
n=20,
\qquad
a=0.1
$$
into step [](#s1-15){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

Numerically,
$$
0.9^{20}
=
0.12157665459\ldots,
$$
so
$$
\boxed{
\frac{V_{20,0.1}}{V_{20}}
=
0.87842334541\ldots
\approx87.84\%.
}
$$


::: pf-proof

Evaluate the expression in step [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Part (d) follows.


::: pf-proof

This is step [](#s1-19){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref}, [](#s1-11){.pf-ref}, and [](#s1-17){.pf-ref}, and [](#s1-20){.pf-ref} establish parts (a)--(d).

:::

:::

:::
