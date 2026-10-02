---
schema: qual/card@1
id: PR-COHLES
kind: proposition
title: Long exact cohomology sequences and ideal sequences
slogan: 'Short exact sequences yield long exact cohomology sequences; connecting maps record the obstruction to lifting.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Long Exact Sequences
  - Ideal Sheaves
relations:
- kind: uses
  target: D-COHDER
- kind: uses
  target: T-IJW1K
review: draft
prompts:
- What is the long exact sequence in sheaf cohomology?
- How do you compute the cohomology of a hypersurface in $\PP^n$?
- What is the long exact sequence in cohomology of a short exact sequence of complexes?
---

::: {.proposition}
A short exact sequence $0 \to \mcf' \to \mcf \to \mcf'' \to 0$ of sheaves of abelian groups gives a long exact sequence
$$
0 \to H^0(\mcf') \to H^0(\mcf) \to H^0(\mcf'') \mapsvia{\delta} H^1(\mcf') \to \cdots ,
$$
natural in morphisms of short exact sequences.
:::

::: {.lemma title="Long exact sequence of a short exact sequence of complexes"}
Let $0 \to C'^\bullet \xrightarrow{u} C^\bullet \xrightarrow{v} C''^\bullet \to 0$ be a short exact sequence of complexes in an abelian category.
Then there are connecting morphisms $\delta^i \colon H^i(C''^\bullet) \to H^{i+1}(C'^\bullet)$, natural in the sequence, making
$$
\cdots \to H^i(C'^\bullet) \to H^i(C^\bullet) \to H^i(C''^\bullet) \xrightarrow{\delta^i} H^{i+1}(C'^\bullet) \to \cdots
$$
exact.
:::

::: {.remark}
Choose a degreewise split short exact sequence of injective resolutions
$$
0\to I'^\bullet\to I^\bullet\to I''^\bullet\to0.
$$
Applying $\Gamma(X,-)$ preserves the split exact sequence in each degree, and the lemma gives the long exact sequence in derived-functor cohomology.
For Čech cohomology of quasicoherent sheaves on a quasicompact separated scheme with a finite affine cover $\mathfrak{U}$, the sequence $0 \to C^\bullet(\mathfrak{U}, \mcf') \to C^\bullet(\mathfrak{U}, \mcf) \to C^\bullet(\mathfrak{U}, \mcf'') \to 0$ is exact because every finite intersection of the cover is affine and sections of quasicoherent sheaves over affines form exact sequences, and the lemma applies directly.
:::

::: {.remark title="What the connecting map is"}
$\delta$ sends a global section of $\mcf''$ to the obstruction to lifting it: lift locally on a cover, take the differences of the lifts on overlaps, and read the result as a class in $H^1(\mcf')$.
A section $s\in H^0(\mcf'')$ lifts globally exactly when $\delta(s)=0$. In particular, $H^1(\mcf')=0$ is sufficient for every global section of $\mcf''$ to lift; for the fixed short exact sequence, surjectivity of $H^0(\mcf)\to H^0(\mcf'')$ is equivalent to $\delta=0$.
:::

::: {.remark title="Standard computations"}
For $Y \subseteq \PP^n$ closed with ideal sheaf $\mci_Y$, twist the ideal sequence:
$$
0 \to \mci_Y(d) \to \OO_{\PP^n}(d) \to \OO_Y(d) \to 0 .
$$
Its long exact sequence relates the cohomology of $\OO_Y(d)$ to that of $\mci_Y(d)$ and $\OO_{\PP^n}(d)$.
If $Y$ is a hypersurface of degree $e$, then $\mci_Y\cong\OO_{\PP^n}(-e)$, so the sequence becomes
$$
0\to\OO_{\PP^n}(d-e)\to\OO_{\PP^n}(d)\to\OO_Y(d)\to0.
$$
Together with the cohomology of twists on $\PP^n$, this computes the Hilbert function and Hilbert polynomial of $Y$. For a smooth plane curve of degree $e$, it gives genus $\binom{e-1}{2}$.

If $C$ is a smooth projective curve over $k$, $D$ is a divisor, $p\in C(k)$, and $i_p\colon\Spec k\hookrightarrow C$ is the corresponding closed immersion, then
$$
0\to\OO_C(D-p)\to\OO_C(D)\to i_{p*}k\to0
$$
implies $\ell(D)-\ell(D-p)\in\{0,1\}$.
:::
