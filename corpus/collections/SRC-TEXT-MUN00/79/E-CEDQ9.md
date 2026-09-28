---
schema: qual/card@1
id: E-CEDQ9
kind: problem
title: Maps of higher spheres into the circle are nulhomotopic
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.exercise}

Show that if $n > 1$, every continuous map $f: S^n \to S^1$ is nulhomotopic.
[Hint: Use the lifting lemma.]
:::

::: {.solution}
Let \(n>1\) and \(f:S^n\to S^1\). Choose a basepoint \(x_0\in S^n\), and let
\[
p:\mathbb R\longrightarrow S^1,\qquad p(t)=e^{2\pi i t}
\]
be the universal covering map. Since \(S^n\) is simply connected for \(n>1\),
\[
f_*\pi_1(S^n,x_0)=0\subset p_*\pi_1(\mathbb R,\tilde b_0)=0.
\]
The lifting criterion therefore gives a lift
\[
\tilde f:S^n\to\mathbb R,\qquad p\tilde f=f.
\]
Because \(\mathbb R\) is contractible, \(\tilde f\) is homotopic to a constant map. Composing this homotopy with \(p\) gives a homotopy of \(f\) to a constant map in \(S^1\). Hence every map \(S^n\to S^1\) is nullhomotopic.
:::
