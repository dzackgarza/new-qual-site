---
schema: qual/card@1
id: P-ALGS14F
kind: problem
title: Base change of $F[x]/(f)$ and $E \otimes_F E$ for finite Galois $E/F$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
(a) Let $F \subseteq E$ be a field extension, and $f(x) \in F[x]$.
Prove that
\[
E \otimes_F F[x]/\langle f(x) \rangle \simeq E[x]/\langle f(x) \rangle
\]
as $E$-algebras.
(Notice that $\langle f(x) \rangle$ at the left hand side is $F[x]f(x)$ and in the right hand side is $E[x]f(x)$). (Hint: $\{x^i \mid 0 \leq i \leq \deg f - 1\}$ is an $F$-basis of $F[x]/\langle f(x) \rangle$.)

(b) Let $E/F$ be a finite Galois extension.
Prove that
\[
E \otimes_F E \simeq E \oplus \cdots \oplus E
\]
($[E:F]$ times) as $E$-algebras.
:::

::: {.solution}
<1>1. Part (a): define
\[
\Phi:E\otimes_F F[x]/(f)\longrightarrow E[x]/(f)
\]
by
\[
\Phi\bigl(e\otimes \overline{g(x)}\bigr)=\overline{e\,g(x)}.
\]
This is a well-defined homomorphism of $E$-algebras.
::: {.proof}
The map $(e,\bar g)\mapsto\overline{eg}$ is $F$-balanced and multiplicative, so the universal property of the tensor product gives $\Phi$.
:::

<1>2. If $f\ne0$ has degree $d$, then
\[
1,\bar x,\ldots,\bar x^{d-1}
\]
is an $F$-basis of $F[x]/(f)$.
Hence
\[
1\otimes1,\ 1\otimes\bar x,\ldots,1\otimes\bar x^{d-1}
\]
is an $E$-basis of $E\otimes_F F[x]/(f)$, while
\[
1,\bar x,\ldots,\bar x^{d-1}
\]
is an $E$-basis of $E[x]/(f)$.
The map $\Phi$ sends the first basis to the second, so it is an isomorphism.
::: {.proof}
Tensoring an $F$-basis with $E$ gives an $E$-basis after scalar extension.
Division by the same nonzero polynomial $f$ over $E$ gives the displayed basis on the target.
:::

<1>3. If $f=0$, the same conclusion is the standard scalar-extension isomorphism
\[
E\otimes_F F[x]\cong E[x].
\]
Thus part (a) holds in all cases.
::: {.proof}
Both sides are free $E$-algebras on one generator, and the map of <1>1 sends $1\otimes x$ to $x$.
:::

<1>4. Part (b): because $E/F$ is finite Galois, it is finite separable.
By the primitive element theorem there exists $\alpha\in E$ such that
\[
E=F(\alpha)\cong F[x]/(m_\alpha(x)),
\]
where $m_\alpha$ is the minimal polynomial of $\alpha$ over $F$.
::: {.proof}
Finite separable extensions are simple.
:::

<1>5. Applying part (a),
\[
E\otimes_F E
\cong
E\otimes_F F[x]/(m_\alpha)
\cong
E[x]/(m_\alpha).
\]
::: {.proof}
Substitute the presentation of $E$ from <1>4 into the second tensor factor and apply part (a).
:::

<1>6. Since $E/F$ is Galois,
\[
m_\alpha(x)=\prod_{\sigma\in\operatorname{Gal}(E/F)}(x-\sigma(\alpha))
\]
in $E[x]$, and the roots $\sigma(\alpha)$ are pairwise distinct.
::: {.proof}
Normality puts every conjugate of $\alpha$ in $E$, and separability makes the conjugates distinct.
Because $E=F(\alpha)$, the $F$-embeddings of $E$ into an algebraic closure are exactly the Galois automorphisms, so there are $[E:F]$ such roots.
:::

<1>7. The ideals $(x-\sigma(\alpha))$ are pairwise comaximal.
Therefore the Chinese remainder theorem gives
\[
E[x]/(m_\alpha)
\cong
\prod_{\sigma\in\operatorname{Gal}(E/F)}E[x]/(x-\sigma(\alpha))
\cong
\prod_{\sigma\in\operatorname{Gal}(E/F)}E.
\]
There are $|\operatorname{Gal}(E/F)|=[E:F]$ factors, proving the claim.
::: {.proof}
Distinct linear factors generate comaximal ideals, and each quotient by $(x-c)$ is canonically $E$ by evaluation at $c$.
:::
:::
