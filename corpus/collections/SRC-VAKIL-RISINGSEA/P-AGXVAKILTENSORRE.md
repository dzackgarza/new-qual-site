---
schema: qual/card@1
id: P-AGXVAKILTENSORRE
kind: problem
title: Right exactness of $({-})\tensor_R N$ on $R\dash$modules
classification:
  areas:
  - algebraic-geometry
  topics:
  - Tensor Products
  - Exact Sequences
  - Module Categories
relations: []
review: draft
---

::: problem
Show that the endofunctor
\[
F: \mods{R} &\to \mods{R} \\
X &\mapsto X\tensor_R N \\
(X\xrightarrow{f} Y) &\mapsto (X\tensor_R N \xrightarrow{f \tensor \id_N} Y\tensor_R N)
\]
is right exact.
:::

::: remark
To make sense of the functor, one may need an isomorphism
\[
\hom_{\mods{R}}(X, Y) \tensor_R \hom_{\mods{R}}(A, B) \to \hom_{\mods{R}}(X\tensor_R A, Y\tensor_R B)
.\]
Is this what makes taking $f:X\to Y$ and $g:A\to B$ and forming $f\tensor g: X\tensor A \to Y\tensor B$ well-defined?
:::

::: solution
Let $A\xrightarrow{f} B \xrightarrow{g} C \to 0$ be an exact sequence, so

- $\im f = \ker g$ by exactness at $B$,
- $\im g = C$ by exactness at $C$.

Applying $F$ yields
\[
A\tensor_R N \xrightarrow{f\tensor \id_N} B\tensor_R N \xrightarrow{g\tensor \id_N} C\tensor_R N \to 0
.\]

We must show

1. Exactness at $C\tensor_R N$: $\im(g\tensor \id_N) = C\tensor_R N$, i.e. this is surjective.
2. Exactness at $B\tensor_R N$: $\im(f\tensor \id_N) = \ker(g\tensor \id_N)$.

We use that every element of a tensor product is a finite sum of elementary tensors.

**Claim**: $\im(g\tensor \id_N) \subseteq C\tensor_R N$.

- Let $b\tensor n \in B\tensor_R N$ be an elementary tensor.
- Then $(g\tensor \id_N)(b\tensor n) \da g(b) \tensor \id_N (n) = g(b) \tensor n$.
- Since $\im(g) = C$, there is $c\in C$ with $g(b) = c$, so $g(b) \tensor n = c \tensor n \in C\tensor_R N$.
- Extend by linearity:
\[
\qty{g\tensor_R \id_N}\qty{\sum_{i=1}^m r_i \cdot b_i \tensor n_i}
= \sum_{i=1}^m (g\tensor \id_N)(r_i\cdot b_i \tensor n_i)
\da \sum_{i=1}^m g(r_i\cdot b_i) \tensor \id_N(n_i)
=_H \sum_{i=1}^m r_i\cdot c_i \tensor n_i \in C\tensor_R N
,\]
using bilinearity for the first equality; the equality marked $H$ uses the proof above for elementary tensors, noting that ring scalars $r_i\in R$ pull through $\mods{R}$ morphisms.

**Claim**: $C \tensor_R N \subseteq \im(g\tensor \id_N)$.

- Let $c\tensor n \in C\tensor_R N$ be an elementary tensor.
- Then $c\in C = \im(g)$, so $c = g(b)$ for some $b\in B$.
- So $c\tensor n = g(b) \tensor n = (g\tensor \id_N)(b\tensor n)$.
- Extend by linearity:
\[
\sum_{i=1}^m r_i\cdot c_i \tensor n_i
=_H \sum_{i=1}^m g(r_i\cdot b_i) \tensor n_i
= \sum_{i=1}^m (g\tensor \id_N)(r_i\cdot b_i \tensor n_i)
= (g\tensor \id_N)\qty{\sum_{i=1}^m r_i\cdot b_i \tensor n_i}
.\]

This proves (1).

**Claim**: $\im(f\tensor \id_N) \subseteq \ker(g\tensor \id_N)$.

- Let $b\tensor n \in \im(f\tensor \id_N)$; we want $(g\tensor \id_N)(b\tensor n) = 0 \in C\tensor_R N$.
- Then $b\tensor n = f(a)\tensor n$ for some $a\in A$.
- By exactness of the original sequence, $\im f \subseteq \ker g$, so $g(f(a)) = 0 \in C$.
- Then
\[
(g\tensor \id_N)\qty{ b \tensor n} = (g\tensor \id_N)(f(a)\tensor n) \da g(f(a)) \tensor n = 0\tensor n = 0\in C\tensor_R N
,\]
using that $0\tensor x = 0$ in any tensor product.
- Extend by linearity.

**Claim** (the nontrivial part): $\ker(g\tensor \id_N) \subseteq \im(f\tensor \id_N)$.

> The problem is that
> \[
> x\in \ker(g\tensor \id_N) \implies x = \sum_{i=1}^m r_i\cdot b_i \tensor n_i
> \implies (g\tensor \id_N)\qty{\sum_{i=1}^m r_i\cdot b_i \tensor n_i} = \sum_{i=1}^m r_i\cdot g(b_i) \tensor n_i = 0\in C\tensor_R N
> ,\]
> **but** this does not imply $g(b_i) = 0\in C$ for all $i$, which is what one would need in order to use $\im f = \ker g$ to write $g(b_i) = 0\implies \exists a_i,\, f(a_i) = b_i$ and pull everything back to $A\tensor_R N$.

Strategy: use the first claim and the first isomorphism theorem to obtain

\begin{tikzcd}
	{B\tensor_R N \over \im(f\tensor_R \id_N)} \ar[r, hook, "i"]\ar[rrr, bend left, dotted, "\alpha"] & {B\tensor_R N \over \ker(g \tensor_R \id_N)} \ar[r, "\cong"] & \im(g\tensor_R \id_N) \ar[equal]{r} & C\tensor_R N
\end{tikzcd}

- The injection $i$ exists because $\im(f\tensor_R \id_N) \subseteq \ker(g\tensor_R \id_N)$ by the first claim.
- The middle isomorphism is the first isomorphism theorem.
- The right-hand equality follows from surjectivity of $g\tensor_R \id_N$.
- We then apply a strengthened first isomorphism theorem for modules:

> Hungerford Ch.4 Thm 1.7: if $f:A\to B$ is an $R\dash$module morphism and $C\leq \ker f$, then there is a unique map $\tilde f: A/C\to B$, which is an isomorphism iff $f$ is an epimorphism and $C = \ker f$.
>
> Following Hungerford Ch.4 Prop. 5.4, p.210.

- Since $\im(f\tensor_R \id_N)\subseteq \ker(g\tensor_R \id_N)$, the theorem gives the map $\alpha$ satisfying the same formula, i.e. $\alpha = \tilde g \tensor \tilde{\id_N}$ where the tilde denotes the induced map on quotients, so $\alpha([b\tensor n]) = g(b)\tensor n$.
- We show it is an isomorphism, which forces $\im(f\tensor_R \id_N) \cong \ker(g\tensor_R \id_N)$ by the above theorem.
- Constructing the inverse map: define
\[
\tilde \alpha^{-1}: C\cross N &\to {B\tensor_R N \over \im(f\tensor_R \id_N) } \\
(c, n) &\mapsto (b \tensor n) \mod \im(f\tensor_R \id_N) {\quad \operatorname{where} \quad} b \in g^{-1}(c)
,\]
which we show is well-defined (independent of the choice of $b$) and $R\dash$linear, lifting to a map $\alpha^{-1}$ out of the tensor product by the universal property, which is a two-sided inverse for $\alpha$.

Well-defined:

- $g^{-1}(c)$ is nonempty because $g$ is surjective.
- If $b\neq b'$ and $g(b) = g(b')$, then $0 = g(b) - g(b') = g(b-b')$, so $b-b' \in \ker g$.
- By the original exactness, $b-b' \in \im f$, so $b-b' = f(a)$ for some $a\in A$.
- Then $f(a) \tensor n \in \im(f\tensor \id)$, so $f(a)\tensor n \equiv 0 \mod \im(f\tensor \id)$.
- Noting $b-b' = f(a) \implies b = f(a) + b'$, working mod $\im(f\tensor_R \id_N)$,
\[
b \tensor n \equiv (f(a) + b') \tensor n \equiv \qty{f(a) \tensor n} + \qty{b' \tensor n} \equiv b'\tensor n
.\]

$R\dash$linear: ?

Two-sided inverse:

- $(\alpha \circ \alpha^{-1})(c\tensor n) = \alpha(b\tensor n) = g(b)\tensor n = c\tensor n$, so $\alpha\circ \alpha^{-1}= \id$.
- $(\alpha^{-1}\circ \alpha)([b\tensor n]) = \alpha^{-1}(g(b) \tensor n) = [b'\tensor n]$ where $b'\in g^{-1}(g(b))$, so $\alpha^{-1}\circ\alpha = \id$.
:::

::: {.remark}
Erratum: the argument above is unfinished and contains the following errors.

- The map $i : (B\tensor_R N)/\im(f\tensor \id_N) \to (B\tensor_R N)/\ker(g\tensor \id_N)$ induced by $\im(f\tensor \id_N) \subseteq \ker(g\tensor \id_N)$ is a surjection, not an injection; it is injective exactly when the two submodules are equal, which is the claim to be proved.
- Elements of $\im(f\tensor \id_N)$ are finite sums of tensors $f(a)\tensor n$, not single tensors $b\tensor n$; the inclusion $\im(f\tensor\id_N) \subseteq \ker(g\tensor\id_N)$ is checked on these generators.
- An isomorphism $\alpha$ gives $\ker(g\tensor\id_N) = \im(f\tensor\id_N)$ as submodules, not merely an abstract isomorphism $\cong$: the kernel of $\alpha$ is $\ker(g\tensor\id_N)/\im(f\tensor\id_N)$.
- The bilinearity of $(c, n) \mapsto [b\tensor n]$ is left as "?". If $g(b) = c$ and $g(b') = c'$, then $g(b+b') = c+c'$ and $g(rb) = rc$, so the map is additive and $R$-linear in $c$; it is additive and $R$-linear in $n$ because $b \tensor n$ is. Without this the inverse $\alpha^{-1}$ on $C\tensor_R N$ is not defined.

The opening remark's question has a negative answer: $f\tensor g$ comes from the universal property applied to the bilinear map $(x, a) \mapsto f(x)\tensor g(a)$, and the natural map $\hom(X,Y)\tensor_R\hom(A,B) \to \hom(X\tensor_R A, Y\tensor_R B)$ is not an isomorphism in general.
:::
