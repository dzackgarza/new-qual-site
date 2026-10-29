---
schema: qual/card@1
id: P-CASP25D
kind: problem
title: Automorphisms of the punctured disk $\DD\setminus\{a\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Conformal Maps
  - Punctured Disk
relations: []
review: draft
---

::: {.problem}
Let $a \in \DD$ and set $G = \DD \setminus \{a\}$.
Find all analytic automorphisms of $G$, i.e., find all one-to-one and onto analytic functions from $G$ to $G$.
Write down the expressions for such functions (can be unsimplified).
Prove your answer.
:::

::: {.solution}
Let $F:G\to G$ be an automorphism, where
$G=\DD\setminus\{a\}$. Since $F$ is bounded, the isolated singularity
at $a$ is removable, so $F$ extends holomorphically to a map
$$
\widetilde F:\DD\to\overline{\DD}.
$$
The extension is nonconstant, hence actually maps into $\DD$ by the
maximum principle. The inverse automorphism extends similarly to
$\widetilde H:\DD\to\DD$. On the punctured disk,
$$
\widetilde H\circ\widetilde F=\operatorname{id},
\qquad
\widetilde F\circ\widetilde H=\operatorname{id},
$$
so the identity theorem makes these equalities hold on all of $\DD$.
Thus $\widetilde F$ is a disk automorphism.

Because $F$ maps $G$ onto itself, the omitted point must map to itself:
$$
\widetilde F(a)=a.
$$
Conversely every disk automorphism fixing $a$ restricts to an automorphism of
$G$.

Let
$$
\phi_a(z)=\frac{z-a}{1-\overline a z}.
$$
All disk automorphisms fixing $a$ are therefore
$$
\boxed{
F_\theta(z)
=\phi_a^{-1}\!\left(e^{i\theta}\phi_a(z)\right),
\qquad \theta\in\RR.
}
$$
:::
