---
schema: qual/card@1
id: E-SS10.EX-1
kind: problem
title: "SS 10.1: A theta-quotient identity for the Weierstrass function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: >-
    Repaired the published erratum: "first two derivatives" should read "first three derivatives".
---

::: {.exercise}
1. Prove that

$$
\frac {(\Theta^ {\prime} (z | \tau)) ^ {2} - \Theta (z | \tau) \Theta^ {\prime \prime} (z | \tau)}{\Theta (z | \tau) ^ {2}} = \wp_ {\tau} (z - 1 / 2 - \tau / 2) + c _ {\tau},
$$

where $c _ { \tau }$ can be expressed in terms of the first three derivatives of $\Theta ( z | \tau )$ , with respect to $z$ , at $z = 1 / 2 + \tau / 2$ . Compare this formula with the result in Exercise 5 in the previous chapter.
:::

::: {.solution}
Let
\[
z_0=\frac12+\frac\tau2,
\qquad
H(z)=\frac{(\Theta'(z|\tau))^2-\Theta(z|\tau)\Theta''(z|\tau)}{\Theta(z|\tau)^2}
=-\left(\frac{\Theta'}{\Theta}\right)'(z).
\]
The theta transformation laws are
\[
\Theta(z+1|\tau)=\Theta(z|\tau),
\qquad
\Theta(z+\tau|\tau)=e^{-\pi i\tau-2\pi iz}\Theta(z|\tau).
\]
Hence
\[
\frac{\Theta'}{\Theta}(z+1)=\frac{\Theta'}{\Theta}(z),
\qquad
\frac{\Theta'}{\Theta}(z+\tau)=\frac{\Theta'}{\Theta}(z)-2\pi i,
\]
so \(H\) is elliptic with periods \(1\) and \(\tau\).

By the Jacobi product formula, \(\Theta(z|\tau)\) has simple zeros exactly at
\[
z_0+\Lambda,
\qquad \Lambda=\mathbb Z+\mathbb Z\tau.
\]
Thus \(H\) has a double pole at every point of \(z_0+\Lambda\). If \(w=z-z_0\), write
\[
\Theta(z|\tau)=aw+\frac b2w^2+\frac c6w^3+O(w^4),
\]
where
\[
a=\Theta'(z_0|\tau)\ne0,
\quad b=\Theta''(z_0|\tau),
\quad c=\Theta'''(z_0|\tau).
\]
Then
\[
\frac{\Theta'}{\Theta}
=\frac1w+\frac b{2a}
+\left(\frac c{3a}-\frac{b^2}{4a^2}\right)w+O(w^2),
\]
and therefore
\[
H(z)=\frac1{w^2}
+\frac{b^2}{4a^2}-\frac c{3a}+O(w).
\tag{1}
\]

The function \(\wp_\tau(z-z_0)\) is elliptic with the same periods and has at each point of \(z_0+\Lambda\) the same principal part \(w^{-2}\). Hence
\[
H(z)-\wp_\tau(z-z_0)
\]
has removable singularities everywhere and extends to an entire elliptic function. It is bounded on a fundamental parallelogram, hence constant by Liouville's theorem. Thus
\[
H(z)=\wp_\tau(z-z_0)+c_\tau.
\]
Since
\[
\wp_\tau(w)=\frac1{w^2}+O(w^2)
\]
has no constant term at \(w=0\), comparison with (1) gives
\[
\boxed{
c_\tau
=\frac14\left(\frac{\Theta''(z_0|\tau)}{\Theta'(z_0|\tau)}\right)^2
-\frac13\frac{\Theta'''(z_0|\tau)}{\Theta'(z_0|\tau)} }.
\]
This is the theta-function analogue of the sigma-function identity from Exercise 5 of Chapter 9.
:::
