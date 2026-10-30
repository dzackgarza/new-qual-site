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
Let $R$ be a ring and $N$ an $R$-module. Show that the endofunctor
$$
\begin{aligned}
F: \mods{R} &\to \mods{R} \\
X &\mapsto X\tensor_R N \\
(X\xrightarrow{f} Y) &\mapsto (X\tensor_R N \xrightarrow{f \tensor \id_N} Y\tensor_R N)
\end{aligned}
$$
is right exact.
:::

::: {.remark}
The morphism $f\tensor \id_N$ is defined by the universal property of the tensor product: the map $X\cross N\to Y\tensor_R N$, $(x, n)\mapsto f(x)\tensor n$, is $R$-bilinear, so it induces a unique $R$-linear map with $x\tensor n\mapsto f(x)\tensor n$.
More generally, $f\tensor g : X\tensor_R A\to Y\tensor_R B$ comes from the bilinear map $(x, a)\mapsto f(x)\tensor g(a)$.
No isomorphism $\hom_{\mods{R}}(X, Y) \tensor_R \hom_{\mods{R}}(A, B) \to \hom_{\mods{R}}(X\tensor_R A, Y\tensor_R B)$ is needed, and the natural map of this form is not an isomorphism in general.
:::

::: {.solution}
Let
$$
A\xrightarrow{f} B \xrightarrow{g} C \to 0
$$
be an exact sequence in $\mods{R}$, so $\ker g = \im f$ and $g$ is surjective.
Write $I \coloneqq \im(f\tensor \id_N) \subseteq B\tensor_R N$ and $Q\coloneqq (B\tensor_R N)/I$, and write $[x]$ for the class of $x\in B\tensor_R N$ in $Q$.
Every element of a tensor product is a finite sum of elementary tensors, so two $R$-linear maps out of a tensor product that agree on elementary tensors are equal.

::: pf

::: {.pf-step #surjective}
$g\tensor \id_N : B\tensor_R N\to C\tensor_R N$ is surjective.

::: pf-proof
Let $c\tensor n$ be an elementary tensor of $C\tensor_R N$.
Since $g$ is surjective, $c = g(b)$ for some $b\in B$, so $c\tensor n = (g\tensor \id_N)(b\tensor n)$.
The image of $g\tensor\id_N$ is a submodule that contains every elementary tensor, so it is all of $C\tensor_R N$.
:::

:::

::: {.pf-step #complex}
$I \subseteq \ker(g\tensor \id_N)$.

::: pf-proof
The composite $(g\tensor \id_N)\circ(f\tensor\id_N)$ sends each elementary tensor $a\tensor n$ of $A\tensor_R N$ to $g(f(a))\tensor n = 0\tensor n = 0$, because $g\circ f = 0$.
Hence the composite is the zero map, and every element of $I$ is in $\ker(g\tensor\id_N)$.
:::

:::

::: {.pf-step #induced}
There is an $R$-linear map $\bar g : Q\to C\tensor_R N$ with $\bar g([b\tensor n]) = g(b)\tensor n$, and $\ker \bar g = \ker(g\tensor\id_N)/I$.

::: pf-proof
By step [](#complex){.pf-ref}, $g\tensor\id_N$ vanishes on $I$, so it factors through the quotient $Q$.
A class $[x]\in Q$ maps to $0$ exactly when $x\in\ker(g\tensor\id_N)$.
:::

:::

::: {.pf-step #section-map}
There is an $R$-linear map $\beta : C\tensor_R N\to Q$ with $\beta(g(b)\tensor n) = [b\tensor n]$ for all $b\in B$ and $n\in N$.

::: pf-proof

::: {.pf-step #beta-well-defined}
The rule $\beta_0(c, n) \coloneqq [b\tensor n]$, for any $b\in B$ with $g(b) = c$, is a well-defined map $C\cross N\to Q$.

::: pf-proof
Such a $b$ exists because $g$ is surjective.
If $g(b) = g(b') = c$, then $b - b'\in \ker g = \im f$, so $b - b' = f(a)$ for some $a\in A$.
Then $b\tensor n - b'\tensor n = f(a)\tensor n = (f\tensor\id_N)(a\tensor n)\in I$, so $[b\tensor n] = [b'\tensor n]$.
:::

:::

::: {.pf-step #beta-bilinear}
$\beta_0$ is $R$-bilinear.

::: pf-proof
Let $g(b) = c$, $g(b') = c'$, and $r\in R$.
Then $g(b + b') = c + c'$ and $g(rb) = rc$, so by step [](#beta-well-defined){.pf-ref} these lifts compute $\beta_0$:
$$
\beta_0(c + c', n) = [(b+b')\tensor n] = [b\tensor n] + [b'\tensor n],
\qquad
\beta_0(rc, n) = [rb\tensor n] = r[b\tensor n].
$$
With the lift $b$ of $c$ fixed, $n\mapsto [b\tensor n]$ is additive and $R$-linear because $b\tensor n$ is additive and $R$-linear in $n$.
:::

:::

::: pf-qed
By the universal property of the tensor product, the bilinear map $\beta_0$ of steps [](#beta-well-defined){.pf-ref} and [](#beta-bilinear){.pf-ref} induces a unique $R$-linear map $\beta$ with $\beta(c\tensor n) = \beta_0(c, n)$; taking $c = g(b)$ gives the stated formula.
:::

:::

:::

::: {.pf-step #injective}
$\bar g$ is injective.

::: pf-proof
For every elementary tensor $b\tensor n$ of $B\tensor_R N$,
$$
\beta(\bar g([b\tensor n])) = \beta(g(b)\tensor n) = [b\tensor n]
$$
by steps [](#induced){.pf-ref} and [](#section-map){.pf-ref}.
The classes $[b\tensor n]$ generate $Q$, and $\beta\circ\bar g$ and $\id_Q$ are $R$-linear, so $\beta\circ\bar g = \id_Q$.
A map with a left inverse is injective.
:::

:::

::: {.pf-step #exact-middle}
$\ker(g\tensor \id_N) = \im(f\tensor\id_N)$.

::: pf-proof
By steps [](#induced){.pf-ref} and [](#injective){.pf-ref}, $\ker(g\tensor\id_N)/I = \ker\bar g = 0$, so $\ker(g\tensor\id_N)\subseteq I$.
Step [](#complex){.pf-ref} gives the reverse inclusion.
:::

:::

::: pf-qed
Steps [](#exact-middle){.pf-ref} and [](#surjective){.pf-ref} show that
$$
A\tensor_R N \xrightarrow{f\tensor \id_N} B\tensor_R N \xrightarrow{g\tensor \id_N} C\tensor_R N \to 0
$$
is exact at $B\tensor_R N$ and at $C\tensor_R N$.
This holds for every exact sequence $A\to B\to C\to 0$, so $F$ is right exact.
:::

:::
:::
