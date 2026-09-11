---
schema: qual/card@1
id: E-SS8.EX-14
kind: problem
title: Conformal maps from the upper half-plane to the unit disk
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
14. Prove that all conformal mappings from the upper half-plane H to the unit disc D take the form

$$
e ^ {i \theta} \frac {z - \beta}{z - \overline {{\beta}}}, \qquad \theta \in \mathbb {R} \text {   and   } \beta \in \mathbb {H}.
$$
:::

::: solution
For $\beta\in\mathbb H$, define
\[
\phi_\beta(z)=\frac{z-\beta}{z-\overline\beta}.
\]
For $z\in\mathbb H$,
\[
|z-\beta|<|z-\overline\beta|,
\]
so $|\phi_\beta(z)|<1$. The map $\phi_\beta$ is Möbius, sends $\beta$ to $0$, and maps the real axis to the unit circle; hence it is a conformal bijection $\mathbb H\to\mathbb D$.

Now let $F:\mathbb H\to\mathbb D$ be any conformal bijection and let
\[
\beta=F^{-1}(0).
\]
Then
\[
G=F\circ\phi_\beta^{-1}:\mathbb D\to\mathbb D
\]
is an automorphism fixing $0$. By Schwarz's lemma applied to $G$ and $G^{-1}$,
\[
G(w)=e^{i\theta}w
\]
for some $\theta\in\mathbb R$. Therefore
\[
F(z)=e^{i\theta}\phi_\beta(z)
=e^{i\theta}\frac{z-\beta}{z-\overline\beta}.
\]
Conversely, every map of this form is a rotation composed with the conformal bijection $\phi_\beta$, so it maps $\mathbb H$ conformally onto $\mathbb D$.
:::
