---
schema: qual/card@1
id: P-APAS04I
kind: problem
title: Frobenius reciprocity and transitivity of induced representations
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $H$ be a subgroup of a finite group $G$ and $A\colon H\to GL(n,\mathbb{C})$ be a representation of $H$.

(a) Prove that for any character $\phi$ of $G$, $(\chi^{A\uparrow_H^G},\phi)_G=(\chi^A,\phi\downarrow^G_H)_H$.

(b) Given an example to show that it is not always the case that if $A$ is irreducible, then $A\uparrow_H^G$ is irreducible.

(c) Prove that if $K$ is a subgroup of $H$ and $B\colon K\to GL(m,\mathbb{C})$ is a representation of $K$, then the representation $B\uparrow_K^G$ is similar to the representation $(B\uparrow_K^H)\uparrow_H^G$.
:::

::: {.solution}
<1>1. For any character $\phi$ of $G$,
\[
(\chi^{A\uparrow_H^G},\phi)_G
=(\chi^A,\phi\downarrow_H^G)_H.
\]
::: {.proof}
The induced-character formula is
\[
\chi^{A\uparrow_H^G}(g)
=\frac1{|H|}\sum_{\substack{x\in G\\x^{-1}gx\in H}}
\chi^A(x^{-1}gx).
\]
Therefore
\[
\begin{aligned}
(\chi^{A\uparrow_H^G},\phi)_G
&=\frac1{|G|}\sum_{g\in G}
\chi^{A\uparrow_H^G}(g)\overline{\phi(g)}\\
&=\frac1{|G||H|}
\sum_{x\in G}\sum_{h\in H}
\chi^A(h)\overline{\phi(xhx^{-1})}.
\end{aligned}
\]
Because characters are class functions,
\[
\phi(xhx^{-1})=\phi(h).
\]
Thus the inner sum is independent of $x$, and
\[
\begin{aligned}
(\chi^{A\uparrow_H^G},\phi)_G
&=\frac1{|H|}\sum_{h\in H}
\chi^A(h)\overline{\phi(h)}\\
&=(\chi^A,\phi\downarrow_H^G)_H.
\end{aligned}
\]
This is Frobenius reciprocity.
:::

<1>2. An irreducible representation can induce to a reducible representation.
::: {.proof}
Take
\[
G=C_2=\{1,s\},\qquad H=\{1\}.
\]
The unique one-dimensional representation $A$ of the trivial group $H$ is irreducible. Its induction to $G$ is the regular representation
\[
A\uparrow_H^G\cong\mathbb C[G],
\]
which decomposes as
\[
\mathbb C[G]\cong \mathbf1\oplus\operatorname{sgn}.
\]
Hence $A\uparrow_H^G$ is reducible.
:::

<1>3. If $K\le H\le G$ and $B$ is a representation of $K$, then
\[
B\uparrow_K^G
\cong
(B\uparrow_K^H)\uparrow_H^G.
\]
::: {.proof}
Using the group-algebra construction of induction,
\[
B\uparrow_K^H
=\mathbb C[H]\otimes_{\mathbb C[K]}B
\]
and hence
\[
(B\uparrow_K^H)\uparrow_H^G
=\mathbb C[G]\otimes_{\mathbb C[H]}
\bigl(\mathbb C[H]\otimes_{\mathbb C[K]}B\bigr).
\]
Define
\[
\Phi:\mathbb C[G]\otimes_{\mathbb C[H]}
\bigl(\mathbb C[H]\otimes_{\mathbb C[K]}B\bigr)
\longrightarrow
\mathbb C[G]\otimes_{\mathbb C[K]}B
\]
by
\[
\Phi(g\otimes(h\otimes v))=gh\otimes v.
\]
This is well-defined because the balancing relations over $\mathbb C[H]$ and $\mathbb C[K]$ map to the balancing relation in the target.

Conversely define
\[
\Psi(g\otimes v)=g\otimes(1\otimes v).
\]
This is well-defined over $\mathbb C[K]$: for $k\in K$,
\[
\Psi(gk\otimes v)
=gk\otimes(1\otimes v)
=g\otimes(k\otimes v)
=g\otimes(1\otimes kv)
=\Psi(g\otimes kv).
\]
The maps $\Phi$ and $\Psi$ are inverse to one another and commute with the left $G$-action. Therefore they give an isomorphism of $G$-representations, proving transitivity of induction.
:::
:::
