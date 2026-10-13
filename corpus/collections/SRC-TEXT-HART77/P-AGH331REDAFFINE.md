---
schema: qual/card@1
id: P-AGH331REDAFFINE
kind: problem
title: Affineness is detected by the reduced scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Affine Schemes
  - Serre Criterion
relations: []
review: draft
---
::: {.problem}
Let $X$ be a noetherian scheme.
Show that $X$ is affine if and only if $X_{\mathrm{red}}$ (II, Ex.
2.3) is affine.

Hint: Use (3.7), and for any coherent sheaf $\mcf$ on $X$, consider the filtration $\mcf \supseteq \mcn \cdot \mcf \supseteq \mcn^2 \cdot \mcf \supseteq \cdots$, where $\mcn$ is the sheaf of nilpotent elements on $X$.
:::

::: {.solution}
Let $\mcn \subseteq \OO_X$ be the sheaf of nilpotent sections, the ideal sheaf of the closed immersion $X_{\mathrm{red}} \to X$.

::: pf

::: {.pf-step #s1}

If $X = \Spec A$ is affine, then $X_{\mathrm{red}} = \Spec A/N$ for the nilradical $N$ of $A$, so $X_{\mathrm{red}}$ is affine.

::: pf-proof

The reduction of an affine scheme is obtained by quotienting its coordinate ring
by the nilradical:
$$
(\Spec A)_{\red}\cong\Spec(A/\sqrt{0_A}).
$$
Thus affineness of $X$ implies affineness of $X_{\red}$.

:::

:::

::: {.pf-step #s2}

$\mcn^n = 0$ for some $n \geq 1$.

::: pf-proof

Because $X$ is noetherian, it is quasi-compact and admits a finite affine open
cover
$$
X=\bigcup_{j=1}^r U_j,
\qquad
U_j=\Spec A_j,
$$
with each $A_j$ noetherian.  On $U_j$, the ideal sheaf $\mcn$ corresponds to
the nilradical $N_j=\sqrt{0_{A_j}}$.

Since $A_j$ is noetherian, $N_j$ is finitely generated, say by
$x_{j1},\ldots,x_{js_j}$.  Choose exponents $e_{jk}\geq1$ with
$x_{jk}^{e_{jk}}=0$.  Any product of
$$
n_j=1+\sum_{k=1}^{s_j}(e_{jk}-1)
$$
generators contains some $x_{jk}$ at least $e_{jk}$ times, hence
$N_j^{n_j}=0$.  Let $n=\max_j n_j$.  Then
$\restrictionof{\mcn^n}{U_j}=0$ for every $j$, so $\mcn^n=0$.

:::

:::

::: {.pf-step #s3}

If $X_{\mathrm{red}}$ is affine, then $H^1(X, \mcf) = 0$ for every coherent sheaf $\mcf$ on $X$.

::: pf-proof

::: {.pf-step #s3-1}

For each $0\leq i<n$, the quotient
$$
\mcf_i\coloneqq
\mcn^i\mcf/\mcn^{i+1}\mcf
$$
is the pushforward of a coherent sheaf on $X_{\red}$.

::: pf-proof

The sheaves $\mcn^i\mcf$ are coherent because $X$ is noetherian and both
$\mcn$ and $\mcf$ are coherent.  The quotient $\mcf_i$ is therefore coherent.
Moreover,
$$
\mcn\mcf_i=0,
$$
so the $\OO_X$-module structure on $\mcf_i$ factors through
$\OO_X/\mcn=\OO_{X_{\red}}$.  Hence $\mcf_i$ is the direct image, under the
closed immersion $j:X_{\red}\hookrightarrow X$, of a coherent
$\OO_{X_{\red}}$-module.

:::

:::

::: {.pf-step #s3-2}

For each $0\leq i<n$,
$$
H^1(X,\mcf_i)=0.
$$

::: pf-proof

Write $\mcf_i=j_*\mathcal G_i$ as in step [](#s3-1){.pf-ref}.  The reduction map is a
homeomorphism on underlying spaces, and for a closed immersion the direct-image
functor on sheaves is exact.  Therefore
$$
H^1(X,\mcf_i)
=H^1(X,j_*\mathcal G_i)
\cong H^1(X_{\red},\mathcal G_i).
$$
The scheme $X_{\red}$ is affine by hypothesis, and $\mathcal G_i$ is
quasi-coherent, so the last group is zero.

:::

:::

::: {.pf-step #s3-3}

For every $0\leq i\leq n$,
$$
H^1(X,\mcn^i\mcf)=0.
$$

::: pf-proof

By step [](#s2){.pf-ref}, $\mcn^n\mcf=0$, so the assertion holds for $i=n$.
For $i<n$, the short exact sequence
$$
0\longrightarrow
\mcn^{i+1}\mcf
\longrightarrow
\mcn^i\mcf
\longrightarrow
\mcf_i
\longrightarrow0
$$
gives the exact segment
$$
H^1(X,\mcn^{i+1}\mcf)
\longrightarrow
H^1(X,\mcn^i\mcf)
\longrightarrow
H^1(X,\mcf_i).
$$
If the outer groups vanish, then the middle group vanishes.  Step [](#s3-2){.pf-ref} and
descending induction on $i$ therefore prove the claim.

:::

:::

::: pf-qed

Taking $i=0$ in step [](#s3-3){.pf-ref} gives
$H^1(X,\mcf)=0$.

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the forward implication.  Conversely, if $X_{\mathrm{red}}$
is affine, step [](#s3){.pf-ref} gives
$$
H^1(X,\mcf)=0
$$
for every coherent sheaf $\mcf$ on the noetherian scheme $X$.  Serre's
affineness criterion [[T-5IOUR]] therefore implies that $X$ is affine.

:::

:::

:::
