## 2. The fundamental group and group actions

## The fundamental group of the circle

1. Prove that $S ^ { 2 }$ minus two points is homotopy-equivalent to $S ^ { 1 }$ , and that $S ^ { 3 }$ minus two points is homotopy-equivalent to $S ^ { 2 }$ . Show that $S ^ { 2 }$ and $S ^ { 3 }$ are not homeomorphic.

2. By choosing suitable explicit identifications of the fundamental group of $S ^ { 1 }$ with $\mathbb { Z } ,$ identify the induced maps $f _ { * }$ of the following maps $f : S ^ { 1 } \to S ^ { 1 }$ , as maps $\mathbb { Z } \to \mathbb { Z }$ :

(a). The map $z \mapsto z ^ { n }$

(b). The antipodal map;

(c). The map $e ^ { i \theta } \mapsto e ^ { 2 \pi i \sin \theta }$

3. A map $f : S ^ { 1 } \to \mathbb { C } - \{ 0 \}$ is given by the formula $z \mapsto 8 z ^ { 4 } + 4 z ^ { 3 } + 2 z ^ { 2 } + z ^ { - 1 }$ . What is the winding number of this map about the origin, and why?

4. Identify the fundamental group of the M¨obius strip M, based at the point $\big [ \big ( 1 , \frac { 1 } { 2 } \big ) \big ]$ . What class does the boundary curve of M represent in this group?

5. Recall that any path $\gamma : x  y$ in a space X induces an isomorphism $\gamma _ { \# } : \pi _ { 1 } ( X , x ) \to \pi _ { 1 } ( X , y )$ If X is the torus $S ^ { 1 } \times S ^ { 1 }$ and $\gamma$ is a loop based at some point $x _ { 0 }$ , identify the induced map $\gamma _ { \# }$

## Group actions

6. Define the torus $T$ as the quotient of $\mathbb { R } ^ { 2 }$ by the action of the integral translation group $\mathbb { Z } ^ { 2 }$

(a) Show that the space $X - \mathrm { a }$ solid hexagon with sides glued in pairs according to the labelled arrows shown below – is homeomorphic to $T .$ . (You don’t have to write down explicit formulae; a clear description of the homeomorphism is enough.)

<!-- image-->

(b) Let $x _ { 0 } \in T$ be the image of $0 \in \mathbb { R } ^ { 2 }$ . Show that there is an order 6 homeomorphism $f : T  T$ which fixes $x _ { 0 }$ . With respect to the standard identification $\pi _ { 1 } ( T , x _ { 0 } ) \cong \mathbb { Z } ^ { 2 }$ , describe the induced map $f _ { * } : \pi _ { 1 } ( T , x _ { 0 } )  \pi _ { 1 } ( T , x _ { 0 } )$ as a $2 \times 2$ integer matrix, and comment on its determinant.

7. The Klein bottle K is formed from a square by the following identifications.

<!-- image-->

(a). Construct a covering map from $\mathbb { R } ^ { 2 }$ to $K .$ , and use it to show that $\pi _ { 1 } ( K )$ is isomorphic to a group whose elements are pairs $( m , n )$ of integers, with group operation given by $( m , n ) * ( p , q ) =$ $( m + ( - 1 ) ^ { n } p , n + q )$

(b) Show that this group is torsion-free (contains no elements of finite order).

(c). Show that the torus is a double (2-sheeted) cover of the Klein bottle.

8. For each of the following three actions of the group $\mathbb { Z } _ { 2 }$ on a sphere, compute the fundamental group of the quotient:

(a) on $S ^ { 1 } , z \mapsto - z$

(b) on $S ^ { 2 } , ( x , y , z ) \mapsto ( - x , - y , z )$

(c) on $S ^ { 3 } , ( z , w ) \mapsto ( - z , - w )$

## Applications

9. Consider the inclusion map $i : \mathbb { R } P ^ { 2 }  \mathbb { R } P ^ { 3 }$ induced by including $S ^ { 2 }$ as the equator in $S ^ { 3 }$ and taking the quotients by the antipodal maps. Show that i is not homotopic to a constant map.

10. (a). Suppose there is a map $f : S ^ { 2 } \to S ^ { 1 }$ which commutes with the antipodal maps, that is satisfies $f ( - x ) = - x$ . Show that f induces a map $g : \mathbb { R } P ^ { 2 }  \mathbb { R } P ^ { 1 }$ between the quotients by the respective antipodal maps. Now, by considering a great circle path in $S ^ { 2 }$ running between the poles, derive a contradiction, showing that no such f may exist.

(b). Use this result to prove Borsuk’s theorem, that for any (continuous) $f : S ^ { 2 } \to \mathbb { R } ^ { 2 }$ , there is a point $x \in S ^ { 2 }$ such that $f ( x ) = f ( - x )$

(c). Using Borsuk’s theorem, prove the Ham Sandwich theorem: that there exists a plane simultaneously bisecting any three bounded measurable sets in $\mathbb { R } ^ { 3 }$ , such as two pieces of bread and a piece of ham! (Hint: given any point on the sphere (i.e. a unit vector), consider a plane perpendicular to the vector, bisecting the ham. Take the measure theory for granted!)

11. A topological group is a group G whose underlying set has a topology with respect to which multiplication map m $\colon G \times G \to G$ and inversion $i : G \to G$ are continuous. (Remark: if the underlying topological space is actually a smooth manifold and the maps m and i are smooth, G is called a Lie group.) Let 1 be the identity element in the group. Prove that the fundamental group $\pi _ { 1 } ( G , 1 )$ of a topological group is abelian. Deduce that the Klein bottle K cannot be a topological group.