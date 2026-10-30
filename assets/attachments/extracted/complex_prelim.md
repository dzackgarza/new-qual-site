# SOLUTIONS TO COMPLEX PRELIM PROBLEMS

## C˙IHAN BAHRAN

In this document, I will collect my solutions to some (not all, probably not even half) of the Complex Prelim problems that were asked in the past in UMN.

Some theorems get used a lot. I will copy some of them from David C. Ullrich’s wonderful book Complex Made Simple.

## 1. Open mapping theorem

This is very useful in general. It’s easy to forget the connectedness assumption, so I will state it precisely. H(V ) denotes the set of analytic maps from an open set V to C.

Open Mapping Theorem. Let V be open and $f \in \mathbf { H } ( V )$ . Also let W be an open and connected set contained in V . Then $f ( W )$ is either a singleton (that is, f is constant on W ) or open in C.

Fall 2011, 7 and Fall 2010, 3. Prove that there is no one-to-one conformal map of the punctured disk $\{ z \in \mathbb { C } : 0 < | z | < 1 \}$ onto the annulus $\{ z \in \mathbb { C } : 1 < | z | < 2 \}$

Let D denote the unit open disk and A the described annulus. Suppose, to the contrary, that there exists $f \in { \bf H } ( \mathbb { D } - \{ 0 \} )$ which is injective and $f ( \mathbb { D } - \{ 0 \} ) = A$ . Firstly, since $| f ( z ) | < 2$ for all $z \in \mathbb { D } - \{ 0 \}$ , we have

$$
\operatorname* { l i m } _ { z \to 0 } z f ( z ) = 0 .
$$

So 0 is a removable singularity of $f .$ Thus $\exists g \in \mathbf { H } ( \mathbb { D } )$ such that $g | _ { \mathbb { D } - \{ 0 \} } = f$ . As 0 is a limit point of $\mathbb { D } - \{ 0 \} , g ( 0 )$ is a limit point of $g ( \mathbb { D } - \left\{ 0 \right\} ) = A$ . Thus

$$
g ( \mathbb { D } ) \subseteq { \overline { { A } } } = \left\{ z \in \mathbb { C } : 1 \leq | z | \leq 2 \right\} .
$$

Moreover, since $f$ is injective, g is not constant. Thus by the open mapping theorem, we get

$$
g ( \mathbb { D } ) \subseteq \operatorname { I n t } ( { \overline { { A } } } ) = A .
$$

Let $\omega = g ( 0 ) \in A$ Since $f ( { \mathbb { D } } - \{ 0 \} ) = A$ , there exists $z \in \mathbb { D } - \{ 0 \}$ such that $g ( z ) = f ( z ) = \omega$ . Since $z \neq 0$ , there exist disjoint open disks $V , W \subseteq { \mathbb { D } }$ such that $z \in V$ and $0 \in W$ Again by the open mapping theorem, $g ( V )$ and $g ( W )$ are open subsets of A. Thus $g ( V ) \cap g ( W )$ is open. However, since f is a bijection and $V , W - \{ 0 \}$ are

contained in $\mathbb { D } - \{ 0 \}$ , we have

$$
\begin{array} { r l } & { g ( V ) \cap g ( W ) = g ( V ) \cap \Big ( g ( \{ 0 \} ) \cup g \big ( W - \{ 0 \} \big ) \Big ) } \\ & { \qquad = f ( V ) \cap \Big ( \{ \omega \} \cup f \big ( W - \{ 0 \} \big ) \Big ) } \\ & { \qquad = \Big ( f ( V ) \cap \{ \omega \} \Big ) \cup \Big ( f ( V ) \cap f \big ( W - \{ 0 \} \big ) \Big ) } \\ & { \qquad = f ( V ) \cap \{ \omega \} } \\ & { \qquad = \{ \omega \} . } \end{array}
$$

This is a contradiction.

Spring 2011, 2. Let h be a holomorphic function on a connected open set V . Prove that if $h ( z ) ^ { 2 } = { \overline { { h ( z ) } } }$ for all $z \in V$ then h is constant on V . Find all possible values for such h.

First of all, V is nonempty1. Let $f = h ^ { 3 } \in \mathbf { H } ( V )$ . So for all $z \in V , f ( z ) = h ( z ) ^ { 2 } h ( z ) =$ $h ( z ) \overline { { h ( z ) } } = | h ( z ) | ^ { 2 } \in \mathbb { R }$ . That is, $f ( V ) \subseteq \mathbb { R }$ . Suppose f is not constant. Then the open mapping theorem yields $f ( V ) \subseteq \operatorname { I n t } ( \mathbb { R } ) = \varnothing$ (we are considering R as a subspace of C here), a contradiction. Thus for all $z \in V , h ( z ) ^ { 3 } = f ( z ) = a$ for some $a \in \mathbb { C }$ . Therefore if we let $\zeta = e ^ { \frac { 2 \pi i } { 3 } }$ , we have

$$
h ( V ) \subseteq \left\{ | a | ^ { \frac { 1 } { 3 } } , \zeta | a | ^ { \frac { 1 } { 3 } } , \zeta ^ { 2 } | a | ^ { \frac { 1 } { 3 } } \right\} ,
$$

so $h ( V )$ is finite. Nonempty open sets in C are infinite, thus $h ( V )$ is not open. Again by the open mapping theorem we deduce that h is constant. The rest is the kind of stuff Calc 1 students fail to do correctly quite often: basic algebra. For some $x , y \in \mathbb { R }$ $h ( z ) = x + i y$ for all $z \in V$ . So

$$
\begin{array} { r } { ( x + i y ) ^ { 2 } = \overline { { x + i y } } } \\ { x ^ { 2 } - y ^ { 2 } + i ( 2 x y ) = x - i y . } \end{array}
$$

Thus $x ^ { 2 } - y ^ { 2 } = x$ and $2 x y = - y .$ . The second equation gives $y = 0$ or $\textstyle x = - { \frac { 1 } { 2 } }$ . Going to the first equation, the first case yields $x ^ { 2 } = x $ and the second case yields $\begin{array} { r } { \frac { 1 } { 4 } - y ^ { 2 } = - \frac { 1 } { 2 } } \end{array}$ So the solutions are $\begin{array} { r } { 0 , 1 , - \frac { 1 } { 2 } + i \frac { \sqrt { 3 } } { 2 } , - \frac { 1 } { 2 } - i \frac { \sqrt { 3 } } { 2 } } \end{array}$

## 2. Linear fractional transformations

I think the most useful linear fractional transformations for the prelims are the ones that map a half plane to the unit disk. And, thanks to Ullrich’s book, I know that there is a way to do this which is really cool and impossible to forget. Let U be the upper half plane and D be the open unit disk. The neat geometric observation is that $z \in \mathbb { U }$ if and only if z is closer to i than it is to −i. This yields

$$
z \in \mathbb { U } \Leftrightarrow | z - i | < | z + i |
$$

$$
\Leftrightarrow \left| { \frac { z - i } { z + i } } \right| < 1
$$

$$
\Leftrightarrow \frac { z - i } { z + i } \in \mathbb { D } .
$$

Thus the $\operatorname { L F T } { \frac { z - i } { z + i } }$ maps U onto D. In exactly the same way, $\frac { z - 1 } { z + 1 }$ maps the right half plane onto D. Let’s roll:

Fall 2012, 1. Show that a M¨obius transformation maps a straight line or circle onto a straight line or circle.

This takes work! I’d like to know if there is a shorter argument. We start with a lemma: Lemma 1. Let T be an LFT. Then $T ^ { - 1 } ( \mathbb R )$ is a circle in $\mathbb { C } ^ { \infty }$ (that is, a line $o r \ a$ circle in C).

Proof. Say

$$
T ( z ) = { \frac { a z + b } { c z + d } }
$$

where $a , b , c , d \in \mathbb { C }$ such that $a d - b c \neq 0$ . Note that

$$
\begin{array} { r l } & { \omega \in T ^ { - 1 } ( \mathbb { R } ) \Leftrightarrow T ( w ) \in \mathbb { R } } \\ & { \qquad \Leftrightarrow \frac { a \omega + b } { c \omega + d } = T ( \omega ) = \overline { { T ( \omega ) } } = \frac { \overline { { a \omega } } + \bar { b } } { \overline { { c \displaystyle { w } } } + \overline { { d } } } } \\ & { \qquad \Leftrightarrow a \overline { { c } } | \omega | ^ { 2 } + a \overline { { d } } \omega + b \overline { { c \omega } } + b \overline { { d } } = \overline { { a } } c | \omega | ^ { 2 } + \overline { { a } } d \overline { { \omega } } + \overline { { b } } c \omega + \overline { { b } } d } \\ & { \qquad \Leftrightarrow ( a \overline { { c } } - \overline { { a } } c ) | \omega | ^ { 2 } + ( a \overline { { d } } - \overline { { b } } c ) \omega + ( b \overline { { c } } - \overline { { a } } d ) \overline { { \omega } } + b \overline { { d } } - \overline { { b } } d = 0 } \end{array}\tag{?}
$$

We have two cases:

$a { \overline { { c } } } - { \overline { { a } } } c = 0$ . Then (?) becomes

$$
\begin{array} { c c } { { ( a \overline { { { d } } } - \overline { { { b } } } c ) \omega + ( b \overline { { { c } } } - \overline { { { a } } } d ) \overline { { { \omega } } } + b \overline { { { d } } } - \overline { { { b } } } d = 0 } } & { { } } \\ { { ( a \overline { { { d } } } - \overline { { { b } } } c ) \omega + \overline { { { ( \overline { { { b } } } c - a \overline { { { d } } } ) \omega } } } + \overline { { { \overline { { { b } } } } d } } - \overline { { { b } } } d = 0 . } } & { { } } \end{array}
$$

So if we write $A = a { \overline { { d } } } - { \bar { b } } c .$ and $B = { \bar { b } } d ,$ , we get

$$
\begin{array} { r l } & { A \omega - \overline { { A \omega } } = B - \overline { { B } } } \\ & { 2 i \operatorname { I m } ( A \omega ) = 2 i \operatorname { I m } ( B ) } \\ & { \qquad \operatorname { I m } ( A \omega ) = \operatorname { I m } ( B ) . } \end{array}\tag{†}
$$

We observe that $A \neq 0$ . Suppose not. Then we have $a { \overline { { d } } } = { \overline { { b } } } c$ and so

$$
\begin{array} { l } { { \overline { { { a } } } c \overline { { { d } } } = a \overline { { { c } } } \overline { { { d } } } = \overline { { { b } } } c \overline { { { c } } } } } \\ { { c \overline { { { ( a d - b c ) } } } = 0 . } } \end{array}
$$

Since ad $- \ b c \ \neq \ 0$ , we get $c = 0$ . But then $a \bar { d } = 0$ so $a d = 0$ and hence ad $- b c = 0$ , a contradiction. Since $A \neq 0 , ( \dag )$ describes a line.

$a \overline { { c } } - \overline { { a } } c \neq 0$ . Then we can write (?) as

$$
| \omega | ^ { 2 } + { \frac { a { \overline { { d } } } - { \overline { { b } } } c } { a { \overline { { c } } } - { \overline { { a } } } c } } \omega + { \frac { b { \overline { { c } } } - { \overline { { a } } } d } { a { \overline { { c } } } - { \overline { { a } } } c } } { \overline { { \omega } } } + { \frac { b { \overline { { d } } } - { \overline { { b } } } d } { a { \overline { { c } } } - { \overline { { a } } } c } } = 0 .
$$

Write $A = { \frac { a { \overline { { d } } } - { \bar { b } } c } { a { \overline { { c } } } - { \overline { { a } } } c } } , \operatorname { s o } { \overline { { A } } } = { \frac { { \overline { { a } } } d - b { \overline { { c } } } } { { \overline { { a } } } c - a { \overline { { c } } } } } = { \frac { b { \overline { { c } } } - { \overline { { a } } } d } { a { \overline { { c } } } - { \overline { { a } } } c } }$ and write $B = \frac { b \overline { { d } } - \bar { b } d } { a \overline { { c } } - \overline { { a } } c }$ . Thus we get

$$
\begin{array} { c } { { | \omega | ^ { 2 } + A \omega + \overline { { { A } } } \omega + B = 0 } } \\ { { | \omega | ^ { 2 } + A \omega + \overline { { { A } } } \overline { { { \omega } } } + A \overline { { { A } } } = A \overline { { { A } } } - B } } \\ { { | \omega + A | ^ { 2 } = A \overline { { { A } } } - B } } \end{array}\tag{‡}
$$

Note that

$$
\begin{array} { r l } { A \overline { { A } } - B = \frac { \sin \overline { { d } } - \overline { { B } } c } { a \mathrm { C - } \mathrm { ~ } \overline { { a } } c } \cdot \frac { \mathrm { ~ B \overline { { c } } } - \overline { { a } } d } { a c - \mathrm { ~ } \overline { { a c } } } - \frac { \mathrm { ~ } \sqrt { \delta } d } { a c - \mathrm { ~ } \overline { { \delta a } } c } } \\ & { = \frac { ( \overline { { a } } \overline { { d } } - \overline { { b } } c ) ( | \overline { { \theta } } - \overline { { a } } \overline { { d } } ) } { \left( \Delta c - \mathrm { ~ } \overline { { a c } } \right) ^ { 2 } } - \frac { \left( \overline { { a } } \overline { { c } } - \overline { { a } } \overline { { c } } \right) ( | \overline { { \theta } } \overline { { d } } - \overline { { b } } d ) } { \left( \Delta c - \mathrm { ~ } \overline { { \delta a } } c \right) ^ { 2 } } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  = \frac { \overline { { \delta } } \widetilde { { \delta a } } \overline { { d } } + \overline { { \delta a } } \overline { { d } } - \overline { { a } } \overline { { \delta a } } \overline { { d } } \overline { { \theta } } \overline { { d } } \cdot \overline { { \delta a } } \overline { { c } } } \\ &  = \frac { a d ( | \overline { { \theta } } - \overline { { a } } \overline { { d } } ) - \overline { { b } } ( | \overline { { \theta } } \overline { { d } } ) ^ { 2 } - \overline { { b } } \overline { { c } } \overline { { \delta a } } \overline { { \delta a } } } { - 4 \left[ \operatorname* { m a x } \mathord { \left( \overline { { \delta a } } \right) } ^ { 2 } \right] } \\ &  \quad \quad \quad \quad \quad \ \end{array}
$$

So if we let $r = { \frac { \left| a d - b c \right| } { 2 \operatorname { I m } ( a { \overline { { c } } } ) } } > 0 \ ( a d - b c \neq 0 )$ , (‡) becomes

$$
| \omega + A | ^ { 2 } = r ^ { 2 } ,
$$

which describes a circle.

Definition 2. Let $z _ { 1 } , z _ { 2 } , z _ { 3 }$ be three distinct points in $\mathbb { C } ^ { \infty }$ . We define an $\mathrm { L F T } \left( _ { - } , z _ { 1 } , z _ { 2 } , z _ { 3 } \right)$ by

$$
( \ l _ { - } , z _ { 1 } , z _ { 2 } , z _ { 3 } ) ( z ) = ( z , z _ { 1 } , z _ { 2 } , z _ { 3 } ) = \left\{ \begin{array} { l l } { \frac { ( z - z _ { 1 } ) ( z _ { 2 } - z _ { 3 } ) } { ( z - z _ { 3 } ) ( z _ { 2 } - z _ { 1 } ) } } & { \mathrm { i f ~ n o n e ~ o f ~ } z _ { 1 } , \ z _ { 2 } , \ z _ { 3 } \mathrm { ~ a r e ~ \infty ~ } } \\ { \frac { z _ { 2 } - z _ { 3 } } { z - z _ { 3 } } } & { \mathrm { i f ~ } \ z _ { 1 } = \infty } \\ { \frac { z - z _ { 1 } } { z - z _ { 3 } } } & { \mathrm { i f ~ } \ z _ { 2 } = \infty } \\ { \frac { z - z _ { 1 } } { z _ { 2 } - z _ { 1 } } } & { \mathrm { i f ~ } \ z _ { 3 } = \infty } \end{array} \right.
$$

Note that $\left( \_ , z _ { 1 } , z _ { 2 } , z _ { 3 } \right)$ sends $z _ { 1 } , z _ { 2 } , z _ { 3 }$ to $0 , 1 , \infty$ , respectively.

Theorem 3. LFT’s sends circles in $\mathbb { C } ^ { \infty }$ to circles in $\mathbb { C } ^ { \infty }$

Proof. Let T be an LFT and C be a circle in $C ^ { \infty }$ . Pick three distinct points $\omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 }$ on C. Let $z _ { i } = T ( \omega _ { i } )$ for $i = { 1 , 2 , 3 }$ and let $\boldsymbol { S } = \left( _ { - } , z _ { 1 } , z _ { 2 } , z _ { 3 } \right)$ . Note that by construction $z _ { 1 } , z _ { 2 } , z _ { 3 } \in S ^ { - 1 } ( \mathbb { R } )$ , which is a circle in $\mathbb { C } ^ { \infty }$ by Lemma 2. But the three distinct points

$z _ { 1 } , z _ { 2 } , z _ { 3 }$ determine a unique circle $C ^ { \prime }$ in $\mathbb { C } ^ { \infty }$ ; thus $S ^ { - 1 } ( \mathbb { R } ) = C ^ { \prime }$ . In a similar fashion, we get $( S \circ T ) ^ { - 1 } ( \mathbb { R } ) = C$ since $\omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 }$ uniquely determine C. Thus we have

$$
T ( C ) = T ( ( S \circ T ^ { - 1 } ) ( \mathbb { R } ) ) = ( T \circ ( S \circ T ) ^ { - 1 } ) ( \mathbb { R } ) = S ^ { - 1 } ( \mathbb { R } ) = C ^ { \prime } .
$$

```latex
Fall 2012, 7. Suppose $f ( z )$ is analytic on the punctured unit disk $\mathbb { D } - \{ 0 \}$ , and
the real part of $f ( z )$ is positive. Prove that $f$ has a removable singularity at 0.
Let $\mathbb { H } = \left\{ z \in \mathbb { C } : \mathrm { R e } ( z ) > 0 \right\}$ We may write $f : \mathbb { D } - \{ 0 \}  \mathbb { H } .$ Also by the above
discussion, we have an invertible analytic map
$\phi : \mathbb { H } \to \mathbb { D }$
$z \mapsto \frac { z - 1 } { z + 1 }$
with the inverse $\phi ^ { - 1 } ( z ) = { \frac { z + 1 } { - z + 1 } } = { \frac { z + 1 } { 1 - z } }$ . Note that $g : = \phi \circ f$ is analytic and maps
$\mathbb { D } - \{ 0 \}$ to D. In particular, $g$ is bounded. Thus
$\operatorname* { l i m } _ { z \to 0 } z g ( z ) = 0$
and hence 0 is a removable singularity of $g .$ So there exists an analytic function
$h : \mathbb { D }  \mathbb { C }$
such that $h | _ { \mathbb { D } - \{ 0 \} } = g .$ Since $h ( \mathbb { D } - \{ 0 \} ) \subseteq \mathbb { D }$ , by continuity we get $h ( \mathbb { D } ) \subseteq \overline { { \mathbb { D } } }$ . There
are two cases by the open mapping theorem:
(1) h is constant. Then pick $a \in \mathbb { D } - \{ 0 \} , \operatorname { s o } h ( 0 ) = h ( a ) = g ( a ) \in \mathbb { D } .$
(2) $h ( \mathbb { D } ) \subseteq \operatorname { I n t } ( \overline { { \mathbb { D } } } ) = \mathbb { D } .$
In any case, we may write $h : \mathbb { D }  \mathbb { D }$ So forming the composition $\phi ^ { - 1 } \circ h$ is legal, and
$( \phi ^ { - 1 } \circ h ) | _ { \mathbb { D } - \{ 0 \} } = \bar { \phi ^ { - 1 } } \circ g = f .$ . We effectively removed the singularity of $f$ at 0.
Fall 2009, 5. Let $f ( z )$ be an analytic function on $\mathbb { C }$ which takes value in the upper
half plane U. Show that $f$ is constant.
Same deal. $\phi ( z ) = { \frac { z - i } { z + i } }$ maps $\mathbb { U }$ conformally to $\mathbb { D } ,$ thus $\phi \circ f$ is an entire function
which takes values in D. Thus by Liouville’s theorem, $\phi \circ f$ is constant. $\phi$ is invertible,
so $f$ is also constant.
Spring 2009, 3. Find an explicit conformal equivalence which maps the open set
bounded by $\begin{array} { r } { \left| z - \frac { 1 } { 2 } i \right| = \frac { 1 } { 2 } } \end{array}$ and $| z - i | = 1$ onto the upper half plane U.
I am too lazy to learn drawing circles in LaTeX now, so the reader should draw them.
Let $D _ { 1 } = \big \{ z \in \mathbb { C } : \big | z - \frac { 1 } { 2 } i \big | < \frac { 1 } { 2 } \big \}$ and $D _ { 2 } = \{ z \in \mathbb { C } : | z - i | < 1 \}$ We want to map
the open set $V : = \dot { D } _ { 2 } - \overrightarrow { D _ { 1 } }$ conformally onto U. Consider the circles $C _ { 1 } = \partial D _ { 1 }$ and
$C _ { 2 } = \partial D _ { 2 }$ . Note that $C _ { 1 } \cap C _ { 2 } = \{ 0 \}$ . Let’s pick two other points on $C _ { 2 } \colon$ 2i and $1 + i$
We can send $C _ { 2 }$ to the real line in various ways, but it’s better to pick an $\mathrm { L F T }$ so that
```

$0 \mapsto \infty$ . This will ensure $C _ { 1 }$ maps to a line as well. The assignments

$$
\begin{array} { c } { { 1 + i \mapsto 0 } } \\ { { 2 i \mapsto 1 } } \\ { { 0 \mapsto \infty } } \end{array}
$$

can be realized by the LFT

$$
\begin{array} { l } { \phi ( z ) = \displaystyle \frac { ( z - ( 1 + i ) ) ( 2 i - 0 ) } { ( 2 i - ( 1 + i ) ) ( z - 0 ) } } \\ { = \displaystyle \frac { ( z - 1 - i ) 2 i } { ( i - 1 ) z } } \\ { = \displaystyle \frac { 2 i z + 2 - 2 i } { ( i - 1 ) z } . } \end{array}
$$

So $\phi$ maps $C _ { 2 }$ to the real line R. And since

$$
\begin{array} { l } { \displaystyle \phi ( \boldsymbol { i } ) = \frac { - 2 + 2 - 2 i } { ( i - 1 ) i } = \frac { - 2 i } { ( i - 1 ) i } } \\ { \displaystyle = \frac { - 2 } { i - 1 } = \frac { 2 } { 1 - i } = \frac { 2 ( 1 + i ) } { 2 } = 1 + i \in \mathbb { U } , } \end{array}
$$

$\phi$ maps $D _ { 2 }$ onto the upper half plane U. Let’s see what $\phi$ does to $C _ { 1 }$ . We already know $\phi ( 0 ) = \infty$ and $\phi ( i ) = 1 + i$ . Let’s choose another point on $C _ { 1 } \colon \frac { i + 1 } { 2 }$ . We have

$$
{ \begin{array} { r l } & { \phi \left( { \frac { 1 + i } { 2 } } \right) = { \frac { 2 i \left( { \frac { 1 + i } { 2 } } \right) + 2 - 2 i } { ( i - 1 ) \left( { \frac { 1 + i } { 2 } } \right) } } } \\ & { \qquad = { \frac { i - 1 + 2 - 2 i } { - 1 } } = - 1 + i } \end{array} }
$$

So we deduce that $\phi ( C _ { 1 } ) = \{ z \in \mathbb { C } : \operatorname { I m } ( z ) = 1 \}$ . And since

$$
\begin{array} { l } { \displaystyle { \phi \left( \frac { i } { 2 } \right) = \frac { 2 i \left( \frac { i } { 2 } \right) + 2 - 2 i } { \left( i - 1 \right) \left( \frac { i } { 2 } \right) } = \frac { 1 - 2 i } { \frac { - 1 - i } { 2 } } } } \\ { \displaystyle { = \frac { 2 - 4 i } { - 1 - i } = \frac { - 2 + 4 i } { 1 + i } = \frac { \left( - 2 + 4 i \right) \left( 1 - i \right) } { 2 } } } \\ { \displaystyle { = \frac { 2 + 6 i } { 2 } = 1 + 3 i , } } \end{array}
$$

we deduce that $\phi ( D _ { 1 } )$ is the half plane $\{ z \in \mathbb { C } : \operatorname { I m } ( z ) > 1 \}$ . Thus

$$
\phi ( V ) = \phi ( D _ { 2 } - \overline { { D _ { 1 } } } ) = \left\{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0 \mathrm { ~ a n d ~ } \operatorname { I m } ( z ) < 1 \right\} .
$$

Consider the translation $\tau ( z ) = z - i$ . We have

$$
\begin{array} { r l } & { ( \tau \circ \phi ) ( V ) = \left\{ z \in \mathbb { C } : \mathrm { R e } ( z ) > 0 \ \mathrm { a n d } \ \mathrm { I m } ( z ) < 0 \right\} } \\ & { \qquad = \left\{ a - i b : a , b > 0 \right\} . } \end{array}
$$

In other words, if we let $\psi = \tau \circ \phi , \psi ( V )$ is the fourth quadrant. Hence $( i \cdot \psi ) ( V )$ is the first quadrant. Since $z \mapsto z ^ { 2 }$ sends the first quadrant onto the upper half plane U, $( i \cdot \psi ) ^ { 2 } ( V ) = - \psi ^ { 2 } ( V ) = \mathbb { U }$ . Being a composition of conformal maps, $- \psi ^ { 2 }$ is conformal.

Spring 2008, 6. Find an explicit conformal equivalence from the region $R _ { 1 }$ to the region $R _ { 2 }$ , where

$$
R _ { 1 } = \left\{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0 , \operatorname { I m } ( z ) > 0 , | z | < 1 \right\}
$$

and

$$
R _ { 2 } = \left\{ z \in \mathbb { C } : \operatorname { R e } ( z ) > 0 , \operatorname { I m } ( z ) > 0 \right\} .
$$

Note that $R _ { 1 }$ is contained in the unit disk D and $R _ { 2 }$ is contained in the upper half plane U. We noted above that

$$
\phi ( z ) = { \frac { z - i } { z + i } }
$$

maps U (conformally) onto D. Note that for any $a \in \mathbb { R }$

$$
\phi ( i a ) = \frac { i a - i } { i a + i } = \frac { a - 1 } { a + 1 }
$$

lies on the real axis R. Thus $\phi$ maps the imaginary axis iR to R. Therefore $\phi ( \mathbb { U } - i \mathbb { R } ) =$ D−R and since $R _ { 2 }$ is a connected component of $\mathbb { U } - i \mathbb { R } , \phi ( R _ { 2 } )$ is a connected component of D − R. Let’s pick a point, say $1 + i \in R _ { 2 }$ , to see which component $\phi ( R _ { 2 } )$ is. We have

$$
\phi ( 1 + i ) = \frac { 1 } { 1 + 2 i } = \frac { 1 - 2 i } { 5 } .
$$

Therefore $\phi ( R _ { 2 } ) = \{ z \in \mathbb { D } : \operatorname { R e } ( z ) > 0 \} = : V$ . So we will be done if we can map $R _ { 1 }$ onto V . And this is easy. Note that applying $\sigma ( z ) = z ^ { 2 }$ yields

$$
\sigma ( R _ { 1 } ) = \left\{ z \in \mathbb { D } : \operatorname { I m } ( z ) > 0 \right\} .
$$

And finally, rotation by $\pi / 4$ (a.k.a multiplying by i) maps this to V . Thus $z \mapsto$ $\phi ^ { - 1 } ( i \sigma ( z ) )$ maps $R _ { 1 }$ to $R _ { 2 }$

## 3. Rouche’s theorem

Rouche’s Theorem. Suppose that γ is a smooth closed curve in the open set V such that Ind $( \gamma , z )$ is either 0 or 1 for $a l l z \in \mathbb { C } - \gamma *$ and equals 0 for all $z \in \mathbb { C } - V$ , and let $\Omega = \{ z \in V : \operatorname { I n d } ( \gamma , z ) = 1 \} . \ I f \ f , g \in \mathbf { H } ( V )$ and

$$
| f ( z ) - g ( z ) | < | f ( z ) | + | g ( z ) |
$$

for all $z \in \gamma *$ then f and g have the same number of zeroes in Ω.

Note that the number of zeros is counted with multiplicity. There are a lot of notations in the statement above. We don’t need to know what most are for the usual applications of Rouche’s theorem, though the reader might figure them out. I’ll just note (again) that H(V ) denotes the set of (complex valued) holomorphic functions defined on the open set V . The following version is a corollary of the general theorem above and we will only use this one:

Rouche’s Theorem. Let V be an open set and D be a closed disk contained in V . If $f , g \in \mathbf { H } ( V )$ satisfy

$$
| f ( z ) - g ( z ) | < | f ( z ) | + | g ( z ) |
$$

on the boundary of D, then f and g have the same number of zeroes in the interior of D.

The more classical Rouche’s theorem states the result for the stronger condition

$$
| f ( z ) - g ( z ) | < | f ( z ) |
$$

which usually suffices.

The applications of Rouche’s theorem come up a lot in prelims. Sometimes even the statement of the theorem gets asked. Here are some examples:

Spring 2012, 2b. Use Rouche’s theorem to find the number of zeros of the polynomial $z ^ { 4 } + 5 z + 3$ in the annulus $1 < | z | < 2$

It is clear what to do here. Let $f ( z )$ be the given polynomial. For $| z | = 2 ,$ we have

$$
| f ( z ) - z ^ { 4 } | = | 5 z + 3 | \leq | 5 z | + 3 = 1 3 < 1 6 = | z ^ { 4 } | .
$$

Therefore by Rouche’s theorem $f ( z )$ and $z ^ { 4 }$ have the same number of zeros inside the disk $| z | < 2 . ~ z ^ { 4 }$ has four zeros (which are all 0, pun intended) in $| z | < 2$ , so $f$ has 4 zeros in $| z | < 2$ . And for $| z | = 1$ ,

$$
\left| f ( z ) - ( 5 z + 3 ) \right| = | z ^ { 4 } | = 1 < 2 = | | 5 z | - | - 3 | | \leq | 5 z - ( - 3 ) | = | 5 z + 3 | .
$$

Therefore again by Rouche’s theorem $f ( z )$ and $5 z + 3$ have the same number of zeros in $| z | < 1$ . The only zero of $5 z + 3 ~ \mathrm { i s \ - 3 / 5 }$ which is in the unit disk; thus $f$ has a single zero in $| z | < 1$

Psychologically, the problem seems over here but there is a subtle point: We showed that f has four zeros in $| z | < 2$ and a single zero in $| z | < 1$ . Hence, $f$ has three zeros in $1 \leq | z | < 2$ . To make the first inequality strict, we also need to show that $f$ has no zeros on $| z | = 1$ . Indeed, in this case

$$
\vert f ( z ) \vert = \vert 5 z + 3 - ( - z ^ { 4 } ) \vert \ge \vert \vert 5 z + 3 \vert - \vert - z ^ { 4 } \vert \vert = \vert \vert 5 z + 3 \vert - 1 \vert
$$

And just above we showed above that $| 5 z + 3 | > 2 \ \mathrm { o n } \ | z | = 1$ . Hence $| f ( z ) | > 1$ o n $| z | = 1$

It might be worth noting that the functions we used to apply Rouche’s theorem to were all entire, i.e. in $\mathbf { H } ( \mathbb { C } )$ , so we were able to use any disk we want.

Fall 2011, 1. Show that $z ^ { 5 } + 3 z ^ { 3 } + 7$ has all its zeros in the disk $| z | < 2 .$

Let $f ( z )$ be the given polynomial. f has five zeros, so $z ^ { 5 }$ , which has all of its five zeros in $| z | < 2$ , is the best candidate to apply Rouche’s theorem. Note that both $f ( z )$ and $z ^ { 5 }$ are entire functions and for $| z | = 2 ,$ we have

$$
| f ( z ) - z ^ { 5 } | = | 3 z ^ { 3 } + 7 | \leq | 3 z ^ { 3 } | + | 7 | = 3 1 < 3 2 = | z ^ { 5 } |
$$

and we are done.

Spring 2011, 1. Prove that for any $a \in \mathbb { C }$ and $n \geq 2 .$ , the polynomial $a z ^ { n } + z + 1$ has at least one root in the disk $| z | \le 2$

Let $f ( z )$ be the given polynomial, it is entire. This question is more challenging than the previous two, because a heavily influences the growth of $f .$ The trick is to write

$$
a z ^ { n } + z + 1 = f ( z ) = a ( z - \omega _ { 1 } ) \cdot \cdot \cdot ( z - \omega _ { n } )
$$

where $\omega _ { i } { ' } \mathrm { s }$ are the roots of $f .$ . This is possible since $\mathbb { C }$ is algebraically closed. Comparing the constant terms, we get

$$
1 = a ( - \omega _ { 1 } ) \cdot \cdot \cdot ( - \omega _ { n } ) ,
$$

thus

$$
\left| \omega _ { 1 } \right| \cdot \cdot \cdot \left| \omega _ { n } \right| = { \frac { 1 } { \left| a \right| } } .
$$

Therefore if ${ \frac { 1 } { | a | } } \leq 2 ^ { n }$ , at least one of $\omega _ { i } { \mathrm { : } }$ ’s should satisfy $| \omega _ { i } | \le 2$ . So this handles the case $\begin{array} { r } { | a | \geq \frac { 1 } { 2 ^ { n } } } \end{array}$ . For $\textstyle | a | < { \frac { 1 } { 2 ^ { n } } }$ , we compare $f ( z )$ and $z + 1$ in Rouche’s theorem on the disk $| z | < 2$ . When $| z | = 2$ , we have

$$
| f ( z ) - ( z + 1 ) | = | a z ^ { n } | < 1 = | | z | - 1 | | \leq | z - ( - 1 ) | = | z + 1 | .
$$

Since the only zero −1 of $z + 1$ is in the disk $| z | < 2$ , f also has a single zero there in this case.

Spring 2011, 8b. Use Rouche’s theorem to prove the fundamental theorem of algebra.

We show that every nonconstant monic polynomial of degree n has n roots. Let $f$ be such a polynomial written as

$$
f ( z ) = z ^ { n } + a _ { n - 1 } z ^ { n - 1 } + a _ { n - 2 } z ^ { n - 2 } + \cdot \cdot \cdot + a _ { 1 } z + a _ { 0 }
$$

Choose R such that

$$
R > | a _ { n - 1 } | + | a _ { n - 2 } | + . . . | a _ { 1 } | + | a _ { 0 } | { \mathrm { ~ a n d ~ } } R > 1 .
$$

For $| z | = R$ we have

$$
\begin{array} { r l } & { | f ( z ) - z ^ { n } | = | a _ { n - 1 } z ^ { n - 1 } + a _ { n - 2 } z ^ { n - 2 } \cdot \cdot \cdot \cdot a _ { 1 } z + a _ { 0 } | } \\ & { \qquad \leq | a _ { n - 1 } z ^ { n - 1 } | + | a _ { n - 2 } z ^ { n - 2 } | \cdot \cdot \cdot | a _ { 1 } z | + | a _ { 0 } | } \\ & { \qquad = | a _ { n - 1 } | R ^ { n - 1 } + | a _ { n - 2 } | R ^ { n - 2 } \cdot \cdot \cdot | a _ { 1 } | R + | a _ { 0 } | } \\ & { \qquad \leq | a _ { n - 1 } | R ^ { n - 1 } + | a _ { n - 2 } | R ^ { n - 1 } \cdot \cdot \cdot | a _ { 1 } | R ^ { n - 1 } + | a _ { 0 } | R ^ { n - 1 } } \\ & { \qquad = R ^ { n - 1 } \left( | a _ { n - 1 } | + | a _ { n - 2 } | + \cdot \cdot \cdot + | a _ { 1 } | + | a _ { 0 } | \right) } \\ & { \qquad < R ^ { n } = | z ^ { n } | } \end{array}
$$

Also $f ( z )$ and $z ^ { n }$ are entire functions. Therefore by Rouche’s theorem, in $| z | < R , f ( z )$ and $z ^ { n }$ zn have the same number of roots, which is n.

Fall 2009, 1. How many roots (counted with multiplicity) does the function

$$
g ( z ) = 6 z ^ { 3 } + e ^ { z } + 1
$$

have in the unit disk $| z | < 1 2$

This time we don’t have a polynomial. $g$ is of course entire though and for $| z | = 1$

$$
\left| g ( z ) - 6 z ^ { 3 } \right| = \left| e ^ { z } + 1 \right| \le \left| e ^ { z } \right| + 1 = e ^ { \mathrm { R e } ( z ) } + 1 \le e ^ { \left| z \right| } + 1 = e + 1 < 6 = \left| 6 z ^ { 3 } \right| .
$$

Therefore by Rouche’s theorem, $f ( z )$ and $6 z ^ { 3 }$ have the same number of zeros in $| z | < 1$ which is three.

Spring 2009, 4. How many zeros does the function $f ( z ) = z ^ { 6 } + 4 z ^ { 2 } e ^ { z + 1 } - 3$ have in the unit disk $D ( 0 , 1 ) \mathrm { ? }$

Let’s try to apply Rouche for the entire functions $f ( z )$ and $4 z ^ { 2 } e ^ { z + 1 }$ . For $| z | = 1$

$$
| f ( z ) - 4 z ^ { 2 } e ^ { z + 1 } | = | z ^ { 6 } - 3 | \leq | z ^ { 6 } | + 3 = 4
$$

On the other hand, again for $| z | = 1$

$$
| 4 z ^ { 2 } e ^ { z + 1 } | = 4 | e ^ { z + 1 } | = 4 e | e ^ { z } | = 4 e \cdot e ^ { \mathrm { R e } ( z ) } \geq 4 e \cdot e ^ { - 1 } = 4
$$

because on the unit circle, $\mathrm { R e } ( z ) \geq - 1$ . Thus, we get that

$$
| f ( z ) - 4 z ^ { 2 } e ^ { z + 1 } | \leq | 4 z ^ { 2 } e ^ { z + 1 } |
$$

on $| z | = 1$ . The problem is we didn’t get the strict inequality that Rouche’s theorem requires. However, looking at how we arrived at this inequality, the two terms being equal can only occur if $| z ^ { \bar { 6 } } - 3 | = 4$ and $\operatorname { R e } ( z ) = - 1$ for some z where $| z | = 1$ . The latter yields $z = - 1$ , but $| ( - 1 ) ^ { \dot { 6 } } - 3 | = 2 \neq 4$ . So equality can never occur. Thus, $f ( z )$ and $4 z ^ { 2 } e ^ { z + 1 }$ have the same number of zeros in $| z | < 1$ , which is $2 ~ ( 0$ is the only root of the latter function and it has order 2).

Fall 2008, 1b. Determine the number of zeros of $\begin{array} { r } { P ( z ) = z ^ { 7 } + z ^ { 3 } + \frac { 1 } { 1 6 } } \end{array}$ that lie in   
the closed disk $| z | \leq 1 / 2 .$

$P ( z )$ and $z ^ { 3 }$ are entire functions and on $| z | = 1 / 2 ,$

$$
| P ( z ) - z ^ { 3 } | = \left| z ^ { 7 } + { \frac { 1 } { 1 6 } } \right| \leq | z ^ { 7 } | + { \frac { 1 } { 1 6 } } = { \frac { 1 } { 2 ^ { 7 } } } + { \frac { 1 } { 2 ^ { 4 } } } = { \frac { 9 } { 2 ^ { 7 } } } < { \frac { 1 6 } { 2 ^ { 7 } } } = { \frac { 1 } { 2 ^ { 3 } } } = | z ^ { 3 } | .
$$

Therefore, in $| z | < 1 / 2 , P ( z )$ and $z ^ { 3 }$ have the same number of zeros, which is 3. For $| z | = 1 / 2$ , we have

$$
\left| P ( z ) \right| \geq \left| | z ^ { 7 } | - \left| z ^ { 3 } + { \frac { 1 } { 1 6 } } \right| \right| = \left| { \frac { 1 } { 2 ^ { 7 } } } - \left| z ^ { 3 } + { \frac { 1 } { 1 6 } } \right| \right| .
$$

Since $\begin{array} { r } { \left| z ^ { 3 } + \frac { 1 } { 1 6 } \right| \geq \left| | z ^ { 3 } | - \frac { 1 } { 1 6 } \right| = \left| \frac { 1 } { 2 ^ { 3 } } - \frac { 1 } { 1 6 } \right| = \frac { 1 } { 1 6 } , } \end{array}$ we get

$$
| P ( z ) | \geq \left| { \frac { 1 } { 2 ^ { 7 } } } - \left( z ^ { 3 } + { \frac { 1 } { 1 6 } } \right) \right| = \left| z ^ { 3 } + { \frac { 1 } { 1 6 } } - { \frac { 1 } { 2 ^ { 7 } } } \right| = \left| z ^ { 3 } + { \frac { 7 } { 2 ^ { 7 } } } \right| \geq \left| | z ^ { 3 } | - { \frac { 7 } { 2 ^ { 7 } } } \right| = \left| { \frac { 1 } { 2 ^ { 3 } } } - { \frac { 7 } { 2 ^ { 7 } } } \right| = { \frac { 9 } { 2 ^ { 7 } } } .
$$

Hence $P ( z )$ has no zeros on $| z | = 1 / 2$ . The answer is 3.

Spring 2008, 4. If $\lambda > 1$ , show that the equation $z + e ^ { - z } = \lambda$ has exactly one solution with positive real part.

Let, by our experience from IVT questions in calculus, $f ( z ) = z + e ^ { - z } - \lambda .$ . Consider the circle centered at the origin with radius $R ,$ cut it into two with the y-axis and let the right semicircle be $\gamma _ { R }$ . It suffices to show that, for every $R > \lambda + 1 , f$ has a single zero inside $\gamma _ { R }$ (because the interiors of such semicircles cover the entire right half plane). Here $f ( z )$ and $z - \lambda$ are entire functions, and when z is on $\gamma _ { R } .$ , we have

$$
\left| f ( z ) - ( z - \lambda ) \right| = \left| e ^ { - z } \right| = e ^ { \operatorname { R e } ( - z ) } = e ^ { - \operatorname { R e } ( z ) } \leq 1 < \left| R - \lambda \right| = \left| \left| z \right| - \left| \lambda \right| \right| \leq \left| z - \lambda \right| .
$$

Therefore by Rouche’s theorem, $f ( z )$ and $z - \lambda$ have the same number of zeros inside $\gamma _ { R }$ . The only root λ of $z - \lambda$ lies inside $\gamma _ { R }$ (as $R > \lambda$ and $\lambda > 0 )$ , therefore f also has

a single root inside $\gamma _ { R }$ . It seems that $\lambda > 0$ is enough for this question. Maybe I did something wrong.

Fall 2007, 7. Determine the number of zeros of $e ^ { z ^ { 2 } } - 4 z ^ { 2 }$ in the open unit disk.

Let $f ( z ) = e ^ { z ^ { 2 } } - 4 z ^ { 2 }$ and $g ( z ) = - 4 z ^ { 2 } . f ( z )$ and $g ( z )$ are entire functions, and on $| z | = 1$ , we have

$$
\left| f ( z ) - g ( z ) \right| = \left| e ^ { z ^ { 2 } } \right| = e ^ { \mathrm { R e } ( z ^ { 2 } ) } \leq e ^ { \left| z ^ { 2 } \right| } = e < 4 = \left| g ( z ) \right| .
$$

Therefore, by Rouche’s theorem f and g have the same number of zeros in $| z | < 1$ , which is 2.

## 4. Schwarz’s lemma

Let D denote the open unit disk.

Scwharz’s Lemma. Suppose that $f : \mathbb { D }  \mathbb { D }$ is holomorphic and $f ( 0 ) = 0$ . Then $| f ( z ) | \leq | z |$ for all $z \in \mathbb { D }$ and $| f ^ { \prime } ( 0 ) | \le 1$ . Furthermore, $i f \left| f ^ { \prime } ( 0 ) \right| = 1 \ o r \left| f ( z ) \right| = | z | \ f o r$ some nonzero $z \in \mathbb { D }$ then f is a rotation: $f ( z ) = \beta z$ for some constant $\beta$ with $| \beta | = 1$

Fall 2012, 6. Let $f ( z )$ be an analytic function in the upper half plane   
{z ∈ C : Im(z) > 0} .   
Suppose that $| f ( z ) | < 1$ for all z in the domain of $f ,$ and $f ( i ) = 0$ . Find the largest   
possible value of $| f ( 2 i ) |$

Let H be the upper half plane. So we can consider f as a function from H to D. The linear-fractional transformation

$$
\phi ( z ) = { \frac { z - i } { z + i } }
$$

maps H conformally onto D (this was observed in a previous section). So its inverse

$$
\phi ^ { - 1 } ( z ) = \frac { i z + i } { - z + 1 } = \frac { z + 1 } { i z - i }
$$

maps D onto H, thus $f \circ \phi ^ { - 1 }$ is a holomorphic function that maps D to D. Moreover,

$$
( f \circ \phi ^ { - 1 } ) ( 0 ) = f ( i ) = 0 .
$$

Hence, by Schwarz’s lemma we have $| ( f \circ \phi ) ( z ) | \leq | z |$ and in particular we have

$$
| f ( 2 i ) | = | ( f \circ \phi ^ { - 1 } \circ \phi ) ( 2 i ) | = | ( f \circ \phi ^ { - 1 } ) ( \phi ( 2 i ) ) | = \left| ( f \circ \phi ^ { - 1 } ) \left( \frac { 1 } { 3 } \right) \right| \leq \left| \frac { 1 } { 3 } \right| = \frac { 1 } { 3 } .
$$

Also, again by Schwarz’s lemma $| f ( 2 i ) | = 1 / 3$ only if $( f \circ \phi ^ { - 1 } ) ( z ) = \beta z$ for some $| \beta | = 1$ So in this case,

$$
f ( z ) = ( f \circ \phi ^ { - 1 } \circ \phi ) ( z ) = \beta \cdot \phi ( z ) .
$$

Indeed, if $f ( z ) = { \boldsymbol { \beta } } \cdot \phi ( z )$ for some $| \beta | = 1 , f$ maps H to D, $f ( i ) = 0$ and $| f ( 2 i ) | = 1 / 3$ So $1 / 3$ actually is the largest possible value for $| f ( 2 i ) |$ •

```latex
Fall 2012, 8c. Let f be a holomorphic function in the unit disk D and suppose
that $f ( 0 ) = 0$ and $| f ( z ) | \leq 1$ Prove that for any integer $m \geq 1 , f ( z ) - 2 ^ { m } z ^ { m }$ has
exactly m zeros (counting multiplicity) in the disk $| z | < 1 / 2$
Note: The (a) and (b) parts of this question ask the statements of Rouche’s theorem
and Schwarz’s lemma, respectively. So the message we get is ‘you will need both in $\mathrm { ( c ) } ^ { \prime }$
Let $g ( z ) = f ( z ) - 2 ^ { m } z ^ { m }$ If f is constant, since $f ( 0 ) = 0 , f$ must be identically 0 and
so 0 is the only zero of $g ( z ) = - 2 ^ { m } z ^ { m }$ and it has order m. If $f$ is not constant, it is
an open map by the open mapping theorem. We are given that $f ( \mathbb { D } ) \subseteq \overline { { \mathbb { D } } }$ , so actually
$f ( \mathbb { D } ) \subseteq \operatorname { I n t } ( { \overline { { \mathbb { D } } } } ) = \mathbb { D } .$ Thus we can use Schwarz’s lemma to conclude that $| f ( z ) | \leq | z |$
This inequality paves the way for Rouche’s theorem. Indeed, $g ( z )$ and $- 2 ^ { m } z ^ { m }$ are
analytic in a neighborhood of the closed disk $| z | \le 1 / 2$ and on the boundary $| z | = 1 / 2$ ,
we have
$| g ( z ) - ( - 2 ^ { m } z ^ { m } ) | = | f ( z ) | \leq | z | = { \frac { 1 } { 2 } } < 1 = | - 2 ^ { m } z ^ { m } | .$
Thus $g ( z )$ and $- 2 ^ { m } z ^ { m }$ have the same number of roots inside $| z | < 1 / 2$ , which is m.
Fall 2011, 4. Let f be a holomorphic function in the right half-plane $\{ z \in \mathbb { C } :$
$\mathrm { R e } ( z ) > 0 \}$ . Suppose that $| f ( z ) | < 1$ for all z in the domain of $f ,$ and $f ( 1 ) = 0$
Find the largest value of $\left| f ( 2 ) \right|$
Let P denote the right half plane. We can consider f as a function from P to the unit
disk D. Similar to the Fall 2012 question, we first map P to D. Since $z \in P$ if and only
if z is closer to 1 than it is to −1, if and only if $| z - 1 | < | z + 1 |$ , the linear fractional
transformation
$\phi ( z ) = \frac { z - 1 } { z + 1 }$
maps P (conformally) onto D. So its inverse
$\phi ^ { - 1 } ( z ) = { \frac { z + 1 } { - z + 1 } } = { \frac { z + 1 } { 1 - z } }$
maps D onto P . Now, the analytic function $f \circ \phi ^ { - 1 } : \mathbb { D } \to \mathbb { D }$ satisfies
$( f \circ \phi ^ { - 1 } ) ( 0 ) = f ( 1 ) = 0 .$
Hence, by Schwarz’s lemma, $| ( f \circ \phi ^ { - 1 } ) ( z ) | \leq | z |$ . In particular,
$| f ( 2 ) | = | ( f \circ \phi ^ { - 1 } \circ \phi ) ( 2 ) | = | ( f \circ \phi ^ { - 1 } ) ( \phi ( 2 ) ) | \leq | \phi ( 2 ) | = { \frac { 1 } { 3 } } .$
To see that this bound is sharp when f varies, note that again by Schwarz’s lemma, if
we have equality above then $( { \bar { f } } \circ \phi ^ { - 1 } ) { \bar { ( } } z ) = \beta z$ for some $| \beta | = 1$ . Then
$f ( z ) = ( f \circ \phi ^ { - 1 } \circ \phi ) ( z ) = ( f \circ \phi ^ { - 1 } ) ( \phi ( z ) ) = \beta \cdot \phi ( z ) .$
And indeed if we define $f$ as above for any $| \beta | = 1$ , f maps P to D, and $| f ( 2 ) | =$
$\begin{array} { r } { | \phi ( 2 ) | = \frac { 1 } { 3 } } \end{array}$ . So $\frac { 1 } { 3 }$ is really the largest possible value for $| f ( 2 ) |$
Spring 2011, 4. Let f be a holomorphic function in the unit disk D and suppose
that $f ( 0 ) = f ^ { \prime } ( 0 ) = 0$ . Prove that $| f ^ { \prime \prime } ( 0 ) | \le 2$ and describe all such $f$ with $| f ^ { \prime \prime } ( 0 ) | =$
2.
```

It should be stated in this question that $f$ maps D to itself, otherwise the statement is false (consider $f ( z ) = 2 z ^ { 2 } )$ .

Note that, if $D _ { r }$ is the disk centered at 0 with radius $r < 1$ , by Cauchy’s integral formula (integrating along the boundary of $D _ { r } )$ f has a power series representation inside $D _ { r }$ Sending $r  1$ we actually get a power series representation for f valid inside all of D. Since $f ( 0 ) = 0$ , the constant term of the power series is 0 and hence

$$
f ( z ) = z g ( z )
$$

for some analytic function $g : \mathbb { D }  \mathbb { C }$ . By Schwarz’s lemma $| f ( z ) | \leq | z |$ , so we get $| g ( z ) | \leq 1$ (for every $z \in \mathbb { D } )$ , that is, $g ( \mathbb { D } ) \subseteq { \overline { { \mathbb { D } } } }$ . By the open mapping theorem, there are two cases:

```latex
$g$ is constant. Then $f ^ { \prime \prime } ( z ) = 0$ for all z, so $f ^ { \prime \prime } ( 0 ) = 0 \quad$
• g is an open map. Then $g ( \mathbb { D } ) \subseteq \operatorname { I n t } ( \overline { { \mathbb { D } } } ) = \mathbb { D }$ . Since $f ^ { \prime } ( 0 ) = 0$ , the degree of the
z term in the power series representation of f is 0; thus $g ( 0 ) = 0 .$ . So Schwarz’s
lemma applies to g and we get $| g ^ { \prime } ( 0 ) | \le 1$ . Considering the coefficient of the $z ^ { 2 }$
term in the power series of $f ,$ , we get ${ \frac { f ^ { \prime \prime } ( 0 ) } { 2 } } = g ^ { \prime } ( 0 )$ . Thus $| f ^ { \prime \prime } ( 0 ) | \le 2$ . And
|f 00(0)| = 2 ⇔ |g0(0)| = 1
⇔ g(z) = βz for some $| \beta | = 1$ (Schwarz)
⇔ f (z) = βz2 for some |β| = 1 .
Spring 2010, 8. Let D be the unit disk and let $f ( z )$ be an analytic function which
maps D to itself. Suppose f has a fixed point $c \in \mathbb { D }$ , that is, $f ( c ) = c$ . Furthermore,
assume that $| f ^ { \prime } ( c ) | < 1$ . Prove that for any point $z _ { 0 } \in \mathbb { D }$ , the sequence $z _ { n }$ defined
by iteration, $z _ { n } = f ( z _ { n - 1 } )$ converges to c. (Hint: first consider the case $c = 0 )$
```

Proposition 4. Let $f : \mathbb { D } \to \mathbb { D }$ be analytic such that $f ( 0 ) = 0$ and let $0 < r < 1$ . If f is not a rotation, then there exists $0 < \delta < 1$ such that for $| z | < r$ , we have $| f ( z ) | \leq \delta | z |$

Proof. We may assume that f is not identically zero, so f is not constant (using the open mapping theorem and $f ( 0 ) = 0 )$ . Let $D _ { r } \dot { = } \{ z \in \mathbb { D } : \lvert z \rvert < r \}$ . On the compact set $\overline { { D _ { r } } } ,$ the function $| f ( z ) |$ achieves a maximum, say $M > 0$ (a nonzero analytic function on D cannot vanish on a disk, however small). By both parts of Schwarz’s lemma, we get that $M \ < \ r$ . Also note that for $z \in D _ { r } , | f ( z ) | < M$ by the maximum modulus theorem. Therefore the function $g : { \mathbb { D } }  { \mathbb { D } }$ given by

$$
g ( \omega ) = { \frac { f ( r \omega ) } { M } }
$$

$$
| g ( \omega ) | \leq | \omega |
$$

$$
g ( 0 ) = 0
$$

$$
\omega \in \mathbb { D }
$$

$$
g ,
$$

$$
z \in D _ { r }
$$

$$
z / r \in \mathbb { D }
$$

$$
\left| { \frac { z } { r } } \right| \geq \left| g \left( { \frac { z } { r } } \right) \right| = { \frac { | f ( z ) | } { M } } .
$$

$$
0 < \delta < 1
$$

$$
| z | < r , | f ( z ) | \leq \delta | z |
$$

We claim that $| z _ { n } | < r$ and $| z _ { n } | \leq \delta ^ { n }$ for every n. Employ induction on $n ;$ the basis case is trivial since $z _ { 0 } \in \mathbb { D }$ . Assuming $| z _ { n - 1 } | < r$ and $| z _ { n - 1 } | \leq \delta ^ { n - 1 }$ , we get

$$
| z _ { n } | = | f ( z _ { n - 1 } ) | < | z _ { n - 1 } | < r
$$

and again by Proposition 4,

$$
| z _ { n } | = | f ( z _ { n - 1 } ) | \leq \delta | z _ { n - 1 } | \leq \delta \cdot \delta ^ { n - 1 } = \delta ^ { n } .
$$

Thus $\scriptstyle \operatorname* { l i m } _ { n \to \infty } z _ { n } = 0$ since $0 < \delta < 1$

For $c \neq 0$ , consider the linear fractional transformation

$$
\phi ( z ) = { \frac { c - z } { 1 - \bar { c } z } } = { \frac { z - c } { \bar { c } z - 1 } } .
$$

We claim that $\phi$ maps D to D. Firstly, $\mathrm { i f } \ | z | = 1$ , we have

$$
\begin{array} { l } { | \phi ( z ) | ^ { 2 } = \displaystyle \frac { ( z - c ) ( \overline { { z } } - \overline { { c } } ) } { ( \overline { { c } } z - 1 ) ( c \overline { { z } } - 1 ) } } \\ { = \displaystyle \frac { | z | ^ { 2 } - c \overline { { z } } - \overline { { c } } z + | c ^ { 2 } | } { | c z | ^ { 2 } - \overline { { c } } z - c \overline { { z } } + 1 } } \\ { = 1 . } \end{array}
$$

So $\phi$ maps the unit circle to itself. And as $\phi ( 0 ) = c \in \mathbb { D } , \phi$ maps D to itself. Moreover since

$$
\left[ \begin{array} { c c } { { 1 } } & { { - c } } \\ { { \overline { { c } } } } & { { - 1 } } \end{array} \right] \left[ \begin{array} { c c } { { 1 } } & { { - c } } \\ { { \overline { { c } } } } & { { - 1 } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 - | c | ^ { 2 } } } & { { 0 } } \\ { { 0 } } & { { 1 - | c | ^ { 2 } } } \end{array} \right]
$$

and $| c | < 1 , \phi \circ \phi = \mathrm { i d } _ { \mathbb { D } }$ . Let $\tilde { f } = \phi \circ f \circ \phi : \mathbb { D } \to \mathbb { D }$ . Now ${ \tilde { f } } ( 0 ) = \phi ( f ( c ) ) = \phi ( c ) = 0$ And by the chain rule,

$$
\begin{array} { r l } & { \tilde { f } ^ { \prime } ( 0 ) = ( \phi \circ f ) ^ { \prime } ( \phi ( 0 ) ) \cdot \phi ^ { \prime } ( 0 ) } \\ & { \qquad = ( \phi \circ f ) ^ { \prime } ( c ) \cdot \phi ^ { \prime } ( 0 ) } \\ & { \qquad = \phi ^ { \prime } ( f ( c ) ) \cdot f ^ { \prime } ( c ) \cdot \phi ^ { \prime } ( 0 ) } \\ & { \qquad = \phi ^ { \prime } ( c ) \cdot f ^ { \prime } ( c ) \cdot \phi ^ { \prime } ( 0 ) } \\ & { \qquad = f ^ { \prime } ( c ) \cdot \phi ^ { \prime } ( \phi ( 0 ) ) \cdot \phi ^ { \prime } ( 0 ) } \\ & { \qquad = f ^ { \prime } ( c ) ( \phi \circ \phi ) ^ { \prime } ( 0 ) } \\ & { \qquad = f ^ { \prime } ( c ) . } \end{array}
$$

Finally, let $\omega _ { n } = \phi ( z _ { n } )$ for each n. Then for $n \geq 1$ , we have

$$
\omega _ { n } = \phi ( z _ { n } ) = \phi ( f ( z _ { n - 1 } ) ) = \phi ( f ( \phi ( \omega _ { n - 1 } ) ) ) = \tilde { f } ( \omega _ { n - 1 } )
$$

therefore $\omega _ { n } \to 0$ from the first part. Therefore by continuity, $z _ { n } = \phi ( \omega _ { n } )  \phi ( 0 ) = c \mathrm { , }$

Fall 2009, 8. Let $f : \mathbb { D } \to \mathbb { D }$ be analytic. Suppose there are points $p , q \in \mathbb { D } , p \neq q$ such that $f ( p ) = p$ and $f ( q ) = q , { \mathrm { i . e . , ~ } } f$ has two fixed points. Show that $f ( z ) = z$ for all $z \in \mathbb { D }$ . Hint: first consider the case where one of the fixed points is the origin, $p = 0$

The previous question can be used as a sledgehammer here, but it is probably unnecessarily strong. We can deal with this by Schwarz only. As suggested, let’s consider the case $p = 0$ . Since $| f ( q ) | = | q |$ and $q \neq 0 , f ( z ) = \beta z$ for some $| \beta | = 1$ by Schwarz’s

lemma. And $\beta$ has to be 1 since $f ( q ) = q$

For the general case, similar to the previous question, let

$$
\phi ( z ) = \frac { p - z } { 1 - \overline { { p } } z } .
$$

Then the analytic function $g = \phi \circ f \circ \phi : \mathbb { D } \to \mathbb { D }$ satisfies

$$
g ( 0 ) = \phi ( f ( \phi ( 0 ) ) ) = \phi ( f ( p ) ) = \phi ( p ) = 0
$$

and

$$
g ( \phi ( q ) ) = \phi ( f ( q ) ) = \phi ( q )
$$

since $\phi = \phi ^ { - 1 }$ . As $p \neq q$ , we have $\phi ( q ) \neq 0$ and hence by the first case $g = \mathrm { i d _ { \mathbb { D } } }$ . Thus $f = \mathrm { i d } _ { \mathbb { D } }$

## 5. Cauchy’s Estimates

These are the only ‘named’ estimates I know. This probably speaks more about my ignorance in analysis than the lack of such estimates. Anyway, here they are:

Cauchy’s Estimates. Suppose that f is holomorphic in a neighborhood of the closed disk $\overline { { D ( z _ { 0 } , r ) } }$ and $| f | \leq M$ in $\overline { { D ( z _ { 0 } , r ) } }$ . Then

$$
\left. f ^ { ( n ) } ( z _ { 0 } ) \right. \leq { \frac { M n ! } { r ^ { n } } }
$$

for every $n \in \mathbb { N } .$

Liouville’s theorem, that is, the fact that entire and bounded functions are constant is an easy corollary. Examples:

Fall 2012, 5 and Fall 2010, 6. Suppose that $g : \mathbb { C } \to \mathbb { C }$ is a holomorphic function, k and n are integers, and $( 2 + \bar { | z ^ { k } | } ) ^ { - 1 } g ^ { ( n ) } ( \bar { z } )$ is bounded on $\mathbb { C } .$

• Prove that g is a polynomial.

• Estimate the degree of g in terms of the integers k and n.

Let $h = g ^ { ( n ) }$ , so h is entire and $| h ( z ) | \leq M ( 2 + | z ^ { k } | )$ for some $M > 0$ . Fix $r > 0$ . Now for $| z | \leq r$ , we have $| h ( z ) | \leq M { \dot { ( 2 + r ^ { k } ) } }$ , therefore we can apply Cauchy’s estimates to $\overline { { { \cal D } ( 0 , r ) } }$ to get

$$
| h ^ { ( m ) } ( 0 ) | \leq \frac { M ( 2 + r ^ { k } ) m ! } { r ^ { m } }
$$

for every $m \in \mathbb { N }$ . Sending $r  \infty$ above yields $g ^ { ( m + n ) } ( 0 ) = h ^ { ( m ) } ( 0 ) = 0$ for $m > k$ As an entire function, g has a global power series representation around 0; thus g is a polynomial of degree at most $k + n$

Spring 2012, 3. Let $f ( z )$ be an entire function. Suppose that there are positive real numbers $a , b$ and k such that $| f ( z ) | \leq a + b | z | ^ { k }$ for all $z \in \mathbb { C }$ . Prove that $f ( z )$ is a polynomial.

Same thing. Fix $r > 0$ . For $| z | \leq r$ , we have

$$
| f ( z ) | \leq a + b r ^ { k } .
$$

Thus by Cauchy’s estimates applied to $D ( 0 , r )$ , we get

$$
\left| f ^ { ( n ) } ( 0 ) \right| \leq { \frac { ( a + b r ^ { k } ) n ! } { r ^ { n } } }
$$

for every $n \in \mathbb N$ . Thus, sending $r  \infty$ above, we get $f ^ { ( n ) } ( 0 ) = 0$ for $n > k$ . Being entire, f has a global power series around 0, so f is a polynomial of degree at most dke.

Spring 2011, 5. Prove that a nonconstant entire function maps C onto a dense subset of C.

We show the contrapositive. Assume f is an entire function such that $f ( \mathbb { C } )$ is not dense in C. Then there exists $z _ { 0 } \in \mathbb { C }$ and $\epsilon > 0$ such that

$$
D ( z _ { 0 } , \epsilon ) \cap f ( \mathbb { C } ) = \varnothing .
$$

That is, $| f ( z ) - z _ { 0 } | \geq \epsilon$ for every $z \in \mathbb { C }$ . Thus

$$
g ( z ) = { \frac { 1 } { f ( z ) - z _ { 0 } } }
$$

is an entire function which is bounded by $\frac { 1 } { \epsilon } .$ . Thus, by Liouville’s theorem g is constant.   
Hence f is constant.

Spring 2011, 6. Suppose f is an entire function, and there is a positive real number M such that $| \operatorname { R e } ( f ( z ) ) | \geq | \operatorname { I m } ( f ( z ) ) |$ for all z with $| z | \geq M$ . Prove that f is constant on C.

By the previous question, it suffices to show that $f ( \mathbb { C } )$ is not dense in C. Suppose, to the contrary, it is dense. Let

$$
K = \{ z \in \mathbb { C } : | z | \leq M \}
$$

and

$$
\begin{array} { r } { \Omega = \left\{ z \in \mathbb { C } : | \operatorname { R e } ( f ( z ) ) | \ge | \operatorname { I m } ( f ( z ) ) | \right\} . } \end{array}
$$

We have $f ( \mathbb { C } - K ) \subseteq \Omega$ . Since Ω is closed, ${ \overline { { f ( \mathbb { C } - K ) } } } \subseteq \Omega$ . Also note that $f ( K )$ is closed and bounded since K is compact. Now,

$$
{ \begin{array} { r l } & { \mathbb { C } = { \overline { { f ( \mathbb { C } ) } } } } \\ & { \quad = { \overline { { f ( K ) \cup f ( \mathbb { C } - K ) } } } } \\ & { \quad = { \overline { { f ( K ) } } } \cup { \overline { { f ( \mathbb { C } - K ) } } } } \\ & { \quad \subseteq f ( K ) \cup \Omega . } \end{array} }
$$

Thus $\mathbb { C } - \Omega \subseteq f ( K )$ . This is a contradiction because $\mathbb { C } - \Omega$ is unbounded.

Fall 2010, 5. Let f be a holomorphic function in the unit disk $D ( 0 , 1 )$ and $| f ( z ) | \leq M$ for all $z \in D ( 0 , 1 )$ . Prove that $| f ^ { \prime } ( z ) | \leq M ( 1 - | z | ) ^ { - 1 }$ for all $z \in D ( 0 , 1 )$

Fix $z _ { 0 } \in D ( 0 , 1 )$ and choose δ such that $| z _ { 0 } | < \delta < 1$ . Then if $z \in \overline { { D ( z _ { 0 } , \delta - | z _ { 0 } | ) } }$ , we have

$$
| z | = | z - z _ { 0 } + z _ { 0 } | \leq | z - z _ { 0 } | + | z _ { 0 } | \leq \delta - | z _ { 0 } | + | z _ { 0 } | = \delta < 1 .
$$

That is, $\overline { { D ( z _ { 0 } , \delta - | z _ { 0 } | ) } } \subseteq D ( 0 , 1 )$ and hence $| f | \le M$ in this closed disk. Thus by Cauchy’s estimates, we get

$$
\left| f ^ { \prime } ( z _ { 0 } ) \right| \leq { \frac { M } { \delta - | z _ { 0 } | } } .
$$

This is true for every $0 < \delta < 1$ . Thus sending $\delta \to 1$ , we get

$$
| f ^ { \prime } ( z _ { 0 } ) | \leq { \frac { M } { 1 - | z _ { 0 } | } } .
$$

Fall 2009, 5. Let $f ( z )$ be an analytic function on C which takes values in the upper half plane, i.e., $f : \mathbb { C } \to H$ , where $H = \{ x + i y : y > 0 \}$ . Show that $f$ is constant.

The only nontrivial part is to recall that H can be mapped conformally onto the unit disk D. Indeed, the linear fractional transformation

$$
\phi ( z ) = { \frac { z - i } { z + i } }
$$

does precisely that because $z \in D$ if and only if z is closer to i than it is to $- i ,$ if and only if $| z - i | < | z + i |$ Thus $g = \phi \circ f$ maps the entire plane into D. Being entire and bounded, g is constant by Liouville’s theorem. So $f = \phi ^ { - 1 } \circ g$ is also constant.

Spring 2009, 1. Suppose that f is entire and that $\frac { f ( z ) } { 1 + | z | ^ { 1 / 2 } }$ is bounded as $z  \infty$ Prove that f is constant.

I want to say ‘So what does it mean?’ in my friend Peyman’s voice to the first statement. I guess it means that there exists $M , L > 0$ such that

$$
| z | \geq L \Rightarrow \left| { \frac { f ( z ) } { 1 + | z | ^ { 1 / 2 } } } \right| \leq M .
$$

Well, $\frac { f ( z ) } { 1 + | z | ^ { 1 / 2 } }$ is also bounded on $| z | \le L$ by compactness, so we may assume

$$
\left| \frac { f ( z ) } { 1 + | z | ^ { 1 / 2 } } \right| \le M .
$$

for all $z \in \mathbb { C }$ . Now we are in business. Fix $r > 0 . { \mathrm { ~ I f ~ } } | z | \leq r$ , we have

$$
| f ( z ) | \leq M ( 1 + | z | ^ { 1 / 2 } ) \leq M ( 1 + r ^ { 1 / 2 } ) .
$$

Thus applying Cauchy’s estimates to the closed disk $\overline { { { \cal D } ( 0 , r ) } }$ , we get

$$
| f ^ { ( n ) } ( 0 ) | \leq \frac { M ( 1 + r ^ { 1 / 2 } ) n ! } { r ^ { n } }
$$

for every $n \in \mathbb { N }$ . Sending $r  \infty$ above, we get $f ^ { ( n ) } ( 0 ) = 0$ for every $n \geq 1$ . Being entire, f has a global power series representation around 0, and therefore all the coefficients in this power series except the constant term is 0. Thus f is constant.

## 6. Residue Calculus

I won’t state the Residue theorem, because its statement is much more confusing than the usual applications and I am lazy.

Let me note the following useful lemma for calculating residues:

Lemma 5. Let g be analytic around $z _ { 0 }$ and $f ( z ) = { \frac { g ( z ) } { ( z - z _ { 0 } ) ^ { n } } }$ . Then

$$
\operatorname { R e s } ( f , z _ { 0 } ) = { \frac { g ^ { ( n - 1 ) } ( z _ { 0 } ) } { ( n - 1 ) ! } } .
$$

Proof. ${ \mathrm { R e s } } ( f , z _ { 0 } )$ is the coefficient of the $\frac { 1 } { z - z _ { 0 } }$ term in the Laurent series expansion of $f$ around $z _ { 0 } ,$ , so it is equal to the coefficient of the $( z - z _ { 0 } ) ^ { n - 1 }$ term in the power series expansion of $g$ around $z _ { 0 }$ 

Fall 2012, 3. Evaluate the following integral for any $\alpha > 0$

$$
\int _ { 0 } ^ { \infty } { \frac { \ln ( x ) } { x ^ { 2 } + \alpha ^ { 2 } } }
$$

Carefully justify your steps.

Pick $r , R$ such that $0 < r < \alpha < R$ . Consider the following curves:

$$
\begin{array} { c } { \varphi _ { R } : [ 0 , \pi ] \to \mathbb { C } } \\ { t \mapsto R e ^ { i t } } \end{array}
$$

$$
\lambda _ { r , R } : [ - R , - r ] \to \mathbb { C }
$$

$$
\psi _ { r } : [ 0 , \pi ] \to \mathbb { C } _ { \mathbf { \alpha } }
$$

$$
\begin{array} { r } { \mu _ { r , R } : [ r , R ] \to \mathbb { C } } \\ { t \mapsto t } \end{array}
$$

These look like a random selection of functions because I am trying to avoid drawing things. Drawing shows that these curves can be juxtaposed consecutively to yield a closed curve $\gamma _ { R , r }$ which has a semicircular shape with a small bump inside. Now let $V = \mathbb { C } - \{ z \in \mathbb { C } : \operatorname { R e } ( z ) = 0$ and Im $1 ( z ) \leq 0 \}$ . Note that every point which have nonzero winding number (which must then be 1) with respect to $\gamma _ { R , r }$ lies in V . Also, there is a continuous angle (or argument) function $\theta : V  ( - \pi / 2 , 3 \pi / 2 )$ which gives rise to the analytic branch of logarithm

$$
\begin{array} { r } { L : V  \mathbb { C } \quad } \\ { z \mapsto \ln | z | + i \theta ( z ) } \end{array}
$$

Let $f ( z ) = \frac { L ( z ) } { z ^ { 2 } + \alpha ^ { 2 } }$ . The only singularity of f which lies inside $\gamma _ { R , r }$ is iα and if we let $g ( z ) = \frac { L ( z ) } { z + i \alpha }$ , Lemma 5 yields

$$
\begin{array} { l } { \displaystyle \mathrm { R e s } ( f , i \alpha ) = g ( i \alpha ) = \frac { L ( i \alpha ) } { 2 i \alpha } } \\ { \displaystyle = \frac { \ln ( | i \alpha | ) + i \theta ( i \alpha ) } { 2 i \alpha } } \\ { \displaystyle = \frac { \ln ( \alpha ) + i \frac { \pi } { 2 } } { 2 i \alpha } . } \end{array}
$$

Therefore by the Residue theorem,

$$
\begin{array} { r l r } & { } & { \int _ { \gamma _ { R , r } } f ( z ) d z = 2 \pi i \operatorname { R e s } ( f , i \alpha ) } \\ & { } & { \int _ { \varphi _ { R } } f ( z ) d z + \int _ { \lambda _ { R , r } } f ( z ) d z + \int _ { \psi _ { r } } f ( z ) d z + \int _ { \mu _ { R , r } } f ( z ) d z = \displaystyle \frac { \pi \ln ( \alpha ) } { \alpha } + i \frac { \pi ^ { 2 } } { 2 \alpha } . } \end{array}\tag{?}
$$

Now we look at how the four integrals in (?) behave. When z is on $\varphi _ { R }$ , we have

$$
\begin{array} { r l } & { | L ( z ) | = \sqrt { [ \ln | z | ] ^ { 2 } + [ \theta ( z ) ] ^ { 2 } } } \\ & { \quad \quad = \sqrt { [ \ln R ] ^ { 2 } + [ \theta ( z ) ] ^ { 2 } } } \\ & { \quad \quad \le \sqrt { [ \ln R ] ^ { 2 } + \left( \displaystyle \frac { 3 \pi } { 2 } \right) ^ { 2 } } } \\ & { \quad \quad \le \ln R + \frac { 3 \pi } { 2 } } \end{array}
$$

and

$$
| z ^ { 2 } + \alpha ^ { 2 } | \geq \left| | z ^ { 2 } | - | \alpha ^ { 2 } | \right| = R ^ { 2 } - \alpha ^ { 2 } .
$$

Thus by the ML-inequality, we have

$$
| \int _ { \varphi _ { R } } f ( z ) d z | \leq { \frac { \ln R + { \frac { 3 \pi } { 2 } } } { R ^ { 2 } - \alpha ^ { 2 } } } \cdot ( { \mathrm { l e n g t h ~ o f ~ } } \varphi _ { R } ) = { \frac { \ln R + { \frac { 3 \pi } { 2 } } } { R ^ { 2 } - \alpha ^ { 2 } } } \pi R \longrightarrow 0 { \mathrm { ~ a s ~ } } R  \infty .
$$

Similarly, we have

$$
| \int _ { \psi _ { r } } f ( z ) d z | \leq { \frac { \ln r + { \frac { 3 \pi } { 2 } } } { \alpha ^ { 2 } - r ^ { 2 } } } \pi r \longrightarrow 0 { \mathrm { ~ a s ~ } } r  0
$$

since lim $1 _ { r \to 0 } r$ ln $r = 0$ . Taking these limits in (?), we get

$$
\begin{array} { r l } { \frac { \pi \ln ( \alpha ) } { \alpha } + i \frac { \pi ^ { 2 } } { 2 \alpha } = \underset { r \to \alpha \hdots } { \operatorname* { l i m } } ( \int _ { \lambda m _ { r } } f ( z ) d z + \int _ { \rho \pi _ { r } } f ( z ) d z ) } & { } \\ & { = \underset { r \to \theta \hdots } { \operatorname* { l i m } } \underset { k \to \infty } { \operatorname* { l i m } } ( \int _ { - \pi } ^ { r } f ( x ) d x + \int _ { r } ^ { \ln } f ( x ) d x ) } \\ & { = \underset { \rho \to \theta \hdots } { \operatorname* { l i m } } \underset { k \to \infty } { \operatorname* { l i m } } ( \int _ { - \kappa } ^ { - \infty } \frac { L ( x ) } { x ^ { 2 } + \alpha ^ { 2 } } d x + \int _ { r } ^ { \kappa } \frac { L ( x ) } { x ^ { 2 } + \alpha ^ { 2 } } d x ) } \\ & { = \underset { r \to \theta \hdots } { \operatorname* { l i m } } \underset { k \to \infty } { \operatorname* { l i m } } ( \int _ { - \pi } ^ { r } \frac { \ln | x | + i \pi } { x ^ { 2 } + \alpha ^ { 2 } } d x + \int _ { r } ^ { \pi } \frac { \ln | x | } { x ^ { 2 } + \alpha ^ { 2 } } d x ) } \\ & { = \underset { \rho \to \theta \hdots } { \operatorname* { l i m } } \underset { k \to \infty } { \operatorname* { l i m } } ( \int _ { - \pi } ^ { - \infty } \frac { \ln | x | } { x ^ { 2 } + \alpha ^ { 2 } } d x + \int _ { - \pi } ^ { - \infty } \frac { i \pi } { x ^ { 2 } + \alpha ^ { 2 } } d x + \int _ { r } ^ { R } \frac { \ln | x | } { x ^ { 2 } + \alpha ^ { 2 } } d x ) } \\ &  = \underset { r \to \theta \hdots } { \operatorname* { l i m } } ( i \int _ { - \pi } ^ { r } \frac { \pi } { x ^ { 2 } + \alpha ^ { 2 } } d x + 2 \int _ { r } ^ { - \infty } \end{array}
$$

Taking the real parts of both parts (note that $\operatorname { R e } ( z )$ is a continuous function so it commutes with limits), we get

$$
{ \frac { \pi \ln ( \alpha ) } { \alpha } } = \operatorname* { l i m } _ { r \to 0 } \operatorname* { l i m } _ { R \to \infty } \left( 2 \int _ { r } ^ { R } { \frac { \ln x } { x ^ { 2 } + \alpha ^ { 2 } } } d x \right) .
$$

Thus

$$
\int _ { 0 } ^ { \infty } { \frac { \ln x } { x ^ { 2 } + \alpha ^ { 2 } } } = { \frac { \pi \ln ( \alpha ) } { 2 \alpha } } .
$$

I don’t think I’ll put any other solutions of integration problems. They are $\mathrm { L O N G }$ , and today is the prelim day.

## 7. Miscellaneous

These are problems which don’t fit in one of the above categories.

Fall 2012, 2. Let f be a complex valued function in the unit disk D such that   
$g = f ^ { 2 }$ and $h = f ^ { 3 }$ are both analytic. Prove that $f$ is analytic.

Note that the zeros of $f , g , h$ in D are the same. Let’s denote this common zero set by Z. We may assume $f$ is not identically zero, so the analytic function $g$ is not identically zero; hence its zero set $Z$ is isolated. Therefore, as $g$ and h are analytic, every $a \in Z$ has a neighborhood such that

$$
\begin{array} { l } { { g ( z ) = ( z - a ) ^ { m } \tilde { g } ( z ) } } \\ { { h ( z ) = ( z - a ) ^ { n } \tilde { h } ( z ) } } \end{array}
$$

where m, n are positive integers and $\tilde { g } , \tilde { h }$ are analytic functions which don’t vanish around a. Observe that a is a zero of the analytic map $g ^ { 3 } = h ^ { 2 }$ of order $3 m = 2 n$ Since 2 and 3 are relatively prime, there exists a positive integer k such that $m = 2 k$ and $n = 3 k$ . The function

$$
{ \hat { f } } ( z ) = ( z - a ) ^ { k } { \frac { { \tilde { h } } ( z ) } { { \tilde { g } } ( z ) } }
$$
is well-defined and analytic around a. When $z \neq a ,$ , we have $\begin{array} { r } { { \hat { f } } ( z ) = { \frac { h ( z ) } { g ( z ) } } = f ( z ) } \end{array}$ . And ${ \hat { f } } ( a ) = 0 = f ( a )$ . Thus $f = { \hat { f } }$ is analytic at $a .$ Since $a \in Z$ was arbitrary, we conclude that $f$ is analytic on $Z$ . Finally as $1 / g$ is analytic on $\mathbb { D } { - } Z , f = h / g$ is analytic on $\mathbb { D } - Z$

$$
\mathbb { D } - \{ 0 \}
$$

$$
f ^ { \prime }
$$

$$
f
$$

$$
B - \{ 0 \}
$$

$$
B
$$

$$
f ^ { \prime } ( z ) = { \frac { c } { z } } + g ( z )
$$

where $c \neq 0$ and $g \in { \bf H } ( B )$ . Since $B$ is simply connected, there exists $G \in \mathbf { H } ( B )$ such that $G ^ { \prime } = g$ . Thus the function $\frac { 1 } { c } ( G - f ) \in \mathbf { H } ( B - \{ 0 \} )$ is an antiderivative of $1 / z$ This is impossible because there are closed curves in $B - \{ 0 \}$ on which the integral of $1 / z$ is nonzero.

Fall 2011, 2. Let h be a nowhere zero, entire holomorphic function. Prove that   
there exists an entire holomorphic function $g$ such that $e ^ { g } = h$   
Observe that $\frac { h ^ { \prime } } { h }$ is entire, therefore has an antiderivative $f$ (C is simply connected).   
Consider the entire function $c ( z ) = h ( z ) e ^ { - f ( z ) }$ . We have   
$c ^ { \prime } ( z ) = h ^ { \prime } ( z ) e ^ { - f ( z ) } - h ( z ) e ^ { - f ( z ) } f ^ { \prime } ( z ) = e ^ { - f ( z ) } \left( h ^ { \prime } ( z ) - h ( z ) f ^ { \prime } ( z ) \right) = 0 ,$   
therefore $c ( z )$ is constant, say $c ( z ) \equiv c .$ Note that $c \neq 0$ since $h$ is nowhere zero.   
Therefore $c = e ^ { a }$ for some $a \in \mathbb { C }$ . So if we let $g ( z ) = a + f ( z )$ , we have   
$h ( z ) = c e ^ { f ( z ) } = e ^ { a } e ^ { f ( z ) } = e ^ { a + f ( z ) } = e ^ { g ( z ) }$

$$
f ( z )
$$

$$
f ( z + 1 )
$$

$$
| f ( z ) | \leq { \dot { e } } ^ { | z | }
$$

$$
z \in \mathbb { C }
$$

$$
f ( z ) =
$$

$$
f ( z )
$$

$$
{ \bar { f ( z ) } } = g ( e ^ { 2 \pi i z } )
$$

$$
f
$$

$$
g .
$$

$$
\dot { E } ( z ) = \dot { e } ^ { 2 \pi i z }
$$

$$
z \in \mathbb { C } - \{ 0 \}
$$

$$
V _ { z }
$$

$$
\varphi _ { z } : V _ { z } \to \mathbb { C }
$$

$$
E \circ \varphi _ { z } = \operatorname { i d }
$$

$$
\varphi : V \to \mathbb { C }
$$

$$
\psi : W \to \mathbb { C }
$$

$$
E
$$

$$
z \in V \cap W
$$

$$
e ^ { 2 \pi i \varphi ( z ) } = E ( \varphi ( z ) ) = z = E ( \psi ( z ) ) = e ^ { 2 \pi i \psi ( z ) }
$$

$$
\varphi ( z ) = \psi ( z ) + \prime
$$

$$
n \in \mathbb { Z }
$$

$$
f
$$

$$
f \circ \varphi = f \circ \psi
$$

$$
g : \mathbb { C } - \{ 0 \}  \mathbb { C }
$$

$$
z \mapsto ( f \circ \varphi _ { z } ) ( z )
$$

is analytic. We have $g \circ E = f ,$ as desired. Now for every $z \in \mathbb { C } - \{ 0 \}$ , there exists $\omega \in \mathbb { C }$ with $0 < \operatorname { R e } ( \omega ) < 1$ such that $z = e ^ { 2 \pi i \omega }$ . We have

$$
| g ( z ) | = | f ( \omega ) | \leq e ^ { | \omega | } = e ^ { \sqrt { | \mathrm { R e } ( \omega ) | ^ { 2 } + [ \mathrm { I m } ( \omega ) ] ^ { 2 } } } < e ^ { \sqrt { 1 + [ \mathrm { I m } ( \omega ) ] ^ { 2 } } } \leq e ^ { 1 + | \mathrm { I m } ( \omega ) | } .\tag{?}
$$

Note that

$$
| z | = | e ^ { 2 \pi i \omega } | = e ^ { \mathrm { R e } ( 2 \pi i \omega ) } = e ^ { - 2 \pi \mathrm { I m } ( \omega ) }
$$

hence

$$
e ^ { - \mathrm { I m } ( w ) } = | z | ^ { \frac { 1 } { 2 \pi } } \mathrm { a n d } e ^ { \mathrm { I m } ( \omega ) } = | z | ^ { \frac { - 1 } { 2 \pi } } .
$$

Thus $| g ( z ) | \leq e$ · max $\left\{ \left| z \right| ^ { \frac { 1 } { 2 \pi } } , \left| z \right| ^ { \frac { - 1 } { 2 \pi } } \right\}$ by (?). So for $R > 1$ , since $g$ is entire, we can apply Cauchy’s estimates to the closed disk $\overline { { D ( 0 , R ) } }$ and get

$$
\vert g ^ { ( n ) } ( 0 ) \vert \leq { \frac { R ^ { { \frac { 1 } { 2 \pi } } n ! } } { R ^ { n } } } = { \frac { n ! } { R ^ { n - { \frac { 1 } { 2 \pi } } } } } \longrightarrow 0 { \mathrm { ~ a s ~ } } R  \infty
$$

for every $n ;$ thus $g ^ { ( n ) } ( 0 ) = 0$ for every $n \geq 1$ . This implies that $g$ is constant (because being entire, g has a global power series representation around 0). Thus $f$ is constant.