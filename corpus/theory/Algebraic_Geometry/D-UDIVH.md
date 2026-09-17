---
schema: qual/card@1
id: D-UDIVH
kind: definition
title: Support of sections and sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Support
relations:
- kind: uses
  target: D-0QSI0
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Checked the stalk definitions and the finite-module annihilator formula against Stacks Project Tag 00L2. Replaced the false assertion that every closed-immersion direct image has closed support by the exact support formula and its stalk proof; the identity immersion gives the counterexample.
prompts:
- Define the support of a section, and of a sheaf.
- Why is $\supp(s)$ closed?
- Give a sheaf whose support is not closed.
---

::: {.definition}
Let $\mcf$ be a sheaf of abelian groups on a topological space $X$.
For an open set $U\subseteq X$ and a section $s\in\mcf(U)$, the \dfn{support of the section} is
$$
\supp(s)\coloneqq\ts{x\in U\st s_x\ne0\text{ in }\mcf_x}.
$$
The \dfn{support of the sheaf} is
$$
\supp(\mcf)\coloneqq\ts{x\in X\st\mcf_x\ne0}.
$$
Here $s_x$ is the [[D-0QSI0|germ]] of $s$ in the [[D-0QSI0|stalk]] $\mcf_x$.
:::

::: {.proposition}
For every open set $U\subseteq X$ and $s\in\mcf(U)$, the subset $\supp(s)$ is closed in $U$.
:::

::: {.proof}
If $s_x=0$, the definition of a [[D-0QSI0|germ]] gives an open neighborhood $x\in V\subseteq U$ with $s|_V=0$.
Every point of $V$ therefore lies outside $\supp(s)$.
Thus $U\setminus\supp(s)$ is open.
:::

::: {.example title="A sheaf with nonclosed support"}
Let $p$ be a prime number and put $X=\Spec\ZZ_{(p)}$.
Its points are the generic point $\eta$ and the closed point $x=(p)$, and its open sets are $\varnothing$, $\{\eta\}$, and $X$.
Define a sheaf of abelian groups $\mcf$ by
$$
\mcf(X)=0,\qquad\mcf(\{\eta\})=\ZZ,\qquad\mcf(\varnothing)=0,
$$
with zero restriction maps for proper inclusions.
Every open cover of a nonempty open set contains that open set itself, so the sheaf axioms hold.
The only neighborhood of $x$ is $X$, whereas $\{\eta\}$ is a neighborhood of $\eta$.
Consequently $\mcf_x=0$ and $\mcf_\eta\cong\ZZ$, giving $\supp(\mcf)=\{\eta\}$, which is not closed in $X$.
For the open inclusion $j:\{\eta\}\hookrightarrow X$, this sheaf is the extension by zero $j_!\ul{\ZZ}$.
:::

::: {.proposition}
Let $X$ be a scheme and $\mcf$ a [[D-QNTZY|quasi-coherent]] $\OO_X$-module of finite type.
Then $\supp(\mcf)$ is closed.
For an affine open $U=\Spec A$ with $\mcf|_U\cong\widetilde M$,
$$
\supp(\mcf)\cap U=V(\Ann_A M).
$$
The finite-generator annihilator argument in [[P-AGH256SUPPORT]], step <1>2, proves this formula over any ring; the open-complement argument in step <1>3 gives closedness on $X$.
:::

::: {.proposition}
Let $i:Z\to X$ be a [[D-MORIMM|closed immersion]] of schemes, and let $\mcf$ be a sheaf of abelian groups on $Z$.
Then
$$
\supp(i_*\mcf)=i(\supp\mcf).
$$
In particular, $\supp(i_*\mcf)$ is closed in $X$ if and only if $\supp\mcf$ is closed in $Z$.
:::

::: {.proof}
For $x\notin i(Z)$, the open set $X\setminus i(Z)$ is a neighborhood on which $i_*\mcf$ is zero, so $(i_*\mcf)_x=0$.
For $x=i(z)$, the sets $i^{-1}(U)$, with $U$ an open neighborhood of $x$ in $X$, form a neighborhood basis at $z$ in $Z$ because $i$ is a homeomorphism onto its image.
Taking the colimit of $(i_*\mcf)(U)=\mcf(i^{-1}(U))$ gives $(i_*\mcf)_{i(z)}\cong\mcf_z$.
The support equality follows.
The closedness equivalence follows because $i$ identifies $Z$ with a closed subspace of $X$.
:::

::: {.remark}
The identity $i:X\to X$ is a [[D-MORIMM|closed immersion]].
For $X=\Spec\ZZ_{(p)}$ and the sheaf with $\mcf_\eta\cong\ZZ$ and $\mcf_x=0$, its direct image has support $\{\eta\}$, which is not closed.
:::
