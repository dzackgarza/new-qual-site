---
schema: qual/card@1
id: D-IV2FROBTWIST
kind: definition
title: The $k$-linear Frobenius and the Frobenius twist
classification:
  areas:
  - algebraic-geometry
  topics:
  - Frobenius
  - Purely Inseparable Extensions
  - Curves
relations:
- kind: related-to
  target: FE-MORFROB
review: draft
prompts:
- Define the Frobenius morphism of a scheme of characteristic $p$.
- Why is it not a morphism of $k$-schemes, and how is that fixed?
- What is the degree of the $k$-linear Frobenius, and which field extension does it induce?
- When is $X_p \cong X$ over $k$?
---

::: {.definition title="Absolute Frobenius"}
Let $X$ be a scheme all of whose local rings contain $\FF_p$.
The **Frobenius morphism** $F : X \to X$ is the identity on the underlying topological space, with
\[
F^\sharp : \OO_X \to \OO_X, \qquad f \mapsto f^p .
\]
This is a ring homomorphism in characteristic $p$, so $F$ is a morphism of schemes.
:::

::: {.definition title="The twist and the $k$-linear Frobenius"}
For $X$ over $k$ with structure morphism $\pi : X \to \Spec k$, let $X_p$ denote $X$ with the structure morphism twisted by Frobenius, so that $k$ acts on $\OO_{X_p}$ through $p$-th powers.
Then $F$ becomes a $k$-morphism
\[
F' : X_p \to X ,
\]
the **$k$-linear Frobenius**. For $X$ a curve over perfect $k$ it is finite of degree $p$, and on function fields it is the inclusion
\[
k(X) \subseteq k(X)^{1/p} .
\]
:::

::: {.remark title="What the twist is for"}
The absolute $F$ is not a morphism over $k$: $F^\sharp$ sends $\lambda \in k$ to $\lambda^p$, so the triangle over $\Spec k$ does not commute, and instead $F$ sits in a square with the Frobenius of $\Spec k$ itself.
Over $k = \FF_p$ nothing happens and the distinction is invisible, which is why it is easy to miss and easy to be asked about.
Twisting the structure map is the minimal repair: absorb the $p$-th power action of $k$ into the source, and what was a square becomes a triangle.

The degree is $p$ and not something else because $k(X)$ has a $p$-basis of one element: it has transcendence degree $1$ over the perfect field $k$, so $k(X)^{1/p}$ is generated over $k(X)$ by the $p$-th root of a separating variable.
Concretely $k(t) \subseteq k(t^{1/p})$, and $(t^{1/p})^p = t$ makes this degree exactly $p$.

Twisting applies the Frobenius of $k$ to the coefficients of the defining equations, so $X_p \cong X$ over $k$ whenever $X$ is defined over $\FF_p$ — for instance $X = \AA^1$, which answers the first half of Hartshorne's exercise.
It fails in general: for an elliptic curve the twist changes $j$ by a $p$-th power, so $E_p \cong E$ over $k$ exactly when $j(E) \in \FF_p$, and a curve with $j$ transcendental over $\FF_p$ is the counterexample.
:::

::: {.remark title="Against the other Frobenius card"}
[[FE-MORFROB]] is a different statement about the same map and the two are routinely confused.
That card is about the *absolute* Frobenius of $\PP^n$ as a counterexample: finite, flat, bijective, and nowhere smooth, because $d(t^p) = 0$.
This card is about making Frobenius a morphism over $k$ at all, and about the degree-$p$ field extension it induces, which is what [[PR-IV2INSEP]] runs on.
The shared computation $d(t^p) = 0$ is why both stories exist: it is simultaneously the failure of smoothness and the inseparability of the field extension.
:::
