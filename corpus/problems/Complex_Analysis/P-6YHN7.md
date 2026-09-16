---
schema: qual/card@1
id: P-6YHN7
kind: problem
title: Schwarz lemma and $g(\{|z|<r\})\subseteq f(\{|z|<r\})$ for holomorphic $f,g:\DD\to\Omega$
  with $f$ injective and $f(0)=g(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Biholomorphisms
  - Conformal Maps
relations: []
review: draft
---

::: {.problem}
Suppose $f, g: \DD\to \Omega$ are holomorphic with $f$ injective and $f(0) = g(0)$.

Show that 
\[  
\Forall 0 < r < 1,\qquad g\qty{\theset{\abs{z} < r}} \subseteq f\qty{\theset{\abs{z} < r}}
.\]

> The first part of this problem asks for a statement of the Schwarz lemma.
:::

::: {.solution}
The statement is false as written. Take $\Omega=\DD$,
\[
f(z)=\frac z2,
\qquad
 g(z)=z.
\]
Then $f$ is injective and $f(0)=g(0)=0$, but for every $0<r<1$,
\[
g(\{|z|<r\})=\{|w|<r\}\not\subseteq\{|w|<r/2\}
=f(\{|z|<r\}).
\]

The natural Schwarz-lemma version is true if $f$ is a biholomorphism
$\DD\to\Omega$. Then
\[
h=f^{-1}\circ g:\DD\to\DD
\]
is holomorphic and fixes $0$. By Schwarz's lemma, $|h(z)|\le |z|$, hence
$h(\{|z|<r\})\subseteq\{|z|<r\}$ for every $0<r<1$. Applying $f$ gives
\[
g(\{|z|<r\})
=f(h(\{|z|<r\}))
\subseteq f(\{|z|<r\}).
\]
:::
