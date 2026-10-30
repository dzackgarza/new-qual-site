# Math 200a (Fall 2016) - Homework 5

Professor D. Rogalski

Posted October 22–Due Wed. November 2 at 3pm

## 1 Reading

Finish reading chapter 5, and then read Chapter 6.

## 2 Exercises to submit on Wed. November 2

Exercise 1. While a semidirect product $G = H \rtimes _ { \psi } K$ depends in general on the choice of homomorphism $\psi : K \to \operatorname { A u t } ( H )$ , sometimes different choices of ψ lead to isomorphic semidirect products. This problem explores some cases where this happens.

(a). Suppose that $\theta \in \operatorname { A u t } ( H )$ and let $\phi _ { \theta } : \operatorname { A u t } ( H ) \to \operatorname { A u t } ( H )$ be the inner automorphism of $\operatorname { A u t } ( H )$ given by $\rho \mapsto \theta \rho \theta ^ { - 1 }$ . Let $\psi _ { 2 } = \phi _ { \theta } \circ \psi : K \to \operatorname { A u t } ( H )$ . Prove that $H \rtimes _ { \psi } K$ and $H \rtimes _ { \psi _ { 2 } } K$ are isomorphic groups. (Hint: Try the map $H \rtimes _ { \psi } K \to H \rtimes _ { \psi _ { 2 } } K$ given by $( h , k ) \mapsto ( \theta ( h ) , k ) . )$

(b) Suppose that $\rho : K \to K$ is an automorphism of K and define $\psi _ { 2 } = \psi \circ \rho : K \to \operatorname { A u t } ( H )$ Prove that $H \rtimes _ { \psi } K$ and $H \rtimes _ { \psi _ { 2 } } K$ are isomorphic groups.

Exercise 2. Suppose that p and q are primes with $p < q$ where p divides $q - 1$ . Show that there are precisely two groups of order pq up to isomorphism. Find a presentation for the non-Abelian group you find, and justify that your presentation is correct.

Exercise 3. Classify groups G of order 20 up to isomorphism (there are 5 such groups). Make sure you justify why the 5 different groups you find really are non-isomorphic.

Exercise 4. Classify groups of order 75 up to isomorphism. (Hint: Find the order of the automorphism group $\mathrm { A u t } ( \mathbb { Z } _ { 5 } \times \mathbb { Z } _ { 5 } )$ and show that all subgroups of order 3 in this group are conjugate. You don’t need to find any of the elements of order 3 explicitly to do this.)

Exercise 5. (a). Suppose that you can show that all groups G with $\left| G \right| < 6 0$ are not simple.   
Prove that this implies that all groups G with $\left| G \right| < 6 0$ are solvable.

(b). It is actually true that all groups G with $\left| G \right| < 6 0$ are not simple, and thus all groups of order less than 60 are solvable. I encourage you to work out a full proof of this, as it is a good review of the techniques we have developed. However, just write out a proof that groups of order 24, 36, and 48 are not simple. (Consider the kernel of a conjugation action on Sylow p-subgroups.)

Exercise 6. A subgroup K of G is maximal if there does not exist a subgroup H of G with $K \subsetneq H \subsetneq G$ . Suppose that G is finite and has the property that every maximal subgroup of G has prime index. Prove that G is solvable, in the following steps.

(a). Prove that if P is a Sylow p-subgroup of G and $N _ { G } ( P ) \leq H \leq G$ for some subgroup H, then $| G : H | \equiv 1 ( { \bmod { p } } )$ . (This part is true in any finite group.) (Hint: P is a Sylow p-subgroup of H and $N _ { G } ( P ) = N _ { H } ( P ) . )$

(b). Taking p to be the largest prime dividing the order of the group G, show that G has a normal Sylow p-subgroup.

(c). Conclude the proof by induction on the order.

Exercise 7. Let G be a finite group. A group G is called characteristically simple if it has no characteristic subgroups other than $\{ e \}$ and G. A normal subgroup $H \leq G$ is minimal normal if there is no normal subgroup $K \triangleleft G$ with $\{ e \} \subsetneq K \subsetneq H$

(a). Prove that if G is characteristically simple, then G is isomorphic to $H \times H \times \cdots \times H$ for some simple group H.

(Hint: Let N be a minimal normal subgroup of G. Consider the collection of subgroups of G which are internal direct products of the form $N _ { 1 } \times N _ { 2 } \dots \times N _ { k }$ where each $N _ { i }$ is minimal normal in G and each $N _ { i }$ is isomorphic to N . Let M be a maximal element of this collection. Show that M is characteristic in $G ,$ , so $M = G$ . Then show that N is simple.)

(b). Does the converse to part (a) hold?

(c). Show that if N is any minimal normal subgroup of any finite group G, then N is characteristically simple, so N is a direct product of isomorphic simple groups by part (a).