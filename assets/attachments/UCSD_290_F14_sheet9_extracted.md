## 9. Euler characteristic

1. Suppose $C _ { * }$ is a chain complex whose homology groups $H _ { * }$ are non-zero only in a bounded range of dimensions, and which are themselves abelian groups of finite rank. Then we can define the Euler characteristic as the alternating sum

$$
\chi = \sum _ { i } ( - 1 ) ^ { i } \operatorname { r k } H _ { i } .
$$

Suppose $C _ { * }$ itself consists of abelian groups of finite rank, non-zero only in a bounded range; then it also makes sense to compute

$$
\sum _ { i } ( - 1 ) ^ { i } \operatorname { r k } C _ { i } .
$$

Show that this quantity equals the Euler characteristic!

2. Prove that the Euler characteristic (here thought of as defined on the category of finite CWcomplexes) behaves like a “measure” in the following senses:

(a). Let X and Y be finite CW-complexes. Then $\chi ( X \times Y ) = \chi ( X ) . \chi ( Y )$

(b). Let Z be a finite CW-complex expressible as $Z = X \cup Y$ , where $X , Y$ and $X \cap Y$ are all CW-subcomplexes of Z. Then $\chi ( Z ) = \chi ( X ) + \chi ( Y ) - \chi ( X \cap Y )$

(c). Suppose $Y  X$ is a d-sheeted covering of a finite CW -complex X. Then $\chi ( Y ) = d . \chi ( X )$

3. (a). Show that the orientable surface $\Sigma _ { 1 0 }$ of genus 10 cannot be a covering space of $\Sigma _ { 5 }$

(b). Give examples to show that the ranks of individual homology groups do not satisfy a simple law like that of $\mathrm { Q . 2 \ ( c ) }$ , and in fact may decrease as well as increase when we go up from X to Y .

4. Prove that the additivity formula of question 2 (b) holds for any topological space Z expressed as a union of open subsets X, Y , as long as the Euler characteristic makes sense for each space (namely that it has finite-rank homology groups, bounded in degree). Hint: Mayer-Vietoris!

5. The orientable surface $\Sigma _ { g }$ of genus g can be made by attaching a single 2-cell to a bouquet of 2g circles along the loop which corresponds to $a _ { 1 } b _ { 1 } a _ { 1 } ^ { - 1 } \dot { b _ { 1 } ^ { - 1 } } a _ { 2 } b _ { 2 } a _ { 2 } ^ { - 1 } \dot { b _ { 2 } ^ { - 1 } } \cdot \cdot \cdot \bar { a _ { g } } b _ { g } a _ { g } ^ { - 1 } b _ { g } ^ { - 1 }$ (if we identify the fundamental group of the bouquet with the free group on 2g generators $a _ { 1 } , \dotsc , a _ { g } , b _ { 1 } , \dotsc , b _ { g } )$ What are the (integral) homology groups of $\Sigma _ { g } \smash { ? }$ Suppose $\Sigma _ { h }  \Sigma _ { g }$ is a d-sheeted covering, for some positive integer d. Find h in terms of g and d.

6. For any topological space X, whose total homology is a finitely-generated abelian group, let $\chi ( X )$ denote the usual Euler characteristic

$$
\chi ( X ) = \sum ( - 1 ) ^ { i } \dim _ { \mathbb { Q } } H _ { i } ( X ; \mathbb { Q } )
$$

and let $\chi _ { 2 } ( X )$ be the “mod-2 homology Euler characteristic”

$$
\chi _ { 2 } ( X ) = \sum ( - 1 ) ^ { i } \dim _ { \mathbb { Z } _ { 2 } } H _ { i } ( X ; \mathbb { Z } _ { 2 } ) .
$$

Use the universal coefficient theorem to show that $\chi ( X ) = \chi _ { 2 } ( X )$

7. Write down the Euler characteristics of the following spaces.

(a). $\mathbb { R } P ^ { 2 }$

(b). $\mathbb { R } P ^ { 3 } .$

(c). $S ^ { 2 } \vee S ^ { 2 } ,$

(d). $S ^ { 2 } \times S ^ { 2 } .$

(e). $S ^ { 2 } \times S ^ { 3 } .$

(f ). $\mathbb { C } P ^ { 3 } .$

(g). The torus with two discs removed.

(h). The closed orientable surface $\Sigma _ { 4 }$ of genus 4.

(i). $\mathbb { R } ^ { 3 }$ minus the unit circle in the (x, y) plane.

(j). $\mathbb { R } ^ { 2 }$ minus five distinct points.

8. A triangulation of a topological space X is a simplicial complex K together with a homeomorphism $h : X \to | K |$ . Prove that there are no triangulations of the torus with fewer than fourteen 2-simplices, and exhibit one with fourteen. The Euler characteristic of the torus might be helpful!