---
schema: qual/card@1
id: P-MMAQ-V6VSLM2FBW
kind: problem
title: a. Let $\mu$ be a measure on a measurable space $(X, \mathcal M)$…
classification:
  areas:
  - real-analysis
  topics:
  - radon-nikodym
  - measure-theory
relations: []
review: draft
---

::: problem
a.  Let $\mu$ be a measure on a measurable space $(X, \mathcal M)$ and $f$ a positive measurable function.

Define a measure $\lambda$ by
$$
\lambda(E):=\int_{E} f ~d \mu, \quad E \in \mathcal{M}
$$

Show that for $g$ any positive measurable function,
$$
\int_{X} g ~d \lambda=\int_{X} f g ~d \mu
$$

b.  Let $E \subset \RR$ be a measurable set such that
    $$
    \int_{E} x^{2} ~d m=0.
    $$
    Show that $m(E) = 0$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) If $\lambda(E) = \int_E f ~d\mu$ for positive measurable $f$, prove $\int_X g ~d\lambda = \int_X fg ~d\mu$ for every positive measurable $g$. (b) If $E \subseteq \RR$ is measurable with $\int_E x^2 ~dm = 0$, prove $m(E) = 0$.

<1>1. Proof of (a) for simple functions.
    <2>1. It suffices to prove the identity for nonnegative simple functions $g = \sum_{j=1}^J c_j \chi_{E_j}$ with $c_j \geq 0$ and $E_j$ measurable.
        Proof: Every positive measurable $g$ is the pointwise limit of an increasing sequence of nonnegative simple functions; the identity then extends by monotone convergence (<1>2).
    <2>2. For $g = \sum_j c_j \chi_{E_j}$,
        $$\int_X g ~d\lambda = \sum_j c_j \lambda(E_j) = \sum_j c_j \int_{E_j} f ~d\mu = \sum_j c_j \int_X f \chi_{E_j} ~d\mu = \int_X f \left(\sum_j c_j \chi_{E_j}\right) ~d\mu = \int_X f g ~d\mu.$$
        Proof: First equality: linearity of the integral against $\lambda$. Second: definition of $\lambda$ (applied to each measurable $E_j$). Third and fourth: linearity of the integral against $\mu$ and regrouping.
    <2>3. Q.E.D.
        Proof: This proves (a) for simple functions.

<1>2. Extension to all positive measurable $g$.
    <2>1. For $g \geq 0$ measurable, choose simple $g_k$ with $0 \leq g_k \uparrow g$ pointwise.
        Proof: Standard approximation of nonnegative measurable functions by simple functions.
    <2>2. $\int_X g_k ~d\lambda = \int_X f g_k ~d\mu$ for each $k$, by <1>1.
        Proof: Apply the simple-function identity to $g_k$.
    <2>3. Both sides converge: $\int_X g_k ~d\lambda \uparrow \int_X g ~d\lambda$ and $\int_X f g_k ~d\mu \uparrow \int_X fg ~d\mu$.
        Proof: Monotone convergence theorem applied to $g_k \uparrow g$ against $\lambda$; and to $f g_k \uparrow f g$ (nonnegative, $f \geq 0$) against $\mu$.
    <2>4. Hence $\int_X g ~d\lambda = \int_X fg ~d\mu$.
        Proof: Take limits in <2>2 using <2>3.
    <2>5. Q.E.D.
        Proof: This proves (a).

<1>3. Proof of (b).
    <2>1. The integrand $x^2$ is nonnegative on $E$, so $\int_E x^2 ~dm = 0$ implies $x^2 = 0$ for $m$-almost every $x \in E$.
        Proof: A nonnegative measurable function with zero integral is zero almost everywhere on the set of integration (standard lemma: $\{x^2 > 0\} = \bigcup_n \{x^2 \geq 1/n\}$, and each piece must have measure $0$).
    <2>2. $x^2 = 0$ iff $x = 0$, so $E \setminus \{0\}$ is a null set.
        Proof: $x^2 = 0 \iff x = 0$; by <2>1, $m(E \cap \{x^2 > 0\}) = 0$ and $E \cap \{x^2 > 0\} = E \setminus \{0\}$.
    <2>3. $m(E) = m(E \cap \{0\}) + m(E \setminus \{0\}) = 0 + 0 = 0$.
        Proof: $\{0\}$ is a single point, hence null; $E \setminus \{0\}$ is null by <2>2; a subset of a null set is null.
    <2>4. Q.E.D.
        Proof: This proves (b).
:::
