---
schema: qual/card@1
id: P-4PTIX
kind: problem
title: Fixed points of holomorphic self-maps of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
solved: true
---

::: problem
Let $g$ be analytic for $|z|\leq 1$ and $|g(z)| < 1$ for $|z| = 1$.

-   Show that $g$ has a unique fixed point in $|z| < 1$.

-   What happens if we replace $|g(z)| < 1$ with $|g(z)|\leq 1$ for
    $|z|=1$? Give an example if (a) is not true or give an proof
    if (a) is still true.


-   What happens if we simply assume that $f$ is analytic for
    $|z| < 1$ and $|f(z)| < 1$ for $|z| < 1$? Suppose that $f(z)
    \not\equiv  z$. Can f have more than one fixed point in
    $|z| < 1$?

> Hint: The map
$\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
> may be useful.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $g$ be analytic on $|z| \le 1$ with $|g(z)| < 1$ for $|z| = 1$. (a) Show $g$ has a unique fixed point in $|z| < 1$. (b) What changes if $|g(z)| \le 1$ on $|z| = 1$? (c) If $f$ is analytic on $|z| < 1$ with $|f(z)| < 1$ and $f \not\equiv z$, can $f$ have more than one fixed point in $|z| < 1$?

<1>1. (a) Setup: apply Rouch\'e to $g(z) - z$ on $|z| = 1$.
<2>1. On $|z| = 1$, $|g(z)| < |z| = 1$.
    Proof: given $|g(z)| < 1$ on $|z| = 1$.
<2>2. $g(z) - z$ and $-z$ have the same number of zeros in $|z| < 1$.
    Proof: Rouch\'e's theorem with $f(z) = -z$ and $g$ as perturbation: $|g(z)| < |{-z}|$ on $|z| = 1$ by <2>1, and $(g - z) = (-z) + g$.
<2>3. $g$ has exactly one fixed point in $|z| < 1$.
    Proof: $-z$ has exactly one zero (at $z = 0$, simple) in $|z| < 1$; by <2>2, $g(z) - z$ has exactly one zero (counting multiplicity) there.

<1>2. (b) With $|g(z)| \le 1$ on $|z| = 1$, the conclusion of (a) may fail.
    Proof: example $g(z) = \tfrac{z+1}{2}$: $|g(z)| \le \tfrac{|z|+1}{2} = 1$ on $|z| = 1$ (equality at $z = 1$), but the only fixed point solves $z = \tfrac{z+1}{2}$, i.e. $z = 1$, which lies on $|z| = 1$, not in $|z| < 1$. So $g$ has no fixed point in the open disk.

<1>3. (c) No: a non-identity analytic map $f: D \to D$ has at most one fixed point in $D$.
<2>1. Recall the Schwarz--Pick inequality: for $a, b \in D$, $\rho(f(a), f(b)) \le \rho(a, b)$ for the hyperbolic distance $\rho$, with strict inequality if $f$ is not an automorphism.
    Proof: standard form of Schwarz--Pick.
<2>2. If $f$ had two distinct fixed points $a, b \in D$, then $f$ must be an automorphism.
    Proof: $\rho(a, b) = \rho(f(a), f(b)) \le \rho(a, b)$; equality in <2>1 forces $f \in \Aut(D)$.
<2>3. A non-identity automorphism of $D$ has exactly one fixed point in $D$.
    Proof: writing $\psi(z) = e^{i\theta}\frac{z - \alpha}{1 - \bar\alpha z}$, the fixed-point equation is a quadratic with product of roots of modulus $|\alpha| < 1$, so exactly one root lies in $D$ (or, for $\alpha = 0$, the only fixed point in $D$ is $0$ unless $\psi$ is the identity).
<2>4. Conclusion for (c).
    Proof: if $f \not\equiv z$ had two fixed points, <2>2 makes $f$ a non-identity automorphism, contradicting <2>3; hence at most one fixed point.

<1>4. Q.E.D.
    Proof: <1>1 proves (a); <1>2 answers (b) with an example; <1>3 answers (c).
:::
