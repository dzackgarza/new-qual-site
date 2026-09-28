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

On the slit plane $\Omega=\CC\setminus(-\infty,0]$, the \dfn{principal branch} of the logarithm is
$$
\log z=\log r+i\theta,\qquad z=re^{i\theta},\ \abs\theta<\pi.
$$
[@SS03, sec. 3.6]

### Integrals and residues

The function $f(z)=1/z$ has no primitive on $\CC\setminus\{0\}$: for the unit circle $C$ parametrized by $z(t)=e^{it}$, $0\le t\le2\pi$,
$$
\int_C f(z)\,dz=\int_0^{2\pi}\frac{ie^{it}}{e^{it}}\,dt=2\pi i\neq0.
$$
[@SS03, sec. 1.3]

::: {.theorem title="Goursat"}
If $\Omega\subseteq\CC$ is open, $T\subset\Omega$ is a triangle whose interior is also contained in $\Omega$, and $f$ is holomorphic on $\Omega$, then $\int_T f(z)\,dz=0$.
[@SS03, Theorem 2.1.1]
:::

### Residues

The contours used with the residue theorem include the keyhole, the multiple keyhole, the rectangular keyhole, the semicircle, the indented semicircle, the sector and the parallelogram [@SS03, ch. 2, Figure 7].

::: {.theorem title="Residue formula"}
Suppose $f$ is holomorphic on an open set containing a circle $C$ and its interior, except for poles at $z_1,\ldots,z_N$ inside $C$. Then
$$
\int_C f(z)\,dz=2\pi i\sum_{k=1}^N\res_{z_k}f.
$$
[@SS03, Corollary 3.2.2]
:::

The proof integrates over a multiple keyhole with one loop around each pole and lets the widths of the corridors tend to zero.

If $f$ has a pole of order $n$ at $z_0$, then near $z_0$
$$
f(z)=\frac{a_{-n}}{(z-z_0)^n}+\frac{a_{-n+1}}{(z-z_0)^{n-1}}+\cdots+\frac{a_{-1}}{z-z_0}+G(z),
$$
with $G$ holomorphic in a neighborhood of $z_0$ [@SS03, Theorem 3.1.3].
The sum of the negative powers is the \dfn{principal part} of $f$ at $z_0$, and the coefficient $a_{-1}$ is the \dfn{residue}, written $\res_{z_0}f=a_{-1}$.
Multiplying the expansion by $(z-z_0)^n$ and differentiating $n-1$ times gives
$$
\res_{z_0}f=\lim_{z\to z_0}\frac1{(n-1)!}\left(\frac{d}{dz}\right)^{n-1}\bigl((z-z_0)^nf(z)\bigr).
$$
[@SS03, Theorem 3.1.4]

At a simple pole $c$ this reads $\res_cf=\lim_{z\to c}(z-c)f(z)$.
If $f=g/h$ near $c$ with $g,h$ holomorphic, $h(c)=0$ and $h'(c)\neq0$, then
$$
\res_cf=\lim_{z\to c}\frac{(z-c)\,g(z)}{h(z)}=\frac{g(c)}{h'(c)},
$$
since $h(z)/(z-c)\to h'(c)$.

The \dfn{residue at infinity} is
$$
\res_\infty f=-\res_0\left(\frac1{z^2}f\!\left(\frac1z\right)\right).
$$
If $f(z)\to0$ as $\abs z\to\infty$, then $g(w)=f(1/w)$ extends holomorphically to $w=0$ with $g(0)=0$, so $w^{-2}g(w)$ has residue $g'(0)$ at $0$, and
$$
\res_\infty f=-\lim_{\abs z\to\infty}zf(z).
$$

### Bounds

::: {.theorem title="$ML$-inequality"}
For a smooth curve $\gamma$ and $f$ continuous on $\gamma$,
$$
\abs{\int_\gamma f(z)\,dz}\le\sup_{z\in\gamma}\abs{f(z)}\cdot\length(\gamma).
$$
[@SS03, Proposition 1.3.1]
:::

[[T-ZO5UU]]

### Blaschke factors

[@SS03, ch. 1, Exercise 7]:

(a) Let $z,w\in\CC$ with $\bar zw\neq1$. Then
$$
\abs{\frac{w-z}{1-\bar wz}}<1\quad\text{if }\abs z<1\text{ and }\abs w<1,
\qquad
\abs{\frac{w-z}{1-\bar wz}}=1\quad\text{if }\abs z=1\text{ or }\abs w=1.
$$
Replacing $z,w$ by $e^{-i\theta}z,e^{-i\theta}w$ reduces both claims to real $z=r$, where
$$
(1-rw)(1-r\bar w)-(r-w)(r-\bar w)=(1-r^2)(1-\abs w^2).
$$

(b) Fix $w$ in the unit disc $\DD$ and let $F(z)\coloneqq\dfrac{w-z}{1-\bar wz}$.

(i) $F$ is holomorphic and maps $\DD$ to itself.

(ii) $F$ interchanges $0$ and $w$: $F(0)=w$ and $F(w)=0$.

(iii) $\abs{F(z)}=1$ when $\abs z=1$.

(iv) $F$ is a bijection $\DD\to\DD$, since $F\circ F=\id$.

### Cauchy's integral formula

::: {.theorem title="Cauchy integral formula"}
If $f$ is holomorphic on an open set containing the closure of a disc $D$, and $C$ is the positively oriented boundary circle of $D$, then
$$
f(z)=\frac1{2\pi i}\int_C\frac{f(\zeta)}{\zeta-z}\,d\zeta\qquad(z\in D).
$$
[@SS03, Theorem 2.4.1]
:::

::: {.corollary}
If $f$ is holomorphic on an open set $\Omega$, then $f$ has complex derivatives of all orders on $\Omega$, and for a circle $C\subset\Omega$ whose interior lies in $\Omega$,
$$
f^{(n)}(z)=\frac{n!}{2\pi i}\int_C\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta
$$
for all $z$ inside $C$ [@SS03, Corollary 2.4.2].
:::

::: {.corollary title="Cauchy inequalities"}
If $f$ is holomorphic on an open set containing the closure of the disc $D$ of radius $R$ centered at $z_0$, with boundary circle $C$, then
$$
\abs{f^{(n)}(z_0)}\le\frac{n!\,\norm f_C}{R^n},\qquad\norm f_C=\sup_{z\in C}\abs{f(z)}.
$$
[@SS03, Corollary 2.4.3]
:::

### Further review

::: {.theorem}
If $f$ is holomorphic on an open set $\Omega$ and $D$ is a disc centered at $z_0$ whose closure lies in $\Omega$, then
$$
f(z)=\sum_{n=0}^\infty a_n(z-z_0)^n\quad(z\in D),\qquad a_n=\frac{f^{(n)}(z_0)}{n!}.
$$
[@SS03, Theorem 2.4.4]
:::

::: {.corollary title="Liouville"}
A bounded entire function is constant.
[@SS03, Corollary 2.4.5]
:::

## Warmup

[[E-W3QMS]]

## Questions

[[P-IOUZO]]

## Qualifying exam problems

[[P-AQRVL]]
