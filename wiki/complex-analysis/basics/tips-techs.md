---
order: 0
---

# Info / Tips / Techniques

> A great deal of content borrowed from [Chris Eur's complex analysis notes (Stanford)](https://web.stanford.edu/~chriseur/notes_pdf/Eur_ComplexAnalysis_Notes.pdf).

Some useful notation:

- $\DD_r(a) \da \ts{z\in \CC \st \abs{z-a}< r}$, the open disc of radius $r$ about $a$.
- $\bar{\DD}_r(a) \da \ts{z\in \CC \st \abs{z-a} \leq r}$, the closed disc of radius $r$ about $a$.
- $\DD_r^*(a) \da \ts{z\in \CC \st 0 < \abs{z-a} < r}$, the punctured disc of radius $r$ about $a$.
- $\Delta \da \DD_1(0)$ the standard unit disc
- $\bar\Delta \da \bar{\DD}_1(0)$ the closed unit disc
- $\Delta^* \da \DD_1^*(0)$ the punctured unit disc.
- $\Omega$ an open simply-connected subset of $\CC$.
- $\OO(\Omega), \Hol(\Omega), \Hol(\Omega, \CC)$ the holomorphic functions $f:\Omega \to \CC$, equipped with the structure of a $\CC\dash$algebra.

## Greatest Hits

Things to know well:

- Estimates for derivatives
- [[complex-analysis/cauchy-theory/cauchys-theorem]]
- [[complex-analysis/cauchy-theory/the-integral-formula|Cauchy's integral formula and mean value property]]
- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's inequality]]
- [[complex-analysis/cauchy-theory/morera-and-converses|Morera's theorem]]
- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Liouville's theorem]]
- [[complex-analysis/cauchy-theory/maximum-modulus-and-open-mapping|Maximum modulus and open mapping]]
- [[complex-analysis/counting-zeros/rouches-theorem|Rouche's theorem]]
- [[complex-analysis/cauchy-theory/schwarz-reflection|The Schwarz reflection principle]]
- [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|The Schwarz lemma]]
- [[complex-analysis/singularities/casorati-weierstrass-and-picard|Casorati-Weierstrass]]
- [[complex-analysis/conformal-maps/build-me-a-map|Conformal maps]]
- [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Automorphisms of the disc and plane]]
- [[complex-analysis/cauchy-theory/the-identity-principle|The identity principle]]
- [[complex-analysis/singularities/casorati-weierstrass-and-picard|Picard theorems]]
- [[complex-analysis/residues-and-contours/computing-residues|Computing residues]]
- Jordan's lemma
- [[complex-analysis/holomorphic-functions/the-cauchy-riemann-equations|The Cauchy-Riemann equations]]
- [[complex-analysis/counting-zeros/the-argument-principle|The argument principle]]
- [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|The Riemann mapping theorem]]
- [[complex-analysis/singularities/removable-poles-essential|Riemann's removable singularity theorem]]
- [[complex-analysis/holomorphic-functions/harmonic-functions|Harmonic functions and their mean value property]]

For a compact statement sheet, see [[attachments/ComplexAnalysisNotes.pdf|Complex analysis theorem summary]].

## Common tricks

- Virtually any time: consider $1/f(z)$ and $f(1/z)$.

:::{.remark title="Showing a function is constant"}
If you want to show that a function $f$ is constant, try one of the following:

- Write $f = u + iv$ and use Cauchy-Riemann to show $u_x, u_y = 0$, etc.
- Show that $f$ is entire and bounded.
  - If you additionally want to show $f$ is zero, show $\lim_{z\to\infty} f(z) = 0$.

:::
:::{.fact}
To show a function is holomorphic,

- Use Morera's theorem
- Find a primitive (sufficient but not necessary)

:::
:::{.fact}
To count zeros:

- Rouche's theorem
- The argument principle

:::
## Basic but Useful Facts

### Arithmetic

:::{.fact title="Some useful facts about basic complex algebra"}
\[
z\bar z &= \abs{z}^2 &&
\Arg(z/w) = \Arg(z) - \Arg(w) \\
\Re(z) &= { z + \bar z \over 2} &&
\Im(z) = {z - \bar{z} \over 2i}
.\]

Exponential forms of cosine and sine, where it's sometimes useful to set $w\da e^{iz}$:
\[
\cos(z)
&= \frac 1 2 \qty{e^{iz} + e^{-iz}} = {1\over 2}(w+ w\inv)\\
\sin(z)
&= \frac{1}{2i}\qty{e^{iz} - e^{-iz}} = {1\over 2i}(w-w\inv)
.\]

Exponential forms of *hyperbolic* cosine and sin:
\[
\cosh(z)
&= \cos(iz)
= {1\over 2}\qty{e^z + e^{-z}} \\
\sinh(z)
&= -i \sin(iz)
= {1\over 2}\qty{e^z - e^{-z}}
.\]

Some other useful facts about the hyperbolic exponentials:

- They are periodic with period $2\pi i$.
- $\dd{}{z}\cosh(z) = \sinh(z)$ and $\dd{}{z}\sinh(z) = \cosh(z)$.
- $\sinh$ is odd and $\cosh$ is even.
- $\cosh(z + i\pi) = -\cosh(z)$ and $\sinh(z + i\pi) = -\sinh(z)$.
- $\cosh$ has zeros at $\ts{i\pi\qty{2k+1\over 2}} = \ts{i \qty{\pi/2 + k\pi}}$, i.e. $\cdots, -\pi/2, \pi/2, 3\pi/2,\cdots$, the half-integers.
- $\sinh$ has zeros at $\ts{i\pi k}$, i.e. the integers.

:::
:::{.fact}
Some computations that come up frequently:
\[
\abs{z \pm w}^2 &= \abs{z}^2 + \abs{w}^z + 2\Re(\bar{w}z) \\
(a+bi)(c+di) &= (ac - bd) + (ad + bc) \\
{1\over \abs{a+b}} &\leq {1 \over {\abs a - \abs b}} &&
\abs{e^{z}} = e^{\Re(z)}, \quad \arg(e^z) = \Im(z)
.\]

:::
### Calculus

:::{.fact}
Various differentials:
\[
dz &= dx + i~dy \\
d\bar z &= dx - i~dy \\ \\
f_z &= f_x = f_y / i
.\]

Integral of a complex exponential:
\[
\int_{0}^{2 \pi} e^{i \ell x} d x
&=\left\{\begin{array}{ll}
{2 \pi} & {\ell=0} \\
{0} & \text{else}
\end{array}\right.
.\]

:::
- Set $w=e^z$.
- If $f$ has no zeros, $1/f$ is holomorphic, so apply a theorem about holomorphic functions to the reciprocal.
  This is the standard route to the minimum modulus principle and to Liouville arguments about functions bounded below.
- If $f$ is holomorphic in a neighborhood of $\DD$ and $\abs{f} = 1$ on $\bd \DD$, then $f$ is a finite Blaschke product.
- If $\Omega$ is connected, $f$ admits a log and exponential, so try setting $f^{1\over n} = \exp\qty{{1\over n}\log(f)}$.

## Holomorphic

- To show a function is holomorphic,
	- Use Morera's theorem
	- Find a primitive (sufficient but not necessary)
	- Express $f$ as a convergent power series

- Holomorphic functions have isolated zeros.

## Arithmetic

Some silly arithmetic tricks:

- Absolutely essential: $\abs{f}^2 = f\bar{f}$.
- $z$ is purely imaginary $\iff \bar{z} = -z$.
- $z\in \RR \iff \bar z = z$.
- $\log\qty{\abs{z}} = {1\over 2}\log\qty{\abs{z}^2} = {1\over 2}\log\qty{x^2 + y^2}$, which is easier to differentiate.
- To prove $a=b$, try $a/b = 1$ or $a-b=0$.
- $\int_0^{2\pi} e^{i(m-n)\theta}\dtheta = \chi_{m=n}\cdot 2\pi$.

## Showing a function is constant (or zero)

- Show $f' = 0$.
	- Can write $f=u+iv$ and show $u_x, u_y = 0$ and apply CR.
- Show $\abs{f}=0$ on the boundary and apply the MMP.
- Show that $f$ attains a minimum or maximum on the interior of a domain where it is nonzero.
- Show that $f$ is entire and bounded.
  - If you additionally want to show $f$ is zero, show $\lim_{z\to\infty} f(z) = 0$.
  - Useful trick: show that *either* $\abs{f} \geq M$ or $\abs{f} \leq M$, then by Liouville on $f$ or $1/f$ respectively, $f$ must be constant.
  - Similar trick: show either $e^f$ or $e^{-f}$ is bounded.
  - If the function is periodic, just bound it on a fundamental domain.
- Show that $f(\CC)$ is not an open set (e.g. $\RR$ or $\bd \DD_r(0)$, and apply the open mapping theorem.
	- More generally, the image can be dimension 0 or 2, but never 1. 
	- E.g. if $\im(f) \subseteq \RR$ or $\abs{f} = R$ is constant.
- A holomorphic function with a non-isolated zero is identically zero.
	- How to use: show $f-g$ has uncountably many zeros
- Show that $f$ omits at least 2 values and apply little Picard.
	- E.g. if $f$ misses an open set, or $\abs{f} \geq M$ or $\abs{f} \leq M$.
- Define $g\da e^f$, then $\abs{g} = e^{\Re(f)}$ and if $g$ is constant then $f$ is constant.
- Show any of the following are constant:
	- $u = \Re(f)$
	- $v = \Im(f)$
	- $\abs{f}$
	- $\Arg(f)$
- Show that $f$ preserves $\bd \DD$, so $\abs{f(z)} = 1$ when $\abs{z} = 1$, and has no zeros in $\DD$.
- To show $f(z) = g(z)$ infinitely often, show $f(z)/g(z)$ (or $f(1/z)/g(1/z)$) has an essential singularity and apply Picard or Casorati.

## Singularities 

- Let $z_0$ be a singularity of $f$. To show $z_0$ is...
	- **Removable**: show that $\lim_{z\to z_0} f(z)$ is bounded.
	- **A pole of some order:** show $\lim_{z\to z_o}f(z) = \infty$.
	- **A pole of order $m$**: write $f(z) = (z-z_0)^mg(z)$ where $g(z_0)\neq 0$ (or check the Laurent expansion directly).
    - Can also check that $\del_z^k f(z_0) \neq 0$ for $k<m$ but $\del_z^m f(z_0) = 0$.
	- **Essential**: show that $\lim_{z\to z_0} f(z)$ doesn't exist (e.g. if it's oscillatory).
    - Alternatively, show $z_0$ is neither removable nor a pole, or that $f$ has a Laurent expansion about $z_0$ with infinitely many negative terms.
  - It can be useful to take a specific sequence $\ts{z_k}\to z_0$.

- $f$ and $f'$ have the same poles.

## Zeros

- To show that a zero $z_0$ is order $n$, show that $f^{(<n)}(z_0) = 0$ but $f^{(n)}(z_0) \neq 0$.
- Getting rid of zeros: divide by a Blaschke product.
- To count zeros:
	- Rouche's theorem
	- The argument principle
- If $f(z_0)\neq 0$, by continuity there is some neighborhood where $f$ is nonzero.
	- Conversely, if $f$ is holomorphic at $z_0$ *is* a zero, there is punctured neighborhood of $z_0$ where $f$ is nonzero.

## Estimating

- To prove $a\leq b$, try showing ${a\over b} \leq 1$ and reason about $\DD$, or show $b-a\geq 0$, 
- To bound a rational function, use the reverse triangle inequality:
\[
\abs{a\pm b} \geq \abs{ \abs{a} - \abs{b}} \implies {1\over \abs{a\pm b}} \leq {1\over \abs{\abs{a} - \abs{b} } }
.\]
- Bounding a derivative using the original function: Cauchy's formula.
  - Also works to bound a function in terms of its integral, e.g. over a compact set like a curve.
- If $\abs{f} = M$ on $\bd \Omega$, then if (importantly) $f\neq 0$ in $\Omega$ then $\abs{f} = M$ on all of $\bar \Omega$ by apply the MMP to $f$ and $1/f$.
	- Why $f\neq 0$ is necessary: take $f(z) = z$.
- To show that a sequence of harmonic functions converge on e.g. a disc or rectangle, find good estimates on the boundary and apply the MMP.
- For real analysis: if $\abs{f'} \leq M$, apply the mean value theorem to get $\abs{f(x) - f(y)} \leq M\abs{x-y}$.
- To show $\abs{f} \leq \abs{g}$: if you have a factor of $z$ to play with, try to apply Schwarz to $f/g$ to get $\abs{f/g}\leq \abs{z}$.

  
## Polynomials

- $f$ is polynomial when:
		- $f^{(n)} =0$ for every $n$ large enough (e.g. using Cauchy's inequality)
		- $f$ is entire and its singularity at $\infty$ is a pole (or removable, for a constant polynomial).

## Series

The standard expansions, generalized binomial coefficients, Cauchy products, inverses, and square-root expansions are collected in [[complex-analysis/basics/series-reference|Series: Reference]].

A frequently used geometric expansion is
\[
\frac{1}{z-w}
=\frac{1}{(z-a)\left(1-\frac{w-a}{z-a}\right)}
=\sum_{n=0}^{\infty}\frac{(w-a)^n}{(z-a)^{n+1}},
\qquad \abs{w-a}<\abs{z-a}.
\]
