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
Let $\mathbb C^*=\mathbb C\cup\{\infty\}$ be the Riemann sphere, let $N<\infty$, and let $\Omega\subset\mathbb C^*$ be a domain for which $\partial\Omega$ has $N$ connected components, none of which are single points. Prove there is a conformal (i.e. one-to-one analytic) mapping from $\Omega$ onto a domain bounded by $N$ pairwise disjoint analytic Jordan curves.
:::

::: {.solution}
<1>1. The domain \(\Omega\) is a nondegenerate finitely connected domain of connectivity \(N\).

::: {.proof}
By hypothesis, \(\partial\Omega\) has exactly \(N<\infty\) connected components, so \(\Omega\) is finitely connected. The additional hypothesis that no boundary component is a singleton is exactly the nondegeneracy condition in the circle-domain theorem.
:::

<1>2. There is a conformal map \(h:\Omega\to D\) onto a circle domain \(D\subset\mathbb C^*\) whose boundary has exactly \(N\) nondegenerate round-circle components.

::: {.proof}
Koebe's circle-domain theorem says that every nondegenerate finitely connected domain is conformally equivalent to a nondegenerate circle domain of the same connectivity. Applying it to step <1>1 gives a conformal map \(h:\Omega\to D\), where every component of \(\partial D\) is a round circle and there are exactly \(N\) such components.
:::

<1>3. After postcomposing \(h\) with a Möbius transformation, every component of the image boundary is an ordinary Euclidean circle contained in \(\mathbb C\).

::: {.proof}
Choose \(p\in D\). There is a Möbius transformation \(M\) of \(\mathbb C^*\) with \(M(p)=\infty\). Since \(p\) lies in the domain rather than on its boundary, \(\infty\) belongs to \(M(D)\) and lies on none of the round circles forming \(\partial M(D)\). Möbius transformations carry generalized circles to generalized circles, so each boundary component of \(M(D)\) is therefore a round circle not containing \(\infty\), hence an ordinary Euclidean circle.
:::

<1>4. Every boundary component of \(M(D)\) is an analytic Jordan curve in the sense of the problem.

::: {.proof}
Let one such component be
\[
C=\{c+Re^{it}:0\le t<2\pi\}
\]
with \(R>0\). The affine map
\[
f(z)=c+Rz
\]
is entire and one-to-one on \(\mathbb C\), hence in particular analytic and one-to-one on every annulus \(\{r<|z|<1/r\}\) with \(0<r<1\). Moreover,
\[
f(\{|z|=1\})=C.
\]
Thus \(C\) is an analytic Jordan curve by the definition in the statement.
:::

<1>5. The map \(M\circ h\) is conformal from \(\Omega\) onto a domain bounded by \(N\) pairwise disjoint analytic Jordan curves.

::: {.proof}
Both \(h\) and \(M\) are conformal and one-to-one, so their composition is conformal and one-to-one. By steps <1>2 and <1>3, the image has exactly \(N\) pairwise disjoint round-circle boundary components, and step <1>4 shows that each of these is an analytic Jordan curve.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conformal representation.
:::
:::
