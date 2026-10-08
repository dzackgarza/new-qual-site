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

::: {.problem}
Show that the endofunctor
\[
F: \mods{R} &\to \mods{R} \\
X &\mapsto X\tensor_R N \\
(X\xrightarrow{f} Y) &\mapsto (X\tensor_R N \xrightarrow{f \tensor \id_N} Y\tensor_R N)
\]
is right exact.
:::

::: {.solution}
Let $R$ be a commutative ring, $N$ an $R$-module, and
\[
A\xrightarrow{f}B\xrightarrow{g}C\longrightarrow0
\]
an exact sequence of $R$-modules. Set $Q=(B\otimes_R N)/\operatorname{im}(f\otimes_R\operatorname{id}_N)$, with quotient map $q:B\otimes_R N\to Q$.

<1>1. The morphism $g\otimes_R\operatorname{id}_N:B\otimes_R N\to C\otimes_R N$ is surjective, and its composite with $f\otimes_R\operatorname{id}_N$ is zero.

::: {.proof}
For each $c\in C$, surjectivity of $g$ supplies $b\in B$ with $g(b)=c$. Thus every elementary tensor $c\otimes n$ is the image of $b\otimes n$, and elementary tensors generate $C\otimes_R N$. Moreover,
\[
(g\otimes\operatorname{id}_N)(f\otimes\operatorname{id}_N)
=(gf)\otimes\operatorname{id}_N=0
\]
because $gf=0$ by exactness of the original sequence.
:::

<1>2. There is a well-defined $R$-linear map $\beta:C\otimes_R N\to Q$ characterized by
\[
\beta(g(b)\otimes n)=q(b\otimes n).
\]

::: {.proof}
Since $\ker g=\operatorname{im}f$, two lifts $b,b'\in B$ of $c\in C$ differ by $f(a)$ for some $a\in A$. Hence
\[
q(b\otimes n)-q(b'\otimes n)
=q(f(a)\otimes n)=0.
\]
Consequently the formula $(c,n)\mapsto q(b\otimes n)$, with any lift $g(b)=c$, is independent of the lift. Lifts of $c+c'$ and $rc$ can be chosen as $b+b'$ and $rb$, respectively, while the tensor-product relations give additivity in $n$ and
\[
q((rb)\otimes n)=q(b\otimes rn).
\]
The formula is therefore $R$-balanced and additive in both variables, and the universal property of $C\otimes_R N$ yields the claimed $R$-linear map.
:::

<1>3. The induced map $\alpha:Q\to C\otimes_R N$ is an isomorphism with inverse $\beta$.

::: {.proof}
By step <1>1, the map $g\otimes_R\operatorname{id}_N$ factors uniquely through $q$, giving $\alpha$ with
\[
\alpha(q(b\otimes n))=g(b)\otimes n.
\]
For all $b\in B$, $c\in C$, and $n\in N$, step <1>2 gives
\[
\beta\alpha(q(b\otimes n))=q(b\otimes n),
\qquad
\alpha\beta(c\otimes n)=c\otimes n.
\]
Elementary tensors generate both targets, so the composites are identities. In particular,
\[
\ker(g\otimes_R\operatorname{id}_N)
=\operatorname{im}(f\otimes_R\operatorname{id}_N).
\]
:::

<1>4. The functor $({-})\otimes_R N$ is right exact.

::: {.proof}
Step <1>1 proves surjectivity onto $C\otimes_R N$, and step <1>3 establishes exactness at $B\otimes_R N$. Thus the sequence
\[
A\otimes_R N\xrightarrow{f\otimes\operatorname{id}_N}
B\otimes_R N\xrightarrow{g\otimes\operatorname{id}_N}
C\otimes_R N\longrightarrow0
\]
is exact.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the asserted right exactness for an arbitrary exact sequence.
:::
:::
