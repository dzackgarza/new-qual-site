---
title: Theorems that give a constant
order: 0
topics:
- Liouville's Theorem
- Entire Functions

---

# Theorems that give a constant

Throughout, $\Omega\subseteq\CC$ is a connected open set.

## Bounded and entire

By [[T-QHIHJ|Liouville's theorem]], a bounded entire function is constant.

Two hypotheses imply boundedness of an entire function $f$:

- $\lim_{z\to\infty} f(z)$ exists.
  Then $f$ is bounded outside a large closed disc and continuous on that disc, so bounded on $\CC$.

- $g(w) \coloneqq f(1/w)$ has a removable singularity at $w=0$.
  This is the same condition as the existence of $\lim_{z\to\infty} f(z)$.

## Entire, with polynomial growth

If $f$ is entire and $\abs{f(z)} \leq C\abs{z}^n$ for all large $\abs z$, then for fixed $z_0$ and large $R$ Cauchy's inequality on the circle $C_R$ given by $\abs{z - z_0} = R$ gives
$$
\abs{f^{(n+1)}(z_0)} \leq {(n+1)!\, \norm{f}_{C_R} \over R^{n+1}} \leq {(n+1)!\, C(R+\abs{z_0})^n \over R^{n+1}} \to 0
,$$
so $f^{(n+1)} \equiv 0$ and $f$ is a polynomial of degree at most $n$.
Liouville's theorem is the case $n=0$.
See [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy estimates and Liouville]].

## $\abs f$ has a local maximum in $\Omega$

By the [[T-BYNL5|maximum modulus principle]], if $\abs f$ has a local maximum at a point of $\Omega$, then $f$ is constant.
For $\Omega$ bounded and $f$ continuous on $\overline\Omega$, the maximum of $\abs f$ over $\overline\Omega$ is attained on $\bd\Omega$.

If $f$ does not vanish on $\Omega$, applying the maximum modulus principle to $1/f$ shows that a local minimum of $\abs f$ in $\Omega$ forces $f$ to be constant ([[T-YLI6Y]]).
The function $f(z)=z$ on $\DD$ has a minimum of $\abs f$ at its zero $0$ and is not constant.

## The image has empty interior

By the [[C-FRF33|open mapping theorem]], a nonconstant holomorphic function on $\Omega$ maps open sets to open sets.
So $f$ is constant if its image has empty interior, in particular if

- $f(\Omega)$ lies in a line or a circle,

- $\abs f$ is constant, so that $f(\Omega)$ lies in a circle,

- $\Re f$ or $\Im f$ is constant, so that $f(\Omega)$ lies in a line, or

- $f(\Omega)$ is a discrete set.

Each of these can also be proved from the Cauchy--Riemann equations.

## $f$ vanishes on a set with a limit point in $\Omega$

By the [[T-SVF2W|identity principle]], if the zero set of $f$ has a limit point in $\Omega$, then $f\equiv 0$.
A segment, an arc, a convergent sequence of distinct points with limit in $\Omega$, and a subset of $\RR\cap\Omega$ of positive measure each have a limit point in $\Omega$.

Applied to $\sin^2 z + \cos^2 z - 1$, which vanishes on $\RR$, the identity principle gives $\sin^2 z + \cos^2 z = 1$ on $\CC$.
See [[complex-analysis/cauchy-theory/the-identity-principle|The identity principle]].

## $f'\equiv 0$ on $\Omega$

If $f' \equiv 0$ on the connected open set $\Omega$, then $f$ is constant: $f$ is constant along every segment in $\Omega$, and $\Omega$ is polygonally connected.
The proofs of Liouville's theorem and of the polynomial-growth bound end with this step.

## $f$ omits values

By the [[T-HWBWI|little Picard theorem]], a nonconstant entire function omits at most one value of $\CC$.

If an entire function $f$ omits every value in a disc $D_r(a)$, then $g\coloneqq 1/(f-a)$ is entire with $\abs g\leq 1/r$, so $g$, and hence $f$, is constant by Liouville's theorem.
[[complex-analysis/singularities/casorati-weierstrass-and-picard|Casorati--Weierstrass and Picard]] gives the corresponding statements near an essential singularity.

## Hypotheses

| Given | Theorem | Hypotheses |
| --- | --- | --- |
| a bound on $\CC$ | Liouville | $f$ entire |
| growth $\bigo(\abs z^n)$ | Cauchy estimates | $f$ entire; the bound for large $\abs z$ |
| a local maximum of $\abs f$ | maximum modulus | $\Omega$ connected |
| a local minimum of $\abs f$ | minimum modulus | $\Omega$ connected, $f$ nonvanishing |
| image in a line or circle | open mapping | $\Omega$ connected |
| a zero set with a limit point | identity principle | $\Omega$ connected, the limit point in $\Omega$ |
| two omitted values | little Picard | $f$ entire |
