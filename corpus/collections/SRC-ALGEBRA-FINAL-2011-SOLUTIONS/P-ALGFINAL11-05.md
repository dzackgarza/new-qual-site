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
Let $f ( X ) = X ^ { 6 } + a X ^ { 3 } + 1 \in \mathbb { Z } [ X ]$ be irreducible, and let $\mathcal G \subset S _ { 6 }$ be its galois group.
(Analyzing possible factorizations, it is not hard to show—but you needn’t do so now—that f is reducible $\iff a = p ^ { 3 } - 3 p$ for some $p \in \mathbb { Z } . )$

Let $F$ be a splitting field of $f \ ( \mathrm { o v e r } \ \mathbb { Q } )$

(a) Show that $\mathrm { i f } \ | a | \geq 2$ then $f$ has a real root $x ,$ and that with ω a primitive cube root of unity, the other roots are ωx, $\omega ^ { 2 } x , 1 / x , \omega / x$ , and $\omega ^ { 2 } / x$ [6]

(b) Show that $\mathcal { G }$ is isomorphic to the order-12 dihedral group $D _ { 1 2 }$

[10]

Hint.
Show that there is an order-6 automorphism ψ of F with $\psi x = \omega / x$ and $\psi \omega = \omega ^ { 2 }$ . Also, complex conjugation gives an automorphism γ of order 2.

(c) For x as in $\mathrm { ( a ) }$ , it is easily seen—and you may assume—that $x + 1 / x , \omega x + 1 / ( \omega x )$ and $\omega ^ { 2 } x + 1 / ( \omega ^ { 2 } x )$ make up a single $\mathcal { G } _ { \mathrm { - o r b i t } }$ , and are distinct roots of $X ^ { 3 } - 3 X + a$

Show that there are precisely three fields $E \subset F$ such that $[ E : \mathbb { Q } ] = 3$ , that these are conjugate to each other, and that each is generated over $\mathbb { Q }$ by a root of $X ^ { 3 } - 3 X + a$ . [9]

Total points:[80]
:::

::: {.solution}
(a) A real cube root x of $( - 1 + \sqrt { a ^ { 2 } - 4 } ) / 2$ is a root of $f .$ It is easy to check that if y is any root of f then $\omega y , \omega ^ { 2 } y , 1 / y , \omega / y$ , and $\omega ^ { 2 } / y$ are also roots.
Since $y \ne 0$ , therefore $y \ne$ ωy and $y \ne \omega ^ { 2 } y$ . If $y = \omega ^ { i } / y \ ( 0 \leq i \leq 2 )$ then $y ^ { 3 } = 1 / y ^ { 3 }$ , so $y ^ { 3 } = \pm 1$ , and $y ^ { 6 } + a y ^ { 3 } + 1 = 1 \pm a + 1 \neq 0$ because $a = \pm 2 \implies f$ reducible.
So $y \neq \omega ^ { i } / y ;$ and as before $y \neq \omega ^ { j } y \ ( j = 1 , 2 )$ . Thus the roots are distinct, and (a) results.

(b) By $( \mathrm { a } ) , F = \mathbb { Q } ( x , \omega )$ ; and since x is real and $\omega$ is not, and x is a root of a degree-6 irreducible polynomial, therefore

$$
| \mathcal { G } | = [ F : \mathbb { Q } ] = [ \mathbb { Q } ( x , \omega ) : \mathbb { Q } ( x ) ] [ \mathbb { Q } ( x ) : \mathbb { Q } ] = 2 \cdot 6 = 1 2 .
$$

The two automorphisms of $\mathbb { Q } ( \omega )$ extend to automorphisms of the splitting field $F$ (shown in class).
An extension θ is uniquely determined by $\theta ( x )$ , which is a root of $f ,$ so there are at most six extensions, and there must be exactly six because $F$ has twelve automorphisms.
In other words, for each root $y$ of $f _ { : }$ there is $\textrm { a } \theta$ with $\theta ( x ) = y$ . Thus the nonidentity automorphism of $\mathbb { Q } ( \omega )$ , which takes ω to $\omega ^ { 2 }$ , extends to an automorphism $\psi$ of $F$ with $\psi x = \omega / x$ . Then

$$
\psi ^ { 2 } ( x ) = \psi ( \omega / x ) = \omega ^ { 2 } / ( \omega / x ) = \omega x \neq x ,
$$

whence $\psi ^ { 4 } ( x ) = \omega ^ { 2 } x$ and $\psi ^ { 6 } ( x ) = x ,$ . Also $\psi ^ { 3 } ( \omega ) = \omega ^ { 2 } \ne \omega ;$ and $\psi ^ { 6 } ( \omega ) = \omega$ . Hence $\psi ^ { 6 }$ is the identity, while $\psi ^ { 2 }$ and $\psi ^ { 3 }$ are not—that is, $\psi$ has order 6. So ψ generates a cyclic subgroup $\mathcal { C } \subset \mathcal { G }$ , which is of index 2 and hence normal.

An easy calculation shows that $\gamma \psi \gamma ^ { - 1 } = \psi ^ { - 1 }$ . (Just apply both sides to x and to $\omega . )$ So γ is not contained in C (which is commutative), and hence generates a complement of $\mathcal { C } .$ Thus $\mathcal { G } \cong \mathbb { Z } _ { 2 } \rtimes _ { \phi } \mathbb { Z } _ { 6 }$ where φ takes the generator of $\mathbb { Z } _ { 2 }$ to the automorphism $\xi \mapsto \xi ^ { - 1 }$ of $\mathbb { Z } _ { 6 }$ that is, $\mathcal { G } \cong D _ { 1 2 }$

(c) Fields $E$ with $[ E : \mathbb { Q } ] = 3$ correspond 1-1 to order-4 subgroups of $\mathcal { G } \cong D _ { 1 2 }$ , i.e., to Sylow 2-subgroups, of which there must be 1 or 3. There can’t be 1, because, $\mathrm { e . g . } , D _ { 1 2 }$ has seven elements of order 2 (as one sees, e.g., by representing $D _ { 1 2 }$ as a group of symmetries of a regular hexagon), each of which is contained in a Sylow 2-subgroup.
So there are 3 subfields of degree 3, conjugate to each other (since that is true for the $\mathrm { S y }$ low 2-subgroups).

The polynomial $X ^ { 3 } - 3 X + a$ is irreducible over $\mathbb { Q } ,$ because it has the three given $\mathcal { G } _ { - }$ conjugate roots.
So any of these roots generates a degree-3 subfield, whose conjugates are the subfields generated (respectively) by the other two roots.
By the preceding paragraph, these must be the three sought-after subfields.

Supplementary exercise.
Prove that F has precisely three quadratic subfields, generated by the square roots of $- 3 , a ^ { 2 } - 4$ and $( - 3 ) ( a ^ { 2 } - 4 )$ , respectively.

Which one is the fixed field of C ? Which contains the discriminant of f? $\mathrm { O f } X ^ { 3 } - 3 X + a ?$
:::
