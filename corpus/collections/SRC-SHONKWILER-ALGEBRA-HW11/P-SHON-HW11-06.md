---
schema: qual/card@1
id: P-SHON-HW11-06
kind: problem
title: Which angles can always be $n$-sected?
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained Algebra HW 11 solution packet.
---

::: {.problem}
For which positive integers $n$ is it possible, using straightedge and compass, to divide every given angle into $n$ equal parts?
Prove your assertion.
:::

::: {.solution}

::: pf

::: pf-step

Every angle can be bisected with straightedge and compass.


::: pf-proof

This is the classical angle-bisector construction.

:::

:::

::: {.pf-step #s1-2}

Therefore every angle can be divided into
$$
\boxed{2^r}
$$
equal parts for every integer $r\ge0$.


::: pf-proof

Apply the angle-bisector construction repeatedly $r$ times. The case $r=0$ is $n=1$, which requires no subdivision.

:::

:::

::: pf-step

Then $n$ has an odd prime divisor $p$.


::: pf-proof

Write the prime factorization of $n$. If every prime divisor were $2$, then $n$ would be a power of $2$.

:::

:::

::: {.pf-step #s1-4}

If every angle could be divided into $n$ equal parts, then every angle could be divided into $p$ equal parts.


::: pf-proof

Write
$$
n=pm.
$$
An $n$-section of an angle produces $n$ adjacent equal subangles. Taking the union of any $m$ consecutive subangles gives one subangle of size
$$
\frac{m}{n}
=
\frac1p
$$
of the original angle. Hence a universal $n$-section construction would yield a universal $p$-section construction.

:::

:::

::: pf-step

The angle
$$
\boxed{\frac{2\pi}{3}}
$$
is constructible.


::: pf-proof

A regular triangle is constructible, so its central angle $2\pi/3$ is constructible.

:::

:::

::: {.pf-step #s1-6}

If every angle were $p$-sectable, then
$$
\boxed{\frac{2\pi}{3p}}
$$
would be constructible.


::: pf-proof

Apply the hypothetical $p$-section construction to the constructible angle $2\pi/3$.

:::

:::

::: {.pf-step #s1-7}

Constructibility of the angle
$$
\frac{2\pi}{3p}
$$
would imply constructibility of a regular $3p$-gon.


::: pf-proof

From a constructible central angle $2\pi/(3p)$, one can mark successive points on a circle by repeatedly rotating that angle, producing the vertices of a regular $3p$-gon.

:::

:::

::: {.pf-step #s1-8}

But a regular $3p$-gon is not constructible when $p$ is an odd prime that is not a Fermat prime.


::: pf-proof

By Gauss--Wantzel, every odd prime divisor of a constructible polygon size must be a Fermat prime. The number $3p$ has the odd prime divisor $p$, which by hypothesis is not Fermat.

:::

:::

::: {.pf-step #s1-9}

Hence no non-Fermat odd prime $p$ universally $p$-sects angles.


::: pf-proof

Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} give a contradiction.

:::

:::

::: pf-step

A regular $p$-gon is constructible.


::: pf-proof

This is exactly one of the Gauss--Wantzel allowed odd prime factors.

:::

:::

::: {.pf-step #s1-11}

Therefore the angle
$$
\boxed{\frac{2\pi}{p}}
$$
is constructible.


::: pf-proof

It is the central angle between adjacent vertices of the constructible regular $p$-gon.

:::

:::

::: {.pf-step #s1-12}

If every angle were $p$-sectable, then
$$
\boxed{\frac{2\pi}{p^2}}
$$
would be constructible.


::: pf-proof

Apply the hypothetical $p$-section construction to the angle from step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Constructibility of
$$
\frac{2\pi}{p^2}
$$
would imply constructibility of a regular $p^2$-gon.


::: pf-proof

As in step [](#s1-7){.pf-ref}, successively laying off the constructible central angle produces the regular polygon.

:::

:::

::: {.pf-step #s1-14}

But a regular $p^2$-gon is not constructible.


::: pf-proof

Gauss--Wantzel permits each odd Fermat prime factor only to the first power. The integer
$$
p^2
$$
contains the odd Fermat prime $p$ with exponent $2$, so it is not of the required form.

:::

:::

::: {.pf-step #s1-15}

Hence no Fermat odd prime $p$ universally $p$-sects angles.


::: pf-proof

Steps [](#s1-12){.pf-ref} through [](#s1-14){.pf-ref} give a contradiction.

:::

:::

::: {.pf-step #s1-16}

Therefore no odd prime $p$ has the property that every angle can be divided into $p$ equal parts.


::: pf-proof

Every odd prime is either a Fermat prime or not. Apply steps [](#s1-9){.pf-ref} and [](#s1-15){.pf-ref}.

:::

:::

::: pf-step

Consequently, if every angle can be divided into $n$ equal parts, then $n$ has no odd prime divisor.


::: pf-proof

If $n$ had an odd prime divisor $p$, step [](#s1-4){.pf-ref} would imply universal $p$-section, contradicting step [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-18}

Hence
$$
\boxed{n=2^r}
$$
for some integer $r\ge0$.


::: pf-proof

A positive integer with no odd prime divisor is a power of $2$.

:::

:::

::: {.pf-step #s1-19}

Combining necessity and sufficiency,
$$
\boxed{
\text{every angle is constructibly }n\text{-sectable}
\iff
n=2^r\text{ for some }r\ge0.}
$$


::: pf-proof

Sufficiency is step [](#s1-2){.pf-ref}, and necessity is step [](#s1-18){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-19){.pf-ref} is the required classification.

:::

:::

:::
