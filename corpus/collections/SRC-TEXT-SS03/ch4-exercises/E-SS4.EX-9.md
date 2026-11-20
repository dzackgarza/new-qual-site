---
schema: qual/card@1
id: E-SS4.EX-9
kind: problem
title: Phragmén--Lindelöf theorems in a half-plane and a sector
classification:
  areas:
  - complex-analysis
  topics:
  - Phragmén–Lindelöf
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with five steps, three for (a) and two for (b), each carrying a `pf-proof`; the arguments and
    both statements are unchanged. Cited by number only: the maximum modulus principle and the
    existence of a branch of the logarithm on a simply connected domain. Checked: that
    $0<\delta<1$ keeps $\delta\theta$ inside an interval where the cosine is positive, that the
    exponent $cR^\gamma-\varepsilon R^\delta\cos(\delta\pi/2)$ tends to $-\infty$ when
    $\delta>\gamma$, and the same for the sector with $\alpha<\delta<\beta$.
---

::: {.exercise}
Here are further results similar to the Phragmén–Lindelöf theorem.

(a) Let $F$ be a holomorphic function in the right half-plane that extends continuously to the boundary, that is, the imaginary axis.
Suppose that $\abs{F(iy)} \le 1$ for all $y \in \RR$, and
$$
\abs{F(z)} \leq C e^{c\abs{z}^{\gamma}}
$$
for some $c, C > 0$ and $\gamma < 1$. Prove that $\abs{F(z)} \le 1$ for all $z$ in the right half-plane.

(b) More generally, let $S$ be a sector whose vertex is the origin, and forming an angle of $\pi/\beta$. Let $F$ be a holomorphic function in $S$ that is continuous on the closure of $S$, so that $\abs{F(z)} \le 1$ on the boundary of $S$ and
$$
\abs{F(z)} \leq C e^{c\abs{z}^{\alpha}} \quad \text{for all } z \in S
$$
for some $c, C > 0$ and $0 < \alpha < \beta$. Prove that $\abs{F(z)} \le 1$ for all $z \in S$.
:::

::: {.solution}

::: pf

::: pf-step

(a) In the right half-plane take the branch of $z^\delta$ determined by $-\frac\pi2<\arg z<\frac\pi2$, and choose $\delta$ with $\gamma<\delta<1$. If $z=re^{i\theta}$ there, then
$$
\Re(z^\delta)=r^\delta\cos(\delta\theta)\ge r^\delta\cos\frac{\delta\pi}{2}>0.
$$

::: pf-proof

Such a $\delta$ exists because $\gamma<1$, and $0<\delta<1$ keeps $\delta\theta$ in $(-\frac{\delta\pi}{2},\frac{\delta\pi}{2})\subseteq(-\frac\pi2,\frac\pi2)$, where the cosine is positive, so $\cos(\delta\theta)\ge\cos(\delta\pi/2)>0$; the branch $z^\delta=e^{\delta\log z}$ with $\log$ the principal branch is holomorphic on the right half-plane, which is simply connected and avoids the negative axis.

:::

:::

::: pf-step

(a) For $\varepsilon>0$ put $F_\varepsilon(z)=F(z)e^{-\varepsilon z^\delta}$. Then $\abs{F_\varepsilon(iy)}\le\abs{F(iy)}\le1$ on the imaginary axis, and on $\abs{z}=R$ in the closed right half-plane
$$
\abs{F_\varepsilon(z)}\le C\exp\Bigl(cR^\gamma-\varepsilon R^\delta\cos\frac{\delta\pi}{2}\Bigr)\longrightarrow0
$$
as $R\to\infty$, because $\delta>\gamma$.

::: pf-proof

On the imaginary axis $z^\delta$ has nonnegative real part by step 1, so $\abs{e^{-\varepsilon z^\delta}}=e^{-\varepsilon\Re z^\delta}\le1$ and the boundary bound follows from the hypothesis. On the semicircle $\abs{z}=R$, $\abs{F}\le Ce^{cR^\gamma}$ and $\abs{e^{-\varepsilon z^\delta}}\le e^{-\varepsilon R^\delta\cos(\delta\pi/2)}$; the exponent is $cR^\gamma-\varepsilon R^\delta\cos(\delta\pi/2)$, in which the negative term dominates because $\delta>\gamma>0$, so the exponential tends to $0$.

:::

:::

::: pf-step

(a) Hence for large $R$ the maximum principle on the right half-disc gives $\abs{F_\varepsilon}\le1$ there; letting $R\to\infty$ and then $\varepsilon\downarrow0$ gives $\abs{F(z)}\le1$ on the right half-plane.

::: pf-proof

The right half-disc $\{z:\abs{z}<R,\ \Re z>0\}$ has boundary the semicircle and the segment of the imaginary axis, and $F_\varepsilon$ is holomorphic on a neighbourhood of its closure and continuous there; the maximum modulus principle gives $\abs{F_\varepsilon}\le\max(1,\text{the semicircle bound})$, which is $1$ once $R$ is large enough. A point $z$ of the half-plane lies in this disc for all $R>\abs z$, so $\abs{F(z)}e^{-\varepsilon\Re z^\delta}=\abs{F_\varepsilon(z)}\le1$, that is $\abs{F(z)}\le e^{\varepsilon\Re z^\delta}$; letting $\varepsilon\downarrow0$ gives $\abs{F(z)}\le1$.

:::

:::

::: pf-step

(b) Rotate the sector to $S=\{z:\abs{\arg z}\le\frac{\pi}{2\beta}\}$ and choose $\alpha<\delta<\beta$. The branch $z^\delta$ is holomorphic on $S$ and
$$
\Re(z^\delta)=r^\delta\cos(\delta\theta)\ge r^\delta\cos\frac{\delta\pi}{2\beta}>0.
$$

::: pf-proof

A rotation is a biholomorphism, so it carries the theorem for the rotated sector to the original one; in the rotated position $\theta$ ranges over $[-\frac{\pi}{2\beta},\frac{\pi}{2\beta}]$ and the sector has angle $\pi/\beta$. Since $0<\alpha<\beta$, a $\delta$ strictly between them exists; then $\delta\theta\in[-\frac{\delta\pi}{2\beta},\frac{\delta\pi}{2\beta}]\subseteq(-\frac\pi2,\frac\pi2)$, so the cosine is at least $\cos\frac{\delta\pi}{2\beta}>0$. The branch is $z^\delta=e^{\delta\log z}$ with $\arg z\in(-\frac{\pi}{2\beta},\frac{\pi}{2\beta})$, which lies in an interval of length $<\pi$, so a branch of the logarithm exists on the simply connected sector.

:::

:::

::: pf-step

(b) With $F_\varepsilon=F e^{-\varepsilon z^\delta}$, the boundary rays keep the bound $\abs{F_\varepsilon}\le1$, while on the arc $\abs{z}=R$
$$
\abs{F_\varepsilon(z)}\le C\exp\Bigl(cR^\alpha-\varepsilon R^\delta\cos\frac{\delta\pi}{2\beta}\Bigr)\longrightarrow0,
$$
so the maximum principle on truncated sectors gives $\abs{F_\varepsilon}\le1$, and letting $\varepsilon\downarrow0$ proves $\abs{F(z)}\le1$ on $S$.

::: pf-proof

On each boundary ray $\Re z^\delta\ge0$ by step 4, so $\abs{e^{-\varepsilon z^\delta}}\le1$ and the hypothesis $\abs F\le1$ gives the bound. On the arc the estimate is as in (a) with $\alpha$ in place of $\gamma$ and $\frac{\delta\pi}{2\beta}$ in place of $\frac{\delta\pi}{2}$, and it tends to $0$ because $\delta>\alpha$. The truncated sector $\{z\in S:\abs{z}<R\}$ has boundary the two segments of the rays and the arc; the maximum modulus principle applied there gives $\abs{F_\varepsilon}\le1$ for large $R$, and a point of $S$ lies in the truncated sector for all large $R$, so $\abs{F(z)}\le e^{\varepsilon\Re z^\delta}$ and $\varepsilon\downarrow0$ gives the result.

:::

:::

:::
:::
