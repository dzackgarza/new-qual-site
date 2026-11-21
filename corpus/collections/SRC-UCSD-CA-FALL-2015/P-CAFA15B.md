---
schema: qual/card@1
id: P-CAFA15B
kind: problem
title: "True or False: real-imaginary inequalities, entire surjection, conformal maps, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the four verdicts already on the card, which are
    correct: False, True, True, False. Added: the route from boundedness of exp(f^2) to
    constancy of f through ff' = 0 and the isolation of zeros (the prose stopped at "f^2 is
    constant, hence f is constant", which is not immediate for a square root); that an entire
    function with a pole at infinity is a polynomial, from the essential-singularity
    alternative; the bijectivity of z -> exp(pi i z) onto the upper half-plane and of the
    Cayley map onto the disk, with the inverse of the Cayley map written; and the estimate that
    turns uniform convergence on the annulus into convergence of the integrals over the circle
    |z| = r, together with the vanishing of the integrals of the polynomials by Cauchy's
    theorem. Not claimed: a retained solution set; the provenance names the examination paper.
---

::: {.problem}
Are the following statements true or false?
Give a brief proof in each case.

(i) Let $f(z)$ be an entire function and let $u(z)$ and $v(z)$ be the real and imaginary parts of $f$.
There is a non-constant function $f(z)$ such that $u^2 \leq v^2 + 2015$.

(ii) If $f(z)$ is an entire function such that $g(z) = f(1/z)$ has a pole at zero, then $f$ is surjective.

(iii) There is a conformal map from the region $U = \{z = x + iy : 0 < x < 1\}$ to the region $\Delta = \{z : \abs{z} < 1\}$.

(iv) There are polynomials $p_1, p_2, \ldots$ such that $\abs{\frac{1}{z(z-4)} - p_n(z)}$ converges uniformly to zero on the annulus $U = \{z \in \CC : 2 < \abs{z} < 3\}$, as $n$ tends to infinity.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2015 complex-analysis examination paper, which carries no solutions. The four verdicts and their arguments below are the card's own and follow the card's previous prose; each part is answered in the order printed.

::: pf

::: {.pf-step #i}
(i) is false: there is no nonconstant entire $f=u+iv$ with $u^2\le v^2+2015$.

::: pf-proof
Suppose $f$ is entire with $u^2\le v^2+2015$. Since $f^2=(u^2-v^2)+2iuv$, one has $\operatorname{Re}(f^2)=u^2-v^2\le2015$ pointwise, so $\abs{e^{f^2}}=e^{\operatorname{Re}(f^2)}\le e^{2015}$: the entire function $e^{f^2}$ is bounded, hence constant by Liouville's theorem. Differentiating, $2ff'e^{f^2}\equiv0$, so $ff'\equiv0$. If $f$ were not identically zero, its zero set would have empty interior (zeros of a nonzero holomorphic function are isolated), so $f'\equiv0$ on a nonempty open set and hence everywhere by continuity; then $f$ is constant. If $f\equiv0$, then $u=v=0$ and $f$ is constant. So in every case $f$ is constant.

:::

:::

::: {.pf-step #ii}
(ii) is true: if $g(z)=f(1/z)$ has a pole at $0$, then $f$ is surjective.

::: pf-proof
$g$ has a pole at $0$ exactly when $\abs{g(z)}\to\infty$ as $z\to0$, that is $\abs{f(w)}\to\infty$ as $w\to\infty$: $f$ has a pole at $\infty$. An entire function with a pole at infinity is a polynomial, because otherwise its Taylor series has infinitely many nonzero terms and $\infty$ would be an essential singularity; and it is nonconstant, a constant having a removable singularity at $\infty$. For each $w\in\CC$ the polynomial $f(z)-w$ is nonconstant, so it has a root by the fundamental theorem of algebra; hence every $w$ lies in $f(\CC)$.

:::

:::

::: {.pf-step #iii}
(iii) is true: $z\mapsto\dfrac{e^{\pi iz}-i}{e^{\pi iz}+i}$ is a conformal map of $U=\theset{0<\operatorname{Re}z<1}$ onto $\Delta$.

::: pf-proof
$z\mapsto e^{\pi iz}$ is the composite of the conformal maps $z\mapsto\pi iz$ and $w\mapsto e^w$, hence conformal; writing $z=x+iy$ with $0<x<1$, one has $e^{\pi iz}=e^{-\pi y}e^{i\pi x}$, whose argument $\pi x$ lies in $(0,\pi)$ and whose modulus $e^{-\pi y}$ ranges over $(0,\infty)$ as $y$ ranges over $\RR$; so the image is exactly the upper half-plane $H$, bijectively. The Cayley map $w\mapsto(w-i)/(w+i)$ is a Möbius transformation carrying $H$ conformally onto $\Delta$: for $w\in H$, $\abs{w-i}<\abs{w+i}$, since the locus $\abs{w-i}=\abs{w+i}$ is the real axis, and $w\mapsto(w-i)/(w+i)$ is injective on $\CC\setminus\theset{-i}$ with inverse $w\mapsto-i(w+1)/(w-1)$ carrying $\Delta$ into $H$. So the composite is the required conformal map.

:::

:::

::: {.pf-step #iv}
(iv) is false: no sequence of polynomials converges uniformly to $\dfrac1{z(z-4)}$ on $U=\theset{2<\abs z<3}$.

::: pf-proof
Suppose $p_n\to h$ uniformly on $U$, where $h(z)=1/(z(z-4))$ is holomorphic on $U$ since its poles $0$ and $4$ lie outside. Fix $r$ with $2<r<3$ and let $\gamma$ be the circle $\abs z=r$, a compact subset of $U$; uniform convergence on $U$ gives uniform convergence on $\gamma$, hence
$$
\int_\gamma p_n(z)\,dz\longrightarrow\int_\gamma h(z)\,dz
$$
because $\abs{\int_\gamma(p_n-h)\,dz}\le2\pi r\sup_\gamma\abs{p_n-h}$. Each $p_n$ is entire, so $\int_\gamma p_n\,dz=0$ for all $n$ by Cauchy's theorem. On the other hand $h$ has no pole on or outside $\gamma$ except at $4$, so the residue theorem applied to the disk $\abs z\le r$, which contains only the pole $z=0$ of $h$, gives
$$
\int_\gamma h(z)\,dz=2\pi i\operatorname{Res}(h,0)=2\pi i\cdot\frac{1}{0-4}=-\frac{\pi i}{2}\ne0 .
$$
So $0\to-\pi i/2$, a contradiction; such polynomials do not exist.

:::

:::

::: {.pf-step #conclusion}
The answers are: (i) false, (ii) true, (iii) true, (iv) false.

::: pf-proof
Steps [](#i){.pf-ref}, [](#ii){.pf-ref}, [](#iii){.pf-ref} and [](#iv){.pf-ref} give the four verdicts with proofs.

:::

:::

:::
:::
