---
schema: qual/card@1
id: P-WESCA16-6
kind: problem
title: 'Automorphisms of the punctured disk'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Determine the conformal automorphism group of
\[
\mathbb D^*=\{z:0<|z|<1\},
\]
and prove your claim.
:::

::: {.solution}
<1>1. Let $f:\mathbb D^*\to\mathbb D^*$ be a conformal automorphism. Then
$f$ extends holomorphically across $0$ to a map
\[
F:\mathbb D\to\mathbb D.
\]

::: {.proof}
The function $f$ is bounded by $1$ on a punctured neighborhood of $0$, so
the removable singularity theorem gives a holomorphic extension $F$ to
$\mathbb D$. The extension satisfies $|F(0)|\le1$. If $|F(0)|=1$, then the
maximum modulus principle would force $F$ to be constant, contradicting that
$f$ is bijective. Hence $|F(0)|<1$, so $F(\mathbb D)\subseteq\mathbb D$.
:::

<1>2. The inverse $f^{-1}$ extends to a holomorphic map
\[
G:\mathbb D\to\mathbb D,
\]
and $F$ and $G$ are inverse automorphisms of $\mathbb D$.

::: {.proof}
Apply step <1>1 to $f^{-1}$ to obtain $G$. On $\mathbb D^*$,
\[
G(F(z))=z.
\]
Both sides are holomorphic on $\mathbb D$, so the identity theorem gives
\[
G\circ F=\operatorname{id}_{\mathbb D}.
\]
Similarly,
\[
F\circ G=\operatorname{id}_{\mathbb D}.
\]
Thus $F$ is a conformal automorphism of the full unit disk, with inverse $G$.
:::

<1>3. The disk automorphism $F$ fixes $0$.

::: {.proof}
By hypothesis,
\[
F(\mathbb D^*)=f(\mathbb D^*)=\mathbb D^*.
\]
By step <1>2, $F$ is a bijection
\[
F:\mathbb D\to\mathbb D.
\]
Therefore the unique point in the image contributed by the omitted domain
point $0$ is the unique point omitted from $F(\mathbb D^*)$. Since
\[
\mathbb D\setminus\mathbb D^*=\{0\},
\]
one must have
\[
F(0)=0.
\]
:::

<1>4. There is $\lambda\in\mathbb C$ with $|\lambda|=1$ such that
\[
F(z)=\lambda z
\qquad(z\in\mathbb D).
\]

::: {.proof}
By step <1>3, $F:\mathbb D\to\mathbb D$ is holomorphic and fixes $0$.
Schwarz's lemma gives
\[
|F(z)|\le|z|.
\]
Its inverse $G$ also fixes $0$, so Schwarz's lemma applied to $G$ gives
\[
|G(w)|\le|w|.
\]
Taking $w=F(z)$ yields
\[
|z|=|G(F(z))|\le|F(z)|.
\]
Hence
\[
|F(z)|=|z|
\]
for every $z$. Equality in Schwarz's lemma at any nonzero point implies that
$F$ is a rotation:
\[
F(z)=\lambda z,
\qquad
|\lambda|=1.
\]
:::

<1>5. Consequently
\[
\boxed{
\operatorname{Aut}(\mathbb D^*)
=\{z\mapsto\lambda z:|\lambda|=1\}
\cong S^1 }.
\]

::: {.proof}
Step <1>4 shows that every conformal automorphism has this form. Conversely,
for every $|\lambda|=1$, the map
\[
z\longmapsto\lambda z
\]
is a conformal bijection of $\mathbb D^*$ with inverse
$z\mapsto\overline\lambda z$. Composition corresponds to multiplication in
$S^1$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 determines the automorphism group.
:::
:::
