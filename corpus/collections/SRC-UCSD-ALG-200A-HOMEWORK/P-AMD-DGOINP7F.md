---
schema: qual/card@1
id: P-AMD-DGOINP7F
kind: problem
title: Automorphisms, inner automorphisms, and central displacement
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 3(a). Corrected
    a substantive transcription error: the source asks when sigma commutes
    with every inner automorphism, not when sigma conjugates Inn(G) to itself.
    The latter holds for every automorphism sigma.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    For the inner automorphism c_g, one has sigma c_g sigma^{-1}=c_{sigma(g)}.
    Thus sigma commutes with c_g exactly when c_{sigma(g)}=c_g, equivalently
    g^{-1}sigma(g) lies in Z(G). If G is centerless this forces sigma(g)=g
    for every g.
---

::: {.problem}
Let $G$ be a group, let
\[
A=\operatorname{Aut}(G),
\qquad
I=\operatorname{Inn}(G),
\]
and let $\sigma\in A$.

Prove that $\sigma$ commutes with every element of $I$ if and only if
\[
g^{-1}\sigma(g)\in Z(G)
\qquad\text{for every }g\in G.
\]
Deduce that if $G$ is centerless, then the only automorphism commuting with every inner automorphism is the identity.
:::

::: {.solution}
For $g\in G$, write
\[
c_g(x)=gxg^{-1}
\]
for the corresponding inner automorphism.

<1>1. For every $g\in G$,
\[
\sigma c_g\sigma^{-1}=c_{\sigma(g)}.
\]
::: {.proof}
For $x\in G$,
\[
\begin{aligned}
(\sigma c_g\sigma^{-1})(x)
&=\sigma\bigl(g\sigma^{-1}(x)g^{-1}\bigr)\\
&=\sigma(g)x\sigma(g)^{-1}\\
&=c_{\sigma(g)}(x).
\end{aligned}
\]
Thus the two automorphisms are equal.
:::

<1>2. For $a,b\in G$,
\[
c_a=c_b
\quad\Longleftrightarrow\quad
b^{-1}a\in Z(G).
\]
::: {.proof}
We have
\[
c_b^{-1}c_a=c_{b^{-1}a}.
\]
Hence $c_a=c_b$ exactly when $c_{b^{-1}a}$ is the identity automorphism.
An inner automorphism $c_z$ is the identity exactly when
\[
zxz^{-1}=x
\]
for every $x\in G$, which is equivalent to $z\in Z(G)$.
:::

<1>3. The automorphism $\sigma$ commutes with $c_g$ if and only if
\[
g^{-1}\sigma(g)\in Z(G).
\]
::: {.proof}
The equality
\[
\sigma c_g=c_g\sigma
\]
is equivalent to
\[
\sigma c_g\sigma^{-1}=c_g.
\]
By <1>1 this becomes
\[
c_{\sigma(g)}=c_g.
\]
Applying <1>2 with $a=\sigma(g)$ and $b=g$ gives precisely
\[
g^{-1}\sigma(g)\in Z(G).
\]
:::

<1>4. Therefore $\sigma$ commutes with every element of $I$ if and only if
\[
g^{-1}\sigma(g)\in Z(G)
\]
for every $g\in G$.
::: {.proof}
The inner automorphism group is
\[
I=\{c_g:g\in G\}.
\]
Apply <1>3 for every $g\in G$.
:::

<1>5. If $Z(G)=\{e\}$ and $\sigma$ commutes with every element of $I$, then
\[
\sigma=\operatorname{id}_G.
\]
::: {.proof}
By <1>4,
\[
g^{-1}\sigma(g)\in Z(G)=\{e\}
\]
for every $g\in G$.
Hence
\[
g^{-1}\sigma(g)=e,
\]
so $\sigma(g)=g$ for every $g\in G$.
Therefore $\sigma$ is the identity automorphism.
:::
:::
