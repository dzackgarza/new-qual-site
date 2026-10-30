---
schema: qual/card@1
id: E-SS8.EX-12
kind: problem
title: Fixed points of holomorphic self-maps of the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Fixed Points
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
A complex number $w \in \DD$ is a fixed point for the map $f : \DD \to \DD { \mathrm { i f ~ } } f ( w ) = w$

(a) Prove that if $f : \DD \to \DD$ is analytic and has two distinct fixed points, then f is the identity, that is, $f ( z ) = z { \mathrm { ~ f o r } }$ all $z \in \DD$

(b) Must every holomorphic function $f : \DD \to \DD$ have a fixed point?
[Hint: Consider the upper half-plane.]
:::

::: {.solution}
For part (a), let $a,b\in\DD$ be distinct fixed points of $f$. Choose a disc automorphism $\phi$ with $\phi(a)=0$ and define
$$
g=\phi\circ f\circ\phi^{-1}.
$$
Then $g:\DD\to\DD$ is holomorphic, $g(0)=0$, and $c=\phi(b)\ne0$ is another fixed point. Schwarz's lemma gives $\abs{g(z)}\le\abs{z}$. Since $\abs{g(c)}=\abs{c}$ for $c\ne0$, the equality case of Schwarz's lemma implies
$$
g(z)=e^{i\theta}z
$$
for some real $\theta$. But $g(c)=c$ and $c\ne0$, so $e^{i\theta}=1$. Hence $g$ is the identity, and therefore so is $f$.

For part (b), no. Let
$$
\phi(z)=\frac{z-i}{z+i}
$$
map the upper half-plane biholomorphically onto $\DD$, and let $T(z)=z+1$, an automorphism of the upper half-plane with no fixed point there. Then
$$
F=\phi\circ T\circ\phi^{-1}:\DD\to\DD
$$
is a holomorphic self-map. If $F(w)=w$, then applying $\phi^{-1}$ would give a fixed point of $T$, impossible. Thus a holomorphic self-map of the disc need not have a fixed point.
:::
