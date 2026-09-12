---
schema: qual/card@1
id: P-CAFA19G
kind: problem
title: "The Perron function on the punctured disk with trivial boundary data is zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
Let $G = \mathbb{D} \setminus \{0\}$ and let $f$ be the function on $\partial G$ such that $f(z) = 0$ for $|z| = 1$ and $f(0) = 1$.
Show that the Perron function $u(z)$ of $f$, $$u(z) = \sup\{\phi(z) : \phi \text{ is subharmonic and } \forall a \in \partial G,\; \limsup_{\zeta \to a} \phi(\zeta) \leq f(a)\}$$ is identically zero.

Hint: Consider the family of functions $u_\epsilon(z) = \frac{\log|z|}{\log\epsilon}$ in the annulus $\epsilon < |z| < 1$ for $\epsilon > 0$.
:::

::: solution
The zero function belongs to the Perron lower class: it is subharmonic on
$G$, has boundary limsup $0$ on $|z|=1$, and at $0$ its boundary limsup is
$0\le1$. Hence $u\ge0$.

Let $\phi$ be any function in the Perron lower class and fix $z\in G$. For
every $\eta>0$, the boundary condition at $0$ gives an $\epsilon_0>0$ such
that
\[
\phi(\zeta)\le1+\eta
\qquad(0<|\zeta|\le\epsilon_0).
\]
Choose $0<\epsilon<\min(\epsilon_0,|z|)$. On the annulus
$A_\epsilon=\{\epsilon<|\zeta|<1\}$ consider
\[
h_\epsilon(\zeta)
=(1+\eta)\frac{\log|\zeta|}{\log\epsilon}.
\]
This is harmonic, equals $1+\eta$ on $|\zeta|=\epsilon$, and equals $0$ on
$|\zeta|=1$. The boundary conditions for $\phi$ and the maximum principle for
subharmonic functions give
\[
\phi(\zeta)\le h_\epsilon(\zeta)
\qquad(\zeta\in A_\epsilon).
\]
In particular,
\[
\phi(z)\le (1+\eta)\frac{\log|z|}{\log\epsilon}.
\]
Letting $\epsilon\downarrow0$ yields $\phi(z)\le0$. Since this holds for every
admissible $\phi$, the Perron function satisfies $u(z)\le0$. Together with
$u\ge0$, this proves
\[
\boxed{u\equiv0.}
\]
:::
