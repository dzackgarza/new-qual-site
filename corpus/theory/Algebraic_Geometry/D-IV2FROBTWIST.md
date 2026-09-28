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
The \dfn{Frobenius morphism} $F : X \to X$ is the identity on the underlying topological space, with
$$
F^\sharp : \OO_X \to \OO_X, \qquad f \mapsto f^p .
$$
This is a ring homomorphism in characteristic $p$, so $F$ is a morphism of schemes.
:::

::: {.definition title="The twist and the $k$-linear Frobenius"}
For $X$ over $k$ with structure morphism $\pi : X \to \Spec k$, let $X_p$ denote $X$ with the structure morphism twisted by Frobenius, so that $k$ acts on $\OO_{X_p}$ through $p$-th powers.
Then $F$ becomes a $k$-morphism
$$
F' : X_p \to X ,
$$
the \dfn{$k$-linear Frobenius}. For $X$ a curve over perfect $k$ it is finite of degree $p$, and on function fields it is the inclusion
$$
k(X) \subseteq k(X)^{1/p} .
$$
:::

::: {.remark title="Effect of the twist"}
The absolute $F$ is not a morphism over $k$ unless $k=\FF_p$: $F^\sharp$ sends $\lambda \in k$ to $\lambda^p$, so $\pi\circ F=\operatorname{Frob}_{\Spec k}\circ\pi$, where $\operatorname{Frob}_{\Spec k}$ is the Frobenius of $\Spec k$.
Over $k=\FF_p$ the Frobenius of $\Spec k$ is the identity, so $F=F'$.
In $X_p$ the $k$-structure is composed with the $p$-th power map of $k$, so $\pi\circ F'$ is the structure morphism of $X_p$ and $F'$ is a morphism over $\Spec k$.

The extension $k(X)^{1/p}/k(X)$ has degree $p$: $k(X)$ has transcendence degree $1$ over the perfect field $k$, so $k(X)^{1/p}$ is generated over $k(X)$ by the $p$-th root of a separating transcendental element.
For $X=\PP^1$, this is $k(t) \subseteq k(t^{1/p})$, of degree $p$ since $t^{1/p}$ is a root of the irreducible polynomial $T^p-t$.

Twisting applies the Frobenius of $k$ to the coefficients of the defining equations, so $X_p \cong X$ over $k$ whenever $X$ is defined over $\FF_p$, for instance $X = \AA^1$.
For $k$ algebraically closed and an elliptic curve $E$ over $k$, the twist replaces $j(E)$ by a $p$-th power or $p$-th root of it, so $E_p \cong E$ over $k$ if and only if $j(E)^p=j(E)$, that is, $j(E) \in \FF_p$; a curve with $j(E)\notin\FF_p$ has $E_p\not\cong E$.
:::

::: {.remark title="Absolute versus relative Frobenius"}
The absolute Frobenius of $\PP^n$ is finite, flat, bijective, and nowhere smooth, because $d(t^p) = 0$ ([[FE-MORFROB]]).
The same identity $d(t^p)=0$ shows that $k(X)^{1/p}/k(X)$ is purely inseparable, which [[PR-IV2INSEP]] uses.
:::
