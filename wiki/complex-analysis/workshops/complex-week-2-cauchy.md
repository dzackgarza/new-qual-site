---
order: 30
title: "Complex analysis workshop week 2: Cauchy's integral formula and residues"
---

# Complex analysis workshop week 2: Cauchy's integral formula and residues

## Topics

- [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors]]

- [[complex-analysis/cauchy-theory/contours-and-primitives|Integrals over circles and other simple contours]]

- [[complex-analysis/cauchy-theory/the-integral-formula|Cauchy's integral formula]]

- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's inequalities]]

- [[complex-analysis/residues-and-contours/real-integrals-by-residues|Computing integrals]] — [[complex-analysis/residues-and-contours/computing-residues|residue formulas]], the [[complex-analysis/residues-and-contours/arc-estimates|ML estimate]], and [[T-ZO5UU|Jordan's lemma]]

## Review

### Branches of the logarithm

Recall the [[D-4CSPM|principal branch of the logarithm]]: on the slit plane $\Omega\coloneqq\CC\sm(-\infty,0]$,
$$
\log z=\log r+i\theta,\qquad z=re^{i\theta},\ \abs{\theta}<\pi.
$$
[@SS03, sec. 3.6]

### Integrals and residues

The function $f(z)=1/z$ has no [[D-6RZQN|primitive]] on $\CC\sm\theset{0}$: for the unit circle $C$ parametrized by $z(t)=e^{it}$, $0\le t\le2\pi$,
$$
\int_C f(z)\dz=\int_0^{2\pi}\frac{ie^{it}}{e^{it}}\,dt=2\pi i\neq0.
$$
[@SS03, sec. 1.3]

[[T-B3BDO]]

### Residues

The contours used with the residue theorem include the multiple keyhole, the rectangular keyhole, the semicircle, the indented semicircle, the sector and the parallelogram [@SS03, ch. 2, Figure 7].

[[T-HRPNO]]

A function with a pole of order $n$ at $z_0$ has the Laurent expansion
$$
f(z)=\frac{a_{-n}}{(z-z_0)^n}+\frac{a_{-n+1}}{(z-z_0)^{n-1}}+\cdots+\frac{a_{-1}}{z-z_0}+G(z)
$$
with $G$ holomorphic near $z_0$ [@SS03, Theorem 1.3 of Chapter 3], the sum of the negative powers is the [[D-C3JIU|principal part]] of $f$ at $z_0$, and $a_{-1}$ is the [[D-C3JIU|residue]] $\Res_{z_0}f$.

[[T-ESKLY]]

[[C-Q6BSL]]

[[D-Q8XRV]]

[[T-WFXQP]]

### Bounds

[[T-SFXI7]]

[[T-ZO5UU]]

### Blaschke factors

[[E-SS1.EX-7]]

### Cauchy's integral formula

[[T-LA2UI]]

[[T-22RQZ]]

### Further review

[[T-GROTS]]

[[T-QHIHJ]]

## Warmup

[[E-W3QMS]]

## Questions

[[P-IOUZO]]

## Qualifying exam problems

[[P-AQRVL]]
