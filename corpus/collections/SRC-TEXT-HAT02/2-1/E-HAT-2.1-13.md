---
schema: qual/card@1
id: E-HAT-2.1-13
kind: problem
title: Homotopic maps induce equal maps on reduced homology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Homotopy Invariance
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restricted the ordinary homology equality to the augmentation kernels defining reduced H_0; higher reduced groups equal ordinary homology.
---

Verify that $f \simeq g$ implies $f_* = g_*$ for induced homomorphisms of reduced homology groups.

::: {.solution}
Suppose
\[
f,g:X\to Y
\]
are homotopic.

<1>1. For every $n>0$,
\[
\widetilde H_n(f)=\widetilde H_n(g).
\]
::: {.proof}
For $n>0$ one has
\[
\widetilde H_n(X)=H_n(X),
\qquad
\widetilde H_n(Y)=H_n(Y).
\]
Homotopic maps induce the same homomorphism on ordinary homology, so the induced maps agree.
:::

<1>2. The same holds in degree zero.
::: {.proof}
For a nonempty space $Z$,
\[
\widetilde H_0(Z)=\ker\bigl(\epsilon:H_0(Z)\to\mathbb Z\bigr),
\]
where $\epsilon$ sends each path-component generator to $1$. Every continuous map commutes with augmentation:
\[
\epsilon\,f_* = \epsilon,
\qquad
\epsilon\,g_* = \epsilon.
\]
Since homotopic maps satisfy
\[
f_*=g_*:H_0(X)\to H_0(Y),
\]
their restrictions to the augmentation kernel are equal. These restrictions are precisely the induced maps on $\widetilde H_0$. If $X$ is empty the assertion is trivial.
:::

<1>3. Hence
\[
\boxed{f_*=g_*:\widetilde H_n(X)\to\widetilde H_n(Y)\text{ for all }n.}
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
