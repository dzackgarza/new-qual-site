---
schema: qual/card@1
id: P-APAS04D
kind: problem
title: External product of representations of a direct product of groups
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $G$ and $H$ be a finite groups, $A:G\to GL(n,\mathbb{C})$ be a representation of $G$ and $B:H\to GL(m,\mathbb{C})$ be a representation of $H$.

(a) Define the representation $A\times B:G\times H\to GL(n\cdot m,\mathbb{C})$.

(b) Show that if $A$ and $B$ are irreducible representations, then $A\times B$ is irreducible.

(c) Show that every irreducible representation of $G\times H$ is of the form $A\times B$ where $A$ is an irreducible representation of $G$ and $B$ is an irreducible representation of $H$.
:::

::: {.solution}

::: pf

::: pf-step
Let $V=\mathbb C^n$ and $W=\mathbb C^m$ be the representation spaces of $A$ and $B$.
Define
\[
(A\times B)(g,h)=A(g)\otimes B(h)
\]
on $V\otimes_{\mathbb C}W$.

::: pf-proof
For $(g_1,h_1),(g_2,h_2)\in G\times H$,
\[
\begin{aligned}
(A\times B)(g_1g_2,h_1h_2)
 &=A(g_1g_2)\otimes B(h_1h_2)\\
 &=(A(g_1)A(g_2))\otimes(B(h_1)B(h_2))\\
 &=(A(g_1)\otimes B(h_1))(A(g_2)\otimes B(h_2)).
\end{aligned}
\]
Also $(A\times B)(1,1)=I_V\otimes I_W$, so this is a representation of dimension $nm$.
:::

:::

::: {.pf-step #character-of-a-times-b}
Its character is
\[
\chi_{A\times B}(g,h)=\chi_A(g)\chi_B(h).
\]

::: pf-proof
For square matrices $X,Y$ one has
\[
\operatorname{tr}(X\otimes Y)=\operatorname{tr}(X)\operatorname{tr}(Y).
\]
Apply this with $X=A(g)$ and $Y=B(h)$.
:::

:::

::: {.pf-step #a-times-b-irreducible}
If $A$ and $B$ are irreducible, then $A\times B$ is irreducible.

::: pf-proof
Over $\mathbb C$, a finite-group representation is irreducible iff the inner product of its character with itself is $1$.
Using step [](#character-of-a-times-b){.pf-ref},
\[
\begin{aligned}
\langle\chi_{A\times B},\chi_{A\times B}\rangle_{G\times H}
&=\frac1{|G||H|}\sum_{g\in G}\sum_{h\in H}
  |\chi_A(g)|^2|\chi_B(h)|^2\\
&=\langle\chi_A,\chi_A\rangle_G
  \langle\chi_B,\chi_B\rangle_H\\
&=1.
\end{aligned}
\]
Thus $A\times B$ is irreducible.
:::

:::

::: {.pf-step #inner-product-of-external-products}
If $A_1,A_2$ are irreducible representations of $G$ and $B_1,B_2$ are irreducible representations of $H$, then
\[
\langle\chi_{A_1\times B_1},\chi_{A_2\times B_2}\rangle_{G\times H}
=
\langle\chi_{A_1},\chi_{A_2}\rangle_G
\langle\chi_{B_1},\chi_{B_2}\rangle_H.
\]

::: pf-proof
The same separation of the double sum used in step [](#a-times-b-irreducible){.pf-ref} gives the displayed equality.
:::

:::

::: {.pf-step #external-products-pairwise-noniso}
Therefore the representations $A\times B$, with $A\in\operatorname{Irr}(G)$ and $B\in\operatorname{Irr}(H)$, are pairwise nonisomorphic irreducible representations of $G\times H$.

::: pf-proof
By step [](#a-times-b-irreducible){.pf-ref} each is irreducible.
By step [](#inner-product-of-external-products){.pf-ref} and orthogonality of irreducible characters, the inner product is $1$ exactly when $A_1\cong A_2$ and $B_1\cong B_2$, and is $0$ otherwise.
:::

:::

::: pf-step
These external products exhaust all irreducible representations of $G\times H$.

::: pf-proof
Let $k(K)$ denote the number of conjugacy classes of a finite group $K$.
Two pairs $(g,h)$ and $(g',h')$ are conjugate in $G\times H$ iff $g$ is conjugate to $g'$ in $G$ and $h$ is conjugate to $h'$ in $H$.
Hence
\[
k(G\times H)=k(G)k(H).
\]
For every finite group over $\mathbb C$, the number of irreducible representations equals the number of conjugacy classes.
Therefore
\[
|\operatorname{Irr}(G\times H)|
=k(G\times H)
=k(G)k(H)
=|\operatorname{Irr}(G)|\,|\operatorname{Irr}(H)|.
\]
By step [](#external-products-pairwise-noniso){.pf-ref} we already have exactly this many pairwise nonisomorphic irreducible external products.
Thus every irreducible representation of $G\times H$ is of the form $A\times B$.
:::

:::

:::

:::
