---
schema: qual/card@1
id: P-FLLFZ
kind: problem
title: Galois groups of $\mathbb{Q}(\sqrt{2+\sqrt{2}})/\mathbb{Q}$ and of $x^3-5$
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked all parts of Fields 4 on PDF page 2; corrected the printed leading exponent from two to four and retained the source hint separately."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both Eisenstein applications, recovery of the second quartic radical, the exact four-cycle of the automorphism, and the cubic degree, root action, and proper Galois subfield."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Fields and Galois Theory (4) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAF4, whose solution repeats this argument."
---

::: {.problem}
1. Show that $\sqrt{2+\sqrt{2}}$ is a root of $p(x) = x^4 - 4x^2 + 2 \in \mathbb{Q}[x]$.

2. Prove that $\mathbb{Q}(\sqrt{2 + \sqrt{2}})$ is a Galois extension of $\mathbb{Q}$ and find its Galois group.

3. Let $f(x) = x^3 - 5$.
   Determine the splitting field $K$ of $f(x)$ over $\mathbb{Q}$ and the Galois group of $f(x)$.
   Give an example of a proper sub-extension $\mathbb{Q} \subset L \subset K$, such that $L/\mathbb{Q}$ is Galois.
:::

::: {.hint}
The number $\sqrt{2-\sqrt2}$ is another root of $p(x)$.
:::

::: {.remark}
The leading term must be $x^4$. The expression
$x^2-4x^2+2$ evaluates to $-4-3\sqrt2\ne0$
at $x=\sqrt{2+\sqrt2}$.
:::

::: {.solution}
Put $a=\sqrt{2+\sqrt2}>0$ and $b=\sqrt{2-\sqrt2}>0$.

<1>1. The number $a$ has minimal polynomial
$p(x)=x^4-4x^2+2$ over $\mathbb Q$.

::: {.proof}
Since $a^2-2=\sqrt2$, squaring gives
$(a^2-2)^2=2$, or $a^4-4a^2+2=0$.
The polynomial is Eisenstein at two, so it is
irreducible over $\mathbb Q$ [@DF04]. Thus it is
the minimal polynomial and $[\mathbb Q(a):\mathbb Q]=4$.
:::

<1>2. The extension $\mathbb Q(a)/\mathbb Q$ is
Galois with cyclic group of order four.

::: {.proof}
The four roots of $p$ are $a,-a,b,-b$: their squares
are the two roots $2+\sqrt2,2-\sqrt2$ of
$y^2-4y+2$. These four real roots are distinct.
Moreover $ab=\sqrt2=a^2-2$, so
$$
b=\frac{a^2-2}{a}\in\mathbb Q(a).
$$
Thus this field contains every root and is the splitting
field of $p$, a separable polynomial. It is Galois
[@DF04].

Sending $a$ to the root $b$ of its minimal polynomial
defines a $\mathbb Q$-embedding $\sigma$ of $\mathbb Q(a)$
into itself. Its image is a four-dimensional rational
subspace, so it is onto and is an automorphism.
Applying it to $\sqrt2=a^2-2$ gives
$\sigma(\sqrt2)=b^2-2=-\sqrt2$. Consequently
$\sigma(b)=\sigma(\sqrt2/a)=-\sqrt2/b=-a$.
The successive images are
$$
a\longmapsto b\longmapsto-a\longmapsto-b\longmapsto a.
$$
Thus $\sigma$ has order four and its powers exhaust
the Galois group of order four. The group is $C_4$,
not the Klein four-group.
:::

<1>3. For $f(x)=x^3-5$, the splitting field and Galois
group are
$$
K=\mathbb Q(c,\zeta),\qquad
\operatorname{Gal}(K/\mathbb Q)\cong S_3,
\quad c=\sqrt[3]{5}>0,\quad \zeta=e^{2\pi i/3}.
$$

::: {.proof}
The roots are $c,\zeta c,\zeta^2c$. Their field
contains $c$ and their ratio $\zeta$, so it is
exactly $K$. Eisenstein at five makes $x^3-5$
irreducible [@DF04]. Thus $\mathbb Q(c)$ has degree
three. It is real, whereas $\zeta$ is nonreal and
satisfies $x^2+x+1=0$. Adjoining $\zeta$ therefore
has degree two, giving $[K:\mathbb Q]=6$.

As a splitting field in characteristic zero, $K$ is
Galois. Its automorphisms permute the three roots
faithfully because the roots generate $K$. Its order
six equals $|S_3|$, so it acts as every permutation.
More explicitly, a three-cycle is
$r(c)=\zeta c$, $r(\zeta)=\zeta$; it exists because
$[K:\mathbb Q(\zeta)]=3$ makes $x^3-5$ still minimal
over that field. Complex conjugation $s$ fixes $c$
and interchanges the other two roots. These give
$r^3=s^2=1$ and $srs=r^{-1}$ and generate the group.
:::

<1>4. A proper Galois subextension in part (3) is
$L=\mathbb Q(\zeta)$.

::: {.proof}
The field $L$ is the splitting field of $x^2+x+1$,
with two distinct roots $\zeta,\zeta^2$, so it is
Galois over $\mathbb Q$. Its degree is two because
its roots are nonreal and hence not rational.
Since $[K:\mathbb Q]=6$, both inclusions
$\mathbb Q\subsetneq L\subsetneq K$ are strict.
:::
:::
