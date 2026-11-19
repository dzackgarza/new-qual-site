---
schema: qual/card@1
id: E-SS4.EX-5
kind: problem
title: Fourier transforms of rational functions without real poles
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, and checked: for xi < 0 the factor
    |e^{-2 pi i z xi}| = e^{2 pi y xi} is at most 1 on the closed upper half-plane, so the upper
    contour is the one used; the bound |R(z)| <= C |z|^{-2} from deg Q >= deg P + 2 makes the
    semicircle integral at most C pi R^{-1}; the residue at a pole of order m is
    (1/(m-1)!) (d/dz)^{m-1}[g e^{-2 pi i z xi}] at the pole with g = (z-alpha)^m R, and Leibniz
    gives a polynomial in xi of degree at most m-1 times e^{-2 pi i alpha xi}. For xi > 0 the same
    argument in the lower half-plane gives the clockwise sign -2 pi i. For (d): the modulus of
    e^{-2 pi i alpha xi} is e^{-2 pi (Im alpha) |xi|} on xi < 0, so the two-sided rate is every
    a < 2 pi dist(poles, R); and the bound cannot be improved, because the leading coefficient
    (1/(m-1)!) g(alpha) (-2 pi i)^{m-1} at a nearest pole is nonzero, so |T(xi)| grows like
    |xi|^{m-1} e^{-2 pi delta |xi|}. The prose's last sentence about the endpoint rate is now a
    step with that reason attached. Statement unchanged; no retained solution set covers the
    exercises of Stein-Shakarchi.
---

::: {.exercise}
More generally, let $R(x) = P(x)/Q(x)$ be a rational function with $(\deg Q) \geq (\deg P) + 2$ and $Q(x) \neq 0$ on the real axis.

(a) Prove that if $\alpha_1, \ldots, \alpha_k$ are the roots of $Q$ in the upper half-plane, then there exists polynomials $P_j(\xi)$ of degree less than the multiplicity of $\alpha_j$ so that
$$
\int_{-\infty}^{\infty} R(x) e^{-2\pi i x\xi}\, dx = \sum_{j=1}^{k} P_j(\xi) e^{-2\pi i\alpha_j\xi}, \quad \text{when } \xi < 0.
$$

(b) In particular, if $Q(z)$ has no zeros in the upper half-plane, then $\int_{-\infty}^{\infty} R(x) e^{-2\pi i x\xi}\, dx = 0$ for $\xi < 0$.

(c) Show that similar results hold in the case $\xi > 0$.

(d) Show that
$$
\int_{-\infty}^{\infty} R(x) e^{-2\pi i x\xi}\, dx = O(e^{-a\abs{\xi}}), \quad \xi \in \RR
$$
as $\abs{\xi} \to \infty$ for some $a > 0$. Determine the best possible $a$'s in terms of the roots of $Q$.

[Hint: For part (a), use residues. The powers of $\xi$ appear when one differentiates the function $f(z) = R(z) e^{-2\pi i z\xi}$ (as in the formula of Theorem 1.4 in the previous chapter). For part (c) argue in the lower half-plane.]
:::

::: {.solution}
Write $R=P/Q$ in lowest terms. The hypothesis $\deg Q\ge\deg P+2$ makes $R$ integrable on the real axis and makes the large semicircle contribute nothing to the contour integral, and the exponential $e^{-2\pi iz\xi}$ decays in the upper half-plane when $\xi<0$ and in the lower half-plane when $\xi>0$; so the transform is a sum of residues at the poles in one half-plane, the residue at a pole of order $m$ being a polynomial in $\xi$ of degree less than $m$ times $e^{-2\pi i\alpha\xi}$. The decay rates follow from that display. The argument is this card's own -- it is the printed hint's route -- since no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #setup}
$R$ is continuous on $\RR$ and $\abs{R(x)}\le C\abs x^{-2}$ for $\abs x\ge\rho$, so the transform $T(\xi)=\int_{\RR}R(x)e^{-2\pi ix\xi}\dd x$ converges absolutely for every $\xi$; and $R$ has finitely many poles, none on $\RR$, each of some multiplicity.

::: pf-proof
Because $Q$ is a polynomial with no real zeros, $R$ is continuous on $\RR$ and bounded there. Since $\deg Q\ge\deg P+2$, the quotient satisfies $\abs{R(z)}\le C\abs z^{-2}$ for large $\abs z$, so $\int_{\abs x\ge\rho}\abs{R}<\infty$ and the integral defining $T$ converges absolutely, as $\abs{e^{-2\pi ix\xi}}=1$ for real $x$. A nonzero polynomial has finitely many roots, so $Q$ has finitely many zeros; $R$ is in lowest terms, so each zero $\alpha$ of $Q$ is a pole of $R$ of order equal to its multiplicity as a root of $Q$.
:::

:::


::: {.pf-step #arc}
For $R>\rho$ put $\Gamma^+_R$ for the boundary of the half-disc $\{\abs z<R,\ \Im z>0\}$ and $\Gamma^-_R$ for that of $\{\abs z<R,\ \Im z<0\}$. Then $\lim_{R\to\infty}\int_{\text{semicircle}}\abs{R(z)e^{-2\pi iz\xi}}\abs{\dd z}=0$: on the upper semicircle when $\xi<0$, and on the lower semicircle when $\xi>0$.

::: pf-proof
For $z=x+iy$ one has $\abs{e^{-2\pi iz\xi}}=e^{2\pi y\xi}$. If $\xi<0$ and $y\ge0$ this is at most $1$; if $\xi>0$ and $y\le0$ it is also at most $1$. In either case, by step [](#setup){.pf-ref} the integrand is bounded by $C R^{-2}$ on the semicircle, whose length is $\pi R$, so the integral is at most $C\pi R^{-1}\to0$.
:::

:::


::: {.pf-step #upper}
For $\xi<0$, $\displaystyle T(\xi)=2\pi i\sum_{\Im\alpha_j>0}\operatorname{Res}_{z=\alpha_j}\bigl(R(z)e^{-2\pi iz\xi}\bigr)$, the sum being over the poles in the upper half-plane; and the residue at a pole $\alpha$ of order $m$ has the form $P_\alpha(\xi)e^{-2\pi i\alpha\xi}$ with $\deg P_\alpha<m$.

::: pf-proof
Let $\xi<0$ and let $R$ be so large that all upper poles lie inside $\Gamma^+_R$. The function $R(z)e^{-2\pi iz\xi}$ is holomorphic except at the poles of $R$, so the residue theorem gives
$$
\oint_{\Gamma^+_R}R(z)e^{-2\pi iz\xi}\dd z=2\pi i\sum_{\Im\alpha_j>0}\operatorname{Res}_{z=\alpha_j}\bigl(R(z)e^{-2\pi iz\xi}\bigr),
$$
the contour being traversed counterclockwise. The contour integral is the sum of the integral over $[-R,R]$, which tends to $T(\xi)$ by step [](#setup){.pf-ref}, and the integral over the upper semicircle, which tends to $0$ by step [](#arc){.pf-ref}. Passing to the limit gives the display.

For the shape of a single residue, write $R(z)=(z-\alpha)^{-m}g(z)$ with $g$ holomorphic near $\alpha$ and $g(\alpha)\ne0$. Then
$$
\operatorname{Res}_{z=\alpha}\bigl(R(z)e^{-2\pi iz\xi}\bigr)=\frac{1}{(m-1)!}\Bigl(\frac{\dd}{\dd z}\Bigr)^{m-1}\Bigl[g(z)e^{-2\pi iz\xi}\Bigr]_{z=\alpha}.
$$
By the Leibniz rule, $(\dd/\dd z)^{m-1}(g\,e^{-2\pi iz\xi})$ evaluated at $\alpha$ is $\sum_{r=0}^{m-1}\binom{m-1}{r}g^{(m-1-r)}(\alpha)(-2\pi i\xi)^re^{-2\pi i\alpha\xi}$, a polynomial in $\xi$ of degree at most $m-1$ times $e^{-2\pi i\alpha\xi}$.
:::

:::


::: {.pf-step #parta}
(a) There are polynomials $P_j(\xi)$ with $\deg P_j<m_j$ and $\displaystyle T(\xi)=\sum_{j=1}^kP_j(\xi)e^{-2\pi i\alpha_j\xi}$ for $\xi<0$, where $\alpha_1,\dots,\alpha_k$ are the roots of $Q$ in the upper half-plane and $m_j$ their multiplicities.

::: pf-proof
By step [](#upper){.pf-ref} each upper pole contributes a term $P_j(\xi)e^{-2\pi i\alpha_j\xi}$ with $\deg P_j<m_j$, and the sum is finite because $Q$ has finitely many roots by step [](#setup){.pf-ref}. Summing those terms gives (a).
:::

:::


::: {.pf-step #partb}
(b) If $Q$ has no zeros in the upper half-plane, then $T(\xi)=0$ for every $\xi<0$.

::: pf-proof
The sum in step [](#parta){.pf-ref} is then empty, so $T(\xi)=0$ for $\xi<0$. For $\xi>0$ there is no reason for $T$ to vanish, and in general it does not.
:::

:::


::: {.pf-step #partc}
(c) For $\xi>0$, $T(\xi)=-2\pi i\sum_{\Im\beta_j<0}Q_j(\xi)e^{-2\pi i\beta_j\xi}$, with $\deg Q_j$ less than the multiplicity of $\beta_j$, the sum being over the poles in the lower half-plane; in particular $T(\xi)=0$ for $\xi>0$ when $Q$ has no zeros there.

::: pf-proof
This is the argument of step [](#upper){.pf-ref} with the lower half-plane in place of the upper one. For $\xi>0$ the exponential decays as $\Im z\to-\infty$ by step [](#arc){.pf-ref}, so the contour $\Gamma^-_R$ is used; it is traversed clockwise, which contributes the sign $-2\pi i$ rather than $+2\pi i$. The residue at a lower pole $\beta$ of order $m$ has the form $Q_\beta(\xi)e^{-2\pi i\beta\xi}$ with $\deg Q_\beta<m$ by the Leibniz computation of step [](#upper){.pf-ref}, and the semicircle contributes $0$ by step [](#arc){.pf-ref}. If there is no lower pole the sum is empty and $T$ vanishes on $\xi>0$.
:::

:::


::: {.pf-step #partd}
(d) With $\delta=\operatorname{dist}(\{\text{poles of }R\},\RR)>0$, for every $a<2\pi\delta$ one has $T(\xi)=O(e^{-a\abs\xi})$ as $\abs\xi\to\infty$, and no larger $a$ works in general: the supremal rate is $2\pi\delta$.

::: pf-proof
Let $\xi<0$. By step [](#parta){.pf-ref}, $\abs{T(\xi)}\le\sum_j\abs{P_j(\xi)}e^{2\pi(\Im\alpha_j)\xi}$, and $\Im\alpha_j\ge\delta$ together with $\xi<0$ gives $e^{2\pi(\Im\alpha_j)\xi}\le e^{-2\pi\delta\abs\xi}$; since $\abs{P_j(\xi)}$ is bounded by a constant times $(1+\abs\xi)^{m_j-1}$, one gets $\abs{T(\xi)}\le C(1+\abs\xi)^{M}e^{-2\pi\delta\abs\xi}$ for a fixed $M$, which is $O(e^{-a\abs\xi})$ for every $a<2\pi\delta$. The same estimate for $\xi>0$ comes from step [](#partc){.pf-ref}; where one half-plane contains no pole the corresponding estimate is the sharper $T=0$ there. So the bound holds with every $a<2\pi\delta$.

For the optimality, let $\alpha$ be a pole at distance $\delta$ from $\RR$, say in the upper half-plane, and let $m$ be its order. The coefficient of $\xi^{m-1}e^{-2\pi i\alpha\xi}$ in the residue at $\alpha$ is $c\ne0$: it is $\frac{1}{(m-1)!}g(\alpha)(-2\pi i)^{m-1}$ in the notation of step [](#upper){.pf-ref}, and $g(\alpha)\ne0$. So $\abs{T(\xi)}$ grows like $\abs c\abs\xi^{m-1}e^{-2\pi\delta\abs\xi}$ along $\xi\to-\infty$, and for $a>2\pi\delta$ the quotient $\abs{T(\xi)}e^{a\abs\xi}\ge\abs c\abs\xi^{m-1}e^{(a-2\pi\delta)\abs\xi}\to\infty$; hence no $a>2\pi\delta$ works. At $a=2\pi\delta$ the estimate holds exactly when every pole at distance $\delta$ is simple, since then $\deg P_j=0$ and no polynomial factor appears; with a multiple pole the factor $\abs\xi^{m-1}$ spoils it, so the endpoint rate is a supremum and not a maximum in general.
:::

:::


::: {.pf-step #conclusion}
Parts (a)--(d) hold as stated, the best possible $a$ in (d) being $2\pi\operatorname{dist}(\{\text{poles of }R\},\RR)$, attained in the estimate when the nearest poles are simple.

::: pf-proof
Steps [](#parta){.pf-ref} through [](#partd){.pf-ref} prove the four parts. For the last sentence of (d): the rate $2\pi\delta$ is a supremum by step [](#partd){.pf-ref}, and it is attained, i.e. $T(\xi)=O(e^{-2\pi\delta\abs\xi})$ holds, when no pole at distance $\delta$ has order $2$ or more, because then every polynomial factor is constant.
:::

:::

:::
:::
