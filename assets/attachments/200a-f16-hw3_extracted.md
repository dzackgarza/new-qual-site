# Math 200a (Fall 2016) - Homework 3

Professor D. Rogalski

Posted October 7th - Due October 14th at 3pm

## 1 Reading

Continue to read Sections 4.1-4.3 of the text on group actions, and begin to read sections 4.4-4.6.

## 2 Exercises to submit on Friday Oct. 14

Exercise 1. Assume that the group G acts transitively on a set X and let H be a normal subgroup of G. Then H also acts on X (by restricting the action to H), but this action might no longer be transitive. Let $\textstyle Y = \{ { \mathcal { O } } _ { \alpha } \} _ { \alpha \in I }$ be the set of orbits of the action of H on X, where α ranges over some index set I.

(a) For each $g \in G$ and orbit $\mathcal { O } _ { \alpha }$ define $g \mathcal { O } _ { \alpha } = \{ g x | x \in \mathcal { O } _ { \alpha } \}$ . Show that $g { \mathcal { O } } _ { \alpha } = { \mathcal { O } } _ { \alpha ^ { \prime } }$ for some $\alpha ^ { \prime }$ . Prove that the rule $g { \mathcal { O } } _ { \alpha } = { \mathcal { O } } _ { \alpha ^ { \prime } }$ defines an action of the group G on the set $Y .$ . Prove that this is a transitive action on $Y .$ , and conclude that $| \mathcal { O } _ { \alpha } | = | \mathcal { O } _ { \alpha ^ { \prime } } |$ for any $\alpha , \alpha ^ { \prime } \in I$

(b) Prove that if $x \in { \mathcal { O } } _ { \alpha }$ then $| \mathcal { O } _ { \alpha } | = | H : H \cap G _ { x } |$ and that $| Y | = | G : H G _ { x } |$ . (Recall that $G _ { x } = \{ g \in G | g x = x \} )$ .

Exercise 2. Let K be a conjugacy class in $S _ { n }$ for some $n \geq 3 .$ , that is, an orbit of the action of $S _ { n }$ on itself by conjugation. Restricting this action we obtain an action of $A _ { n }$ on $S _ { n }$ by conjugation.

(a) Show that either (i) K is also an orbit of the $A _ { n } { \mathrm { - a c t i o n } }$ on $S _ { n }$ , or else (ii) K is the union of two orbits of equal size under the $A _ { n } { \mathrm { - a c t i o n } }$

(b) Recall that the conjugacy classes of $S _ { n }$ are determined by the possible cycle shapes, so that there is some list of positive integers $k _ { 1 } , k _ { 2 } , \ldots . k _ { d }$ (possibly with repeats) such that K consists of all permutations whose disjoint cycle representation has cycles of lengths $k _ { 1 } , k _ { 2 } , \ldots , k _ { d }$ (including 1-cycles). Show that case (ii) occurs in part (a) if and only if the list $\{ k _ { i } \}$ consists of odd integers without repeats.

Exercise 3. Let G be a finite group and let H be a proper subgroup of $G$ (that is, $H \neq G )$ . Recall that a subgroup of the form $g H g ^ { - 1 }$ is called a conjugate of H.

(a) Show that the number of distinct conjugates of H is equal to $| G : N _ { G } ( H ) |$ |, where $N _ { G } ( H )$ is the normalizer of H in G.

(b) Prove that $G \neq \textstyle \bigcup _ { g \in G } g H g ^ { - 1 }$ . Thus a finite group cannot be equal to the union of the conjugates of a proper subgroup. (Hint: show that the union on the right hand side cannot have enough elements).

Exercise 4. In this exercise you will prove the following theorem often called Cauchy’s theorem: If G is a finite group and p is a prime dividing the order of G, then G has an element x of order $p .$

Fix a finite group G and a prime p dividing |G|. Let

$$
X = \{ ( a _ { 1 } , a _ { 2 } , \ldots , a _ { p } ) \in G ^ { p } | a _ { 1 } a _ { 2 } \ldots a _ { p } = e \} .
$$

In words, X is the set of (ordered) p-tuples of elements of G whose product in the given order is the identity element.

(a) Show that if $a _ { 1 } a _ { 2 } \ldots a _ { p } = e$ in a group G, then $a _ { 2 } a _ { 3 } \dots , a _ { p } a _ { 1 } = e$ as well.

(b) Using (a), show that there is an action of the cyclic group $K = ( \mathbb { Z } _ { p } , + )$ on X such that the generator 1 of K acts on $( a _ { 1 } , a _ { 2 } , \ldots , a _ { p } )$ and sends it to $( a _ { 2 } , a _ { 3 } , \dotsc , a _ { p } , a _ { 1 } )$

(c) Show that the orbits of size 1 under the action in (b) are precisely the p-tuples $( a , a , \ldots , a )$ where $a ^ { p } = e$

(d) Show that $| X | = | G | ^ { p - 1 }$

(e) Show that there must be more than one orbit of size 1 under the action in (b), and thus there is a nonidentity element a such that $a ^ { p } = e$ . Conclude that a is an element of order p in G, as desired.

Exercise 5. Let G be a finite group that acts transitively on a finite set X of size at least 2. Prove that there exists an element $g \in G$ that has no fixed points in X, i.e. gx 6= x for all $x \in X$ . (Hint: Burnside’s counting lemma.) Show that the same result holds true if G is infinite and X is finite, but give an example showing that we cannot remove the finiteness assumption on both G and X.

Exercise 6. Let H be a subgroup of a group G. Show that there exists a normal subgroup core(H), called the normal core of H in G, that enjoys the following equivalent properties:

(i) core(H) is the largest normal subgroup of G contained in H

(ii) core(H) is the subgroup generated by all normal subgroups contained in H

(iii) $\begin{array} { r } { \operatorname { c o r e } ( H ) = \bigcap _ { q \in G } g H g } \end{array}$ −1

(iv) core(H) is the kernel of the action of G on the set $G / H$ of left cosets of H in G by left multiplication.

Exercise 7. Let G be a group that has a proper subgroup H of finite index n.

(a) Prove that the index of core(H) divides n! (see exercise 6).

(b) If G happens to be a simple group, show that |G| divides n!; in particular, G is finite. (Recall that a group is said to be simple when it has no proper non-trivial normal subgroups.)

(c) Assuming the fact that the alternating group $A _ { n }$ is a simple group for all $n \geq 5$ (as we will prove later), show that if $n \geq 5$ then $A _ { n }$ has no subgroups of index less than n, but that $A _ { n }$ does have a subgroup of index exactly n.

Exercise 8. A jewelry store sells necklaces made out of r beads attached on a circular string. Using beads of n different colors, the owner made all the different necklace combinations possible. (Two necklaces are considered the same if they look exactly the same after some sequence of rotations and/or flips.) Out of convenience for the customer, he then stored the necklaces in boxes, putting all the same necklaces into the same box, and with precisely one type of necklace per box. How many boxes did the owner use?