ALGEBRAIC TOPOLOGY I: FALL 2008
TIM PERUTZ
Contents
I. The fundamental group 3
1. Introduction 3
1.1. Homotopy equivalence 3
1.2. The fundamental groupoid 4
2. The fundamental group of the circle 6
2.1. Trivial loops 6
2.2. Computing π1(S1) 6
2.3. Applications 7
3. Van Kampen in theory 9
3.1. Group presentations 9
3.2. Push-outs 9
3.3. Van Kampen’s theorem 11
4. Van Kampen in practice 13
4.1. Fundamental groups of spheres 13
4.2. A useful lemma 13
4.3. Fundamental groups of compact surfaces 13
4.4. The complement of a trefoil knot 15
5. Covering spaces 17
5.1. Deck transformations 18
5.2. Examples 18
5.3. Unique path lifting 19
6. Classifying covering spaces 21
6.1. An equivalence of categories 21
6.2. Existence of a simply connected covering space 23
II. Singular homology theory 25
7. Singular homology 25
7.1. The deﬁnition 25
7.2. The zeroth homology group 26
7.3. The ﬁrst homology group 26
8. Simplicial complexes and singular homology 28
8.1. ∆-complexes 28
8.2. The Hurewicz map revisited 29
9. Homological algebra 30
9.1. Exact sequences 30
9.2. Chain complexes 31
10. Homotopy invariance of singular homology 34
11. The locality property of singular chains 37
12. Mayer–Vietoris and the homology of spheres 39
1

2 TIM PERUTZ
12.1. The Mayer–Vietoris sequence 39
12.2. Degree 41
13. Relative homology and excision 42
13.1. Relative homology 42
13.2. Suspension 43
13.3. Summary of the properties of relative homology 44
14. Vanishing theorems for homology of manifolds 45
14.1. Local homology 46
14.2. Homology in dimension n 46
15. Orientations and fundamental classes 49
15.1. Homology with coeﬃcients 49
15.2. What it’s good for 49
15.3. The local homology cover 49
15.4. Orientations 50
15.5. Fundamental classes 50
16. Universal coeﬃcients 53
16.1. Homology with coeﬃcients 53
16.2. Tor 53
16.3. Universal coeﬃcients 55
III. Cellular homology 57
17. CW complexes 57
17.1. Compact generation 59
17.2. Degree matrices 59
17.3. Cellular approximation 59
18. Cellular homology 61
19. Cellular homology calculations 64
19.1. Calculations 64
20. The Eilenberg–Steenrod axioms 67
IV. Product structures 70
21. Cohomology 70
21.1. Ext 71
22. Product structures, formally 74
22.1. The evaluation pairing 74
22.2. The cup product 74
22.3. The cap product 75
23. Formal computations in cohomology 77
23.1. The K¨ unneth formula 78
23.2. An algebraic application of cup product 78
24. Cup products deﬁned 80
24.1. The basic mechanism 80
24.2. Cup products in cellular cohomology 80
24.3. Cup products in singular cohomology 81
25. Non-commutativity 83
26. Poincar´ e duality 84

ALGEBRAIC TOPOLOGY I: FALL 2008 3
I. The fundamental group
1. Introduction
We explain that algebraic topology aims to distinguish homotopy types. We in-
troduce the fundamental groupoid and the fundamental group.
1.1. Homotopy equivalence.
1.1.1. A topological space is a set X equipped with a distinguished collection of
subsets, called ‘open’. The collection must be closed under ﬁnite intersections and
arbitrary unions. In particular, it includes the empty union ∅, and the empty
intersectionX.
A map X → Y between topological spaces is continuous if the preimage of
every open set in Y is open in X. A homeomorphism is a continuous map with a
continuous two-sided inverse.
Convention: In this course, ‘map’ will mean ‘continuous map’.
1.1.2. Elementary properties of spaces that are preserved by homeomorphism (e.g.
the Hausdorﬀ property, compactness, connectedness, path-connectedness) allow us
to distinguish some spaces. For instance, the interval [0 , 1] is not homeomorphic
to the circle S1 = R/Z because [0, 1]\{ 1/2} is disconnected, whilst S1\{x} is
connected for any x∈S1. The spaces Xn =⋁n
i=1S1 (the wedge product, or one-
point union, of n copies of S1) are all distinct, because it is possible to delete n,
but not n + 1, distinct points of Xn without disconnecting it.
However, if we thickened the circles in Xn to ribbons, making a space Yn, the
argument would fail. In algebraic topology, one looks for invariants of spaces which
are insensitive to such thickenings, so that if they distinguish the Xn they also
distinguish the Yn.
Deﬁnition 1.1. If f0,f 1 : X→ Y are maps, a homotopy from X→ Y is a map
F : [0, 1]×X→Y such thatF◦it =ft fort∈{ 0, 1}, whereit(x) = (t,x )∈ [0, 1]×X.
We often think of F as a path{ft}t∈[0,1] of maps ft : X→Y .
Homotopy deﬁnes an equivalence relation on the set of maps f : X→Y , which
we denote by the symbol ≃.
Deﬁnition 1.2. A homotopy equivalence is a mapf : X→Y such that there exists
g : Y →X which is an inverse up to homotopy. That is,f◦g≃ idY andg◦f≃ idX.
Exercise 1.1: Homotopy equivalence deﬁnes an equivalence relation on spaces.
The equivalence classes are called homotopy types. Algebraic topology provides
a collection of invariants of homotopy types. The principal invariants are the fun-
damental group and the homology groups, and the homomorphisms between these
groups associated with maps between spaces.
Exercise 1.2: The following equivalent conditions deﬁne what is means for a non-empty
space X to be contractible. Check their equivalence.
• X is homotopy equivalent to a one-point space.
• For every x∈X, the inclusion {x}→ X is a homotopy equivalence.
• For some x∈X, the inclusion {x}→ X is a homotopy equivalence.
• For some x∈X, the constant map cx : X→X at x is homotopic to idX.
Exercise 1.3: Any convex subset of Rn is contractible.

4 TIM PERUTZ
Convex subsets of Rn are contractible for a particular reason: their points are
deformation retracts. In general, if X is a space and i: A→ X the inclusion of a
subspace, we say that A is a deformation retract of X if there is a map r : X→A
such that r◦i = idA and i◦r≃ idX by a homotopy{ht} so that (in addition to
h0 = i◦r and h1 = idX) one has ht(a) = a for all t and a∈ A. Such a map r,
called a deformation retraction, is obviously a homotopy equivalence.
Exercise 1.4: Show carefully that the letter A, considered as a union of closed line
segments in R2, is homotopy equivalent but not homeomorphic to the letter O. Show
brieﬂy that all but one of the capital letters of the alphabet is either contractible or
deformation-retracts to a subspace homeomorphic to O. Show that the letters fall into
exactly three homotopy types. How many homeomorphism types are there? (View a
letter as a ﬁnite union of the images of paths [0, 1]→ R2. Choose a typeface!)
Exercise 1.5: Let {Xα}α∈A be a collection of spaces indexed by a set A. Let xα∈Xα
be basepoints. Deﬁne the wedge sum (or 1-point union)⋁
α∈AXα as the quotient space
of the disjoint union ∐
αXα by the equivalence relation xα∼ xβ for all α, β∈ A.
Show carefully that, for n≥ 1, the complement of p distinct points in Rn is homotopy-
equivalent to the wedge sum of p copies of the sphere Sn−1 ={x∈ Rn :|x| = 1}.
Remark. Let’s look ahead. Theorems of Hurewicz and J. H. C. Whitehead imply
that, among all spaces which are cell complexes , the sphere Sn ={x∈ Rn+1 :
|x| = 1}, with n> 1, is characterized up to homotopy equivalence by its homology
groupsH0(Sn)∼=Hn(Sn)∼= Z,Hi(Sn) = 0 fori /∈{ 0, 1} and its trivial fundamental
group. In general, distinct homotopy types can have trivial fundamental groups and
isomorphic homology groups (e.g. S2×S2, CP 2#CP 2). Another invariant, the
cohomology ring, distinguishes these two examples. When it fails to distinguish
spaces, one localizes the problem and works over Q and mod primes p. Over Q, a
certain commutative diﬀerential graded algebra gives a new invariant [D. Sullivan,
Inﬁnitesimal computations in topology , Publ. Math. I.H.E.S. (1977)]. Mod p, one
considers the Steenrod operations on cohomology. There is an algebraic structure
which captures all this at once, and gives a complete invariant for the homotopy
type of cell complexes with trivial fundamental group [M. Mandell, Cochains and
homotopy type, Publ. Math. I.H.E.S. (2006)].
1.2. The fundamental groupoid.
1.2.1. Our ﬁrst invariants of homotopy type are the fundamental groupoid and the
isomorphism class of the fundamental group.
A path in a space X is a map f : I→X, where I = [0, 1]. Two paths f0 and f1
are homotopic rel endpoints if there is a homotopy {ft}t∈[0,1] between them such
thatft(0) andft(1) are both independent of t. Write∼ for the equivalence relation
of homotopy rel endpoints.
Two paths f and g are composable if f(1) = g(0). In this case, their composite
f·g is the result of traversing ﬁrstf, theng, both at double speed: (f·g)(t) =f(2t)
for t∈ [0, 1/2] and (f·g)(t) =g(2t− 1) for t∈ [1/2, 1].
The composition operation is not associative: ( f·g)·h⁄= f· (g·h). What is
true, however, is that (f·g)·h∼f· (g·h). (Proof by picture.)
If f is a path, let f−1 denote the reversed path: f−1(t) = f(1−t). One has
f·f−1 ∼ cf(0) and f−1·f ∼ cf(1), where cx denotes the constant path at x.
(Picture.) Moreover, cf(0)·f≃f and f·cf(1)≃f.

ALGEBRAIC TOPOLOGY I: FALL 2008 5
We now deﬁne a category Π1(X), the fundamental groupoid of X. A category
consists of a collection (for instance, a set) of objects, and for any pair of objects
(x,y ), a set Mor( x,y ) of ‘morphisms’ (or ‘maps’) from x to y. Also given is an
associative composition rule
Mor(x,y )× Mor(y,z )→ Mor(x,z ).
Each set Mor(x,x ) must contain an identityex (meaning that composition with ex
on the left or right does nothing).
The objects of the category Π 1(X) are the points of X. Deﬁne Π 1(x,y ) as the
set of equivalence classes of paths from x to y under the relation of homotopy rel
endpoints. Π 1(x,y ) will be the morphism set Mor( x,y ) in the category. One has
well-deﬁned composition maps Π1(x,y )×Π1(y,z )→ Π1(x,z ), which are associative
by our discussion. The class [cx] of the constant path atx deﬁnes an identity element
ex for Π1(x,x ). This shows that Π 1(X) is a category.
A category in which every morphism has a 2-sided inverse is called a groupoid.
Every morphism [f]∈ Π1(x,y ) has a 2-sided inverse [f−1]∈ Π1(y,x ).
1.2.2. Groupoids are too complicated to be really useful as invariants. However,
as with any groupoid, the sets Π 1(x,x ) form groups under composition, and we
can use this to extract a practical invariant. When a basepoint x∈ X is ﬁxed,
π1(X,x ) := Π 1(x,x ) is called the fundamental group . It is the group of based
homotopy classes of loops based at x.
• IfX is path connected, the fundamental groups for diﬀerent basepoints are
all isomorphic. Indeed, if f is a path from x to y then the map
π1(X,x )→π1(Y,y ), [γ]↦→ [f]· [γ]· [f−1]
is an isomorphism.
• If F : X→Y is a map, there is an induced homomorphism
F∗ : π1(X,x )→π1(Y,F (x)), [f]↦→ [F◦f].
If G: Y →Z is another map, one clearly has G∗F∗ = (G◦F )∗.
• MapsF0 andF1 which are based homotopic (i.e. homotopic through maps
Ft withFt(x) constant for all t) give the same homomorphismπ1(X,x )→
π1(Y,F 0(x)).
Exercise 1.6: (a) If f0 and f1 are loops (I,∂I )→ (X,x ), we say they are homo-
topic through loops if they are joined by a homotopy ft with ft(0) equal to
ft(1) but not necessarily to x. Show that f0 is homotopic to f1 through loops
iﬀ [f0] is conjugate to [f1] in π1(X,x ).
(b) Show that a homotopy equivalence between path connected space induces an
isomorphism on π1, regardless of the choices of basepoints.
A point ∗ clearly has trivial π1 (there’s only one map I→∗ ). By (b) from the
exercise, π1(X,x ) ={1} for any contractible space X and any x∈X.
A space is called simply connected if it is path-connected and has trivial π1. We
have just seen that contractible spaces are simply connected.
Exercise 1.7: (*) Prove directly that the 2-sphere S2 ={x∈ R3 :|x| = 1} is simply
connected.

6 TIM PERUTZ
2. The fundamental group of the circle
Our ﬁrst calculation of a non-trivial fundamental group has already has remark-
able consequences.
2.1. Trivial loops. We begin by interpreting what it means for a loop to be trivial
in the fundamental group. It is convenient to regard a loop not as a map f : I→X
with f(1) =f(0) but as a map from the unit circle S1 =∂D2⊂ C intoX.
Proposition 2.1. A loopf : S1→X represents the identity elemente∈π1(X,f (1))
if and only if it extends to a map from the closed unit disc D2 into X.
Thus a simply connected space is a path-connected space in which every loop
bounds a disc.
Proof. If [f] = 1 ∈ π1(X,f (1)), let {ft}t∈[0,1] be a homotopy rel endpoints from
the constant map cf(1) to f =f1. Deﬁne a continuous extension F : D2→X of f
by setting F (z) =f|z|(z/|z|) if z⁄= 0 and F (0) =f(1).
Conversely, iff extends toF : D2→X, deﬁne a mapI×S1→X, (t,z )↦→F (tz).
Then F is a homotopy from the constant map cF(0) to f. The latter is in turn is
homotopic through constant maps to cf(1). Hence f is homotopic through loops to
cf(1). By (a) from Exercise 1.6, [ f] is conjugate to [ cf(1)]. But [ cf(1)] = e, hence
[f] =e. □
2.2. Computing π1(S1).
Theorem 2.2. The fundamental group of S1 is inﬁnite cyclic: there is a (unique)
homomorphism deg: π1(S1)∼= Z such that deg(idS1) = 1.
We think ofS1 as R/Z, and take [0] as basepoint. Note that two maps S1→S1
taking [0] to [0] are homotopic through loops iﬀ they represent conjugate elements
in π1(S1, [0]). By the theorem, π1 is abelian, so conjugate elements are actually
equal. Hence deg is actually an invariant of homotopy through loops, indeed a
complete invariant.
The key idea of the proof is to look at the quotient map p: R→ R/Z =S1. This
map is the prototypical example of a covering map.
Lemma 2.3. Every map f : (I,∂I )→ (S1, [0]) lifts uniquely to a map ˜f : I→ R
such that (i) ˜f(0) = 0, and (ii) p◦ ˜f =f.
Proof. Let T be the set of t∈I such that ˜f exists and is unique on [0 ,t ]. For any
[x] = p(x)∈ S1, the open set U[x] = p(x− 1/4,x + 1/4)⊂ S1 contains [x] and
has the following property: the preimage p−1(U) is the disjoint union of open sets
Vn
x := (n+x−1/4,n +x−1/4),n∈ Z. Moreover, p maps eachVn
x homeomorphically
ontoU.
If ˜f has been deﬁned on [0,t ], witht< 1, there existsδ >0 so thatf(t−δ,t +δ)⊂
Uf(t). Since ˜f(t)∈V 0
˜f(t), we are forced to deﬁne ˜f on [t,t +δ) as the composite
[t +δ)
f
−−−−→Uf(t)
p−1
−−−−→V 0
f(t).
This does indeed deﬁne an extension of ˜f to [0,t +δ). So T is an open set.
Now suppose ˜f exists and is unique on [0 ,t ). Since f(s) → f(t) as s → t,
when 0 < t−s≪ 1 the lifts ˜f(s) must lie in one of the open sets V projecting

ALGEBRAIC TOPOLOGY I: FALL 2008 7
homeomorphically to Uf(t), independent of s. Thus we can deﬁne ˜f(t) to be the
preimage of f(t) that lies in V , and this deﬁnes the unique continuous lift of f on
[0,t ]. Hence T is closed. Since I is connected and T non-empty, we have T = I.
□
Proof of the theorem. Given f : (I,∂I )→ (S1, [0]), construct ˜f as in the lemma.
Since p◦ ˜f(1) = [0], ˜f(1) is an integer. Deﬁne the degree deg(f) to be this integer.
Since ˜f was uniquely determined byf, deg(f) is well-deﬁned. We now observe that
if{ft}t∈[0,1] is a based homotopy then deg(f0) = deg(f1). Indeed, we can lift each
ft to a unique map ˜ft : I→ R, p( ˜ft(0)) = [0], and p◦ ˜ft = ft. It is easy to check
that the ˜ft vary continuously in t, hence deﬁne a homotopy { ˜ft} from ˜f0 to ˜f1.
Thus deg(ft) = ˜ft(1) is a continuous Z-valued function, hence constant.
Thus deg deﬁnes a map π1(S1)→ Z. It is a homomorphism because ~f·g is
given on [0, 1/2] by the unique lift of t↦→ f(2t) which begins at 0 (this ends at
deg(f)), and on [1/2, 1] by the unique lift of t↦→f(2t− 1) which begins at deg(f)
(this ends at deg(g) + deg(f)).
The degree homomorphism is surjective because deg(id S1) = 1. To see that it
is injective, suppose deg f = 0. Then ˜f is a loop in R, based at 0. Since R is
simply connected, ˜f is based-homotopic to the constant map, and applying p to
this homotopy we see that the same is true of f. □
2.3. Applications.
Corollary 2.4 (The fundamental theorem of algebra) . Every non-constant poly-
nomial p(z)∈ C[z] has a complex root.
Proof. We may assumep is monic. If p(z) =zn +cn−1zn−1 +··· +c0 has no root,
p(z)/|p(z)| is a well-deﬁned function C→ S1⊂ C. Let f denote its restriction to
the circle{|z| = 1}. Now, f extends to a map from the unit disc to S1, whence f
is null-homotopic (cf. the last lecture) so deg( f) = 0 by the homotopy-invariance
of degree.
Now deﬁne ft : S1 → S1 for t > 1 by ft(z) = p(tz)/|p(tz)|. The ft are all
homotopic, and f1 =f, so deg(ft) = 0 for all t. But for |z|≫ 0,|cn−1zn−1 +··· +
c0|<|zn|, and hence ps(z) :=zn +s(cn−1zn +··· +c0) has no root for 0 ≤s≤ 1.
Thus, for some ﬁxed t≫ 0, we can deﬁne gs : S1→S1 bygs(z) = ps(tz)/|ps(tz)|,
and this deﬁnes a homotopy from ft = g1 to g0. But g0(z) = zn/|zn|, and so
degg0 =n (check this!). Hence n = 0. □
Remark. Some proofs of FTA invoke Cauchy’s theorem from complex analysis. To
make the link with our approach, note that if γ : S1→ C∗ is a loop then, by the
residue theorem (a consequence of Cauchy’s theorem) the complex number
d(γ) = 1
2πi
∫
γ
z−1dz
is actually an integer depending on γ only through its homotopy class in C∗. When
γ is a based loop S1→ S1⊂ C∗, d(γ) = deg(γ) (this follows from our theorem,
bearing in mind that d deﬁnes a homomorphismd: π1(S1)→ Z and thatd(idS1) =
1).
Another corollary is the Brouwer ﬁxed point theorem.
Corollary 2.5. Every continuous map g : D2→D2 has a ﬁxed point.

8 TIM PERUTZ
(Here D2 denotes the closed unit disc.)
Proof. Suppose g has no ﬁxed point. Then, for any x∈ D2, there is a unique
line passing through x and g(x). Deﬁne r(x)∈S1 to be the point where this line
hits S1 =∂D2 when one starts at g(x) and moves along the line towards x. Thus
r(x) = x when x∈ ∂D2. Writing r(x) = x +t(g(x)−x), one calculates from the
requirements that|r(x)| = 1 and t≤ 0 that
t =⟨x,x−g(x)⟩−
√
⟨x,x−g(x)⟩2− (|x|2− 1)|x−g(x)|2
|x−g(x)|2 .
Thusr is continuous.
On the other hand, there can be no continuous r : D2→ ∂D2 with r|∂D 2 = id,
for if such an r existed, the degree of its restriction r′ to the boundary would be 1
(because r′ = id) but also 0 (because r′ extends over D2). Hence there must be a
ﬁxed point. □
Remark. The Brouwer ﬁxed point theorem holds in higher dimensions too: every
continuous map g : Dn→Dn has a ﬁxed point. One can attempt to prove it using
the same argument. For this to work, what one needs is a homotopy-invariant,
integer-valued degree for mapsSn−1→Sn−1. The identity map should have degree
1 and the constant map degree 0. With such a function in place, the same argument
will run.
There are many ways of deﬁning a degree function (actually, the same degree
function): one can use homology theory, homotopy theory, diﬀerential topology or
complex analysis.
Exercise 2.1: Show that every matrix A∈SL2(R) can be written uniquely as a product
KL with K∈ SO(2) and L lower-triangular with positive diagonal entries. Use this
to write down (i) a deformation-retraction of SL2(R) (topologized as a subspace of
R4) onto its subspace SO(2); and (ii) a homeomorphism S1× (0,∞)× R→SL2(R).
Deduce that SL2(R) is path-connected and that π1(SL2(R))∼= Z.
Exercise 2.2: The polar decomposition. It is known that every matrix A∈ SL2(C)
can be written uniquely as a product UP with U ∈ SU (2) and P positive-deﬁnite
hermitian. Assuming this, deduce a homeomorphism S3×(0,∞)× C→SL2(C). (We
will soon see that this implies π1SL2(C) ={1}.)

ALGEBRAIC TOPOLOGY I: FALL 2008 9
3. Van Kampen in theory
There are two basic methods for computing fundamental groups. One, the method
of covering spaces, generalises our proof thatπ1(S1) = Z. The other, which we shall
discuss today, is to cut the space into simpler pieces and use a ‘locality’ property of
π1 called van Kampen’s theorem (a.k.a. the Seifert–van Kampen theorem).
3.1. Group presentations.
Deﬁnition 3.1. A free group on a set S is a group FS equipped with a map
i: S→ FS enjoying a ‘universal property’: for any map f from S to a group G
there is a unique homomorphism ˜f : FS→G with ˜f◦i =f.
If FS and F′
S are both free groups on S, and i: S → FS and i′ : S → F′
S
the deﬁning maps, then there are unique homomorphisms h: FS→ F′
S such that
h◦i =i′ and h′ : F′
S→FS such that h◦i′ =i. Thus h′◦h◦i =i. It follows that
h′◦h = id, since both sides are homomorphisms FS→ FS extending i. Hence h
and h′ are inverse isomorphisms.
The free group Fn :=F{1,...,n} can be realised as the group of all ‘words’ made
up of ‘letters’ a1,...,a n and their formal inverses a−1
1 ,...,a −1
n , e.g. a4a−1
3 a2
4a−7
1 .
Expressions aia−1
i and a−1
i ai can be deleted or inserted. The group operation is
concatenation of words, e.g. ( a4a−1
3 )· (a3a3
2) = a4a−1
3 a3a3
2 = a4a3
2. The identity
element is the empty word. The mapi sendsm toam, and given anf :{1,...,n }→
G we extend it to ˜f by sending, for example, a2a−1
1 a2
3 to f(a2)f(a1)−1f(a3)2.
We often write this group as ⟨a1,...,a n⟩. For example, F1 =⟨a⟩∼= Z.
Lemma 3.2. The groups Fn, for diﬀerent n, are all distinct.
Proof. The abelianization ( Fn)ab := Fn/[Fn, Fn] is isomorphic to Zn, and Zn/2Zn
has 2n elements. □
Now suppose that r1,...,r m are elements of⟨a1,...,a n⟩. Let R be the smallest
normal subgroup containing theri (R is thought of as a group of ‘relations’). Deﬁne
⟨a1,...,a n|r1,...,r m⟩ =⟨a1,...,a r⟩/R.
IfG is a group, andg1,...,g n∈G group elements, there’s a unique homomorphism
f :⟨a1,...,a n⟩→ G sending each ai togi. It is surjective iﬀ g1,...,g n generateG.
In this case, G∼=⟨a1,...,a n⟩/ kerf. Thus, if g1,...g n generate G, and r1,...,r m
are elements of ⟨a1,...,a n⟩ which generate ker f as a normal subgroup, then f
induces an isomorphism
⟨a1,...,a n|r1,...,r m⟩→ G.
Such an isomorphism is called a (ﬁnite)presentation forG. As examples, we have(!)
Z/(n)∼=⟨a|an⟩, D 2n∼=⟨a,b|an, b2, (ba)2⟩, Z2∼=⟨a,b|aba−1b−1⟩.
3.2. Push-outs.
Deﬁnition 3.3. Consider three groups, G1, G2 and H, and a pair of homomor-
phisms
G1
f1
←−H
f2
−→G2.

10 TIM PERUTZ
A push-out for (f1,f 2) is another group P and a pair of homomorphisms p1 : G1→
P and g2 : G2→P forming a commutative square
H
f1
−−−−→G1
f2
↓
↓p1
G2
p2
−−−−→P
and satisfying a universal property: given any other such square (a group K and
homomorphisms k1 : G1→K and k2 : G2→K such that k1◦f1 =k2◦f2), there
is a unique homomorphism h: P→K such that k1 =h◦p1 and k2 =h◦p2.
Exercise 3.1: Prove that the universal property determines P up to isomorphism. In
what sense is the isomorphism unique?
We can understand push-outs concretely using group presentations. Suppose
G1 =⟨a1,...,a n| r1,...r m⟩ and that G2 =⟨b1,...,b p| s1,...,s q⟩. Also suppose
thatH has generatorsh1,...,h o. In the push-out square above, the groupP is then
a group called the free product of G1 and G2 amalgamated along H and notated
G1∗H G2. It has the presentation
G1∗H G2 =⟨a1,...,a n,b 1,...,b p|r1,...r m,s 1,...,s q,c 1,...,c o⟩,
where ci =f1(hi)f2(hi)−1.
Exercise 3.2: Check that K =G1∗H G2 ﬁts into a push-out square for f1 and f2.
Note that there was no need for our group presentations to be ﬁnite, except for
notational convenience: we can allow inﬁnite sets of generators and relations.
Exercise 3.3: The free product G1∗G2 of groups G1 and G2 is the push-out of the
diagramG1←{ 1}→ G2. Deﬁne D∞ as the subgroup of the group of aﬃne transfor-
mations R→ R generated byx↦→−x andx↦→x+1. Prove that D∞∼= (Z/2)∗(Z/2).
Exercise 3.4: In this exercise we show that the modular group, PSL 2(Z) =SL2(Z)/{±I},
is the free product (Z/2)∗ (Z/3). Deﬁne three elements of SL2(Z),
S =
[ 0 1
−1 0
]
, T =
[ 1 −1
0 1
]
, U =ST =
[ 0 1
−1 1
]
.
(a) Verify that S2 =U3 =−I.
(b) Show that, for any A∈ SL2(Z), there is an n∈ Z such that the matrix[
a b
c d
]
=ATn has c = 0 or|d|≤| c|/2.
(c) Explain how to ﬁnd an integer l≥ 0 and a sequence of integers n1,...,n l
such that either ATn1STn2S...ST l or ATn1STn2S...ST lS has 0 as its
lower-left entry.
(d) Show that S and T generate SL2(Z).
(e)* Deﬁne θ :⟨a,b | a2,b 3⟩ = ( Z/2)∗ (Z/3) → PSL 2(Z) to be the unique
homomorphism such that θ(a) = ±S and θ(b) = ±U. Remind yourself
how PSL 2(R) acts on the upper half-plane H⊂ C by M¨ obius maps. Take
1⁄= w∈ (Z/2)∗ (Z/3). Prove that the M¨ obius map µw corresponding to
θ(w)∈PSL 2(R) has the property that µw(D)∩D =∅, where
D ={z∈ H : 0< Rez <1/2,|z− 1|> 1}.
[Hint: consider A :={z∈ H : Re z > 0} and B :={z∈ H :|z− 1| >
max(1,|z|)}.] Deduce that θ is an isomorphism.

ALGEBRAIC TOPOLOGY I: FALL 2008 11
3.3. Van Kampen’s theorem.
Theorem 3.4. Suppose that X is the union of two path-connected open subsets
U and V with path-connected intersection U∩V . Take x∈ U∩V . Then the
commutative diagram
π1(U∩V,x ) −−−−→π1(U,x )
↓
↓
π1(V,x ) −−−−→π1(X,x )
of maps induced by the inclusions is a push-out square.
Example 3.5. Let Cn be the complement of n points in the plane. Observe that
Cn deformation-retracts to the wedge sum⋁n
i=1S1. We haveπ1(Cn)∼= Fn. Indeed,
when n >0,⋁n
i=1S1 is the union of a subspace U which deformation-retracts to⋁n−1
i=1 S1, and a subspace V which deformation-retracts to S1, where the subspace
U∩V is contractible. By induction, π1(U)∼= Fn−1. We know π1(V )∼= Z = F1.
The push-out of Fn−1 and Z along the trivial group H is Fn−1∗ F1∼= Fn. Thus the
result follows from van Kampen’s theorem.
Lemma 3.6. For any loop γ : (I,∂I )→ (X,x ), there exists a ﬁnite, strictly in-
creasing sequence 0 = s0 <s 1 <s 2 <··· <s n = 1 such that γ maps each interval
[si,si+1] into U or into V .
Proof. Everyx∈I has a connected open neighbourhood whose closure maps to U
or toV . Since I is compact, ﬁnitely many of these intervals coverI. The endpoints
of the intervals in the ﬁnite cover form a ﬁnite subset ofI, which we may enumerate
in ascending order as (s0,...,s n). □
Let us call the sequence (si) a subdivison for γ.
Lemma 3.7. Suppose Γ = {γt}t∈[0,1] is a homotopy of paths (I,∂I )→ (X,x ).
Then there are increasing sequences 0 = t0 < t1 <··· < tm = 1, and 0 = s0 <
··· < sn = 1, such that Γ maps each rectangle [ti,ti+1]× [sj,sj+1] into U or into
V . Moreover, we can take the sequence (si) to reﬁne given subdivisions of γ0 and
γ1.
Exercise 3.5: Prove the lemma.
Proof of Van Kampen’s theorem. Suppose we are given a group G and homomor-
phismsf : π1(U)→G,g : π1(V )→G which agree on the images of π1(U∩V ). We
construct a map α: π1(X)→ G so that f = α◦ (iU)∗ and g = α◦ (iV )∗, where
iU : U→X and iV : V →X are the inclusions.
Takeγ : (I,∂I )→ (X,x ), and choose a subdivision s0 <··· < sn. Label the
intervals [si,si+1] as red or blue, in such a way that γ maps red intervals to U
and blue intervals to V . For 0 < i < n, connect γ(si) to x by a path δi inside
U (if both adjacent intervals [ si−1,si] and [ si,si+1] are red), inside V (if both
adjacent intervals are blue), or inside U∩V (if the adjacent intervals are diﬀerent
colours). Then βi :=δ−1
i ∗γ|[si,si+1]∗δi is a loop in either U or V . Deﬁne α[γ] =
α1[β0]····· αn−1[βn−1], where αi is either f or g according to whether [si,si+1] is
red or blue.
We need to see that α is well-deﬁned, and does not depend on the choices of
path, subdivision and colouring. Observe that for a ﬁxed γ and ﬁxed subdivision,

12 TIM PERUTZ
changing the colouring does not aﬀect α, because f and g agree on the image of
π1(U∩V ). Moreover, reﬁning a subdivision for givenγ does not aﬀect the deﬁnition
ofα. Nor does changing the choice of a path δi (instead of trying to replace δi by a
rival path δ′
i, insert an extra point into the subdivision, and use both paths δi and
δ′
i).
Hence we are left with considering homotopic paths γ0 and γ1 with a common
subdivision s0 <··· <s n.
Given a homotopy Γ = {γt}, we can subdivide [0 , 1]× [0, 1] into rectangles
Rij = [ti,ti+1]× [sj,sj+1] and color the Rij as red or blue in such a way so that Γ
maps the red rectangles to U and the blue ones to V . It will suﬃce to show that
γ0 and γt1 give the same deﬁnition for α.
This last part of the argument requires pictures, which I will draw in class.
(Consult Hatcher if you need to.) The idea is this: rather than going along the
bottom edge ofR0j we can go around the other three sides. We haveγ0≃β0∗···∗ βn,
but by going round these three sides we can replace βi by a new loop β′
i, and this
will not aﬀect α. By eliminating backtracking we can get from β0∗···∗ βn to γt1,
again without aﬀecting α.
Knowing it is well-deﬁned, one can check that α is a homomorphism making the
two triangles commute (do so!). Note also that it is theunique such homomorphism:
sinceγ is homotopic to the composite of the δi∗γ|[si,si+1]∗δ−1
i , we have no choice
but to deﬁne α this way. This concludes the proof. □

ALGEBRAIC TOPOLOGY I: FALL 2008 13
4. Van Kampen in practice
We compute some fundamental groups using van Kampen’s theorem.
4.1. Fundamental groups of spheres. A ﬁrst use of van Kampen’s theorem is
to show that spaces that should be simply connected are simply connected.
Proposition 4.1. Let Sn ={x∈ Rn+1 :|x| = 1} be the n-sphere. When n≥ 2,
π1(Sn) is trivial.
Proof. Notice that the subspace U ={x = (x0,...,x n)∈ Sn : x0⁄= 1} is home-
omorphic to Rn. Similarly, V :={x = (x0,...,x n)∈ Sn : x0⁄=−1} is homeo-
morphic to Rn. Thus U and V are contractible open sets, and their intersection is
path connected: it deformation-retracts to the equator {x0 = 0}∼=Sn−1, which is
path connected when n− 1 > 0. By van Kampen, π1(Sn) is the push-out of two
homomorphisms to the trivial group; it is therefore trivial. □
4.2. A useful lemma.
Lemma 4.2. Suppose
H
f
−−−−→G
↓
↓p
{1} −−−−→P
is a pushout square. Then p is surjective, and its kernel is the normalizer of imf.
Proof. Put P′ = G/N, where N is the normalizer of im f, and deﬁne p′ : G→ P′
to be the quotient map. It is easy to check that P′ andp′ ﬁt into a push-out square
for the homomorphisms f : H→G and H→{ 1}. Thus P is isomorphic to P′ so
that p is identiﬁed with p′. □
In conjunction with van Kampen’s theorem, this lemma has the following con-
sequence.
Proposition 4.3. Suppose that X is the union of a path-connected open set U and
a simply connected open set V , with U∩V path-connected. Let x∈U∩V . Then
π1(X,x ) is generated by loops in U. A based loop in U becomes trivial in π1(X) iﬀ
it lies in the normal subgroup of π1(U,x ) generated by loops in U∩V .
4.3. Fundamental groups of compact surfaces.
Proposition 4.4. Let T 2 be the 2-torus, RP 2 the real projective plane, K2 the
Klein bottle. Then
π1(T 2)∼= Z2; π1(RP 2)∼= Z/2; π1(K2)∼=⟨a,b|aba−1b⟩.
No two of these spaces are homotopy-equivalent.
Proof. These spaces X are all quotient spaces q : I2→ X of the square I2⊂ R2,
obtained by gluing together its sides in pairs. Take p in int(I2).
Let U = q(I2\{p}), and V = q(D) with D a small open disc containing p.
ThusU∩V deformation-retracts to a circle and V is simply connected. By the last
proposition, π1(X) is generated by loops in the subspace U, which deformation-
retracts to q(∂I 2).
Going anticlockwise round ∂I 2, we label the sides as s1, s2, s3, s4 (as directed
paths).

14 TIM PERUTZ
In T 2, q(s1) = q(s−1
3 ) and q(s2) = q(s−1
4 ). Thus U deformation-retracts to
a wedge of two circles a = q(s1) and b = q(s2), and ∂U ≃ s1·s2·s3·s4 ≃
a·b·a−1·b−1. To apply van Kampen, note that π1(U∩V ) = Z andπ1(U) =⟨a,b⟩.
The homomorphism Z→ F2 induced by U∩V ↪→ U sends 1 to aba−1b−1. Thus,
by the last proposition,
π1(T 2)∼=⟨a,b|aba−1b−1⟩∼= Z2.
InK2, q(s1) =q(s3) and q(s2) =q(s−1
4 ). The argument is just the same as for the
torus, except that now the homomorphism Z→F2 sends 1 to aba−1b. Thus
π1(K2)∼=⟨a,b|aba−1b⟩.
In RP 2, q(s1) = q(s3) and q(s2) = q(s4). Thus q(∂I 2) is a single circle, and the
map q : ∂I 2→ 1(∂I 2) has degree 2. So π1(U) = Z and π1(U∩V ) = Z. The map
π1(U∩V )→π1(U) corresponds to x↦→ 2x as a map Z→ Z. Hence
π1(RP 2)∼= Z/2.
It follows easily that these three spaces are homotopically inequivalent: the abelian-
ized fundamental groups (in which everything commutes) are π1(T 2)ab ∼= Z2,
π1(RP 2)ab∼= Z/2 and π1(K2)ab∼= Z/2⊕ Z. □
As part of the last proposition, we showed π1(T 2) = Z2. We now compute π1
for a torus with n punctures.
Lemma 4.5. Letp1,...,p n be distinct points of T 2. There are isomorphisms
θn : π1(T 2\{p1,...,p n})→Gn :=⟨γ1,...,γ n,a,b |aba−1b−1(γ1··· γn)−1⟩
so that ﬁlling in pn induces the following commutative diagram:
π1(T 2\{p1,...,p n}) −−−−→π1(T 2\{p1,...,p n−1})
θn
↓
↓θn−1
Gn −−−−→
gn
Gn−1,
wheregn(γn) = 1, gn(γi) =γi for i<n , gn(a) =a and gn(b) =b.
Proof. Apply van Kampen to a decomposition of T 2\{p1,...,p n} into a once-
punctured torus U and an (n + 1)-punctured 2-sphere. □
Proposition 4.6. Let Σg be the closed orientable surface of genus g. Then
π1(Σg)∼=⟨a1,b 1,...,a g,bg| [a1,b 1]··· [ag,bg]⟩,
where [a,b ] :=aba−1b−1. If p1,...,p n are distinct points in Σg then
π1(Σg\{p1,...,p n})∼=⟨a1,b 1,...,a g,bg,γ 1,...,γ n| [a1,b 1]··· [ag,bg] =γ1··· γn⟩.
Proof. By induction on g. We have already proved it for g = 0 and for g = 1.
Decompose Σg\{p1,...,p n} as the union of U ≃ Σg\{p1,...,p n,q} and V ≃
T 2\{q′} along an annulus U∩V (wrapping round q inU and around q′ inV ). By
induction ong, van Kampen, and the last lemma, we ﬁnd thatπ1(Σg\{p1,...,p n})
has generators
a1,b 1,...,a g−1,bg−1,γ 1,...,γ n,δ
coming from U;
ag,bg,γn+1,δ′

ALGEBRAIC TOPOLOGY I: FALL 2008 15
coming from V ; a relation δ =δ′ from U∩V ; and relations
[a1,b 1]··· [ag−1,bg−1] =γ1··· γnδ, [ag,bg] =δ′−1γn+1
from U and V . It is easy to check that this system of generators and relations are
equivalent to those given. □
Another standard way to prove this is to think of Σ g as an identiﬁcation-space
of the 4g-gon.
4.4. The complement of a trefoil knot. The left-handed trefoil knot K is the
image of the embedding f : S1→S3 ={(z,w )∈ C2 :|z|2 +|w|2 = 1} given by
f(e2πit) = ( 1√
2e4πit, 1√
2e6πit).
Proposition 4.7. π1(S3\K)∼=⟨a,b|a2b−3⟩.
Proof. We decompose S3 as the union of two subspaces Y ={(z,w ) :|z|≥| w|}
and Z ={(z,w ) : |z|≤ w}. Both are solid tori S1×D2, and Y ∩Z is a torus
S1×S1. There results a decomposition S3\K = (Y\K)∪ (Z\K). Though the
sets in this decomposition are not open, van Kampen is applicable because we can
thicken upK to a ‘rope’ R, and then take thin open neighbourhoods of Y\R and
Z\R which deformation-retract onto them. Now, Y\K deformation-retracts to
the ‘core’ circle|w| = 0, andZ\K to the core circle|z| = 0, while (Y\K)∩(Z\K)
deformation retracts to a circle K′ parallel to K inside the torus Y∩Z. Now K′
wraps twice around the core circle in Y\K, three times around that in Z\K. Van
Kampen shows that π1(S3\K) is a push-out of the diagram
Z
2
←− Z
3
−→ Z,
and this gives the presentation claimed. □
Exercise 4.1: An n-dimensional manifold is a Hausdorﬀ space X covered by open sets
homeomorphic to Rn. Let X1 and X2 be connected n-dimensional manifolds. A
connected sum X1#X2 is constructed by choosing embeddings i1 : Dn → X1 and
i2 : Dn→X2 of the closed n-disc Dn, and letting
X1#X2 = (X1\i1(intD′))∐ (X2\i2(intD′))/∼,
D′ = 1
2Dn⊂Dn, where∼ identiﬁes i1(x) with i2(x) for all x∈Sn−1 =∂D′.
(a) Prove that if n> 2 then π1(X1#X2)∼=π1(X1)∗π1(X2).
(b) Let X be an iterated connected sum of r copies of S1×Sn−1, where n≥ 3.
Compute π1(X).
(c)* Given a ﬁnitely presented group G =⟨g1,...,g k|r1,...,r l⟩, ﬁnd a connected,
compact, 4-dimensional manifold M with π1(M)∼=G. [ Hint: Start with the
case of no relations. Use the fact that ∂(S1×D3) =S1×S2 =∂(D2×S2).]
Exercise 4.2: Let K be the trefoil knot. We’ve seen that π1(S3\K) =⟨a,b|a2 =b3⟩.
How do you ﬁnd a word representing a given loop in S3\K? Find words representing a
meridian for K (i.e., the boundary of a small normal disc) and a longitude (parallel to
the knot; not unique!). Let Z be the the kernel of the homomorphism π1(S3\K)→
⟨a,b | a2,b 3⟩ which sends a to a and b to b. Show that Z ∼= Z, generated by a
longitude, and that Z is contained in the center of π1(S3\K). [ Interestingly, by an
earlier exercise we have ⟨a,b|a2,b 3⟩∼=PSL 2(Z).]

16 TIM PERUTZ
Exercise 4.3: The braid group on 3 strings . In this extended exercise (based on one in
Serre’s book Trees) we’ll see that the following ﬁve groups are isomorphic:
• π1(S3\K), where K is a (left-handed) trefoil knot.
• The group⟨a,b|a2 =b3⟩.
• The algebraic braid group on 3 strings, ⟨s,t|sts =tst⟩.
• The geometric braid group on 3 strings B3, deﬁned as the fundamental group
of the conﬁguration space C3 of 3-element subsets of C.
• π1(C2\C), where C⊂ C2 is the cuspidal cubic {(X,Y ) :X2 =Y 3}.
(a) We already know that π1(S3\K)∼=⟨a,b | a2 = b3⟩. Show that a↦→ sts,
b↦→ts deﬁnes an isomorphism
⟨a,b|a2 =b3⟩→⟨ s,t|sts =tst⟩.
(b) Take as basepoint {−2, 0, 2} ∈C3. Deﬁne loops σ and τ in X3, σ(t) =
{−1−eπit,−1 +eπit, 2} and τ(t) = {−2, 1−eπit, 1 +eπit} for t∈ [0, 1].
Let s = [σ] and t = [τ] in B3. Check that sts = tst, so that one has a
homomorphism⟨s,t|sts =tst⟩→ B3.
(b) C3 is the subspace of Sym3(C) (the quotient of C3 by the action of the
symmetric group S3 permuting coordinates) where the three points are dis-
tinct. Let Sym3
0(C) = {{a,b,c}∈ Sym3(C) : a +b +c = 0}. Show that
Sym3(C)∼= C× Sym3
0(C). Deﬁne a homeomorphism h: Sym 3
0(C)→ C2 by
sending{a,b,c} to the point (x,y ) such that
(t−a)(t−b)(t−c)≡t3 +xt +y.
Verify that the points a, b and c are distinct iﬀ 4x3 + 27y2⁄= 0. Deduce that
C3∼= C× (C2\C), hence that B3∼=π1(C2\C).
(d) Show that C2\C is homotopy-equivalent to S3\K, whence π1(C2\C)∼=
π1(S3\K).
(e)* Show that going round the full circle of homomorphisms, the resulting homo-
morphismπ1(S3\K)→π1(S3\K) is an isomorphism.

ALGEBRAIC TOPOLOGY I: FALL 2008 17
5. Covering spaces
Another basic method of computing fundamental groups is to identify the space
X as the quotient ˜X/G of a simply connected space ˜X by a discrete group G acting
freely on it by homeomorphisms. Under certain additional conditions, one then has
π1(X)∼= G (just as π1(S1) = π1(R/Z) = Z). In this lecture we will explore how
covering spaces arise in practice. We also see how a covering map gives rise to
two groups: (i) its group of deck transformations, and (ii) the image of π1 of the
covering space in π1 of the base.
Deﬁnition 5.1. A covering map is a surjective map p: ˜X→X such thatX has a
cover by open sets U with the property that p−1(U) is the disjoint union of open
sets, each of which is mapped by p homeomorphically onto U. The domain ˜X of a
covering map is called a covering space of X.
The ﬁbre F =p−1(x) is a discrete space. For an open set U as in the deﬁnition,
and x∈U, there is a homeomorphism t: p−1(U)→F×U such that pr2◦t =p as
maps p−1(U)→ U (t is called a trivialisation for p overU). Thus the ﬁbres over
points of U are all homeomorphic, and hence, if X is path-connected, all the ﬁbres
of p are homeomorphic. The covering map is trivial if there exists a trivialisation
overX.
Remark. In the theory of covering spaces it’s a useful safety precaution to assume
that all spaces are locally path connected (i.e., for any point x and any neighbour-
hood of x there is a smaller neighbourhood which is path connected).
Exercise 5.1: The following are covering maps:
(1) The quotient map R→ R/Z.
(2) The map S1→S1, eit↦→eint.
(3) The product of covering maps (e.g. Rn→ (R/Z)n = Rn/Zn).
(4) The quotient map Sn→ RPn.
Example 5.2. Let (X,x ) be a based space. A covering space Y for S1∨X can
be obtained by taking a family (Xn)n∈Z of identical copies of X, then letting Y be
the result of attaching Xn to R by identifyingx∈Xn =X ton∈ Z. The covering
map p: Y →X is given on R by the quotient map R→ R/Z =S1⊂S1∨X and
on Xn by the identiﬁcation Xn =X.
Graphs. A graph is a topological space Γ obtained by the following procedure.
One takes a discrete space V (the vertices), a set E (the edges) and for each e∈E
a map ae :{0, 1}→ V . One forms the identiﬁcation space of V ∐∐
e∈E [0, 1] in
which 0∈ [0, 1]e is identiﬁed with its image ae(0)∈V , and 1∈ [0, 1]e is identiﬁed
with ae∈V .
Example 5.3. A covering space of a graph is again a graph. For example S1∨S1
is a graph with one vertex and 2 edges. The vertex has valency 4 (i.e., 4 intervals
emanate from it). Any covering space Γ of S1∨S1 is a graph in which each vertex
has valency 4. The edges of Γ can be coloured red and blue so that each vertex
has two red and two blue intervals emanating from it. Moreover, Γ can be oriented
(i.e., each edge given a direction) so that at each vertex, exactly one red interval
is outgoing and exactly one blue interval is outgoing. Conversely any oriented,
coloured graph Γ with these properties deﬁnes a covering of S1∨S1.

18 TIM PERUTZ
5.1. Deck transformations.
Deﬁnition 5.4. Fix covering maps p1 : Y1 → X and p2 : Y2 → X. A map of
covering spaces from (Y1,p 1) to (Y2,p 2) is a map f : Y1→Y2 such thatp1◦f =p2.
A deck transformation for a covering space p: Y →X is a map of covering spaces
h from (Y,p ) to itself which is also a homeomorphism.
The inverse of a deck transformation is another deck transformation. Hence the
deck transformations form a group Aut(Y/X ).
Example 5.5. In Example 5.2, the covering space p: Y → S1∨X has Z as its
group of deck transformations. The generator is the ‘shift’ homeomorphism, acting
on R byt↦→t + 1 and sending Xn identically to Xn+1.
Coverings arise ‘in nature’ via group actions. Suppose given a continuous action
G×Y →Y of the discrete group G on the space Y .
Proposition 5.6. The quotient map q : Y →Y/G is a covering map provided the
action is a ‘covering action’: Y is covered by open sets V such that gV∩V =∅ for
all g∈G\{e}. If Y is path connected, the group of deck tranformations is G.
Proof. Given x∈ Y , take a neighbourhood V of x as in the statement. We may
assume V is connected. Let U = q(V ). Then q−1(U) is the disjoint union of the
open sets gV for g∈ G. Each is mapped bijectively to U; the map is open by
deﬁnition of the quotient topology, hence a homeomorphism. This shows that q is
a covering map.
Any g∈ G determines a deck transformation x↦→ g·x, and these give a ho-
momorphism G→ G′, where G′ is the group of deck transformations. Since the
action is free, the kernel of this homomorphism is trivial. To see that it is surjec-
tive, suppose f is a deck transformation. Pick a point y∈ Y , choose g∈ G such
that f(y) = hg·y, where hg is the action of g. Then hg−1◦f ﬁxes y. By the last
theorem, G′ acts freely, hence hg−1◦f = id, i.e. f =hg. □
5.2. Examples.
• The action of Zn on Rn by translations is a covering action (take the cover
to be by balls of radius 1 /3).
• The action of the cyclic group Z/p on S2n−1 ={z∈ Cn :|z| = 1}, where
the generator acts by scalar multiplication by e2πi/p, is a covering action.
Indeed, a non-trivial group element moves every point by a distance ≥ d
(for the Euclidean metric in Cn), where d = mink∈{1,...,p−1}|1−e2πik/p|,
hence the open sets S2n−1∩B(z;d/2) (with |z| = 1) provide a suitable
cover. The quotient L2n−1(p) =S2n−1/(Z/p) is called a lens space.
• The last example generalises: if Y is compact and simply connected, and a
ﬁnite group G acts freely on Y , then π1(Y/G)∼=G.
• If G is a compact, simply connected topological group, and Z⊂G a ﬁnite
subgroup, then the action ofZ onG is a covering action. An interesting ex-
ample is G = SU(2) and Z ={±I}⊂ G. The quotient PU (2) := SU(2)/Z
is isomorphic to SO(3). Indeed, PU(2) is the group of conformal symme-
tries of C∪{∞} , while SO(3) the group of orientation-preserving isome-
tries ofS2. These symmetries coincide under the standard homeomorphism

ALGEBRAIC TOPOLOGY I: FALL 2008 19
C∪{∞} =S2. Moreover, there is a homeomorphism
SU(2)→S3 ={(α,β )∈ C2 :|α|2 +|β|2 = 1}, (α,β )↦→
[ α β
− ¯β ¯α
]
.
The involutionA→−A on SU(2) corresponds to the antipodal map on S3,
hence PU(2)∼= RP 3.
Exercise 5.2: Do this exercise if you know the basic facts about smooth manifolds.
Suppose Y and X are smooth n-manifolds, and p: Y → X a smooth, proper map
whose derivative Dp : TxY → Tp(x)X is an isomorphism for all x∈ Y . Then p is a
(ﬁnite-sheeted) covering map.
Exercise 5.3: Show that T 2\{ 4 points} is a 2-sheeted covering of S2\{ 4 points}.
Some possible approaches are (a) a direct topological argument; (b) the Weierstrass
℘-function from complex analysis; (c) a pencil of divisors of degree 2 on an elliptic
curve.
5.3. Unique path lifting.
Lemma 5.7. Let p: ˜X → X be a covering map. Fix basepoints x ∈ X and
˜x∈p−1(x).
(1) If γ : I→ X a path, and γ(0) = x, then there is a unique path ˜γ : I→ ˜X
such that ˜γ(0) =x which lifts γ in the sense that p◦ ˜γ =γ.
(2) A homotopy Γ: I2→X lifts uniquely to a map ˜Γ: I2→ ˜X once we specify
˜Γ(0, 0).
(3) The map p∗ : π1( ˜X, ˜x)→π1(X,x ) is injective.
(4) If ˜x′ also lies in p−1(x) then p∗(π1( ˜X, ˜x′)) and p∗(π1( ˜X, ˜x)) are conjugate
subgroups of π1(X,x ).
(5) All conjugates of p∗(π1( ˜X, ˜x)) arise in this way.
Proof. (1) The proof is exactly the same as the proof of unique path lifting for
R→S1 that we gave in our proof that π1(S1) = Z. Similarly (2).
(3) If p∗(γ0) and p∗(γ1) are homotopic rel endpoints then the unique lift of the
homotopy to ˜X deﬁnes a homotopy rel endpoints between γ0 and γ1.
(4) Choose a path γ in ˜X joining ˜x′ to ˜x. Then we have
p∗(π1( ˜X, ˜x′)) = (p∗γ)·p∗(π1( ˜X, ˜x))· (p∗γ)−1.
(5) Follows from (1). □
Exercise 5.4: Write out the missing details.
Exercise 5.5: A surjective map p: Y → X which has unique path-lifting need not be
a covering map. (You may choose Y not to be locally path connected. For a harder
exercise, ﬁnd an example where Y is locally path connected.)
Let us summarise where we have got to. A covering space p: ˜X→X gives rise
(a) to a group of deck transformations Aut( ˜X/X ); and (b) to a conjugacy class of
subgroups of π1(X,x ), the images of π1( ˜X, ˜x), for basepoints ˜x∈p−1(x).
Example 5.8. If ˜X =X =S1, andp is the coveringeit↦→eint, then Aut( ˜X/X ) =
Z/n (the generator being multiplication by e2πi/n), while the image of π1( ˜X) in
π1(X) is nZ⊂ Z. We see in this example that the image of π1( ˜X) in π1(X) is
a subgroup whose index is equal to the number of sheets of the covering. It is a
normal subgroup, and the quotient group is isomorphic to Aut( ˜X/X ). If we take

20 TIM PERUTZ
˜X = R, with p: R→ R/Z = S1 the quotient map, then Aut( ˜X/X ) = Z and
π1(R) ={1}, so again Aut( ˜X/X ) =π1(X)/p∗π1( ˜X).
In the next lecture we will see that these observations generalise (except that
the image of π1( ˜X) is not always normal). In particular, if ˜X is simply connected
then Aut( ˜X/X )∼=π1(X).

ALGEBRAIC TOPOLOGY I: FALL 2008 21
6. Classifying covering spaces
In the previous lecture we introduced covering spaces. Today we classify the
covering spaces of a given space X.
The following theorem could be called the fundamental lemma of covering space
theory.
Theorem 6.1 (lifting criterion). Letp: ˜X→X be a covering map, with ˜X path-
connected, andf : B→X a map from a path-connected and locally path-connected
spaceB. Choose b∈ B and ˜x∈ ˜X such that p(˜x) = f(b). Then f lifts to a map
˜f : B→ ˜X with p◦ ˜f =f and ˜f(b) = ˜x if and only if
f∗(π1(B,b ))⊂p∗(π1( ˜X, ˜x))
in π1(X,f (b)). When it exists, the lift is unique.
Proof. If the lift exists then p∗◦ ˜f∗ =f∗, hence imf∗⊂ imp∗. Uniqueness follows
from the uniqueness of lifts of paths. We now consider existence. Take y∈B and
a path γ from b to y. We attempt to deﬁne ˜f(y) = δ(1), where δ : B→ ˜X is the
unique lift of f◦γ with δ(0) = ˜x. If this make sense and is continuous then it will
certainly fulﬁl the requirements. We need to prove that δ(1) is independent of the
choice of γ. If γ′ is another such path then γ followed by (γ′)−1 is a loop l in B.
But if f∗(π1(Y,y ))⊂ p∗(π1( ˜X, ˜x)) then l is homotopic rel endpoints to the image
of a loop ζ in ˜X. Lifting the homotopy gives a homotopy rel endpoints between ζ
and the lift of γ∗ (γ′)−1, which shows that the lift δ′ of f◦γ′ ends at the same
point as does f◦γ. Continuity of f follows from local path-connectedness of B (cf.
Hatcher). □
From now on, the base spaces of our covering maps will be assumed path-
connected and locally path-connected.
Corollary 6.2. If p1 : Y1→ X and p2 : Y2→ X are covering maps, and p(y1) =
x = p2(y2), then there exists a homeomorphism h: Y1→ Y2 with p2◦h = p1 and
h(y1) = y2 if and only if p1∗π1(Y1,y 1) = p2∗π1(Y2,y 2) in π1(X,x ). Hence two
coverings of X are isomorphic iﬀ they deﬁne conjugate subgroups of π1(X,x ).
Corollary 6.3. Any two simply connected covering spaces of X are isomorphic.
Because of this result, we shall refer to a simply connected covering space of X
as a universal cover of X.
Corollary 6.4. Ifp: ˜X→X is a universal cover, Aut( ˜X/X ) acts freely and tran-
sitively on any ﬁbre p−1(x). We obtain an isomorphism I˜x : π1(X,x )→ Aut( ˜X/X )
by ﬁxing a base-point ˜x∈p−1(x), then mapping [γ] to the unique deck transforma-
tion which sends ˜x to ˜γ(1), ˜γ being the unique lift of γ with ˜γ(0) = ˜x.
Proof. According to the lifting criterion, maps h: ˜X→ ˜X intertwiningp are nec-
essarily homeomorphisms, and they are in natural bijection with the ﬁbre p−1(x).
□
6.1. An equivalence of categories. We now formulate the classiﬁcation theorem
for coverings of X. In a nutshell, this says that isomorphism classes of path con-
nected covering spaces correspond to conjugacy classes of subgroups of π1(X,x ).
We give a sharper statement, which classiﬁes not only the coverings, but also the
maps between them.

22 TIM PERUTZ
We shall deﬁne two categories and prove their equivalence. An equivalence of
categoriesF :C→C ′ is a functor such that there exists a functor G :C′→C so
thatF◦G andG◦F are naturally isomorphic to the identity functors on C′ and
C respectively. A standard result in category theory says that F is an equivalence
provided that (i)F∗ : Hom(X,Y )→ Hom(F(X),F(Y )) is bijective for all objects
X and Y , and (ii) every object of C′ is isomorphic to some C(X).
Deﬁnition 6.5. Let G be a group. Its orbit categoryO(G) is the category whose
objects are the subgroups H ≤ G. For any H, the set G/H of left cosets of H
is a transitive G-set. We deﬁne the morphisms H → K to be maps of G-sets
G/H→G/K.
Deﬁnition 6.6. If X is a path-connected space, we deﬁne a category Cov( X)
whose objects are path-connected covering spacesp: Y →X and whose morphisms
are maps of covering spaces.
Theorem 6.7. Suppose that (X,x ) is a based space. Fixing a universal cover
p: ˜X→X and a basepoint ˜x∈p−1(X) determines an equivalence of categories
G :O(π1(X,x ))→ Cov(X).
Proof. We deﬁne a functor G :O(π1(X,x ))→ Cov(X). Thus let ˜X → X be a
simply-connected covering space, and ﬁx a basepoint ˜ x over x∈ X. Path-lifting
starting at ˜x deﬁnes an isomorphism I˜x : G→ Aut( ˜X/X ) where G = π1(X,x ).
TakeH⊂π1(X,x ), and deﬁneG(H) = ˜X/I ˜x(H). It comes with a projection map
G(H)→X, induced by p: ˜X→X, and this is certainly a covering. Its ﬁbre over x
is canonically identiﬁed withG/H, andπ1(G(X), [˜x]) maps toH under the covering
map.
Every path-connected covering Y → X is isomorphic to G(H) for some H.
Indeed, we take H to be the image of π1(Y,y ) in π1(X,x ) for some y lying over x,
cf. Corollary 6.2.
IfK is another subgroup, andf : G/H→G/K a map ofG-sets, letf(H) =γK.
Then, for all g∈ G, we have f(gH) = gγK . Notice that if h∈ H then f(hH) =
hγK = γK, hence γ−1Hγ⊂ K; conversely, an element γ such that γ−1Hγ⊂ K
deﬁnes a map of G-sets.
We shall deﬁneG(f) via the lifting criterion. We are looking for a map˜X/I ˜x(H)→
˜X/I ˜x(K) covering the identity onX. Such a map will be unique once we specify its
eﬀect on a point. For existence, take a basepoint z∈ ˜X/I ˜x(H) such that the image
of π1( ˜X/I ˜x(H),z ) in G is γ−1Hγ (cf. Lemma 5.7, (5)). By the lifting criterion,
there is a unique map of covering spaces ˜X/I ˜x(H)→ ˜X/I ˜x(K) which sends z to
[˜x]. This is G(f). It’s straightforward to check this gives a functor.
It remains to see thatG gives a bijection between morphism sets. This is another
application of the lifting criterion, but we omit the details. □
Let us spell out some aspects of this correspondence.
• At one extreme, we can consider the trivial subgroup {1} ⊂G, which
corresponds to the universal cover. At the other extreme, G⊂G gives the
trivial cover X→X.
• In general, the ﬁbre of the coveringG(H) corresponding to H≤G isG/H.
Thus ﬁnite index subgroups correspond to coverings with ﬁnite ﬁbres.

ALGEBRAIC TOPOLOGY I: FALL 2008 23
• We can recover the conjugacy class of H≤ G fromG(H) as the image of
π1(G(H)) in π1(X,x ). (To recover H on the nose, we have to remember
the basepoint [˜x] coming from ˜x∈ ˜X.)
• The normal (or regular, or Galois) coverings of X are those coverings
q : Y → X for which q∗π1(Y ) is a normal subgroup of G. Equivalently,
Aut(Y/X ) acts transitively on the ﬁbre. A normal covering determines an
actual subgroup, not just a conjugacy class of subgroups.
The similarity of the classiﬁcation theorem with the fundamental theorem of Galois
theory is not coincidental; the theory of ´ etale mapsin algebraic geometry unites
them. In particular, ﬁnite extensions of the function ﬁeld K(X) of a variety X
correspond to ﬁnite (´ etale) coverings ofX.
6.2. Existence of a simply connected covering space. Under very mild hy-
potheses, a simply connected covering exists. Assume X locally path connected.
Proposition 6.8. Suppose thatX admits a covering map p: ˜X→X from a simply
connected space ˜X. Then X is semi-locally simply connected , meaning that each
x∈ X has a path-connected neighbourhood U such that im(π1(U)→ π1(X)) is
trivial.
Proof. Let U be a neighbourhood over which p is trivial. Then any loop γ in U
lifts to a loop in ˜X, which is nullhomotopic (rel ∂I). Projecting the nullhomotopy
to X, we see that γ is nullhomotopic in X. □
Exercise 6.1: Find a path connected, locally path connected space which is not semi-
locally simply connected.
Now ﬁx a basepoint x∈X. Deﬁne ˜X as the set of homotopy classes [γ], where
γ : I→ X with γ(0) = x and [γ] its homotopy class rel ∂I . Deﬁne p: ˜X→ X to
be the evaluation map [γ]↦→ γ(1). The topology on ˜X ought to be generated by
the ‘path components’ of the sets p−1(V ) with V ⊂X open. Path components do
not make sense a priori, but we can make sense of them, via path-lifting, when V
is path connected and im(π1(V )→π1(X)) is trivial.
Proposition 6.9. If X is path-connected, locally path-connected and semi-locally
simply connected then p: ˜X→ X is a covering map and ˜X is simply connected.
Thus X admits a simply connected covering space.
Exercise 6.2: Make the topology on ˜X more precise, then prove the proposition.
Exercise 6.3: (From May’s book.) Identify all index 2 subgroups of the free group F2.
Show that they are all free groups and identify generators for them.
Exercise 6.4: (a) The universal cover of the torus T 2 is R2. Identify all the deck
transformations and hence determine (once again) the fundamental group. Which
surfaces can cover T 2? (b) Show that the Klein bottle is also covered by R2; identify
the deck transformations and hence the fundamental group.
Exercise 6.5: Let p: Y →X be a covering (with Y path connected and X locally path
connected) such that p∗π1(Y,y ) = H⊂ G = π1(X,p (y)). Show that Aut( ˜X/X )∼=
(NGH)/H, where NGH ={g∈G :gHg−1 =H}.
For the next exercise, you may use the following fact: the quotient SU(2) /{±I}
is isomorphic, as a topological group, to SO(3).

24 TIM PERUTZ
Exercise 6.6: Deﬁne a regular tetrahedron as a set of four distinct, unordered, equidis-
tant points on S2⊂ R3. Let T be the space of regular tetrahedra. (a) Show that
π1(T ) has a central subgroup Z∼= Z/2 such that π1(T )/Z∼=A4. (b) Identify several
(at least 5) pairwise non-isomorphic, path connected covering spaces of T , describing
them geometrically. (c) Show that the fundamental group of the space P of regular
icosahedra (unordered collections of 20 distinct points on S2 forming the vertices of a
regular icosahedron) has order 120, but that the abelianization π1(P)ab has order at
most 2. (In fact it is trivial.) [Recall that the icosahedral group A5 is simple.]
Exercise 6.7: Rotation about a ﬁxed axis, by angles increasing from 0 up to 2π, deter-
mines a loop γ in SO(3). Show that γ∗γ is nullhomotopic.

ALGEBRAIC TOPOLOGY I: FALL 2008 25
II. Singular homology theory
7. Singular homology
We explain a fundamental construction of algebraic topology—singular homology.
We compute the 0th homology groups in terms of the path components of the space,
and show that π1 maps onto the ﬁrst homology group.
Precursors of homology theory go back to the 18th Century and Euler’s formula
v−e +f = 2 for the numbers of vertices, edges and faces of a convex polyhedron.
Its systematic development began with Poincar´ e in the 1890s. The deﬁnition of
singular homology we shall give is due to Eilenberg (1944), but it rests on ﬁfty
years of exploration and reﬁnement by many mathematicians. Every aspect of it is
the result of a gradual process of experiment and abstraction. It is perfectly simple
and, at ﬁrst, perfectly mysterious.
7.1. The deﬁnition. The geometricn-simplex is
∆n ={(x0,...,x n)∈ [0, 1]n+1 :
∑
xi = 1}.
It is the convex hull [v0,...,v n] of the points vi = (0,..., 0, 1i, 0,..., 0).
Deﬁne the ith face map
δi : ∆n−1→ ∆n, (x0,...,x n−1)↦→ (x0,...x i−1, 0,xi,...,x n−1).
It is homeomorphism onto the face [v0,..., ˆvi,...,v n].
An n-simplex in the space X is a continuous map σ : ∆n→ X. Let Σ n(X) be
the set of all n-simplices. Deﬁne the nth singular chain group Sn(X) as
Sn(X) = ZΣn(X),
the free abelian group generated by Σ n(X). It is the group of ﬁnite formal sums∑
iniσi with ni∈ Z and σi∈ Σn(X). For n >0, deﬁne ∂n : Sn→ Sn−1 as the
Z-linear map such that
∂nσ =
n∑
i=0
(−1)i(σ◦δi), σ ∈ Σn(X).
In alternative notation, ∂nσ =∑n
i=0 (−1)i(σ|[v0,...,ˆvi,...,vn]).
Lemma 7.1. ∂n◦∂n+1 = 0.
Proof. This is a consequence of the following relations among the face maps:
δi◦δj =δj◦δi−1, j <i.
For anyn + 1-simplexσ, we have
∂n◦∂n+1σ =
∑
0≤j≤n
∑
0≤i≤n+1
(−1)i+jσ◦δi◦δj
=
∑
0≤j<i≤n+1
(−1)i+jσ◦δi◦δj +
∑
0≤i≤j≤n
(−1)i+jσ◦δi◦δj
=
∑
0≤j<i≤n+1
(−1)i+jσ◦δj◦δi−1 +
∑
0≤i≤j≤n
(−1)i+jσ◦δi◦δj
=
∑
0≤k≤l≤n
(−1)k+l+1σ◦δk◦δl +
∑
0≤i≤j≤n
(−1)i+jσ◦δi◦δj
=0.

26 TIM PERUTZ
Since simplices generate Sn+1(X), the result follows. □
It is convenient to let ∂0 : S0(X)→ 0 be the zero-map. The nth singular homol-
ogy of X is the abelian group
Hn(X) := ker∂n/ im∂n+1.
Elements of ker ∂n are called n-cycles; elements of im ∂n+1 are n-boundaries. By
the lemma, an n-boundary is an n-cycle, and the nth homology is the group of
n-cycles modulo n-boundaries.
In future lectures we will develop these groups systematically. Today we will
look only at the zeroth and ﬁrst homology groups.
7.2. The zeroth homology group.
Proposition 7.2. The map ε: S0(X)→ Z,ε(∑niσi) =∑ni induces a surjection
H0(X)→ Z provided only that X is non-empty. When X is path-connected, this
map is an isomorphism.
Proof. We have to show that ε descends to H0(X) = S0(X)/ im∂1. If τ is a 1-
simplex then ∂τ = τ◦δ0−τ◦δ1. Thus ε(∂τ ) = 1− 1 = 0. Hence ε(imδ1) = 0,
and ε descends to H0(X). For any 0-simplex σ, ε(nσ) =n, so ε is surjective. If X
is path-connected, take s =∑niσi∈ kerε. We may assume ni =±1 for all i. The
number of + and − signs is equal, so we may partition the 0-simplices into pairs
(σi,σj) with ni = 1 and nj =−1. But σi−σj is the boundary of a 1-simplex (i.e.,
of a path), since X is path-connected. Hence s∈ im∂1. □
Exercise 7.1: Show that, in general, Hn(X) =⨁
Y∈π0(X)Hn(Y ), where π0(X) is the
set of path-components of X. Thus H0(X)∼= Zπ0(X).
So, whilst S0(X) is typically very large (often uncountably generated), H0(X)
is ﬁnitely generated for all compact spaces.
7.3. The ﬁrst homology group. There’s a homeomorphism I→ ∆1 given by
t↦→tv1+(1−t)v0. Thus a pathγ : I→X deﬁnes a 1-simplex ˆγ. When γ(0) =γ(1),
ˆγ is a 1-cycle.
Lemma 7.3. Fix a basepoint x∈X. The map γ↦→ ˆγ induces a homomorphism
h: π1(X,x )→H1(X).
Proof. A constant loop is the boundary of a constant 2-simplex. Loops which are
homotopic rel endpoints give homologous 1-simplices (by subdividing a square into
two triangles and using the fact that constant loops are boundaries). Thus h is
well-deﬁned. If f and g are composable paths, the composition f∗g maps under
h to ˆf + ˆh: deﬁne a 2-simplex σ = (f∗g)◦p: ∆2→X, where p is the projection
[v0,v 1,v 2]→ [v0,v 2],t0v0 +t1v1 +t2v2↦→t1v1 +t2v2. We have ∂σ = ˆg− ˆf∗g + ˆf.
□
The map h is sometimes called the Hurewicz map.
Proposition 7.4. The kernel of the Hurewicz map h: π = π1(X,x )→ H1(X)
contains the commutator subgroup [π,π ], and hence h induces a homomorphism
πab :=π/[π,π ]→H1(X).
When X is path-connected,h is surjective.

ALGEBRAIC TOPOLOGY I: FALL 2008 27
Proof. Sinceh is a homomorphism,h(f·g·f−1·g−1) =h(f)+h(g)−h(f)−h(g) = 0.
Thus [π,π ]⊂ kerh. To obtain surjectivity in the path-connected case, note that
the group of 1-cycles is generated by loops, where a loop is a 1-cycle ±∑
i∈Z/Nσi
with δ1σi +δ0σi+1 = 0 for all i∈ Z/N. Thus it suﬃces to show that any loop lies
in the image of h. But any loop is homologous to a loop based at x (insert a path
γ from x to σ0(0), and γ−1 from σN−1(1) to x). The composition of all the paths
making up the based loop is homologous to their sum, and it lies in im( h). □
Example 7.5. Any simply connected space X has H1(X) = 0.
Remark. By analogy, one can look at the groupH2(X)/s(X), wheres(X)⊂H2(X)
is the subgroup generated by the ‘spherical cycles’: those represented by a map from
a tetrahedron (built from four 2-simplices) into X. This group is zero when X is
simply connected. A theorem of Hopf [Comment. Math. Helv. 14, (1942), 257–309]
says that, for a general path-connected X, H2(X)/s(X) depends only on π1(X).
It is naturally isomorphic to a group which is now understood as H2(π1(X)), the
second group homology ofπ1(X). Indeed, group homology was developed partly in
response to Hopf’s theorem. See, e.g., Brown, Cohomology of groups (GTM 87).

28 TIM PERUTZ
8. Simplicial complexes and singular homology
We show that a singularn-cycle can be represented by a map from ann-dimensional
∆-complex. We complete our calculation of H1 in terms of π1.
8.1. ∆ -complexes.
Deﬁnition 8.1. A ∆-complex (or semi-simplicial complex) is a spaceX equipped
with sets Sn, empty for n≫ 0, and for each n and each α∈ Sn a continuous maps
σn
α : ∆n→ X. We require that (i) σn
α is injective on int(∆n), and X (as a set) is
the disjoint union over n and α of the images σn
α(int(∆n); (ii) when n > 0, the
restriction to a face, σn
α◦δi, is equal to σn−1
β for some β∈ Sn−1; and (iii), a set
U⊂X is open iﬀ (σn
α)−1(U) is open for all n and all α.
There are a number of connections between ∆-complexes and singular homology.
If a space is given the structure of a ∆-complex, there is a distinguished sub-space
Ssimp
n (X) ⊂ Sn(X), spanned by the n-simplices σn
α. One has ∂(Ssimp
n )(X) ⊂
Ssimp
n−1 (X), so it makes sense to form the simplicial homology group
Hsimp
n (X) = ker(∂n : Ssimp
n (X)→Ssimp
n−1 (X))
im(∂n+1 : Ssimp
n+1 (X)⊂Ssimp
n (X)
.
This comes with a natural homomorphism Hsimp
n (X)→ Hn(X), induced by the
inclusion Ssimp
n (X)→Sn(X).
Exercise 8.1: Think of S2 as a tetrahedron, i.e., a ∆-complex with four 2-simplices, six
1-simplices and four 0-simplices. Show that for this structure
Hsimp
0 (S2) = Z, H simp
1 (S2) = 0, H simp
2 (S2) = Z, H simp
>2 (S2) = 0.
Exercise 8.2: Compute Hsimp
∗ for the spaces T 2, RP 2 and K2, each thought of as a
∆-complex with two 2-simplices (and some 1- and 0-simplices).
Remark. You may like to keep in mind the following fact, even though it’s not
part of the logical development of this course: the map Hsimp
n (X)→ Hn(X) an
isomorphism. So, for example, the homology of a ∆-complex is ﬁnitely generated.
The following simple observation gives some geometric insight into singular ho-
mology.
Lemma 8.2. Let z be a singular n-cycle in X, so ∂nz = 0 . Write it as z =∑N
i=1ϵiσi with ϵi = ±1. Then there is an ∆-complex Z, with precisely N n-
simplices (τ1,...,τ N) and no higher-dimensional simplices, and a map f : Z→X,
such that (i) ∑ϵiτi represents a simplicial n-cycle for Z, and (ii) σi = f◦τi for
eachi.
Proof. Since ∂nz = 0, each face σi◦δj must cancel with another face σ′
i◦δj′.
Thus, we can partition the set of faces of all σi into pairs. We deﬁne a ∆-complex
Z by gluing N n-simplices together along their faces, paired up in the way just
determined. This has the right properties. □
More generally, if∂nz =y, we can build a ∆-complex and a map from it into X
so that the summed boundary of the n-simplices in the complex maps to X as the
cycle y.

ALGEBRAIC TOPOLOGY I: FALL 2008 29
8.2. The Hurewicz map revisited. Last lecture, we introduced the ‘Hurewicz
map’ h: π1(X)ab → H1(X) and proved its surjectivity (assuming X path con-
nected). We did not analyse its kernel. We now ﬁnish the job.
Theorem 8.3. WhenX is path-connected, the Hurewicz maph: π1(X)ab→H1(X)
is an isomorphism.
Example 8.4. • Recall thatπ1(S1)∼= Z. Since this group is already abelian,
H1(S1)∼= Z also.
• Recall that π1(T 2) =π1(T 2)ab∼= Z2, π1(K2)ab∼= Z⊕ Z/2 and π1(RP 2) =
π1(RP 2)ab∼= Z/2, where T 2 is the 2-torus, K2 the Klein bottle, and RP 2
the real projective plane.
• Recall that the closed, oriented surface Σ g of genus g has
π1(Σg)∼=⟨a1,...,a g;b1,...,b g| [a1,b 1]··· [ag,bg]⟩.
ThusH1(Σg)∼= Z2g, generated by the classes of a1,...,a g and b1,...,b g.
Proof of the theorem. Take a loop γ∈ kerh: say γ =∂2β. We will show that [γ] is
a product of commutators in π, hence lies in [ π,π ]. We have already proved that
h is onto, so this will complete the proof. But we can build from the 2-chain β a
2-dimensional ∆-complex K, and a map f : K→X, with the following properties:
ifz is the sum of the 2-simplices, then∂2z =σ for a 1-simplexσ such thatf◦σ =γ.
Moreover, the image of σ in K is a loop ∂K. It suﬃces, then, to show that ∂K
is in the commutator subgroup of π1(K,b ) (for the obvious basepoint b∈∂K), for
then the corresponding result will hold in X just by applying f. Thus we deduce
the theorem from the following lemma. □
Lemma 8.5. Let K be a compact, connected, 2-dimensional ∆-complex. Suppose
z is the sum of the 2-simplices, and that ∂2z = ∑N
i=1σi for some 1-simplices σi
such that σi(1) = σi+1(0), i∈ Z/N. Fix a basepoint b; take it to be a vertex lying
on ∂K . Then ∂2z represents an element of π =π1(K,b ). This element lies in the
normal subgroup [π,π ] generated by commutators.
Proof. First observe (exercise!) that in general, if we have a free homotopy through
loops γt : S1→ X, then we have two fundamental groups π = π1(X,γ 0(1)) and
π′ =π1(X,γ 1(1)); and [γ0]∈ [π,π ]⊂π iﬀ [γ1]∈ [π′,π′]⊂π′.
We now proceed by induction on the number of 2-simplices. The lemma is
obvious when there is only one 2-simplex. When there is more than one, remove a
2-simplexσ adjacent to the boundary which has the basepoint as one of its vertices,
so as to create a new ∆-complex K’ which again satisﬁes the hypotheses(!). Pick a
new basepoint b′ on ∂K′ which was one of the vertices of σ. By induction, ∂K′ is
a product of commutators in π1(K′,b′), hence in π1(K,b′). But ∂K is homotopic
through loops to ∂K′, so the result follows from our observation. □
Remark. The lemma is connected with the geometric interpretation of the algebraic
notion of ‘commutator length’. In general, for a group π, the commutator length
cl(γ) ofγ∈ [π,π ] is the least integer g such thatγ is the product of g commutators
in π. If π = π1(X,x ), then one can show that cl(γ) is the minimal genus g of a
compact oriented surfaceK boundingγ. Here by a compact oriented surface I mean
a ∆-complex K, equipped with a map f : K→X, which satisﬁes the conditions of
the lemma and which is locally homeomorphic to R2. The genus of K is half the
rank of Hsimp
1 (K).

30 TIM PERUTZ
9. Homological algebra
Having introduced singular homology, we now need an adequate algebraic lan-
guage to describe it.
9.1. Exact sequences. We shall work with modules over a base ring R, which
we will assume to be commutative and unital. We write 0 for the zero-module. A
sequence of R-modules and linear maps
A
a
→B
b
→C
is exact if kerb = ima. A longer sequence of maps is called exact if it is exact at
each stage.
• 0→B
b
→C is exact iﬀ b is injective.
• A
a
→B→ 0 is exact iﬀ a is surjective.
• 0→A
a
→B→ 0 is exact iﬀ a is bijective, i.e., iﬀ a is an isomorphism.
• Exact sequences of the form
0→A
a
→B
b
→C→ 0,
are called short exact sequences . In such a sequence, coker a = B/ ima =
B/ kerb. But b induces an isomorphism B/ kerB→ imb = C. Thus a is
injective with cokernel C, while b is surjective with kernel A.
• A short exact sequence is called split if it satisﬁes any of the following
equivalent conditions: (i) there is a homomorphism s: C→ B with bs =
idC; (ii) there is a homomorphismt: B→A witht◦a = idA; or (iii) there is
an isomorphismf : B→A⊕C so thata(x) =f(x, 0) andb(f−1(x,y )) =y.
• If the six-term sequence
0→A
a
→B
b
→C
c
→D→ 0
is exact then a induces an isomorphism A∼= kerb while c induces an iso-
morphism D∼= cokerb.
Exact sequences are useful because if one has partial information about the groups
and maps in a sequence (in particular, the ranks of the groups) then exactness helps
ﬁll the gaps.
Example 9.1. Suppose one has an exact sequence of Z-modules
0→ Z
i
→A
p
→ Z/2→ 0.
What can one say about A (and about the maps)? Choose x∈ A with p(x)⁄= 0.
Then 2x∈ kerp = imi. There are two possibilities:
(i) 2x = i(2k) for some k. Let x′ = x−i(k). Then 2 x′ = 0. We can then
deﬁne a homomorphism s: Z/2→ A with p◦s = id by sending 1 to x. Thus the
sequence splits, and so may be identiﬁed with the ‘trivial’ short exact sequence
0→ Z→ Z/2⊕ Z→ Z/2→ 0.
(ii) 2x = i(2k + 1) for some k. Let x′ = x− i(k). Then 2 x′ = i(1) and
p(x′) = p(x) ⁄= 0. Given y ∈ A, either y = i(m) for some m, in which case
y = 2mx′, or else y−x′ =i(m) for some m, in which case y = (2m + 1)x′. Thus
A = Zx′. Moreover, x′ has inﬁnite order (since Zx′ contains imi). So the sequence
may be identiﬁed with the sequence 0 → Z→ Z→ Z/2→ 0, in which the map
Z→ Z is multiplication by 2 and Z→ Z/2 is the quotient map.

ALGEBRAIC TOPOLOGY I: FALL 2008 31
9.2. Chain complexes. A chain complex over R is a collection {Cp}p∈Z of R-
modules, together with linear maps dp : Cp→Cp−1, called diﬀerentials, satisfying
dp−1◦dp = 0. We write C∗ for the sum ⨁
pCp, which is a graded module, and
d =⨁dp : C∗→ C∗ (an endomorphism map which lowers degree by 1, satisfying
d2 = 0). We deﬁne the homology
H(C∗) = kerd/ imd.
Notice that kerd =⨁
p kerdp and imd =⨁ imdp, so H(C∗) =⨁
pHp(C∗), where
Hp(C∗) = kerdp/ imdp+1.
Elements of Zp(C) := kerdp are called p-cycles; elements of Bp(C) := imdp+1,
p-boundaries. If H(C∗) = 0, we say that C is acyclic.
A chain map from (C∗,dC) to ( D∗,dD) is a linear map f : C∗ → D∗ such
that f(Cp)⊂ Dp and dD◦f = f◦dC. A chain map induces homomorphisms
Hp(f): Hp(C∗)→Hp(D∗). A chain map which induces an isomorphism on homol-
ogy is called a quasi-isomorphism.
9.2.1. Chain homotopies. We need a criterion for two chain maps f and g : C∗→
D∗ to induce the same map on homology. For this we introduce the notion of
chain homotopy . A chain homotopy from g to f is a collection of linear maps
hp : Cp→Dp+1 such that
dD◦hp +hp−1◦dC =f−g.
If x∈ Zp(C) then f(x) = g(x) +dD(hpx), hence [f(x)] = [g(x)]∈ H(D∗). If, for
example, there is a chain homotopy fromf : C∗→C∗ to the identity map idC, then
f is a quasi-isomorphism. If there is a null-homotopy, i.e., a chain homotopy from
f to the zero-map, then f induces the zero-map on homology. If both possibilities
occur then C∗ must be acyclic, i.e., H∗(C) = 0.
9.2.2. Short and long exact sequences. We study the eﬀect of passing to homology
on a short exact sequence
0→A∗
a
→B∗
b
→C∗→ 0
of chain complexes and chain maps.
Lemma 9.2. (i) The sequence Hp(A)
Hp(a)
→ Hp(B)
Hp(b)
→ Hp(C) is exact.
(ii) Takex∈Ap with dAx = 0. Then [x]∈ kerHp(a) iﬀ there exists y∈Bp+1
such that a(x) =dBy.
(iii) Takez∈ Cp with dCz = 0. Then [z]∈ imHp(b) iﬀ there exists y∈ Bp−1
such that b(y) =z and dBy = 0.
Proof. (i) Take y∈ Bp with dBy = 0 and b(y) = dCz for some z∈ Cp+1. Then
z = b(y′), say, and b(y−dBy′) = dC(z−b(y′)) = 0, so y−dBy′ = a(x) for some
x∈Ap, i.e. y∈ ima + imdB, as required.
(ii) is obvious, and (iii) almost so. □
Points (ii) and (iii) can be pushed considerably further. Deﬁne the connecting
homomorphism
δ : Zp(C)→Hp−1(A)
as follows:
δ(z) = [x] when there exists y∈Bp with b(y) =z and a(x) =dBy.

32 TIM PERUTZ
Lemma 9.3. δ is a well-deﬁned map.
Proof. Note ﬁrst that, since b is onto, there is some y withb(y) =z; and b(dBy) =
dC(by) = dCz = 0, hence dBy ∈ kerb = im a. Thus suitable y and x exist.
Moreover,x is determined by y, because of the injectivity of a. If b(y) =b(y′) =z
theny−y′∈ kerb = ima, soy =y′+a(x′) for somex′, anddBy =dBy′+dBa(x′) =
dBy′ +a(dAx′). Thus replacing y by y′ has the eﬀect of replacing x by x +dAx′,
so the homology class [x] is well-deﬁned. □
Linearity of δ is clear. Note that δ maps Bp(C) to 0, and hence descends to a
map on homology,
δ : Hp(C)→Hp−1(A).
Theorem 9.4. The short exact sequence of chain complexes
0→A∗
a
→B∗
b
→C∗→ 0
induces an exact sequence
···→ Hp(A)
Ha
→ Hp(B)
Hb
→Hp(C)
δ
→Hp−1(A)
Ha
→ Hp−1(B)
Hb
→Hp−1(C)→··· .
Proof. We have already established exactness atHp(C) and well-deﬁnedness of the
connecting map δ.
Exactness at Hp(C): Say [z]∈ kerδ. This means that z = b(y) and a(dAx′) =
dBy for some x′∈Ap. Then dB(y−ax′) = 0, and b(y−ax′) =z, so z∈ imb.
Exactness at Hp−1(A): Let x∈ Zp−1(A), and suppose that ax = dBy. Then
[x] =δ(b(y)). □
Exercise 9.1: We consider chain complexes (C∗,δ ) over a ﬁeldk such that dimkH∗(C)<
∞. The Euler characteristic of C∗ is then deﬁned as the alternating sum
χ(C∗) =
∑
p
(−1)p dimkHp(C).
(i) Show that when ∑
p dimkCp <∞, one has χ(C∗) =∑
p (−1)p dimkCp.
(ii) Show that if
···→ Cp→Cp−1→Cp−2→...
is an exact sequence, and ∑
p dimCp <∞, then ∑ (−1)p dimCp = 0.
Exercise 9.2: A collection C of Z-modules is called a Serre class if for every short exact
sequence 0→ A→ B→ C→ 0 such that two out of the three Z-modules A, B,
C are in C, the third is in C also. Fix a prime p∈ Z. Identify which of the following
properties of Z-modulesM deﬁne Serre classes: (a) M is torsion; (b) M is torsion-free;
(c) M is torsion but has no p-torsion; (d) every element of M has p-power order; (e);
every element of M is divisible by p; (f) every M is ﬁnitely generated. (*) What if we
replace M by an arbitrary commutative ring R (and p by a prime of R?).
Exercise 9.3: Prove or give a counterexample: given two path connected open sets U
andV whose union is X and whose intersection U∩V is path connected, there exists
a short exact sequence of abelian groups
0→H1(U∩V )→H1(U)⊕H1(V )→H1(X)→ 0.
Exercise 9.4: If a: A∗→ B∗ is a chain map its mapping cone , denoted cone (a)∗, is
the complex
cone(a)n =An−1⊕Bn

ALGEBRAIC TOPOLOGY I: FALL 2008 33
with diﬀerential dcone(a)(x,y ) =−dAx +a(x) +dBy (check that this squares to zero).
The point of this construction is to convert questions about chain maps to questions
about chain complexes.
(i) Show that the induced map on homology, a∗ = H(a): H∗(A)→ H∗(B), is an
isomorphism iﬀ H(cone(a)∗) = 0.
(ii) Construct a short exact sequence
0→B∗→ cone(a)∗→A∗−1→ 0,
and identify the connecting map in the resulting long exact sequence.
(iii) Show that to give a map of complexes f = (h,b ): cone(a)∗→C∗ is to give a
chain map b: B∗→C∗ and a chain-homotopy h from b◦a to the zero map.
(iv) Show that if the map f from (iii) induces an isomorphism on homology then
there is a long exact sequence
···→ Hn(A)
a∗
→Hn(B)
b∗
→Hn(C)→Hn−1(A)
a∗
→Hn−1(B)
b∗
→Hn−1→...
Exercise 9.5: (*) If a: A∗ → B∗ and b∗ : B∗ → C∗ are chain maps, what can we
say about cone (b◦a)? Show how to arrange the six groups H∗(A), H∗(B), H∗(C),
H∗(cone(a)),H∗(cone(b)) andH∗(cone(ba)) as the vertices of an octahedral diagram
of maps. Four of the faces should be commuting triangles, the other four exact triangles
(i.e., long exact sequences visualised as triangles). The last of these triangles is a long
exact sequence
···→ Hp(cone(a))→Hp(cone(ba))→Hp−1(cone(b))→....
The hard part of the exercise is constructing this triangle and proving its exactness.
[Hint: deﬁnef : cone(a)→ cone(ba) byf(x,y ) = (x,by ). There is a natural inclusion
i: cone(b)→ cone(f). Show that i is a chain-homotopy equivalence.]
This exercise shows shows that the derived category of the abelian category of chain
complexes satisﬁes Verdier’s ‘octahedral axiom’ for triangulated categories.

34 TIM PERUTZ
10. Homotopy invariance of singular homology
We prove that singular homology is an invariant of homotopy type. We thereby
we compute the homology of contractible spaces.
Proposition 10.1. Let∗ denote a one-point space. Then Hi(∗) = 0 for all i> 0.
Proof. There is exactly one simplex σi in each dimension. Thus the singular com-
plex is
···→ Zσ2→ Zσ1→ Zσ0→ 0.
Since σn◦δi =σn−1, the boundary operator is given by
∂nσn =
n∑
i=0
(−1)iσn−1 = 1
2[1 + (−1)n]σn−1.
Thus the complex is
···→ Zσ3
0
→ Zσ2
1
→ Zσ1
0
→ Zσ0→ 0.
So ker∂i = 0 when i is even and positive; and when i is odd, ∂i+1 is onto. Thus
Hi(∗) = 0 when i> 0. As expected, we ﬁnd H0(∗)∼= Z. □
Maps between spaces introduce homomorphisms between homology groups. Given
f : X→Y , deﬁne f# : Sn(X)→Sn(Y ) by
f#(σ) =f◦σ.
It is clear that this is a chain map: ∂nf# =f#∂n. Thus there is an induced map
f∗ =Hn(f): Hn(X)→Hn(Y ).
Notice that if g : Y → Z is another map then ( g◦f)# = g#◦f#, and hence
(g◦f)∗ =g∗◦f∗.
Remark. In categorical language, we can express this by saying that Hn deﬁnes a
functor from the category Top of topological space and continuous maps to the
category Ab of abelian groups and homomorphisms. That is, Hn associates with
each spaceX an abelian groupHn(X); with each mapf : X→Y a homomorphism
Hn(f): Hn(X)→ Hn(Y ); and the homomorphism Hn(g◦f) associated with a
composite is the composite Hn(g)◦Hn(f). Moreover, identity maps go to identity
maps.
Theorem 10.2. Suppose that F is a homotopy from f0 : X→ Y to f1 : X→ Y .
The homotopy then gives rise to a chain homotopy PF : S∗(X)→ S∗+1(Y ) from
(f0)# to (f1)#, that is, a sequence of maps PF
n : Sn(X)→Sn+1(Y ) such that
∂n+1◦PF
n +PF
n−1◦∂n = (f1)#− (f0)#.
HenceHn(f0) =Hn(f1).
Corollary 10.3. If f : X→ Y is a homotopy equivalence then Hn(f) is an iso-
morphism for all n.
Corollary 10.4. A contractible space X has Hi(X) = 0 for all i> 0.
Remark. We can express the theorem in categorical language. Deﬁne a category
hTop whose objects are topological spaces, and whose morphisms are homotopy
classes of continuous maps. Then singular homology deﬁnes a sequence of functors
Hn : hTop→ Ab.

ALGEBRAIC TOPOLOGY I: FALL 2008 35
To prove the theorem, we begin with low-dimensional cases, because there the
geometry is transparent.
Proof of the theorem when n is 0 or 1. First, given a 0-simplex ρ: ∆0→ X, note
that we have a 1-simplex PF
0 (ρ) :=F◦ρ: I = ∆1→Y , and ∂1(PF
0 (ρ)) =f1◦ρ−
f0◦ρ.
Next, consider some 1-simplex σ : ∆1→X. We want to examine f1◦σ−f0◦σ.
Since ∆1 =I, our homotopy F deﬁnes a map on from the square ∆ 1×I to Y ,
F◦ (σ× idI): ∆ 1×I.
But the square is a union of two 2-simplices along a common diagonal. To notate
this, let the bottom edge be ∆1×{0} = [v0,v 1], and the top edge ∆1×{1} = [w0,w 1].
Thus the square is the convex hull [v0,v 1,w 0,w 1] of its four vertices. It is the union
of the two triangles [v0,v 1,w 1] and [v0,w 0,w 1] along the common edge [v0,w 1]. Note
that by expressing these triangles as convex hulls, we implicitly identify them with
the geometric 2-simplex ∆ 2: for the ﬁrst of them, say, the point t0v0 +t1v1 +t2w1
corresponds to the (t0,t 1,t 2)∈ ∆2.
Now deﬁne a 2-chain PF
1 (σ) by applying F to each of these two simplices:
PF
1 (σ) =F◦ (σ× idI)|[v0,w0,w1]−F◦ (σ× idI)|[v0,v1,w1]
We have
∂2PF
1 (σ) =f1◦σ−f0◦σ +PF
0 (∂1σ) :
the ﬁrst terms come fom the top of the square, the second term from the bottom,
and the third from the two other sides. Thus, deﬁning PF
1 : S1(X)→ S0(Y ) and
PF
2 : S2(X)→S1(Y ) by linearly extending the deﬁnitions from simplices to singular
chains, we have that
∂2PF
2 +PF
1 ∂1 = (f1)#− (f0)#.
□
Proof of the theorem in arbitrary dimensions. We proceed in the same way. For an
n-simplex σ : ∆n→X, we have a map
F◦ (σ× idI): ∆n×I→Y
deﬁned on the ‘prism’ ∆n×I, and we want to express this as a sum ofn+1-simplices.
To do this, we think of the prism as the convex hull [ v0,...,v n,w 0,...,w n], where
vi is the ith vertex of ∆×{ 0} = ∆, and wi the ith vertex of ∆×{ 1} = ∆. Then
one can check (as Hatcher does) that
∆×I =
n⋃
i=0
[v0,...,v i,wi,wi+1,...,w n],
that each [v0,...,v i,wi,wi+1,...,w n] is an n + 1-simplex, and that these simplices
intersect along common faces. This gives ∆ ×I the structure of a ∆-complex.
We now deﬁne
PF
n (σ) =
n∑
i=0
(−1)iF◦ (σ× idI)|[v0,...,vi,wi,wi+1,...,wn],
extending by linearity to get a map PF
n : Sn(X)→ Sn+1(Y ). The boundary of
Pn(σ) should then consist (geometrically and hence algebraically) of f1◦σ, f0◦σ
and Pn−1(∂σ). Since we did not actually verify that we had a ∆-complex, let us
instead verify algebraically that PF deﬁnes a chain homotopy.

36 TIM PERUTZ
We have
∂n+1PF
n (σ) =
∑
j≤i
(−1)i+jF◦ (σ× idI)|[v0,...ˆvj...,vi,wi,...,wn]
+
∑
l>k
(−1)k+lF◦ (σ× idI)|[v0,...,vk,wk,... ˆwl−1...,wn].
The term with j =i = 0 in the ﬁrst sum is
F◦ (σ× idI)|[w0,...,wn] =f1◦σ.
The term with l =k + 1 =n in the second sum is
−F◦ (σ× idI)|[v0,...,vn] =−f0◦σ.
Next we look for the cancelling pairs of faces which we expect geometrically. These
appear as the equality of [v0,..., ˆvi,wi,...,w n] = [v0,...,v i−1, ˆwi−1,...,w n]. Apart
from the exceptional cases i =j = 0 and l =k + 1 =n, the j =i term in the ﬁrst
sum cancels with the l =k + 1 term in the second sum where k =i− 1. So, at this
point we have
∂n+1PF
n (σ) =f1◦σ−f0◦σ
+
∑
j<i
(−1)i+jF◦ (σ× idI)|[v0,...ˆvj...,vi,wi,...,wn]
+
∑
l>k
(−1)k+l+1F◦ (σ× idI)|[v0,...,vk,wk,... ˆwl...,wn].
We want the two sums here to total −PF
n (∂nσ). But if j <i, then
PF
n (σ◦δi) =
∑
j
(−1)j+i−1(σ× idI)|[v0,...ˆvj...vi,wi,...,wn].
If j≥i then instead
PF
n (σ◦δi) =
∑
j
(−1)j+i(σ× idI)|[v0,......,vi,wi,... ˆwj−1...,wn].
So the desired equality does indeed hold. □
Exercise 10.1: Suppose that X is a subspace of Rn such that there is a mapr : Rn→X
with r|X = idX. Show that X has the homology of a point.
Exercise 10.2: Compute the ﬁrst homology group H1 of the n-torusTn = (S1)n. Use
this to construct a surjective homomorphism G→ GLn(Z), where G is the group of
homotopy equivalences Tn→Tn. Show that when n = 1 its kernel consists of maps
homotopic to the identity.
Exercise 10.3: (*) The model Dehn twist on the annulus A = [−1, 1]× (R/Z) is the
homeomorphismt: A→A of form (s,t )↦→ (s,t + (s + 1)/2). A Dehn twist along an
embedded circle C in a surface S is a homeomorphism S→S obtained by identifying
a neighbourhood of C with A, and ‘transplanting’ a model Dehn twist into S. (I am
being careless about right/left-handed twists.)
Let Σ be a genus 2 surface, and C⊂ Σ a circle dividing it into two 1-holed tori.
Show that if f is a Dehn twist along C then f∗ acts on H1(Σ) as the identity, but f
is not homotopic to the identity map.

ALGEBRAIC TOPOLOGY I: FALL 2008 37
11. The locality property of singular chains
There is a ‘locality’ theorem for singular chains, reminiscent of the proof of van
Kampen’s theorem on π1. This may be regarded as the technical core of singular
homology theory. We do not give a complete proof, but we reduce it to a lemma
concerning the geometric p-simplex ∆p.
Deﬁnition 11.1. An excisive triad is a triple (X;A,B ) with X a space and A,B
subspaces of X such that X = int(A)∪ int(B).
Theorem 11.2 (locality for singular chains) . Suppose (X;A,B ) is an excisive
triad. Let Sn(A +B) denote the subgroup of Sn(X) generated by the images of
Σn(A) and Σn(B). Notice that it is a subcomplex. Then the inclusion map
i: S∗(A +B)→S∗(X)
is a quasi-isomorphism.
(Hatcher proves that i is a chain-homotopy equivalence, but this is more than
we need.)
Setting up the proof. Form the quotient complex Q∗ = S∗(X)/ im(i). Then we
have a short exact sequence
0→S∗(A +B)
i
→S∗(X)→Q∗→ 0
and hence a long exact sequence of homology groups
···→ Hp+1(Q∗)→Hp(S∗(A +B))
i∗
→Hp(X)→Hp(Q∗)→...
The theorem asserts that i∗ is an isomorphism. From the long exact sequence, we
see that this is equivalent to the assertion that Q∗ is acyclic, i.e., that
Hp(Q∗) = 0 for all p∈ Z.
Thus we have to show that if q is a singular p-chain representing a cycle in q, so
∂q =r +s
with r∈ Sp−1(A) and s∈ Sp−1(B), then there are p-chains a∈ Sp(A) and b∈
Sp(B), and a (p + 1)-chainc∈Sp+1(X), such that
q =a +b +∂c.
Clearly it suﬃces to do this when q is a simplex. So, in words: we must show that
any σ : ∆p→ X is homologous to the sum of a p-chain in A and a p-chain in B.
□
We could hope to ﬁnd such a homology by breaking up the simplex σ as a
union of sub-simplices making ∆ p into a ∆-complex. If the p-simplices in this
decomposition are suﬃciently small then they will map either to A or to B under
σ. When σ is a 1-simplex, i.e., a path I→X, it is clear how we could do this: we
write I = [0, 1/2]∪ [1/2, 1]. Then σ is homologous to σ|[0,1/2] +σ|[1/2,1]. Iterating
this subdivision k times, we break up the unit interval into sub-intervals of length
2−k; when k≫ 0, each sub-interval will map into int(A) or int(B).
The proof in higher dimensions uses a generalization of this subdivision of ∆ 1.

38 TIM PERUTZ
Lemma 11.3 (Subdivision lemma) . The geometric p-simplex ∆p can be decom-
posed as ap-dimensional ∆-complex in such a way that all the p-simplicesτ1,...,τ N
in this decomposition have diameter < 1, and such that in the singular chain com-
plex S∗(∆p), one has
id∆p−
∑
i
τi∈ im∂p+1.
Here we regard id∆p as a p-simplex in ∆p. (In fact, one can take N =p! and the
diameters to be ≤ p
p+1.)
The particular subdivision we have in mind here is calledbarycentric subdivision.
For the proof of the lemma we refer to Hatcher (it can be extracted from Steps 1 and
2 of the proof of the Excision Theorem). We will at least say what the barycentric
subdivision is. The barycenter b of a p-simplex [v0,...,v p] is the point
b = 1
p + 1(v0 +··· +vp).
We now deﬁne the barycentric subdivision by induction on p. When p = 0, the
subdivision of ∆ 0 = [v0] has just one simplex: [ v0] itself. When p > 0, the p-
simplices of the barycentric subdivision of [v0,...,v p] are of form [b,w 0,...,w p−1],
where [w0,...,w p−1] is a (p−1)-simplex in the barycentric subdivision of some face
[v0,..., ˆvi,...,v p] of [v0,...,v p].
The subdivision lemma is a little ﬁddly to prove. Since we are omitting the proof,
let us emphasize that this is an entirely combinatorial lemma concerning convex
geometry in Euclidean spaces; the target space X does not appear at all.
Proof of locality, granting the subdivision lemma. Writeβ =∑
iτi∈Sp(∆p). Now,
each τi is a map ∆ p→ ∆p (actually an embedding), so we can iterate the subdi-
vision process, considering the composed maps τj◦τi : ∆p → ∆p. Let’s write
β2 =∑
i,jτj◦τi, and more generally
βn =
∑
i1,...,in
τin◦···◦ τi1.
By induction on n, we have that id ∆p−βn∈ im∂p+1.
Let 1−ϵ be the maximum diameter of one of the τi. Any x∈ ∆p has an open
neighbourhood Nx such that σ(N) is contained in int(A) or in int(B), since these
are open sets that cover X. But the image of τin◦···◦ τi1 has diameter≤ (1−ϵ)n,
so for large enough n, Nx is contained is the image of such a simplex. Thus ∆ p
is covered by subdivided simplices τin◦···◦ τi1 which map either to int( A) or to
int(B). A priori, the number n depends on x, but because ∆ p is compact we can
use the same n =n0 for all these subdivided simplices.
We know that id ∆p−βn0∈ Bp(∆p) (recall that Bp denotes im∂p+1), and ap-
plying σ we ﬁnd that
σ−σ#◦βn0∈Bp(X).
Butσ#◦βn0 is the sum of simplices σ◦τin0◦···◦ τi1 that map either to int(A) or
to int(B). This proves the theorem. □

ALGEBRAIC TOPOLOGY I: FALL 2008 39
12. Mayer–Vietoris and the homology of spheres
The locality theorem from the previous lecture has an important consequence:
the exact Mayer–Vietoris sequence. Using this sequence, we can at last carry out
interesting calculations in singular homology. We show that the homotopy type of
Sn, and hence the homeomorphism type of Rn, detects the dimension n.
12.1. The Mayer–Vietoris sequence. We extract from the locality theorem an
extremely useful computational tool in singular homology.
Theorem 12.1. Suppose (X;A,B ) is an excisive triad. Let a: A→X,b: B→X,
α: A∩B→A and β : A∩B→B be the inclusion maps. Then there is a canonical
long exact sequence
···→ Hp(A∩B)
α∗−β∗
−→ Hp(A)⊕Hp(B)
(a∗,b∗)
−→ Hp(X)
δ
→Hp−1(A∩B)→....
Remark. Since H−1(A∩B) = 0, the sequence ends with ···→ H0(A)⊕H0(B)→
H0(X)→ 0.
Proof. There’s a short exact sequence of chain complexes
0→S∗(A∩B)
α−β
→ S∗(A)⊕S∗(B)
a+b
→ S∗(A +B)→ 0,
simply because S∗(A∩B) =S∗(A)∩S∗(B). This results in a long exact sequence
of homology groups. But Hn(S∗(A +B)) = Hn(X) by the locality theorem, and
hence the long exact sequence has the form claimed. □
Exercise 12.1: Show that the connecting map δ can be understood as follows. Take
a p-cycle z∈ Sp(X). By locality, there is a homologous p-cycle z′ = x +y with x a
chain in A and y a chain in B. Then ∂x =−∂y, hence ∂x is a cycle in A∩B. We
have δ[z] = [∂x].
Exercise 12.2: Show that the Mayer–Vietoris sequence is not merely canonical, but also
natural in the following sense. Given an another excisive triad (X′;A′,B′) and a map
f : X→X′ such that f(A)⊂A′ and f(B)⊂B′, the two long exact sequences and
the maps between them induced by f form a commutative diagram.
Example 12.2. As a ﬁrst example of the Mayer–Vietoris sequence, let us prove
that
H∗(S1) = Z⊕ Z
where the ﬁrst Z is in degree 0, the second Z in degree 1. We have S1 = A∪B
whereA =S1\{ (1, 0)} andB =S1\{ (−1, 0)}. Then A∩B≃S0. Since A andB
are contractible, and A∩B the disjoint union of two contractible components, the
exactness of the Mayer–Vietoris sequence
Hp(A)⊕Hp(B)→Hp(S1)→Hp−1(A∩B),
tells us thatHp(S1) = 0 for allp> 1. We already know H1(S1) = Z =H0(S1) (via
π1 and path-connectedness), but let’s see that we can recover this by the present
method. The sequence ends with the 6-term sequence
0→H1(S1)→ Z2→ Z2→H0(S1)→ 0,
where the map Z2 = H0(A∩B)→ H0(A)⊕H0(B) = Z2 is given by ( m,n )↦→
(m−n,m−n). Thus H1(S1) is isomorphic to the kernel of this map, which is
Z(1, 1), and H0(S1) to its cokernel, which is also Z.

40 TIM PERUTZ
Proposition 12.3. We have
H∗(Sn)∼= Z⊕ Z, n ≥ 0,
where the ﬁrst Z is in degree 0, the second Z in degreen.
Proof. By induction onn. Since S0 is a 2-point space, it’s true for that case. We’ve
just proved it for n = 1, so we’ll start the induction there.
So now assume n > 1. We have Sn = A∪B where A = Sn\{N} and B =
Sn\{S},N andS being the north and south poles. Then A∩B≃Sn−1. Since A
andB are contractible, Mayer–Vietoris tells us that Hp(A)⊕Hp(B) = 0 for p> 0.
Thus, from the exactness of
Hp(A)⊕Hp(B)→Hp(Sn)→Hp−1(A∩B)→Hp−1(A)⊕Hp−1(B),
we see that Hp(Sn)∼=Hp−1(Sn−1) for all p> 1. We also have an exact sequence
0→H1(S1)→ Z→ Z2,
where the map Z =H0(A∩B)→H0(A)⊕H0(B) = Z2 is n↦→ (n,−n), and so is
injective. Hence H1(Sn) = 0 (which we knew anyway,Sn being simply connected.)
□
Remark. The argument can be made slicker using reduced homology.
Note that, in all dimensions (even n = 1) the connecting map δn : Hn(Sn)→
Hn−1(Sn) is an isomorphism.
Exercise 12.3: Describe an n-cycle cn∈Sn(Sn) that generates Hn(Sn). (Prove that
your cycle generates by induction, looking at the explicit form of the connecting map.)
We now take a break from the formal development of the theory and harvest
some applications.
Theorem 12.4. If Rn is homeomorphic to Rm then m =n.
Proof. We may assume that m and n are positive. If Rm∼= Rn then Rm\{ 0}∼=
Rn\{ pt.}∼= Rn\{ 0}, hence Sn−1 is homotopy equivalent toSm−1. But Sn−1 and
Sm−1 have diﬀerent homology in degree n− 1, unless m =n. □
Theorem 12.5 (Brouwer ﬁxed point theorem). LetDn denote the closed n-ball in
Rn, n≥ 1. Then every continuous map Dn→Dn ﬁxes a point.
Proof. Recall that we already proved this using π1, when n = 2. By the same
argument that we gave there, it suﬃces to show there is no retraction r : Dn→
∂Dn =Sn−1, i.e. no r such that r◦i = idSn−1, where i: Sn−1→Dn denotes the
inclusion map. If such an r existed, we would have
idHn−1(X) =Hn−1(r)◦Hn−1(i).
ButHn−1(Sn−1)⁄= 0, whereasHn−1(Dn) (the target of Hn−1(i)) is zero, assuming
n >1. This proves the theorem (except when n = 1; but in that case it follows
from the intermediate value theorem). □

ALGEBRAIC TOPOLOGY I: FALL 2008 41
12.2. Degree. Deﬁne the degree deg(f) of a map f : Sn→Sn by the equation
Hn(f)(m) = deg(f)m, m ∈Hn(Sn)∼= Z.
The following properties of degree follow from the deﬁnition and the basic properties
of homology:
(1) Homotopic maps have the same degree.
(2) deg(idSn) = 1.
(3) deg f = 0 when f extends to a map Dn+1→Sn.
(4) deg(fg ) = deg(f) deg(g).
You will ﬁnd solutions to the following exercise in Hatcher, but I recommend trying
to work it out for yourself.
Exercise 12.4: Degree has the following further properties:
(i) When n = 1, the homological degree deﬁned here coincides with the degree as
we deﬁned it earlier via π1(S1).
(ii) degs =−1 when s is the restriction to Sn of a reﬂection in Rn+1.
(iii) dega = (−1)n+1 when a is the antipodal map x↦→−x.
(iv) degf = (−1)n+1 when f has no ﬁxed points.
Use the last point to show (a) that no group of order > 2 can act freely on S2m, and
(b) that S2m possesses no nowhere-vanishing vector ﬁeld.
Exercise 12.5: Complex projective n-space CPn is deﬁned as (Cn+1\{ 0})/C∗, where
C∗ acts by scalar multiplication. Use Mayer–Vietoris to show that
Hp(CPn)∼=
{
Z, if p is even and 0≤p≤ 2n,
0, else.
Show, moreover, that the inclusion of CPn in CPn+1, induced by the inclusion of Cn+1
as a linear subspace of Cn+2, induces an isomorphism on homology up to degree 2n.
Exercise 12.6: Use Mayer–Vietoris to compute H∗(T 2), H∗(RP 2) and H∗(K2). In
each case, ﬁnd an explicit (minimal) collection of cycles that span the homology.
Exercise 12.7: Use Mayer–Vietoris to compute H∗(Σg) where Σg is a 2-sphere with g
handles attached.

42 TIM PERUTZ
13. Relative homology and excision
13.1. Relative homology. Suppose i: A → X is the inclusion of a subspace.
There is a short exact sequence of chain complexes
0→S∗(A)
i#
→S∗(X)→S∗(X,A )→ 0,
where S∗(X,A ) = S∗(X)/i#S∗(A). We denote by H∗(X,A ) the homology of
S∗(X,A ). Thus a chain in X deﬁnes a cycle in S∗(X,A ) if its boundary is a
sum of simplices in A. A map of pairs f : (X,A )→ (Y,B ) induces f∗ : H∗(X,A )→
H∗(Y,B ).
The short exact sequence for the pair ( X,A ) induces the long exact sequence of
the pair
···→ Hp(A)
i∗
→Hp(X)→Hp(X,A )
δ
→Hp−1(A)→....
We can understand the connecting map δ as follows. If c∈Sp(X,A ) is a cycle, δ[c]
is deﬁned by lifting c to a chain ˜c in Sp(X), and putting δ[c] = [i∗(∂pc)]. In other
words,δ[c] is the boundary of a chain representing c, considered as a cycle in A.
Exercise 13.1: Show that if B⊂A⊂X, one has a long exact sequence of the triple
···→ Hi(A,B )→Hi(X,B )→Hi(X,A )→Hi−1(A,B )→...,
and describe the maps in this sequence.
We now state the excision theorem. It has essentially the same content as the
Mayer–Vietoris sequence.
Theorem 13.1 (Excision). Suppose (X;A,B ) is an excisive triad. Then the map
H∗(A,A∩B)→H∗(X,B )
induced by the inclusion (A,A∩B)→ (X,B ) is an isomorphism.
Proof. We invoke the locality theorem for chains. Note that H∗(A,A∩B) is the
homology of the complex S∗(A)/S∗(A∩B) = S∗(A)/(S∗(A)∩S∗(B)) (where we
think of S∗(A) and S∗(B) as subcomplexes of S∗(X)). By a general property of
abelian groups, the inclusion of S∗(A) in S∗(A) +S∗(B) induces an isomorphism
S∗(A)/(S∗(A)∩S∗(B))∼= (S∗(A) +S∗(B))/S∗(B).
ButS∗(A)+S∗(B) =S∗(A+B) by deﬁnition of the latter, and the mapS∗(A+B)→
S∗(X) is a quasi-isomorphism. Let In = Hn(S∗(A +B)/S∗(B)). Then we have a
commutative diagram with exact rows
Hn(B) −−−−→Hn(S∗(A +B)) −−−−→ In −−−−→Hn−1(B) −−−−→Hn−1(S∗(A +B))
=
↓ ∼=
↓
↓ =
↓ ∼=
↓
Hn(B) −−−−→ Hn(X) −−−−→Hn(X,B ) −−−−→Hn−1(B) −−−−→ Hn−1(X)
All the vertical arrows but the middle one are isomorphisms, and hence so is
the middle one (this is the 5-lemma). Putting things together, we ﬁnd that
S∗(A)/S∗(A∩B)→ S∗(X)/S∗(B) is a quasi-isomorphism, which is the result we
want. □
Exercise 13.2: Re-derive H∗(Sn)∼= Z(0)⊕ Z(n) using excision.

ALGEBRAIC TOPOLOGY I: FALL 2008 43
Example 13.2. When working with spaces X equipped with basepoints x, it’s
often useful to work with reduced homology ˜H∗. We put
˜Hn(X) =Hn(X,{x}).
Then, by the exact sequence of the pair, the natural map
Hn(X)→ ˜Hn(X)
is an isomorphism for all n> 0. The end of the sequence looks like this:
H1(X,{x})→H0({x})→H0(X)→H0(X,{x})→ 0.
The map H0({x})→H0(X) is injective (which explains why ˜H1(X) =H1(X)), so
˜H0(X) =H0(X)/H0({x}). Thus, when X is path connected, we have
˜Hn(X) =
{
0, n = 0
Hn(X), n> 0.
This justiﬁes the omission of x from the notation (when X is not path connected,
x is important).
Exercise 13.3: Let A be a non-empty closed subspace of X. There is a natural homo-
morphismH∗(X,A )→H∗(X/A,A/A) = ˜H∗(X/A). Use excision to show that, when
A has a neighbourhood N that deformation-retracts to A, this map is an isomorphism.
Exercise 13.4: Show that if (X;A,B ) is an excisive triad, and b∈A∩B a basepoint,
there is an exact Mayer–Vietoris sequence in reduced homology (formally the same as
the usual one, but with ˜H∗ instead of H∗).
13.2. Suspension. We now set up the suspension isomorphisms. The (unreduced)
suspensionSX ofX is the space (X×[−1, 1])/∼ where (x,t )∼ (x′,t′) ift =t′ = 1
or t =t′ =−1. For example, S(Sn)∼=Sn+1.
Proposition 13.3. Fix a basepoint x∈X. There are natural isomorphisms
sn : ˜Hn+1(SX)→ ˜Hn(X), n ≥ 0.
Proof. We haveSX =C+∪C−, where
C+ = (X× [−1
2, 1])/(X×{ 1}), C − = (X× [−1, 1
2])/(X×{− 1}).
BothC+ andC− are cones on X; they deformation retract to their respective cone
points c± = (X×{± 1})/(X×{± 1}). Thus
Hn(SX,C +) =Hn(SX,{c+}) = ˜Hn(SX).
On the other hand (X;C+,C−) is an excisive triad, so
Hn(SX,C +)∼=Hn(C−,C +∩C−).
Since C− is contractible, the long exact sequence of the pair tells us that
Hn(C−,C +∩C−)→Hn−1(C+∩C−) =Hn−1(X)
is an isomorphism when n> 1, and that H1(C−,C +∩C−) = ˜H0(X). Putting this
together, we get isomorphisms
˜Hn(SX)∼=Hn(SX,C +)∼=Hn(C−,C +∩C−)∼= ˜Hn−1(X).
□

44 TIM PERUTZ
Exercise 13.5: Show that the two spaces S2∨S4 and CP 2 have isomorphic homology
groups. Likewise the two spaces S3∨S5 and S(CP 2).
Remark. We will see later that the homotopy types of S2∨S4 and CP 2 can be dis-
tinguished by their cohomology rings, but thatS3∨S5 andS(CP 2) have isomorphic
cohomology rings.
13.3. Summary of the properties of relative homology.
• To each pair of spaces ( X,A ), and each integer n, it assigns an abelian
group Hn(X,A ) (and we write Hn(X) for Hn(X,∅)).
• To each map f : (X,A )→ (X′,A′) and each n∈ Z it assigns a homomor-
phismHn(f): Hn(X,A )→Hn(X′,A′). One has Hn(f◦g) =Hn(f)◦Hn(g)
andHn(id(X,A)) = idHn(X,A). If f0 is homotopic tof1 via a homotopy{ft}
such that ft|A =f0|A, then Hn(f1) =Hn(f0).
• To each pair of spaces ( X,A ), and each integer n, it assigns a homomor-
phism
δn : Hn(X,A )→Hn−1(A).
These maps are natural transformations. That is, given f : (X,A ) →
(X′,A′), one has
δn◦Hn(f) =Hn−1(f)◦δn
as homomorphisms Hn(X,A )→Hn−1(A′).
Besides these basic properties, the following also hold:
• DIMENSION: If∗ denotes a 1-point space then Hn(∗) = 0 for n⁄= 0, while
H0(∗) = Z.
• EXACTNESS: The sequence
···→ Hn(A)→Hn(X)→Hn(X,A )
δn
→Hn−1(A)→Hn−1(A)→...
is exact, where the unlabelled maps are induced by the inclusions ( A,∅)→
(X,∅) and (X,∅)→ (X,A ).
• EXCISION: if (X;A,B ) is an excisive triad then the map
Hn(A,A∩B)→Hn(X,B )
induced by the inclusion (A,A∩B)→ (X,B ) is an isomorphism.
• ADDITIVITY: If (Xα,Aα) is a family of pairs, then one has an isomorphism
⨁
α
Hn(Xα,Aα)→Hn(
∐
α
Xα,
∐
α
Aα)
given by the sum of the maps induced by the inclusions into the disjoint
union.
(Additivity is easy to check; for ﬁnite families, it follows from excision and exact-
ness.)
Remark. As stated, these axioms do not uniquely characterise relative homology.
However, they do characterise it if one restricts the pairs ( X,A ) to be CW pairs.
Alternatively, if we include one more axiom, that ‘weak equivalences’ induce isomor-
phisms on homology, then the axioms uniquely characterise the theory for arbitrary
pairs, because every pair is weakly equivalent to a CW pair. If one omits the di-
mension axiom, there are many diﬀerent homology theories on CW pairs, including
stable homotopy, real or complex K-theory, and oriented, unoriented or complex
bordism.

ALGEBRAIC TOPOLOGY I: FALL 2008 45
14. Vanishing theorems for homology of manifolds
Theorem 14.1. Let M be an n-manifold, i.e., a space locally homeomorphic to
Rn. Then Hp(M) = 0 for p>n .
The proof will use Mayer–Vietoris sequences to increase the generality incre-
mentally, starting from a very banal statement. So as to avoid low-dimensional
exceptions, we use Mayer–Vietoris for reduced homology. However, we can and
shall assume throughout that n> 0.
Proof. Step 1: If n≥ 1 and X is the union of strictly less than 2n of the faces of
the n-cubeIn, then ˜Hp(X) = 0 for p≥n− 1.
This we prove by induction on n; the n = 1 case is clear. The induction step
is done by a further induction, on the number of faces of X. When X is empty
it it trivial. Otherwise, choose a face F of In which is contained in X, and let
X′ =X\ int(F ). Choose F so that not all its neighbours are in X. Mayer–Vietoris
(and a few deformation retractions of open neighbourhoods) then gives an exact
seqence
˜Hp(F )⊕ ˜Hp(X′)→ ˜Hp(X)→ ˜Hp−1(F∩X′).
ButF∩X′ is a union of strictly less than 2( n− 1) of the faces of the (n− 1)-cube
F , so inductively ˜Hp−1(F∩X′) = 0. Trivially ˜Hp(F ) = 0, and by induction on the
number of faces, ˜Hp(X′) = 0. This completes the induction.
Step 2: If C1,...,C q are integer cubes in Rn then Hp(⋃
iCi) = 0 for p≥n.
Here an integer cube C in Rn means a translate by some ( m1,...,m n)∈ Zn
of In. We prove this by induction on the number of cubes q. A single cube is
contractible. For the induction step, observe that one of the cubes, which we may
take to be Cq, has maximal x1-coordinate. It then intersects less than 2 n of its
neighbours. Write Dq =C1∪···∪ Cq. We then have a Mayer–Vietoris sequence
Hp(Cq)⊕Hp(Dq−1)→Hp(Dq)→ ˜Hp−1(Dq−1∩Cq).
By induction, the left-hand term is zero for p ≥ n, so it suﬃces to show that
Hp−1(Dq−1∩Cq) = 0 also. But this follows from Step 1.
Step 3: Let U⊂ Rn be an open set. Then Hp(U) = 0 for p≥n.
Let z =∑aiσi be a p-cycle, and let K denote the union ⋃ imσi. Note that K
is compact. Thus we can ﬁnd ϵ> 0 and a ﬁnite collection of integer cubes Cj such
that the interiors of the small cubes ϵCj cover K, but the union L of the ϵCj is
contained in U. Then z represents a p-cycle in L. But Hp(L) = 0 by Step 2; so z
is a boundary in L, and hence in U.
Step 4: For an n-manifold M, we have Hp(M) = 0 when p>n .
Let z =∑aiσi be a p-cycle in M, and let K =⋃ imσi. Again it is compact,
and hence covered by ﬁnitely many open sets homeomorphic to Rn. We prove by
induction onN that ap-cyclez contained inN open setsV1,...,V N homeomorphic
to Rn is a boundary in ⋃Vi (hence in M). The case N = 1 was Step 3. For the
induction step, assume N >1 and let U =V1∪···∪ VN−1. Mayer–Vietoris gives
an exact sequence
Hp(U)⊕Hp(VN)→Hp(U∪VN)→Hp−1(U∩VN).
By induction, the left term vanishes. The term on the right vanishes by Step 3.
Hence the middle term also vanishes. □

46 TIM PERUTZ
14.1. Local homology. The local homology of a space M at x∈M is deﬁned as
H∗(M,M \{x}).
Lemma 14.2. When M is an n-manifold, one has H∗(M,M \{x})∼= Z(n).
Proof. Choose a neighbourhood D ofx homeomorphic to a closed n-ball. By exci-
sion,H∗(M,M\{x})∼=H∗(D,D\{x}). One ﬁnds from the long exact sequence of
the pair that Hp(D,D\{x})∼= ˜Hp−1(D−{x}) for all p. But D\{x} deformation-
retracts to Sn−1, and H∗(Sn−1)∼= Z(p−1), whence the result. □
We can form a natural covering space p: HM → M whose ﬁber over x is
Hn(M,M \{x}). Thus a point in HM is a pair ( x,hx) where x∈ M and hx∈
Hn(M,M \{x}), and p(x,hx) = x. The topology is deﬁned as follows. Let U be
an open set in X homeomorphic to Rn, and let B⊂U be a closed neighbourhood
homeomorphic to the closed disc Dn. Then one has isomorphisms
Hn(M,M \{y})←Hn(M,M \B)→Hn(M,M \{x}).
Deﬁne a ‘component’ ofp−1(U) to be an equivalence class of pairs (x,hx)∈p−1(U),
where (x,hx) is equivalent to (y,hy) if there is a ballB containing bothx andy and
an element z∈ Hn(M,M \B) mapped by the above isomorphisms to hx and hy.
The components of p−1(U), as U varies over open neighbourhoods homeomorphic
to Rn, form a basis for a topology making p a covering map.
14.2. Homology in dimension n.
Theorem 14.3. Hn(M) = 0 when M is a connected but non-compact n-manifold.
We have already established a special case of this, the case where M is an open
set in Rn. The principle of the proof is standard, but the details here are from
May’s book. The proof is more technical than one would ideally like, but there is
only really new idea:
Ann-dimensional homology class z determines a section sz ofp: HM→M, and
z = 0 if sz(x) = 0 for some x.
Lemma 14.4. LetU⊂ Rn be open. Then the natural homomorphism
Hn(Rn,U )→
∏
x∈Rn\U
Hn(Rn, Rn\{x})
is injective. Equivalently, the product of maps induced by inclusions,
˜Hn−1(U)→
∏
x∈Rn\U
˜Hn−1(Rn\{x}),
is injective.
The equivalence of the two assertions follows from the long exact sequences of
the pairs (Rn,U ) and (Rn, Rn\{x}). Informally, the second assertion says that any
non-trivial (n− 1)-cycle in U must wrap around some point outside U. We prove
the second assertion.
Proof. Suppose s∈ ˜Hn−1(U) maps to zero in ˜Hn(Rn\{x}) for all x /∈U. We will
show that s = 0. The notation will be rather heavy: we ﬁx a chain of subspaces
K⊂V ⊂ ¯V ⊂U

ALGEBRAIC TOPOLOGY I: FALL 2008 47
whereK is compact,V open, ¯V compact, ands is the image of somer∈ ˜Hn−1(K).
LetT be a cube (−d,d )n large enough that ¯V ⊂T . We discard everything outside
T : we shall show that r maps to zero in ˜Hn−1(T∩U), hence also in ˜Hn−1(U). We
know that r maps to zero in ˜Hn−1(T\{x}) for all x∈T\U. Our method will be
to ‘eat away’ more and more of T\U, showing that r maps to zero in ˜Hn−1(T\S)
for progressively larger subsets E ⊂ T\U, starting at E ={x} and ending at
E =T\U itself. Since T\ (T\U) =T∩U, this will do the job.
Now,T\U is covered by a grid of small compact cubes in Rn, whose diameter is
chosen small enough that none of them hits V . Let C1,...,C q be the intersections
of these small cubes withT . We claim thatr maps to zero in ˜Hn−1(T\Ep) forp≤q,
where Ep =C1∪···∪ Cp. Indeed, the case p = 0 is trivial, and for p> 0 we have
T\Ep = (T\Ep−1)∩(Rn\Ep). On the other hand, (T\Ep−1)∪(Rn\Ep) = Rn\Ep.
Mayer–Vietoris gives
Hn(Rn\Ep) = 0→ ˜Hn−1(T\Ep)→ ˜Hn−1(T\Ep−1)⊕ ˜Hn−1(Rn\Ep).
Here the group on the left is zero by Step 3 in the proof of the earlier theorem.
Sincer maps to zero in ˜Hn−1(T\Ep−1)⊕ ˜Hn−1(Rn\Ep), it must then map to zero
in ˜Hn−1(T\Ep). □
Proof of the theorem. Anyz∈Hn(M) deﬁnes a continuous section sz : M→HM.
If M is connected (hence path-connected), it follows from unique path-lifting that
any continuous section is determined by its value at a point. Butz is represented by
a cycle that maps to a compact subsetZ⊂M. If M is connected but non-compact,
we can choosing x∈M\Z. Then sz(x) = 0, and hence sz = 0.
Thus we take a class z∈ Hn(M) that maps to zero in some Hn(M,M \{x}).
We must show that z = 0.
There is some compact set Z⊂M such that z is in the image of Hn(Z). Now,
Z is contained in a ﬁnite union U1∪···∪ Uq of coordinate neighbourhoods Ui,
and it suﬃces to show [ z] = 0 in Hn(U1∪···∪ Uq). We have already proved that
Hn(U1) = 0. Now take q > 1, and inductively suppose that we’ve shown that
Hn(U1∪···∪ Uq−1) = 0. Mayer–Vietoris gives an exact sequence
Hn(U)⊕Hn(V )→Hn(U1∪···∪ Uq)→ ˜Hn−1(U∩V )→ ˜Hn−1(U)⊕ ˜Hn−1(V ),
where V =U1∪···∪ Uq−1 and U =Uq. This reduces to
0→Hn(U1∪···∪ Uq)→ ˜Hn−1(U∩V )→ ˜Hn−1(V ),
and so the task is to show that the map j∗ : ˜Hn−1(U∩V )→ ˜Hn−1(V ) induced by
inclusion is injective. This step is a little tricky. Take r∈ kerj∗. From the long
exact sequence of the pair (V,U ∩V ),
0→Hn(V,U ∩V )→ ˜Hn−1(U∩V )→ ˜Hn−1(V ),
we ﬁnd a (unique)t∈Hn(V,U∩V ) such thatδt =r. From the long exact sequence
of the pair (U,U∩V ),
0→Hn(U,U∩V )→ ˜Hn−1(U∩V )→ 0,
we ﬁnd a (unique) s∈ Hn(U,U ∩V ) with δs = r. Now, s and t have images
s′ and t′ in a common group Hn(U∪V,U ∩V ), and s′−t′ lies in the kernel of
δ : Hn(U∪V,U∩V )→ ˜Hn−1(V ), hence in the image ofHn(U∪V ): say s′−t′ comes
from w∈ Hn(U∪V ). Since U∪V is non-compact, the composite Hn(U∪V )→
Hn(M)→Hn(M,M \{x}) maps w to zero (by the argument at the beginning of

48 TIM PERUTZ
this proof). Take x outside U∪V . Then we have a map Hn(U∪V,U ∩V )→
Hn(M,M \{x}) factoring Hn(U∪V )→ Hn(M,M \{x}) which therefore carries
t′−s′ to zero. Moreover, t′ maps to zero inHn(M,M\{x}), because it comes from
t∈Hn(V,U ∪V ), and the map Hn(V,U ∪V )→Hn(M,M \{x}) factors through
Hn(M\{x},M \{x}) = 0. Hence s′ maps to zero in Hn(M,M \{x}). It follows
that s maps to zero in Hn(U,U\{c})∼=Hn(M,M \{c}).
SinceU∼= Rn, we haves∈Hn(Rn, Rn\V ) ands maps to zero inHn(Rn, Rn\{y})
for every y lying outside V . We wish to show that s is zero (so that r =δs = 0).
But that is what we proved in the last lemma. □
Exercise 14.1: (a) Let X be a path connected space. Show how 2-sheeted covering
spaces of X, up to isomorphism, correspond to homomorphisms π1(X,x )→ Z/2.
(b) Let ˜M⊂ HM be the subspace consisting of pairs (x,hx) with hx a generator
for Hn(M,M \{x})∼= Z. Thus p: ˜M → M is a 2-sheeted covering space. The
corresponding homomorphism π1(M)→ Z/2 is called the orientation character or ﬁrst
Stiefel–Whitney class w1(M) of M. Compute it for X the Klein bottle and for RP 2.

ALGEBRAIC TOPOLOGY I: FALL 2008 49
15. Orientations and fundamental classes
15.1. Homology with coeﬃcients. Homology with coeﬃcients is a simple gen-
eralisation of singular homology.
Let R be a commutative unital ring. The case we have been considering up to
this point is R = Z, but we could also take, for example, a ﬁeld such as Fp = Z/p
(where p is prime) or Q.
Deﬁne a chain complex of R-modules S∗(X;R) by deﬁning Sn(X;R) as the free
R-module generated by the n-simplices in X:
Sn(X;R) =RΣn(X)∼=Sn(X)⊗ZR.
Deﬁne the diﬀerential ∂ on simplices by the familiar formula, and in general by
R-linearity. Let Hn(X;R) =Hn(S∗(X;R)), as an R-module.
IfA⊂X is a subspace then one has an injective chain mapS∗(A;R)→S∗(X;R).
Put
S∗(X,A ;R) =S∗(X;R)/S∗(A;R), H n(X,A ;R) =Hn(S∗(X,A ;R)).
Then one has a long exact sequence of the pair. Locality, Mayer–Vietoris and
excision hold just as before, as does homotopy invariance. One has H0(X;R) =
Rπ0(X). The homology of a point, Hi(∗;R), vanishes for i> 0. For an n-manifold
M, one has Hi(M;R) = 0 for all i>n and, in the non-compact case, for i =n. All
these assertions follow from routine generalisations of the proofs we have given.
Slightly trickier is the assertion that, for X path connected, one has
H1(X;R)∼=π1(X)ab⊗ZR.
The proof we gave for the case R = Z uses the integer coeﬃcients in a signiﬁcant
way, but the general case follows from it and the universal coeﬃcients theorem, to
be given in the next lecture. (If you have a simpler proof, tell me!)
15.2. What it’s good for. Homology with coeﬃcients contains no more informa-
tion than ordinary homology, but is useful for the following reasons.
• When R is a ﬁeld, algebraic properties of homology simplify. For instance,
over a ﬁeld, passing to homology commutes with the tensor product and
dualisation operations on chain complexes.
• For many spaces, the Z-homology is more complicated than the homology
over the prime ﬁeldsZ/p or over Q. Moreover, considering these collectively,
one does not lose information. Good examples are RPn and various Lie
groups, notably SO(n).
• When working with manifolds, in Z-homology one must distinguish the ori-
entable and non-orientable cases, but in Z/2-homology this is unnecessary.
15.3. The local homology cover. Recall from the last lecture that the local
homology of an n-manifold (now with R-coeﬃcients) is given by
H∗(M,M \{x};R)∼=R(n).
Collectively, these form a covering spaceHM,R→M with ﬁbresHn(M,M\{x};R).
(Here one gives Hn(M,M \{x};R) the discrete topology.) The sections Γ M,R of
this covering space form an R-module. A class z∈ Hn(M;R) gives classes zx∈
Hn(M,M \{x};R) for all x, and this determines a homomorphism Hn(M;R)→
ΓM,R.

50 TIM PERUTZ
Theorem 15.1. The the natural homomorphism Hn(M;R)→ ΓM,R is injective.
Proof. We may assume M is connected. Fix x∈ M, and observe that by our
vanishing theorem for homology of non-compact manifolds, Hn(M\{x}) = 0. The
long exact sequence of the pair therefore reads
0→Hn(M)→Hn(M,M \{x}).
That is, the homomorphism Hn(M)→Hn(M,M\{x}) is injective. Our vanishing
theorem was proved for Z coeﬃcients, but the proof applies to an arbitrary coeﬃ-
cient ring. Since it injects into Hn(M,M \{x}), a fortiori Hn(M;R) injects into
ΓM,R. □
15.4. Orientations. Depending on the ground ringR, there may be more than one
isomorphism ofR-modulesHn(M,M\{x};R)∼=R: for instance, whenR = Z, there
are exactly two isomorphisms (the one you ﬁrst thought of, and its composition with
n↦→−n). However, when R = Z/2, there is a unique isomorphism.
Deﬁnition 15.2. An R-orientation for the n-manifold M at x is an isomorphism
of R-modules
η : Hn(M,M \{x};R)→R.
If R is not speciﬁed, we understand R = Z.
Deﬁne the R-orientation cover
˜MR ={(x,ηx) :x∈M and η is an R -orientation for M at x},
and let pR : ˜M→M be the projection (x,ηx)↦→x. The topology is constructed in
much the same way as that of HM (work this through!). Notice that ˜MR is itself
an n-manifold. When R = Z, it is a 2-sheeted covering of M. Assuming M is
connected, ˜MZ is either connected, hence a non-trivial covering, or disconnected,
hence(!) trivial.
Deﬁnition 15.3. AnR-orientation forM is a section of p, i.e., a map s: M→ ˜M
such that pR◦s = idM. If an orientation exists, M is called R-orientable. Again,
if no ring is speciﬁed we understand R = Z.
Thus an R-orientation for M is a coherent choice of orientations for all points.
Observe that there is automatically a unique ( Z/2)-orientation.
The orientation cover is closely related to the local homology cover HM,R→M.
We illustrate this with the case R = Z. If a∈ Z then the subset
˜M(a) :={(x,hx)∈HM,R :ηx(hx) =a for some orientation ηx}
then ˜M(a) = ˜M(−a). If a⁄= 0 then the covering ˜M(a)→ M is isomorphic to
˜MZ→M, while if a = 0 it is a trivial covering M→M.
15.5. Fundamental classes.
Deﬁnition 15.4. (i) If M is an n-manifold, an R-fundamental class for M is a
class z∈ Hn(M;R) whose image in Hn(M,M \{x};R) is a generator, for every
x∈M.
(ii) More generally, ifK⊂M is a subspace, an R-fundamental class forM atK
is a class z∈Hn(M,M \K;R) whose image in Hn(M,M \{x};R) is a generator,
for every x∈K.

ALGEBRAIC TOPOLOGY I: FALL 2008 51
Theorem 15.5. AnR-orientation forM determines anR-fundamental classzK at
K, for every compact subspace K⊂M. The orientation maps zK(x)∈Hn(M,M\
{x}) to 1∈R.
Proof. We drop the coeﬃcients from the notation. It is technically easier to prove,
alongside the theorem, that Hp(M,M \K) = 0 for p>n .
Start by supposing K ⊂ U, with U ∼= Rn. Notice that by excision and a
deformation retraction, Hn(M,M \U)∼= Hn(Rn, Rn\{ 0}). Thus an orientation
determines a fundamental class for M at U, and hence at K. Also, in this case
Hp(M,M \K) = 0 for p > n by the long exact sequence of the pair and our
vanishing theorem from last time.
A general compact subsetK⊂M, is the union of ﬁnitely many compact subsets
Ki, each contained in a neighbourhood Ui∼= Rn. So, by induction, it suﬃces to
show that if the theorem (including the statement about p>n ) holds forK,L and
K∩L then it holds for K∪L.
To prove this, we need a relative form of Mayer–Vietoris. IfY ⊂X, and (Y ;A,B )
is an excisive triad, then one has a long exact sequence
···→ Hp(X,X\ (A∪B))→Hp(X,X\A)⊕Hp(X,X\B)→Hp(X,A∩B)→....
In our case we get
Hn+1(M,M\ (K∩L))→Hn(M,M\ (K∪L))→Hn(M,M\K)⊕Hn(M,M\L).
By hypothesis, the module on the left is zero, but we have fundamental classes
zK ∈ Hn(M,M \ (K∪L)) and zL ∈ Hn(M,M \ (K∪L)) determined by the
orientation. Their diﬀerence, in Hn(M,M \ (K∩L), is zero, and hence zK +zL
comes from a class zK∪L∈ Hn(M,M \ (K∪L)) which is clearly a fundamental
class. □
Exercise 15.1: Use the locality theorem for chains to derive this relative Mayer–Vietoris
sequence.
Corollary 15.6. If M is compact, connected andR-oriented then Hn(M;R) =R.
Hence any compact, connected n-manifold M has Hn(M; Z/2)∼= Z/2. If it is also
orientable then Hn(M)∼= Z.
Proof. We know by the last theorem that a fundamental class exists, so the homo-
morphism
Hn(M;R)→ ΓM,R
is onto. We observed earlier that it is injective. Hence it is an isomorphism. But
ΓM,R∼=R, and an orientation speciﬁes such an isomorphism. □
Corollary 15.7. If M is connected but not orientable then Hn(M) = 0.
Proof. The natural map Hn(M)→ ΓM is injective. If it had non-trivial image, the
image would contain a section of one of the covers ˜M(a)→ M with a⁄= 0. But
these covers are copies of ˜M→M, and so have no sections by hypothesis. □
Exercise 15.2: Convince yourself that the deﬁnition of an orientation at x is not crazy.
More speciﬁcally, take R = Z and M to be an n-dimensional vector space V . An
orientation for V in a more familiar sense would be an isomorphism V → Rn, where
two isomorphisms θ1 and θ2 are considered equivalent if det(θ◦θ−1
2 )> 0. Show how
an orientation for the vector space V determines an orientation for V as a manifold, at
any chosen point x.

52 TIM PERUTZ
Exercise 15.3: If M is given a smooth structure then it is orientable iﬀ there is a smooth
atlas whose transition functions τij have positive Jacobian determinants detDxτij.
Exercise 15.4: A manifold M is orientable if it is simply connected, or more generally,
if π1(M) is ﬁnite and has odd order.
Exercise 15.5: If p is odd then a Z/p-orientation determines, and is determined by, a
Z-orientation.
Exercise 15.6: Show that if a group G acts freely on M = Sn, then the orientation
character π1(M/G) = G → Z/2 of the quotient manifold is given by G ∋ g ↦→
deg(g)∈{± 1} = Z/2. For which n is RPn orientable?
Exercise 15.7: (i) Show that there is no homeomorphism Hn ∼= Rn, where Hn =
{(x1,...,x n)∈ Rn :x1≥ 0}.
(ii) Let M be a space, and N the subspace of points x∈ M which have a neigh-
bourhood U such that there is a homeomorphism U→ Hn sending x to 0. Say M is
an n-manifold with boundary if M\N is an n-manifold. In that case write ∂M for
the boundary N. Check that that ∂M is an (n− 1)-manifold.
Exercise 15.8: Suppose M is a compact, connected n-manifold with non-empty bound-
ary ∂M . It is a fact (see Hatcher) that there is a neighbourhood U of ∂M and a
homeomorphismU→∂M× [0, 1) sending any x∈∂M to (x, 0).
(a) Show that Hp(M) = 0 forp≥n and Hp(M,∂M ) = 0 forp>n .
(b) Show that if M\∂M is orientable then Hn(M,∂M )∼= Z.
(c) Let X be a space. Suppose h∈ Hn−1(X) is a homology class that is repre-
sentable by a manifold, in that there is a compact oriented n− 1-manifold N with
fundamental class zN and a map f : N → X with f∗zN = h. Show that h = 0 if
N = ∂M for a compact oriented n-manifold with ∂M = N such that f extends to
F : M→X.
Exercise 15.9: Let h: S3→S2 denote the Hopf map, given by
h(z1,z 2)↦→z1/z2.
Here we think ofS3 as the unit sphere in C2 and ofS2 as the Riemann sphere C∪{∞}.
Letω be a generator for H3(S3) = Z. Then h∗ω = 0, since H3(S2) = 0. Can you ﬁnd
a direct explanation for why the particular class h∗ω should be zero? In other words,
can you ﬁnd a 4-chain bounding a 3-cycle representing h∗ω?

ALGEBRAIC TOPOLOGY I: FALL 2008 53
16. Universal coefficients
In this lecture, we address the following question. Let C∗ be a chain complex over
R, and Q an R-module. How does one compute H(C∗⊗RQ) in terms of H(C∗)?
We obtain a solution when R is a principal ideal domain (PID) and C∗ is a free
R-module.
16.1. Homology with coeﬃcients. Last time, we introduced homologyH∗(X;k)
with coeﬃcients in a ring k. This was deﬁned as the homology of the complex of
k-modules
kΣ∗(X) =S∗(X)⊗Zk.
What is its relation to H∗(X)? The answer is supplied by the universal coeﬃcients
theorem:
Theorem 16.1 (Universal coeﬃcients: homology version) . There are short exact
sequences of k-modules,
0→Hn(X)⊗k→Hn(X;k)→ TorZ(Hn−1(X),k )→ 0,
natural in X. These sequence split, so Hn(X;k)∼= Hn(X)⊕ TorZ(Hn−1(X),k ),
but the splitting cannot be chosen naturally in X.
A ﬁrst task will be to explain what Tor is.
16.2. Tor. Fix a commutative ring R (for instance Z) and an R-module Q. We
investigate the eﬀect on exact sequences of the functor ·⊗ Q from R-modules to
R-modules. (Later we may suppose that Q is actually an R-algebra, and think of
·⊗ Q as a functor from R-modules to Q-modules.)
Lemma 16.2. Let 0→ M1
i
→ M2
p
→ M3→ 0 be a short exact sequence of R-
modules. Let Q be another R-module. Then the induced sequence
M1⊗Q→M2⊗Q→M3⊗Q→ 0
is also exact. If the short exact sequence splits (for instance, if M3 is a free module)
then M1⊗Q→M2⊗Q is injective.
Proof. Takem3⊗q∈M3⊗Q. Say q =p(m2). Then (p⊗ id)(m2⊗q) = m3⊗q.
Hence p⊗ id is onto.
Now, (p⊗ id)◦ (i⊗ id) = ( p◦ i)⊗ id = 0, and hence there is an induced
map [p⊗ id]: (M2⊗Q)/ im(i⊗ id) → M3⊗Q. Exactness of the sequence at
M2⊗Q is equivalent to the assertion that [ p⊗ id] is injective. But im( i⊗ id) =
imi⊗Q = kerp⊗Q, and hence we can deﬁne s: M3⊗Q→ (M2⊗Q)/ im(i⊗ id)
bys(m⊗q) = [p−1m⊗q]. We have s◦ [p⊗ id] = id, so [p⊗ id] is indeed injective.
Now suppose the sequence splits. Then there is a homomorphism l: M2→M2
withl◦i = id. Thus l⊗ id: M2⊗Q→M1⊗Q satisﬁes (l⊗ id)◦ (i⊗ id) = id⊗ id,
hence i⊗ id is injective. □
In general, i⊗ id is not injective, but its kernel can be measured by the intro-
duction of the ‘torsion products’. For simplicity, we assume R is Z, a ﬁeld, or more
generally a principal ideal domain (PID). A PID is a commutative ring R such that
(i)xy = 0 impliesx = 0 ory = 0, and (ii) every ideal is of form (x) ={ax :a∈R}.
The simpliﬁcation in the present context because ifR is a PID then every submodule
of a free R-module is free, i.e., has a basis. For the proof see, e.g., Lang’s Algebra,

54 TIM PERUTZ
Appendix 2 (in the general case, not restricted to ﬁnite rank free modules, this uses
Zorn’s lemma).
This has the following consequence: any R-module M has a two-step free reso-
lution, i.e. an exact sequence
0→F1
f1
→F0
f0
→M→ 0
withF0 andF1 free. Just take any generating set S forM, letF0 be free on S, and
let F1 be the kernel of the natural map F0→M.
Applying·⊗ Q to this sequence, we obtain a complex
0→F1⊗Q
f1⊗id
→ F0⊗Q
f0⊗id
→ M⊗Q→ 0
which is exact at M⊗Q and at F0⊗Q. We prefer to truncate this to the complex
0→F1⊗Q
f1⊗id
→ F0⊗Q→ 0.
By the lemma, its homology at F0⊗Q (i.e., the cokernel of f1⊗ id) is naturally
isomorphic to M⊗Q. We deﬁne Tor(M,Q ) to be its homology at F1⊗Q:
Tor(M,Q ) = kerf1⊗ id.
In brief: to deﬁne Tor, we took a free resolution of M, tensored it with Q, and
measured its failure to be exact by taking homology.
The next point is that Tor(M,Q ) is independent of the choice of free resolution.
It is convenient to think of 0 → F1→ F0 as a chain complex F∗, and of f0 as an
‘augmentation’ (F∗→M) of the complex.
Lemma 16.3. Take two free resolutions (F∗
f0
→M) and (G∗
g0
→M). Then there is
a chain map α: F∗→G∗ such that g0◦α =f0. Moreover, α is unique up to chain
homotopy.
The proof is left as an exercise.
Proposition 16.4. Tor(M,Q ) is independent of the choice of two-step free reso-
lution F∗→M→ 0.
Proof. In the notation of the last lemma, we have to compare the homologies of the
complexes F∗⊗Q and G∗⊗Q. But the lemma supplies us with an augmentation-
preserving chain maps α: F∗→ G∗ and β : G∗→ F∗. Moreover, the uniqueness
clause tells us that βα is chain homotopic to the identity; likewise αβ. Thus α⊗ id
andβ⊗ id give chain-homotopy equivalences betweenF∗⊗Q andG∗⊗Q, showing
that they have canonically isomorphic homologies. □
Example 16.5. • WhenR is a ﬁeld we may takeF0 =M andF1 = 0. Thus
Tor(M,Q ) = 0, consistent with our ﬁrst lemma.
• IfM is torsion-free over the PIDR, we may takeF0 =M have Tor(M,Q ) =
0 for any Q and F1 = 0. Hence Tor(M,Q ) = 0 for all Q.
• TheR-module M =R/(x) has the free resolution 0→R
x
→R→R/(x)→
0. Thus
Tor(R/(x),Q ) = ker(x⊗ id: R⊗Q→R⊗Q) = ker(x: Q→Q),
i.e., Tor(R/(x),Q ) is the x-torsion in Q. For instance, if p is prime then
Tor(R/(pn),R/ (p)) =R/(p).

ALGEBRAIC TOPOLOGY I: FALL 2008 55
16.3. Universal coeﬃcients.
Theorem 16.6 (Universal coeﬃcients) . Let C∗ be a chain complex of free R-
modules over a PID R. Then, for any R-moduleQ, one has short exact sequences
0→Hp(C∗)⊗Q
j
→Hp(C∗⊗Q)
p
→ Tor(Hp−1(C∗),Q )→ 0,
where the map j is induced by the inclusion kerdp⊗Q→ ker(dp⊗ idQ). These
sequences are functorial in C∗. They always split, but not in a natural way.
Proof of universal coeﬃcients. We let ip : Bp → Zp be the inclusion of the p-
boundaries into the p-cycles. From the free resolution
0→Bp
ip
→Zp→Hp(C∗)→ 0
for the homology Hp(C∗), we see that
coker(ip⊗ id) =Hp(C∗)⊗Q, ker(ip−1⊗ id) = Tor(Hp−1(C∗),Q ).
Now consider the short exact sequence
0→Zp→Cp
dp
→Bp−1→ 0.
Since the terms are free modules, the sequence splits, and so the sequence
0→Zp⊗Q
jp⊗id
→ Cp⊗Q
dp⊗id
→ Bp−1⊗Q→ 0
is also exact. It is, moreover, a short exact sequence of chain complexes, so it induces
a long exact sequence of homology groups. With a little thought one identiﬁes the
connecting maps; the long exact sequence reads
···→ Hp+1(C∗⊗Q)→Bp⊗Q
ip⊗id
→ Zp⊗Q→Hp(C∗⊗Q)→...,
with ip : Bp→ Zp the inclusion. Its exactness tells us that there are short exact
sequences
0→ coker(ip⊗ id)→Hp(C∗⊗Q)→ ker(ip−1⊗ id)→ 0,
i.e.,
0→Hp(C∗)⊗Q→Hp(C∗⊗Q)→ Tor(Hp−1(C∗),Q )→ 0.
It is left as an exercise to think through why the map on the left is j. A splitting
arises from a chosen splitting of 0 → Zp→ Cp
dp
→ Bp−1→ 0; again, this is left as
an exercise.
It is also left as an exercise to see that the whole sequence is functorial in C∗.
The non-naturality of the splittings will follow from a topological example in one
of the exercises below. □
Notice that ifQ is a commutativeR-algebra, thenHp(C∗)⊗Q and Tor(Hp−1(C∗),Q )
are naturally Q-modules. And, rather obviously, the universal coeﬃcients theorem
is valid as a statement about Q-modules. In particular taking R = Z and Q = k,
we obtain the topological universal coeﬃcients theorem stated at the outset.
Exercise 16.1: Compute H∗(K), whereK is the Klein bottle. Now compute H∗(K; Z/2n)
(i) by a direct argument, and (ii) using universal coeﬃcients.

56 TIM PERUTZ
Exercise 16.2: Prove that the splittings of the universal coeﬃcient theorem cannot
be chosen naturally in X by means of the following example. Take an embedding
i: R2 → RP 2, let D = i({z ∈ R2 : |z| < 1}), and let q be the quotient map
RP 2→ RP 2/(RP 2\D)∼=S2. Show that the k = Z/2 universal coeﬃcients sequences
for RP 2 and S2 cannot be split compatibly with q.
Exercise 16.3: This exercise develops an alternative approach to a special case of uni-
versal coeﬃcients. Let C∗ be a chain complex of free abelian groups. Show that
tensoring by the short exact sequence 0→ Z→ Z→ Z/n→ 0 gives rise to a short
exact sequence of chain complexes 0→C∗→C∗→C∗⊗ Z/n→ 0. By analyzing the
resulting long exact sequence of homology groups, deduce a short exact sequence
0→Hp(C∗)⊗Z Z/n→Hp(C∗⊗ Z/n)→{x∈Hp−1(C∗) :nx = 0}→ 0.

ALGEBRAIC TOPOLOGY I: FALL 2008 57
III. Cellular homology
17. CW complexes
We introduce a manageable category of spaces and maps, the category of CW
complexes and cellular maps.
CW complexes are a particularly convenient and useful class of spaces to work
with, for a number of reasons.
• There is an eﬃcient and geometrically clear way of computing the homology
groups of a CW complex.
• Maps between CW complexes behave far better than maps between general
spaces: a weak homotopy equivalence between CW complexes is a homotopy
equivalence. A weak equivalence f : X→Y is a map which induces bijec-
tions hTop(Sn,X )→ hTop(Sn,Y ),h↦→f◦h for alln (here hTop(Sn,X )
denotes the set of homotopy class of maps).
• One can localise the category hTop, artiﬁcially inverting the weak equiva-
lences to form the topological derived category. Simplistically, performing
this localisation is equivalent to working with CW complexes. The precise
statement is that the topological derived category is equivalent to the ho-
motopy category of CW spectra, see C. Weibel, Introduction to homological
algebra, Chapter 10.
• On a smooth compact manifold M, a Morse function gives rise to a cell
structure making M a CW complex.
Deﬁnition 17.1. The n-cell en is the closed unit disc Dn⊂ Rn. For n >0, its
boundary is ∂en = Sn−1. We put ∂e0 =∅. If A is a space, and f : Sn−1→ A a
map, we can build a space
Cf =en∪f A = (A∐en)/∼ where f(x)∼x for x∈∂en.
We say thatA∪fen results from attaching an n-cell toA via the attaching map f.
The notation Cf refers to the general notion of the ‘homotopy coﬁber’ Cf =
CX∪f Y of a map f : X→Y , where CX =X×I/X×{ 1} is the cone on X.
Example 17.2. Letc: Sn−1→e0 be the constant map. Then Sn∼=Cc =en∪ce0.
Two crucial observations are:
• that Cf containsA as a closed subspace; and
• that the quotient Cf/A is homeomorphic to en/∂en, hence to Sn.
More generally, given an indexing set I and a map f =∐
i∈Ifi : ∐
i∈I∂en→ A,
we can build a space
Cf = (A∐
∐
i
en)/∼ where fi(x)∼x for x∈∂en.
The images of the fi need not be disjoint. We say Cf is obtained by attaching
n-cells to A.
Note that Cf/A∼=⋁
i∈ISn.
Deﬁnition 17.3. A cell complex of dimension ≤ d is a space X together with a
sequence of closed subspaces
∅ =X−1⊂X0⊂X1⊂···⊂ Xd =X

58 TIM PERUTZ
such that eachXk+1 is obtained fromXk by attaching a (possibly empty) collection
of n-cells. We call Xk the k-skeleton of X. A cell complex is a space X together
with a sequence of closed subspaces
∅ =X−1⊂X0⊂X1⊂X2⊂...
such thatX =⋃
kXk. A cell complex is a CW complex ifX has the weak topology,
i.e. U⊂X is open iﬀ U∩Xk is open in Xk for each k.
(I’m not sure how standard my usage of the term ‘cell complex’ is here. However,
the term ‘CW complex’ is certainly standard.)
Mostly we shall work with cell complexes with ﬁnitely many cells, which are
automatically CW complexes.
Remark. It is perhaps a pity that J. H. C. Whitehead’s term ‘CW complex’, which
refers to certain technical properties, has not been replaced by something more
descriptive. ‘W’ is for ‘weak topology’; ‘C’ for ‘closure ﬁniteness’, the property
that the image of each closed cell intersects the interiors of only ﬁnitely many cells
of lower dimension. In this as in other aspects of algebraic topology, there were
many possible variants of the deﬁnition—the ones that we use lead to a streamlined
theory, and most of the others do not, but this is far from obvious.
Example 17.4. A graph is just a CW complex of dimension ≤ 1.
Example 17.5. The ‘Hawaiian earring’, i.e. the union ⋃
n≥1Cn of circles Cn in
R2 of radius n−1 centered at n−1, is naturally a cell complex, but the topology
inherited from R2 does not make it a CW complex ( ⋃C2n\{ 0} is open in the
weak topology but not the subspace topology).
Example 17.6. The 2-torus T 2 has the structure of a CW complex with one 0-
cell, one 1-cell (so the 1-skeleton is S1) and one 2-cell. The same goes for the Klein
bottle K2. The real projective plane RP 2 has the structure of a CW complex with
two 0-cells, one 1-cell and one 2-cell.
Example 17.7. Complex projective space CPn = (Cn+1\{0})/C∗ is a cell complex
e2n∪e2n−2∪···∪ e0. To see this, deﬁne
X2k ={[z0,...,z n]∈ CPn :zj = 0 for all j >k}.
Thus X0 ⊂ X2 ⊂ ··· ⊂X2n = CPn, and X2k ∼= CPk. We will exhibit X2k
as the 2k-skeleton of a cell decomposition. If [ z]∈ X2k\X2(k−1) ⊂ CPn then
zk+1 =··· = zn = 0 but zk⁄= 0, so [ z] = [w1,...,w k−1, 1, 0..., 0] for a unique
(w0,...,w k−1)∈ Ck. Thus X2k\X2(k−1)∼= Ck. Thus CPn is a disjoint union of
open cells, one of each even dimension up to 2 n. To see that they are attached in
the proper way, think of e2k as{w = (w0,...,w k−1)∈ Ck :|w|≤ 1} and deﬁne
i2k : e2k→X2k−2 as follows:
ik(w) = (w0,...,w k−1, (1−|w|2)1/2, 0,..., 0).
This map extends to a homeomorphism e2k∪fk X2k−2→ Xk which restricts to
the inclusion on X2k−2, where fk : S2k−1 → X2k−2 is given by fk(ζ0,...,ζ k) =
[ζ0,...,ζ k, 0,..., 0].
Example 17.8. Let C[t] be the C-vector space of polynomials int. Denote by CP∞
its projective space ( C[t]\{ 0})/C∗. Then CP∞ is a CW complex with 2k-skeleton
(and 2k + 1-skeleton) CPk.

ALGEBRAIC TOPOLOGY I: FALL 2008 59
17.1. Compact generation. CW complexes are examples of compactly generated
spaces. A space X is compactly generated if (i) it is ‘weak Hausdorﬀ’, meaning
that any compact Hausdorﬀ subspace is closed, and (ii) every ‘compactly closed’
subspace is closed. Here a subspace A⊂X is compactly closed if g−1(A) is closed
in K for every compact Hausdorﬀ space K and every map g : K→X.
There’s a functor k from weak Hausdorﬀ spaces to compactly generated spaces
(the closed sets ofkX are the compactly closed sets ofX). Algebraic topologists like
to work in the category of compactly generated spaces because compact generation
is a more intrinsic notion than that of a (space homotopy equivalent to a) CW
complex, and because this category has excellent properties. The quotient of a
compactly generated space by a closed equivalence relation is compactly generated.
The direct limit of compactly generated spaces is compactly generated. Deﬁne a
product X×Y in this category to be k(X×Y ) (k applied to the usual product);
and deﬁne YX as kMap(X,Y ) where Map(X,Y ) has its compact–open topology.
Then the canonical bijection ZX×Y ∼= (ZY )X is a homeomorphism. For instance,
a homotopy I×X→Y is the same thing as a map X→YI.
17.2. Degree matrices. A good deal of information about how a CW complex
X =⋃
kXk is built is encoded in its ‘degree matrices’ Dn.
Suppose that for eachn, one has a labelling of then-cells ase1,...,e N(n). Deﬁne
an N(n− 1)×N(n) matrix Dn with integer entries as follows: the matrix entry
Dij
n is equal to the degree of the map
πj◦qn−1◦fi : Sn−1→Sn−1,
where fi : Sn−1→Xn−1 is the attaching map for ei; qn−1 : Xn−1→Xn−1/Xn−2
the quotient map; and πj : Xn−1/Xn−2 = ⋁
jSn−1→ Sn−1 the map which col-
lapses all the spheres in the wedge except the jth.
Exercise 17.1: Compute degree matrices for the above-mentioned CW structures on
T 2, RP 2 and K2.
Remark. The degree matrix has a geometric interpretation in Morse theory. Fix a
smooth Riemannian manifold (M,g ). If f is a Morse function on M then the union
of the unstable manifolds (with respect to g) of the critical points is a subspace M′
such that M′→M is a homotopy equivalence. M′ has a canonical cell decompo-
sition in which the p-cells are the unstable manifolds of the index p critical points
ci
p. If now cj
p−1 is an index p− 1 critical point then the matrix entry Dp
ij for the
cell decomposition is the signed count of downward gradient ﬂow lines from ci
p to
cj
p−1. (To make this count ﬁnite and meaningful, we perturb the pair ( f,g ) so that
it satisﬁes the ‘Morse–Smale’ transversality condition.)
17.3. Cellular approximation. The following theorem is not especially diﬃcult
to prove, but we shall nonetheless omit the proof.
Theorem 17.9 (Cellular approximation of maps). Letf : X→Y be a map between
CW complexes. Then f is homotopic to a cellular map, i.e. a map g such that
g(Xk)⊂Yk for all k.
The next theorem is best proved using a little homotopy theory. Again we shall
omit the proof.
Theorem 17.10 (CW approximation of spaces). There is a procedure which assigns
to any space X a CW complex Γ(X) and a weak homotopy equivalence ΓX→X.

60 TIM PERUTZ
Moreover, the procedure can be made functorial, in the sense that if f : X→Y is
a map then there is a map Γf : ΓX→ ΓY so that the obvious square commutes up
to homotopy.
This theorem has an important consequence. If one wants to prove a theorem
about the homology of general spaces, it suﬃces to prove it for CW complexes; by
cellular approximation of maps, one can also take the maps to be cellular.

ALGEBRAIC TOPOLOGY I: FALL 2008 61
18. Cellular homology
We compute the singular homology of cell complexes in terms of the cells and
the degree matrix obtained from their attaching maps.
Let X be a CW complex, and Xk its k-skeleton; thus
∅ =X−1⊂X0⊂X1⊂X2⊂···⊂
⋃
k≥0
Xk =X.
We wish to compute H∗(X) in terms of the cells and their attaching maps.
One of the convenient properties of CW complexes is that the subspace Xn−1
of Xn has an open neighbourhood U which deformation-retracts to Xn−1. Also
Xn−1 is closed inXn. Hence (this was an exercise using the excision theorem), one
has H∗(Xn,Xn−1) = ˜H∗(Xn/Xn−1) when Xn−1⁄=∅.
Now, the idea of our calculation is to exploit the fact that Xn/Xn−1 is a very
simple space:
Xn/Xn−1∼=
⋁
n-cells
Dn+1/∂Dn+1 =
⋁
n-cells
Sn.
ThusHn(Xn,Xn−1) = Z{n-cells}.
Deﬁne δn+1 as the connecting homomorphism
Hn+1(Xn+1,Xn)
δn+1
→ Hn(Xn)
from the exact sequence of the pair ( Xn+1,Xn). Deﬁne qn as the natural map
Hn(Xn)
qn
→Hn(Xn,Xn−1).
Theorem 18.1. Let Cn = Hn(Xn,Xn−1) = Z{n-cells}. Deﬁne dn = qn−1◦
δn : Cn → Cn−1. Then one has dn◦dn+1 = 0 . The homology Hn(C∗) of the
chain complex
···→ Cn+1
dn+1
→ Cn
dn
→Cn−1→...
is canonically isomorphic to the singular homology Hn(X).
This theorem is very useful as a computational tool, as we will see next time.
For now, we record two simple corollaries.
Corollary 18.2. If X is a d-dimensional CW complex then Hn(X) = 0 for all
n > d. If X is a CW complex with a ﬁnite number l of n-cells then the rank of
Hn(X) is ﬁnite and ≤l.
Corollary 18.3. If X is a CW with only even-dimensional cells then Hn(X) =
Z{n-cells} for all n. In particular, H∗(CPn) = Z(0)⊕ Z(2)⊕···⊕ Z(2n), where the
subscripts denote degrees of the Z-summands.
Proof of the theorem. We will simplify by assuming that X is ﬁnite-dimensional,
i.e., that X = Xd for some d≥ 0. We also assume that X ⁄=∅, which forces
X0⁄=∅.
Step 1. We have already mentioned this step. By excision (which applies because
Xn−1 is a deformation retract of an open neighbourhood in Xn) one has, forn> 0,
Hk(Xn,Xn−1)∼=Hk(
⋁
n-cells
Sn,∗) = ˜Hk(
⋁
n-cells
Sn)∼=
⨁
n-cells
˜Hk(Sn).
Thus one has
Hn(Xn,Xn−1)∼= Z{n-cells},

62 TIM PERUTZ
and this is valid even when n = 0.
Step 2. From the long exact sequence of the pair (Xn,Xn−1), one sees that, for
k>n ≥ 0,Hk(Xn) =Hk(Xn−1), and thus iteratively Hk(Xn) =Hk(X0) = 0. So,
when X =Xd, X has homology only up to dimension d.
Step 3. From the long exact sequence of the pair (Xn+1,Xn), one sees that, for
k<n +1, Hk(Xn) =Hk(Xn+1). Thus, iteratively,Hk(Xn) =Hk(Xn+p) =Hk(X)
since Xn+p =X for all n +p≥d. So to compute nth homology we can get away
with considering the n + 1-skeleton ofX:
Hn(X) =Hn(Xn+1)
Step 4. Part of the long exact sequence of the pair ( Xn+1,Xn) reads
Hn+1(Xn+1,Xn)
δn+1
→ Hn(Xn)→Hn(Xn+1)→ 0.
Thus Hn(X) = Hn(Xn+1) is isomorphic to coker δn+1. This represents progress,
since the domain of δn+1 is a known group Z{(n+1)-cells}.
Step 5. The target of δn+1, Hn(Xn), sits in another exact sequence
0→Hn(Xn)
qn
→Hn(Xn,Xn−1)→Hn−1(Xn−1)
(the zero on the left comes from Step 3). So, crucially, the map qn is injective. Let
dn+1 =qn◦δn+1. Here’s the tricky step: one has
Hn(X)∼=Hn(Xn)/ imδn+1∼= imqn/ imdn+1,
since qn carries Hn(Xn) isomorphically to im qn and im δn+1 isomorphically to
imdn+1.
Step 6. One has
imqn = ker
(
δn : Hn(Xn,Xn−1)→Hn−1(Xn−1)
)
= ker
(
dn−1 : Hn(Xn,Xn−1)→Hn(Xn−1,Xn−2)
)
.
Thus
Hn(X)∼=Hn(Xn)/ imδ∼= kerdn/ imdn+1.
Note that dn◦dn+1 = 0 because δn◦qn = 0. □
Remark. Let us make a note of what we have used in the proof. We needed excision
and the long exact sequence of the pair. We also needed the fact that the reduced
homology of a wedge is the direct sum of the reduced homologies. We needed
to know that ˜H∗(Sn) = Z(n). Recall that this was proved using excision (and
homotopy invariance of singular homology) by an inductive argument beginning
with ˜Hk(S0) = Z.
We have Cn = Z{n-cells} and Cn−1 = Z{(n−1)-cells}, so dn is represented by an
integer-valued matrix (Dij
n ):
Dn⟨i⟩ =
∑
j
Dij
n⟨j⟩,
where⟨i⟩ represents an n-cell and the sum is over (n− 1)-cells j.
Theorem 18.4. For any n > 1, the matrix Dn representing the diﬀerential dn
is equal to the degree matrix for the cellular attachments. The diﬀerential d1 is
characterized by d⟨i⟩ =⟨fi(1)⟩−⟨ fi(0)⟩.

ALGEBRAIC TOPOLOGY I: FALL 2008 63
Proof. We can think of the closure of the cell ek as an k-simplex (since it is home-
omorphic to ∆k. Thus the ith Z-summand in Hn(Xn,Xn−1) is represented by the
cell ei
n, considered as a singular chain (notice that it is a relative n-cycle, since its
boundary lies in Xn).
Under δn, the singular chain ei
n is mapped to its boundary, which is the image
of the fundamental class [Sn]∈Hn(Sn) under the cellular attaching map fi: that
is, δnei
n = (fi)∗[Sn−1]. Next we have to apply the quotient map qn : Xn−1 →
Xn−1/Xn−2, since dn(ei
n) = (qn−1)∗(fi)∗[Sn−1]∈Hn(Xn−1/Xn−2).
The projection Hn(Xn−1/Xn−2)→ Z to the jth Z-summand is induced by the
collapsing map
πj : Xn−1/Xn−2 =
⋁
(n−1)−cells
Sn−1→Sn−1
which acts as the identity on jth copy of Sn−1 and sends everything else to the
wedge point. Thus the jth component of δnei
n is
(πj)∗(qn−1)∗(fi)∗[Sn−1] = (πj◦qn−1◦fi)∗[Sn−1]∈Hn−1(Sn−1).
But this is exactly the deﬁnition of the degree matrix Dn. □

64 TIM PERUTZ
19. Cellular homology calculations
We compute some examples of cellular homology, and observe the uniqueness of
homology theories.
We begin by repeating the theorem from last time:
Theorem 19.1. If X is a CW complex then the homology of the cellular complex
(C∗,d ) is canonically isomorphic to H∗(X). Here Cn = Z{n-cells} and Cn−1 =
Z{(n−1)-cells}, so the cellular diﬀerential dn is represented by an integer-valued ma-
trix (Dij
n ):
Dn⟨i⟩ =
∑
j
Dij
n⟨j⟩,
where⟨i⟩ represents an n-cell and the sum is over (n− 1)-cells j.
When n > 1, the matrix entry Dij
n is the degree of πj◦Qn−1◦fi : Sn−1 →
Sn−1, where fi is the attaching map of the ith n-cell, Qn : Xn−1→Xn−1/Xn−2 =⋁
(n−1)−cellsSn−1 the quotient map, and πj : Xn−1/Xn−2→ Sn−1 the collapsing
map on the jth wedge-summand. The diﬀerential d1 is characterized by d1⟨i⟩ =
⟨fi(1)⟩−⟨ fi(0)⟩.
19.1. Calculations. Let us use this theorem to compute the homology ofT 2, RP 2
and K2. The homology vanishes in degrees > 2, because these are 2-dimensional
cell complexes, but the interesting thing is to compute H1 and H2.
• X =T 2 has an obvious cell decomposition with one 0-cell, two 1-cells and
one 2-cell. These cells give bases v0 for C0, (va
1,vb
1) for C1, and v2 for C2.
One has d1va
1 = v0−v0 = 0 = d1vb
1. The attaching map for the 2-cell is
a map S1→ S1
a∨S1
b . For T 2 it is aba−1b−1, so after collapsing S1
b we
get a map homotopic to a·a−1 : S1→S1
a (which has degree 0), and after
collapsingS1
b we get a map homotopic to b·b−1 : S1→S1
b (alslo degree 0).
Hence d2v2 = 0. So H2(T 2) = Z and H1(T 2) = Z2.
• X = K2 has a cell decomposition with X0 = e0, X1 = ea
1∪eb
1∪X0, and
X = X2 = e2∪X1. These cells give bases v0 for C0, (va
1,vb
1) for C1, and
v2 for C2. As for T 2, one has d1 = 0. The attaching map for e2 is aba−1b,
so d2v2 = 2vb
1. Hence H2(K2) = 0 and H1(K2) = Z⊕ (Z/2).
• X = RP 2 has a cell decomposition with two 0-cells, two 1-cells, and one
2-cell. These cells give bases ( v0,v′
0) for C0, (va
1,vb
1) for C1, and v2 for C2.
Our conventions are such that d1(va
1) = v′
0−v0 =−d1(vb
1); thus ker d1 =
Z(va
1 +vb
1). The attaching map for e2 is then abab, so d2v2 = 2va
1 + 2vb
1.
Hence H2(K2) = 0 and H1(K2) = Z/2.
Happily, these calculations are consistent with our earlier results concerning π1.
Example 19.2. Real projective space RPn = (Rn+1\{ 0})/R∗ is a cell complex
with one k-cell of each dimension k∈{ 0, 1,...,n }. To see this, deﬁne
Xk ={[x0 :··· :xn]∈ RPn :xj = 0 for all j >k}.
ThusX0⊂X1⊂···⊂ Xn = RPn, and Xk∼= RPk. We will exhibit Xk as the k-
skeleton of a cell decomposition. If [x]∈Xk\Xk−1⊂ RPn thenxk+1 =··· =xn =
0 but xk⁄= 0, so [x] = [y0 :...,y k−1 : 1 : 0··· : 0] for a unique (y0,...,y k−1)∈ Rk.
Thus Xk\Xk−1∼= Rk. Thus RPn is a disjoint union of open cells, one of each
dimension up to n. To see that they are attached in the proper way, think of ek as

ALGEBRAIC TOPOLOGY I: FALL 2008 65
{y = (y0,··· :yk−1)∈ Rk :|y|≤ 1} and deﬁne ik : ek→Xk as follows:
ik(y) = (y0 :··· :yk−1 : (1−|y|2)1/2 : 0 :··· : 0).
Then ik is injective on the interior of ek, but restricts to ∂ek = Sk−1 as the map
fk(ζ0,...,ζ k−1) = [ζ0 : ...,ζ k−1 : 0 : ··· : 0] which is the quotient map Sk−1→
Xk−1 = RPk−1. Notice that ik extends to a homeomorphism ek∪fk Xk−1→Xk
which restricts to the inclusion on Xk−1.
To compute the cellular chain complex, we need to look at the composite Qk−1◦
fk, where Qk−1 : Xk−1→ Xk−1/Xk−2 = Sk−1 is the collapsing map. Well, when
|y| = 1, we have fk(y0,...,y k−1) = [y0 :··· : yk−1 : 0 : ... 0]. Thus fk(y)∈ Xk−2
precisely when yk−1 = 0. Cut Sk−1 into two hemispheres Dk−1
± ={(y0,...,y k−1) :
|y| = 1,±yk−1≥ 0}. Then, if y∈ int(Dk−1
+ ), we have
i−1
k−1◦fk(y) =i−1
k−1◦ik(y)
=i−1
k−1(y0 :··· :yk−1 : 0 :··· : 0)
= (y0,...,y k−2)
(check the last line for yourself!). If y∈ int(Dk−1
+ ), then we have instead
i−1
k−1◦fk(y) = (−y0,..., −yk−2).
We now see that the cellular diﬀerential dk is given by dk⟨ek⟩→ λ⟨ek−1⟩, where λ
is the degree of the composite map
Sk−1 p
→Sk−1∨Sk−1 id∨a
→ Sk−1.
Here p is the ‘pinching map’ that collapses the equator to the wedge point. The
second map acts as the identity on the ﬁrst wedge summand Sk−1
+ and as the
antipodal mapa on the second wedge summandSk−1
− . Now, on fundamental classes
we havep∗[Sk−1] = [Sk−1]+ + [Sk−1]−, whilst (id∨a)∗ maps [Sk−1]+ + [Sk−1]− to
(1 + deg(a))[Sk−1] = (1 + (−1))[Sk−1]. Thus λ = 1 + (−1)k.
Hence the cellular complex reads
···→ Z
0
→ Z
2
→ Z
0
→ Z→ 0.
So we ﬁnd the following: if n is even then
Hk(RPn) =



Z, k = 0,
Z/2, k<n odd
0, k<n even
0, p ≥n.
If n is odd then
Hk(RPn) =



Z, k = 0,
Z/2, k<n odd
0, k<n even
Z, k =n,
0, p>n.

66 TIM PERUTZ
Taking the last example further, let’s now calculate H∗(RPn; Z/2). We can do
this in two ways. One way is to use the cellular chain complex reduced mod 2,
which reads
0→ Z/2→ Z/2→···→ Z/2→ 0
with a Z/2 in each degree between 0 and n. The maps are all zero. Hence
Hi(RPn; Z/2) = Z/2 if 0≤i≤n, and it is zero otherwise.
The other method is to use our calculation for Z-coeﬃcients in conjunction with
universal coeﬃcients. For n even, say, the Z/2-module Hk(RPn)⊗Z/2 is Z/2 for
k = 0 or 0 < k < nodd, and 0 otherwise. However, Tor( Hk−1(RPn), Z/2) is Z/2
if k− 1 > 0 with k even, and is zero otherwise. Thus for any k between 0 and n,
the ﬂanking terms in the universal coeﬃcients exact sequence
0→Hk(RPn; Z)⊗Z Z/2→Hk(RPn; Z/2)→ Tor(Hk−1(RPn), Z/2)→ 0
always consist of Z/2 and 0 (in some order), hence Hk(RPn; Z/2) = Z/2.
Exercise 19.1: Compute H∗(RPn; Z/4). Do it in two ways: via the Z/4 cellular chain
complex; and via the homology over Z and universal coeﬃcients.
Exercise 19.2: Use cellular homology to compute H∗(Σg), where Σg is a standard
closed, orientable surface of genus g (deﬁned, for instance, as a quotient of the 4g-
gon). Also, compute H∗(Σg#RP 2), the connected sum of Σg and RP 2.
Exercise 19.3: Describe how the product X×Y of ﬁnite CW complexes X and Y
inherits a structure of CW complex.
(1) Compute the Euler characteristic χ(X×Y ) in terms of χ(X) and χ(Y ).
(2) Show that Ccell
∗ (X×Y ) = Ccell
∗ (X)⊗Ccell
∗ (Y ) as a graded abelian group.
(You are not asked to compute the diﬀerential.)
(3) Compute H∗(Sn×Sn).
(4) Let X = (S3)×n = S3×···× S3. Show that H3p(X) is isomorphic to the
exterior power ΛpZn, and that Hq(X) = 0 if q is not a multiple of 3.

ALGEBRAIC TOPOLOGY I: FALL 2008 67
20. The Eilenberg–Steenrod axioms
We show that the Eilenberg–Steenrod axioms uniquely characterize a homology
theory for CW pairs.
A CW pair (X,A ) is a CW complexX and a subspaceA which is a subcomplex,
i.e. it is a union of cells of X which form a CW complex.
Deﬁnition 20.1. An Eilenberg–Steenrod homology theory E∗ on CW pairs as-
signs:
• To each CW pair ( X,A ), and each integer n, an abelian group En(X,A )
(and we write En(X) for En(X,∅)).
• To each map f : (X,A )→ (X′,A′) and each n∈ Z it assigns a homomor-
phismEn(f): En(X,A )→Hn(X′,A′). One has En(f◦g) =En(f)◦En(g)
andEn(id(X,A)) = idEn(X,A). If f0 is homotopic to f1 via a homotopy{ft}
such that ft|A =f0|A, then En(f1) =En(f0).
• To each pair of spaces ( X,A ), and each integer n, it assigns a homomor-
phism
δn : En(X,A )→En−1(A).
These maps are natural transformations. That is, given f : (X,A ) →
(X′,A′), one has
δn◦En(f) =En−1(f)◦δn
as homomorphisms En(X,A )→En−1(A′).
Besides these basic properties, the following axioms are required to hold:
• DIMENSION: If∗ denotes a 1-point space then En(∗) = 0 for n⁄= 0, while
E0(∗) = Z.
• EXACTNESS: The sequence
···→ En(A)→En(X)→En(X,A )
δn
→En−1(A)→Hn−1(A)→...
is exact, where the unlabelled maps are induced by the inclusions ( A,∅)→
(X,∅) and (X,∅)→ (X,A ).
• EXCISION: if (X;A,B ) is an excisive triad then the map
En(A,A∩B)→En(X,B )
induced by the inclusion (A,A∩B)→ (X,B ) is an isomorphism.
• ADDITIVITY: If (Xα,Aα) is a family of pairs, then one has an isomorphism
⨁
α
En(Xα,Aα)→En(
∐
α
Xα,
∐
α
Aα)
given by the sum of the maps induced by the inclusions into the disjoint
union.
Theorem 20.2 (Eilenberg–Steenrod). Take any homology theoryE∗ on CW pairs.
Then for any CW complex X, one has En(X,A )∼= Hn(X,A ). In fact, there is a
unique natural transformation E∗→ H∗ extending a given isomorphism E∗(∗)→
H∗(∗), and this natural transformation is a natural isomorphism.
Remark. The Eilenberg–Steenrod theorem is one of two general organising princi-
ples for (co)homology theories. The other is sheaf cohomology: the idea that one
can use diﬀerent resolutions of the same sheaf to compute its cohomology. This
leads to a proof that singular cohomology is isomorphic to ˇCech cohomology, and

68 TIM PERUTZ
that the real cohomology H∗(M; R) of a smooth manifold is isomorphic to its de
Rham cohomology H∗
dR(M).
We will not give a complete proof of the theorem: for a start, we will restrict our
attention, for simplicity’s sake, to ﬁnite-dimensional CW complexes. We will prove
the existence of the natural isomorphism, but not its uniqueness. We will also not
prove that the natural transformations δn are uniquely determined.
Proof. We have already proved the heart of this theorem in showing thatH∗(X)∼=
Hcell
∗ (X), for our proof only used properties of singular homology derivable from
the axioms.
To ﬂesh this out, it is more convenient to work with reduced homology theories.
Let’s put ˜En(X) =En(X,{b}), where the basepointb∈X is one of the 0-simplices.
Then ˜En deﬁnes a ‘reduced homology theory’ on based CW complexes, satisfying
analogues of the axioms above. To state them, we need the notion of thereduced sus-
pension ΣX ofX: ΣX = (X× [−1, 1])/∼, where (x, 1)∼ (y, 1), (x,−1)∼ (y,−1),
and (unlike the unreduced suspension) ( b,s )∼ (b,t ), where b is the basepoint. It
is made a CW complex by thinking of it as the ‘smash product’
S1∧X = (S1×X)/(S1∨X)
(think this through). In general, the reduced suspension diﬀers from the unreduced
suspension. However, one still has Σ Sn∼= Sn+1. A map f : X → Y preserving
basepoints induces Σf : ΣX→ ΣY in a functorial manner.
The new axioms are as follows.
• DIMENSION: ˜E∗(S0) = Z.
• EXACTNESS: if A is a CW subcomplex containing b then the sequence
˜E∗(A)→ ˜E∗(X)→ ˜E∗(X/A)
is exact.
• SUSPENSION: There is a natural (in X) isomorphism
Σ: ˜E∗(X)→ ˜E∗+1(ΣX).
• ADDITIVITY: The natural map ⨁
i ˜E∗(Xi)→ ˜E∗(⋁
iXi) is an isomor-
phism. Here the Xi are based CW complexes, and ⋁
iXi their wedge sum
along the basepoints.
Exercise 20.1: Show that if E∗ is a homology theory then ˜E∗ is a reduced homology
theory.
Let CE
∗ (X) be the cellular chain complex deﬁned via ˜E∗:
CE
∗ (X) = ˜E∗(Xn/Xn−1).
We can run our proof from two lectures ago to show that ˜En(X)∼= Hn( ˜CE
∗ (X)),
where ˜CE
∗ (X) is the reduced cellular chain complex CE
∗ (X)/CE
∗ (b). (This necessi-
tates some slight adjustments in degree 0; otherwise the argument is identical.) To
be precise, the argument shows that we can obtain an isomorphism
α: ˜En(X)→Hn( ˜CE
∗ (X))
as follows: x∈ ˜En(X) lifts to some ˆx∈ ˜En(Xn). We deﬁne α(x) as the image of ˆx
in ˜En(Xn/Xn−1).
The dimension and suspension axioms tell us that ˜E∗(Sn)∼= Z(n), and hence that
˜En(Xn/Xn−1) = Z{n−cells}. As before, the cellular diﬀerential may be identiﬁed

ALGEBRAIC TOPOLOGY I: FALL 2008 69
with a degree matrix, but at this point we hit a snag. The degree matrix is computed
using ˜E∗ rather than ordinary homology. Do these degrees agree?
Let f : Sn→ Sn be a map preserving a basepoint. It has a homology degree
and an ˜E∗-degree, and we would like to prove that they are the same. This is easy
to check for S0, and quite easy also for S1, where we know that every map f is
homotopic rel basepoint to z ↦→ zd for some d∈ Z. We can try to prove it in
general by induction onn, using naturality of the suspension isomorphism, but this
will only work for maps f homotopic to Σg for some g : Sn−1→ Sn−1. Does this
exhaust all possible maps Sn→Sn? Yes. This can be seen as a special case of the
Hurewicz theorem, one of the basic principles of homotopy theory. Alternatively,
it can be proved using a little diﬀerential topology (see Milnor, Topology from the
diﬀerentiable viewpoint).
The upshot is that the cellular chain complexes as deﬁned via˜E∗ and ˜H∗ coincide.
We deduce an isomorphism
˜E∗(X)→ ˜H∗(X).
One now checks that this isomorphism is natural with respect to cellular maps
(those that send k-skeleta to k-skeleta) and so, by cellular approximation, with
respect to arbitrary based maps. We have now succeeded in rebuilding ˜E∗ (and
hence E∗) from the cellular homology of X.
We now recoverE∗ from its reduced theory ˜E∗. Indeed, it follows from excision
that the quotient map X→ X/A induces an isomorphism E∗(X,A )∼= ˜E∗(X/A)
when A⁄=∅; and one has E∗(X) = ˜E∗(X∐∗ ).
One can also recover the natural transformation δn, though this is trickier, and
I will omit it (see May chapters 14 and 8).
□

70 TIM PERUTZ
IV. Product structures
21. Cohomology
A cochain complex overR is a sequence of R-modules and maps
···→ Cp−1 dp−1
→ Cp dp
→Cp+1→..., p ∈ Z,
such that dp◦dp−1 = 0 for all p. It’s just the same as a chain complex, except
that the indexing runs the other way. We use superscripts for cochain complexes,
subscripts for chain complexes. We write C∗ = ⨁
pCp. The pth cohomology
module is then
Hp(C∗) = kerdp/ imdp−1,
and we put H∗(C∗) =⨁Hp(C∗).
If (D∗,∂ ) is a chain complex then one obtains a cochain complex by dualisation,
putting Cp = HomR(Dp,R ) and (dpf)(x) =f(∂p+1x).
Remark. It is not true that C∗ = HomR(D∗,R ), unlessCp = 0 for|p|≫ 0: one has
HomR(D∗,R ) =∏
pCp, which is usually bigger than ⨁
pCp.
If X is a space, one deﬁnes the singular cochains S∗(X;R) by
Sp(X;R) = HomZ(Sp(X),R ),
with the diﬀerentials dp deﬁned by dualising ∂:
(dpc)(σ) =c(∂σ) =
∑
i
(−1)ic(σ◦δi).
One then puts Hp(X;R) =Hp(S∗(X;R)). Note that singular cochains, and hence
singular cohomology, are contravariantly functorial: a map f : X → Y induces
f∗ : H∗(Y ;R)→H∗(X;R), and one has (f◦g)∗ =g∗◦f∗.
Relative cohomology Hp(X,A ;R) for a subspace i: A→ X is deﬁned as the
cohomology of ker(i∗ : S∗(X;R)→S∗(A;R)).
All the familiar properties of homology (long exact sequences of the pair, homo-
topy invariance, excision, Mayer–Vietoris, etc.) have dual versions in cohomology,
with essentially identical proofs. Note that the connecting maps in long exact
sequences go up not down in degree.
Exercise 21.1: Formulate these properties of cohomology, and think through how you
would prove them.
Theorem 21.1 (Dual universal coeﬃcients). IfX is a space, and R any commuta-
tive unital ring, there are natural (in X), non-naturally split short exact sequences
0→ Ext(Hp−1(X),R )
j
→Hp(X;R)
q
→ HomZ(Hp(X),R )→ 0.
In particular, there are non-canonical isomorphisms
Hn(X)∼= Hom(Hn(X), Z)⊕Hn−1(X)tors.
where the Ators denotes the torsion subgroup of A.
This is a direct consequence of an algebraic theorem given below.
Exercise 21.2: Show that H1(X;R)∼= HomZ(π1(X),R ) for path connected X. De-
duce that H1(X) = H1(X; Z) is a torsion-free abelian group for X locally path con-
nected X.

ALGEBRAIC TOPOLOGY I: FALL 2008 71
21.1. Ext. Fix a commutative ring R and an R-module P . We investigate the
eﬀect on exact sequences of the functor Hom( ·,P ) from R-modules to R-modules.
This problem is dual to the one we considered earlier involving tensor product,
because of the adjunction
Hom(M⊗Q,P )∼= Hom(Q, Hom(M,P )).
The arguments closely parallel those in the proof of homology universal coeﬃcients,
and we shall mostly leave the veriﬁcations to the reader to work through.
Lemma 21.2. Let 0→ M1
i
→ M2
p
→ M3→ 0 be a short exact sequence of R-
modules. Let P be another R-module. Then the induced sequence
0→ Hom(M3,P )
p∗
→ Hom(M2,P )
i∗
→ Hom(M1,P )
is also exact. If the short exact sequence splits (for instance, if M3 is a free module)
then Hom(M2,P )→ Hom(M1,P ) is surjective.
In general, i∗ is not surjective but its cokernel is measured by ‘Ext’. We assume
R is a PID, so (as discussed in the context of homology universal coeﬃcients) any
R-module M has a two-step free resolution
0→F1
f1
→F0
f0
→M→ 0.
Applying Hom(·,P ) to this sequence, we obtain a complex
0→ Hom(M,P )
f∗
0
→ Hom(F0,P )
f∗
1
→ Hom(F1,P )→ 0
which is exact at Hom(M,P ) and at Hom(F0,P ). We prefer to truncate this to the
(non-exact) sequence
0→ Hom(F0,P )
f∗
1
→ Hom(F1,P )→ 0.
which we think of as a cochain complex. By the lemma, its cohomology at Hom(F0,P )
(i.e., kerf∗
1 ) is naturally isomorphic to Hom(M,P ). We deﬁne Ext(M,P ) to be its
cohomology at Hom(F1,P ):
Ext(M,P ) = cokerf∗
1.
We showed in our treatment of Tor that given two free resolutions ( F∗
f0
→ M)
and (G∗
g0
→ M), there is a chain map α: F∗→ G∗, unique up to chain homotopy,
such that g0◦α =f0. This shows that Ext( M,P ) is independent of the choice of
free resolution, up to canonical isomorphism.
Remark. Those who have studied Ext in other contexts should note that one can
compute Ext(M,P ) from a projective resolution of M or an injective resolution of
P . We have opted for a special case of the former.
Example 21.3. • WhenR is a ﬁeld we may takeF0 =M andF1 = 0. Thus
Ext(M,P ) = 0 for all P .
• If M is a free module over the PID R, we may take F0 = M and F1 = 0.
Hence Ext(M,P ) = 0 for all P .

72 TIM PERUTZ
• The R-module M =R/(x) has free resolution 0 →R
x
→R→R/(x)→ 0.
Thus
Ext(R/(x),P ) = coker(x∗ : Hom(R,P )→ Hom(R,P ))
= coker(x: P→P )
=P/xP.
For instance, Ext(R/(x),R ) =R/(x). Since Ext commutes with direct sum
(on either factor), one deduces that for a ﬁnitely-generated R-module M
one has Ext(M,R ) =Mtors, the torsion submodule of M.
Theorem 21.4 (Dual universal coeﬃcients). LetC∗ be a chain complex of free R-
modules over a PID R. Then, for any R-moduleP , one has short exact sequences
0→ Ext(Hp−1(C∗),P )
j
→Hp(Hom(C∗,P ))
q
→ Hom(Hp(C∗),P )→ 0.
These sequences split, but there is no preferred splitting. In particular, taking P =
R, we get short exact sequences
0→Hp−1(C∗)tors
j
→Hp(C∨
∗ )
q
→Hp(C∗)∨→ 0,
where for any R-moduleM, M∨ denotes Hom(M,R ).
Proof. The proof is similar to that of the universal coeﬃcient theorem for tensor
products. We take for our free resolution of the homology groups
0→Bp
ip
→Zp→Hp(C∗)→ 0
(Bp and Zp are free because Bp⊂Zp⊂Cp). Thus we have
Ext(Hp−1(C∗),R ) = coker[i∗
p−1 : Hom(Zp−1,R )→ Hom(Bp−1,R )].
As in the tensor product argument, we have short exact sequences
0→Zp→Cp
∂p
→Bp−1→ 0
which split and therefore induce short exact sequences
0→ Hom(Bp−1,R )
dp
→ Hom(Cp,R )→ Hom(Zp,R )→ 0.
These constitute a short exact sequence of cochain complexes, and the resulting
long exact sequence on cohomology reads(!)
Hom(Zp−1,R )
i∗
p−1
→ Hom(Bp−1,R )
dp
→Hp(Hom(C∗,R ))→ Hom(Zp,R )
i∗
p
→ Hom(Bp,R ).
We deduce from this short exact sequences
0→ coker(i∗
p−1)→Hp(Hom(C∗,R ))→ ker(i∗
p)→ 0.
But keri∗
p = Hom(Hp(C∗),R ) and coker(i∗
p−1) = Ext(Hp−1(C∗),R ). These short
exact sequences split because Hom(Hp(C∗),R ) is a free R-module. □
Remark. The universal coeﬃcients theorems show thatH∗(X) determinesH∗(X;R)
and H∗(X;R) up to isomorphism, but not functorially. It is arguably better to
think of the singular chains as deﬁning functors Sn : hTop→ hCh, where the cat-
egory on the right is the category of chain complexes and chain homotopy classes
of chain maps. These functors can then be followed by algebraic functors ·⊗R and
Hom(·,R ).

ALGEBRAIC TOPOLOGY I: FALL 2008 73
Exercise 21.3: Work over Z and ﬁx distinct primes p andq. Compute (i) Ext(Z, Z/pn);
(ii) Ext(Z/pn, Z); (iii) Ext(Z/pn, Z/qm); (iv) Ext(Z/pn, Z/pm).
Exercise 21.4: Working over Z, compute Ext(A, Q/Z) for an arbitrary ﬁnitely generated
abelian group A.
Exercise 21.5: For any simply connected space X, one has H2(X)∼= Hom(H2(X), Z).
Exercise 21.6: Verify a case of the theorem by computing H∗(RP 2; Z) in two ways.
Do the same for H∗(RP 2; Z/2).
Exercise 21.7: What is the relation between H∗(X;R) and H∗(X)?

74 TIM PERUTZ
22. Product structures, formally
We explain the formal structure of the cup and cap products and state the
Poincar´ e duality theorem.
Homology and cohomology are much more powerful invariants when one takes
account of their multiplicative structures. The cohomology H∗(X) is a graded ring
under the cup product. Homology H∗(X) is not a ring, but it is a graded module
over the graded ring H∗(X). This is expressed by the cap product.
22.1. The evaluation pairing. The most basic product structure is the ‘evalua-
tion’ pairing
Hp(X)×Hp(X), (c,h )↦→⟨c,h⟩.
In singular theory, this is induced by the evaluation
Sp(X)×Sp(X) = Hom(Sp(X), Z)×Sp(X)→ Z;
similarly in cellular theory. One extends the evaluation pairing to a linear map
H∗(X)⊗H∗(X)→ Z
which is zero on Hp⊗Hq when p⁄=q.
Remark. It might be interesting to axiomatise this pairing in an arbitrary Eilenberg–
Steenrod theory. Over a ﬁeld k,Hn(·;k) is dual to Hn(·;k) in a functorial manner.
Over Z this is not so, but there are specialisation maps Hn(·)→ Hn(·; Z/p) and
Hn(·)→Hn(·; Z/p), so one could ask that an evaluation pairing should be naural,
and should specialise to the dual pairing between mod p homology and cohomology
for all primes p.
22.2. The cup product. The cup product is an associative bilinear product
H∗(X)×H∗(X)→H∗(X), (a,b )↦→a⌣b.
Its fundamental properties are as follows:
• One has Hp(X) ⌣ Hq(X)⊂ Hp+q(X). Thus ⌣ makes H∗(X) into a
graded ring.
• The ring has a unit element 1 ∈ H0(X): it is characterised by ⟨1,h⟩ = 1
when h∈H0(X) is the class of a point.
• The cup product is commutative in the graded sense:
a⌣b = (−1)|a||b|b⌣a.
• The cup product is functorial: if f : X→Y is a map then
f∗(a⌣b ) =f∗a⌣f ∗b.
hence f∗ is a homomorphism of unital graded rings. In particular, the
cohomology ring is an invariant of homotopy type.
• The natural isomorphism H∗(∐
i∈IXi)∼=
∏
i∈IH∗(Xi) is an isomorphism
of rings.
So, for example, the ‘pinching’ map ∐
i∈IXi→⋁
i∈IXi induces a ring homomor-
phism
Hn(
⋁
i∈I
Xi)→
∏
i∈I
Hn(Xi),
which is an isomorphism in degrees n> 0. Since this isomorphism is induced by a
map between the spaces, it respects the cup product.

ALGEBRAIC TOPOLOGY I: FALL 2008 75
22.3. The cap product. The cap product is a bilinear product
H∗(X)×H∗(X)→H∗(X), (c,h )↦→c⌢h.
Its fundamental properties are as follows:
• One has (a⌣b )⌢h =a⌢ (b⌢h ).
• One has 1 ⌢h =h.
• One has Hp(X) ⌢ Hn(X)⊂ Hn−p(X). Thus ⌢ makes H∗(X) into a
graded unital module (with suitable grading conventions...) over the ring
H∗(X).
• One has
⟨a⌣b,h ⟩ =⟨a,b⌢h ⟩.
• If f : X→Y is a map then
f∗(f∗c⌢h ) =c⌢f ∗h
for h∈ H∗(X) and c∈ H∗(Y ). This shows that homology, as a graded
module over cohomology, is an invariant of homotopy type.
• The natural isomorphism H∗(∐
i∈IXi)∼=⨁
i∈IH∗(Xi) is an isomorphism
of modules.
I don’t know whether the axioms for the cap and cup products that I have
listed, when considered together, characterise both of them uniquely. However, the
relation between cup, cap and evaluation products does force them to be non-trivial
(e.g. one can’t deﬁne the cup product of positive-degree cohomology classes to be
identically zero).
Most interesting computations of cohomology rings and homology modules in-
voke the Poincar´ e duality theorem.
Theorem 22.1 (Poincar´ e duality). Suppose M is a compact, connected, oriented
n-manifold with fundamental class [M]∈Hn(M). Then the ‘duality map’
D : Hp(M)→Hn−p(M), D (c) =c⌢ [M],
is an isomorphism for all p∈ Z.
The proof of this theorem mostly uses the naturality properties of cap and cup
products, though at one point it becomes necessary to look more closely at the
deﬁnition.
In practice, one works with a corollary. Next time we’ll use this to compute the
cohomology ring of projective space.
Corollary 22.2 (Poincar´ e duality: cup product version). Let M be a compact,
connected, oriented n-manifold, and [M]∈ Hn(M) the fundamental class. Then
for any p∈ Z the Poincar´ e pairing
Hp(M)/Tp×Hn−p(M)/Tn−p→ Z, (a,b )↦→⟨a⌣b, [M]⟩,
is non-degenerate. Here Tk⊂Hk(M) denotes the submodule of torsion classes, so
Hk(M)/Tk is torsion-free and hence free.
Remark. Note that the ‘hence’ here uses a fact that we have not proved, that
the (co)homology of a compact manifold is ﬁnitely generated (a ﬁnitely generated
torsion-free abelian group is free). In fact, any compact manifold is homotopy-
equivalent to a ﬁnite CW complex. In the smooth case, this follows easily from
Morse theory; in general, it is a hard theorem.

76 TIM PERUTZ
Remark. Non-degeneracy means that the adjoint map
Hp(M)/Tp→ Hom(Hn−p(M)/Tn−p, Z), a ↦→ (b↦→⟨a⌣b, [M]⟩)
is an isomorphism. If one ﬁxes bases for the free abelian groups Hk(M)/Tk, it is
the assertion that the matrix of the pairing is square and its determinant is ±1.
Proof of the corollary. Recall a corollary of universal coeﬃcients (which used ﬁnite
generation): Hp(M) = Hom( Hp(M), Z)⊕Hp−1(M)tors. Thus Hp(M;R)/Tp ∼=
Hom(Hp(M), Z). The adjoint map α: Hp(M)→ Hom(Hn−p(M), Z) sends a to
the map b↦→⟨a⌣b, [M]⟩ =±⟨b⌣a, [M]⟩ =±⟨b,a⌢ [M]⟩. If b is non-zero (mod
torsion) then it evaluates non-trivially on some homology class, and by the Poincar´ e
duality theorem, we may take that class to be of form b⌢ [M]. Hence ker α =Tp.
Andα is also surjective, because given any homomorphism f∈Hn−p(M)→ Z, we
can represent it as evaluation on some homology classh =D(c), and thenf =α(c).
□

ALGEBRAIC TOPOLOGY I: FALL 2008 77
23. Formal computations in cohomology
We show that Poincar´ e duality leads to computations of cup product structures.
We explain an algebraic application.
Last time, we noted a corollary of Poincar´ e duality, that on a compact oriented
manifold, the cup-product pairing on cohomology mod torsion is non-degenerate.
We now apply this to complex projective space. Take a polynomial ring Z[u], and
make it a graded ring by declaring u to have degree 2. Truncate it to the graded
ring Z[u]/(un+1). As a graded abelian group, we have
H∗(CPn)∼= Z[u]/(un+1).
Theorem 23.1. There is an isomorphism of graded rings,
H∗(CPn)∼= Z[u]/(un+1), degu = 2.
Proof. Induction on n. The space CP 0 is a point, and the result is trivially true
in this case. It is also trivially true when n = 1, and we will start the induction
there. If n > 1, observe that we have an inclusion i: CPn−1 → CPn, induced
by a linear inclusion Cn+1→ Cn+2. By induction, H∗(CPn−1)∼= Z[t]/tn where
degt = 2. Now, i∗ is additively an isomorphism up to degree 2( n− 1). Let
u∈ H2(CPn) be deﬁned by i∗u = t. Since tn generates H2(n−1)(CPn−1), un
generates H2(n−1)(CPn). By Poincar´ e duality, the pairing
H2(n−1)(CPn)×H2(CPn)→ Z
is non-degenerate over Z. It follows that the generators of the two groups pair to
give±1, i.e.,
⟨un−1∪u, [CPn]⟩ =⟨un, [CPn]⟩ =±1.
Hence un generates H2n(CPn), and the result follows. □
Exercise 23.1: Specify a suitable cohomology class u. Describe uk for all k. (Part of
the exercise is to work out what format the answer should sensibly take.)
Remark. A precisely similar argument, using the mod 2 version of Poincar´ e duality,
shows that
H∗(RPn; Z/2)∼= (Z/2)[t]/tn+1, degt = 1.
The result for projective spaces shows that the cup product makes cohomology
a more powerful invariant.
Example 23.2. CP 2 is not homotopy equivalent to S2∨S4. Indeed, H∗(CP 2)
contains a degree 2 class u such that u ⌣ uis non-tivial, whereas the cup-square
of a degree 2 class in H∗(S2∨S4) is always zero.
Example 23.3. Any homeomorphism h: CP 2→ CP 2 preserves orientation. For
it suﬃces to show that h∗[CP 2] = [ CP 2] (where [ CP 2] is the fundamental class),
i.e., that h has degree 1 rather than −1. But h∗u =±u, since these are the two
generators for H2. So h∗(u ⌣ u) = h∗u ⌣ h∗u =u ⌣ u, hence h∗ is the identity
on H4. Hence the dual map h∗ on H4 is also the identity.
The argument also extends to CP 2n, but not to CP 2n+1 (indeed, it is false for
CP 1).
However, it still has limitations:

78 TIM PERUTZ
Example 23.4. S3∨S5 andS(CP 2) have isomorphic cohomology rings: additively,
both are Z(0)⊕ Z(3)⊕ Z(5) where the subscripts denote degree. The product of two
classes of positive degree has to be zero, for reasons of degree.
Exercise 23.2: (a) Suppose that X and Y are compact, connected, orientable n-
manifolds. Describe the cohomology ring of their connected sum X#Y . (b) Prove
that CP 2#CP 2 and CP 2#CP 2 are not homotopy-equivalent. Here CP 2 is the com-
plex projective plane with one orientation, and CP 2 the same space with the opposite
orientation.
23.1. The K¨ unneth formula.There is one other general result which is very
useful in computing cup products. To state it I need to work with cohomology
with coeﬃcients in a ring k. Cohomology with coeﬃcients in k also carries a cup
product, which is linear over k and so makes H∗(X;k) a k-algebra.
The result is the K¨ unneth formula.In general, if A andB are graded k-algebras
then their tensor product A⊗B is also a graded k-algebra, with ith graded part⨁
jAj⊗Bi−j, and product given on homogeneous monomials by
(x⊗y)· (x′⊗y′) = (−1)|y||x′|(x⌣x ′)⊗ (y ⌣y′).
Theorem 23.5 (K¨ unneth formula). Let X and Y be spaces. Deﬁne the ‘cross
product’ map
H∗(X;k)⊗kH∗(Y ;k)→H∗(X×Y ;k), (x,y )↦→x×y := pr∗
Xx⌣ pr∗
Yy,
where prX and prY the two projection maps fromX×Y . One checks that it is a map
of graded k-algebras. When X and Y are CW complexes, and H∗(Y ) is a ﬁnitely
generated free k-module (e.g. when k is a ﬁeld), this map is an isomorphism.
Without the assumption that H∗(Y ) is a free module, there is still a K¨ unneth
theorem; it says that the cross product map is injective, and expresses its cokernel
using Tor.
Example 23.6.
H∗(CPn× CPm)∼= Z[t,u ]/(tn+1,um+1)
with|t| =|u| = 2, and
H∗(RPn× RPm; Z/2)∼= (Z/2)[x,y ]/(xn+1,ym+1)
with|x| =|y| = 1 (the signs become irrelevant when k = Z/2).
23.2. An algebraic application of cup product. A division algebra over a ﬁeld
F is an F -vector space A equipped with a bilinear map m: A×A→A, such that
for each x∈ A\{ 0} the linear maps m(x,·): A→ A and m(·,x ): A→ A are
isomorphisms.
Theorem 23.7 (Hopf). The dimension of a ﬁnite-dimensional division algebra
over R is a power of 2.
Proof. Let A be an n-dimensional real division algebra, with multiplication
m: A×A→A.
Bilinearity of m, and the fact that m(x,y ) = 0 implies x = 0 or y = 0, tell us that
there is an induced map
M = Pm: PA× PA→ PA.

ALGEBRAIC TOPOLOGY I: FALL 2008 79
Let k be the ﬁeld Z/2. On mod 2 cohomology, M gives us a map
M∗ : H∗(PA× PA;k)→H∗(PA;k).
We have H∗(PA;k) = k[x]/(xn) where deg x = 1, and by the K¨ unneth formula,
H∗(PA× PA; Z/2) =k[y,z ]/(yn,zn). Thus we have a map of graded rings
M∗ : k[x]/(xn)→k[y,z ]/(yn,zn).
We claim that M∗(x) = y +z. Indeed, we know that for some (or indeed, any)
µ ∈ PA, the composite PA → PA× PA → PA, λ ↦→ (λ,µ ) ↦→ M(λ,µ ) is a
homeomorphism, hence thatM∗x =y mod z, and similarly thatM∗x =z mod y.
This proves the claim.
Hence (y +z)n∈ k[y,z ] lies in the ideal generated by yn and zn. This implies
that the coeﬃcient of ykzn−j for 1≤ j < n, namely
(n
j
)
, must be zero in k, and
hence that the equation
(1 +t)n = 1 +tn
holds in k[t]. Now, (1 +t)2 = 1 +t2 ink[t]. Thus (1 +t)4 = (1 +t2)2 = 1 +t4, and
more generally, (1 +t)2m
= (1 +t2m
). But if we write n in binary form, putting
n = 2m1 + 2m2 +··· + 2ma, m 1 <m 2 <··· <m a,
then (1 + t)n =∏ (1 +t)2mi
=∏ (1 +t2mi
). But this expression is 1 + t2m1
plus
higher order terms. So the equation (1 + t)n = 1 +tn holds only if a = 1, i.e. n is
a power of 2. □
Remark. The proof applies to a slightly more general kind of algebra: we can assume
that there exist some x and y in A so that m(x,·) and m(·,y ) are isomorphisms.
Exercise 23.3: Prove that the cohomology groups of a compact, simply connected,
oriented 4-manifold M are completely determined by the second Betti number
b2(M) = dimQH2(M; Q).
Prove that the cohomology ring is determined by the cup-product pairingH2×H2→ Z.
Exercise 23.4: A special case of the Lefschetz ﬁxed point theorem states that if X is a
ﬁnite CW complex, and g : X→X a map without ﬁxed points, then
∑
p≥0
(−1)p trHp(g) = 0.
Here Hp(g) is the induced map on H∗(X; Q). What restrictions does this entail for
groups acting freely on CPn?

80 TIM PERUTZ
24. Cup products defined
We deﬁne the cup product of cochains.
24.1. The basic mechanism. The deﬁnition of cup products combines two ideas:
(1) There is a chain map
D∗ : C∗(X×X)→C∗(X)
induced by the diagonal map D : X→X×X, x↦→ (x,x ).
(2) There is a natural chain map (actually, a quasi-isomorphism)
ζ : C∗(X)⊗C∗(X)→C∗(X×X).
Here by C∗ denotes cochains, but they could be singular or cellular. Given these
elements, one deﬁnes a chain map
⌣: Cp(X)⊗Cq(X)→Cp+q(X), a⌣b =D#◦ζ(a⊗b).
24.2. Cup products in cellular cohomology. Suppose, for instance, we work
with cellular cohomology.
Proposition 24.1. Suppose X has a CW decomposition with p-cells eα
p , and Y
a CW decomposition with q-cell fβ
q . Then X×Y has a cell decomposition with
(p +q)-cells eα
p×eβ
q . The cellular chain complex of the product is given by
Ccell
∗ (X×Y ) =Ccell
∗ (X)⊗Ccell
∗ (Y ),
with the cellular boundary dX×Y (e⊗f) =dXe⊗f + (−1)degee⊗dYf.
I won’t give the proof (see Hatcher p. 268 or May p.99), but the basic point is
that the product of a p-cell and a q-cell is a p +q-cell.
Let’s apply this to X×X. It has a cell decomposition with cells eα
p⊗eβ
q , and
one has an isomorphism of chain complexes
Ccell
∗ (X×X)→Ccell
∗ (X)⊗Ccell
∗ (X),
where the diﬀerential on the right-hand side is given on the summand Ccell
p (X)⊗
Ccell
q (X) by
dp⊗ id + (−1)pid⊗dq.
The cellular cochain complex C∗
cell(X) is deﬁned as the dual cochain complex to
(C∗(X),d ). Thus by duality one has an isomorphism of cochain complexes
ζ : C∗
cell(X)⊗C∗
cell(X)→C∗
cell(X×X).
Now,D is not a cellular map, but we have the cellular approximation theorem:
Theorem 24.2. Every map between CW complexes is homotopic to a cellular map,
i.e., one which maps the k-skeleton to the k-skeleton for all k.
So D is homotopic to a cellular map D′ : X→X×X.
Example 24.3. MakeS1 a CW complex with exactly two cells. Then one can see
from a picture how the diagonal S1→S1×S1 is homotopic to a cellular map.
Exercise 24.1: Find a cellular approximation to the diagonal Sn→Sn×Sn.

ALGEBRAIC TOPOLOGY I: FALL 2008 81
Deﬁne the cup product on the cellular cochain complex by
a⌣b =D′#◦ζ(a⊗b).
This is a perfectly reasonable (and correct) deﬁnition; for instance, it satisﬁes
d(a⌣b ) =da⌣b + (−1)|a|a⌣db.
Its only deﬁciency is that it is non-explicit, because of the cellular approximation
to D.
In some cases, one can write down an explicit cellular approximation and use it
compute the cup product:
Example 24.4. Use a cellular approximation to the diagonal S1→ S1×S1 to
construct another such approximationS1×S1→S1×S1×S1×S1. Hence compute
the cup-product structure of H∗(S1×S1).
24.3. Cup products in singular cohomology. We have a canonically-deﬁned
chain mapD# : S∗(X×X)→S∗X. Explicitly, for c∈Sp(X×X) andτ∈ Σp(X),
one has
⟨D#(c),τ⟩ =⟨c,τ ×τ⟩.
We want to deﬁne
a⌣b =D#ζ(a⊗b).
We need to set up a suitable chain map ζ, which should be natural in X. There is
an explicit formula for such a ζ, called the Alexander–Whitney map :
Proposition 24.5 (Alexander–Whitney). Deﬁne a linear map
ζ =ζX : Sp(X)⊗Sq(X)→Sp+q(X×X)
by
⟨ζ(a⊗b),σ⟩ =⟨a, (pr1◦σ)|[v0,...,vp])⟩⟨b, (pr2◦σ)|[vp,...,vp+q])⟩
for a∈ Sp(X), b∈ Sq(X), and σ∈ Σp+q(X×X). Then ζ is a chain map. It is
natural in X in that
(f×f)∗◦ζY =ζX◦f∗
for f : X→Y . One has
ζ(1X⊗ 1X) = 1X×X,
where 1X∈S0(X) evaluates as 1 on any simplex (similarly 1X×X).
Exercise 24.2: Check the proposition.
We can use the Alexander–Whitney map to deﬁne the cup product as D#◦ζ:
Deﬁnition 24.6. The cup product of cochains a and b is deﬁned by
⟨a⌣b,σ ⟩ =⟨a,σ|[v0,...,vp])⟩⟨b,σ|[vp,...,vp+q])⟩.
Remark. It is a theorem of Eilenberg–Zilber thatζ is a chain-homotopy equivalence.
Moreover, any other chain map ζ′ that is natural in X and satisﬁes ζ′(1X⊗ 1X) =
1X×X is naturally chain-homotopic to ζ. Thus one could deﬁne cup product via ζ′,
but on cohomology the deﬁnition would give the same product.

82 TIM PERUTZ
Lemma 24.7. One has
d(a⌣b ) =da⌣b + (−1)|a|a⌣db ;
a⌣ (b⌣c ) = (a⌣b )⌣c ;
a⌣ 1X =a = 1X ⌣a.
Thus S∗(X) is a diﬀerential graded algebra (DGA). For a map f, one has f∗(a⌣
b) =f∗a⌣f ∗b, so this DGA is natural in X.
Thus⌣ descends to give a unital ring structure on cohomology H∗(X) bilinear
product on cohomology, natural in X.
Exercise 24.3: Use singular cohomology to compute H∗(S1×S1) as a ring. [You may
ﬁnd it helpful to think of S1×S1 as a ∆-complex.]
The cap product is deﬁned by a similar procedure:
Sp(X)⊗Sn(X)
1⊗D#
→ Sp(X)⊗Sn(X×X))
1⊗ζ∨
→ Sp(X)⊗[S∗(X)⊗S∗(X)]n→Sn−p(X).
Here the last map is
c⊗y⊗z↦→⟨c,y⟩z.
Exercise 24.4: Check that the cap product has the properties I claimed two lectures
back.

ALGEBRAIC TOPOLOGY I: FALL 2008 83
25. Non-commutativity
We sketch a deﬁnition of the simplest interesting Steenrod operation,
Sqn−1 : Hn(X; Z/2)→H2n−1(X; Z/2)
and use it to distinguish two homotopy types.
In the de Rham cohomology theory of smooth manifolds M, which is naturally
isomorphic toM↦→H∗(M; R), the wedge product of diﬀerential forms is commuta-
tive (in the graded sense). However, the cup product of cochains is not commuative.
Lemma 25.1. The cochain-level cup product of singular cochains is not commuta-
tive. However, there exist natural maps κ: Sp(X)⊗Sq(X)→Sp+q−1(X) satisfying
the chain homotopy identity
a⌣b − (−1)|a||b|b⌣a =dκ(a⊗b) +κ(da⊗b + (−1)|a|a⊗db).
Hence the cohomology cup product is commutative (in the graded sense).
I will not prove this lemma.
Suppose we work with cochains over Z/2. Construct the natural map κ as in
the lemma. For [c]∈Hn(X; Z/2), deﬁne Sqn([c]) = [c⌣c ]∈H2n(X; Z/2), and
Sqn−1([c]) = [κ(c⊗c)]∈H2n−1(X; Z/2).
This makes sense because the identity satisﬁed by κ implies that, working mod 2,
we have thatdκ(c⊗c) = 0 whendc = 0, and also thatκ((c+db)⊗(c+db))−κ(c⊗c)
is exact.
It is eminently plausible—and moreover true—that if ( X;A,B ) is an excisive
triad then the Mayer–Vietoris connecting maps δp : Hp(A∩B)→Hp+1(X) satisfy
Sqn−1(δnc) =δ2n−1(Sqn−1c), c ∈Hn−1(A∩B).
(Here the Sqn−1 on the right is the cup-square, that on the left the one deﬁned
using κ.) It follows that one has (for n> 0)
Sqn−1(Σc) = Σ(Sqn−1c) = Σ(c⌣c ), c ∈Hn−1(X),
where Σ: ˜H∗(X)→H∗+1(SX) is the suspension isomorphism.
Example 25.2. For instance, if 0 ⁄= u∈ H2(CP 2; Z/2) then in H5(SCP 2; Z/2)
one has
Sq2(Σu) = Σ(u2)⁄= 0.
SoSq2 is non-zero. On the other hand, in S5∨S3, which has the same cohomology
ring as S(CP 2), one has Sq2(H3) = 0. So, once the operation Sq2 : H3→H5 has
been put on a sound footing, we will have a proof that S5∨S3⁄≃S(CP 2).
We have omitted several details in this discussion, but the basic points are these.
• There is no commutative cochain-level cup product on mod 2 cochains
which is natural in X.
• This non-commutativity has a manifestation in an operation on mod 2
cohomology which is sometimes non-trivial. This can be used to distinguish
homotopy types (such as S5∨S3 versusS(CP 2)).

84 TIM PERUTZ
26. Poincar´e duality
We provide most but not all of the details of the proof of Poincar´ e duality.
Poincar´ e duality is primarily a statement about compact manifolds. Let us recall
the statement in that case.
Theorem 26.1 (Poincar´ e duality: compact case). Suppose M is a compact, con-
nected,R-oriented n-manifold with fundamental class [M]∈Hn(M;R). Then the
‘duality map’
D : Hp(M;R)→Hn−p(M;R), D (c) =c⌢ [M],
is an isomorphism for all p∈ Z.
We shall prove the Poincar´ e duality theorem using Mayer–Vietoris sequences,
starting from simple cases and gradually expanding the generality. However, most
of the manifolds one encounter along the way are non-compact, and it is therefore
useful to have a formulation valid in the non-compact case. This involves the
compactly supported cohomology and relative cap products.
The compactly supported cohomology H∗
c (M;R) is is the cohomology of a com-
plex built from singular cochains c for which there is some compact subset K so
that c annihilates all chains in X\K.1 More precisely, we deﬁne
Hp
c (M;R) = lim−→K
Hp(X,X\K;R)
where the direct limit is over compact subsets K⊂X. To explain this, note that
the compact subsets of X form a direct system under inclusion. This means that
one has inclusion maps i: K1→K2, and the composite of inclusion maps is again
an inclusion map. The identity map on X is then a map of pairs
(X,X\K2)→ (X,X\K1),
and hence induces a homomorphism
Hp(X,X\K2;R)→Hp(X,X\K1;R).
In this way, the modules Hp(X,X \K) become a direct system as K ranges over
compact subsets. We deﬁned Hp
c (M;R) as the direct limit of this system. Thus
one has a canonical map
Hp(X,X\K;R)→Hp
c (X;R)
for each compact K, and these commute with the maps in the inverse system.
Indeed, Hp
c (X;R) is universal with respect to this property.
In practice, one computes Hp
c (X) as the direct limit of Hp(X,X \K) as K
ranges over some compact exhaustion, i.e., a family of compact subspaces Ki such
that every compact subspace is contained in some Ki. This is valid by abstract
nonsense about coﬁnal families.
Example 26.2. Let us compute Hp
c (Rn). A compact exhaustion is given by the
discs Dn(m) centred at 0 and of radius m = 1, 2,... . One has H∗(Rn, Rn\
Dn(m))∼= Z(n). The inclusion of D(m) in D(m + 1) obviously induces an iso-
morphism on the relative cohomology groups. Hence H∗
c (Rn)∼= Z(n).
1If you know about de Rham theory, you should think of diﬀerential forms with compact
support.

ALGEBRAIC TOPOLOGY I: FALL 2008 85
Remark. Taking direct limits of (co)chain complexes is an exact functor , i.e. it
commutes with passing to (co)homology. This is not true of inverse limits; the
failure of exactness is measured by the derived functor lim←−
1 of the inverse limit.
The cap product ⌢: Hp(X)×Hq(X)→Hq−p(X) generalizes to a relative cap
product
Hp(X,A )×Hq(X,A )→Hq−p(X),
deﬁned at (co)chain level by the same formula as the original cap product. Indeed,
one has ∂(φ ⌢ a) = dφ ⌢ a±φ ⌢ ∂c. If φ represents a cocycle rel A, and a a
cycle rel A, then both terms vanish. When p = q, the cap product is essentially
just the evaluation pairing. More precisely,
⟨1,φ⌢a ⟩ =⟨φ,a⟩.
Theorem 26.3 (Poincar´ e duality: general case). IfM is an R-orientedn-manifold
then the duality map
D : Hp
c (M;R)→Hn−p(M;R),
is an isomorphism. Here D is deﬁned as the direct limit of the maps
DK : Hp(M,M \K;R)→Hn−p(M;R), c ↦→c⌢ [MK],
where [MK]∈Hn(M,M \K) is the fundamental class of M relative to K, and ⌢
the relative cap product.
In the proof we shall need the observation that the inclusion i: U → M of
an open subspace U induces a covariant homomorphism i∗∗ : Hp
c (U)→ Hp
c (M).
Indeed, if K⊂U with K compact then excision gives an isomorphism
Hp(U,U\K)∼=Hp(M,M \K),
and these isomorphisms commute with the maps in the direct system. We deﬁne
i∗∗ as the composite
Hp
c (U) = lim−→K⊂U
Hp(U,U\K)∼= lim−→K⊂U
Hp(M,M \K)→Hp
c (M).
Proof of the theorem. We drop the coeﬃcientsR from the notation. We shall prove
that D : Hp
c (U) → Hn−p(U) is an isomorphism for each open subset D ⊂ M
(including, eventually,M itself).
Step 1. The result holds when U = Rn.
Indeed, we saw above thatH∗
c (Rn)∼=R(n)∼=Hn−∗(Rn). For any compact subset
K, the cap product of a generator for Hn(Rn, Rn\K) by the fundamental class
[Rn
K]∈Hn(Rn, Rn\K) is (up to a sign) the point class in H0(Rn), because of the
relation between relative cap product and the evaluation pairing. Passing to the
direct limit, we ﬁnd that D is an isomorphism in this case.
Step 2: If the result holds for U, V and U∩V then it holds for U∪V .
I claim that there is a covariant Mayer–Vietoris sequence in compactly supported
cohomology, and that one has a commutative diagram with exact rows of which
one portion reads
−−−−→ Hp
c (U)⊕Hp
c (V ) −−−−→Hp
c (U∪V ) −−−−→Hp+1
c (U∩V ) −−−−→
D
↓ D
↓ D
↓
−−−−→Hn−p(U)⊕Hn−p(V ) −−−−→Hn−p(U∪V ) −−−−→Hn−p−1(U∩V ) −−−−→

86 TIM PERUTZ
Once this is veriﬁed, the 5-lemma assures us that D : Hp
c (U∪V )→Hn−p(U∪V ) is
an isomorphism. The proof of this claim involves locality for chains (unsurprising
since that underlies Mayer–Vietoris) and a good deal of checking, for which I refer
to Hatcher.
Step 3: If the result holds for each Ui in a nested sequence U1⊂U2⊂U3⊂ of
open subspaces, then it holds for V =⋃Ui.
Any compact subset K⊂ V is contained in some Ui. The algebraic properties
of direct limits give
Hp
c (V ) = lim−→i
lim−→K⊂Ui
Hp(Ui,Ui\K) = lim−→i
Hp
c (Ui).
But
Hn−p(V ) =Hn−p(
⋃
Ui) = lim−→i
Hn−p(Ui),
because the singular chain complex of an expanding union is the direct limit of
the singular chain complexes, and taking homology commutes with direct limits.
Now D : Hp
c (Ui)→ Hn−p(Ui) is an isomorphism, and it commutes with the maps
induced by inclusion of Ui in Ui+1; hence D = lim−→i(D : Hp
c (V )→Hn−p(M)) is an
isomorphism.
Step 4: The result holds for open subsets of Rn.
Every open set U⊂ Rn is the union of a countable set of open balls. Hence U
is the union of a nested family U1⊂U2⊂U3⊂... , where U1 is an open ball, and
Ui+1 is the union of Ui and a convex open set C homeomorphic to Rn. Note that
C∩Ui is convex, open, and has compact closure, and hence is homeomorphic to a
ball. Thus the result holds for Ui+1 by induction and steps 1 and 2.
Step 5: The result holds for M.
By Steps 1 and 4, and Zorn’s lemma, there is a non-empty, maximal open set O
for which the result holds. If this weren’t all of M, we could take the union of O
and a coordinate neighbourhood U∼= Rn, disjoint from O; the result would then
hold for O∪U by steps 1 and 2. This contradicts maximality of O. □
Remark. There is an almost trivial proof of duality for compact smooth manifolds
M in the context of Morse theory. The cellular chain complex can be understood
in terms of critical points and gradient ﬂows for a Morse function f. Replacing f
by−f does not change the homology (which is just H∗(M)) but it has the eﬀect of
dualizing the chain complex and changing degree ∗ to degree n−∗ . Thus H∗(M)
is isomorphic to the cellular cohomology of M in degree n−∗ .
Exercise 26.1: Let M be a compact, connected, oriented 3-manifold. Determine the
graded ring H∗(M) when (i) π1(M) is ﬁnite; (ii) H1(M)∼= Z; (iii) H1(M)∼= Z2.
Exhibit two such 3-manifolds with non-isomorphic cohomology rings, both of which
have H1∼= Z3.
Exercise 26.2: Show that the Euler characteristic of a compact, orientable, odd-dimensional
manifold is zero.
Exercise 26.3: For which even dimensions 2n is it true that the Euler characteristic of
a compact, connected, orientable 2n-manifold is necessarily even?
Exercise 26.4: Show that for every map f : S2n → CPn, the induced map ˜f∗ on
reduced homology is zero.

