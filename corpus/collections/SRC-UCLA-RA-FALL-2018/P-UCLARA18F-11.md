---
schema: qual/card@1
id: P-UCLARA18F-11
kind: problem
title: Finitely connected domains are conformally equivalent to domains bounded by analytic Jordan curves
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 11. An analytic Jordan curve is a set of the form
\[
\Gamma=f(\{|z|=1\}),
\]
where $f$ is analytic and one-to-one on an annulus
\[
\{r<|z|<1/r\},\qquad 0<r<1.
\]
Let $\CC^*=\CC\cup\{\infty\}$ be the Riemann sphere, let $N<\infty$, and let $\Omega\subset\CC^*$ be a domain for which $\partial\Omega$ has $N$ connected components, none of which are single points. Prove there is a conformal (i.e. one-to-one analytic) mapping from $\Omega$ onto a domain bounded by $N$ pairwise disjoint analytic Jordan curves.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The domain \(\Omega\) is a nondegenerate finitely connected domain of connectivity \(N\).


::: pf-proof

By hypothesis, \(\partial\Omega\) has exactly \(N<\infty\) connected components, so \(\Omega\) is finitely connected. The additional hypothesis that no boundary component is a singleton is exactly the nondegeneracy condition in the circle-domain theorem.

:::

:::

::: {.pf-step #s1-2}

There is a conformal map \(h:\Omega\to D\) onto a circle domain \(D\subset\CC^*\) whose boundary has exactly \(N\) nondegenerate round-circle components.


::: pf-proof

Koebe's circle-domain theorem says that every nondegenerate finitely connected domain is conformally equivalent to a nondegenerate circle domain of the same connectivity. Applying it to step [](#s1-1){.pf-ref} gives a conformal map \(h:\Omega\to D\), where every component of \(\partial D\) is a round circle and there are exactly \(N\) such components.

:::

:::

::: {.pf-step #s1-3}

After postcomposing \(h\) with a Möbius transformation, every component of the image boundary is an ordinary Euclidean circle contained in \(\CC\).


::: pf-proof

Choose \(p\in D\). There is a Möbius transformation \(M\) of \(\CC^*\) with \(M(p)=\infty\). Since \(p\) lies in the domain rather than on its boundary, \(\infty\) belongs to \(M(D)\) and lies on none of the round circles forming \(\partial M(D)\). Möbius transformations carry generalized circles to generalized circles, so each boundary component of \(M(D)\) is therefore a round circle not containing \(\infty\), hence an ordinary Euclidean circle.

:::

:::

::: {.pf-step #s1-4}

Every boundary component of \(M(D)\) is an analytic Jordan curve in the sense of the problem.


::: pf-proof

Let one such component be
\[
C=\{c+Re^{it}:0\le t<2\pi\}
\]
with \(R>0\). The affine map
\[
f(z)=c+Rz
\]
is entire and one-to-one on \(\CC\), hence in particular analytic and one-to-one on every annulus \(\{r<|z|<1/r\}\) with \(0<r<1\). Moreover,
\[
f(\{|z|=1\})=C.
\]
Thus \(C\) is an analytic Jordan curve by the definition in the statement.

:::

:::

::: {.pf-step #s1-5}

The map \(M\circ h\) is conformal from \(\Omega\) onto a domain bounded by \(N\) pairwise disjoint analytic Jordan curves.


::: pf-proof

Both \(h\) and \(M\) are conformal and one-to-one, so their composition is conformal and one-to-one. By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, the image has exactly \(N\) pairwise disjoint round-circle boundary components, and step [](#s1-4){.pf-ref} shows that each of these is an analytic Jordan curve.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conformal representation.

:::

:::

:::
