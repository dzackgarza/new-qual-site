For which γ is $M _ { \gamma }$ positive?

What is det $\ ( \mathcal { M } _ { \gamma } ) ?$

(h) Find the matrix of $M _ { \gamma }$ in the basis $\{ 1 , i \}$

(i) If T is a linear operator on V, find necessary and sufficient conditions for $\tau$ to be an $M _ { \gamma }$

(i)Find a unitary operator on V which is not an $M _ { \gamma }$

4. Let V be $R ^ { 2 } ,$ with the standard inner product. If U is a unitary operator on $V ,$ show that the matrix of U in the standard ordered basis is either

$$
\left[ \sin \theta \begin{array} { c c } { { \cos \theta } } & { { - \sin \theta } } \\ { { \sin \theta } } & { { \cos \theta } } \end{array} \right] \quad \mathrm { o r } \quad \left[ \begin{array} { c c } { { \cos \theta } } & { { \sin \theta } } \\ { { \sin \theta } } & { { - \cos \theta } } \end{array} \right]
$$

for some real $\theta , 0 \leq \theta < 2 \pi$ . Let $U _ { \theta }$ be the linear operator corresponding to the first matrix, i.e., $U _ { \theta }$ is rotation through the angle θ. Now convince yourself that every unitary operator on V is either a rotation, or reflection about the er-axis followed by a rotation.

a)What is $U _ { \vartheta } U _ { \phi } ?$

Show that $U _ { \theta } ^ { * } = U _ { - \theta } .$

cLet $\phi$ be a fixed real number, and let $\mathbb { B } = \{ \alpha _ { 1 } , \alpha _ { 2 } \}$ be the orthonormal basis obtained by rotating $\{ \epsilon _ { 1 } , \epsilon _ { 2 } \}$ through the angle φ, i.e., $\alpha _ { i } = U _ { \phi } \epsilon _ { i }$ If θ is another real number, what is the matrix of $U _ { \theta }$ in the ordered basis B?

5. Let V be $R ^ { 3 } ,$ with the standard inner product. Let W be the plane spanned by $\alpha = ( 1 , 1 , 1 )$ and $\beta = ( 1 , 1 , - 2 )$ . Let U be the linear operator defined, geometrically, as follows: U is rotation through the angle θ, about the straight line through the origin which is orthogonal to W. There are actually two such rotations —choose one. Find the matrix of U in the standard ordered basis. (Here is one way you might proceed. Find $\pmb { \alpha _ { 1 } }$ and $\alpha _ { 2 }$ which form an orthonormal basis for W. Let $\alpha _ { 3 }$ be a vector of norm I which is orthogonal to W. Find the matrix of U in the basis $\{ \alpha _ { 1 } , \alpha _ { 2 } , \alpha _ { 3 } \}$ . Perform a change of basis.)

6. Let V be a finite-dimensional inner product space, and let $W$ be a subspace of V. Then $V = W \oplus W ^ { \perp }$ , that is, each α in V is uniquely expressible in the form $\alpha = \beta + \gamma ,$ with $\beta$ in W and γ in $W ^ { \downarrow }$ . Define a linear operator U by $U \alpha = \beta - \gamma$ I n 1 , rY. 1 1 ^ 1.

(a) Prove that U is both self-adjoint and unitary.

If V is $R ^ { 3 }$ with the standard inner product and W is the subspace spanned by (1, 0, 1), find the matrix of U in the standard ordered basis.

7. Let V be a complex inner product space and T a self-adjoint linear operator on V. Show that

(a) $| | \alpha + i T \alpha | | = | | \alpha - i T \alpha | |$ for every α in V.

(b) $\alpha + i T \alpha = \beta + i T \beta$ if and only if $\alpha \ : = \ : \beta .$

(c) $I + i T$ is non-singular.

(d) $I - i T$ is non-singular.

(e) Now suppose V is finite-dimensional, and prove that

$$
U = \langle I - i T \rangle ( I + i T ) ^ { - 1 }
$$

is a unitary operator; U is called the Cayley transform of T. In a certain sense, $U = f ( T )$ , where $f ( x ) = ( 1 - i x ) / ( 1 + i x )$

8. If θ is a real number, prove that the following matrices are unitarily equivalent

$$
{ \begin{array} { r l } { { \mathord { \left[ \cos \theta \right. \kern - delimiterspace } \cos \theta \left. \right] } , \ } & { { \mathord { \left[ \begin{array} { l l } { e ^ { i \theta } } & { 0 } \\ { 0 } & { e ^ { - i \theta } } \end{array} \right] } } . } \end{array} }
$$

9. Let V be a finite-dimensional inner product space and T a positive linear operator on V. Let $p _ { T }$ be the inner product on V defined by $p _ { T } ( \alpha , \beta ) = ( T \alpha | \beta )$ Let U be a linear operator on V and $U ^ { * }$ its adjoint with respect to $( \quad | \quad )$ Prove that U is unitary with respect to the inner product $p _ { T }$ if and only if $T = U ^ { * } T U$

10. Let V be a finite-dimensional inner product space. For each $\alpha , ~ \beta$ in $V ,$ let $T _ { \alpha , \beta }$ be the linear operator on V defined by $T _ { \alpha , \beta } ( \gamma ) = ( \gamma | \beta ) \alpha ,$ Show that

(a) $T _ { \alpha , \beta } ^ { * } = T _ { \beta , \alpha } .$

()trace $( T _ { \alpha , \beta } ) = ( \alpha | \beta )$

(c) $T _ { \alpha , \beta } T _ { \gamma , \delta } = T _ { \alpha , ( \beta \mid \gamma ) \delta } .$

(d) Under what conditions is $T _ { \alpha , \beta }$ self-adjoint?

11. Let V be an n-dimensional inner product space over the field F, and let $L ( V , V )$ be the space of linear operators on V. Show that there is a unique inner product on $L ( V , V )$ with the property that $\| T _ { \alpha , \beta } \| ^ { 2 } = | | \alpha | | ^ { 2 } | | \beta | | ^ { 2 }$ for all $\alpha , \beta$ in $V . ~ ( T _ { \alpha , \beta }$ is the operator defined in Exercise 10.) Find an isomorphism between $L ( V , V )$ with this inner product and the space of $n \times n$ matrices over $F ,$ with the inner product $( A | B ) = \mathrm { t r } \left( A B ^ { * } \right)$ •

12. Let V be a finite-dimensional inner product space. In Exercise 6, we showed how to construct some linear operators on V which are both self-adjoint and unitary. Now prove that there are no others, i.e., that every self-adjoint unitary operator arises from some subspace W as we described in Exercise 6.

13. Let V and W be finite-dimensional inner product spaces having the same dimension. Let U be an isomorphism of V onto W. Show that:

(a) The mapping $T  U T U ^ { - 1 }$ is an isomorphism of the vector space $L ( V , V )$ onto the vector space $L ( W , W )$

() trace $( U T U ^ { - 1 } ) = \operatorname { t r a c e } \left( T \right)$ for each T in $L ( V , V )$

(c) $U T _ { \alpha , \beta } U ^ { - 1 } = T _ { U \alpha , U \beta } \ ( T _ { \alpha , \beta }$ defined in Exercise 10).

(d) $( U T U ^ { - 1 } ) ^ { * } = U T ^ { * } U ^ { - 1 } .$

If we equip $L ( V , V )$ with inner product $( T _ { 1 } | T _ { 2 } ) = \mathrm { t r a c e } ( T _ { 1 } T _ { 2 } ^ { * } )$ , and similarly for $L ( W , W )$ , then $T \to U T U ^ { - 1 }$ is an inner product space isomorphism.

14. If V is an inner product space, a rigid motion is any function T from V into V (not necessarily linear) such that $| | T \alpha - T \beta | | = | | \alpha - \beta | |$ for all $\alpha , \beta$ in V. One example of a rigid motion is a linear unitary operator. Another example is translation by a fixed vector $\gamma$

$$
T _ { \gamma } ( \alpha ) = \alpha + \gamma
$$

(a Let V be $R ^ { 2 }$ with the standard inner product. Suppose $T$ is a rigid motion of V and that $T ( 0 ) = 0$ . Prove that T is linear and a unitary operator.

(b) Use the result of part (a) to prove that every rigid motion of $R ^ { 2 }$ is composed of a translation, followed by a unitary operator.

(c) Now show that a rigid motion of $R ^ { 2 }$ is either a translation followed by a rotation, or a translation followed by a reflection followed by a rotation.

15. A unitary operator on $R ^ { 4 }$ (with the standard inner product) is simply a linear operator which preserves the quadratic form

$$
| | ( x , y , z , t ) | | ^ { 2 } = x ^ { 2 } + y ^ { 2 } + z ^ { 2 } + t ^ { 2 }
$$

that is, a linear operator U such that $\| U \alpha \| ^ { 2 } = \| \alpha \| ^ { 2 }$ for all α in $R ^ { 4 }$ In a certain part of the theory of relativity, it is of interest to find the linear operators $T$ which preserve the form

$$
| | ( x , y , z , t ) | | _ { L } ^ { 2 } = t ^ { 2 } - x ^ { 2 } - y ^ { 2 } - z ^ { 2 } .
$$

Now $| { \bf \underline { { { \sf \vert } } } } | \quad | | _ { L } ^ { \bf 2 }$ does not come from an inner product, but from something called the 'Lorentz metric' (which we shall not go into). For that reason, a linear operator $\boldsymbol { T }$ on $R ^ { 4 }$ such that $| | T \alpha | | _ { L } ^ { 2 } = | | \alpha | | _ { L } ^ { 2 }$ , for every α in $R ^ { 4 } ,$ is called a Lorentz transformation.

(a) Show that the function U defined by

$$
U ( x , y , z , t ) = { \left[ \begin{array} { l l } { t + x } & { y + i z } \\ { y - i z } & { t - x } \end{array} \right] }
$$

is an isomorphism of $R ^ { 4 }$ onto the real vector space H of all self-adjoint $2 \times 2$ complex matrices.

(b) Show that $| | \alpha | | _ { L } ^ { 2 } = \operatorname* { d e t } \left( U \alpha \right)$

(cSuppose $T$ is a (real) linear operator on the space H of $2 \times 2$ self-adjoint matrices. Show that $L = U ^ { - 1 } T U$ is a linear operator on $R ^ { 4 } .$

(d) Let M be any $2 \times 2$ complex matrix. Show that $T _ { M } ( A ) = M ^ { * } A M$ defines a linear operator $T _ { M }$ on H. (Be sure you check that $T _ { M }$ maps H into H.)

If M is a $2 \times 2$ matrix such that |det $M \vert = 1$ , show that $L _ { M } = \left. U ^ { - 1 } T _ { M } U \right.$ is a Lorentz transformation on $R ^ { 4 }$

(f) Find a Lorentz transformation which is not an $L _ { M }$

## 8.5. Normal Operators

The principal objective in this section is the solution of the following problem. If $T$ is a linear operator on a finite-dimensional inner product space V, under what conditions does V have an orthonormal basis consisting of characteristic vectors for $T ?$ In other words, when is there an orthonormal basis ® for V, such that the matrix of T in the basis © is diagonal?

We shall begin by deriving some necessary conditions on $T ,$ which we shall subsequently show are sufficient. Suppose $\mathbb { \ B } = \{ \alpha _ { 1 } , \dots , \alpha _ { n } \}$ is an orthonormal basis for V with the property

$$
T \alpha _ { j } = c _ { j } \alpha _ { j } , \qquad j = 1 , \ldots , n .\tag{8-16}
$$

This simply says that the matrix of $T$ in the ordered basis © is the diagonal matrix with diagonal entries $c _ { 1 } , \ldots , c _ { n }$ The adjoint operator $\boldsymbol { T } ^ { * }$ is represented in this same ordered basis by the conjugate transpose matrix, i.e., the diagonal matrix with diagonal entries $\overline { { c } } _ { 1 } , \ldots , \overline { { c } } _ { n } ,$ If V is a real inner