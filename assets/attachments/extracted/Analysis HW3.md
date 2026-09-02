# Math 8100 Assignment 3 Lebesgue measurable sets and functions

Due date: 5:00 pm Friday the 20th of September 2019

1. (a) Prove that for every $E \subseteq \mathbb { R } ^ { n }$ there exists a Borel set $B \supseteq E$ with the property that $m ( B ) = m _ { * } ( E )$

(b) Prove that if $E \subseteq \mathbb { R } ^ { n }$ is Lebesgue measurable, then there exists a Borel set $B \subseteq E$ with the property that $m ( B ) = m ( E )$

(c) Prove that if $E \subseteq \mathbb { R } ^ { n }$ is Lebesgue measurable with $m ( E ) < \infty$ , then for every $\varepsilon > 0$ there exists a set A that is a finite union of closed cubes such that $m ( E { \triangle } A ) < \varepsilon$

[Recall that $E \triangle A$ stands for the symmetric difference, defined by $E \triangle A = ( E \setminus A ) \cup ( A \setminus E ) ]$

2. Let E be a Lebesgue measurable subset of $\mathbb { R } ^ { n }$ with $m ( E ) > 0$ and $\varepsilon > 0$

(a) Prove that E “almost” contains a closed cube in the sense that there exists a closed cube $Q$ such that $m ( E \cap Q ) \geq ( 1 - \varepsilon ) m ( Q )$

(b) Prove that the so-called difference set $E - E : = \{ d : d = x - y$ with $x , y \in E \}$ necessarily contains an open ball centered at the origin.

Hint: It may be useful to observe that $d \in E - E \Longleftrightarrow E \cap ( E + d ) \neq \emptyset$

3. We say that a function $f : \mathbb { R } ^ { n }  \mathbb { R }$ is upper semicontinuous at a point x in $\mathbb { R } ^ { n }$ if

$$
f ( x ) \geq \operatorname* { l i m } _ { y \to x } f ( y ) .
$$

Prove that if $f$ is upper semicontinuous at every point x in $\mathbb { R } ^ { n }$ , then $f$ is Borel measurable.

4. Let $\left\{ f _ { n } \right\}$ be a sequence of measurable functions on $\mathbb { R } ^ { n }$ . Prove that $\{ x \in \mathbb { R } ^ { n } : \operatorname* { l i m } _ { n \to \infty } f _ { n } ( x )$ exists} defines a measurable set.

5. Recall that the Cantor set $\mathcal { C }$ is the set of all $x \in [ 0 , 1 ]$ that have a ternary expansion $\textstyle x = \sum _ { k = 1 } ^ { \infty } a _ { k } 3 ^ { - k }$ with $a _ { k } \neq 1$ for all k. Consider the function

$$
f ( x ) = \sum _ { k = 1 } ^ { \infty } b _ { k } 2 ^ { - k } \mathrm { w h e r e } b _ { k } = a _ { k } / 2 .
$$

(a) Show that f is well defined and continuous on ${ \mathcal { C } } ,$ and moreover $f ( 0 ) = 0$ as well as $f ( 1 ) = 1$

(b) Prove that there exists a continuous function that maps a measurable set to a non-measurable set.

6. Let us examine the map f defined in Question 5 even more closely.
   One readily sees that if $x , y \in { \mathcal { C } }$ and $x < y .$ , then $f \left( x \right) < f \left( y \right)$ unless x and y are the two endpoints of one of the intervals removed from [0, 1] to obtain C. In this case $f ( x ) = \ell 2 ^ { m }$ for some integers \` and m, and $f ( x )$ and $f ( y )$ are the two binary expansions of this number.
   We can therefore extend f to a map $F : [ 0 , 1 ]  [ 0 , 1 ]$ by declaring it to be constant on each interval missing from C. F is called the Cantor-Lebesgue function.

(a) Prove that F is non-decreasing and continuous.

(b) Let $G ( x ) = F ( x ) + x$ . Show that G is a bijection from [0, 1] to [0, 2].

(c) i. Show that $m ( G ( \mathcal { C } ) ) = 1$

ii.
By considering rational translates of $\mathcal { N }$ (the non-measurable subset of [0, 1] that we constructed in class), prove that $G ( \mathcal { C } )$ necessarily contains a (Lebesgue) non-measurable set $\mathcal { N } ^ { \prime }$ iii.
Let $E = G ^ { - 1 } ( \mathcal { N } ^ { \prime } )$ . Show that E is Lebesgue measurable, but not Borel.

(d) Give an example of a measurable function ϕ such that $\varphi \circ G ^ { - 1 }$ is not measurable.

Hint: Let $\varphi$ be the characteristic function of a null set whose image under G is not measurable.

## Extra Challenge Problems Not to be handed in with the assignment

1. Let $\chi _ { [ 0 , 1 ] }$ be the characteristic function of [0, 1]. Show that there is no function f satisfying $f = \chi _ { [ 0 , 1 ] }$ almost everywhere which is also continuous on all of R.

2. Question 6d above supplies us with an example that if f and g are Lebesgue measurable, then it does not necessarily follow that $f \circ g$ will be Lebesgue measurable, even if $g$ is assumed to be continuous.
   Prove that if f is Borel measurable, then $f \circ g$ will be Lebesgue or Borel measurable whenever g is.

3. Let f be a measurable function on [0, 1] with $| f ( x ) | < \infty$ for a.e. x. Prove that there exists a sequence of continuous functions $\left\{ g _ { n } \right\}$ on [0, 1] such that $g _ { n }  f$ for a.e. $x \in [ 0 , 1 ]$
