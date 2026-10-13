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
<1>1. Every angle can be bisected with straightedge and compass.

::: {.proof}
This is the classical angle-bisector construction.
:::

<1>2. Therefore every angle can be divided into
\[
\boxed{2^r}
\]
equal parts for every integer \(r\ge0\).

::: {.proof}
Apply the angle-bisector construction repeatedly \(r\) times. The case \(r=0\) is \(n=1\), which requires no subdivision.
:::

To prove the converse, suppose \(n\) is not a power of \(2\).

<1>3. Then \(n\) has an odd prime divisor \(p\).

::: {.proof}
Write the prime factorization of \(n\). If every prime divisor were \(2\), then \(n\) would be a power of \(2\).
:::

<1>4. If every angle could be divided into \(n\) equal parts, then every angle could be divided into \(p\) equal parts.

::: {.proof}
Write
\[
n=pm.
\]
An \(n\)-section of an angle produces \(n\) adjacent equal subangles. Taking the union of any \(m\) consecutive subangles gives one subangle of size
\[
\frac{m}{n}
=
\frac1p
\]
of the original angle. Hence a universal \(n\)-section construction would yield a universal \(p\)-section construction.
:::

Thus it suffices to show that no odd prime \(p\) has the property that every angle is \(p\)-sectable.

Recall the Gauss--Wantzel theorem: a regular \(N\)-gon is constructible if and only if
\[
N=2^s q_1\cdots q_t,
\]
where the \(q_i\) are distinct Fermat primes.

## Case 1: \(p\) is not a Fermat prime

<1>5. The angle
\[
\boxed{\frac{2\pi}{3}}
\]
is constructible.

::: {.proof}
A regular triangle is constructible, so its central angle \(2\pi/3\) is constructible.
:::

<1>6. If every angle were \(p\)-sectable, then
\[
\boxed{\frac{2\pi}{3p}}
\]
would be constructible.

::: {.proof}
Apply the hypothetical \(p\)-section construction to the constructible angle \(2\pi/3\).
:::

<1>7. Constructibility of the angle
\[
\frac{2\pi}{3p}
\]
would imply constructibility of a regular \(3p\)-gon.

::: {.proof}
From a constructible central angle \(2\pi/(3p)\), one can mark successive points on a circle by repeatedly rotating that angle, producing the vertices of a regular \(3p\)-gon.
:::

<1>8. But a regular \(3p\)-gon is not constructible when \(p\) is an odd prime that is not a Fermat prime.

::: {.proof}
By Gauss--Wantzel, every odd prime divisor of a constructible polygon size must be a Fermat prime. The number \(3p\) has the odd prime divisor \(p\), which by hypothesis is not Fermat.
:::

<1>9. Hence no non-Fermat odd prime \(p\) universally \(p\)-sects angles.

::: {.proof}
Steps <1>6--<1>8 give a contradiction.
:::

## Case 2: \(p\) is a Fermat prime

<1>10. A regular \(p\)-gon is constructible.

::: {.proof}
This is exactly one of the Gauss--Wantzel allowed odd prime factors.
:::

<1>11. Therefore the angle
\[
\boxed{\frac{2\pi}{p}}
\]
is constructible.

::: {.proof}
It is the central angle between adjacent vertices of the constructible regular \(p\)-gon.
:::

<1>12. If every angle were \(p\)-sectable, then
\[
\boxed{\frac{2\pi}{p^2}}
\]
would be constructible.

::: {.proof}
Apply the hypothetical \(p\)-section construction to the angle from step <1>11.
:::

<1>13. Constructibility of
\[
\frac{2\pi}{p^2}
\]
would imply constructibility of a regular \(p^2\)-gon.

::: {.proof}
As in step <1>7, successively laying off the constructible central angle produces the regular polygon.
:::

<1>14. But a regular \(p^2\)-gon is not constructible.

::: {.proof}
Gauss--Wantzel permits each odd Fermat prime factor only to the first power. The integer
\[
p^2
\]
contains the odd Fermat prime \(p\) with exponent \(2\), so it is not of the required form.
:::

<1>15. Hence no Fermat odd prime \(p\) universally \(p\)-sects angles.

::: {.proof}
Steps <1>12--<1>14 give a contradiction.
:::

<1>16. Therefore no odd prime \(p\) has the property that every angle can be divided into \(p\) equal parts.

::: {.proof}
Every odd prime is either a Fermat prime or not. Apply steps <1>9 and <1>15.
:::

<1>17. Consequently, if every angle can be divided into \(n\) equal parts, then \(n\) has no odd prime divisor.

::: {.proof}
If \(n\) had an odd prime divisor \(p\), step <1>4 would imply universal \(p\)-section, contradicting step <1>16.
:::

<1>18. Hence
\[
\boxed{n=2^r}
\]
for some integer \(r\ge0\).

::: {.proof}
A positive integer with no odd prime divisor is a power of \(2\).
:::

<1>19. Combining necessity and sufficiency,
\[
\boxed{
\text{every angle is constructibly }n\text{-sectable}
\iff
n=2^r\text{ for some }r\ge0.}
\]

::: {.proof}
Sufficiency is step <1>2, and necessity is step <1>18.
:::

<1>20. Q.E.D.

::: {.proof}
Step <1>19 is the required classification.
:::
:::
