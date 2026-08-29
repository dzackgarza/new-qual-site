---
schema: qual/card@1
id: P-RAF16D
kind: problem
title: "Conditional expectation via Radon-Nikodym"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) = 1$, $\mathcal{M}_0$ a sub-$\sigma$-algebra of $\mathcal{M}$, and $\nu = \mu|_{\mathcal{M}_0}$ (the restriction of $\mu$ onto $\mathcal{M}_0$). Let $f \in L^1(\mathcal{M}, \mu)$ be real-valued.
Use the Radon-Nikodym Theorem to prove that there exists a unique $g \in L^1(\mathcal{M}_0, \nu)$ such that
$$
\int_E f\,d\mu = \int_E g\,d\nu \qquad \forall E \in \mathcal{M}_0.
$$
(Note that $g$ is, but $f$ may not be, measurable with respect to $\mathcal{M}_0$.)
:::

::: {.solution}
<1>1. Define a signed measure $\lambda$ on $\mathcal M_0$ by $\lambda(E) = \int_E f\, d\mu$ for $E \in \mathcal M_0$.
Proof: definition.

<1>2. $\lambda$ is a finite signed measure on $\mathcal M_0$.
Proof: $f \in L^1(\mu)$ and $\mu(X) = 1$, so $|\lambda(E)| \le \int |f|\, d\mu < \infty$; countable additivity follows from the dominated convergence theorem.

<1>3. $\lambda$ is absolutely continuous with respect to $\nu$.
Proof: if $\nu(E) = \mu(E) = 0$ for $E \in \mathcal M_0$, then $\lambda(E) = \int_E f\, d\mu = 0$ (the integral over a null set is $0$).

<1>4. By the Radon–Nikodym theorem, there is a unique $g \in L^1(\mathcal M_0, \nu)$ with $\lambda(E) = \int_E g\, d\nu$ for all $E \in \mathcal M_0$.
Proof: Radon–Nikodym theorem applied to <1>2 and <1>3.

<1>5. Hence $\int_E f\, d\mu = \int_E g\, d\nu$ for all $E \in \mathcal M_0$.
Proof: <1>1 and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
