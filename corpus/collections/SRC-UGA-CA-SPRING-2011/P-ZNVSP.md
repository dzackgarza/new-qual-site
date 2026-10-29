---
schema: qual/card@1
id: P-ZNVSP
kind: problem
title: Density of $f(\halfplane)$ for a holomorphic map of the half-plane real precisely
  on $\RR$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Picard
  - Open Mapping Theorem
relations: []
review: draft
---

::: {.problem}
Suppose $f: \HH\union \RR\to \CC$ satisfies the following:

- $f(i) = i$

- $f$ is continuous

- $f$ is analytic on $\HH$

- $f(z) \in \RR \iff z\in \RR$.

Show that $f(\HH)$ is a dense subset of $\HH$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
f(\HH)\subseteq\HH.
$$


::: pf-proof

By hypothesis, $f(z)\notin\RR$ for every $z\in\HH$. Since $\HH$ is
connected and $f$ is continuous, the connected set $f(\HH)$ must lie
entirely in one of the two connected components of $\CC\setminus\RR$.
Because $f(i)=i\in\HH$, that component is the upper half-plane.

:::

:::

::: pf-step

Schwarz reflection extends $f$ to an entire function
$F:\CC\to\CC$ satisfying
$$
F(\bar z)=\overline{F(z)}.
$$


::: pf-proof

For $\Im z<0$, define
$$
F(z)=\overline{f(\bar z)},
$$
and on $\HH\cup\RR$ set $F=f$. The boundary values of $f$ on $\RR$ are
real by hypothesis, so the upper and lower definitions agree
continuously on $\RR$.

At each real point, the Schwarz reflection theorem applies on a small
disk centered at that point because $f$ is holomorphic in the upper
half-disk, continuous on the diameter, and real-valued there. Hence the
reflected function is holomorphic across every real point. It is already
holomorphic off $\RR$, so $F$ is entire on $\CC$.

:::

:::

::: {.pf-step #s1-3}

The extension satisfies
$$
F(\{\Im z<0\})\subseteq\{\Im w<0\}
$$
and $F(\RR)\subseteq\RR$.


::: pf-proof

The second assertion is part of the hypothesis. If $\Im z<0$, then
$\bar z\in\HH$, so step [](#s1-1){.pf-ref} gives $f(\bar z)\in\HH$. Therefore
$$
F(z)=\overline{f(\bar z)}
$$
lies in the lower half-plane.

:::

:::

::: {.pf-step #s1-4}

The entire function $F$ is nonconstant.


::: pf-proof

One has $F(i)=f(i)=i$. On the other hand, for every real $x$,
$F(x)=f(x)\in\RR$. Thus $F(x)\ne i$ for any real $x$, so $F$ cannot be
constant.

:::

:::

::: {.pf-step #s1-5}

If $f(\HH)$ were not dense in $\HH$, then the entire function
$F$ would omit a nonempty open subset of $\CC$.


::: pf-proof

Assume $f(\HH)$ is not dense in $\HH$. Then there exist
$w_0\in\HH$ and $\varepsilon>0$ such that
$$
B(w_0,\varepsilon)\subseteq\HH
$$
and
$$
B(w_0,\varepsilon)\cap f(\HH)=\varnothing.
$$

No point of this disk can be attained by $F$ from the lower half-plane,
because step [](#s1-3){.pf-ref} maps that half-plane into itself. No point can be
attained from the real axis, because $F(\RR)\subseteq\RR$. No point can
be attained from the upper half-plane by the choice of the disk.
Therefore
$$
B(w_0,\varepsilon)\cap F(\CC)=\varnothing.
$$

:::

:::

::: {.pf-step #s1-6}

A nonconstant entire function cannot omit a nonempty open subset
of $\CC$.


::: pf-proof

If an entire function is a nonconstant polynomial, then it is surjective
onto $\CC$: for any $w\in\CC$, the nonconstant polynomial $F-w$ has a
zero by the Fundamental Theorem of Algebra.

If an entire function is not a polynomial, then $\infty$ is an essential
singularity. Casorati--Weierstrass implies that the image of every
punctured neighborhood of $\infty$ is dense in $\CC$. Such a function
therefore cannot omit any nonempty open subset of $\CC$.

Thus in either case a nonconstant entire function cannot omit an open
disk.

:::

:::

::: {.pf-step #s1-7}

The set $f(\HH)$ is dense in $\HH$.


::: pf-proof

If it were not dense, step [](#s1-5){.pf-ref} would force the nonconstant entire
function $F$ from step [](#s1-4){.pf-ref} to omit a nonempty open set, contradicting
step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
