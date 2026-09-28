---
schema: qual/card@1
id: P-AGXHWDISTINGOPEN
kind: problem
title: A distinguished open of an affine scheme is the spectrum of a localization
classification:
  areas:
  - algebraic-geometry
  topics:
  - Affine Schemes
  - Localization
  - Distinguished Opens
relations: []
review: draft
---

::: {.problem}
Let $A\in \Ring$ and $X\da \Spec(A)$, and for $f\in A$ let $D(f) \da V(\gens{f})^c$.
Show that there is an isomorphism of ringed spaces
\[
(D(f), \ro{\OO_X}{D(f)}) \iso \Spec(A_f)
.\]
:::

::: {.hint}
- Take $\iota: A\to A_f$ and the induced map $\iota^*: \Spec A_f \to \Spec A$.
- Use $\Spec S^{-1}A \cong \ts{\mfp\in \Spec A \st \mfp \intersect S = \emptyset }$, so $\Spec A_f = \ts{\mfp\in \Spec A \st \mfp \not\supseteq \gens{f}}$.
- Construct $\psi \da \iota^*$, and check $D(g/f^k) \xrightarrow{\psi} D(gf)$ and $D(g) \xrightarrow{\psi^{-1}} D(g/1)$.
- Use $\ro{\OO_{\Spec A}}{D(f)}(D(g)) = (A_f)_g$ and define $\psi^\# = \id$.
:::

::: {.solution}
Recall: for $I\normal A$ any ideal,
\[
V(I) &= \ts{\mfp\in \Spec A \st \mfp\supseteq I} \\
D(I) &\da V(I)^c = \ts{\mfp\in \Spec A \st \mfp\not\supseteq I}
,\]
and there is a correspondence
\[
i: A&\to A_f \\
a &\mapsto {\left[ {a\over 1} \right]}
,\]
with
\[
\ts{\mfp\in \Spec A \st \mfp \intersect \ts{f^n} = \emptyset} \iff \Spec A_f
,\]
\[
\mfp &\mapsto \gens{i(\mfp)} = \ts{\mfp'/s \st \mfp'\in \mfp,\ s\in \ts{f^n} } \\
i^{-1}(\mfq) &\mapsfrom \mfq = \ts{g/f^n}\normal A_f
,\]
i.e. the prime ideals of $S^{-1}A$ are the prime ideals of $A$ not meeting $S$.

Let $Y\da \Spec A_f$. The isomorphism consists of
\[
\psi&\in \Top(D(f), Y)\\
\psi^\# &\in \Mor_{\Sh_{Y}}(\OO_{Y}, \psi_* \ro{\OO_X}{D(f)})
.\]

- Let $i: A\to A_f$ be $a\mapsto a/1$. Since the primes of $A_f$ correspond to the primes of $A$ not meeting $\ts{f^n}_{n\geq 1}$, this induces
\[
\Spec A_f
&\xrightarrow{i^*}
\ts{\mfp\in \Spec A\st \mfp \intersect \ts{f^n}_{n\geq 1} = \emptyset } \\
&= \ts{\mfp\in \Spec A \st \mfp \not\supseteq \gens{f}} \\
&\da D(\gens{f}) = D(f)
.\]
  Here $i^*(\mfq) = i^{-1}(\mfq)$, and $i_*(\mfp) = \gens{i(\mfp)}$.

- Let $\psi: \Spec A_f \to D(f)$ be $i^*$; it is a continuous bijection.

- $\psi$ is a homeomorphism, because it is an open map:
\[
D(g/f^k ) &\xrightarrow{\psi} D(gf) \\
D(g) &\xrightarrow{\psi^{-1}} D(g/1)
.\]

- Put $\psi^\#\da \id$. On distinguished opens,
\[
D(g) \subseteq Y \implies  \psi_* \ro{\OO_X}{D(f)}(D(g))
&\da \ro{\OO_X}{D(f)}(\psi^{-1}( D(g)) ) \\
&= \ro{\OO_X}{D(f)}( D(g/1) ) \\
&= (A_f)_{g/1}
,\]
using that $\OO_X(D(h)) = A_{h}$, so the coordinate ring of $D(f)$ is $A_f$.

- Similarly
\[
\OO_{\Spec A_f}(D(g)) = (A_f)_g
,\]
and these are equal.

- For an open $U \subseteq \Spec A_f$, cover $U$ by distinguished opens $D(g_k)$; the sections of each sheaf agree on each $D(g_k)$, and by the sheaf axioms they glue to agreeing sections on $U$, so this induces an isomorphism of sheaves.
:::
