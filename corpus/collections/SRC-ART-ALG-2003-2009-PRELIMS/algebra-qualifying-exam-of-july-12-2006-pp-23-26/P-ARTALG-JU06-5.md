---
schema: qual/card@1
id: P-ARTALG-JU06-5
kind: problem
title: Galois extension definition and fundamental theorem of Galois theory
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the finite-extension setting and both definition/theorem requests with July 2006 Fields 5 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the hypotheses, inverse maps, degree formulas, and the distinction between K/E being Galois and E/F requiring a normal subgroup."
---

::: {.problem}
Let $K$ and $F$ be fields, with $K$ a finite-dimensional algebraic extension of $F$.

(a) Give the definition of "$K$ is a Galois extension of $F$".

(b) State the Fundamental Theorem of Galois Theory.
:::

::: {.solution}
<1>1. Definition for part (a).

The finite extension $K/F$ is **Galois** if it is both normal and
separable. Normality means that every irreducible polynomial in
$F[x]$ with a root in $K$ splits into linear factors in $K[x]$.
Separability means that the minimal polynomial over $F$ of every
element of $K$ has distinct roots in an algebraic closure of $F$.
Its Galois group is
$$
\operatorname{Gal}(K/F)
=\{\sigma:K\to K:\sigma\text{ is a field automorphism and }
\sigma(a)=a\text{ for all }a\in F\},
$$
with composition as the group operation.

<1>2. The fundamental theorem for part (b).

Assume now that $K/F$ is finite Galois, and set
$G=\operatorname{Gal}(K/F)$. Then the following statements hold
[@DF04].

<2>1. There is an inclusion-reversing bijection between intermediate
fields $F\subseteq E\subseteq K$ and subgroups $H\leq G$, given by
$$
E\longmapsto\operatorname{Gal}(K/E),\qquad
H\longmapsto K^H
=\{a\in K:\sigma(a)=a\text{ for every }\sigma\in H\}.
$$
The maps are inverse:
$$
K^{\operatorname{Gal}(K/E)}=E,\qquad
\operatorname{Gal}(K/K^H)=H.
$$
Thus $F$ corresponds to $G$, and $K$ corresponds to the trivial
subgroup. For intermediate fields $E_1,E_2$,
$$
E_1\subseteq E_2
\quad\Longleftrightarrow\quad
\operatorname{Gal}(K/E_2)\subseteq\operatorname{Gal}(K/E_1).
$$

<2>2. For every intermediate field $E$, the extension $K/E$ is
Galois. With $H=\operatorname{Gal}(K/E)$, the degree formulas are
$$
[K:E]=|H|,\qquad [E:F]=[G:H],\qquad [K:F]=|G|.
$$

<2>3. The extension $E/F$ is Galois if and only if
$H=\operatorname{Gal}(K/E)$ is normal in $G$.
When these equivalent conditions hold, restriction to $E$ is a
surjective homomorphism
$$
G\longrightarrow\operatorname{Gal}(E/F)
$$
with kernel $H$, and therefore induces an isomorphism
$$
G/H\cong\operatorname{Gal}(E/F).
$$
:::
