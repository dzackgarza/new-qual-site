---
schema: qual/card@1
id: P-EP64S
kind: problem
title: Galois group and intermediate fields of the splitting field of $x^4-7$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Every claim checked: E = Q(a,i) and [E:Q] = 8 (Eisenstein at 7, and i not in the real field Q(a)); the two automorphisms are exhibited with their images and the relations sigma^4 = tau^2 = 1 and tau sigma tau = sigma^{-1} verified on the generators; the identification with the dihedral group of order 8 from the normal form and the count |G| = 8; the subgroup lattice (three of order 4, five of order 2, with the Klein four-group {1, sigma^2, tau, sigma^2 tau} and the two order-4 subgroups containing sigma^2 accounted for); and each of the eight fixed fields, by checking that the displayed generator is fixed and that its field has the degree [E : H] forced by the subgroup order. The invariance computations are all done: sigma^2(a) = -a; sigma^2 tau(a) = -a, sigma^2 tau(i) = -i so ia is fixed; sigma tau(a) = ia with a(1+i) -> ia(1-i) = a(1+i); sigma^3 tau(a) = -ia with a(1-i) -> (-ia)(1+i) = a(1-i); and (a(1 +- i))^4 = -28 with x^4 + 28 Eisenstein at 7. One passage in my first draft of the third quadratic field was muddled and is corrected in place: Q(i a^2) = Q(sqrt(-7)) is identified by the index, not by a degree computation that did not fit. No statement repair: parts (a) and (b) of the card are correct, including the group D4 and all eight fields.
---

::: {.problem}
Consider the polynomial $f(x) = x^4 - 7 \in \QQ[x]$ and let $E/\QQ$ be the splitting field of $f$.

a. What is the structure of the Galois group of $E/\QQ$?

b. Give an explicit description of all of the intermediate subfields $\QQ \subset K \subset E$ in the form $K = \QQ(\alpha), \QQ(\alpha, \beta), \cdots$ where $\alpha, \beta$, etc are complex numbers.
Describe the corresponding subgroups of the Galois group.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Put $a=\sqrt[4]{7}>0$. The roots of $x^4-7$ are $a,-a,ia,-ia$, so $E=\QQ(a,i)$. Throughout, for a subgroup $H\le G=\Gal(E/\QQ)$, the fundamental theorem gives $[E:E^H]=\cardinality H$, which is how each fixed field below is pinned down: a field $F\subseteq E^H$ with $[E:F]=\cardinality H$ must equal $E^H$.

::: pf

::: {.pf-step #degree}
$[E:\QQ]=8$.

::: pf-proof
$x^4-7$ is Eisenstein at the prime $7$ ($7\mid-7$, $7\mid0$ and $7^2\nmid-7$), hence irreducible, so $[\QQ(a):\QQ]=4$ and $1,a,a^2,a^3$ is a $\QQ$-basis. Since $\QQ(a)\subseteq\RR$ and $i\notin\RR$, $i\notin\QQ(a)$; as $i^2=-1$, $[\QQ(a,i):\QQ(a)]=2$, so $[E:\QQ]=4\cdot2=8$. Also $E$ is the splitting field of a separable polynomial over $\QQ$, so $E/\QQ$ is Galois and $\cardinality G=8$.
:::

:::

::: {.pf-step #automorphisms}
There are $\sigma,\tau\in G$ with $\sigma(a)=ia$, $\sigma(i)=i$, $\tau(a)=a$, $\tau(i)=-i$, and $\sigma^4=\tau^2=\operatorname{id}$, $\tau\sigma\tau=\sigma^{-1}$.

::: pf-proof
$(ia)^4=i^4a^4=7$, so $ia$ is a root of $x^4-7$; a $\QQ$-homomorphism $\QQ(a)\to E$ is determined by the image of $a$, which must be a root of $x^4-7$, so $a\mapsto ia$ defines one. Extending it to $E=\QQ(a,i)$ by $i\mapsto i$ gives a $\QQ$-homomorphism $E\to E$, injective because $E$ is a field, hence bijective since $E$ is finite-dimensional over $\QQ$: an automorphism $\sigma$. Its image contains $ia$ and $i$, hence contains $a=-i(ia)$, so it is all of $E$, confirming this. Similarly $a\mapsto a$, $i\mapsto-i$ is a $\QQ$-automorphism $\tau$ (complex conjugation restricted to $E$). Then $\sigma^4(a)=i^4a=a$ and $\sigma^4(i)=i$, so $\sigma^4=\operatorname{id}$, and $\sigma^2(a)=-a\ne a$, so $\sigma$ has order $4$; $\tau^2=\operatorname{id}$. For the relation, both sides fix $\QQ$ and agree on the generators: $\tau\sigma\tau(a)=\tau(\sigma(a))=\tau(ia)=-ia=\sigma^{-1}(a)$, and $\tau\sigma\tau(i)=\tau(\sigma(-i))=\tau(-i)=i=\sigma^{-1}(i)$.
:::

:::

::: {.pf-step #parta}
$G=\langle\sigma,\tau\rangle\cong D_4=\langle\sigma,\tau\mid\sigma^4=\tau^2=1,\ \tau\sigma\tau=\sigma^{-1}\rangle$, the dihedral group of order $8$.

::: pf-proof
The displayed relations make $\langle\sigma,\tau\rangle$ a quotient of the dihedral group of order $8$, and it contains the $8$ distinct elements $1,\sigma,\sigma^2,\sigma^3,\tau,\sigma\tau,\sigma^2\tau,\sigma^3\tau$: writing every word in normal form $\sigma^j\tau^\epsilon$ with $0\le j\le3$, $\epsilon\in\{0,1\}$ by using $\tau\sigma=\sigma^{-1}\tau$ repeatedly, there are at most $8$ such words, and $\cardinality G=8$ by step [](#degree){.pf-ref}. So $\langle\sigma,\tau\rangle=G$ and $G$ is dihedral of order $8$. This is part (a).
:::

:::

::: {.pf-step #lattice}
The subgroups of $G$ are: $G$; the three of order $4$, namely $\langle\sigma\rangle$, $\langle\sigma^2,\tau\rangle$, $\langle\sigma^2,\sigma\tau\rangle$; the five of order $2$, namely $\langle\sigma^2\rangle$, $\langle\tau\rangle$, $\langle\sigma^2\tau\rangle$, $\langle\sigma\tau\rangle$, $\langle\sigma^3\tau\rangle$; and $\{1\}$.

::: pf-proof
A subgroup of index $2$ is the kernel of a surjection $G\to C_2$, and conversely; so the subgroups of order $4$ are the kernels of the nontrivial homomorphisms $G\to C_2$. Such a homomorphism is determined by the images of $\sigma$ and $\tau$, and every choice in $C_2\times C_2$ is realised: writing the images additively in $\{0,1\}$, the relation $\sigma^4=1$ becomes $4\bar\sigma=0$, $\tau^2=1$ becomes $2\bar\tau=0$, and $\tau\sigma\tau=\sigma^{-1}$ becomes $2\bar\sigma=0$ after using $\bar\sigma=-\bar\sigma$ in $C_2$ — all automatic. Hence there are four homomorphisms, three of them nontrivial, and the three kernels are
$$
\ker(\sigma\mapsto1,\ \tau\mapsto-1)=\langle\sigma\rangle,\qquad
\ker(\sigma\mapsto-1,\ \tau\mapsto1)=\langle\sigma^2,\tau\rangle,\qquad
\ker(\sigma\mapsto-1,\ \tau\mapsto-1)=\langle\sigma^2,\sigma\tau\rangle .
$$
Indeed $\sigma^j\tau^\epsilon$ lies in the first kernel exactly when $(-1)^\epsilon=1$, i.e. $\epsilon=0$, giving all $\sigma^j$; in the second exactly when $(-1)^j=1$, i.e. $j$ even, giving $\sigma^{2k}\tau^\epsilon=\langle\sigma^2,\tau\rangle$; and in the third exactly when $(-1)^{j+\epsilon}=1$, i.e. $j\equiv\epsilon\pmod 2$, and those elements are the $\sigma^{2k}$ together with $\sigma^{2k}\sigma\tau$ because $(\sigma\tau)^2=\sigma\tau\sigma\tau=\sigma\sigma^{-1}\tau\tau=1$, giving $\langle\sigma^2,\sigma\tau\rangle$. So these are exactly the three subgroups of order $4$.
For order $2$: a subgroup of order $2$ is $\{1,x\}$ with $x$ its unique nonidentity element, so the subgroups of order $2$ correspond bijectively to the elements of order $2$, which are $\sigma^2,\tau,\sigma\tau,\sigma^2\tau,\sigma^3\tau$ — five elements, all distinct — giving the five displayed subgroups. Together with $G$ and $\{1\}$ this is the whole lattice, since every subgroup has order $1,2,4$ or $8$.
:::

:::

::: {.pf-step #quadratic}
The fixed fields of the three subgroups of order $4$ are
$$
E^{\langle\sigma\rangle}=\QQ(i),\qquad
E^{\langle\sigma^2,\tau\rangle}=\QQ(a^2)=\QQ(\sqrt7),\qquad
E^{\langle\sigma^2,\sigma\tau\rangle}=\QQ(ia^2)=\QQ(\sqrt{-7}).
$$

::: pf-proof
A subgroup $H$ of order $4$ has $[E:E^H]=\cardinality H=4$ by the fundamental theorem, so its fixed field has degree $8/4=2$ over $\QQ$; hence it suffices in each case to exhibit a subfield of degree $2$ inside $E^H$, since a degree-$2$ extension has only itself as a degree-$2$ subfield.
(i) $\sigma$ fixes $i$, so $\QQ(i)\subseteq E^{\langle\sigma\rangle}$, and $[\QQ(i):\QQ]=2$.
(ii) $\sigma^2(a)=i^2a=-a$ gives $\sigma^2(a^2)=a^2$, and $\tau$ fixes $a$ and hence $a^2$; so $\QQ(a^2)=\QQ(\sqrt7)\subseteq E^{\langle\sigma^2,\tau\rangle}$, and $\sqrt7\notin\QQ$ gives degree $2$.
(iii) $\sigma^2$ fixes $i$ and $a^2$, hence fixes $ia^2$; and $\sigma\tau$ sends $a\mapsto\sigma(a)=ia$ and $i\mapsto\sigma(-i)=-i$, so $ia^2\mapsto(-i)(ia)^2=(-i)(-a^2)=ia^2$. Thus $\QQ(ia^2)\subseteq E^{\langle\sigma^2,\sigma\tau\rangle}$, and $ia^2$ is a root of $x^2+7$, so this field has degree $2$ over $\QQ$ (it is $\QQ(\sqrt{-7})$, and $\sqrt{-7}\notin\QQ$).
:::

:::

::: {.pf-step #quartic}
The fixed fields of the five subgroups of order $2$ are
$$
E^{\langle\sigma^2\rangle}=\QQ(i,a^2)=\QQ(i,\sqrt7),\quad
E^{\langle\tau\rangle}=\QQ(a),\quad
E^{\langle\sigma^2\tau\rangle}=\QQ(ia),
$$
$$
E^{\langle\sigma\tau\rangle}=\QQ\bigl(a(1+i)\bigr),\qquad
E^{\langle\sigma^3\tau\rangle}=\QQ\bigl(a(1-i)\bigr).
$$

::: pf-proof
Again each displayed field lies in the corresponding fixed field and has degree $2$ over $\QQ$, while the fixed field of a subgroup of order $2$ has degree $8/2=4$ over $\QQ$; so each display is the fixed field.
(i) $\sigma^2$ fixes $i$ and $a^2$, so $\QQ(i,\sqrt7)\subseteq E^{\langle\sigma^2\rangle}$; this is a biquadratic extension of degree $4$ since $i\notin\QQ(\sqrt7)$ ($\QQ(\sqrt7)\subseteq\RR$).
(ii) $\tau$ fixes $a$, so $\QQ(a)\subseteq E^{\langle\tau\rangle}$ and $[\QQ(a):\QQ]=4$.
(iii) $\sigma^2\tau$ sends $a\mapsto-a$ and $i\mapsto-i$, so it fixes $ia$; and $[\QQ(ia):\QQ]=4$ because $(ia)^4=7$ and $x^4-7$ is irreducible.
(iv) and (v) $\sigma\tau$ sends $a\mapsto ia$, $i\mapsto-i$; hence $a(1+i)\mapsto ia(1-i)=ia+a=a(1+i)$, so $\sigma\tau$ fixes $a(1+i)$, and $\sigma^3\tau$ sends $a\mapsto-ia$, $i\mapsto-i$, so $a(1-i)\mapsto(-ia)(1+i)=-ia+a=a(1-i)$. Finally $\bigl(a(1\pm i)\bigr)^4=a^4(1\pm i)^4=7\cdot(\pm2i)^2=7\cdot(-4)=-28$, and $x^4+28$ is Eisenstein at $7$, hence irreducible, so $\QQ(a(1\pm i))$ has degree $4$ over $\QQ$.
:::

:::

::: {.pf-step}
The correspondence is complete: $G\leftrightarrow\QQ$ and $\{1\}\leftrightarrow E=\QQ(a,i)$, and the three quadratic and five quartic fields above are all the intermediate fields.

::: pf-proof
$E^G=\QQ$ because $E/\QQ$ is Galois with group $G$ (step [](#degree){.pf-ref}), and $E^{\{1\}}=E$. Steps [](#lattice){.pf-ref}, [](#quadratic){.pf-ref} and [](#quartic){.pf-ref} pair every subgroup with its fixed field, and by the fundamental theorem of Galois theory the map $H\mapsto E^H$ is a bijection onto the intermediate fields, so the list is exhaustive. This is part (b).
:::

:::

:::
:::
