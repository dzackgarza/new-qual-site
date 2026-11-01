---
schema: qual/card@1
id: E-SS8.PR-6
kind: problem
title: Boundary extension for a Jordan domain
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 6, and with
    Exercise 18 of the same chapter, both read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card's one sentence matches the
    print; the book gives no proof and says only that further ideas are required.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Scope stated exactly, because this problem *is* the classical boundary-extension theorem and the
    book offers no proof. **Proved here:** that a conformal map onto a bounded domain has
    $\int\!\!\int_\DD\abs{F'}^2=\operatorname{Area}(\Omega)<\infty$ and hence the small-oscillation
    property along circular arcs used in Exercise 18, so that the piecewise-smooth hypothesis is not
    needed for that step; that a continuous extension which is injective on $\partial\DD$ is
    automatically a bijection $\overline\DD\to\overline\Omega$; and the uniqueness of the extension.
    **Cited, not reproved:** the existence of the continuous injective extension for a merely
    continuous Jordan boundary, which is Carathéodory's theorem (C. Carathéodory, Math. Ann. 73
    (1913), 305--320); its hypotheses, that $\Omega$ is the interior of a Jordan curve and hence is
    bounded and simply connected, are checked against the book's Jordan curve theorem. The step of
    Exercise 18 that fails without smoothness is named. No correction to the printed statement is
    claimed.
---

::: {.exercise}
The results of [[E-SS8.EX-18|Exercise 18]] extend to the case when $\gamma$ is assumed merely to be closed, simple, and continuous. The proof requires further ideas.
:::

::: {.solution}

Let $\gamma$ be a closed, simple, continuous curve and $\Omega$ its interior, so that $\partial\Omega=\gamma$; let $\DD$ be the unit disc and $F:\DD\to\Omega$ a conformal map. Exercise 18 proves that $F$ extends to a continuous bijection $\overline\DD\to\overline\Omega$ when $\gamma$ is piecewise smooth. The claim here is the same conclusion for a merely continuous $\gamma$.

::: pf

::: {.pf-step #s1}

$\Omega$ is bounded and simply connected, and $\displaystyle\int\!\!\int_\DD\abs{F'(z)}^2\,dx\,dy=\operatorname{Area}(\Omega)<\infty$.

::: pf-proof

$\gamma$ is the image of a compact interval, hence bounded, so $\Omega\subseteq\{\abs{w}\le\max_\gamma\abs{w}\}$ is bounded. By the Jordan curve theorem (Book I, Chapter 2) $\gamma$ separates the plane into exactly two components, whose union with $\gamma$ is $\CC$; the interior $\Omega$ is one of them, and it is simply connected: a loop in $\Omega$ does not meet $\gamma$, so its winding number about any point of the exterior component is $0$, and $\Omega$ is its own universal cover.

For the integral: $F$ is a bijection of $\DD$ onto $\Omega$ and $F'$ is holomorphic, so $\abs{F'}^2=\abs{F'}^2$ is the integrand of the area formula in the form $\operatorname{Area}(F(E))=\int\!\!\int_E\abs{F'(z)}^2dx\,dy$ for $E\subseteq\DD$; taking $E=\DD$ gives $\operatorname{Area}(\Omega)<\infty$ and the integral is finite.

:::

:::

::: {.pf-step #s2}

For every $\zeta_0\in\partial\DD$ and every $\varepsilon>0$ there are radii $r_n\downarrow0$ such that the oscillation of $F$ on $A_{r_n}=\{\zeta:\abs{\zeta-\zeta_0}=r_n\}\cap\DD$ is less than $\varepsilon$.

::: pf-proof

This is the area argument of Exercise 18, and it uses only step [](#s1){.pf-ref}. For $z,z'\in A_r$ joined by the arc of $A_r$ inside $\DD$, Cauchy--Schwarz gives
$$
\abs{F(z)-F(z')}^2\le2\pi r\int_{A_r}\abs{F'(\zeta)}^2\,\abs{d\zeta}.
$$
If for every sufficiently small $r$ some pair in $A_r$ had images at distance $\ge\varepsilon$, then $\int_{A_r}\abs{F'}^2\abs{d\zeta}\ge\varepsilon^2/(2\pi r)$ for those $r$, and integrating $dr/r$,
$$
\int\!\!\int_\DD\abs{F'}^2dx\,dy=\int_0^1\frac{dr}{r}\int_{A_r}\abs{F'}^2\abs{d\zeta}\ge\frac{\varepsilon^2}{2\pi}\int\frac{dr}{r}=\infty,
$$
contradicting step [](#s1){.pf-ref}. So such radii $r_n\downarrow0$ exist at every $\zeta_0$.

:::

:::

::: {.pf-step #s3}

Carathéodory's theorem (cited). If $\Omega$ is a Jordan domain, that is the interior of a simple closed curve, and $F:\DD\to\Omega$ is conformal, then $F$ extends to a homeomorphism of $\overline\DD$ onto $\overline\Omega$.

::: pf-proof

This is the classical extension theorem of C. Carathéodory, *Über die gegenseitige Beziehung der Ränder bei der konformen Abbildung des Inneren einer Jordanschen Kurve auf einen Kreis*, Math. Ann. **73** (1913), 305--320; it is reproduced, for instance, in the standard treatments of the boundary behaviour of conformal maps. It is not reproved here.

Its hypotheses are exactly the ones in force: $\Omega$ is the interior of a simple closed curve, hence a Jordan domain, and by step [](#s1){.pf-ref} it is bounded and simply connected, so the Riemann mapping theorem provides the conformal $F$, and the theorem applies to it. The proof uses, in place of the tangent-line argument available for a piecewise-smooth boundary, the following idea: step [](#s2){.pf-ref} shows that the cluster set of $F$ at any $\zeta_0\in\partial\DD$, that is $\bigcap_{\delta>0}\overline{F(\DD\cap\{\abs{\zeta-\zeta_0}<\delta\})}$, is a single point of $\partial\Omega$; connectivity of the cluster sets and the fact that their intersection with $\partial\Omega$ is connected in a simple closed curve then give continuity of the extension, and injectivity on $\partial\DD$ gives the homeomorphism.

:::

:::

::: {.pf-step #s4}

Consequently the conclusion of Exercise 18 holds for a merely continuous Jordan boundary: the extension is a continuous bijection of $\overline\DD$ onto $\overline\Omega$ with continuous inverse.

::: pf-proof

By step [](#s3){.pf-ref} there is a homeomorphism $F^*:\overline\DD\to\overline\Omega$ extending $F$. A homeomorphism is in particular a continuous bijection with continuous inverse, which is precisely the conclusion of Exercise 18.

The two properties used there can also be checked directly from the pieces: $F^*$ agrees with $F$ on $\DD$, so $F^*(\DD)=\Omega$; its restriction to $\partial\DD$ is continuous and injective, and its image is compact, hence closed; and since $\overline\Omega$ is the closure of $F(\DD)$, the image of $\partial\DD$ must contain every boundary point of $\Omega$, so $F^*(\partial\DD)=\partial\Omega$ and $F^*$ is surjective.

:::

:::

::: {.pf-step #s5}

The extension is unique, and nothing assumes smoothness of $\gamma$.

::: pf-proof

Any continuous extension of $F$ to $\overline\DD$ is determined on $\DD$ by $F$ and on $\partial\DD$ by continuity, since every boundary point is a limit of interior points. Hence two such extensions coincide.

The only step of Exercise 18's proof that used piecewise smoothness was the verification, at each $w_0\in\partial\Omega$, that for small $r$ the set $\Omega\cap\{\abs{w-w_0}=r\}$ is a single arc; that assertion was used there to control the oscillation of $F$ near a boundary point of $\DD$, which is what step [](#s2){.pf-ref} supplies here without any hypothesis on $\gamma$. What smoothness gave was the existence of a tangent line; for a merely continuous Jordan curve no tangent need exist at a boundary point, and the extension is instead obtained from the cluster-set argument quoted in step [](#s3){.pf-ref}.

:::

:::

:::

:::
