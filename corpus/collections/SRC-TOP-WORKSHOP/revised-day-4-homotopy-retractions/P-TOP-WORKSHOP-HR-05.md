---
schema: qual/card@1
id: P-TOP-WORKSHOP-HR-05
kind: problem
title: No map from the torus to $S^1\vee S^1$ has a left inverse
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 5, labeled Arizona Spring 2005, in assets/attachments/day_4_homotopy_retractions.pdf.
---

::: {.problem}
Let $f:S^1\vee S^1\to T$ be a continuous map, where $T$ is the torus.
Show that there is no continuous map
\[
g:T\to S^1\vee S^1
\]
such that $f\circ g$ is the identity map on $T$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The second homology group of the wedge is
\[
H_2(S^1\vee S^1;\ZZ)=0.
\]


::: pf-proof

The space
\[
S^1\vee S^1
\]
is a $1$-dimensional CW complex: it has one $0$-cell and two $1$-cells, with no cells of dimension at least $2$.

Hence its cellular chain group in degree $2$ is
\[
C_2^{\mathrm{cell}}(S^1\vee S^1)=0.
\]
Therefore
\[
H_2(S^1\vee S^1;\ZZ)=0.
\]

:::

:::

::: {.pf-step #s1-2}

The second homology group of the torus is
\[
H_2(T;\ZZ)\cong\ZZ.
\]


::: pf-proof

Use the standard CW structure on the torus with one $0$-cell, two $1$-cells $a,b$, and one $2$-cell attached by the word
\[
aba^{-1}b^{-1}.
\]
Thus
\[
C_2^{\mathrm{cell}}(T)\cong\ZZ,
\qquad
C_1^{\mathrm{cell}}(T)\cong\ZZ^2.
\]
The cellular boundary of the $2$-cell records the total exponent sums of $a$ and $b$ in the attaching word. Both exponent sums are zero, so
\[
\partial_2=0.
\]
There are no $3$-cells, hence
\[
H_2(T;\ZZ)
=
\ker\partial_2
\cong
\ZZ.
\]

:::

:::

::: {.pf-step #s1-3}

Suppose there were a continuous map
\[
g:T\to S^1\vee S^1
\]
such that
\[
f\circ g=\operatorname{id}_T.
\]
Then on second homology,
\[
f_*\circ g_*
=
\operatorname{id}_{H_2(T;\ZZ)}.
\]


::: pf-proof

Singular homology is functorial, so
\[
(f\circ g)_*
=
f_*\circ g_*.
\]
Under the assumed identity
\[
f\circ g=\operatorname{id}_T,
\]
the left-hand side is
\[
(\operatorname{id}_T)_*
=
\operatorname{id}_{H_2(T;\ZZ)}.
\]

:::

:::

::: {.pf-step #s1-4}

The identity in step [](#s1-3){.pf-ref} is impossible.


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
H_2(S^1\vee S^1;\ZZ)=0.
\]
Therefore the homomorphism
\[
g_*:
H_2(T;\ZZ)
\longrightarrow
H_2(S^1\vee S^1;\ZZ)
\]
is the zero map. Consequently
\[
f_*\circ g_*=0.
\]

But by step [](#s1-2){.pf-ref},
\[
H_2(T;\ZZ)\cong\ZZ\ne0,
\]
so its identity homomorphism is not the zero map. This contradicts step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore no such continuous map $g$ exists.


::: pf-proof

The assumption that $g$ exists leads to the contradiction in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is exactly the required conclusion.

:::

:::

:::
