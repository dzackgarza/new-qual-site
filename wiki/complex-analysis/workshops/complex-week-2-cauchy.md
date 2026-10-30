---
order: 30
title: "Complex analysis workshop week 2: Cauchy's integral formula and residues"
---

# Complex analysis workshop week 2: Cauchy's integral formula and residues

## Topics

- [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors]]

- Integrals over circles and other simple contours

- [[complex-analysis/cauchy-theory/the-integral-formula|Cauchy's integral formula]]

- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's inequalities]]

- [[complex-analysis/residues-and-contours/real-integrals-by-residues|Computing integrals]] — [[complex-analysis/residues-and-contours/computing-residues|residue formulas]], the [[complex-analysis/residues-and-contours/arc-estimates|$ML$-inequality]], and [[T-ZO5UU|Jordan's lemma]]

## Review

### Branches of the logarithm

Recall the [[D-4CSPM|principal branch of the logarithm]]: on the slit plane $\Omega\coloneqq\CC\sm(-\infty,0]$,
$$
\log z=\log r+i\theta,\qquad z=re^{i\theta},\ \abs{\theta}<\pi.
$$
[@SS03, sec. 3.6]

### Integrals and residues

The function $f(z)=1/z$ has no primitive on $\CC\sm\theset{0}$: for the unit circle $C$ parametrized by $z(t)=e^{it}$, $0\le t\le2\pi$,
$$
\int_C f(z)\dz=\int_0^{2\pi}\frac{ie^{it}}{e^{it}}\,dt=2\pi i\neq0.
$$
[@SS03, sec. 1.3]

[[T-B3BDO]]

### Residues

The contours used with the residue theorem include the keyhole, the multiple keyhole, the rectangular keyhole, the semicircle, the indented semicircle, the sector and the parallelogram [@SS03, ch. 2, Figure 7].

[[T-HRPNO]]

If $f$ has a pole of order $n$ at $z_0$, then near $z_0$
$$
f(z)=\frac{a_{-n}}{(z-z_0)^n}+\frac{a_{-n+1}}{(z-z_0)^{n-1}}+\cdots+\frac{a_{-1}}{z-z_0}+G(z),
$$
with $G$ holomorphic in a neighborhood of $z_0$ [@SS03, Theorem 3.1.3].
Recall that the sum of the negative powers is the [[D-C3JIU|principal part]] of $f$ at $z_0$, and the coefficient $a_{-1}$ is the [[D-C3JIU|residue]] $\Res_{z_0}f$.
Multiplying the expansion by $(z-z_0)^n$ and differentiating $n-1$ times gives
$$
\Res_{z_0}f=\lim_{z\to z_0}\frac1{(n-1)!}\left(\frac{d}{dz}\right)^{n-1}\bigl((z-z_0)^nf(z)\bigr).
$$
[@SS03, Theorem 3.1.4]

At a simple pole $c$ this reads $\Res_cf=\lim_{z\to c}(z-c)f(z)$.
If $f=g/h$ near $c$ with $g,h$ holomorphic, $h(c)=0$ and $h'(c)\neq0$, then
$$
\Res_cf=\lim_{z\to c}\frac{(z-c)\,g(z)}{h(z)}=\frac{g(c)}{h'(c)},
$$
since $h(z)/(z-c)\to h'(c)$.

The [[T-WFXQP|residue at infinity]] is
$$
\Res_\infty f=-\Res_0\left(\frac1{z^2}f\!\left(\frac1z\right)\right).
$$
If $f(z)\to0$ as $\abs{z}\to\infty$, then $g(w)\coloneqq f(1/w)$ extends holomorphically to $w=0$ with $g(0)=0$, so $w^{-2}g(w)$ has residue $g'(0)$ at $0$, and
$$
\Res_\infty f=-\lim_{\abs{z}\to\infty}zf(z).
$$

### Bounds

[[T-SFXI7]]

[[T-ZO5UU]]

### Blaschke factors

The following is [@SS03, ch. 1, Exercise 7].

(a) Let $z,w\in\CC$ with $\bar zw\neq1$. Then
$$
\abs{\frac{w-z}{1-\bar wz}}<1\quad\text{if }\abs{z}<1\text{ and }\abs{w}<1,
\qquad
\abs{\frac{w-z}{1-\bar wz}}=1\quad\text{if }\abs{z}=1\text{ or }\abs{w}=1.
$$
Replacing $z,w$ by $e^{-i\theta}z,e^{-i\theta}w$ reduces both claims to real $z=r$, where
$$
(1-rw)(1-r\bar w)-(r-w)(r-\bar w)=(1-r^2)(1-\abs{w}^2).
$$

(b) Fix $w$ in the unit disc $\DD$ and let $F(z)\coloneqq\dfrac{w-z}{1-\bar wz}$.
Then $F$ is holomorphic and maps $\DD$ to itself; $F$ interchanges $0$ and $w$, that is, $F(0)=w$ and $F(w)=0$; $\abs{F(z)}=1$ when $\abs z=1$; and $F$ is a bijection $\DD\to\DD$, since $F\circ F=\id$.

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
