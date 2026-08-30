---
title: Theorems that give a constant
order: 0
problems:
  topics:
  - Liouville's Theorem
  - Liouville Theorem
  - Entire Functions
---

# Theorems that give a constant

"Show that $f$ is constant" is the most common sentence in a complex analysis exam, and there are about eight theorems that end it.
Each one is triggered by a different hypothesis, so the work is matching what you were given to the theorem that consumes it.

## Bounded, and entire

**Liouville.**
The cleanest case, and the one every other entire-function argument reduces to.
If a problem gives you a bound on all of $\CC$ and holomorphy on all of $\CC$, this is finished.

Two ways the hypothesis arrives disguised:

- $f$ is entire and $\lim_{z\to\infty} f(z)$ exists.
  Then $f$ is bounded outside a large disc and continuous on it, so bounded everywhere.

- $f$ is entire and $g(w) \da f(1/w)$ has a removable singularity at $w=0$.
  Same conclusion, stated at infinity.

## Entire, with polynomial growth

**Cauchy's estimates**, not Liouville directly.
If $\abs{f(z)} \leq C\abs{z}^n$ for large $\abs z$, the estimate on the $(n+1)$st derivative gives
\[
\abs{f^{(n+1)}(z_0)} \leq {(n+1)!\, \norm{f}_{C_R} \over R^{n+1}} \leq {(n+1)!\, CR^n \over R^{n+1}} \to 0
,\]
so $f^{(n+1)} \equiv 0$ and $f$ is a polynomial of degree at most $n$.
Liouville is the case $n=0$.
See [[Complex_Analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimates and Liouville]].

## $\abs f$ attains an interior maximum

**Maximum modulus.**
The trigger word is *interior*: on a compact set the maximum is attained somewhere, and the theorem says it is on the boundary unless $f$ is constant.

The same theorem does the minimum, provided $f$ is nonvanishing: apply it to $1/f$.
That proviso is the whole content of the minimum modulus principle, and forgetting it is the standard error.

## The image is not open

**The open mapping theorem.**
A nonconstant holomorphic map sends open sets to open sets, so anything that pins the image into a set with empty interior forces constancy:

- $f(\Omega) \subseteq \RR$, or into any line or circle.
- $\abs f$ is constant, so the image lies in a circle.
- $\Re f$ or $\Im f$ is constant, so the image lies in a line.
- $f$ takes values in a discrete set.

This is usually faster than computing with the Cauchy–Riemann equations, which is the other route to the same conclusions.

## $f$ vanishes on a set with a limit point

**The identity principle.**
The hypothesis is easy to miss because it is usually phrased as data rather than as a limit point: $f$ vanishes on a segment, on a convergent sequence, on an arc, on a set of positive measure in $\RR$.
Any of those has a limit point in the domain, and the conclusion is $f\equiv 0$ on the whole connected domain.

Its everyday use is transferring a real identity to $\CC$: $\sin^2 + \cos^2 = 1$ holds on $\RR$, which has limit points, hence on $\CC$.
See [[Complex_Analysis/cauchy-theory/the-identity-principle|The identity principle]].

## $f'\equiv 0$ on a domain

Connectedness, and nothing more.
Worth listing because it is the cheapest of all and is the last step of most of the arguments above: Liouville's proof ends here, and so does the polynomial-growth argument.

## $f$ omits two values

**Little Picard.**
A nonconstant entire function misses at most one point of $\CC$.
Reach for this only when the problem is genuinely about omitted values, since [[Complex_Analysis/singularities/casorati-weierstrass-and-picard|Casorati–Weierstrass]] settles most such questions with an elementary proof.

## Which hypothesis each one consumes

| Given | Theorem | What it really needs |
| --- | --- | --- |
| a bound on $\CC$ | Liouville | entire, and the bound uniform |
| growth $\bigo(\abs z^n)$ | Cauchy estimates | the bound only for large $\abs z$ |
| an interior max of $\abs f$ | maximum modulus | the domain connected |
| an interior min of $\abs f$ | minimum modulus | $f$ nonvanishing |
| image in a line or circle | open mapping | $f$ nonconstant, to contradict |
| a zero set with a limit point | identity principle | the limit point *inside* the domain |
| two omitted values | little Picard | entire |

The last column is where these problems are actually decided.
A missing connectedness assumption, a limit point on the boundary rather than inside, or a zero of $f$ in a minimum-modulus argument each break the theorem while leaving the statement looking true.
