# School of Mathematics and Statistics MT5824 Topics in Groups Problem Sheet VII: Nilpotent groups (Solutions)

1. Show that $\gamma _ { 2 } ( G ) = G ^ { \prime }$ . Deduce that abelian groups are nilpotent.

Solution: By definition $\gamma _ { 2 } ( G ) = [ G , G ]$ . Thus $\gamma _ { 2 } ( G ) = \langle [ x , y ] \mid x , y \in G \rangle = G ^ { \prime }$ . If G is abelian, then $[ x , y ] = 1$ for all $x , y \in G$ , so $\gamma _ { 2 } ( G ) = G ^ { \prime } = { \bf 1 }$ . Hence G is nilpotent $( \mathrm { o f ~ c l a s s \leqslant 1 } )$

2. Show that $\mathbf { Z } ( S _ { 3 } ) = \mathbf { 1 }$ . Hence calculate the upper central series of $S _ { 3 }$ and deduce that $S _ { 3 }$ is not nilpotent.

Show that $\gamma _ { i } ( S _ { 3 } ) = A _ { 3 }$ for all ${ \textbf { \em i } } \geqslant { \bf 2 } .$ . [Hint: We have calculated ${ S _ { 3 } ^ { \prime } }$ previously and now know that $S _ { 3 }$ is not nilpotent.]

Find a normal subgroup N of $\mathbf { { S 3 } }$ such that $S _ { 3 } / N$ and N are both nilpotent.

Solution: Recall that all permutations with the same cycle structure are conjugate in $S _ { n }$ . Therefore a permutation lies in the centre of $S _ { 3 }$ if and only if it is the only permutation of its cycle structure. Hence $\mathbf { Z } ( S _ { 3 } ) = \mathbf { 1 }$ (there are three permutations of cycle structure $( \alpha \beta )$ and two of cycle structure $\left( \alpha \beta \gamma \right) )$

This shows that $\mathrm { Z } _ { 1 } ( S _ { 3 } ) = { \bf 1 }$ . Suppose that $\mathrm { Z } _ { i } ( S _ { 3 } ) = { \bf 1 }$ . Then $\mathrm { Z } _ { i + 1 } ( S _ { 3 } ) = \mathrm { Z } _ { i + 1 } ( S _ { 3 } ) / \mathrm { Z } _ { i } ( S _ { 3 } ) =$ $\mathrm { Z } ( S _ { 3 } / \mathrm { Z } _ { i } ( S _ { 3 } ) ) ~ = ~ \mathrm { Z } ( S _ { 3 } ) ~ = ~ { \bf 1 }$ Hence, by induction, $\mathrm { Z } _ { i } ( S _ { 3 } ) \ = \ { \bf 1 }$ for all i. Since $\mathrm { Z } _ { i } ( S _ { 3 } ) < S _ { 3 }$ for all i, we deduce that $S _ { 3 }$ is not nilpotent.

Now $S _ { 3 } ^ { \prime } \ = \ A _ { 3 }$ , by Question $2 ( \mathrm { i } )$ on Problem Sheet VI. Hence $\gamma _ { 2 } ( S _ { 3 } ) = S _ { 3 } ^ { \prime } = A _ { 3 }$ Now $A _ { 3 }$ is of order 3, so has no proper non-trivial subgroups. Hence for $i > 2$ , either $\gamma _ { i } ( S _ { 3 } ) = A _ { 3 } ~ \mathrm { o r } ~ \gamma _ { i } ( S _ { 3 } ) = { \bf 1 }$ . But $S _ { 3 }$ is not nilpotent, so $\gamma _ { i } ( S _ { 3 } ) \neq \mathbf { 1 }$ for all i. Hence $\gamma _ { i } ( S _ { 3 } ) = A _ { 3 }$ for all $i \geqslant 2 .$

Let $N = A _ { 3 } \triangleleft S _ { 3 }$ Then $S _ { 3 } / N \cong C _ { 2 }$ and $N \cong C _ { 3 }$ , so these are both abelian and hence nilpotent. (Thus we have an example of a non-nilpotent group G with normal subgroup N such that $G / N$ and N are nilpotent.)

## 3. Show that $\mathbf { Z } ( G \times H ) = \mathbf { Z } ( G ) \times \mathbf { Z } ( H )$

Show, by induction on i, that ${ \bf Z } _ { i } ( G \times H ) = { \bf Z } _ { i } ( G ) \times { \bf Z } _ { i } ( H )$ for all i.

Deduce that a direct product of a finite number of nilpotent groups is nilpotent.

Solution: Let $( x , y ) \in \mathrm { Z } ( G \times H )$ Then for $g \in G$ and $h \in H$ , it follows that $( x , y ) ( g , h ) = ( g , h ) ( x , y )$ . That is, $( x g , y h ) = ( g x , h y )$ . Hence $x g = g x$ for all $g \in G$ and $y h = h y$ for all $h \in H$ . Therefore $x \in \mathrm { Z } ( G )$ and $y \in \operatorname { Z } ( H )$ , so $\mathrm { Z } ( G \times H ) \leqslant$ $\mathrm { Z } ( G ) \times \mathrm { Z } ( H )$

Conversely, if $( x , y ) \in \mathrm { Z } ( G ) \times \mathrm { Z } ( H )$ ; that is, $x \in \mathrm { Z } ( G )$ and $y \in \mathrm { Z } ( H )$ , then

$$
( x , y ) ( g , h ) = ( x g , y h ) = ( g x , h y ) = ( g , h ) ( x , y )
$$

so $( x , y ) \in \mathrm { Z } ( G \times H )$ . This shows that $\operatorname { Z } ( G ) \times \operatorname { Z } ( H ) \leqslant \operatorname { Z } ( G \times H )$ . The equality now follows.

For the next step, induct on i. $\mathrm { I f } \ i = 0 .$ then ${ \mathrm { Z } } _ { 0 } ( G \times H ) = \{ ( 1 , 1 ) \} = \mathbf { 1 } \times \mathbf { 1 } = { \mathrm { Z } } _ { 0 } ( G ) \times$ $\mathrm { Z } _ { 0 } ( H )$ , so the result holds. Suppose as an inductive hypothesis that $\mathrm { Z } _ { i } ( G \times H ) =$ $\mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H )$ for some i. Then

$$
{ \frac { G \times H } { \mathrm { Z } _ { i } ( G \times H ) } } = { \frac { G \times H } { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } } .
$$

The map $\phi$ that sends $( \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) ) ( x , y )$ to $( \mathrm { Z } _ { i } ( G ) x , \mathrm { Z } _ { i } ( H ) y )$ is an isomorphism:

$$
\phi \colon \frac { G \times H } { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } \to \frac { G } { \mathrm { Z } _ { i } ( G ) } \times \frac { H } { \mathrm { Z } _ { i } ( H ) } .
$$

(This works whenever M  G and $N \leqslant G$ , for then $( G \times H ) / ( M \times N ) \cong G / M \times H / N$ via a similar isomorphism.) This isomorphism φ maps the centre of the group on the left-hand side to the centre of the group on the right-hand side. Hence

$$
\begin{array} { r l r } { \left( \frac { \mathrm { Z } _ { i + 1 } ( G \times H ) } { \mathrm { Z } _ { i } ( G \times H ) } \right) \phi = \left( \mathrm { Z } \left( \frac { G \times H } { \mathrm { Z } _ { i } ( G \times H ) } \right) \right) \phi } & { } & \\ { = \left( \mathrm { Z } \left( \frac { G \times H } { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } \right) \right) \phi } & \\ { = \mathrm { Z } ( G / \mathrm { Z } _ { i } ( G ) \times H / \mathrm { Z } _ { i } ( G ) ) } & \\ { = \mathrm { Z } ( G / \mathrm { Z } _ { i } ( G ) ) \times \mathrm { Z } ( H / \mathrm { Z } _ { i } ( G ) ) } & { } & \\ { = \mathrm { Z } _ { i + 1 } ( G ) / \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i + 1 } ( H ) / \mathrm { Z } _ { i } ( H ) } & { \mathrm { ~ b y ~ d e f i n i t i o n ~ } } \\ { = \left( \frac { \mathrm { Z } _ { i + 1 } ( G ) \times \mathrm { Z } _ { i + 1 } ( H ) } { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } \right) \phi } & { } & \\ { = \left( \frac { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } { \mathrm { Z } _ { i } ( G ) \times \mathrm { Z } _ { i } ( H ) } \right) \phi } & { } & \end{array}
$$

with the last step being the definition of $\phi .$ Since $\phi$ is a bijection,

$$
\frac { \mathrm { Z } _ { i + 1 } ( G \times H ) } { \mathrm { Z } _ { i } ( G \times H ) } = \frac { \mathrm { Z } _ { i + 1 } ( G ) \times \mathrm { Z } _ { i + 1 } ( H ) } { \mathrm { Z } _ { i } ( G \times H ) }
$$

and the Correspondence Theorem yields $\operatorname { Z } _ { i + 1 } ( G \times H ) = \operatorname { Z } _ { i + 1 } ( G ) \times \operatorname { Z } _ { i + 1 } ( H )$ , which completes the induction.

Let $G _ { 1 } , G _ { 2 } , \ldots , G _ { n }$ be nilpotent groups. Then there exist $c _ { i }$ such that $\mathrm { Z } _ { c _ { i } } ( G _ { i } ) = G _ { i }$ Choose c to be the largest of all the $c _ { i }$ . Then $\mathrm { Z } _ { c } ( G _ { i } ) = G _ { i }$ for $i = 1 , 2 , \dots , n$ . By the previous result, we see that

$$
\begin{array} { c } { { \mathrm { Z } _ { c } ( G _ { 1 } \times G _ { 2 } \times \cdot \cdot \cdot \times G _ { n } ) = \mathrm { Z } _ { c } ( G _ { 1 } ) \times \mathrm { Z } _ { c } ( G _ { 2 } ) \times \cdot \cdot \cdot \times \mathrm { Z } _ { c } ( G _ { n } ) } } \\ { { { } } } \\ { { = G _ { 1 } \times G _ { 2 } \times \cdot \cdot \cdot \times G _ { n } , } } \end{array}
$$

and hence $G _ { 1 } \times G _ { 2 } \times \cdots \times G _ { n }$ is nilpotent.

4. Let G be an finite elementary abelian p-group. Show that $\Phi ( G ) = { \bf 1 }$

Solution: Let $G = C _ { p } \times C _ { p } \times \cdot \cdot \cdot \times C _ { p }$ (d times, for some d). Then

$$
M = M _ { i } = C _ { p } \times \cdots \times C _ { p } \times \mathbf { 1 } \times C _ { p } \times \cdots \times C _ { p }
$$

(where the 1 occurs in the ith entry) is a subgroup of G of index p. If H is a subgroup of G such that $M \leqslant H \leqslant G$ , then $| G : H | \cdot | H : M | = | G : M | = p .$ , so as p is prime, either H = G or $H = M$ . Hence M is a maximal subgroup of G. Clearly

$$
\bigcap _ { i = 1 } ^ { d } M _ { i } = { \bf 1 }
$$

and this is the intersection of just some of the maximal subgroups of G. Hence

$$
\Phi ( G ) = \bigcap _ { M \underset { \mathrm { ~ i n ~ } G } { \operatorname* { m a x i m a l } } } M \leqslant \bigcap _ { i = 1 } ^ { d } M _ { i } = \mathbf { 1 } .
$$

5. Let G be a finite p-group.

If M is a maximal subgroup of $_ { G , }$ show that $| G : M | = p { \mathrm { . } }$ . [Hint: G is nilpotent, so $M \leqslant G . ]$ Deduce that GpG! " Φ(G).

Use the previous question to show that $\Phi ( G ) = G ^ { p } G ^ { \prime } ,$

Show that G can be generated by precisely d elements if and only if ${ \bf \ddot { G } } / \Phi ( G )$ is a direct product of d copies of the cyclic group of order p.

Solution: Since G is a finite p-group, it is nilpotent (Example 7.6). Let M be a maximal subgroup of $G .$ Then $M \leqslant G$ (Lemma 7.15), and $G / M$ possesses no nontrivial proper subgroups (by the Correspondence Theorem). Therefore $G / M$ is cyclic of prime order, so $| G : M | = p { \mathrm { . } }$

If $x \in G$ , then $( M x ) ^ { p } = M 1$ 1, so $x ^ { p } \in M$ . Hence

$$
x ^ { p } \in \bigcap _ { M { \mathrm { ~ m a x i m a l } } } M = \Phi ( G ) \qquad { \mathrm { f o r ~ a l l ~ } } x \in G .
$$

We deduce that $G ^ { p } = \langle x ^ { p } \mid x \in G \rangle \leqslant \Phi ( G )$ . We have already observed that $G ^ { \prime } { \triangleleft { \Phi } ( G ) }$ (see Theorem 7.18), so

$$
G ^ { p } G ^ { \prime } \leqslant \Phi ( G ) .
$$

Let $N = G ^ { p } G ^ { \prime }$ . This is a product of two normal subgroups of $G ,$ so $N \leqslant G$ . Now $G / N$ is abelian (since $G ^ { \prime } \leqslant N )$ ) and if $x \in G ,$ , then

$$
( N x ) ^ { p } = N x ^ { p } = N 1
$$

(since $x ^ { p } \in G ^ { p } \leqslant N )$ Hence $G / N$ is an elementary abelian p-group. It is therefore a direct product of a number of copies of $C _ { p } .$ The previous question now gives $\Phi ( G / N ) = { \bf 1 }$ Hence there is a collection $M _ { 1 } , M _ { 2 } , . . . , M _ { k }$ of subgroups of G containing N such that $M _ { i } / N$ is a maximal subgroup of $G / N$ and $\textstyle \bigcap _ { i = 1 } ^ { k } ( M _ { i } / N ) = \mathbf { 1 }$ . By the Correspondence Theorem, $M _ { i }$ is a maximal subgroup of G and

$$
\bigcap _ { i = 1 } ^ { k } M _ { i } = N .
$$

Hence

$$
\Phi ( G ) = \bigcap _ { M \underset { \mathrm { i n } \stackrel { G } { G } } { \mathrm { m a x i m a l } } } M \leqslant \bigcap _ { i = 1 } ^ { k } M _ { i } = N = G ^ { p } G ^ { \prime } .
$$

Taken together with the previous inclusion, $\Phi ( G ) = G ^ { p } G ^ { \prime }$

Now as $G / \Phi ( G )$ is an elementary abelian $p { \mathrm { - g r o u p . } }$ , it is a direct product of d copies of the cyclic group $C _ { p }$ (for some d). Choose $x _ { 1 } , x _ { 2 } , \dots , x _ { d } \in G$ such that

$$
\Phi ( G ) x _ { 1 } , \ \Phi ( G ) x _ { 2 } , . . . , \ \Phi ( G ) x _ { d }
$$

are the generators of these d direct factors. If $g \in G$ , then

$$
\Phi ( G ) g = \Phi ( G ) x _ { 1 } ^ { e _ { 1 } } x _ { 2 } ^ { e _ { 2 } } \ldots x _ { d } ^ { e _ { d } }
$$

for some $e _ { i } \in \{ 0 , 1 , \ldots , p - 1 \}$ , so $g = y x _ { 1 } ^ { e _ { 1 } } x _ { 2 } ^ { e _ { 2 } } \cdot \cdot \cdot x _ { d } ^ { e _ { d } }$ where $y \in \Phi ( G )$ . Hence

$$
G = \langle x _ { 1 } , x _ { 2 } , \ldots , x _ { d } , \Phi ( G ) \rangle .
$$

Suppose that $x _ { 1 } , x _ { 2 } , \ldots , x _ { d }$ do not generate G. Then $\langle x _ { 1 } , x _ { 2 } , \ldots , x _ { d } \rangle$ is a proper subgroup of $G ,$ so there exists a maximal subgroup M such that

$$
\langle x _ { 1 } , x _ { 2 } , \ldots , x _ { d } \rangle \leqslant M < G .
$$

Then $x _ { 1 } , x _ { 2 } , \ldots , x _ { d } \in M$ while, by definition, $\Phi ( G ) \leqslant M$ . Hence

$$
G = \langle x _ { 1 } , x _ { 2 } , \ldots , x _ { d } , \Phi ( G ) \rangle \leqslant M < G ,
$$

a contradiction. So $x _ { 1 } , x _ { 2 } , \ldots , x _ { d }$ generate G. This shows that if $G / \Phi ( G )$ is a direct product of d copies of $C _ { p } ,$ then G can be generated by d elements.

On the other hand, if G can be generated by d elements, then so can every quotient. A direct product of more than $d$ copies of $C _ { p }$ cannot be generated by d elements, so the number of copies of $C _ { p }$ appearing in the direct product for $G / \Phi ( G )$ is at most $d .$ Putting the above together we deduce that $G$ can be generated by precisely d elements (and no fewer) if and only if $G / \Phi ( G )$ is a direct product of d copies of the cyclic group $C _ { p }$ of order $p .$

6. Let G be a nilpotent group with lower central series

$$
G = \gamma _ { 1 } ( G ) > \gamma _ { 2 } ( G ) > \cdots > \gamma _ { c } ( G ) > \gamma _ { c + 1 } ( G ) = 1 .
$$

Suppose N is a non-trivial normal subgroup of G. Choose i to be the largest positive integer such that N $\cap \gamma _ { i } ( G ) \neq { \bf 1 }$ . Show that $[ { \breve { N } } \cap { \dot { \gamma } } _ { i } ( G ) , G ] = 1$

Deduce that $N \cap \mathbf { Z } ( G ) \neq \mathbf { 1 }$

Solution: $N \neq { \bf 1 }$ , so $N \cap \gamma _ { 1 } ( G ) = N \cap G = N \neq { \bf 1 }$ . Hence we may choose i to be the largest positive integer such that $N \cap \gamma _ { i } ( G ) \neq { \bf 1 }$ . Then

$$
[ N \cap \gamma _ { i } ( G ) , G ] \leqslant [ \gamma _ { i } ( G ) , G ] = \gamma _ { i + 1 } ( G )
$$

while

$$
[ N \cap \gamma _ { i } ( G ) , G ] \leqslant [ N , G ] \leqslant N
$$

since N  G (for ${ \mathrm { i f ~ } } x \in N$ and $g \in G ,$ then $[ x , g ] = x ^ { - 1 } x ^ { g } \in N )$ . Hence

$$
[ N \cap \gamma _ { i } ( G ) , G ] \leqslant N \cap \gamma _ { i + 1 } ( G ) = { \bf 1 }
$$

by the hypothesis that i is largest with the given property.

Hence $N \cap \gamma _ { i } ( G ) \leqslant \mathrm { Z } ( G )$ since $[ x , g ] = 1$ for all $x \in N \cap \gamma _ { i } ( G )$ and all $g \in G$ . Therefore

$$
{ \bf 1 } \neq N \cap \gamma _ { i } ( G ) \leqslant N \cap \mathrm { Z } ( G )
$$

so $N \cap \mathbf { Z } ( G ) \neq \mathbf { 1 }$