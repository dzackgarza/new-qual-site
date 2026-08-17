---
schema: qual/card@1
id: P-7UD7E
kind: problem
title: Borel measurability of distribution functions and $\int|f|=\int_0^\infty(\phi+\psi)\,d\lambda$
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Let $(X, \mathcal M, \mu)$ be a measure space.
For $f\in L^1(\mu)$ and $\lambda > 0$, define
$$
\phi(\lambda)=\mu(\{x \in X | f(x)>\lambda\}) 
\quad \text { and } \quad 
\psi(\lambda)=\mu(\{x \in X | f(x)<-\lambda\})
$$

Show that $\phi, \psi$ are Borel measurable and
$$
\int_{X}|f| ~d \mu=\int_{0}^{\infty}[\phi(\lambda)+\psi(\lambda)] ~d \lambda
$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\phi$ and $\psi$ are Borel measurable functions of $\lambda \in (0, \infty)$.
Proof: $\lambda \mapsto \mu\{f > \lambda\}$ is decreasing (if $\lambda_1 < \lambda_2$ then $\{f > \lambda_1\} \supseteq \{f > \lambda_2\}$); decreasing (indeed monotone) functions are Borel measurable; likewise $\psi$ is decreasing.

<1>2. $\int_0^\infty \mu\{|f| > \lambda\}\,d\lambda = \int_X |f|\,d\mu$.
<2>1. Write $\mu\{|f| > \lambda\} = \int_X \chi_{\{|f(x)| > \lambda\}}\,d\mu(x)$.
Proof: definition of the measure of a set.
<2>2. Interchange: $\int_0^\infty\int_X \chi_{\{|f| > \lambda\}}\,d\mu(x)\,d\lambda = \int_X \int_0^\infty \chi_{\{|f(x)| > \lambda\}}\,d\lambda\,d\mu(x)$.
Proof: Tonelli — the integrand is non-negative and measurable.
<2>3. $\int_0^\infty \chi_{\{|f(x)| > \lambda\}}\,d\lambda = |f(x)|$ for every $x$.
Proof: the inner integral is the length of $\{\lambda > 0 : \lambda < |f(x)|\} = (0, |f(x)|)$.
<2>4. Q.E.D. Proof: <2>2 and <2>3 give $\int_0^\infty\mu\{|f|>\lambda\}d\lambda = \int_X|f|d\mu$.

<1>3. $\{|f| > \lambda\} = \{f > \lambda\} \cup \{f < -\lambda\}$, a disjoint union, so $\mu\{|f| > \lambda\} = \phi(\lambda) + \psi(\lambda)$.
Proof: $|f(x)| > \lambda \iff f(x) > \lambda$ or $f(x) < -\lambda$, and the two sets are disjoint.

<1>4. Q.E.D. Proof: <1>2 and <1>3 give $\int_X|f|\,d\mu = \int_0^\infty[\phi(\lambda) + \psi(\lambda)]\,d\lambda$.
:::
