---
schema: qual/card@1
id: P-CASP18C
kind: problem
title: "An analytic self-map of a simply connected region that is not the identity has at most one fixed point"
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Riemann Mapping Theorem
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The correspondence of fixed points under the Riemann-map conjugacy is now proved (a fixed point of f is a fixed point of F and conversely), the Schwarz equality case is applied with the nonzero point T(b) and the rotation forced to be 1 by evaluating at T(b) again, and the descent back to f = id is written out. No retained solution set covers the exercise; the card says the argument is its own. No statement repair.
---

::: {.problem}
Show that if $G \neq \CC$ is a simply connected subset of $\CC$, $f : G \to G$ is analytic, and $f(z)$ is not identically equal to $z$, then $f$ has at most one fixed point in $G$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #conjugate}
There is a conformal bijection $\phi:G\to\DD$, and $F=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\DD$ with the same number of fixed points as $f$.

::: pf-proof
$G$ is a simply connected proper subdomain of $\CC$, so the Riemann mapping theorem provides a conformal bijection $\phi$ onto the disc. Then $F$ is holomorphic as a composite and maps $\DD$ into $\DD$ because $f$ maps $G$ into $G$. Moreover $z$ is a fixed point of $f$ exactly when $\phi(z)$ is a fixed point of $F$: $F(\phi(z))=\phi(z)\iff\phi(f(z))=\phi(z)\iff f(z)=z$, using injectivity of $\phi$.
:::

:::

::: {.pf-step #schwarz}
If $F$ has two distinct fixed points then $F=\operatorname{id}_\DD$.

::: pf-proof
Let $a\ne b$ be fixed points of $F$ and let $T$ be a disc automorphism with $T(a)=0$, for instance $T(w)=\frac{w-a}{1-\overline a w}$. Put $H=T\circ F\circ T^{-1}$, a holomorphic self-map of $\DD$ with $H(0)=T(F(a))=T(a)=0$. Schwarz's lemma gives $\abs{H(w)}\le\abs w$ for all $w$, and $H(T(b))=T(F(b))=T(b)$, so equality $\abs{H(w)}=\abs w$ holds at the nonzero point $w=T(b)$; the equality case of Schwarz's lemma then gives $H(w)=e^{i\theta}w$ for some $\theta$. Applying this at $T(b)\ne0$ gives $e^{i\theta}T(b)=H(T(b))=T(b)$, hence $e^{i\theta}=1$ and $H=\operatorname{id}$.
:::

:::

::: {.pf-step #identity}
If $F=\operatorname{id}_\DD$ then $f=\operatorname{id}_G$.

::: pf-proof
$T\circ F\circ T^{-1}=\operatorname{id}$ gives $F=\operatorname{id}$, and then $\phi(f(\phi^{-1}(w)))=w$ for all $w$, so $f(\phi^{-1}(w))=\phi^{-1}(w)$; since $\phi^{-1}$ is onto $G$, $f=\operatorname{id}_G$, contrary to the hypothesis.
:::

:::

::: {.pf-step}
$f$ has at most one fixed point in $G$.

::: pf-proof
If $f$ had two distinct fixed points, then $F$ would have two distinct fixed points by step [](#conjugate){.pf-ref}, whence $F=\operatorname{id}$ by step [](#schwarz){.pf-ref} and $f=\operatorname{id}_G$ by step [](#identity){.pf-ref}, contradicting the hypothesis.
:::

:::

:::
:::
