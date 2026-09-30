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
Let $A\in \Ring$ and $X\definedas \Spec(A)$, and for $f\in A$ let $D(f) \definedas V(\generators{f})^c$.
Show that there is an isomorphism of ringed spaces
\[
(D(f), \restrictionof{\OO_X}{D(f)}) \iso \Spec(A_f)
.\]
:::

::: {.hint}
- Take $\iota: A\to A_f$ and the induced map $\iota^*: \Spec A_f \to \Spec A$.
- Use $\Spec S^{-1}A \cong \theset{\mfp\in \Spec A \st \mfp \intersect S = \emptyset }$, so $\Spec A_f = \theset{\mfp\in \Spec A \st \mfp \not\supseteq \generators{f}}$.
- Construct $\psi \definedas \iota^*$, and check $D(g/f^k) \xrightarrow{\psi} D(gf)$ and $D(g) \xrightarrow{\psi^{-1}} D(g/1)$.
- Use $\restrictionof{\OO_{\Spec A}}{D(f)}(D(g)) = (A_f)_g$ and define $\psi^\# = \id$.
:::

::: {.solution}
Let $\iota\colon A\to A_f$, $a\mapsto a/1$, let $Y\definedas\Spec A_f$, and let $\psi\colon Y\to X$ be $\psi(\mfq)\definedas\iota^{-1}(\mfq)$.

::: pf

::: {.pf-step #psi-homeomorphism}
$\psi$ is a homeomorphism of $Y$ onto $D(f)$.

::: pf-proof
The primes of $A_f$ correspond to the primes $\mfp$ of $A$ with $f\notin\mfp$, by $\mfq\mapsto\iota^{-1}(\mfq)$ with inverse $\mfp\mapsto\mfp A_f$; so $\psi$ is a bijection onto $D(f)$. For $a\in A$, $\psi^{-1}(D(a))=D(a/1)$, so $\psi$ is continuous. Every $a/f^k\in A_f$ differs from $a/1$ by a unit, so the sets $D(a/1)$ form a basis of $Y$, and $\psi(D(a/1))=D(a)\cap D(f)=D(af)$ is open. So $\psi$ is open onto $D(f)$.
:::

:::

::: {.pf-step #sections-isomorphism}
For $a\in A$, there is an isomorphism $\OO_X(D(af))\to\OO_Y(\psi^{-1}(D(af)))$, compatible with restriction.

::: pf-proof
By step [](#psi-homeomorphism){.pf-ref}, $\psi^{-1}(D(af))=D(a/1)$. The sections are $\OO_X(D(af))=A_{af}$ and $\OO_Y(D(a/1))=(A_f)_{a/1}$, and $x/(af)^n\mapsto (x/1)/(af/1)^n$ is an isomorphism $A_{af}\to(A_f)_{a/1}$, since both rings are $A$ with $a$ and $f$ inverted. For $D(bf)\subseteq D(af)$ the restriction maps on both sides are the canonical maps between localizations of $A$, so the isomorphisms commute with them.
:::

:::

::: pf-qed
The sets $D(af)$, $a\in A$, form a basis of $D(f)$ closed under intersection. By step [](#sections-isomorphism){.pf-ref}, $\psi^\#\colon\restrictionof{\OO_X}{D(f)}\to\psi_*\OO_Y$ is defined and bijective on this basis and commutes with restriction, so it extends uniquely to an isomorphism of sheaves on $D(f)$. With step [](#psi-homeomorphism){.pf-ref}, $(\psi,\psi^\#)\colon(Y,\OO_Y)\to(D(f),\restrictionof{\OO_X}{D(f)})$ is an isomorphism of ringed spaces, and its inverse is the required isomorphism.
:::

:::

:::
