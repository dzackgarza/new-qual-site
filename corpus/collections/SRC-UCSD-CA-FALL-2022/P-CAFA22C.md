---
schema: qual/card@1
id: P-CAFA22C
kind: problem
title: "Punctured disk and annulus are not conformally equivalent"
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
    Lamport structure, and the argument replaced. The prose's "contradiction" was not one: it said that an interior value of F-tilde(0) "would violate injectivity" and that a value on a boundary circle "would put values with modulus < 1 or > 2 in the image", neither of which it derived, and the parenthetical about zeros of F-tilde - F-tilde(0) is not an argument. The card now runs: removable singularity (F bounded), open mapping theorem to see F-tilde(D) = A u {c} is open, so c cannot lie on the boundary circle (a boundary point has no neighbourhood inside the closed annulus), whence c is in A and F-tilde(D) = A; then G o F-tilde is holomorphic on D and equals the identity off 0, so it is the identity everywhere by the identity theorem, making F-tilde a homeomorphism of D onto A; that is impossible because D is simply connected and A is not (the loop |w| = 3/2 has nonzero integral of dw/w, so it is not nullhomotopic). No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Show that the punctured unit disk $\DD^* = \DD \setminus \{0\}$ and the annulus $A = \{z : 1 < \abs{z} < 2\}$ are not conformally equivalent.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Suppose, for contradiction, that $F:\DD^*\to A$ is a biholomorphism, where $\DD^*=\DD\setminus\{0\}$ and $A=\{1<\abs w<2\}$. Write $\overline A=\{1\le\abs w\le2\}$ and $c=\widetilde F(0)$ in the notation below.

::: pf

::: {.pf-step #extend}
$F$ extends to a holomorphic $\widetilde F:\DD\to\CC$ with $\widetilde F=F$ on $\DD^*$, and $c=\widetilde F(0)$ lies in $\overline A$.

::: pf-proof
$F$ is bounded, since $F(\DD^*)=A\subseteq\{\abs w<2\}$, so the isolated singularity at $0$ is removable: $\widetilde F$ exists and is holomorphic on $\DD$. Choose $z_n\in\DD^*$ with $z_n\to0$; then $\widetilde F(z_n)=F(z_n)\in A$ and $\widetilde F(z_n)\to c$, so $c\in\overline A$ because $\overline A$ is closed.
:::

:::

::: {.pf-step #image}
$\widetilde F$ is nonconstant, and $\widetilde F(\DD)=A\cup\{c\}$ is an open set.

::: pf-proof
$F$ is a bijection onto $A$, so it is nonconstant; a holomorphic function agreeing with it off $0$ is then nonconstant too. Since $\DD$ is a nonempty open connected set and $\widetilde F$ is nonconstant holomorphic, $\widetilde F(\DD)$ is open (open mapping theorem). Finally $\DD=\DD^*\cup\{0\}$, so $\widetilde F(\DD)=\widetilde F(\DD^*)\cup\{c\}=A\cup\{c\}$.
:::

:::

::: {.pf-step #cinA}
$c\in A$, hence $\widetilde F(\DD)=A$.

::: pf-proof
$\overline A=A\cup\partial\overline A$ with $A$ the interior of $\overline A$. If $c\in\partial\overline A$, then, $\widetilde F(\DD)=A\cup\{c\}$ being open, there is $\rho>0$ with the disc $B(c,\rho)$ contained in $A\cup\{c\}\subseteq\overline A$; but every neighbourhood of a boundary point of $\overline A$ meets $\CC\setminus\overline A$, a contradiction. So $c\notin\partial\overline A$; combined with $c\in\overline A$ from step [](#extend){.pf-ref}, this gives $c\in A$.
:::

:::

::: {.pf-step #inverse}
Let $G=F^{-1}:A\to\DD^*$. Then $G\circ\widetilde F=\operatorname{id}_\DD$ and $\widetilde F\circ G=\operatorname{id}_A$.

::: pf-proof
$G$ is holomorphic because $F$ is a biholomorphism. Since $\widetilde F(\DD)=A$ by step [](#cinA){.pf-ref}, the composite $G\circ\widetilde F$ is defined and holomorphic on $\DD$. On $\DD^*$ we have $\widetilde F=F$, so $G\circ\widetilde F=\operatorname{id}$ there; $\DD^*$ is a nonempty open subset of the region $\DD$, so the identity theorem gives $G\circ\widetilde F=\operatorname{id}_\DD$. The other composite is the definition of $G$.
:::

:::

::: {.pf-step #homeo}
$\widetilde F:\DD\to A$ is a homeomorphism.

::: pf-proof
Step [](#inverse){.pf-ref} exhibits $\widetilde F$ as a bijection with inverse $G$, and both are continuous (holomorphic).
:::

:::

::: {.pf-step #contradiction}
No such $F$ exists.

::: pf-proof
$\DD$ is simply connected, being convex: the straight-line homotopy $H(z,s)=(1-s)z$ contracts every loop to a point. The annulus $A$ is not simply connected: the loop $\gamma(t)=\frac32e^{2\pi it}$ lies in $A$, and $w\mapsto1/w$ is holomorphic on $A$ with
$$
\int_\gamma\frac{dw}{w}=2\pi i\ne0,
$$
whereas Cauchy's theorem gives $\int_{h\circ\gamma}\frac{dw}{w}=0$ for any loop nullhomotopic in $A$; so $\gamma$ is not nullhomotopic. A homeomorphism carries loops to loops and homotopies to homotopies, so it preserves simple connectivity; hence $A$ would be simply connected if $\DD$ is, a contradiction. So $\DD^*$ and $A$ are not conformally equivalent.
:::

:::

:::
:::
