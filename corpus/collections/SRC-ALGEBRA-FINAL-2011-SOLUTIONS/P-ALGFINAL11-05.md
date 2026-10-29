---
schema: qual/card@1
id: P-ALGFINAL11-05
kind: problem
title: Galois group of X^6+aX^3+1
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f ( X ) = X ^ { 6 } + a X ^ { 3 } + 1 \in \ZZ [ X ]$ be irreducible, and let $\mathcal G \subset S _ { 6 }$ be its galois group.
(Analyzing possible factorizations, it is not hard to show—but you needn’t do so now—that f is reducible $\iff a = p ^ { 3 } - 3 p$ for some $p \in \ZZ . )$

Let $F$ be a splitting field of $f \ ( \mathrm { o v e r } \ \QQ )$

(a) Show that $\mathrm { i f } \ | a | \geq 2$ then $f$ has a real root $x ,$ and that with ω a primitive cube root of unity, the other roots are ωx, $\omega ^ { 2 } x , 1 / x , \omega / x$ , and $\omega ^ { 2 } / x$ [6]

(b) Show that $\mathcal { G }$ is isomorphic to the order-12 dihedral group $D _ { 1 2 }$

[10]

Hint.
Show that there is an order-6 automorphism ψ of F with $\psi x = \omega / x$ and $\psi \omega = \omega ^ { 2 }$ . Also, complex conjugation gives an automorphism γ of order 2.

(c) For x as in $\mathrm { ( a ) }$ , it is easily seen—and you may assume—that $x + 1 / x , \omega x + 1 / ( \omega x )$ and $\omega ^ { 2 } x + 1 / ( \omega ^ { 2 } x )$ make up a single $\mathcal { G } _ { \mathrm { - o r b i t } }$ , and are distinct roots of $X ^ { 3 } - 3 X + a$

Show that there are precisely three fields $E \subset F$ such that $[ E : \QQ ] = 3$ , that these are conjugate to each other, and that each is generated over $\QQ$ by a root of $X ^ { 3 } - 3 X + a$ . [9]

Total points:[80]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
Since $f$ is irreducible, $a\ne\pm2$; thus the hypothesis $|a|\ge2$ actually gives $|a|>2$.

::: pf-proof
If $a=2$, then
$$
f(X)=(X^3+1)^2,
$$
and if $a=-2$, then
$$
f(X)=(X^3-1)^2.
$$
Both are reducible, contrary to hypothesis.
:::

:::

::: {.pf-step #s1-2}
The polynomial $f$ has a real root $x$, and its six roots are
$$
\boxed{x,\ \omega x,\ \omega^2x,\ x^{-1},\ \omega x^{-1},\ \omega^2x^{-1}}.
$$

::: pf-proof
Put
$$
t=X^3.
$$
Then $f(X)=0$ is equivalent to
$$
t^2+at+1=0.
$$
Since $|a|>2$ by step [](#s1-1){.pf-ref}, the discriminant $a^2-4$ is positive, so this quadratic has two distinct nonzero real roots
$$
t_\pm=\frac{-a\pm\sqrt{a^2-4}}2,
$$
with
$$
t_+t_-=1.
$$
Choose a real cube root $x$ of one root, say $x^3=t_+$. Then
$$
x^{-3}=t_-=t_+^{-1}.
$$
The cube roots of $x^3$ are $x,\omega x,\omega^2x$, and the cube roots of $x^{-3}$ are $x^{-1},\omega x^{-1},\omega^2x^{-1}$. These are all six roots of $f$. Since $f$ is irreducible over $\QQ$ in characteristic zero, it is separable, so the six roots are distinct.
:::

:::

::: {.pf-step #s1-3}
The splitting field is
$$
F=\QQ(x,\omega)
$$
and
$$
[F:\QQ]=12.
$$

::: pf-proof
Step [](#s1-2){.pf-ref} shows that all roots lie in $\QQ(x,\omega)$, so this is the splitting field. Since $f$ is irreducible of degree $6$,
$$
[\QQ(x):\QQ]=6.
$$
The element $x$ is real, so $\QQ(x)\subset\RR$, while $\omega\notin\RR$. Hence
$$
[\QQ(x,\omega):\QQ(x)]=2,
$$
and therefore
$$
[F:\QQ]=2\cdot6=12.
$$
:::

:::

::: {.pf-step #s1-4}
There is an automorphism $\psi\in\Gal(F/\QQ)$ such that
$$
\psi(x)=\frac{\omega}{x},
\qquad
\psi(\omega)=\omega^2.
$$

::: pf-proof
Over $\QQ(\omega)$, the element $x$ still has degree $6$, because
$$
[F:\QQ(\omega)]=\frac{12}{2}=6.
$$
Thus $f$ is the minimal polynomial of $x$ over $\QQ(\omega)$.

Start with the nontrivial automorphism of $\QQ(\omega)/\QQ$, sending $\omega$ to $\omega^2$. The embedding-extension theorem allows it to extend to a $\QQ$-embedding of $F$ into an algebraic closure sending $x$ to any root of the conjugated minimal polynomial, which is again $f$. Choose the root $\omega/x$. Since $F/\QQ$ is normal, the resulting embedding has image $F$ and is an automorphism.
:::

:::

::: {.pf-step #s1-5}
The automorphism $\psi$ has order $6$.

::: pf-proof
Using step [](#s1-4){.pf-ref},
$$
\psi^2(x)
=\psi\left(\frac\omega x\right)
=\frac{\omega^2}{\omega/x}
=\omega x,
$$
and therefore
$$
\psi^3(x)=x^{-1},
\qquad
\psi^4(x)=\omega^2x,
\qquad
\psi^6(x)=x.
$$
Also $\psi$ interchanges $\omega$ and $\omega^2$, so $\psi^6(\omega)=\omega$. Hence $\psi^6=1$.

But $\psi^2(x)=\omega x\ne x$, and
$$
\psi^3(\omega)=\omega^2\ne\omega.
$$
Thus the order of $\psi$ is neither $1$, $2$, nor $3$; since it divides $6$, it is exactly $6$.
:::

:::

::: {.pf-step #s1-6}
If $\gamma$ is complex conjugation on $F$, then
$$
\gamma^2=1
\qquad\text{and}\qquad
\gamma\psi\gamma^{-1}=\psi^{-1}.
$$

::: pf-proof
Because $x$ is real,
$$
\gamma(x)=x,
\qquad
\gamma(\omega)=\omega^2.
$$
On the generators $x$ and $\omega$,
$$
(\gamma\psi\gamma)(x)
=\gamma\left(\frac\omega x\right)
=\frac{\omega^2}{x}
=\psi^{-1}(x),
$$
and
$$
(\gamma\psi\gamma)(\omega)
=\gamma\bigl(\psi(\omega^2)\bigr)
=\gamma(\omega)
=\omega^2
=\psi^{-1}(\omega).
$$
Thus the automorphisms agree on generators of $F$.
:::

:::

::: {.pf-step #s1-7}
The Galois group is
$$
\boxed{\Gal(F/\QQ)\cong D_{12}}.
$$

::: pf-proof
By step [](#s1-5){.pf-ref}, the subgroup
$$
C=\langle\psi\rangle
$$
has order $6$. Step [](#s1-6){.pf-ref} shows that $\gamma$ conjugates $\psi$ to $\psi^{-1}$, so $\gamma\notin C$ and
$$
\langle\psi,\gamma\rangle
$$
has the dihedral presentation
$$
\langle r,s:r^6=s^2=1,\ srs=r^{-1}\rangle.
$$
This subgroup has order $12$, equal to $|\Gal(F/\QQ)|$ by step [](#s1-3){.pf-ref}. Hence it is the whole Galois group.
:::

:::

::: {.pf-step #s1-8}
The group $D_{12}$ has exactly three subgroups of order $4$, and they are conjugate.

::: pf-proof
Write
$$
D_{12}=\langle\psi,\gamma:\psi^6=\gamma^2=1,\ \gamma\psi\gamma=\psi^{-1}\rangle.
$$
The element $\psi^3$ is the unique element of order $2$ in the rotation subgroup. Every Sylow $2$-subgroup has order $4$ and is generated by $\psi^3$ together with a reflection. The six reflections are
$$
\psi^k\gamma,
\qquad
0\le k<6,
$$
and the reflections with indices $k$ and $k+3$ generate the same subgroup with $\psi^3$. Thus the three Sylow $2$-subgroups are
$$
\langle\psi^3,\gamma\rangle,
\qquad
\langle\psi^3,\psi\gamma\rangle,
\qquad
\langle\psi^3,\psi^2\gamma\rangle.
$$
They are conjugate by Sylow's theorem.
:::

:::

::: {.pf-step #s1-9}
There are precisely three intermediate fields $E\subset F$ with
$$
[E:\QQ]=3,
$$
and they are conjugate.

::: pf-proof
By Galois correspondence and step [](#s1-7){.pf-ref}, such fields correspond to subgroups of
$$
\Gal(F/\QQ)
$$
of order
$$
\frac{12}{3}=4.
$$
Step [](#s1-8){.pf-ref} gives exactly three such subgroups, all conjugate. Their fixed fields are therefore exactly three degree-$3$ intermediate fields, also conjugate.
:::

:::

::: {.pf-step #s1-10}
Let
$$
u_0=x+x^{-1},
\qquad
u_1=\omega x+\omega^2x^{-1},
\qquad
u_2=\omega^2x+\omega x^{-1}.
$$
Then each $u_i$ is a root of
$$
h(T)=T^3-3T+a,
$$
and
$$
[\QQ(u_i):\QQ]=3.
$$

::: pf-proof
The problem allows the first assertion and states that the three roots form one Galois orbit and are distinct. Since $F/\QQ$ is Galois, the size of the Galois orbit of $u_i$ equals the degree of its minimal polynomial over $\QQ$. The orbit has size $3$, hence
$$
[\QQ(u_i):\QQ]=3.
$$
In particular, $h$ is irreducible over $\QQ$.
:::

:::

::: {.pf-step #s1-11}
The three degree-$3$ fields are exactly
$$
\boxed{\QQ(u_0),\quad\QQ(u_1),\quad\QQ(u_2)}.
$$

::: pf-proof
By step [](#s1-10){.pf-ref}, each displayed field has degree $3$. Their stabilizers in the Galois group have order $4$, hence are Sylow $2$-subgroups. By step [](#s1-8){.pf-ref} there are exactly three Sylow $2$-subgroups, so for any one of them $H$,
$$
[\Gal(F/\QQ):N_{\Gal(F/\QQ)}(H)]=3.
$$
Since $|\Gal(F/\QQ)|=12$, this gives $|N(H)|=4=|H|$, hence $N(H)=H$. Thus distinct points in the three-element Galois orbit have distinct stabilizers. Their stabilizers are therefore exactly the three Sylow $2$-subgroups from step [](#s1-8){.pf-ref}, and their fixed fields are precisely the three degree-$3$ fields from step [](#s1-9){.pf-ref}.
:::

:::

::: pf-qed
Step [](#s1-2){.pf-ref} proves part (a), step [](#s1-7){.pf-ref} proves part (b), and step [](#s1-9){.pf-ref} through step [](#s1-11){.pf-ref} prove part (c).
:::

:::

:::

::: {.remark}
The three quadratic subfields of $F$ are generated by $\sqrt{-3}$, $\sqrt{a^2-4}$, and $\sqrt{-3(a^2-4)}$. They correspond to the three index-two subgroups of $D_{12}$. The element $\sqrt{a^2-4}$ belongs to $F$ because $x^3=(-a\pm\sqrt{a^2-4})/2$.
:::
