---
schema: qual/card@1
id: E-SS4.EX-12
kind: problem
title: 'Hardy''s theorem: $f$ and $\hat f$ both $O(e^{-\pi x^2})$ force $f=ce^{-\pi x^2}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Phragmén–Lindelöf
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the limiting parameter in part (b) from beta tending to pi to beta decreasing to 1, so the sectors exhaust the upper half-plane.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    The card's statement omitted the bracketed hint the book prints at PDF page 147, printed p.128: "[Hint: To prove the result, use the inequality −ξ p + ξu ≤ uq ...]"
    A completeness audit of the collection against the book flagged the omission; the hint
    is restored verbatim from the print. The mathematics of the statement is unchanged.

---

::: {.exercise}
The principle that a function and its Fourier transform cannot both be too small at infinity is illustrated by the following theorem of Hardy.

If $f$ is a function on $\RR$ that satisfies
$$
f(x) = O(e^{-\pi x^2}) \quad \text{and} \quad \hat{f}(\xi) = O(e^{-\pi\xi^2}),
$$
then $f$ is a constant multiple of $e^{-\pi x^2}$. As a result, if $f(x) = O(e^{-\pi Ax^2})$, and $\hat{f}(\xi) = O(e^{-\pi B\xi^2})$, with $AB > 1$ and $A, B > 0$, then $f$ is identically zero.

(a) If $f$ is even, show that $\hat{f}$ extends to an even entire function. Moreover, if $g(z) = \hat{f}(z^{1/2})$, then $g$ satisfies
$$
\abs{g(x)} \leq c e^{-\pi x} \quad \text{and} \quad \abs{g(z)} \leq c e^{\pi R\sin^2(\theta/2)} \leq c e^{\pi\abs{z}}
$$
when $x \in \RR$ and $z = Re^{i\theta}$ with $R \geq 0$ and $\theta \in \RR$.

(b) Apply the Phragmén–Lindelöf principle to the function
$$
F(z) = g(z) e^{\gamma z} \quad \text{where } \gamma = i\pi \frac{e^{-i\pi/(2\beta)}}{\sin \pi/(2\beta)}
$$
and the sector $0 \leq \theta \leq \pi/\beta < \pi$, and let $\beta \downarrow 1$ to deduce that $e^{\pi z} g(z)$ is bounded in the closed upper half-plane. The same result holds in the lower half-plane, so by Liouville's theorem $e^{\pi z} g(z)$ is constant, as desired.

(c) If $f$ is odd, then $\hat{f}(0) = 0$, and apply the above argument to $\hat{f}(z)/z$ to deduce that $f = \hat{f} = 0$. Finally, write an arbitrary $f$ as an appropriate sum of an even function and an odd function.
[Hint: To prove the result, use the inequality $-\xi^p+\xi u\le u^q$, which is valid when $\xi$ and $u$ are non-negative. To establish this inequality, examine separately the cases $\xi^p\ge\xi u$ and $\xi^p<\xi u$; note also that the functions $\xi=u^{q-1}$ and $u=\xi^{p-1}$ are inverses of each other because $(p-1)(q-1)=1$.]
:::

::: {.solution}

The argument is the card's own, following the three steps the exercise prescribes. The Fourier transform is normalised as $\widehat f(\zeta)=\int_{\RR}f(x)e^{-2\pi ix\zeta}dx$.

::: pf

::: {.pf-step #entire}

(a) $\widehat f$ extends to an entire function with $\abs{\widehat f(\xi+i\eta)}\le C'e^{\pi\eta^{2}}$.

::: pf-proof

The hypothesis $\abs{f(x)}\le Ce^{-\pi x^{2}}$ makes the integral $\widehat f(\zeta)=\int_{\RR}f(x)e^{-2\pi ix\zeta}dx$ converge for every $\zeta\in\CC$, locally uniformly in $\zeta$, since $\abs{f(x)e^{-2\pi ix\zeta}}\le Ce^{-\pi x^{2}+2\pi\abs{\eta}\abs{x}}$ with $\zeta=\xi+i\eta$, and this is integrable in $x$ and locally bounded in $\eta$. A locally uniform limit of holomorphic functions is holomorphic, so $\widehat f$ is entire. Completing the square, $-\pi x^{2}+2\pi\eta x=-\pi(x-\eta)^{2}+\pi\eta^{2}$, so
$$
\abs{\widehat f(\xi+i\eta)}\le C\int_{\RR}e^{-\pi(x-\eta)^{2}}e^{\pi\eta^{2}}dx=C'e^{\pi\eta^{2}}.
$$

:::

:::

::: {.pf-step #even}

(a) If $f$ is even then $g(z)=\widehat f(\sqrt z)$ is a well-defined even entire function satisfying $\abs{g(x)}\le Ce^{-\pi x}$ for real $x$ and $\abs{g(z)}\le C'e^{\pi R\sin^{2}(\theta/2)}$ for $z=Re^{i\theta}$.

::: pf-proof

For even $f$, $\widehat f(-\zeta)=\int f(x)e^{2\pi ix\zeta}dx=\widehat f(\zeta)$ after substituting $x\mapsto-x$, so $\widehat f$ is even and $\widehat f(\zeta)$ depends only on $\zeta^{2}$; hence there is an entire $g$ with $g(w^{2})=\widehat f(w)$, which is the stated $g$ and is independent of the choice of square root. For $x\ge0$ take $\sqrt x\in\RR_{\ge0}$: $\abs{g(x)}=\abs{\widehat f(\sqrt x)}\le Ce^{-\pi x}$. For $x<0$ take $\sqrt x=i\sqrt{\abs x}$, so $\eta=\sqrt{\abs x}$ and $\abs{g(x)}\le C'e^{\pi\abs x}=C'e^{-\pi x}$. For $z=Re^{i\theta}$ take $\sqrt z=\sqrt Re^{i\theta/2}$, whose imaginary part is $\sqrt R\sin(\theta/2)$, so $\abs{g(z)}\le C'e^{\pi R\sin^{2}(\theta/2)}\le C'e^{\pi R}=C'e^{\pi\abs z}$.

:::

:::

::: {.pf-step #sector}

(b) With $\alpha=\frac{\pi}{2\beta}$, $\gamma=i\pi e^{-i\alpha}/\sin\alpha$ and $F_{\beta}(z)=g(z)e^{\gamma z}$, the function $F_{\beta}$ is bounded on the sector $S_{\beta}=\{0\le\arg z\le\pi/\beta\}$, for every $\beta>1$.

::: pf-proof

$\gamma=\pi(1+i\cot\alpha)$, so $\Re\gamma=\pi$. $F_{\beta}$ is holomorphic on a neighbourhood of $S_{\beta}$ and of at most exponential growth there, and the sector has opening $\pi/\beta<\pi$, so the Phragmén–Lindelöf principle applies: it suffices to bound $F_{\beta}$ on the two boundary rays. On $z=r\ge0$, $\abs{F_{\beta}(r)}=e^{\pi r}\abs{g(r)}\le C$ by step [](#even){.pf-ref}. On $z=re^{2i\alpha}$, $\Re(\gamma e^{2i\alpha})=\pi\cos2\alpha-\pi\cot\alpha\sin2\alpha=\pi(\cos2\alpha-2\cos^{2}\alpha)=-\pi$, while the exponent of step [](#even){.pf-ref} is $\pi r\sin^{2}\alpha$; hence $\abs{F_{\beta}(re^{2i\alpha})}\le C'e^{-\pi r}e^{\pi r\sin^{2}\alpha}=C'e^{-\pi r\cos^{2}\alpha}\le C'$.

:::

:::

::: {.pf-step #halfplane}

(b) $\abs{e^{\pi z}g(z)}\le C''$ on all of $\CC$.

::: pf-proof

Let $\beta\downarrow1$: then $\alpha\downarrow\frac\pi2$, $\gamma\to i\pi\frac{e^{-i\pi/2}}{1}=\pi$, and $S_{\beta}$ increases to the open upper half-plane. For fixed $z$ in the upper half-plane, step [](#sector){.pf-ref} gives $\abs{e^{\pi z}g(z)}\le\max(C,C')$ once $\beta>1$ is close enough to $1$ that $z\in S_{\beta}$, and by continuity the bound holds in the closed upper half-plane. The same argument applied to $\overline{g(\bar z)}$ — which is again entire and satisfies the same estimates, since the estimates are invariant under conjugation — gives the bound in the closed lower half-plane. So the entire function $e^{\pi z}g(z)$ is bounded on $\CC$.

:::

:::

::: {.pf-step #liouville}

(b) $g(z)=ce^{-\pi z}$, hence $\widehat f(w)=ce^{-\pi w^{2}}$ and $f(x)=ce^{-\pi x^{2}}$.

::: pf-proof

A bounded entire function is constant by Liouville's theorem, so $e^{\pi z}g(z)=c$ and $g(z)=ce^{-\pi z}$. Substituting $z=w^{2}$ gives $\widehat f(w)=g(w^{2})=ce^{-\pi w^{2}}$. The Gaussian $e^{-\pi x^{2}}$ is its own Fourier transform in this normalisation, so Fourier inversion gives $f(x)=ce^{-\pi x^{2}}$.

:::

:::

::: {.pf-step #odd}

(c) If $f$ is odd and satisfies the two Gaussian bounds then $f=0$.

::: pf-proof

For odd $f$, $\widehat f(-\zeta)=-\widehat f(\zeta)$, so $\widehat f$ is odd and $\widehat f(0)=0$; hence $h(z)=\widehat f(z)/z$ extends to an even entire function. Near $0$ the estimate $\abs{\widehat f(z)}\le C'e^{\pi\eta^{2}}$ bounds $h$ after increasing the constant, and on the real axis $\abs{h(x)}\le Ce^{-\pi x^{2}}$ for $\abs x\ge1$ with a larger constant near $0$. So $h$ satisfies the estimates of steps [](#entire){.pf-ref} and [](#even){.pf-ref}, and the even case applies: $h(z)=ce^{-\pi z^{2}}$, that is $\widehat f(z)=cze^{-\pi z^{2}}$. But the hypothesis $\abs{\widehat f(x)}\le Ce^{-\pi x^{2}}$ on the real axis then reads $\abs c\abs x\le C$ for all real $x$, which forces $c=0$. Hence $\widehat f=0$ and, by injectivity of the Fourier transform, $f=0$.

:::

:::

::: {.pf-step #general}

(c) An arbitrary $f$ satisfying the two Gaussian bounds is a constant multiple of $e^{-\pi x^{2}}$; in particular, if $\abs{f(x)}\le Ce^{-\pi Ax^{2}}$ and $\abs{\widehat f(\xi)}\le C'e^{-\pi B\xi^{2}}$ with $AB>1$, then $f\equiv0$.

::: pf-proof

Write $f=f_{e}+f_{o}$ with $f_{e}(x)=\frac{f(x)+f(-x)}{2}$ and $f_{o}(x)=\frac{f(x)-f(-x)}{2}$; both satisfy the same two bounds, up to constants, and $\widehat f=\widehat{f_{e}}+\widehat{f_{o}}$. By step [](#odd){.pf-ref} $f_{o}=0$, and applying the even case of steps [](#entire){.pf-ref}–[](#liouville){.pf-ref} to $f_{e}$ gives $f=f_{e}=ce^{-\pi x^{2}}$. Now suppose the sharper bounds with $AB>1$ hold, and choose $\lambda>0$ with $1/A<\lambda^{2}<B$, possible because $AB>1$. Then $G(x)=f(\lambda x)$ satisfies $\abs{G(x)}\le Ce^{-\pi A\lambda^{2}x^{2}}\le Ce^{-\pi x^{2}}$ and $\widehat G(\xi)=\lambda^{-1}\widehat f(\xi/\lambda)$ satisfies $\abs{\widehat G(\xi)}\le C'\lambda^{-1}e^{-\pi B\xi^{2}/\lambda^{2}}\le C''e^{-\pi\xi^{2}}$. So $G=ce^{-\pi x^{2}}$, and then $\abs c e^{-\pi x^{2}}=\abs{G(x)}\le Ce^{-\pi A\lambda^{2}x^{2}}$ for all $x$; dividing and letting $\abs x\to\infty$ gives $c=0$ because $A\lambda^{2}>1$. Hence $f\equiv0$.

:::

:::

::: {.pf-step #conclusion}

Hardy's theorem holds, and the $AB>1$ consequence holds.

::: pf-proof

Steps [](#entire){.pf-ref}–[](#general){.pf-ref} show that a function with $\abs{f(x)}=O(e^{-\pi x^{2}})$ and $\abs{\widehat f(\xi)}=O(e^{-\pi\xi^{2}})$ is a constant multiple of $e^{-\pi x^{2}}$, and that the sharper pair of bounds with $AB>1$ forces $f\equiv0$:
$$
\boxed{f=ce^{-\pi x^{2}}\ \text{under the two Gaussian bounds};\qquad f\equiv0\ \text{when } AB>1.}
$$

:::

:::

:::

:::
