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
---

::: {.problem}
Consider the polynomial $f(x) = x^4 - 7 \in \QQ[x]$ and let $E/\QQ$ be the splitting field of $f$.

a. What is the structure of the Galois group of $E/\QQ$?

b. Give an explicit description of all of the intermediate subfields $\QQ \subset K \subset E$ in the form $K = \QQ(\alpha), \QQ(\alpha, \beta), \cdots$ where $\alpha, \beta$, etc are complex numbers.
Describe the corresponding subgroups of the Galois group.
:::

::: {.solution}
Put
\[
a=\sqrt[4]{7}>0.
\]
The roots of $x^4-7$ are $\pm a,\pm ia$, so
\[
E=\QQ(a,i).
\]
By Eisenstein's criterion at $7$, $x^4-7$ is irreducible over $\QQ$, hence
$[\QQ(a):\QQ]=4$. Since $\QQ(a)\subset\RR$, it does not contain $i$, and
therefore
\[
[E:\QQ]=8.
\]

Define automorphisms $\sigma,\tau\in\operatorname{Gal}(E/\QQ)$ by
\[
\sigma(a)=ia,\qquad \sigma(i)=i,
\]
and
\[
\tau(a)=a,\qquad \tau(i)=-i.
\]
Then
\[
\sigma^4=\tau^2=1,
\qquad
\tau\sigma\tau=\sigma^{-1}.
\]
These automorphisms generate eight distinct elements, so
\[
\boxed{\operatorname{Gal}(E/\QQ)
\cong D_4=\langle\sigma,\tau\mid
\sigma^4=\tau^2=1,\ \tau\sigma\tau=\sigma^{-1}\rangle,}
\]
where $D_4$ denotes the dihedral group of order $8$.

We now list every subgroup and its fixed field. The three subgroups of order
$4$ give the three quadratic subfields:
\[
\begin{array}{c|c}
\text{subgroup} & \text{fixed field}\\ \hline
\langle\sigma\rangle & \QQ(i)\\
\langle\sigma^2,\tau\rangle & \QQ(a^2)=\QQ(\sqrt7)\\
\langle\sigma^2,\sigma\tau\rangle & \QQ(ia^2)=\QQ(\sqrt{-7}).
\end{array}
\]
For example, $\sigma$ fixes $i$; both $\sigma^2$ and $\tau$ fix $a^2$;
and both $\sigma^2$ and $\sigma\tau$ fix $ia^2$. Since in each case the
displayed field has degree $2$ over $\QQ$, it is the full fixed field.

The five subgroups of order $2$ give the five quartic subfields:
\[
\begin{array}{c|c}
\text{subgroup} & \text{fixed field}\\ \hline
\langle\sigma^2\rangle & \QQ(i,a^2)=\QQ(i,\sqrt7)\\
\langle\tau\rangle & \QQ(a)\\
\langle\sigma^2\tau\rangle & \QQ(ia)\\
\langle\sigma\tau\rangle & \QQ(a(1+i))\\
\langle\sigma^3\tau\rangle & \QQ(a(1-i)).
\end{array}
\]
The invariance assertions are immediate from the definitions. For instance,
$\sigma^2\tau$ sends $a\mapsto-a$ and $i\mapsto-i$, so it fixes $ia$;
$\sigma\tau$ fixes $a(1+i)$; and $\sigma^3\tau$ fixes $a(1-i)$.
Each displayed field has degree $4$ over $\QQ$: this is clear for
$\QQ(a)$ and $\QQ(ia)$ from $x^4-7$, for $\QQ(i,a^2)$ because it is the
biquadratic extension $\QQ(i,\sqrt7)$, and for $a(1\pm i)$ because
\[
(a(1\pm i))^4=-28
\]
and $x^4+28$ is Eisenstein at $7$. Thus these are exactly the fixed fields of
the corresponding order-$2$ subgroups.

Finally,
\[
\langle\sigma,\tau\rangle\longleftrightarrow\QQ,
\qquad
\{1\}\longleftrightarrow E=\QQ(a,i).
\]
These are all subgroups of $D_4$, hence by the fundamental theorem of Galois
theory the table lists all intermediate fields.
:::
