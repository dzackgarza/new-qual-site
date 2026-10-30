1. Let X be a compact 7-dimensional manifold with

$$
H _ { 7 } ( X , \mathbb { Z } ) \cong \mathbb { Z } , \quad H _ { 6 } ( X , \mathbb { Z } ) \cong \mathbb { Z } , \quad H _ { 5 } ( X , \mathbb { Z } ) \cong \mathbb { Z } / 2 \mathbb { Z } , \quad H _ { 4 } ( X , \mathbb { Z } ) \cong \mathbb { Z } \oplus \mathbb { Z } / 3 \mathbb { Z } .
$$

Give all the information you can about the cohomology groups $H ^ { * } ( X , \mathbb { Z } )$

2. What is $\pi _ { n } ( S ^ { 3 } \times S ^ { 4 } \times S ^ { 5 } )$ for $n \leq 3 ?$

3. (a) Let $X \subset \mathbb { R } ^ { 3 }$ be the union of a 2-dimensional sphere and two disjoint chords intersecting the sphere only at their endpoints. Compute the fundamental group of X by finding a more standard space Y which is homotopy equivalent to X. Give a short explanation for why X and Y are homotopy equivalent.

(b) Now let X be obtained similarly as the union of a 2-dimensional sphere and two chords intersecting the sphere only at their endpoints, but such that the chords intersect at precisely one point lying in the interior of each chord. What is the fundamental group X?

<!-- image-->  
Figure for (a).

<!-- image-->  
Figure for (b).

4. The Klein bottle sandwich.

(a) Consider the CW complex constructed as follows. First construct a Klein bottle K out of two two-cells as indicated in this picture:

<!-- image-->

Attach to K two additional two-cells. The two attaching maps $\partial D ^ { 2 } \to K$ are taken to be homeomorphisms between $\partial D ^ { 2 }$ and the circles a and b respectively. Call the resulting CW complex S. Calculate $H _ { * } ( S , \mathbb { Z } )$ using cellular homology. (Don’t just appeal to part (b)!)

(b) Show S is homotopy equivalent to $S ^ { 2 }$

5. Prove by contradiction that there does not exist a continuous map $f : \mathbb { R } ^ { 3 } - \{ 0 \} \to \mathbb { R } ^ { 2 }$ with the property that $f \left( x \right) \neq f \left( - x \right)$ for all $x \in \mathbb { R } ^ { 3 } - \{ 0 \}$ .

Hints: (a) Define $g : \mathbb { R } ^ { 3 } - \{ 0 \}  S ^ { 1 }$ by

$$
g \left( x \right) = \frac { f \left( x \right) - f \left( - x \right) } { \left| f \left( x \right) - f \left( - x \right) \right| } ,
$$

which satisfies $g \left( - x \right) = - g \left( x \right)$

(b) Define the loop $\eta : I \to \mathbb { R } ^ { 3 } - \{ 0 \}$ by $\eta _ { \mathbf { \lambda } } ( s ) = ( \cos ( 2 \pi s ) , \sin ( 2 \pi s ) , 0 )$ and consider the loop $h = g \circ \eta$ in $S ^ { 1 }$

6. Let M be a Z5-orientable manifold. Show that M is orientable.

7. (a) Let k be a positive integer. Compute the fundamental group of the space $X _ { k }$ resulting from attaching a 2-cell $e ^ { 2 }$ to a circle $S ^ { 1 }$ (identified with the unit circle in C) by the map $\varphi : \partial e ^ { 2 } = S ^ { 1 }  S ^ { 1 }$ defined by $\varphi \left( z \right) = z ^ { k }$

(b) How many path-connected covering spaces of $X _ { 3 0 }$ are there, up to equivalence (isomorphism)?

8. Let X, Y and Z be spaces, and let $f : X \to Y , g : X \to Z$ be continuous maps. Define the double mapping cylinder D to be the quotient of the disjoint union of $X \times [ 0 , 1 ]$ , Y and $Z$ via the equivalence relation $( x , 0 ) \sim f ( x ) , ( x , 1 ) \sim g ( x )$ . Show there is an exact sequence

$$
\cdots \to H _ { q } ( X ) \to H _ { q } ( Y ) \oplus H _ { q } ( Z ) \to H _ { q } ( D ) \to H _ { q - 1 } ( X ) \to \cdots .
$$