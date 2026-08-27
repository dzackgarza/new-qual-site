SOLUTIONS TO COMPLEX PRELIM PROBLEMS
C˙IHAN BAHRAN
In this document, I will collect my solutions to some (not all, probably not even half)
of the Complex Prelim problems that were asked in the past in UMN.
Some theorems get used a lot. I will copy some of them from David C. Ullrich’s
wonderful book Complex Made Simple .
1. Open mapping theorem
This is very useful in general. It’s easy to forget the connectedness assumption, so I
will state it precisely. H(V ) denotes the set of analytic maps from an open set V to C.
Open Mapping Theorem. LetV be open andf∈ H(V ). Also let W be an open and
connected set contained in V . Then f(W ) is either a singleton (that is, f is constant
on W ) or open in C.
Fall 2011, 7 and Fall 2010, 3. Prove that there is no one-to-one conformal map
of the punctured disk{z∈ C : 0<|z|< 1} onto the annulus{z∈ C : 1<|z|< 2}.
Let D denote the unit open disk andA the described annulus. Suppose, to the contrary,
that there exists f∈ H(D−{ 0}) which is injective and f(D−{ 0}) =A. Firstly, since
|f(z)|< 2 for all z∈ D−{ 0}, we have
lim
z→0
zf (z) = 0.
So 0 is a removable singularity of f. Thus∃g∈ H(D) such that g|D−{0} =f. As 0 is a
limit point of D−{ 0}, g(0) is a limit point of g(D−{ 0}) =A. Thus
g(D)⊆A ={z∈ C : 1≤|z|≤ 2}.
Moreover, since f is injective, g is not constant. Thus by the open mapping theorem,
we get
g(D)⊆ Int(A) =A.
Let ω = g(0) ∈ A. Since f(D−{ 0}) = A, there exists z ∈ D−{ 0} such that
g(z) =f(z) =ω. Since z⁄= 0, there exist disjoint open disksV,W ⊆ D such thatz∈V
and 0 ∈ W . Again by the open mapping theorem, g(V ) and g(W ) are open subsets
of A. Thus g(V )∩g(W ) is open. However, since f is a bijection and V ,W−{ 0} are
1

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 2
contained in D−{ 0}, we have
g(V )∩g(W ) =g(V )∩
Å
g({0})∪g
Ä
W−{ 0}
äã
=f(V )∩
Å
{ω}∪ f
Ä
W−{ 0}
äã
=
Å
f(V )∩{ω}
ã
∪
Å
f(V )∩f
Ä
W−{ 0}
äã
=f(V )∩{ω}
={ω}.
This is a contradiction.
Spring 2011, 2. Let h be a holomorphic function on a connected open set V .
Prove that if h(z)2 =h(z) for all z∈V then h is constant on V . Find all possible
values for such h.
First of all, V is nonempty1. Let f =h3∈ H(V ). So for all z∈V ,f(z) =h(z)2h(z) =
h(z)h(z) =|h(z)|2∈ R. That is, f(V )⊆ R. Suppose f is not constant. Then the open
mapping theorem yields f(V )⊆ Int(R) =∅ (we are considering R as a subspace of C
here), a contradiction. Thus for all z∈V ,h(z)3 =f(z) =a for some a∈ C. Therefore
if we let ζ =e
2πi
3 , we have
h(V )⊆{|a|
1
3,ζ|a|
1
3,ζ 2|a|
1
3},
so h(V ) is ﬁnite. Nonempty open sets in C are inﬁnite, thus h(V ) is not open. Again
by the open mapping theorem we deduce that h is constant. The rest is the kind of
stuﬀ Calc 1 students fail to do correctly quite often: basic algebra. For some x,y∈ R,
h(z) =x +iy for all z∈V . So
(x +iy)2 =x +iy
x2−y2 +i(2xy) =x−iy.
Thusx2−y2 =x and 2xy =−y. The second equation gives y = 0 orx =− 1
2. Going to
the ﬁrst equation, the ﬁrst case yields x2 =x and the second case yields 1
4−y2 =− 1
2.
So the solutions are 0,1,− 1
2 +i
√
3
2 ,− 1
2−i
√
3
2 .
2. Linear fractional transformations
I think the most useful linear fractional transformations for the prelims are the ones
that map a half plane to the unit disk. And, thanks to Ullrich’s book, I know that
there is a way to do this which is really cool and impossible to forget. Let U be the
upper half plane and D be the open unit disk. The neat geometric observation is that
1Why? Because the correct deﬁnition of connectedness excludes the empty space. Otherwise we
wouldn’t get a unique decomposition of every topological space into its connected components. The
same reason as why we don’t count 1 as a prime number: to have unique factorization.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 3
z∈ U if and only if z is closer to i than it is to−i. This yields
z∈ U⇔|z−i|<|z +i|
⇔
⏐⏐⏐⏐⏐
z−i
z +i
⏐⏐⏐⏐⏐< 1
⇔ z−i
z +i∈ D.
Thus the LFT z−i
z +i maps U onto D. In exactly the same way, z− 1
z + 1 maps the right
half plane onto D. Let’s roll:
Fall 2012, 1. Show that a M¨ obius transformation maps a straight line or circle
onto a straight line or circle.
This takes work! I’d like to know if there is a shorter argument. We start with a lemma:
Lemma 1. LetT be an LFT. Then T−1(R) is a circle in C∞ (that is, a line or a circle
in C).
Proof. Say
T (z) = az +b
cz +d
where a,b,c,d ∈ C such that ad−bc⁄= 0. Note that
ω∈T−1(R)⇔T (w)∈ R
⇔ aω +b
cω +d =T (ω) =T (ω) = aω +b
cw +d
⇔ac|ω|2 +adω +bcω +bd =ac|ω|2 +adω +bcω +bd
⇔ (ac−ac)|ω|2 + (ad−bc)ω + (bc−ad)ω +bd−bd = 0 ( ⋆)
We have two cases:
• ac−ac = 0. Then (⋆) becomes
(ad−bc)ω + (bc−ad)ω +bd−bd = 0
(ad−bc)ω + (bc−ad)ω +bd−bd = 0.
So if we write A =ad−bc, and B =bd, we get
Aω−Aω =B−B
2i Im(Aω) = 2i Im(B)
Im(Aω) = Im(B). (†)
We observe that A⁄= 0. Suppose not. Then we have ad =bc and so
acd =acd =bcc
c(ad−bc) = 0.
Since ad−bc ⁄= 0, we get c = 0. But then ad = 0 so ad = 0 and hence
ad−bc = 0, a contradiction. Since A⁄= 0, (†) describes a line.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 4
• ac−ac⁄= 0. Then we can write ( ⋆) as
|ω|2 + ad−bc
ac−acω + bc−ad
ac−acω + bd−bd
ac−ac = 0.
WriteA = ad−bc
ac−ac, soA = ad−bc
ac−ac = bc−ad
ac−ac and writeB = bd−bd
ac−ac. Thus we
get
|ω|2 +Aω +Aω +B = 0
|ω|2 +Aω +Aω +AA =AA−B
|ω +A|2 =AA−B (‡)
Note that
AA−B = ad−bc
ac−ac· bc−ad
ac−ac− bd−bd
ac−ac
= (ad−bc)(bc−ad)− (ac−ac)(bd−bd)
(ac−ac)2
= abcd +abcd−aadd−bbcc
[2i· Im(ac)]2
= ad(bc−ad)−bc(ad−bc)
−4 [Im(ac)]2
= (ad−bc)(ad−bc)
4 [Im(ac)]2
= |ad−bc|2
4 [Im(ac)]2.
So if we let r =|ad−bc|
2 Im(ac) > 0 (ad−bc⁄= 0), (‡) becomes
|ω +A|2 =r2,
which describes a circle.
□
Deﬁnition 2. Letz1,z 2,z 3 be three distinct points inC∞. We deﬁne an LFT (,z 1,z 2,z 3)
by
( ,z 1,z 2,z 3)(z) = (z,z 1,z 2,z 3) =



(z−z1)(z2−z3)
(z−z3)(z2−z1) if none of z1, z2, z3 are∞
z2−z3
z−z3
if z1 =∞
z−z1
z−z3
if z2 =∞
z−z1
z2−z1
if z3 =∞
Note that ( ,z 1,z 2,z 3) sends z1,z 2,z 3 to 0, 1,∞ , respectively.
Theorem 3. LFT’s sends circles in C∞ to circles in C∞.
Proof. Let T be an LFT and C be a circle in C∞. Pick three distinct points ω1,ω 2,ω 3
onC. Let zi =T (ωi) for i = 1, 2, 3 and let S = ( ,z 1,z 2,z 3). Note that by construction
z1,z 2,z 3∈S−1(R), which is a circle in C∞ by Lemma 2. But the three distinct points

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 5
z1,z 2,z 3 determine a unique circle C′ in C∞; thus S−1(R) = C′. In a similar fashion,
we get (S◦T )−1(R) =C since ω1,ω 2,ω 3 uniquely determine C. Thus we have
T (C) =T ((S◦T−1)(R)) = (T◦ (S◦T )−1)(R) =S−1(R) =C′.
□
Fall 2012, 7. Suppose f(z) is analytic on the punctured unit disk D−{ 0}, and
the real part of f(z) is positive. Prove that f has a removable singularity at 0.
Let H ={z∈ C : Re(z) > 0}. We may write f : D−{ 0}→ H. Also by the above
discussion, we have an invertible analytic map
φ : H→ D
z↦→ z− 1
z + 1
with the inverse φ−1(z) = z + 1
−z + 1 = z + 1
1−z . Note that g :=φ◦f is analytic and maps
D−{ 0} to D. In particular, g is bounded. Thus
lim
z→0
zg(z) = 0
and hence 0 is a removable singularity of g. So there exists an analytic function
h : D→ C
such that h|D−{0} = g. Since h(D−{ 0})⊆ D, by continuity we get h(D)⊆ D. There
are two cases by the open mapping theorem:
(1) h is constant. Then pick a∈ D−{ 0}, so h(0) =h(a) =g(a)∈ D.
(2) h(D)⊆ Int(D) = D.
In any case, we may write h : D→ D. So forming the composition φ−1◦h is legal, and
(φ−1◦h)|D−{0} =φ−1◦g =f. We eﬀectively removed the singularity of f at 0.
Fall 2009, 5. Letf(z) be an analytic function on C which takes value in the upper
half plane U. Show that f is constant.
Same deal. φ(z) = z−i
z +i maps U conformally to D, thus φ◦f is an entire function
which takes values in D. Thus by Liouville’s theorem, φ◦f is constant. φ is invertible,
so f is also constant.
Spring 2009, 3. Find an explicit conformal equivalence which maps the open set
bounded by
⏐⏐⏐z− 1
2i
⏐⏐⏐ = 1
2 and|z−i| = 1 onto the upper half plane U.
I am too lazy to learn drawing circles in LaTeX now, so the reader should draw them.
Let D1 ={z∈ C :
⏐⏐⏐z− 1
2i
⏐⏐⏐ < 1
2} and D2 ={z∈ C :|z−i| < 1}. We want to map
the open set V := D2−D1 conformally onto U. Consider the circles C1 = ∂D1 and
C2 =∂D2. Note that C1∩C2 ={0}. Let’s pick two other points on C2: 2i and 1 +i.
We can send C2 to the real line in various ways, but it’s better to pick an LFT so that

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 6
0↦→∞ . This will ensure C1 maps to a line as well. The assignments
1 +i↦→ 0
2i↦→ 1
0↦→∞
can be realized by the LFT
φ(z) = (z− (1 +i))(2i− 0)
(2i− (1 +i))(z− 0)
= (z− 1−i)2i
(i− 1)z
= 2iz + 2− 2i
(i− 1)z .
So φ maps C2 to the real line R. And since
φ(i) =−2 + 2− 2i
(i− 1)i = −2i
(i− 1)i
= −2
i− 1 = 2
1−i = 2(1 +i)
2 = 1 +i∈ U,
φ mapsD2 onto the upper half plane U. Let’s see what φ does to C1. We already know
φ(0) =∞ and φ(i) = 1 +i. Let’s choose another point on C1: i+1
2 . We have
φ
Ç1 +i
2
å
= 2i
Ä 1+i
2
ä
+ 2− 2i
(i− 1)
Ä 1+i
2
ä
= i− 1 + 2− 2i
−1 =−1 +i
So we deduce that φ(C1) ={z∈ C : Im(z) = 1}. And since
φ
Çi
2
å
= 2i
Äi
2
ä
+ 2− 2i
(i− 1)
Äi
2
ä = 1− 2i
−1−i
2
= 2− 4i
−1−i =−2 + 4i
1 +i = (−2 + 4i)(1−i)
2
= 2 + 6i
2 = 1 + 3i,
we deduce that φ(D1) is the half plane {z∈ C : Im(z)> 1}. Thus
φ(V ) =φ(D2−D1) ={z∈ C : Re(z)> 0 and Im(z)< 1}.
Consider the translation τ(z) =z−i. We have
(τ◦φ)(V ) ={z∈ C : Re(z)> 0 and Im(z)< 0}
={a−ib :a,b> 0}.
In other words, if we let ψ = τ◦φ, ψ(V ) is the fourth quadrant. Hence ( i·ψ)(V ) is
the ﬁrst quadrant. Since z↦→z2 sends the ﬁrst quadrant onto the upper half plane U,
(i·ψ)2(V ) =−ψ2(V ) = U. Being a composition of conformal maps, −ψ2 is conformal.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 7
Spring 2008, 6. Find an explicit conformal equivalence from the region R1 to the
region R2, where
R1 ={z∈ C : Re(z)> 0, Im(z)> 0,|z|< 1}
and
R2 ={z∈ C : Re(z)> 0, Im(z)> 0}.
Note thatR1 is contained in the unit disk D andR2 is contained in the upper half plane
U. We noted above that
φ(z) = z−i
z +i
maps U (conformally) onto D. Note that for any a∈ R,
φ(ia) = ia−i
ia +i = a− 1
a + 1
lies on the real axis R. Thus φ maps the imaginary axisiR to R. Therefore φ(U−iR) =
D−R and sinceR2 is a connected component of U−iR,φ(R2) is a connected component
of D− R. Let’s pick a point, say 1 +i∈R2, to see which component φ(R2) is. We have
φ(1 +i) = 1
1 + 2i = 1− 2i
5 .
Therefore φ(R2) ={z∈ D : Re(z) > 0} =: V . So we will be done if we can map R1
ontoV . And this is easy. Note that applying σ(z) =z2 yields
σ(R1) ={z∈ D : Im(z)> 0}.
And ﬁnally, rotation by π/4 (a.k.a multiplying by i) maps this to V . Thus z ↦→
φ−1(iσ(z)) maps R1 to R2.
3. Rouche’s theorem
Rouche’s Theorem. Suppose that γ is a smooth closed curve in the open set V such
that Ind(γ,z ) is either 0 or 1 for all z∈ C−γ∗ and equals 0 for all z∈ C−V , and let
Ω ={z∈V : Ind(γ,z ) = 1}. If f,g ∈ H(V ) and
|f(z)−g(z)|<|f(z)| +|g(z)|
for all z∈γ∗ then f and g have the same number of zeroes in Ω.
Note that the number of zeros is counted with multiplicity. There are a lot of notations
in the statement above. We don’t need to know what most are for the usual applications
of Rouche’s theorem, though the reader might ﬁgure them out. I’ll just note (again)
that H(V ) denotes the set of (complex valued) holomorphic functions deﬁned on the
open set V . The following version is a corollary of the general theorem above and we
will only use this one:
Rouche’s Theorem. LetV be an open set and D be a closed disk contained in V . If
f,g ∈ H(V ) satisfy
|f(z)−g(z)|<|f(z)| +|g(z)|
on the boundary of D, then f and g have the same number of zeroes in the interior of
D.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 8
The more classical Rouche’s theorem states the result for the stronger condition
|f(z)−g(z)|<|f(z)|
which usually suﬃces.
The applications of Rouche’s theorem come up a lot in prelims. Sometimes even the
statement of the theorem gets asked. Here are some examples:
Spring 2012, 2b. Use Rouche’s theorem to ﬁnd the number of zeros of the
polynomial z4 + 5z + 3 in the annulus 1 <|z|< 2.
It is clear what to do here. Let f(z) be the given polynomial. For |z| = 2, we have
|f(z)−z4| =|5z + 3|≤| 5z| + 3 = 13< 16 =|z4|.
Therefore by Rouche’s theorem f(z) and z4 have the same number of zeros inside the
disk|z| < 2. z4 has four zeros (which are all 0, pun intended) in |z| < 2, so f has 4
zeros in|z|< 2. And for |z| = 1,
|f(z)− (5z + 3)| =|z4| = 1< 2 =||5z|−|− 3||≤| 5z− (−3)| =|5z + 3|.
Therefore again by Rouche’s theorem f(z) and 5z + 3 have the same number of zeros
in|z|< 1. The only zero of 5z + 3 is−3/5 which is in the unit disk; thus f has a single
zero in|z|< 1.
Psychologically, the problem seems over here but there is a subtle point: We showed
that f has four zeros in |z| < 2 and a single zero in |z| < 1. Hence, f has three zeros
in 1≤|z|< 2. To make the ﬁrst inequality strict, we also need to show that f has no
zeros on|z| = 1. Indeed, in this case
|f(z)| =|5z + 3− (−z4)|≥|| 5z + 3|−|− z4|| =||5z + 3|− 1|
And just above we showed above that |5z + 3| > 2 on |z| = 1. Hence |f(z)| > 1 on
|z| = 1.
It might be worth noting that the functions we used to apply Rouche’s theorem to were
all entire, i.e. in H(C), so we were able to use any disk we want.
Fall 2011, 1. Show that z5 + 3z3 + 7 has all its zeros in the disk |z|< 2.
Let f(z) be the given polynomial. f has ﬁve zeros, so z5, which has all of its ﬁve zeros
in|z|< 2, is the best candidate to apply Rouche’s theorem. Note that both f(z) and
z5 are entire functions and for |z| = 2, we have
|f(z)−z5| =|3z3 + 7|≤| 3z3| +|7| = 31< 32 =|z5|
and we are done.
Spring 2011, 1. Prove that for any a∈ C and n≥ 2, the polynomial azn +z + 1
has at least one root in the disk |z|≤ 2.
Let f(z) be the given polynomial, it is entire. This question is more challenging than
the previous two, because a heavily inﬂuences the growth of f. The trick is to write
azn +z + 1 =f(z) =a(z−ω1)··· (z−ωn)

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 9
whereωi’s are the roots off. This is possible since C is algebraically closed. Comparing
the constant terms, we get
1 =a(−ω1)··· (−ωn),
thus
|ω1|···| ωn| = 1
|a|.
Therefore if 1
|a|≤ 2n, at least one of ωi’s should satisfy |ωi|≤ 2. So this handles the
case|a|≥ 1
2n . For |a| < 1
2n , we compare f(z) and z + 1 in Rouche’s theorem on the
disk|z|< 2. When|z| = 2, we have
|f(z)− (z + 1)| =|azn|< 1 =||z|−|− 1||≤| z− (−1)| =|z + 1|.
Since the only zero −1 of z + 1 is in the disk |z|< 2, f also has a single zero there in
this case.
Spring 2011, 8b. Use Rouche’s theorem to prove the fundamental theorem of
algebra.
We show that every nonconstant monic polynomial of degree n has n roots. Let f be
such a polynomial written as
f(z) =zn +an−1zn−1 +an−2zn−2 +··· +a1z +a0
Choose R such that
R> |an−1| +|an−2| +...|a1| +|a0| and R> 1.
For|z| =R we have
|f(z)−zn| =|an−1zn−1 +an−2zn−2...a 1z +a0|
≤|an−1zn−1| +|an−2zn−2|...|a1z| +|a0|
=|an−1|Rn−1 +|an−2|Rn−2...|a1|R +|a0|
≤|an−1|Rn−1 +|an−2|Rn−1...|a1|Rn−1 +|a0|Rn−1
=Rn−1 (|an−1| +|an−2| +··· +|a1| +|a0|)
<R n =|zn|
Alsof(z) and zn are entire functions. Therefore by Rouche’s theorem, in |z|<R ,f(z)
and zn have the same number of roots, which is n.
Fall 2009, 1. How many roots (counted with multiplicity) does the function
g(z) = 6z3 +ez + 1
have in the unit disk|z|< 1?
This time we don’t have a polynomial. g is of course entire though and for |z| = 1,
|g(z)− 6z3| =|ez + 1|≤| ez| + 1 =eRe(z) + 1≤e|z| + 1 =e + 1< 6 =|6z3|.
Therefore by Rouche’s theorem,f(z) and 6z3 have the same number of zeros in|z|< 1,
which is three.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 10
Spring 2009, 4. How many zeros does the function f(z) =z6 + 4z2ez+1− 3 have
in the unit disk D(0, 1)?
Let’s try to apply Rouche for the entire functions f(z) and 4z2ez+1. For|z| = 1,
|f(z)− 4z2ez+1| =|z6− 3|≤| z6| + 3 = 4
On the other hand, again for |z| = 1,
|4z2ez+1| = 4|ez+1| = 4e|ez| = 4e·eRe(z)≥ 4e·e−1 = 4
because on the unit circle, Re(z)≥− 1. Thus, we get that
|f(z)− 4z2ez+1|≤| 4z2ez+1|
on|z| = 1. The problem is we didn’t get the strict inequality that Rouche’s theorem
requires. However, looking at how we arrived at this inequality, the two terms being
equal can only occur if |z6− 3| = 4 and Re( z) =−1 for some z where|z| = 1. The
latter yields z =−1, but|(−1)6− 3| = 2⁄= 4. So equality can never occur. Thus, f(z)
and 4z2ez+1 have the same number of zeros in |z|< 1, which is 2 (0 is the only root of
the latter function and it has order 2).
Fall 2008, 1b. Determine the number of zeros of P (z) = z7 +z3 + 1
16 that lie in
the closed disk|z|≤ 1/2.
P (z) and z3 are entire functions and on |z| = 1/2,
|P (z)−z3| =
⏐⏐⏐⏐z7 + 1
16
⏐⏐⏐⏐≤|z7| + 1
16 = 1
27 + 1
24 = 9
27 < 16
27 = 1
23 =|z3|.
Therefore, in|z| < 1/2, P (z) and z3 have the same number of zeros, which is 3. For
|z| = 1/2, we have
|P (z)|≥
⏐⏐⏐⏐|z7|−
⏐⏐⏐⏐z3 + 1
16
⏐⏐⏐⏐
⏐⏐⏐⏐ =
⏐⏐⏐⏐
1
27−
⏐⏐⏐⏐z3 + 1
16
⏐⏐⏐⏐
⏐⏐⏐⏐ .
Since
⏐⏐⏐z3 + 1
16
⏐⏐⏐≥
⏐⏐⏐|z3|− 1
16
⏐⏐⏐ =
⏐⏐⏐ 1
23− 1
16
⏐⏐⏐ = 1
16, we get
|P (z)|≥
⏐⏐⏐⏐⏐
1
27−
Ç
z3 + 1
16
å⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐z3 + 1
16− 1
27
⏐⏐⏐⏐ =
⏐⏐⏐⏐z3 + 7
27
⏐⏐⏐⏐≥
⏐⏐⏐⏐|z3|− 7
27
⏐⏐⏐⏐ =
⏐⏐⏐⏐
1
23− 7
27
⏐⏐⏐⏐ = 9
27.
Hence P (z) has no zeros on |z| = 1/2. The answer is 3.
Spring 2008, 4. If λ >1, show that the equation z +e−z = λ has exactly one
solution with positive real part.
Let, by our experience from IVT questions in calculus,f(z) =z +e−z−λ. Consider the
circle centered at the origin with radius R, cut it into two with the y-axis and let the
right semicircle be γR. It suﬃces to show that, for every R>λ + 1,f has a single zero
inside γR (because the interiors of such semicircles cover the entire right half plane).
Here f(z) and z−λ are entire functions, and when z is on γR, we have
|f(z)− (z−λ)| =|e−z| =eRe(−z) =e− Re(z)≤ 1<|R−λ| =||z|−| λ||≤| z−λ|.
Therefore by Rouche’s theorem, f(z) and z−λ have the same number of zeros inside
γR. The only root λ of z−λ lies inside γR (as R>λ and λ> 0), therefore f also has

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 11
a single root inside γR. It seems that λ >0 is enough for this question. Maybe I did
something wrong.
Fall 2007, 7. Determine the number of zeros of ez2
− 4z2 in the open unit disk.
Let f(z) = ez2
− 4z2 and g(z) = −4z2. f(z) and g(z) are entire functions, and on
|z| = 1, we have
|f(z)−g(z)| =|ez2
| =eRe(z2)≤e|z2| =e< 4 =|g(z)|.
Therefore, by Rouche’s theorem f and g have the same number of zeros in |z| < 1,
which is 2.
4. Schwarz’s lemma
Let D denote the open unit disk.
Scwharz’s Lemma. Suppose that f : D→ D is holomorphic and f(0) = 0 . Then
|f(z)|≤| z| for all z∈ D and|f′(0)|≤ 1. Furthermore, if|f′(0)| = 1 or|f(z)| =|z| for
some nonzero z∈ D then f is a rotation: f(z) =βz for some constant β with|β| = 1.
Fall 2012, 6. Let f(z) be an analytic function in the upper half plane
{z∈ C : Im(z)> 0}.
Suppose that|f(z)|< 1 for all z in the domain of f, andf(i) = 0. Find the largest
possible value of|f(2i)|.
Let H be the upper half plane. So we can consider f as a function from H to D. The
linear-fractional transformation
φ(z) = z−i
z +i
maps H conformally onto D (this was observed in a previous section). So its inverse
φ−1(z) = iz +i
−z + 1 = z + 1
iz−i
maps D ontoH, thus f◦φ−1 is a holomorphic function that maps D to D. Moreover,
(f◦φ−1)(0) =f(i) = 0.
Hence, by Schwarz’s lemma we have|(f◦φ)(z)|≤| z| and in particular we have
|f(2i)| =|(f◦φ−1◦φ)(2i)| =|(f◦φ−1)(φ(2i))| =
⏐⏐⏐⏐⏐(f◦φ−1)
Ç1
3
å⏐⏐⏐⏐⏐≤
⏐⏐⏐⏐
1
3
⏐⏐⏐⏐ = 1
3.
Also, again by Schwarz’s lemma|f(2i)| = 1/3 only if (f◦φ−1)(z) =βz for some|β| = 1.
So in this case,
f(z) = (f◦φ−1◦φ)(z) =β·φ(z).
Indeed, if f(z) =β·φ(z) for some|β| = 1, f mapsH to D,f(i) = 0 and|f(2i)| = 1/3.
So 1/3 actually is the largest possible value for |f(2i)|.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 12
Fall 2012, 8c. Let f be a holomorphic function in the unit disk D and suppose
that f(0) = 0 and|f(z)|≤ 1. Prove that for any integer m≥ 1, f(z)− 2mzm has
exactly m zeros (counting multiplicity) in the disk |z|< 1/2.
Note: The (a) and (b) parts of this question ask the statements of Rouche’s theorem
and Schwarz’s lemma, respectively. So the message we get is ‘you will need both in (c)’.
Let g(z) = f(z)− 2mzm. If f is constant, since f(0) = 0, f must be identically 0 and
so 0 is the only zero of g(z) =−2mzm and it has order m. If f is not constant, it is
an open map by the open mapping theorem. We are given that f(D)⊆ D, so actually
f(D)⊆ Int(D) = D. Thus we can use Schwarz’s lemma to conclude that |f(z)|≤| z|.
This inequality paves the way for Rouche’s theorem. Indeed, g(z) and −2mzm are
analytic in a neighborhood of the closed disk |z|≤ 1/2 and on the boundary|z| = 1/2,
we have
|g(z)− (−2mzm)| =|f(z)|≤| z| = 1
2 < 1 =|− 2mzm|.
Thusg(z) and−2mzm have the same number of roots inside |z|< 1/2, which is m.
Fall 2011, 4. Let f be a holomorphic function in the right half-plane {z∈ C :
Re(z) > 0}. Suppose that |f(z)| < 1 for all z in the domain of f, and f(1) = 0.
Find the largest value of|f(2)|.
Let P denote the right half plane. We can consider f as a function from P to the unit
disk D. Similar to the Fall 2012 question, we ﬁrst map P to D. Since z∈P if and only
if z is closer to 1 than it is to −1, if and only if |z− 1|<|z + 1|, the linear fractional
transformation
φ(z) = z− 1
z + 1
maps P (conformally) onto D. So its inverse
φ−1(z) = z + 1
−z + 1 = z + 1
1−z
maps D ontoP . Now, the analytic function f◦φ−1 : D→ D satisﬁes
(f◦φ−1)(0) =f(1) = 0.
Hence, by Schwarz’s lemma,|(f◦φ−1)(z)|≤| z|. In particular,
|f(2)| =|(f◦φ−1◦φ)(2)| =|(f◦φ−1)(φ(2))|≤| φ(2)| = 1
3.
To see that this bound is sharp when f varies, note that again by Schwarz’s lemma, if
we have equality above then (f◦φ−1)(z) =βz for some|β| = 1. Then
f(z) = (f◦φ−1◦φ)(z) = (f◦φ−1)(φ(z)) =β·φ(z).
And indeed if we deﬁne f as above for any |β| = 1, f maps P to D, and |f(2)| =
|φ(2)| = 1
3. So 1
3 is really the largest possible value for |f(2)|.
Spring 2011, 4. Let f be a holomorphic function in the unit disk D and suppose
thatf(0) =f′(0) = 0. Prove that|f′′(0)|≤ 2 and describe all suchf with|f′′(0)| =
2.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 13
It should be stated in this question that f maps D to itself, otherwise the statement is
false (consider f(z) = 2z2).
Note that, ifDr is the disk centered at 0 with radiusr <1, by Cauchy’s integral formula
(integrating along the boundary of Dr) f has a power series representation inside Dr.
Sending r→ 1 we actually get a power series representation for f valid inside all of D.
Since f(0) = 0, the constant term of the power series is 0 and hence
f(z) =zg(z)
for some analytic function g : D→ C. By Schwarz’s lemma |f(z)|≤| z|, so we get
|g(z)|≤ 1 (for every z∈ D), that is, g(D)⊆ D. By the open mapping theorem, there
are two cases:
• g is constant. Then f′′(z) = 0 for all z, so f′′(0) = 0.
• g is an open map. Then g(D)⊆ Int(D) = D. Since f′(0) = 0, the degree of the
z term in the power series representation of f is 0; thus g(0) = 0. So Schwarz’s
lemma applies to g and we get|g′(0)|≤ 1. Considering the coeﬃcient of the z2
term in the power series of f, we get f′′(0)
2 =g′(0). Thus|f′′(0)|≤ 2. And
|f′′(0)| = 2⇔|g′(0)| = 1
⇔g(z) =βz for some|β| = 1 (Schwarz)
⇔f(z) =βz 2 for some|β| = 1.
Spring 2010, 8. Let D be the unit disk and let f(z) be an analytic function which
maps D to itself. Suppose f has a ﬁxed pointc∈ D, that is,f(c) =c. Furthermore,
assume that|f′(c)|< 1. Prove that for any point z0∈ D, the sequence zn deﬁned
by iteration, zn =f(zn−1) converges to c. (Hint: ﬁrst consider the case c = 0).
The following proposition is helpful:
Proposition 4. Letf : D→ D be analytic such that f(0) = 0 and let 0<r < 1. If f is
not a rotation, then there exists 0<δ < 1 such that for |z|<r , we have |f(z)|≤ δ|z|.
Proof. We may assume that f is not identically zero, so f is not constant (using the
open mapping theorem and f(0) = 0). Let Dr ={z∈ D :|z|<r}. On the compact set
Dr, the function |f(z)| achieves a maximum, say M > 0 (a nonzero analytic function
on D cannot vanish on a disk, however small). By both parts of Schwarz’s lemma, we
get that M < r. Also note that for z∈ Dr,|f(z)| < M by the maximum modulus
theorem. Therefore the function g : D→ D given by
g(ω) = f(rω)
M
is well-deﬁned. Clearly g is analytic and g(0) = 0. By Schwarz’s lemma applied to g,
we get|g(ω)|≤| ω| for every ω∈ D. Now for z∈Dr, we have z/r∈ D and hence
⏐⏐⏐⏐
z
r
⏐⏐⏐⏐≥
⏐⏐⏐⏐g
Åz
r
ã⏐⏐⏐⏐ =|f(z)|
M .
Thus we can pick δ = M
r . □
Let’s go back to the question and deal with the case c = 0 as suggested. Since|f′(0)|<
1, f is not a rotation by Schwarz. Pick r such that|z0| < r <1. By Proposition 4,

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 14
there exists 0 <δ < 1 such that for|z|<r ,|f(z)|≤ δ|z|.
We claim that |zn| < r and|zn|≤ δn for every n. Employ induction on n; the basis
case is trivial since z0∈ D. Assuming|zn−1|<r and|zn−1|≤ δn−1, we get
|zn| =|f(zn−1)|<|zn−1|<r
and again by Proposition 4,
|zn| =|f(zn−1)|≤ δ|zn−1|≤ δ·δn−1 =δn.
Thus limn→∞zn = 0 since 0 <δ < 1.
Forc⁄= 0, consider the linear fractional transformation
φ(z) = c−z
1−cz = z−c
cz− 1.
We claim that φ maps D to D. Firstly, if|z| = 1, we have
|φ(z)|2 = (z−c)(z−c)
(cz− 1)(cz− 1)
=|z|2−cz−cz +|c2|
|cz|2−cz−cz + 1
= 1.
So φ maps the unit circle to itself. And as φ(0) =c∈ D, φ maps D to itself. Moreover
since ñ
1 −c
c −1
ô ñ
1 −c
c −1
ô
=
ñ
1−|c|2 0
0 1 −|c|2
ô
and|c|< 1, φ◦φ = idD. Let ˜f =φ◦f◦φ : D→ D. Now ˜f(0) = φ(f(c)) = φ(c) = 0.
And by the chain rule,
˜f′(0) = (φ◦f)′(φ(0))·φ′(0)
= (φ◦f)′(c)·φ′(0)
=φ′(f(c))·f′(c)·φ′(0)
=φ′(c)·f′(c)·φ′(0)
=f′(c)·φ′(φ(0))·φ′(0)
=f′(c)(φ◦φ)′(0)
=f′(c).
Finally, letωn =φ(zn) for each n. Then for n≥ 1, we have
ωn =φ(zn) =φ(f(zn−1)) =φ(f(φ(ωn−1))) = ˜f(ωn−1)
therefore ωn→ 0 from the ﬁrst part. Therefore by continuity, zn =φ(ωn)→φ(0) =c.
Fall 2009, 8. Letf : D→ D be analytic. Suppose there are points p,q∈ D,p⁄=q
such that f(p) = p and f(q) = q, i.e., f has two ﬁxed points. Show that f(z) = z
for all z∈ D. Hint: ﬁrst consider the case where one of the ﬁxed points is the
origin, p = 0.
The previous question can be used as a sledgehammer here, but it is probably unnec-
essarily strong. We can deal with this by Schwarz only. As suggested, let’s consider
the case p = 0. Since |f(q)| =|q| and q⁄= 0, f(z) = βz for some|β| = 1 by Schwarz’s

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 15
lemma. And β has to be 1 since f(q) =q.
For the general case, similar to the previous question, let
φ(z) = p−z
1−pz.
Then the analytic function g =φ◦f◦φ : D→ D satisﬁes
g(0) =φ(f(φ(0))) =φ(f(p)) =φ(p) = 0
and
g(φ(q)) =φ(f(q)) =φ(q)
since φ =φ−1. As p⁄=q, we have φ(q)⁄= 0 and hence by the ﬁrst case g = idD. Thus
f = idD.
5. Cauchy’s Estimates
These are the only ‘named’ estimates I know. This probably speaks more about my
ignorance in analysis than the lack of such estimates. Anyway, here they are:
Cauchy’s Estimates. Suppose that f is holomorphic in a neighborhood of the closed
disk D(z0,r ) and|f|≤ M in D(z0,r ). Then
|f (n)(z0)|≤ Mn!
rn
for every n∈ N.
Liouville’s theorem, that is, the fact that entire and bounded functions are constant is
an easy corollary. Examples:
Fall 2012, 5 and Fall 2010, 6. Suppose that g : C → C is a holomorphic
function, k and n are integers, and (2 +|zk|)−1g(n)(z) is bounded on C.
• Prove that g is a polynomial.
• Estimate the degree of g in terms of the integers k and n.
Let h =g(n), so h is entire and|h(z)|≤ M(2 +|zk|) for some M >0. Fix r >0. Now
for|z|≤ r, we have|h(z)|≤ M(2 +rk), therefore we can apply Cauchy’s estimates to
D(0,r ) to get
|h(m)(0)|≤ M(2 +rk)m!
rm
for every m∈ N. Sending r→∞ above yields g(m+n)(0) = h(m)(0) = 0 for m > k.
As an entire function, g has a global power series representation around 0; thus g is a
polynomial of degree at most k +n.
Spring 2012, 3. Let f(z) be an entire function. Suppose that there are positive
real numbers a,b and k such that|f(z)|≤ a +b|z|k for all z∈ C. Prove that f(z)
is a polynomial.
Same thing. Fix r >0. For|z|≤ r, we have
|f(z)|≤ a +brk.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 16
Thus by Cauchy’s estimates applied to D(0,r ), we get
|f (n)(0)|≤ (a +brk)n!
rn
for every n∈ N. Thus, sending r→∞ above, we get f (n)(0) = 0 for n > k. Being
entire,f has a global power series around 0, so f is a polynomial of degree at most⌈k⌉.
Spring 2011, 5. Prove that a nonconstant entire function maps C onto a dense
subset of C.
We show the contrapositive. Assumef is an entire function such thatf(C) is not dense
in C. Then there exists z0∈ C and ϵ> 0 such that
D(z0,ϵ )∩f(C) =∅.
That is,|f(z)−z0|≥ ϵ for every z∈ C. Thus
g(z) = 1
f(z)−z0
is an entire function which is bounded by 1
ϵ . Thus, by Liouville’s theorem g is constant.
Hence f is constant.
Spring 2011, 6. Suppose f is an entire function, and there is a positive real
numberM such that| Re(f(z))|≥| Im(f(z))| for all z with|z|≥ M. Prove that f
is constant on C.
By the previous question, it suﬃces to show that f(C) is not dense in C. Suppose, to
the contrary, it is dense. Let
K ={z∈ C :|z|≤ M}
and
Ω ={z∈ C :| Re(f(z))|≥| Im(f(z))|}.
We have f(C−K)⊆ Ω. Since Ω is closed, f(C−K)⊆ Ω. Also note that f(K) is
closed and bounded since K is compact. Now,
C =f(C)
=f(K)∪f(C−K)
=f(K)∪f(C−K)
⊆f(K)∪ Ω.
Thus C− Ω⊆f(K). This is a contradiction because C− Ω is unbounded.
Fall 2010, 5. Let f be a holomorphic function in the unit disk D(0, 1) and
|f(z)|≤ M for allz∈D(0, 1). Prove that|f′(z)|≤ M(1−|z|)−1 for allz∈D(0, 1).
Fix z0∈ D(0, 1) and choose δ such that|z0| < δ <1. Then if z∈ D(z0,δ−|z0|), we
have
|z| =|z−z0 +z0|≤| z−z0| +|z0|≤ δ−|z0| +|z0| =δ <1.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 17
That is, D(z0,δ−|z0|)⊆ D(0, 1) and hence |f|≤ M in this closed disk. Thus by
Cauchy’s estimates, we get
|f′(z0)|≤ M
δ−|z0|.
This is true for every 0 <δ < 1. Thus sending δ→ 1, we get
|f′(z0)|≤ M
1−|z0|.
Fall 2009, 5. Let f(z) be an analytic function on C which takes values in the
upper half plane, i.e., f : C→ H, where H ={x +iy : y > 0}. Show that f is
constant.
The only nontrivial part is to recall that H can be mapped conformally onto the unit
disk D. Indeed, the linear fractional transformation
φ(z) = z−i
z +i
does precisely that because z ∈ D if and only if z is closer to i than it is to −i,
if and only if |z−i| <|z +i|. Thus g = φ◦f maps the entire plane into D. Being
entire and bounded,g is constant by Liouville’s theorem. Sof =φ−1◦g is also constant.
Spring 2009, 1. Suppose thatf is entire and that f(z)
1 +|z|1/2 is bounded asz→∞ .
Prove that f is constant.
I want to say ‘So what does it mean?’ in my friend Peyman’s voice to the ﬁrst statement.
I guess it means that there exists M,L> 0 such that
|z|≥ L⇒
⏐⏐⏐⏐⏐
f(z)
1 +|z|1/2
⏐⏐⏐⏐⏐≤M.
Well, f(z)
1 +|z|1/2 is also bounded on |z|≤ L by compactness, so we may assume
⏐⏐⏐⏐⏐
f(z)
1 +|z|1/2
⏐⏐⏐⏐⏐≤M.
for all z∈ C. Now we are in business. Fix r >0. If|z|≤ r, we have
|f(z)|≤ M(1 +|z|1/2)≤M(1 +r1/2).
Thus applying Cauchy’s estimates to the closed disk D(0,r ), we get
|f (n)(0)|≤ M(1 +r1/2)n!
rn
for everyn∈ N. Sending r→∞ above, we getf (n)(0) = 0 for everyn≥ 1. Being entire,
f has a global power series representation around 0, and therefore all the coeﬃcients in
this power series except the constant term is 0. Thus f is constant.

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 18
6. Residue Calculus
I won’t state the Residue theorem, because its statement is much more confusing than
the usual applications and I am lazy.
Let me note the following useful lemma for calculating residues:
Lemma 5. Letg be analytic around z0 and f(z) = g(z)
(z−z0)n . Then
Res(f,z 0) = g(n−1)(z0)
(n− 1)! .
Proof. Res(f,z 0) is the coeﬃcient of the 1
z−z0
term in the Laurent series expansion of
f around z0, so it is equal to the coeﬃcient of the ( z−z0)n−1 term in the power series
expansion of g around z0. □
Fall 2012, 3. Evaluate the following integral for any α> 0
∫ ∞
0
ln(x)
x2 +α2
Carefully justify your steps.
Pickr,R such that 0 <r <α<R . Consider the following curves:
ϕR : [0,π ]→ C
t↦→Reit
λr,R : [−R,−r]→ C
t↦→t
ψr : [0,π ]→ C
t↦→rei(π−t)
µr,R : [r,R ]→ C
t↦→t
These look like a random selection of functions because I am trying to avoid drawing
things. Drawing shows that these curves can be juxtaposed consecutively to yield a
closed curve γR,r which has a semicircular shape with a small bump inside. Now let
V = C−{z∈ C : Re(z) = 0 and Im( z)≤ 0}. Note that every point which have
nonzero winding number (which must then be 1) with respect to γR,r lies in V . Also,
there is a continuous angle (or argument) function θ : V → (−π/2, 3π/2) which gives
rise to the analytic branch of logarithm
L :V→ C
z↦→ ln|z| +iθ(z)

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 19
Let f(z) = L(z)
z2 +α2 . The only singularity of f which lies inside γR,r is iα and if we let
g(z) = L(z)
z +iα, Lemma 5 yields
Res(f,iα ) =g(iα) = L(iα)
2iα
= ln(|iα|) +iθ(iα)
2iα
= ln(α) +iπ
2
2iα .
Therefore by the Residue theorem,
∫
γR,r
f(z)dz = 2πi Res(f,iα )
∫
ϕR
f(z)dz +
∫
λR,r
f(z)dz +
∫
ψr
f(z)dz +
∫
µR,r
f(z)dz = π ln(α)
α +iπ2
2α. (⋆)
Now we look at how the four integrals in ( ⋆) behave. When z is on ϕR, we have
|L(z)| =
»
[ln|z|]2 + [θ(z)]2
=
»
[lnR]2 + [θ(z)]2
≤
Ã
[lnR]2 +
Ç3π
2
å2
≤ lnR + 3π
2
and
|z2 +α2|≥
⏐⏐⏐|z2|−| α2|
⏐⏐⏐ =R2−α2.
Thus by the ML-inequality, we have
⏐⏐⏐⏐⏐
∫
ϕR
f(z)dz
⏐⏐⏐⏐⏐≤ lnR + 3π
2
R2−α2 · (length of ϕR) = lnR + 3π
2
R2−α2 πR−→0 as R→∞ .
Similarly, we have
⏐⏐⏐⏐⏐
∫
ψr
f(z)dz
⏐⏐⏐⏐⏐≤ lnr + 3π
2
α2−r2 πr−→0 as r→ 0

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 20
since limr→0r lnr = 0. Taking these limits in (⋆), we get
π ln(α)
α +iπ2
2α = lim
r→0
lim
R→∞
Ç∫
λR,r
f(z)dz +
∫
µR,r
f(z)dz
å
= lim
r→0
lim
R→∞
Ç∫ −r
−R
f(x)dx +
∫ R
r
f(x)dx
å
= lim
r→0
lim
R→∞
Ç∫ −r
−R
L(x)
x2 +α2dx +
∫ R
r
L(x)
x2 +α2dx
å
= lim
r→0
lim
R→∞
Ç∫ −r
−R
ln|x| +iπ
x2 +α2 dx +
∫ R
r
ln|x|
x2 +α2dx
å
= lim
r→0
lim
R→∞
Ç∫ −r
−R
ln|x|
x2 +α2dx +
∫ −r
−R
iπ
x2 +α2dx +
∫ R
r
ln|x|
x2 +α2dx
å
= lim
r→0
lim
R→∞
Ç
i
∫ −r
−R
π
x2 +α2dx + 2
∫ R
r
ln|x|
x2 +α2dx
å
.
Taking the real parts of both parts (note that Re( z) is a continuous function so it
commutes with limits), we get
π ln(α)
α = lim
r→0
lim
R→∞
Ç
2
∫ R
r
lnx
x2 +α2dx
å
.
Thus
∫ ∞
0
lnx
x2 +α2 = π ln(α)
2α .
I don’t think I’ll put any other solutions of integration problems. They are LONG, and
today is the prelim day.
7. Miscellaneous
These are problems which don’t ﬁt in one of the above categories.
Fall 2012, 2. Let f be a complex valued function in the unit disk D such that
g =f 2 and h =f 3 are both analytic. Prove that f is analytic.
Note that the zeros of f,g,h in D are the same. Let’s denote this common zero set by
Z. We may assumef is not identically zero, so the analytic functiong is not identically
zero; hence its zero set Z is isolated. Therefore, as g and h are analytic, every a∈ Z
has a neighborhood such that
g(z) = (z−a)m˜g(z)
h(z) = (z−a)n˜h(z)
where m,n are positive integers and ˜g, ˜h are analytic functions which don’t vanish
around a. Observe that a is a zero of the analytic map g3 = h2 of order 3m = 2n.
Since 2 and 3 are relatively prime, there exists a positive integer k such that m = 2k
and n = 3k. The function
ˆf(z) = (z−a)k ˜h(z)
˜g(z)

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 21
is well-deﬁned and analytic around a. When z⁄=a, we have ˆf(z) = h(z)
g(z) =f(z). And
ˆf(a) = 0 = f(a). Thus f = ˆf is analytic at a. Since a∈Z was arbitrary, we conclude
thatf is analytic onZ. Finally as 1/g is analytic on D−Z,f =h/g is analytic on D−Z.
Spring 2012, 4. Prove that there is no functionf that is analytic on the punctured
disk D−{ 0}, and f′ has a simple pole at 0.
Suppose, to the contrary, that there is such a function. So there is an open ball B
containing 0 such that in B−{ 0}, we have
f′(z) = c
z +g(z)
where c⁄= 0 and g∈ H(B). Since B is simply connected, there exists G∈ H(B) such
that G′ = g. Thus the function 1
c(G−f)∈ H(B−{ 0}) is an antiderivative of 1 /z.
This is impossible because there are closed curves in B−{ 0} on which the integral of
1/z is nonzero.
Fall 2011, 2. Let h be a nowhere zero, entire holomorphic function. Prove that
there exists an entire holomorphic function g such that eg =h.
Observe that h′
h is entire, therefore has an antiderivative f (C is simply connected).
Consider the entire function c(z) =h(z)e−f (z). We have
c′(z) =h′(z)e−f (z)−h(z)e−f (z)f′(z) =e−f (z) (h′(z)−h(z)f′(z)) = 0,
therefore c(z) is constant, say c(z)≡ c. Note that c⁄= 0 since h is nowhere zero.
Therefore c =ea for some a∈ C. So if we let g(z) =a +f(z), we have
h(z) =cef (z) =eaef (z) =ea+f (z) =eg(z).
Fall 2011, 5. Let f(z) be an entire holomorphic function. Suppose that f(z) =
f(z + 1) and|f(z)|≤ e|z| for all z∈ C. Prove that f(z) must be constant.
NOTE: My friend Theo solved this problem. He was very concerned that I won’t give
credit to him when I put the solution here :(
The idea is to write f(z) =g(e2πiz) and transfer the growth condition on f to a growth
condition on g. Let E(z) = e2πiz. E is locally invertible, that is, every z∈ C−{ 0}
has a neighborhood Vz such that there is an analytic map ϕz :Vz→ C which satisﬁes
E◦ϕz = id. Note that if ϕ :V → C and ψ :W→ C are two such local inverses of E,
for z∈V∩W we have
e2πiϕ(z) =E(ϕ(z)) =z =E(ψ(z)) =e2πiψ(z)
thereforeϕ(z) =ψ(z)+n for somen∈ Z. Since f is invariant under integer translations,
we havef◦ϕ =f◦ψ. Thus, the map
g : C−{ 0}→ C
z↦→ (f◦ϕz) (z)

SOLUTIONS TO COMPLEX PRELIM PROBLEMS 22
is analytic. We have g◦E = f, as desired. Now for every z∈ C−{ 0}, there exists
ω∈ C with 0 < Re(ω)< 1 such that z =e2πiω. We have
|g(z)| =|f(ω)|≤ e|ω| =e
√
[Re(ω)]2+[Im(ω)]2
<e
√
1+[Im(ω)]2
≤e1+| Im(ω)|. (⋆)
Note that
|z| =|e2πiω| =eRe(2πiω) =e−2π Im(ω)
hence
e− Im(w) =|z|
1
2π and eIm(ω) =|z|
−1
2π .
Thus|g(z)|≤ e· max{|z|
1
2π,|z|
−1
2π} by (⋆). So for R> 1, since g is entire, we can apply
Cauchy’s estimates to the closed disk D(0,R ) and get
|g(n)(0)|≤ R
1
2πn!
Rn = n!
Rn− 1
2π
−→0 as R→∞
for every n; thus g(n)(0) = 0 for every n≥ 1. This implies that g is constant (because
being entire,g has a global power series representation around 0). Thus f is constant.

