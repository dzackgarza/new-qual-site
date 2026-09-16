---
schema: qual/card@1
id: E-SMI-8000E-ED6
kind: problem
title: Kernel and cokernel are unchanged under isomorphisms of source and target
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the source/target-isomorphism statement with the local 8000e extraction, Euclidean-domains problem 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Identified the new kernel as g^{-1}(ker f) and constructed the quotient isomorphism induced by h on cokernels."
---

::: {.exercise}
Prove that if $f: M \to N$ is any $R$ module map, and $g: M \to M$ and $h: N \to N$ are isomorphisms, then $h \circ f \circ g: M \to N$ has kernel and cokernel isomorphic to those of $f$.
:::


::: {.solution}
Put
$$
F=h\circ f\circ g:M\longrightarrow N.
$$

<1>1. The kernels of $F$ and $f$ are isomorphic.
::: {.proof}
Because $h$ is injective,
$$
F(x)=0
\iff h(f(gx))=0
\iff f(gx)=0.
$$
Thus
$$
\ker F=g^{-1}(\ker f).
$$
Since $g$ is an automorphism of $M$, its restriction
$$
g|_{\ker F}:\ker F\longrightarrow\ker f
$$
is injective. It is also surjective: if $y\in\ker f$, then
$x=g^{-1}(y)$ satisfies
$$
F(x)=h(f(y))=0
$$
and $g(x)=y$. Therefore
$$
\boxed{\ker(hfg)\cong\ker f.}
$$
:::

<1>2. The image of $F$ is $h(\operatorname{im}f)$.
::: {.proof}
Since $g$ is surjective,
$$
f(g(M))=f(M)=\operatorname{im}f.
$$
Applying $h$ gives
$$
\operatorname{im}F=h(\operatorname{im}f).
$$
:::

<1>3. The cokernels of $F$ and $f$ are isomorphic.
::: {.proof}
By step <1>2,
$$
\operatorname{coker}F
=N/h(\operatorname{im}f).
$$
Define
$$
\overline h:N/\operatorname{im}f
\longrightarrow
N/h(\operatorname{im}f)
$$
by
$$
\overline h(y+\operatorname{im}f)
=h(y)+h(\operatorname{im}f).
$$
This is well defined because $h$ sends $\operatorname{im}f$ onto
$h(\operatorname{im}f)$. Since $h$ is an isomorphism, the quotient map
$\overline h$ is an isomorphism, with inverse induced by $h^{-1}$. Hence
$$
\boxed{\operatorname{coker}(hfg)\cong\operatorname{coker}f.}
$$
:::

Thus precomposing and postcomposing a module map with isomorphisms changes
neither its kernel nor its cokernel up to isomorphism.
:::
