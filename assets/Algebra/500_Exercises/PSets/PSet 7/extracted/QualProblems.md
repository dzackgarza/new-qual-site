# Assignment 7 Qual Problems

D. Zack Garza

November 7, 2019

## Contents

1 Problem 1 1\
1.1 Part (a) 1\
1.2 Part (b) 1\
1.3 Part (c) 2\
2 Problem 2 2\
3 Problem 3 2

## 1 Problem 1

## 1.1 Part (a)

Definition: A field extension $L / F$ is said to be a splitting field of a polynomial $f ( x )$ if L contains all roots of $f$ and thus decomposes as

$$
f ( x ) = \prod _ { i = 1 } ^ { n } ( x - \alpha _ { i } ) ^ { k _ { i } } \in L [ x ]
$$

where $\alpha _ { i }$ are the distinct roots of f and $k _ { i }$ are the respective multiplicities.

## 1.2 Part (b)

Let F be a finite field with q elements, where $q = p ^ { k }$ is necessarily a prime power, so $F \cong \mathbb { F } _ { p ^ { k } }$ Then any finite extension of $E / F$ is an F -vector space, and contains $q ^ { n } = ( p ^ { k } ) ^ { n } = p ^ { k n }$ elements.
Thus $E \cong \mathbb { F } _ { p ^ { k n } }$ Then if $\alpha \in E$ , we have $\alpha ^ { p ^ { k n } } = \alpha$ , so we can define

$$
f ( x ) : = x ^ { p ^ { k n } } - x \in F [ x ] .
$$

The roots of f are exactly the elements of E, so f splits in $E$

## 1.3 Part (c)

The polynomial f is separable, since $f ^ { \prime } ( x ) = p ^ { k n } x ^ { p ^ { k n } - 1 } - 1 = - 1$ since $\operatorname { c h a r } ( E ) = p $ . Since E is a finite extension, E is thus a separable extension.
Then, since E is a separable splitting field, it is a Galois extension by definition.

## 2 Problem 2

We can write $I = \mathrm { A n n } _ { \mu }$ for some $\mu \in R ,$ so suppose xy ∈ I so $x y \mu = 0$

If $y \mu = 0$ , then $y \in I$

Otherwise, $y \mu \neq 0$ and $x \in \mathrm { A n n } _ { y \mu }$ . But by maximality, $\mathrm { A n n } _ { y \mu } \subseteq I , \mathrm { s o } x \in I$

## 3 Problem 3

Let $I \leq R ,$ then since R is a PID we have $I = ( b )$ for some $b \in R$ . We can write $( b ) = R b ;$ if $a \in I$ is an irreducible element, we’d like to show that $R b = R a$ •

Note that since $a \in ( b )$ , we have $( a ) \subseteq ( b )$ and thus $R a \subseteq R b$

Since $a \in R b$ , we have $a = r b$ for some $r \in R$ . Since a is irreducible, either r is a unit or b is a unit.

If r is a unit, then $a = r b \implies r ^ { - 1 } a = b$ . But then $x \in R b \implies x = r ^ { \prime } b = r ^ { \prime } r ^ { - 1 } a \in R a$ , so $R b \subseteq R a$ and thus $R a = R b = I$

Otherwise, if b is a unit, $a = r b \implies R a = R$ . But any ideal containing a unit is the entire ring, so $R b = ( b ) = R$ as well, so again $R a = I$
