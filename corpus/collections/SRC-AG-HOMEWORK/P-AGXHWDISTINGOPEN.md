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
Let $A\in \Ring$ and $X\coloneqq\Spec(A)$, and for $f\in A$ let $D(f)\coloneqq V(\generators{f})^c$.
Show that there is an isomorphism of ringed spaces
$$
(D(f), \restrictionof{\OO_X}{D(f)}) \iso \Spec(A_f)
.$$
:::

::: {.solution}
Let $S=\{1,f,f^2,\ldots\}$ and let $\lambda:A\to A_f=S^{-1}A$ be the localization map.

::: pf

::: pf-step

Contraction along $\lambda$ gives a bijection
$$
\phi:\Spec(A_f)\longrightarrow D(f),
\qquad
\mathfrak q\longmapsto\lambda^{-1}(\mathfrak q).
$$

::: pf-proof

Prime ideals of a localization $S^{-1}A$ are in bijection with prime ideals $\mathfrak p\subseteq A$ disjoint from $S$, by contraction and extension. For the present multiplicative set,
$$
\mathfrak p\cap S=\varnothing
\iff f\notin\mathfrak p
\iff \mathfrak p\in D(f).
$$
Thus contraction has the stated image and is bijective, with inverse $\mathfrak p\mapsto\mathfrak pA_f$.

:::

:::

::: {.pf-step #s2}

For every $g\in A$,
$$
\phi^{-1}(D(g)\cap D(f))=D(g/1)\subseteq\Spec(A_f).
$$

::: pf-proof

For $\mathfrak q\in\Spec(A_f)$,
$$
\begin{aligned}
\mathfrak q\in\phi^{-1}(D(g)\cap D(f))
&\iff g\notin\lambda^{-1}(\mathfrak q)\\
&\iff g/1\notin\mathfrak q\\
&\iff \mathfrak q\in D(g/1).
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The map $\phi$ is a homeomorphism.

::: pf-proof

The sets $D(g)\cap D(f)$ form a basis for the subspace topology on $D(f)$, while the sets $D(h)$ form a basis for $\Spec(A_f)$. Every element $h\in A_f$ has the form $g/f^n$, and
$$
D(g/f^n)=D(g/1)
$$
because $f/1$ is a unit in $A_f$. Step [](#s2){.pf-ref} therefore identifies basis opens on the two spaces under the bijection $\phi$, proving that both $\phi$ and $\phi^{-1}$ are continuous.

:::

:::

::: {.pf-step #s4}

On corresponding basis opens there are canonical ring isomorphisms
$$
\mathcal O_{\Spec(A_f)}(D(g/1))
\cong
\restrictionof{\mathcal O_X}{D(f)}(D(g)\cap D(f)).
$$

::: pf-proof

By the definition of the structure sheaf on an affine scheme,
$$
\mathcal O_{\Spec(A_f)}(D(g/1))=(A_f)_{g/1}.
$$
Since $D(g)\cap D(f)=D(fg)$ inside $\Spec(A)$,
$$
\restrictionof{\mathcal O_X}{D(f)}(D(g)\cap D(f))
=\mathcal O_X(D(fg))
=A_{fg}.
$$
Localization is transitive, and both rings canonically identify with the localization of $A$ in which both $f$ and $g$ are inverted:
$$
(A_f)_{g/1}\cong A_{fg}.
$$
These isomorphisms commute with restriction maps because all restriction maps on distinguished opens are the canonical localization homomorphisms.

:::

:::

::: {.pf-step #s5}

The basis isomorphisms of step [](#s4){.pf-ref} determine an isomorphism of sheaves
$$
\mathcal O_{\Spec(A_f)}
\cong
\phi^{-1}\!\left(\restrictionof{\mathcal O_X}{D(f)}\right).
$$

::: pf-proof

Distinguished opens form a basis closed under finite intersections. An isomorphism on such a basis that is compatible with restriction maps extends uniquely to an isomorphism of sheaves. The compatibility was established in step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Hence
$$
\boxed{(D(f),\restrictionof{\mathcal O_X}{D(f)})\cong\Spec(A_f)}
$$
as ringed spaces.

::: pf-proof

Step [](#s3){.pf-ref} gives the homeomorphism of underlying spaces, and step [](#s5){.pf-ref} identifies the structure sheaves under that homeomorphism. Together they define the required isomorphism of ringed spaces.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the desired conclusion.

:::

:::

:::

::: {.remark}
The isomorphism is induced by the localization map $A\to A_f$: on points it is contraction of prime ideals, and on distinguished opens it is the canonical localization isomorphism $(A_f)_{g/1}\cong A_{fg}$.
:::
