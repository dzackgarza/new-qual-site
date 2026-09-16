---
schema: qual/card@1
id: P-MMAQ-HGDYVCO7CN
kind: problem
title: A finite field extension of a finite field is Galois with cyclic Galois group
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the inclusion and both conclusions with Fields 2 on PDF page 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the splitting-field identity, separability, the relative Frobenius automorphism and its exact order, including the trivial extension."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Fields and Galois Theory (2) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAF2, whose solution repeats this Frobenius argument."
---

::: problem
Let $K$ and $L$ be finite fields with $K \subseteq L$.
Prove that $L$ is Galois over $K$ and that $\mathrm{Gal}(L/K)$ is cyclic.
:::

::: solution
Write $q=|K|=p^r$, where $p$ is the characteristic,
and put $d=[L:K]$. Counting coordinates in a $K$-basis
gives $|L|=q^d$.

<1>1. The extension $L/K$ is Galois.

::: proof
The group $L^\times$ has order $q^d-1$, so every
$a\in L$ satisfies $a^{q^d}=a$, also for $a=0$.
The factor theorem and comparison of degrees give
$$
T^{q^d}-T=\prod_{a\in L}(T-a).
$$
Consequently $L$ is the splitting field over $K$ of
$T^{q^d}-T$: its roots are all the elements of $L$.
The derivative is $-1$, since $q^d$ is zero in
characteristic $p$, so the polynomial is separable.
A splitting field of a separable polynomial is a
Galois extension [@DF04].
:::

<1>2. The automorphism $\varphi(a)=a^q$ generates
$\operatorname{Gal}(L/K)$ and has order $d$.

::: proof
The characteristic-$p$ binomial identity, iterated
$r$ times, gives $(a+b)^q=a^q+b^q$.
Multiplication and the identity are preserved as well,
so $\varphi$ is an injective field homomorphism and
is surjective because $L$ is finite. For $a\in K$,
Lagrange's theorem in $K^\times$ gives $a^q=a$,
including zero. Thus $\varphi$ fixes $K$.

Step <1>1 gives $\varphi^d=1$. For $0<j<d$, equality
$\varphi^j=1$ would make all $q^d$ elements of $L$
roots of the nonzero polynomial $T^{q^j}-T$, whose
degree $q^j$ is smaller than $q^d$. The root bound
rules this out. Hence the order is exactly $d$.
Since a finite Galois group has order equal to the
extension degree [@DF04], these $d$ powers exhaust
$\operatorname{Gal}(L/K)$. It is therefore cyclic.
For $d=1$, this argument gives the trivial group.
:::
:::
