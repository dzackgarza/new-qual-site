---
schema: qual/card@1
id: D-COMMACAT
kind: definition
title: Comma categories, and colimits as initial cocones
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Colimits
  - Comma Categories
relations:
- kind: related-to
  target: D-5MX7E
- kind: related-to
  target: D-0QSI0
review: draft
prompts:
- What is a comma category, and how does it specialize to a slice category?
- How is a colimit an initial object in a category of cocones?
---

::: {.definition title="Comma category"}
Let $S \colon \mathsf{A} \to \mathsf{C}$ and $T \colon \mathsf{B} \to \mathsf{C}$ be functors.
The \dfn{comma category} $S \downarrow T$ has as objects the triples $(A, B, h)$ with $A \in \mathsf{A}$, $B \in \mathsf{B}$ and $h \colon S(A) \to T(B)$ a morphism of $\mathsf{C}$.
A morphism $(A_0, B_0, h_0) \to (A_1, B_1, h_1)$ is a pair $(f, g)$ of morphisms $f \colon A_0 \to A_1$ in $\mathsf{A}$ and $g \colon B_0 \to B_1$ in $\mathsf{B}$ such that $h_1 \circ S(f) = T(g) \circ h_0$:

\begin{tikzcd}
	{S(A_0)} & {S(A_1)} \\
	{T(B_0)} & {T(B_1)}
	\arrow["{S(f)}", from=1-1, to=1-2]
	\arrow["{h_0}"', from=1-1, to=2-1]
	\arrow["{h_1}", from=1-2, to=2-2]
	\arrow["{T(g)}"', from=2-1, to=2-2]
\end{tikzcd}

Composition is componentwise.
:::

::: {.example title="Slice categories"}
Let $\mathsf{pt}$ be the category with one object $\ast$ and only its identity morphism, $X \in \mathsf{A}$, and $T_X \colon \mathsf{pt} \to \mathsf{A}$ the functor with $T_X(\ast) = X$.
Then $\id_{\mathsf{A}} \downarrow T_X$ has objects $(A, \ast, h \colon A \to X)$ and morphisms $(f, \id_\ast)$ with $h_1 \circ f = h_0$, so it is the slice category $\mathsf{A}_{/X}$ of objects over $X$.
:::

::: {.definition title="Cocones"}
Let $F \colon \mathsf{J} \to \mathsf{C}$ be a functor, and let $\Delta \colon \mathsf{C} \to \operatorname{Fun}(\mathsf{J}, \mathsf{C})$ be the diagonal functor, sending $N$ to the constant functor $\Delta(N)$ with value $N$ on objects and $\id_N$ on morphisms.
A \dfn{cocone} over $F$ is an object $N \in \mathsf{C}$ with a natural transformation $\psi \colon F \to \Delta(N)$: morphisms $\psi_X \colon F(X) \to N$ for $X \in \mathsf{J}$ with $\psi_Y \circ F(u) = \psi_X$ for every $u \colon X \to Y$ in $\mathsf{J}$.
The \dfn{category of cocones} over $F$ is the comma category $\ast_F \downarrow \Delta$, also written $F \downarrow \Delta$, where $\ast_F \colon \mathsf{pt} \to \operatorname{Fun}(\mathsf{J}, \mathsf{C})$ picks out $F$; its objects are the cocones $(N, \psi)$, and a morphism $(N, \psi) \to (N', \psi')$ is a morphism $g \colon N \to N'$ with $g \circ \psi_X = \psi'_X$ for all $X$.
:::

::: {.proposition}
A colimit of $F$ ([[D-5MX7E]]) is exactly an initial object of the category of cocones over $F$.
In particular a colimit is unique up to unique isomorphism.
:::

::: {.example}
For a presheaf $\mathcal{F}$ on a space $Y$ and a point $p \in Y$, the stalk $\mathcal{F}_p$ ([[D-0QSI0]]) is the colimit of the functor $U \mapsto \mathcal{F}(U)$ on the category of open neighbourhoods of $p$ with the opposite of inclusion, and the maps $\mathcal{F}(U) \to \mathcal{F}_p$, $s \mapsto s_p$, form the initial cocone.
:::
