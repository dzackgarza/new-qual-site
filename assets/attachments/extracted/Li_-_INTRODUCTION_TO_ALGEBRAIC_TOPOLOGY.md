INTRODUCTION TO ALGEBRAIC TOPOLOGY
SI LI
ABSTRACT . To be continued. This is course note for Algebraic Topology in Spring 2018 at Tsinghua university.
Coure References:
(1) Hatcher: Algebraic Topology
(2) Bott and Tu: Differential forms in algebraic topology.
(3) May: A Concise Course in Algebraic Topology
(4) Spanier: Algebraic Topology.
CONTENTS
1. Category and Functor 2
2. Fundamental Groupoid 5
3. Covering and ﬁbration 7
4. π1(S1) and applications 9
5. Classiﬁcation of covering 11
6. Seifert-van Kampen Theorem 14
7. Path space and homotopy ﬁber 15
8. Group object and homotopy group 19
9. Exact Puppe sequence 21
10. Coﬁbration 24
11. CW complex 27
12. Whitehead Theorem 29
13. Cellular and CW approximations 32
14. Eilenberg-MacLane Space 34
15. Singular Homology 36
16. Exact homology sequence 39
17. Excision 41
18. Homology of spheres 44
19. Cellular homology 46
20. Cohomology and Universal Coefﬁcient Theorem 49
1

2 SI LI
21. Eilenberg-Zilber Theorem and K ¨unneth formula 53
22. Cup and Cap product 56
23. Poincar ´e duality 60
24. Intersection and Lefschetz Fixed Point Theorem 63
25. Spectral sequence 65
26. Obstruction theory 66
27. The Theorem of Hurewicz 66
28. Eilenberg-Steenrod Axioms 67
1. C ATEGORY AND FUNCTOR
Category.
Deﬁnition 1.1. A categoryC consists of
(1) a class of objects: Obj(C)
(2) morphisms: a set HomC (A, B),∀A, B∈ Obj(C). An element f∈ Hom(A, B) will be denoted by
A
f
→ B or f : A→ B.
(3) composition:
Hom(A, B)× Hom(B, C)→ Hom(A, C),∀A, B, C∈ Obj(C)
f× g→ g◦ f
satisfying the following axioms
(1) associativity: h◦ (g◦ f ) = ( h◦ g)◦ f for any A
f
→ B
g
→ C h→ D.
(2) identity:∀A∈ Obj(C),∃1A∈ Hom(A, A) called the identity element, such that
f◦ 1A = f = 1B◦ f , ∀A
f
→ B.
A category is called small if its objects form a set.
Deﬁnition 1.2. A morphism f : A→ B is called an equivalence/invertible if∃g : B→ A such that
f◦ g = 1B, g◦ f = 1A.
Two objects A, B are called equivalent if there exists an equivalence f : A→ B.
Deﬁnition 1.3. A category where all morphisms are equivalences is called a groupoid.
Deﬁnition 1.4. A subcategoryC′⊂C is a category such that
• Obj(C′)⊂ Obj(C)
• HomC′ (A, B)⊂ HomC (A, B),∀A, B∈ Obj(C′)
• composition coincides.
C′ is called a full subcategory ofC if HomC′ (A, B) = HomC (A, B),∀A, B∈ Obj(C′).

INTRODUCTION TO ALGEBRAIC TOPOLOGY 3
Deﬁnition 1.5. Let∼ be an equivalence relation deﬁned on each Hom(A, B), A, B∈ Obj(C) satisfying
f1∼ f2, g1∼ g2 =⇒ g1◦ f1∼ g2◦ f2.
Then we deﬁne the quotient categoryC′ =C/∼ by
• Obj(C′) = Obj(C′)
• HomC′ (A, B) = HomC (A, B)/∼,∀A, B∈ Obj(C′)
Example 1.6. We will frequently use the following categories.
• Set: the category of set.
• Vect: the category of vector spaces.
• Group: the category of groups.
• Ab: the category of abelian groups.
• Ring: the category of rings.
Vect⊂ Set is a subcategory, and Ab⊂ Group is a full subcategory.
The main object of our interest is the category of topological spaces Top
• objects of Top are topological spaces.
• morphism f : X→ Y is a continuous map.
Deﬁnition 1.7. Given X, Y∈ Top, f0, f1 : X→ Y are said to to homotopic, denoted by f0≃ f1, if
∃F : X× I→ Y, such that F|X×0 = f0, F|X×1 = f1. I = [0, 1].
Homotopy deﬁnes an equivalence relation on Top. We denote its quotient category by
hTop = Top/≃ .
We also denote
HomhTop(X, Y) = [ X, Y].
Deﬁnition 1.8. Two topological spacesX, Y are said to have thesame homotopy type (or homotopy equiv-
alent) if they are equivalent in hTop.
There is also a relative version as follows.
Deﬁnition 1.9. Let A⊂ X∈ Top, f0, f1 : X→ Y such that f0|A = f1|A : A→ Y. We say f0 is homotopic to
f1 relative to A, denoted by
f0≃ f1 rel A
if there exists F : X× I→ Y such that
F|X×0 = f0, F|X×1 = f1, F|A×t = f0|A,∀t∈ I.
Functor.
Deﬁnition 1.10. LetC,D be two categories. A covariant functor (or contravariant functor) F :C →D
consists of
• F : Obj(C)→ Obj(D), A→ F(A)

4 SI LI
• HomC (A, B)→ HomD(F(A), F(B)),∀A, B∈ Obj(C). We denote by
A
f
→ B =⇒ F(A)
F( f )
→ F(B)
( or HomC (A, B)→ HomD(F(B), F(A)),∀A, B∈ Obj(C), denoted by A
f
→ B =⇒ F(B)
F( f )
→ F(A) )
satisfying
• F(g◦ f ) = F(g)◦ F( f ) (or F(g◦ f ) = F( f )◦ F(g)) for any A
f
→ B
g
→ C
• F(1A) = 1F(A),∀A∈ Obj(C).
F is called faithful (or full) if HomC (A, B)→ HomD(F(A), F(B)) is injective (or surjective)∀A, B∈ Obj(C).
Example 1.11.∀X∈ Obj(C),
Hom(X,−) :C→ Set, A→ Hom(X, A)
deﬁnes a covariant functor. Similarly Hom (−, X) deﬁnes a contravariant functor. A functor F :C→ Set of
such type is called representable.
Example 1.12. Let G be an abelian group. Given X∈ Top, we will study its n-th cohomology H n(X; G). It
deﬁnes a functor
Hn(−; G) : hTop→ Set, X→ Hn(X; G)
We will see that this functor is representable by the Eilenberg-Maclane space if we work with the subcate-
gory of CW-complexes.
Example 1.13. We deﬁne a contravariant functor
Fun : Top→ Ring, X→ Fun(X) = Hom(X, R)
F(X) are continuous real functions onX. A classical theorem of Gelfand-Kolmogoroff says that two compact
Hausdorff spaces X, Y are homeomorphic if and only if Fun(X), Fun(Y) are ring isomorphic.
Proposition 1.14. Let F :C→D be a functor. f : A→ B is an equivalence. Then F ( f ) : F(A)→ F(B) is also an
equivalence.
Natural transformation.
Deﬁnition 1.15. LetC,D be two categories. F, G :C → Dbe two functors. A natural transformation
τ : F→ G consists of morphisms
τ ={τA : F(A)→ G(A)|∀A∈ Obj(C)}
such that the following diagram commutes for any A, B∈ Obj(C)
F(A)
τA

F( f ) // F(B)
τB

G(A)
G( f ) // G(B)
τ is called natural equivalence if τA is an equivalence for any A∈ Obj(C). We write F≃ G.
Deﬁnition 1.16. Two categoriesC,D are called isomorphic if∃F :C→D , G :D→C such that F◦ G =
1D, G◦ F = 1C. They are called equivalent if∃F :C→D , G :D→C such that F◦ G≃ 1D, G◦ F≃ 1C
Proposition 1.17. Let F :C→D be an equivalence of categories. Then F is fully faithful.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 5
Deﬁnition 1.18. LetC be a small category, andD be a category. We deﬁne the functor category Fun(C,D)
• objects: covariant functors fromC toD
• morphism: natural transformations between two functors (which is indeed a set sinceC is small).
2. F UNDAMENTAL GROUPOID
Path connected component.
Deﬁnition 2.1. Let X∈ Top. A map γ : I→ X is called a path from γ(0) to γ(1). We denote γ−1 be the
path from γ(1) to γ(0) deﬁned by γ−1(t) = γ(1− t). We denote ix0 : I→ X be the constant map to x0∈ X.
Let us introduce an equivalence relation on X by
x0∼ x1⇐⇒∃ a path from x0 to x1.
We denote the quotient space
π0(X) = X/∼
which is the set of path connected components of X.
Proposition 2.2. π0 : hTop→ Set deﬁnes a covariant functor.
As a consequence, π0(X)∼= π0(Y) if X, Y are homotopy equivalent.
Path category/fundamental groupoid.
Deﬁnition 2.3. Let γ : I→ X be a path. We deﬁne the path class of γ
[γ] ={ ˜γ : I→ X| ˜γ≃ γ rel ∂I ={0, 1}}
Deﬁnition 2.4. Let γ1, γ2 : I→ X such that γ1(1) = γ2(0). We deﬁne
γ2 ⋆ γ1 : I→ X
by
γ2 ⋆ γ1(t) =



γ1(2t) 0≤ t≤ 1/2
γ2(2t− 1) 1/2≤ t≤ 1.
⋆ is not associative for strict paths. However, ⋆ deﬁnes an associative composition on path classes.
Theorem 2.5. Let X∈ Top. We deﬁne a category Π1(X) as follows:
• Obj(Π1(X)) = X.
• HomΠ1(X)(x0, x1)=path classes from x0 to x1.
• 1x0 = ix0.
Then Π1(X) deﬁnes a category which is in fact a groupoid. The inverse of [γ] is given by [γ−1]. Π1(X) is called the
fundamental groupoid of X.
LetC be a groupoid. Let A∈ Obj(C), then
AutC (A) := HomC (A, A)

6 SI LI
forms a group. For any f : A→ B, it induces a group isomorphism
Ad f : AutC (A)→ AutC (B)
g→ f◦ g◦ f−1.
This naturally deﬁnes a functor
C→ Group
A→ AutC (A)
f→ Ad f
Specialize this to topological spaces, we ﬁnd a functor
Π1(X)→ Group .
Deﬁnition 2.6. Let x0∈ X, the group
π1(X, x0) := AutΠ1(X)(x0)
is called the fundamental group of the pointed space (X, x0).
Theorem 2.7. Let X be path connected. Then for x 0, x1∈ X, the have group isomorphism
π1(X, x0)∼= π1(X, x1).
Let f : X→ Y be a continuous map. It deﬁnes a functor
Π1( f ) : Π1(X)→ Π1(Y)
x→ f (x)
[γ]→ [ f◦ γ].
Then Π1 deﬁnes a functor
Π1 : Top→ Groupoid , X→ Π1(X)
from the category Top to the category Groupoid of groupoids. Here morphisms in Groupoid are given by
natural transformations.
Proposition 2.8. Let f , g : X→ Y be maps which are homotopic by F : X× I→ Y. Let us deﬁne path classes
τx0 = [ F|x0×I]∈ HomΠ1(Y)( f (x0), g(x0)).
Then τ deﬁnes a natural transformation
τ : Π1( f ) =⇒ Π1(g).
This proposition can be pictured by the following diagram
X
f
&&
g
88 F Y =⇒ Π1(X)
Π1( f ) ++
Π1(g)
33 τ Π1(Y)
The following theorem is a formal consequence of the above proposition

INTRODUCTION TO ALGEBRAIC TOPOLOGY 7
Theorem 2.9. Let f : X→ Y be a homotopy equivalence. Then
Π1( f ) : Π1(X)→ Π1(Y)
is an equivalence of categories. In particular, it induces group isomorphisms
π1(X, x0)∼= π1(Y, f (x0)),
3. C OVERING AND FIBRATION
Covering.
Deﬁnition 3.1. Let p : E→ B be continuous. A trivialization of p over an open U⊂ B is a homeomorphism
ϕ : p−1(U)→ U× F over U, i.e. , the following diagram commutes
p−1(U)
ϕ //
""
U× F
||
U
p is called locally trivial if there exists an open coverU of B such that p has a trivialization over each open
U∈U . Such p is also called a ﬁber bundle and F is called the ﬁber.
Deﬁnition 3.2. A covering is a locally trivial map p : E→ B with discrete ﬁber F.
Example 3.3. ex : R1→ S1, t→ e2πit is a covering.
Deﬁnition 3.4. Let p : E→ B, f : X→ B. A lifting of f along p is a map F : X→ E such that p◦ F = f
E
p

X
F
??
f // B
Lemma 3.5. Let p : E→ B be a covering. Let
D ={(x, x)∈ E× E|x∈ E}
Z ={(x, y)∈ E× E|p(x) = p(y)}.
Then D⊂ Z is open and closed.
Theorem 3.6 (Uniqueness of lifting) . Let p : E→ B be a covering. Let F 0, F1 : X→ E be two liftings of f .
Suppose X is connected and F0, F1 agree somewhere. Then F0 = F1.
Proof. Consider the map ˜F = ( F0, F1) : X→ Z. ˜F(X)∩ D⁄= ∅. The above lemma implies ˜F(X)⊂ D.
□
ﬁbration.
Deﬁnition 3.7. A map p : E→ B is said to have the homotopy lifting property (HLP) with respect to X if
for any maps ˜f : X→ E and F : X× I→ B such that p◦ ˜f = F|X×0, there exists a lifting ˜F of F along p such

8 SI LI
that ˜F|X×0 = ˜f , i.e., the following diagram commutes
X× 0
˜f // _

E
p

X× I
F
//
∃ ˜F
<<
B
Deﬁnition 3.8. A map p : E→ B is called a ﬁbration (or Hurewicz ﬁbration) if p has HLP for any space.
Theorem 3.9. A covering is a ﬁbration .
Corollary 3.10. Let p : E→ B be a ﬁbration. Then for any path γ : I→ B and e∈ E such that p (e) = γ(0), there
exists a unique path ˜γ : I→ E that lifts γ and ˜γ(0) = e.
Proof. Apply HLP to X=pt.
0
e // _

E
p

I γ
//
˜γ
@@
B
□
Corollary 3.11. Let p : E→ B be a covering. Then Π1(E)→ Π1(B) is a faithful functor. In particular, the induced
map π1(E, e)→ π1(B, p(e)) is injective.
Transport functor.
Let p : E→ B be a covering. Let γ : I→ B be a path in B from b1 to b2. It deﬁnes a map
Tγ : p−1(b1)→ p−1(b2)
e1→ ˜γ(1)
where ˜γ is a lift of γ with initial condition ˜γ(0) = e1.
Assume [γ1] = [ γ2] in B. HLP implies that Tγ1 = Tγ2. We ﬁnd a well-deﬁned map
T : HomΠ1(B)(b1, b2)→ HomSet(p−1(b1), p−1(b2))
[γ]→ T[γ]
Proposition 3.12. The following data
T : Π1(B)→ Set
b→ p−1(b)
[γ]→ T[γ].
deﬁnes a functor, called the transport functor. In particular, we have a well-deﬁned map
π1(B, b)→ Aut(p−1(b)).
Proposition 3.13. Let p : E→ B be a covering, E path connected. Let e ∈ E, b = p(e)∈ B. Then the action of
π1(B, b) on p−1(b) is transitive, whose stabilizer at e is π1(E, e). In other words,
p−1(b)∼= π1(B, b)/π1(E, e)
as a coset space.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 9
Lifting Criterion.
Theorem 3.14 (Lifting Criterion). Let p : E→ B be a covering. f : X→ B for X path connected and locally path
connected. Let e∈ E, x0∈ X such that f (x0) = p(e). Then there exists a lift F of f with F (x0) = e if and only if
f∗(π1(X, x0))⊂ p∗(π1(E, e)).
Proof. If such F exists, f∗(π1(X, x0)) = p∗F∗(π1(X, x0))⊂ p∗(π1(E, e)). Conversely, consider the product
˜E
˜p

// E
p

X
f // B
Let ˜e = (e, x0)∈ ˜E. Then ˜p is a covering and we have a commuting diagram of functors
Π1(X)
T
""
Π1(B)
T
// Set
which induces a natural map
π1(X, x0)→ π1(B, b)→ Aut(p−1(b)).
The condition f∗(π1(X, x0))⊂ p∗(π1(E, e)) says that π1(X, x0) stabilizes ˜e. This implies
π1( ˜E, ˜e)∼= π1(X, x0).
Since X is locally path connected, ˜E is also locally path connected. Then path connected components and
connected components of ˜E coincide. Let ˜X be the (path) connected component of ˜E containing ˜e, then
π1( ˜E, ˜e)∼= π1(X, x0) implies that ˜p : ˜X→ X is a covering with ﬁber a single point, hence a homeomor-
phism. Its inverse deﬁnes a continuous map X→ ˜E whose composition with ˜E→ E gives F. □
4. π1(S1) AND APPLICATIONS
G-principal covering.
Deﬁnition 4.1. Let G be a discrete group. An action G× X → X is called properly discontinuous if
∀x∈ X,∃ open neighborhood U of x such that
g(U)∩ U = ∅, ∀g⁄= 1∈ G.
We deﬁne the orbit space X/G by the quotient X/∼ where x∼ g(x) for any x∈ X, g∈ G.
Proposition 4.2. Assume G acts properly discontinuously on X, then the quotient map X→ X/G is a covering.
Deﬁnition 4.3. A left (right) G-principal covering is a covering p : E→ B with a left (right) properly
discontinuous G-action on E over B
E
g //
p 
E
p
B
, ∀g∈ G
such that the induced map E/G→ B is a homeomorphism.
Example 4.4. ex : R1→ S1 is a Z-principal covering for the action n : t→ t + n,∀n∈ Z.

10 SI LI
Example 4.5. Sn→ RPn∼= Sn/Z2 is a Z2-principal covering.
Proposition 4.6. Let p : E→ B be a G-principal covering. Then transportation commutes with G-action, i.e.,
T[γ]◦ g = g◦ T[γ], ∀g∈ G, γ a path in B.
Theorem 4.7. Let p : E→ B be a G-principal covering, E path connected, e∈ E, b = p(e). Then we have an exact
sequence of groups
1→ π1(E, e)→ π1(B, b)→ G→ 1.
In other words, π1(E, e) is a normal subgroup of π1(B, b) and G = π1(B, b)/π1(E, e).
Proof. Let F = p−1(b). The previous proposition implies that π1(B, b)-action and G-action on F commute.
It induces a π1(B, b)× G-action on F. Consider its stabilizer at e and two projections
Stabe(π1(B, b)× G)
pr1
vv
pr2
’’π1(B, b) G
pr1 is an isomorphism and pr2 is an epimorphism with ker(pr2) = Stabe(π1(B, b)) = π1(E, e). □
Apply this theorem to the covering ex : R1→ S1, we ﬁnd a group isomorphism
deg : π1(S1)→ Z
which is called the degree map.
Applications.
Deﬁnition 4.8. i : A⊂ X be a subspace. A continuous map r : X→ A is called a retraction if r◦ i = 1A. It
is called a deformation retraction if furthermore i◦ r≃ 1X. We say A is a (deformation) retract of X if such
a (deformation) retraction exists.
Proposition 4.9. If i : A⊂ X is a retract, then r∗ : π1(A)→ π1(X) is injective.
Corollary 4.10. Let D2 be the unit disk in R2. Then its boundary S1 is not a retract of D2.
Theorem 4.11 (Brouwer ﬁxed point Theorem). Let f : D2→ D2. Then there exists x∈ D2 such that f (x) = x.
Proof. Assume f has no ﬁxed point. Let lx be the ray starting from f (x) pointing toward x. Then
D2→ S1, x→ lx∩ ∂D2
is a retraction of ∂D2 = S1⊂ D2. Contradiction. □
Theorem 4.12 (Fundamental Theorem of Algebra). Let f (x) = xn + c1xn−1 +··· + cn be a polynomial with
ci∈ C, n > 0. Then there exists a∈ C such that f (a) = 0.
Proof. Assume f has no root in C. Deﬁne a homotopy
F : S1× I→ S1, F(e2πiθ, t) = f (tan( πt
2 )e2πiθ)⏐⏐ f (tan( πt
2 )e2πiθ)
⏐⏐ .
Then deg(F|S1×0) = 0 and deg(F|S1×1) = n. Contradiction. □
Theorem 4.13 (Borsuk-Ulam). Let f : S2→ R2. Then∃x∈ S2 such that f (x) = f (−x).

INTRODUCTION TO ALGEBRAIC TOPOLOGY 11
Proof. Assume f (x)⁄= f (−x),∀x∈ S2. Deﬁne
ρ : S2→ S1, ρ(x) = f (x)− f (−x)
| f (x)− f (−x)| .
Let D2 be the upper hemi-sphere of S2. It deﬁnes a homotopy between constant map and ρ|∂D2 : S1→ S1,
hence deg(ρ|∂D2 ) = 0. On the other hand, ρ|∂D2 is antipode-preserving: ρ|∂D2 (−x) = −ρ|∂D2 (x), hence
deg(ρ|∂D2 ) is odd. Contradiction. □
Corollary 4.14 (Ham Sandwich Theorem). Let A1, A2 be two bounded regions of positive areas in R2. Then there
exists a line which cuts each Ai into half of equal areas.
Proof. Let A1, A2⊂ R2×{ 1}⊂ R3. Given u∈ S2, let Pu be the plane passing the origin and perpendicular
to the unit vector u. Let Ai(u) ={p∈ Ai|p· u≤ 0}. Deﬁne the map
f : S2→ R2, fi(u) = Area(Ai(u)).
By Borsuk-Ulam,∃u such that f (u) = f (−u). The intersection R2×{ 1}∩ Pu gives the required line. □
5. C LASSIFICATION OF COVERING
Deﬁnition 5.1. The universal cover of B is a covering map p : E→ B with E simply connected.
Theorem 5.2. Assume B is path connected and locally path connected. Then universal cover of B exists if and only
if B is semi-locally simply connected space.
Deﬁnition 5.3. We deﬁne the category Cov(B) of coverings of B
• objects are covering maps
• a morphism between two coverings p1 : E1→ B and p2 : E2→ B is a map f : E1→ E2 such that
the following diagram commutes
E1
f //
p1 
E2
p2
B
Deﬁnition 5.4. Let B be connected. We deﬁne Cov 0(B)⊂ Cov(B) to be the subcategory whose objects
consist of coverings of B which are connected spaces.
Proposition 5.5. Let B be connected and locally path connected. Then any morphism in Cov0(B) is a covering map.
Deﬁnition 5.6. We deﬁne the orbit category Orb(G)
• objects consist of (left) coset G/H, where H is a subgroup of G
• morphisms are G-equivariant maps: G/H1→ G/H2.
A morphism ρ : G/H1→ G/H2 is equivalent to an element γ∈ G such that H1⊂ γH2γ−1. Then
ρ(gH1) = gγH2.
In particular. G/H1 and G/H2 are equivalent if and only if H1 and H2 are conjugate subgroups of G.
For convenience, we also introduce the following category
Deﬁnition 5.7. We deﬁne the category G -Set

12 SI LI
• objects consist of sets with G-action
• morphisms are G-equivariant set maps.
Given a covering p : E→ B, b∈ B, we ﬁnd
p−1(b)∈ π1(B, b) -Set.
Proposition 5.8. Assume B is path connected and locally path connected. Let p 1, p2∈ Cov(B). Then
HomCov(B)(p1, p2)∼= Homπ1(B,b) -Set(p−1
1 (b), p−1
2 (b))
Proof. This is a consequence of Lifting Criterion and the Theorem of Uniqueness of lifting. □
Deﬁnition 5.9. Let B be path connected and p : E→ B be a connected covering. deck transformation (or
covering transformation) of p is a homeomorphism f : E→ E such that p◦ f = p. Let Aut (p) denote the
group of deck transformation.
Note that Aut(p) acts freely on E by the Uniqueness of Lifting.
Proposition 5.10. Let B be path connected and p : E→ B be a connected covering. Then Aut(p) acts properly
discontinuous on E.
We ﬁnd that the universal cover E is a π1(B, b)-principal covering.
Corollary 5.11. Assume B is path connected, locally path connected. Let p : E→ B be a connected covering,
e∈ E, b = p(e)∈ B, G = π1(B, b), H = π1(E, e). Then
Aut(p)∼= NG(H)/H
where NG(H) is the normalizer of H in G.
Proof. By the above proposition,
Aut(p)∼= HomG -Set(G/H, G/H) = NG(H)/H.
□
Theorem 5.12. Assume B is path connected, locally path connected and semi-locally simply connected. b∈ B. Then
there exists an equivalence of categories
Cov(B)≃ π1(B, b) -Set .
Proof. Let us denote π1 = π1(B, b). Let ˜p : ˜B→ B be a ﬁxed universal cover of B and ˜b∈ π−1(b) chosen.
We deﬁne the following functors
Cov(B)
F -- π1 -Set.
G
mm
Let p : E→ B be a covering, we deﬁne
F(p) = p−1(b).
Let S∈ π1 -Set, we deﬁne
G(S) = ˜B×π1 S = ˜B× S/∼, where (e· g, s)∼ (e, g· s),∀e∈ ˜B, s∈ S, g∈ π1.
Here e· g represents the (right) π1-action on ˜B. Then we have natural equivalences
F◦ G
η
≃ 1, G◦ F
τ
≃ 1.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 13
Here η is the natural equivalence
ηS∈ Homπ1 -Set(F◦ G(S), S), ηS(e, s) = g· s if e = ˜b· g.
τ is the natural equivalence
τE∈ HomCov(B)(p′, p)∼= Homπ1 -Set(p−1(b), p−1(b)), p′ : ˜B×π1 p−1(b)→ B,
which is determined by the identity map in Homπ1 -Set(p−1(b), p−1(b)). □
If we restrict the above theorem to connected coverings, we ﬁnd an equivalence of categories
Cov0(B)≃ Orb(π1(B, b)) .
The universal cover ˜B→ B corresponds to the orbit π1(B, b). For the orbit π1(B, b)/H, it corresponds to
E = ˜B/H→ B.
We have the following commuting diagram
π1(B, b)
##
// ˜π1(B, b)/H
zz1
=⇒ ˜B
f //

˜B/H
}}
B
A more intrinsic formulation is as follows. Given a covering p : E→ B, we obtain a transport functor
Tp : Π1(B)→ Set .
Given a commuting diagram
E1
f //
p1 
E2
p2
B
we ﬁnd a natural transformation
τ : Tp1 =⇒ Tp2, τ ={ f : p−1
1 (b)→ p−1
2 (b)|b∈ B}.
The above structure can be summerized by a functor
T : Cov(B)→ Fun(Π1(B), Set) .
Theorem 5.13. Assume B is path connected, locally path connected and semi-locally simply connected. Then
T : Cov(B)→ Fun(Π1(B), Set)
is an equivalence of categories.

14 SI LI
6. S EIFERT -VAN KAMPEN THEOREM
Product.
Deﬁnition 6.1. LetC be a category,{Aα}α∈I be a set of objects in C. Their product is an object A inC
together with πα : A→ Aα satisfying the following universal property: for any X inC and fα : X→ Aα,
there exists a unique morphism f : X→ A such that the following diagram commutes
X
∃! f //
fα   
A
πα

Aα
The universal property implies that the product is unique up to equivalence if it exists. We denote it by
∏
α∈I
Aα.
Example 6.2.
• Let Sα∈ Set. ∏
α
Sα ={(sα)|sα∈ Sα} is the Cartesian product.
• Let Xα∈ Top. ∏
α
Xα is the Cartesian product with induced product topology.
• Let Gα∈ Group. ∏
α
Gα is the Cartesian product with induced group structure.
Coproduct.
Deﬁnition 6.3. LetC be a category,{Aα}α∈I be a set of objects in C. Their coproduct is an object A inC
together with iα : Aα→ A satisfying the following universal property: for any X inC and fα : Aα→ X,
there exists a unique morphism f : A→ X such that the following diagram commutes
X A
∃! foo
Aα
πα
OO
fα
‘‘
The universal property implies that the product is unique up to equivalence if it exists. We denote it by
∐
α∈I
Aα.
Example 6.4.
• Let Xα∈ Top. ∐
α
Xα is the disjoint union of topological spaces.
• Let Gα∈ Group. ∐
α
Gα is the free product of groups.
Pushout.
Deﬁnition 6.5. LetC be a category. Given f1 : A0→ A1, f2 : A0→ A2, their pushout is an object A together
with π1 : A1→ A, π2 : A2→ A such that
• π1◦ f1 = π2◦ f2.
• pi : Ai→ X inC such that p1◦ f1 = p2◦ f2, there exists a unique F : A→ X such that pi = F◦ πi.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 15
It can be described by the following diagram
A0
f1 //
f2

A1
π1
 p1

A2
p2
((
π2 // A
∃!F
  
X
The universal property implies that the pushout is unique up to equivalence if it exists. We denote it by
A1 ∐
A0
A2.
Example 6.6.
• Let j1 : X0→ X1, j2 : X0→ X2 in Top. Their pushout is the quotient of X1 ∐ X2 by identifying
j1(y)∼ j2(y), y∈ X0. It glues X1, X2 along X0 using j1, j2.
• Let ρ1 : H→ G1, ρ2 : H→ G2 in Group, then
G1 ∐
H
G2 = ( G1∗ G2)/N
where G1∗ G2 is the free product and N is the normal subgroup generated by ρ1(h)ρ−1
2 (h), h∈ H.
Seifert-van Kampen Theorem.
Theorem 6.7 (Seifert-van Kampen Theorem, Groupoid version) . Let X = U∪ V where U , V⊂ X are open.
Then the following diagram
Π(U∩ V) //

Π(U)

Π(V) // Π(X)
is a pushout in the category Groupoid.
Corollary 6.8 (Seifert-van Kampen Theorem). Let X = U∪ V where U , V⊂ X are open and U , V, U∩ V are
path connected. Let x 0∈ U∩ V. Then the following diagram
π1(U∩ V, x0) //

π1(U, x0)

π(V, x0) // π(X, x0)
is a pushout in the category Group.
7. P ATH SPACE AND HOMOTOPY FIBER
Path space and loop space.
Deﬁnition 7.1. Let X, Y∈ Top, we let C(X, Y)∈ Top denote the set of continuous maps from X to Y with
the compact open topology. It is also denoted YX. For A⊂ X, B⊂ Y, we denote the subspace
C(X, A; Y, B) ={ f∈ C(X, Y)| f (A)⊂ B}.

16 SI LI
Theorem 7.2 (Exponential Correspondence) . Let Y be locally compact Hausdorff. Then the evaluation map
C(Y, Z)× Y→ Z is continuous and we have
HomTop(X× Y, Z) = HomTop(X, C(Y, Z)).
If furthermore X is Hausdorff, then
C(X× Y, Z) = C(X, C(Y, Z)).
Deﬁnition 7.3. Let X∈ Top, we deﬁne
• free path space PX = C(I, X) and based path space PxX = C(I, 0;X, x);
• free loop spaceLX = C(S1, X) and based loop space ΩxX = C(S1, 1;X, x) or simply ΩX.
We denote the two maps
PX
p1 //
p0

X
X
where p0(γ) = γ(0) is the start point and p1(γ) = γ(1) is the end point of the path γ. It induces
p = ( p0, p1) : PX→ X× X.
Theorem 7.4. Let X∈ Top.
(1) p : PX→ X× X is a ﬁbration.
(2) The map p0 : PX→ X is a ﬁbration whose ﬁber at x 0 is Px0 X.
(3) The map p1 : Px0 X→ X is a ﬁbration whose ﬁber at x 0 is Ωx0 X.
(4) p0 : PX→ X is homotopy equivalence. Px0 X is contractible.
Proof. (1) We need to prove the HLP of the diagram
Y×{ 0} // _

XI
p

Y× I //
?
99
X× X
Since I is locally compact Hausdorff, this is equivalent to the extension problem
Y×{ 0}× I∪ Y× I× ∂I //

X
Y× I× I
?
66
which is easily solved by observing that Y×{ 0}× I∪ Y× I× ∂I is a deformation retract of Y× I× I.
(2) follows from the composition of two ﬁbrations
PX //
##
X× X

X

INTRODUCTION TO ALGEBRAIC TOPOLOGY 17
(3) follows from the pull-back diagram
Px0 X

// PX

X
x0×id// X× X.
(4) follows from retracting the path. □
Deﬁnition 7.5. Let f : X→ Y. We deﬁne the mapping path space Pf by the pull-back diagram
Pf //

YI
p1

X
f // Y
An element of Pf is a pair (x, γ) where γ is a path in Y that ends at f (x).
Let ι : X ↪→ Pf represent the constant paths and q0 : Pf→ Y be the start point of the path. We have
X
ι //
f 
Pf
q0

Y
Theorem 7.6. ι : X→ Pf is strong deformation retract (hence homotopy equivalence) and q0 : Pf→ Y is a ﬁbration.
In particular, any map f : X→ Y is a composition of a homotopy equivalence with a ﬁbration.
Proof. The pull-back diagram
Pf

// YI

Y× X
id× f // Y× Y
implies that Pf→ Y× X is a ﬁbration. Since Y× X→ Y is also a ﬁbration, its composition q1 is a ﬁbration.
□
This theorem says that in hTop, every map is equivalent to a ﬁbration.
Fiber homotopy.
Deﬁnition 7.7. Let p1 : E1→ B and p2 : E2→ B be two ﬁbrations. A ﬁber map from p1 to p2 is a map
f : E1→ E2 such that p1 = p2◦ f :
E1
p1 
f // E2
p2
B
Two ﬁber maps f0, f1 : p1→ p2 are said to be ﬁber homotopic
f0≃B f1
if there exists a homotopy F : E1× I→ E2 from f0 to f1 such that F(−, t) is a ﬁber map for each t∈ I.
f : p1→ p2 is a ﬁber homotopic equivalence if there exists g : p2→ p1 such that both f◦ g and g◦ f are
ﬁber homotopic to identity maps.

18 SI LI
Proposition 7.8. Let p 1 : E1→ B and p 2 : E2→ B be two ﬁbrations and f : E1→ E2 be a ﬁber map. Assume
f : E1→ E2 is a homotopy equivalence, then f is a ﬁber homotopy equivalence. In particular, f : p−1
1 (b)→ p−1
2 (b)
is a homotopy equivalence for any b∈ B.
Proof. We only need to prove that for any ﬁber map f : E1→ E2 which is a homotopy equivalence, there is
a ﬁber map g : E2→ E1 such that g◦ f≃B 1. In fact, such a g is also a homotopy equivalence and we can
ﬁnd h : E1→ E2 such that h◦ g≃B 1. Then f≃B h◦ g◦ f≃B h, which implies f◦ g≃B 1 as well.
Let g : E2→ E1 be a homotopy inverse of f , so g = f−1 in hTop. We ﬁrst show that we can choose a
homotopy class of g such that g is a ﬁber map. In fact, consider the diagram
E1
p1

E2
p1◦g
&&
p2
88
g
>>
B
Since g◦ p1 = g◦ f◦ p2 is homotopic to p2 and p1 is a ﬁbration, we can lift the above homotopy to a
homotopy from g to g′ : E2→ E1 which lifts p2. Then g′ is a ﬁber map as required.
We further reduce the problem to prove the following
“Claim”: Let p : E→ B be a ﬁbration and f : E→ E is a ﬁber map that is homotopic to 1 E, then there is a
ﬁber map h : E→ E such that h◦ f≃B 1.
In fact, let f : E1→ E2 as in the proposition, g : E2→ E1 be a ﬁber map such that g◦ f≃ 1 as chosen
above. The “Claim” implies that we can ﬁnd a ﬁber map h : E1→ E1 such that h◦ g◦ f≃B 1. The the ﬁber
map ˜g = h◦ g has the required property that ˜g◦ f≃B 1.
Now we prove the “Claim”. Let F be a homotopy from f to 1E and G = p◦ F. Since p is ﬁbration, we
can construct a homotopy H that starts from 1E and lifts G. Here is the picture
E
f
))
1E
55 F E
p

E
p
))
p
55 G B
E
1E
))
h
55 H E
p

E
p
))
p
55 G B
Combining these two homotopy we ﬁnd a homotopy ˜F from h◦ f to 1E that lifts the following homotopy
˜G : E× I→ B, ˜G(−, t) =



G(−.2t) 0≤ t≤ 1/2
G(−, 2− 2t) 1/2≤ t≤ 1
Here is the picture
E
h◦ f
))
1E
55 ˜F E
p

E
p
))
p
55 ˜G B
It is easy to see that we can construct a homotopy K : E× I× I→ B such that
K(−, u, 0) = ˜G(−, u), K(−, u, 1) = p(−) = K(−, 0,t) = K(−, 1,t), ∀u, t∈ I.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 19
Since p is a ﬁbration, we can ﬁnd a lift ˜K : E× I× I→ E of K such that
˜K(−, u, 0) = ˜F(−, u).
Then we have the following ﬁber homotopy
h◦ f = ˜K(−, 0, 0)≃B ˜K(−, 0, 1)≃B ˜K(−, 1, 1)≃B ˜K(−, 1, 0) = 1E.
□
Homotopy ﬁber.
Deﬁnition 7.9. Let f : X→ Y, we deﬁne its homotopy ﬁber over y∈ Y to be the ﬁber of Pf→ Y over y.
If Y is path connected, then all homotopy ﬁbers are homotopic equivalent since Pf→ Y is a ﬁbration. In
this case we will usually write the following diagram
F // X
f

Y
where F denotes the homotopy ﬁber.
Proposition 7.10. If f : X→ Y is a ﬁbration, then its homotopy ﬁber at y is homotopy equivalent to f −1(y).
Proof. We have
X
ι //
f 
Pf
q1

Y
where ι is a homotopy equivalence. Then ι is ﬁber homotopy equivalence. □
8. G ROUP OBJECT AND HOMOTOPY GROUP
Deﬁnition 8.1. We deﬁne the category Top* of pointed topological space where
• An object (X, x0) is a topological space X with a based point x0∈ X
• morphisms are based continuous maps that map based point to based point.
Deﬁnition 8.2. Let X, Y ∈ Top* be two pointed spaces. A based homotopy between two based maps
f0, f1 : X → Y is a homotopy between f0, f1 relative to the base points. We denote [X, Y]0 to be based
homotopy classes of based maps. We deﬁne the category hTop* by the quotient of Top* where
HomhTop*
(X, Y) = [ X, Y]0.
The loop space deﬁnes a functor
Ω : Top*→ Top*, X→ ΩX
where ΩX is based at the constant loop to the base point of X. It is easy to see that it also deﬁnes
Ω : hTop*→ hTop* .

20 SI LI
Deﬁnition 8.3. LetC be a category with ﬁnite product and terminal object ⋆. A group object inC is an
object G inC together with morphisms
µ : G× G→ G, η : G→ G, ϵ : ⋆→ G
such that the following diagrams commute
(1) associativity:
G× G× G
1×µ //
µ×1

G× G
µ

G× G
µ // G
(2) unit:
G× ⋆
1×ϵ //
$$
G× G
µ

⋆× G
ϵ×1oo
zzG
(3) inverse
G

1×η// G× G
µ

G
η×1oo

⋆
ϵ // G ⋆
ϵoo
µ is called the multiplication, η is called the inverse, ϵ is called the unit.
Example 8.4.
• Group objects in Set are groups.
• Group objects in Top are topological groups.
• Group objects in hTop are called H-groups.
Proposition 8.5. LetC be a category with ﬁnite product and terminal object. Let G be a group object. Then
Hom(−, G) :C→ Group
deﬁnes a contravariant functor fromC to Group.
In the category Top* and hTop*, product exists and is given by
(X, x0)× (Y, y0) = ( X× Y, x0× y0).
Initial objects and terminal objects are a single pointed space.
Theorem 8.6. Let X∈ Top*. Then ΩX is a group object in hTop*.
Corollary 8.7. For any X, Y∈ Top*, [Y, ΩX]0 forms a group.
Deﬁnition 8.8. Let (X, x0)∈ Top*. We deﬁne its suspension ΣX by the quotient of X× I
ΣX = X× I/X× ∂I∪ x0× I .
It deﬁnes functors
Σ : Top*→ Top*, hTop *→ hTop* .

INTRODUCTION TO ALGEBRAIC TOPOLOGY 21
Example 8.9. ΣSn∼= Sn+1 are homeomorphic for any n≥ 0.
Deﬁnition 8.10. Let F :C→D and G :D→C be two functors. (F, G) is called adjoint pair if there are
isomorphisms
τ : HomD(FX, Y)∼= HomC (X, GY), ∀X∈C , Y∈D
which are natural for all X, Y. In other words, τ deﬁnes a natural equivalence between two functors
HomD(F−,−), HomC (−, G−) :Cop×D→ Set .
F (G) is called the left (right) adjoint of G (F), denoted by F⊢ G.
Example 8.11. Let Y be locally compat Hausdorff, then−× Y is left adjoint to C(Y,−).
Proposition 8.12. (Σ, Ω) is an adjoint pair in Top* and hTop*.
Deﬁnition 8.13. Let (X, x0)∈ Top*. We deﬁne the n-th homotopy group
πn(X, x0) = [ Sn, X]0 .
Sometimes we simply denote it by πn(X).
For n≥ 1, we know that
πn(X) = [ ΣSn−1, X]0 = [Sn−1, ΩX]
which is a group since ΩX is a group object.
Proposition 8.14. πn(X) is abelian if n≥ 2.
Proposition 8.15. Let X be path connected. There is a natural functor
T : Π1(X)→ Group
which sends x0 to πn(X, x0). In particular, there is a natural action of π1(X, x0) on πn(X, x0) and all πn(X, x0)’s
are isomorphic for different choices of x0.
Proposition 8.16. Let f : X→ Y be homotopy equivalence. Then
f∗ : πn(X, x0)→ πn(Y, f (x0))
is a group isomorphism.
9. E XACT PUPPE SEQUENCE
Deﬁnition 9.1. A sequence of maps of sets with base points
(A, a0)
f
→ (B, b0)
g
→ (C, c0)
is said to be exact at B if im( f ) = ker(g) where im( f ) = f (A), ker(g) = g−1(c0). A sequence
···→ An+1→ An→ An−1→···
is called an exact sequence if it is exact at every Ai.
Deﬁnition 9.2. A sequence of maps in hTop*
···→ Xn+1→ Xn→ Xn−1→···
is called exact if for any Y∈ hTop*, the following sequence of pointed sets is exact
···→ [Y, Xn+1]0→ [Y, Xn]0→ [Y, Xn−1]0→···

22 SI LI
Deﬁnition 9.3. Let f : (X, x0)→ (Y, y0) be a map in Top*. We deﬁne its homotopy ﬁber Ff in hTop* by the
pull-back diagram
Ff //
π

Py0Y
p1

X
f // Y.
Ff ={(x, γ)∈ X× PY|γ(0) = y0, γ(1) = f (x)}
Note that Ff is precisely the ﬁber of Pf→ Y over y0. We have the following commutative diagram
f−1(y0) //

Ff

X
ι //
f ##
Pf

Y
f−1(y0) //

Ff
π
wwX
When f is a ﬁbration, ι is a ﬁber homotopy equivalence, hence f−1(y0)→ Ff is a homotopy equivalence.
Lemma 9.4. The sequence
Ff
π→ X
f
→ Y
is exact at X in hTop*.
Proof. We ﬁrst observe that f◦ π factors through Py0Y which is contractible. Therefore f◦ π is null homo-
topy. Let Z∈ hTop*. Consider
[Z, Ff ]0
π∗→ [Z, X]0
f∗
→ [Z, Y]0.
Since f◦ π is null homotopic, we have im π∗⊂ ker f∗.
Let g : Z→ X such that [g]0∈ ker f∗. Let G be a homotopy of f◦ g to the trivial map. G deﬁnes a lifting
Py0Y
p1

Z
g //
G
77
X
f // Y
By the deﬁnition of pull-back, the pair(G, g) deﬁnes a map to Ff such that the following diagram commutes
Ff //
π

Py0Y
p1

Z
g //
??
X
f // Y
This implies [g]0∈ im π∗. Therefore ker f∗⊂ im π∗. □
The ﬁber of Ff over x0 is precisely ΩY. We ﬁnd the following sequence of pointed maps
ΩX
Ω f
→ ΩY→ Ff
π→ X
f
→ Y.
Lemma 9.5. The sequence ΩX
Ω f
→ ΩY→ Ff
π→ X
f
→ Y is exact in hTop*.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 23
Proof. We construct the following diagram in hTop* with all vertical arrows homotopy equivalences
ΩX //
j′

ΩY //
j

Ff
π //

X
f //

Y

Fπ′
π′′
// Fπ
π′
// Ff
π // X
f // Y
Since Ff
π→ X is a ﬁbration with ﬁber ΩY, we have a commutative diagram
ΩY = π−1(x0)
j //
%%
Fπ

Ff
where j is a homotopy equivalence. This explains the second square above.
Similarly, the ﬁber of the ﬁbration Fπ→ Ff is ΩX. We ﬁnd the following diagram
ΩX
j′

k
!!
Fπ′
π′′
// Fπ
Fπ′ is the homotopy ﬁber, and j′ is homotopy equivalence as before. However, the following diagram
ΩX
k ""
Ω f // ΩY
j

Fπ.
is NOT commutative in Top*
However, it is easy to see that j◦ Ω f is homotopic to k, so this diagram is commutative in hTop*. Therefore
ΩX
j′

Ω f // ΩY
j

Fπ′
π′′
// Fπ
is commutative in hTop* .
The lemma follows from the above commutative diagram in hTop* and that j, j′ are homotopy equivalence.
□
Lemma 9.6. Let X1→ X2→ X3 be exact in hTop*, then so is ΩX1→ ΩX2→ ΩX3.
Proof. Use the fact that Ω is right adjoint to the suspension Σ. □
The following Theorem is a direct consequence of the above Lemmas.
Theorem 9.7 (Exact Puppe Sequence). Let f : X→ Y in Top*. Then the following sequence in exact in hTop*
···→ Ω2Y→ ΩFf→ ΩX→ ΩY→ Ff→ X→ Y.

24 SI LI
Theorem 9.8. Let π : E→ B be a map in Top*. Assume π is ﬁbration whose ﬁber over the base point is F. Then we
have the following exact sequence of homotopy groups
···→ πn(F)→ πn(E)→ πn(B)→ πn−1(F)→···→ π0(E)→ π0(B)
where all homotopy groups are understood to have based points on the relevant spaces.
Proof. Since π is a ﬁbration, F is homotopy equivalent to Fπ. Apply [S0,−] to the Puppe Sequence.
□
The following proposition gives a criterion for ﬁbration
Theorem 9.9. Let p : E→ B with B paracompact Hausdorff. Assume there exists an open cover {Uα} of B such
that p−1(Uα)→ Uα is a ﬁbration. Then p is a ﬁbration.
Corollary 9.10. Let p : E→ B be a ﬁber bundle with B paracompact Hausdorff. Then p is a ﬁbration.
Proposition 9.11. If i < n, then πi(Sn) = 0.
Example 9.12. We have the Hopf ﬁbrationS3→ S2 with ﬁber S1. Its associated exact sequence of homotopy
groups implies
π2(S2)∼= Z, πn(S3)∼= πn(S2) for n≥ 3.
10. C OFIBRATION
Coﬁbration.
Deﬁnition 10.1. A map i : A→ X is said to have the homotopy extension property (HEP) with respect to
Y if for any maps f : X→ Y and F : A→ YI such that p0◦ F = f◦ i, there exists a map ˜F : X→ YI such
that the following diagram commutes
Y X
foo
∃ ˜F
~~
YI
p0
OO
A
i
OO
F
oo
Deﬁnition 10.2. A map i : A→ X is called a coﬁbration if it has HEP for any spaces.
The notion of coﬁbration is dual to that of the ﬁbration. Fibration is deﬁned by the HLP of the diagram
Y
˜f // _

E
p

Y× I
F
//
∃ ˜F
<<
B
If we reverse the arrows and observe that Y× I is dual to the path space YI via the adjointness of (−)× I
and (−)I, we arrive at HEP .

INTRODUCTION TO ALGEBRAIC TOPOLOGY 25
Deﬁnition 10.3. Let f : A→ X. We deﬁne its mapping cylinder M f by the push-out
A×{ 0}
f

// A× I

X×{ 0} // M f
The HEP of i : A→ X is equivalent to the property of ﬁlling the commutative diagram
Mi

// Y
X× I
∃?
==
It is enough to consider Y = Mi to check coﬁbration by the universal property of push-out. .
Proposition 10.4. Let i : A→ X and j : Mi→ X× I be the above map. Then i is a coﬁbration if and only there
exists r : X× I→ Mi such that r◦ j = 1Mi.
Proposition 10.5. Let i : A→ X be a coﬁbration. Then i is a homeomorphism to its image (i.e. embedding). If
furthermore X is Hausdorff. Then i has closed image (i.e. closed embedding).
Proof. Use the retraction in the previous proposition
Mi

1Mi // Mi
X× I
<<
□
Lemma 10.6. Let A be a closed subspace of X. Then the inclusion map i : A⊂ X is a coﬁbration if and only if
X×{ 0}∪ A× I is a retract of X× I.
Proof. If i is closed embedding, then Mi is homeomorphic to the subspace X×{ 0}∪ A× I of X× I. □
Remark 10.7. This lemma still holds if we only assume A is a subspace without closeness condition. It can
be shown that if X×{ 0}∪ A× I is a retract of X× I, then Mi is again homeomorphic to the subspace
X×{ 0}∪ A× I of X× I. This homeomorphism may fail without the assumption of the existence of retract.
Example 10.8. The inclusion Sn−1 ↪→ Dn is a coﬁbration.
Deﬁnition 10.9. Let A be a subspace of X. We say (X, A) is coﬁbered if the inclusion A⊂ X is a coﬁbration.
Deﬁnition 10.10. Let A be a subspace of X. A is called a neighborhood deformation retract (NDR) if there
exists a continuous map u : X→ I with A = u−1(0) and a homotopy H : X× I→ X such that



H(x, 0) = x ∀x∈ X
H(a, t) = a if (a, t)∈ A× I
H(x, 1)∈ A if u(x) < 1
Note that if A is a NDR of X, then A is a strong deformation retract of the open subset u−1([0, 1)) of X.
Theorem 10.11. Let A be a closed subspace of X. Then the following conditions are equivalent

26 SI LI
(1) (X, A) is a coﬁbered pair.
(2) A is a NDR of X.
(3) X×{ 0}∪ A× I is a retract of X× I.
(4) X×{ 0}∪ A× I is a strong deformation retract of X× I.
Proposition 10.12. Let i : A→ X be a coﬁbration, f : A→ B is a map. Consider the push-out
A
i

f // B
j

X // Y
Then j : B→ Y is also a coﬁbration.
Deﬁnition 10.13. Let i : A→ X, j : A→ Y be coﬁbrations. A map f : X→ Y is called a coﬁber map if the
following diagram commutes
A
i

j

X
f // Y
A coﬁber homotopy between two coﬁber maps f , g : X→ Y is a homotopy of coﬁber maps between f
andg. Coﬁber homotopy equivalence is deﬁned similarly.
Proposition 10.14. Let i : A→ X, j : A→ Y be coﬁbrations. Let f : X→ Y be a coﬁber map. Assume f is a
homotopy equivalence. Then f is a coﬁber homotopy equivalence.
Let f : A→ X be a map. Consider the diagram of mapping cylinder
A
f

i0 // A× I

X // M f
There is a natural commuting diagram
A
i1
~~
f

M f
r // X
Here i1(a) = ( a, 1), r(a, t) = f (a), r(x, 0) = x. It is easy to see that r is a homotopy equivalence. Moreover,
A is a closed subspace of M f and M f×{ 0}∪ A× I is a retract of M f× I. Therefore i1 is a coﬁbration.
We arrive at the dual result of ﬁbrations: any map f : A→ X can be factored as f = r◦ i1 where i1 is a
coﬁbration and r is a homotopy equivalence. Moreover, if f is a coﬁbration, then r : M f → X is a coﬁber
homotopy equivalence.
Coﬁber exact sequence.
Now we work with the category Top* and hTop*.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 27
Deﬁnition 10.15. Let (X, x0)∈ Top*. We deﬁne its cone in Top* by
CX = X∧ I = X× I/X×{ 0}∪ x0× I.
Given f : X→ Y in Top*, we deﬁne its homotopy coﬁber C f by the push-out
X
f

i1 // CX

Y
j // C f
where i1(x) = ( x, 1).
The closed embedding i1 is a coﬁbration. Therefore j : Y → C f is also a coﬁbration. Note that the
quotient of C f by Y is precisely ΣX. We can extend the above maps by
X // Y // C f // ΣX // ΣY // ΣC f // Σ2X //···
Deﬁnition 10.16. A sequence of maps in hTop*
···→ Xn+1→ Xn→ Xn−1→···
is called co-exact if for any Y∈ hTop*, the following sequence of pointed sets is exact
···→ [Xn−1, Y]0→ [Xn, Y]0→ [Xn+1, Y]0→···
Theorem 10.17 (Co-exact Puppe Sequence). Let f : X→ Y in Top*. The following sequence is co-exact in hTop*
X // Y // C f // ΣX // ΣY // ΣC f // Σ2X //···
Proposition 10.18. Let i : A→ X be a coﬁbration. Then the natural map
¯r : C f→ X/A
is a homotopy equivalence. In other words, coﬁber is homotopy equivalent to the homotopy coﬁber.
Theorem 10.19. Let i : A→ X be a coﬁbration. The following sequence is co-exact in hTop*
A // X // X/A // ΣA // ΣX // Σ(X/A) // Σ2A //···
11. CW COMPLEX
Dn denotes the n-disk and en = Dn− ∂Dn = Dn− Sn−1 denotes the open disk called n-cell.
Deﬁnition 11.1. A cell decomposition of a space X is a familyE ={en
α|α∈ Jn} of subspaces of X such that
each en
α is a n-cell and we have a disjoint union of sets
X = ∐ en
α.
The n-skeleton of X is the subspace
Xn = ∐
α∈Jm,m≤n
em
α .
Deﬁnition 11.2. A CW complex is a pair (X,E ) of a Hausdorff space X with a cell decomposition such that
(1) Characteristic map: for each n-cell en
α, there is a characteristic map Φenα : Dn→ X such that the
restriction of Φeαn to Dn− Sn−1 is a homeomorphism to en
α and Φenα (Sn−1)⊂ Xn−1.

28 SI LI
(2) Closure ﬁniteness: for any cell e∈E the closure ¯e intersects only a ﬁnite number of other cells inE.
(3) Weak topology: a subset A⊂ X is closed if and only if A∩ ¯e is closed in ¯e for each e∈E .
We say X is n-dim CW complex if the maximal dimension of cells inE is n (n could be ∞).
Note that the Hausdorff property of X implies that ¯e = Φe(Dn) for each cell e∈E . The surjective map
Φe : Dn→ ¯e is a quotient since Dn is compact and ¯e is Hausdorff. Let us denote the full characteristic maps
Φ : ∐
e∈E
Dn ∐ Φe
−→ X.
Then the weak topology implies that Φ is a quotient map. This implies the following proposition.
Proposition 11.3. Let (X,E ) be a CW complex. Then f : X→ Y is continuous if and only if f ◦ Φe is continuous
for each e∈E .
Proposition 11.4. Let (X,E ) be a CW complex. Then any compact subspace of X meets only ﬁnite many cells inE.
Example 11.5. Rn, Sn, CPn, HPn, S∞, CP∞, HP∞.
Deﬁnition 11.6. A subcomplex (X′,E′) of the CW complex (X,E ) is a closed subspace X′⊂ X with a cell
decompositionE′⊂E . We will just write X′⊂ X when the cell decomposition is clear. We will also write
X′ =|E′|. Equivalently, a subcomplex is described by a subsetE′⊂E such that
e1∈E ′, e2∈E , ¯e1∩ e2⁄= ∅ =⇒ e2∈E ′.
Example 11.7. The n-skeleton Xn is a subcomplex of X of dimension≤ n.
Deﬁnition 11.8. Given f : Sn−1→ X. Consider the push-out
Sn−1 f // _

X _

Dn Φ f
// Dn ∐ f X
We say Dn ∐ f X is obtained by attaching an n-cell to X. Φ f is called the characteristic map of the attached
n-cell. More generally, if we have a set of maps fα : Sn−1→ X, the push-out
∐α Sn−1 f // _

X _

∐α Dn Φ f
// (∐ Dn) ∐ f X
f = ∐ fα
is called X with n-cells attached.
Proposition 11.9. Let (X,E ) be a CW complex, andE = ∐E n whereE n is the set of n-cells. Then the diagram
∐
e∈E n
Sn−1 ∂Φn
//
 _

Xn−1

∐
e∈E n
Dn Φn
// Xn
Φn = ∐
e∈E n
Φe
is a push-out. In particular, Xn is obtained from Xn−1 by attaching n-cells in X.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 29
Proof. This follows from the fact that Xn−1 is a closed subspace of Xn and the weak topology.
□
The converse is also true. The next proposition can be viewed as an alternate deﬁnition of CW complex.
Proposition 11.10. Suppose we have a sequence of spaces
∅ = X−1⊂ X0⊂ X1⊂···⊂ Xn⊂ Xn+1⊂···
where Xn is obtained from Xn−1 by attaching n-cells. Let X =∪n≥0Xn be the union with the weak topology: A⊂ X
is closed if and only if A∩ Xn is closed in Xn for each n. Then X is a CW complex.
Proof. The nontrivial part is to show that X is Hausdorff.
□
Deﬁnition 11.11. Let A be a subspace of X. A CW decomposition of (X, A) consiss of a sequence
A = X−1⊂ X0⊂ X1⊂···⊂ X
such that Xn is obtained from Xn−1 by attaching n-cells and X carries the weak topology with respect to the
subspaces Xn. The pair (X, A) is called a relative CW complex.
Note that for a relative CW complex (X, A), A itself may not have any cell structures.
Proposition 11.12. Let (X, A) be a relative CW complex. Then A⊂ X is a coﬁbration.
Proof. S n−1 ↪→ Dn is a coﬁbration, and coﬁbration is preserved under push-out and compositions.
□
Corollary 11.13. Let X be a CW complex and X′ be a CW subcomplex. Then X′→ X is a coﬁbration.
Proof. (X, X′) is a relative CW complex. □
Proposition 11.14. Let X.Y be CW complexes. X is locally compact. Then X× Y is a CW complex
12. W HITEHEAD THEOREM
Relative homotopy group.
Deﬁnition 12.1. The deﬁne the category TopP of topological pairs where an object (X, A) is a topological
space X with a subspace X, and morphisms (X, A)→ (Y, B) are continuous maps f : X→ Y such that
f (A)⊂ B. A homotopy between two maps f1, f2 : (X, A)→ (Y, B) is a homotopy F : X× I→ Y between
f0, f1 such that F|X×t(A)⊂ B for any t∈ I.
The quotient category of TopP by homotopy of maps is denoted by hTopP . The pointed versions are
deﬁned similarly and denoted by TopP* and hTopP*. Morphisms in hTopP and hTopP* are denoted by
[(X, A), (Y, B)], [(X, A), (Y, B)]0.
Lemma 12.2. Let f : (X, A)→ (Y, B). Let ¯f = f|A. Then the sequence
(X, A)→ (Y, B)→ (C f , C ¯f )
is co-exact in hTopP*. When A = B = point, this recovers the co-exactness of homotopy coﬁber.

30 SI LI
Theorem 12.3. Let f : (X, A)→ (Y, B). Let ¯f = f|A. Then the sequence
(X, A)→ (Y, B)→ (C f , C ¯f )→ Σ(X, A)→ Σ(Y, B)→ Σ(C f , C ¯f )→ Σ2(X, A)→···
is co-exact in hTopP*. This generalizes the co-exact Puppe sequence to the pair case.
Deﬁnition 12.4. Let (X, A)∈ TopP*. We deﬁne the relative homotopy group πn(X, A)
πn(X, A) = [( Dn, Sn−1), (X, A)]0.
We will also write πn(X, A; x0) when we want to specify the base point.
Note that for n≥ 2
(Dn, Sn−1)≃ Σn−1(D1, S0),
therefore πn(X, A) is a group for n≥ 2 by the adjunct pair (Σ, Ω).
Lemma 12.5. f : (Dn, Sn−1)→ (X, A) is zero in πn(X, A) if and only if f is homotopic rel S n−1 to a map whose
image lies in A.
This lemma can be summarized by the following diagram
Sn−1 _

// A _

Dn ’’
f
77
g
==
X
Here g maps Dn to A and g≃ f rel Sn−1.
Theorem 12.6. Let B⊂ A⊂ X in Top*. Then there is a long exact sequence
···→ πn(A, B) i∗→ πn(X, B)
j∗
→ πn(X, A) ∂→ πn−1(A, B)···→ π0(X)
Here the boundary map ∂ sends f ∈ [(Dn, Sn−1), (X, A)]0 to its restriction to Sn−1 = Dn−1/Sn−2 viewed as
∂ f : (Dn−1, Sn−2)→ (A, B)
where ∂ f sends the whole S n−2 to the base point in B.
Proof. We prove the case for A = B = base point x0∈ X. Consider
f : (S0,{0})→ (S0, S0).
Let ¯f = f|{0} :{0}→ S0. It is easy to see that
(C f , C ¯f )≃ (D1, S0).
Since Σn(S0) = Sn, Σ(Dn, Sn−1) = ( Dn+1, Sn), the co-exact Puppe sequence
(S0,{0})→ (S0, S0)→ (D1, S0)→ (S1,{0})→ (S1, S1)→ (D2, S1)→ (S2,{0})→···
implies the exact sequence
···→ πn(A) i∗→ πn(X)
j∗
→ πn(X, A) ∂→ πn−1(A)···→ π0(X)
□
Deﬁnition 12.7. A pair (X, A) is called n-connected (n≥ 0) if π0(A)→ π0(X) is surjective andπk(X, A; x0) =
0 for any 1≤ k≤ n, x0∈ A.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 31
From the long exact sequence
···→ πn(A) i∗→ πn(X)
j∗
→ πn(X, A) ∂→ πn−1(A)···→ π0(X)
we see that (X, A) is n-connected if and only if for any x0∈ A



πr(A, x0)→ πr(X, x0) is bijective for r < n
πn(A, x0)→ πn(X, x0) is surjective
Deﬁnition 12.8. A map f : X→ Y is called an n-equivalence (n≥ 0) if for any x0∈ X



f∗ : πr(X, x0)→ πr(Y, f (x0)) is bijective for r < n
f∗ : πn(X, x0)→ πn(Y, f (x0)) is surjective
f is called weak homotopy equivalence or ∞-equivalence if f is n-equivalence for any n≥ 0.
Example 12.9. For any n≥ 0, the pair (Dn+1, Sn) is n-connected.
CW complex.
Lemma 12.10. Let X be obtained from A by attaching n-cells. Let (Y, B) be a pair such thatπn(Y, B; b) = 0,∀b∈ B
if n≥ 1 or π0(B)→ π0(Y) surjective if n = 0. Then any map from (X, A)→ (Y, B) is homotopic rel A to a map
from X to B.
Proof. Apply the universal property of push-out and the result for Sn−1 ↪→ Dn.
∐ Sn−1 // _

A _

// B _

∐ Dn //
66
X &&
88
@@
Y
□
Theorem 12.11. Let (X, A) be a relative CW complex with relative dimension ≤ n. Let (Y, B) be n-connected
(0≤ n≤ ∞). Then any map from (X, A) to (Y, B) is homotopic relative to A to a map from X to B.
A _

// B _

X &&
88
??
Y
Proof. Apply the previous Lemma to
A⊂ X0⊂ X1⊂···⊂ Xn = X
and observe that all embeddings are coﬁbrations. □
Proposition 12.12. Let f : X→ Y be a weak homotopy equivalence, P be a CW complex. Then
f∗ : [P, X]→ [P, Y]
is a bijection.

32 SI LI
Proof. We can assume f is an embedding and (Y, X) is ∞-connected. Otherwise replace Y by M f .
Surjectivity follows from the diagram
∅ _

// X _

P &&
88
??
Y
Injectivity follows from the diagram (observe P× I, P× ∂I are CW complexes)
P× ∂I _

// X _

P× I ’’
77
<<
Y
□
Theorem 12.13 (Whitehead Theorem). A map between CW complexes is a weak homotopy equivalence if and only
if it is a homotopy equivalence.
Proof. Let f : X→ Y be a weak homotopy equivalence between CW complexes. We have bijections
f∗ : [X, X]0→ [X, Y]0, f∗ : [Y, X]→ [Y, Y]0.
Let g∈ [Y, X]0 such that f∗[g] = 1Y. Then g◦ f≃ 1Y. On the other hand,
f∗[ f◦ g] = [ f◦ g◦ f ]≃ [ f◦ 1] = [ f ] = f∗[1X]
we ﬁnd [ f◦ g] = 1X. Therefore f is a homotopy equivalence. The reverse direction is obvious. □
13. C ELLULAR AND CW APPROXIMATIONS
Cellular Approximation.
Deﬁnition 13.1. Let (X, Y) be CW complexes. A map f : X→ Y is called cellular if f (Xn)⊂ Yn for any n.
We deﬁne the category CW whose objects are CW complexes and morphisms are cellular maps.
Deﬁnition 13.2. A cellular homotopy between two cellular maps X→ Y of CW complexes is a homotopy
X× I→ Y that is itself a cellular map. Here I is naturally a CW complex. We deﬁne the quotient category
hCW of CW whose morphisms are cellular homotopy class of cellular maps.
Lemma 13.3. Let X be obtained from A by attaching n-cells (n≥ 1), then (X, A) is (n− 1)-connected.
Proof. Let r < n. Consider a diagram
Sr−1 _

// A _

Dr f // X
Since Dr is compact, f (Dr) meets only ﬁnitely many attached n-cells on X, say e1,··· , em. Let pi be the
center of ei. Let e∗
i = ei−{ pi}. Y = X−{ p1,··· , pm}. We subdivide Dr into small disks Dr =∪αDr
α
such that f (Dr
α)⊂ Y or f (Dr
α)⊂ e∗
i . For each Dr
α such that f (Dr
α)⊂ ei but not in Y, we use the fact that

INTRODUCTION TO ALGEBRAIC TOPOLOGY 33
(ei, e∗
i )≃ (Dn, Sn−1) is (n− 1)-connected to ﬁnd a homotopy rel ∂Dr
α to adjust mapping Dr
α into e∗
i . It glues
together to obtain
Sr−1 _

// Y _

Dr ’’
77
==
X
Then we can further ﬁnd a homotopy
Sr−1 _

// A _

Dr &&
88
==
Y
□
Corollary 13.4. Let (X, A) be a relative CW complex, then for any n≥ 0, the pair (X, Xn) is n-connected.
Theorem 13.5. Let f : (X, A)→ ( ˜X, ˜A) between relative CW complexes which is cellular on a subcomplex (Y, B)
of (X, A). Then f is homotopic rel Y to a cellular map g : (X, A)→ ( ˜X, ˜A).
Proof. Assume we have constructed fn−1 : (X, A)→ ( ˜X, ˜A) which is homotopic to f rel Y and cellular on
the (n− 1)-skeleton Xn−1. Let Xn be obtained from Xn−1 by attaching n-cells. Consider
Xn−1 _

// ˜Xn _

Xn fn−1 // ˜X
Since Xn is obtained from Xn−1 by attaching n-cells and ( ˜X, ˜Xn) is n-connected,
Xn−1 _

// ˜Xn _

Xn ’’
fn−1
77
<<
˜X
we can ﬁnd a homotopy rel Xn−1 from fn−1|Xn : Xn→ ˜X to a map Xn→ ˜Xn. Since f is cellular on Y,
we can choose this homotopy rel Y by adjusting only those n-cells not in Y. This homotopy extends to a
homotopy rel Xn−1∪ Y from fn−1 to a map fn : X→ ˜X since Xn⊂ X is a coﬁbration. Then f∞ works. □
Theorem 13.6 (Cellular Approximation Theorem). Any map between relative CW complexes is homotopic to a
cellular map. If two cellular maps between relative CW complexes are homotopic, then they are cellular homotopic.
Proof. Apply the previous Theorem to (X, ∅) and (X× I, X× ∂I). □
Remark 13.7. This theorem says that hCW is a full subcategory of hTop.

34 SI LI
CW Approximation.
Deﬁnition 13.8. A CW approximation of a topological space Y is a CW complex X with a weak homotopy
equivalence f : X→ Y.
Theorem 13.9. Any space has a CW approximation.
Proof. We may assume Y is path connected. We construct a CW approximation X of Y by induction on the
skeleton Xn. Assume we have constructed fn : Xn→ Y which is an n-equivalence. We attach an (n + 1)-cell
to every generator of ker(πn(Xn)→ πn(Y)) to obtain ˜Xn+1. We can extend fn to a map ˜fn+1 : ˜Xn+1→ Y
∐ Sn
 _

// Xn

fn

∐ Dn+1 //
))
˜Xn+1
˜fn+1
!!
Y
Since ( ˜Xn+1, Xn) is also n-connected, ˜fn+1 is an n-equivalence. By construction and the surjectivity of
πn( ˜Xn+1)→ πn(Xn), ˜fn+1 deﬁnes also an isomorphism for πn( ˜Xn+1)→ πn(Y).
Now for every generator Sn+1
α of coker(πn+1( ˜Xn+1)→ πn+1(Y)), we take a wedge sum to obtain
Xn+1 = ˜Xn+1∨ (∨αSn+1).
Then the induced map fn+1 : Xn+1→ Y extends fn to an (n + 1)-equivalence. Inductively we obtain a
weak homotopy equivalence f∞ : X = X∞→ Y. □
Theorem 13.10. Let f : X→ Y. Let ΓX→ X, and ΓY→ Y be CW approximations. Then there exists a unique
map in [ΓX, ΓY] making the following diagram commutes in hTop
ΓX

Γ f // ΓY

X
f // Y
Proof. Weak homotopy equivalence of ΓY→ Y implies the bijection [ΓX, ΓY]→ [ΓX, Y].
□
Deﬁnition 13.11. Two spaces X1, X2 are said to have the same weak homotopy type if there exists a space
Y and weak homotopy equivalences fi : Y→ Xi, i = 1, 2.
Proposition 13.12. Weak homotopy type is an equivalence relation.
14. E ILENBERG -MACLANE SPACE
Graphs.
Deﬁnition 14.1. A graph is a one-dimensional CW complex. The points of the 0-skeleton are calledvertices
and the 1-cells are called edges.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 35
By deﬁnition, a basis for the topology of a graph consists of the open intervals in the edges together with
the path-connected neighborhoods of the vertices. A graph is compact if and only if it contains only ﬁnitely
many vertices and edges.
Deﬁnition 14.2. A subgraph of a graph is a CW subcomplex. A tree is a contractible graph. By a tree in a
graph X we mean a subgraph that is a tree. We call a tree in X maximal if it contains all the vertices of X.
Proposition 14.3. Every connected graph contains a maximal tree, and in fact any tree in the graph is contained in
a maximal tree.
Lemma 14.4. Let A⊂ X be a coﬁbration and A is contractible, then X→ X/A is a homotopy equivalence.
Theorem 14.5. For a connected graph X with maximal tree T , π1(X) is a free group with basis the classes corre-
sponding to the edges e of X− T.
Theorem 14.6 (Nielsen-Schreier theorem). Every subgroup of a free group is itself free.
Proof. Let F be a free group with basis indexed by I. Let X = ⋁
I∈B
S1. Then π1(X) = F. Let G⊂ F and
˜X→ X be the covering such that π1( ˜X) = G. Then ˜X is also a CW complex. It follows that G is free. □
πn(Sn).
We have seen that πk(Sn) = 1 for k < n. In this subsection we compute
πn(Sn) = [ Sn, Sn]0∼= Z.
Given f : Sn→ Sn, its class [ f ]∈ Z under the above isomorphism is called the degree of f .
Theorem 14.7 (Homotopy Excision Theorem)). Let (A, C), (B, C) be relative CW complex. Let X be the push-out
C //

B

A // X
If (A, C) is m-connected and (B, C) is n-connected, then
πi(A, C)→ πi(X, B)
is an isomorphism for i < m + n, and a surjection for i = m + n.
Corollary 14.8 (Freudenthal Suspension Theorem). The suspension map
πi(Sn)→ πi+1(Sn+1)
is an isomorphism for i < 2n− 1 and a surjection for i = 2n− 1.
Proof. Apply Homotopy Excision to X = Sn+1, C = Sn, A the upper half disk, B the lower half disk. □
Freudenthal Suspension Theorem holds similarly replacing Sn by general (n− 1)-connected space.
Proposition 14.9. πn(Sn)∼= Z for n≥ 1.
Proof. Freudenthal Suspension Theorem reduces to showπ2(S2)∼= Z. This follows from the Hopf ﬁbration
S1→ S3→ S2.
□

36 SI LI
Eilenberg-MacLane Space.
Deﬁnition 14.10. An Eilenberg-MacLane Space is a CW complex K(G, n) such that πn(K(G, n))∼= G and
πk(K(G, n)) = 0 for k⁄= n. Here G is abelian if n > 1.
Theorem 14.11. Eilenberg-MacLane Space K(G, n) exists.
Proof. We prove the case for n≥ 2. There exists an exact sequence
0→ F1→ F2→ G→ 0
where F1, F2 are free abelian groups. Let Bi be a basis of Fi. Let
A =
⋁
i∈B1
Sn, B =
⋁
j∈B2
Sn.
A, B are (n− 1)-connected and πn(A) = F1, πn(B) = F2. Using the degree map, we can construct
f : A→ B
such that πn(A)→ πn(B) realizes the map F1→ F2. Let X be obtained from B by attaching (n + 1)-cells
via f . Then X is (n− 1)-connected and πn(X) = G. Now we proceed as the proof of CW approximation
theorem to attach cells of dimension≥ (n + 2) to kill all higher homotopy groups of X to get K(G, n). □
As we will see, K(G, n) is the representing space for cohomology functor with coefﬁcients in G
Hn(X; G)∼= [X, K(G, n)] for any CW complex X.
Example 14.12. S1 = K(Z, 1). Connected graphs are Eilenberg-MacLane space for free groups at n = 1.
Example 14.13. Using the ﬁbration S1→ S∞→ CP∞, we ﬁnd CP∞ = K(Z, 2).
Example 14.14. A knot is an embedding K : S1 ↪→ S3. Let G = π1(S3− K). Then S3− K = K(G, 1).
15. S INGULAR HOMOLOGY
Chain complex.
Deﬁnition 15.1. Let R be a commutative ring. A chain complex over R is sequence of R-module maps
···→ Cn+1
∂n+1
→ Cn
∂n
→ Cn−1→···
such that ∂n◦ ∂n+1 = 0∀n. When R is not speciﬁed, we mean chain complex of abelian groups (i.e. R = Z).
Sometimes we just write the map by ∂ and the chain complex by (C•, ∂). Then ∂n = ∂|Cn and ∂2 = 0.
Deﬁnition 15.2. A chain map f : C•→ C′• between two chain complexes over R is a sequence of R-module
maps fn : Cn→ C′
n such that the following diagram commutes
··· // Cn+1
fn+1

∂n+1 // Cn
fn

∂n // Cn−1
fn−1

//···
··· // C′
n+1 ∂′
n+1
// C′
n ∂′n
// C′
n−1 //···
We simply write it as
f◦ ∂ = ∂′◦ f

INTRODUCTION TO ALGEBRAIC TOPOLOGY 37
Chain complexes over R together with chain maps form the category Ch•(R) of chain complexes over R,
or simply Ch• when R = Z.
Deﬁnition 15.3. Given a chain complex (C•, ∂), its n-cycles Zn and n-boundaries Bn are
Zn = Ker(∂ : Cn→ Cn−1), Bn = Im(∂ : Cn+1→ Cn).
∂2 = 0 implies Bn⊂ Zn. We deﬁne the n-th homology group by
Hn(C•, ∂) := Zn
Bn
= ker(∂n)
im(∂n+1) .
A chain complex C• is called acyclic or exact if Hn(C•) = 0,∀n.
Proposition 15.4. n-th homology group deﬁnes a functor
Hn : Ch•→ Ab
Deﬁnition 15.5. A chain homotopy f
s
≃ g between two chain maps f , g : C• → C′• is a sequence of
homomorphisms sn : Cn→ C′
n+1 such that fn− gn = sn−1◦ ∂n + ∂′
n+1◦ sn, or simply
f− g = s◦ ∂ + ∂′◦ s .
Two complexes C•, C′• are called chain homotopy equivalent if there exists chain maps f : C•→ C′• and
h : C′•→ C• such that f◦ g≃ 1 and g◦ f≃ 1.
Proposition 15.6. Chain homotopy deﬁnes an equivalence relation on chain maps and compatible with compositions.
In other word, chain homotopy deﬁnes an equivalence relation on Ch•. We deﬁne the quotient category
hCh• = Ch• /≃ .
Chain homotopy equivalence becomes an equivalence in hCh•.
Proposition 15.7. Let f , g be chain homotopic chain maps. Then they induce identical map on homology groups
Hn( f ) = Hn(g) : Hn(C•)→ Hn(C′
•).
In other words, the functor Hn factor through
Hn : Ch•→ hCh•→ Ab .
Singular homology.
Deﬁnition 15.8. We deﬁne the standard n-simplex
∆n ={(t0,··· , tn)∈ Rn+1|
n
∑
i=0
ti = 1, ti≥ 0}
We let{v0,··· , vn} denote its vertices. Here vi = (0,··· , 0, 1, 0,··· , 0) where 1 sits at the i-th position.
Deﬁnition 15.9. Let X be a topological space. A singular n-simplex in X is a continuous map σ : ∆n→ X.
For each n≥ 0, we deﬁne Sn(X) as the free abelian group with basis all singular n-simplexes in X
Sn(X) =
⨁
σ∈Hom(∆n,X)
Zσ.
The elements of Sn(X) are called singular n-chains in X.

38 SI LI
A singular n-chain is given by a ﬁnite formal sum
γ = ∑
σ∈Hom(∆n,X)
mσσ, mσ∈ Z and only ﬁnitely many mσ’s are nonzero.
The abelian group structure is:−γ := ∑σ(−mσ)σ and
(∑
σ
mσσ) + (∑
σ
m′
σσ) = ∑
σ
(mσ + m′
σ)σ.
Deﬁnition 15.10. Given a n-simplex σ : ∆n→ X and 0≤ i≤ n, we deﬁne
∂(i)σ : ∆n−1→ X
to be the(n− 1)-simplex by restrictingσ to the i-th face of∆n whose vertices are given by{v0, v1,··· , ˆvi,··· , vn}.
We deﬁne the boundary map
∂ : Sn(X)→ Sn−1(X)
by the abelian group homomorphism generated by
∂σ :=
n
∑
i=0
(−1)i∂(i)σ .
Proposition 15.11. (S•(X), ∂) deﬁnes a chain complex, i.e., ∂2 = ∂◦ ∂ = 0.
Deﬁnition 15.12. For each n≥ 0, we deﬁne n-th singular homology group of X by
Hn(X) := Hn(S•(X), ∂) .
Let f : X→ Y be a continuous map, it deﬁnes a chain map
S•( f ) : S•(X)→ S•(Y).
This deﬁnes the functor of singular chain complex
S• : Top→ Ch• .
Singular homology group can be viewed as the composition of functors
Top→ Ch•
Hn
→ Ab .
Proposition 15.13. Let f , g : X → Y be homotopic maps. Then S •( f ), S•(g) : S•(X) → S•(Y) are chain
homotopic. In particular, they induce identical map Hn( f ) = Hn(g) : Hn(X)→ Hn(Y).
Proof. We only need to prove that for i0, i1 : X→ X× I, the induced map
S•(i0), S•(i1) : S•(X)→ S•(X× I)
are chain homotopic. Then their composition with the homotopy X× I→ Y gives the proposition.
Let us deﬁne a homotopy
s : Sn(X)→ Sn+1(X× I).
For σ : ∆n→ X, we deﬁne (topologically)
s(σ) : ∆n× I σ×1→ X× I
Here we treat ∆n× I as a collection of (n + 1)-simplexes as follows: let{v0,··· , vn} denote the vertices of
∆n, then the vertices of ∆n× I contain two copies{v0,··· , vn} and{w0,··· , wn}. Then
∆n× I =
n
∑
i=0
(−1)n[v0, v1,··· vi, wi, wi+1,··· , wn]

INTRODUCTION TO ALGEBRAIC TOPOLOGY 39
cuts ∆n× I into (n + 1)-simplexes. Its sum deﬁnes s(σ)∈ Sn+1(X× I). The intuitive formula holds
∂(∆n× I) = ∆× ∂I− (∂∆n)× I
as an equation for singular chains, leading to
S•(i1)− S•(i0) = ∂◦ s + s◦ ∂.
□
Theorem 15.14. Singular homologies are homotopy invariants. They factor through
Hn : hTop→ hCh•→ Ab .
16. E XACT HOMOLOGY SEQUENCE
Exact homology sequence.
Deﬁnition 16.1. Chain maps 0→ C′•
i→ C•
p
→ C′′•→ 0 is called an short exact sequence if for each n
0→ C′
n
i→ Cn
p
→ C′′
n→ 0
is an exact sequence of abelian groups.
We have the following commuting diagram
  
0 // C′
n+1
i //
∂′

Cn+1
p //
∂

C′′
n+1
∂′′

// 0
0 // C′
n
i //
∂′

Cn
p //
∂

C′′
n
∂′′

// 0
0 // C′
n−1
i //
∂′

Cn−1
p //
∂

C′′
n−1
∂′′

// 0
Lemma/Deﬁnition 16.2. Let 0→ C′•
i→ C•
p
→ C′′•→ 0 be a short exact sequence. There is a natural homomorphism
δ : Hn(C′′
• )→ Hn−1(C′
•)
called the connecting map. It induces a long exact sequence of abelian groups
···→ Hn(C′
•) i∗→ Hn(C•)
p∗
→ Hn(C′′
• ) δ→ Hn−1(C′
•) i∗→ Hn−1(C•)
p∗
→ Hn−1(C′′
• )→···
The connecting map δ is natural in the sense that a commutative diagram of complexes with exact rows
0 // C′• //

C• //

C′′• //

0
0 // D′• // D• // D′′• // 0

40 SI LI
induces a commutative diagram of abelian groups with exact rows
··· // Hn(C′′• ) //

Hn(C•) //

Hn(C′′• )

δ // Hn−1(C′•) //

···
··· // Hn(D′′• ) // Hn(D•) // Hn(D′′• )
δ // Hn−1(D′•) //···
Relative homology.
Deﬁnition 16.3. Let A⊂ X be a subspace. It indues a natural injective chain map S•(A) ↪→ S•(X). We
deﬁne the singular chain complex of X relative to A to be
Sn(X, A) := Sn(X)/Sn(A)
with the induced differential. Its homology Hn(X, A) := Hn(S•(X, A)) is called then-th relative homology.
Proposition 16.4. For A⊂ X, there is a long exact sequence of abelian groups
···→ Hn(A)→ Hn(X)→ Hn(X, A) δ→ Hn−1(A)→···
Proof. This follows from the short exact sequence of complexes
0→ S•(A)→ S•(X)→ S•(X, A)→ 0.
□
Let us deﬁne relative n-cycles Zn(X, A) and relative n-boundaries Bn(X, A) to be
Zn(X, A) ={γ∈ Sn(X) : ∂γ∈ Sn−1(A)}
Bn(X, A) = Bn(X) + Sn(A)⊂ Sn(X).
Then it is easy to check that Sn(A)⊂ Bn(X, A)⊂ Zn(X, A)⊂ Sn(X) and
Hn(X, A) = Zn(X, A)/Bn(X, A)
Two relative n-cycles γ1, γ2 deﬁnes the same class [γ1] = [ γ2] in Hn(X, A) if and only if γ1− γ2 is homolo-
gous to a chain in A. The connecting map
δ : Hn(X, A)→ Hn−1(A)
can be understood as follows: a n-cycle in H n(X, A) is represented by a n-chain γ∈ Sn(X) such that its
boundary ∂(γ) lies in A. Viewing ∂(γ) as a (n− 1)-cycle in A, then
δ[γ] = [ ∂(γ)].
Let f : (X, A)→ (Y, B) be a map of pairs. It naturally induces a commutative diagram
0 // S•(A) //

S•(X) //

S•(X, A) //

0
0 // S•(B) // S•(Y) // S•(Y, B) // 0
which further induces compatible maps on various homology groups.
Proposition 16.5. Let{Xα} be path connected components of X, then
Hn(X) =
⨁
α
Hn(Xα).

INTRODUCTION TO ALGEBRAIC TOPOLOGY 41
Proposition 16.6. Let X be path connected. Then H0(X)∼= Z.
In general, we have a surjective map
ϵ : H0(X)→ Z, ∑
p∈X
mp p→ ∑
p
mp.
Deﬁnition 16.7. We deﬁne the reduced homology group by
˜Hn(X) =



Hn(X) n > 0
ker(H0(X)→ Z) n = 0
The long exact sequence still holds for the reduced case
···→ ˜Hn(A)→ ˜Hn(X)→ Hn(X, A) δ→ ˜Hn−1(A)→···
Example 16.8. If X is contractible, then ˜Hn(X) = 0 for all n.
Example 16.9. Let x0∈ X be a point. Using the long exact sequence for A ={x0}⊂ X, we ﬁnd
Hn(X, x0) = ˜Hn(X).
17. E XCISION
The fundamental property of homology which makes it computable is excision.
Barycentric Subdivision.
Deﬁnition 17.1. Let ∆n be the standard n-simplex with vertices v0,··· , vn. We deﬁne its barycenter to be
c(∆n) = 1
n + 1
n
∑
i=0
vi∈ ∆n.
Deﬁnition 17.2. We deﬁne the barycentric subdivision B∆n of a n-simplex ∆n as follows:
(1) B∆0 = ∆0.
(2) Let F0,··· , Fn be the n-simplexes of faces of ∆n+1. c be the barycenter of ∆n+1. Then B∆n+1 consists
of (n + 1)-simplexes with ordered vertices [c, w0,··· , wn] where [w0,··· , wn] is a n-simplexes in
BF0,··· , BFn.
Equivalently, a simplex in B∆n is indexed by a sequence{S0⊂ S1···⊂ Sn = ∆n} where Si is a face of
Si+1. Then its vertices are [c(Sn), c(Sn−1),··· , c(S0)]. It is seen that ∆n is the union of simplexes in B∆n.
Deﬁnition 17.3. We deﬁne the n-chain of barycentric subdivision Bn by
Bn = ∑
α
±σα∈ Sn(∆n)
where the summation is over all sequence α ={S0⊂ S1···⊂ Sn = ∆n}. σα is the simplex with ordered
vertices [c(Sn), c(Sn−1),··· , c(S0)], viewed as a singular n-chain in ∆n. The sign± is about orientation: if
the orientation of [c(Sn), c(Sn−1),··· , c(S0)] coincides with that of ∆n, we take +; otherwise we take−.

42 SI LI
Deﬁnition 17.4. We deﬁne the composition map denoted by
Sk(∆m)× Sn(∆k)→ Sn(∆m), σ× η→ σ◦ η.
This is deﬁned on generators via the composition ∆n→ ∆k→ ∆m and extended linearly on singular chains.
Similarly, there is a natural map denoted by
Sn(∆m) : Sm(X)→ Sn(X), η : σ→ η∗(σ) = σ◦ η
where η∗(σ) = σ◦ η is the composition of σ with η.
Example 17.5. Let ˜∂n∈ Sn−1(∆n) be the faces. Then ˜∂n◦ ˜∂n−1 = 0 and
∂n = ˜∂∗
n : Sn(X)→ Sn−1(x)
deﬁnes the boundary map in singular chains.
Lemma 17.6.
Bn◦ ˜∂n = ˜∂n◦ Bn−1
Proof. The choice of ordering and orientation guarantees that
∂Bn = B(∂∆n)
where B(∂∆n) is the barycentric subdivision of faces ∂∆n of ∆n, viewed as a (n− 1)-chain in ∆n. □
Deﬁnition 17.7. We deﬁne the barycentric subdivision on singular chain complex by
B∗ : S•(X)→ S•(X)
where B∗ = B∗
n on Sn(X).
Lemma 17.8. B : S•(X)→ S•(X) is a chain map. Moreover, it is chain homotopic to the identity map.
Proof. The previous lemma implies
∂n◦ B∗
n = ˜∂∗
n◦ B∗
n = ( Bn◦ ˜∂n)∗ = ( ˜∂n◦ Bn−1)∗ = B∗
n−1◦ ∂n.
This show that B∗ is a chain map.
To show the chain homotopy, it is enough to constructTn+1∈ Sn+1(∆n) such that
Bn− 1∆n = Tn+1◦ ˜∂n+1 + ˜∂n◦ Tn.
Here 1∆n : ∆n→ ∆n is the identity map, viewed as a n-chain. Then T∗
n+1 gives the required homotopy. T
is constructed inductively in n as follows. T1 = 0. Suppose we have constructed Tn. We need to ﬁnd Tn+1
such that
∂(Tn+1) = Bn− 1∆n− ˜∂n◦ Tn.
Observe
∂
(
Bn− 1∆n− ˜∂n◦ Tn
)
=
(
Bn− 1∆n− ˜∂n◦ Tn
)
◦ ˜∂n = ˜∂n◦
(
Bn−1− 1∆n−1− Tn◦ ˜∂n
)
= ˜∂n◦ ˜∂n−1◦ Tn−1 = 0.
Therefore Bn− 1∆n− ˜∂n◦ Tn is a n-cycle. However H n(∆n) = 0 for n≥ 1. It follows that Tn+1 can be
constructed.
□
Corollary 17.9. The barycentric subdivision map B∗ : S•(X)→ S•(X) is a quasi-isomorphism.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 43
Excision.
Theorem 17.10 (Excision). Let U⊂ A⊂ X be subspaces such that ¯U⊂ A◦ (the interior of A). Then the inclusion
i : (X− U, A− U) ↪→ (X, A) induces isomorphisms
i∗ : Hn(X− U, A− U)∼= Hn(X, A), ∀n.
Proof. Let us call σ : ∆n→ X small if
σ(∆n)⊂ A or σ(∆n)⊂ X− U.
Let S′•(X)⊂ S•(X) denote the subcomplex generated by small simplexes, and S′•(X, A) deﬁned by the
exact sequence
0→ S•(A)→ S′(X)→ S′(X, A)→ 0.
It is easy to see that
S′
•(X, A)∼= S•(X− U, A− U).
There is a natural commutative diagram of chain maps
0 // S•(A) //

S′•(X) //

S′•(X, A) //

0
0 // S•(A) // S•(X) // S•(X, A) // 0
By the Five Lemma, it is enough to show that
S′
•(X)→ S•(X)
is a quasi-isomorphism.
(1) Injectivity of H(S′•(X))→ H(S•(X)):
Let α be a cycle in S′•(X) and α = ∂β for β∈ S•(X). Take k big enough that (B∗)k(β)∈ S′(X). Then
(B∗)k(α) = ∂(B∗)k(β).
Hence (B∗)k(α) is zero in H(S′•(X)), so is α which is homologous to (B∗)k(α).
(2) Surjectivity of H(S′•(X))→ H(S•(X)):
Let α be a cycle in S•(X). Take k big enough that (B∗)k(α)∈ S′•(X). Then (B∗)k(α) is a small cycle
which is homologous to α. □
Theorem 17.11. Let X1, X2 be subspaces of X and X = X◦
1∪ X◦
2. Then
H•(X1, X1∩ X2)→ H•(X, X2)
is an isomorphism for all n.
Proof. Apply Excision to U = X− X1, A = X2.
□
Theorem 17.12 (Mayer-Vietoris). Let X1, X2 be subspaces of X and X = X◦
1∪ X◦
2. Then there is an exact sequence
···→ Hn(X1∩ X2)
(i1∗,i2∗)
→ Hn(X1)⊕ Hn(X2)
j1∗−j2∗
→ Hn(X) δ→ Hn−1(X1∩ X2)→···
It is also true for the reduced homology.

44 SI LI
Proof. Let S•(X1) + S•(X2)⊂ S•(X) be the subspace spanned by S•(X1) and S•(X2). We have a short exact
sequence
0→ S•(X1∩ X2)
(i1,i2)
→ S•(X1)⊕ S•(X2)
j1−j2
→ S•(X1) + S•(X2)→ 0.
Similar to the proof of Excision via barycentric subdivision, the embedding S•(X1) + S•(X2)⊂ S•(X) is a
quasi-isomorphism. Mayer-Vietoris sequence follows. □
Theorem 17.13. Let A⊂ X be a closed subspace. Assume A is a strong deformation retract of a neighborhood in X.
Then the map (X, A)→ (X/A, A/A) induces an isomorphism
H•(X, A)∼= ˜H•(X/A).
Proof. Let U be an open neighborhood of A that deformation retracts to A. Then H•(A)∼= H•(U), hence
H•(X, A)∼= H•(X, U)
by Five Lemma. Since A is closed and U is open, we can apply Excision to ﬁnd
H•(X, A)∼= H•(X, U)∼= H•(X− A, U− A).
The same consideration applied to (X/A, A/A) and U/A gives
H•(X/A, A/A)∼= H•(X/A− A/A, U/A− A/A) = H•(X− A, U− A).
□
This Theorem in particular applies to coﬁbrations.
18. H OMOLOGY OF SPHERES
Theorem 18.1. The reduced homology of the sphere Sn is given by
˜Hk(Sn) =



Z k = n
0 k⁄= n
Proof. Let Sn = Dn
+∪ Dn
−, where Dn
+ (Dn
−) is the upper (lower) hemi-sphere and we choose a bit bigger
ones to satisfy excision. Dn
+∩ Dn
− = Sn−1× I≃ Sn−1. Apply Mayer-Vietoris sequence we ﬁnd
˜Hk(Sn) = ˜Hk−1(Sn−1).
The theorem follows. □
Corollary 18.2. If m⁄= n, then Rm and Rn are not homeomorphic.
Deﬁnition 18.3. A continous map f : Sn→ Sn (n≥ 0) has degree d, denoted by deg( f ) = d, if
f∗ : ˜Hn(Sn) = Z→ ˜Hn(Sn) = Z
is multiplication by d.
Lemma 18.4. Let f , g : Sn→ Sn be continuous maps.
(1) deg ( f◦ g) = deg( f ) deg(g).
(2) If f ≃ g are homotopic, then deg( f ) = deg(g)
(3) If f is a homotopy equivalence, then deg( f ) =±1.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 45
Proposition 18.5. Let r : Sn→ Sn, (x0,··· , xn)→ (−x0, x1,··· , xn) be the reﬂection. Then
deg(r) =−1.
Proof. Prove by induction onn. This is true forn = 0. The induction follows from the commutative diagram
˜Hn(Sn)
r∗

δ // ˜Hn−1(Sn−1)
r∗

˜Hn(Sn)
δ // ˜Hn−1(Sn−1)
□
Corollary 18.6. Let σ : Sn→ Sn, (x0,··· , xn)→ (−x0,··· ,−xn) be the antipodal map. Then
deg(σ) = (−1)n+1.
Proof. σ is a composition of n + 1 reﬂections. □
Theorem 18.7 (Hairy Ball Theorem). Sn has a nowhere vanishing tangent vector ﬁeld if and only if n is odd.
Proof. If n is odd, we construct
v(x0,··· , xn) = (−x1, x0,−x3, x2,··· ).
Conversely, assume v is no-where vanishing vector ﬁeld. Let
f : Sn→ Sn, x→ v(x)
|v(x)| .
The map
F : Sn× I→ Sn, F(x, t) = cos(πt)x + sin(πt) f (x)
deﬁnes a homotopy between the identity map 1 and the antipodal map σ. It follows that
deg(σ) = 1 =⇒ n = odd.
□
Theorem 18.8 (Brower’s Fixed Point Theorem). Any continuous map f : Dn→ Dn has a ﬁxed point.
Proof. Assume f has no ﬁxed point. Deﬁne
r : Dn→ Sn−1
where r(p) is the intersection of ∂Dn with the ray starting from f (p) pointing toward p. Then r deﬁnes a
retract of Sn−1 ↪→ Dn. This implies H•(Dn) = H•(Sn−1)⊕ H•(Dn, Sn−1), a contradiction.
□
We give a geometric interpretation of the degree of f : Sn→ Sn. Let V⊂ Sn be a small open ball such
that f−1(V)→ V is a disjoint union of open balls
f−1(V) = U1∪···∪ Ud.

46 SI LI
Let fi : ¯Ui/∂ ¯Ui∼= Sn→ ¯V/∂ ¯V∼= Sn. We have the commutative diagram
Hn(Sn) //
f∗

Hn(Sn/Sn−∪ iUi)∼=⊕iHn(Sn)
⊕i( fi)∗

Hn(Sn) // Hn(Sn/Sn− V)∼= Hn(Sn)
It is easy to see that ﬁrst row is k→ (k, k,··· , k) and the second row is k→ k. It follows that
deg( f ) =
d
∑
i=1
deg( fi).
Note that when f−1(V) → V is a covering map, then f : Ui → V is a homeomorphism. We have
deg( fi) =±1 and deg( f ) is given by a counting with signs.
Example 18.9. Identify S2 = C∪{ ∞}. Consider the map f : S2→ S2, z→ zk. Then deg( f ) = k.
19. C ELLULAR HOMOLOGY
Cellular homology.
Deﬁnition 19.1. Let (X, A) be a relative CW complex with skeletons: A = X−1⊂ X0⊂···⊂ Xn⊂··· .
We deﬁne the relative cellular chain complex (Ccell
• (X, A), ∂)
···→ Ccell
n (X, A) ∂→ Ccell
n−1(X, A) ∂→···→ Ccell
0 (X, A)→ 0
where Ccell
n (X, A) := Hn(Xn, Xn−1) and the boundary map ∂ is deﬁned by the commutative diagram
Hn(Xn, Xn−1)
∂ //
δ
((
Hn−1(Xn−1, Xn−2)
Hn−1(Xn−1, A)
j
55
Here δ is the connecting map of relative homology for A⊂ Xn−1⊂ Xn and j is the natural map.
Assume Xn is obtained from Xn−1 by attaching n-cells indexed by Jn
∐
α∈Jn
Sn−1 f //
 _

Xn−1 _

∐
α∈Jn
Dn Φ f
// Xn
Since Xn−1 ↪→ Xn is a coﬁbration,
Ccell
n (X, A)∼= ˜Hn(Xn/Xn−1)∼=
⨁
Jn
˜Hn(Sn)∼=
⨁
Jn
Z

INTRODUCTION TO ALGEBRAIC TOPOLOGY 47
is the free abelian group generated by each attached Hn(Dn, Sn−1). Using the diagram
Hn(Xn, Xn−1)
∂n //
δn
((
Hn−1(Xn−1, Xn−2)
∂n−1 //
δn−1
))
Hn−2(Xn−2, Xn−3)
Hn−1(Xn−1, A)
jn
55
Hn−1(Xn−2, A)
jn−1
55
and δn−1◦ jn = 0, we see that
∂n−1◦ ∂n = jn−1◦ δn−1◦ jn◦ δn = 0.
Therefore (Ccell
• (X, A), ∂) indeed deﬁnes a chain complex.
Deﬁnition 19.2. Let (X, A) be a relative CW complex. We deﬁne its n-th relative cellular homology by
Hcell
n (X, A) := Hn(Ccell
• (X, A), ∂) .
When A = ∅, we simply denote it by Hcell
n (X) called the n-th cellular homology.
Lemma 19.3. Let (X, A) be a relative CW complex. Let 0≤ q < p≤ ∞. Then
Hn(Xp, Xq) = 0, n≤ q or n > p.
Theorem 19.4. Let (X, A) be a relative CW complex. Then cellular homology coincides with singular homology
Hcell
n (X, A)∼= Hn(X, A) .
Proof. Consider the following commutative diagram
Hn+1(Xn+1, Xn)

∂n+1
))
Hn(Xn−2, A)(= 0)

Hn(Xn−1, A)(= 0) // Hn(Xn, A) //

Hn(Xn, Xn−1) //
∂n
))
Hn−1(Xn−1, A)

Hn(Xn+1, A)

Hn−1(Xn−1, Xn−2)

Hn(Xn+1, Xn)(= 0) Hn−1(Xn−2, A)(= 0)
Diagram chasing implies Hn(Xn+1, A)∼= Hcell
n (X, A). Theorem follows from the exact sequence
Hn+1(X, Xn+1)(= 0)→ Hn(Xn+1, A)→ Hn(X, A)→ Hn(X, Xn+1)(= 0)
□
Let f : (X, A)→ (Y, B) be a cellular map. It induces a map on cellular homology
f∗ : Hcell
• (X, A)→ Hcell
• (Y, B).
Therefore in the category of CW complexes, we can work entirely with cellular homology which is combi-
natorially easier to compute by the next formula.

48 SI LI
Cellular Boundary Formula.
Let us now analyze cellular differential
∂n : Hn(Xn, Xn−1)→ Hn−1(Xn−1, Xn−2).
For each n-cell en
α, we have the gluing map
fenα : Sn−1→ Xn−1.
This deﬁnes a map
¯fenα : Sn−1→ Xn−1/Xn−2 =
⋁
Jn−1
Sn−1
which induces a degree map
( ¯fenα )∗ : ˜Hn−1(Sn−1)∼= Z→
⨁
Jn−1
˜Hn−1(Sn−1)∼=
⨁
Jn−1
Z.
Collecting all n-cells, this generates the degree map
dn :
⨁
Jn
Z→
⨁
Jn−1
Z.
Theorem 19.5. Under the identiﬁcation Ccell
n (Xn, Xn−1)∼=
⨁
Jn
Z, cellular differential coincides with the degree map
∂n∼= dn .
Example 19.6. CPn has a CW structure with a single 2m-cell for each m≤ n. Since there is no odd dim cells,
the degree map d = 0. We ﬁnd
Hk(CPn) =



Z k = 0, 2,··· , 2n
0 otherwise
Example 19.7. A closed oriented surface Σg of genus g has a CW structure with a 0-cell, 2g 1-cells, and a
2-cell. It is easy to see that the degree map is zero. We ﬁnd
Hk(Σg) =



Z k = 0
Z2g k = 1
Z k = 2
0 k > 2.
Example 19.8. RPn has a CW structure with a k-cell for each 0≤ k≤ n. The degree map is dk = 1 + (−1)k.
Hk(RPn) =



Z k = 0
Z/2Z 0 < k < n, k odd
Z k = n = odd
0 k = n = even
0 k > n

INTRODUCTION TO ALGEBRAIC TOPOLOGY 49
Euler characteristic.
Deﬁnition 19.9. Let X be a ﬁnite CW complex of dimension n and denote by ci the number of i-cells of X.
The Euler characteristic of X is deﬁned as:
χ(X) := ∑
i
(−1)ici.
Recall that any ﬁnitely generaed abelian group G is decomposed into a free part and a torsion part
G∼= Zr⊕ Z/m1Z⊕···⊕ Z/mkZ.
The integer r := rk(G) is called the rank of G.
Theorem 19.10. Let X be a ﬁnite CW complex. Then
χ(X) = ∑
i
(−1)ibi(X)
where bi(X) := rk(Hi(X)) is called the i-th Betti number of X In particular, χ(X) is independent of the chosen CW
structure on X and only depend on the cellular homotopy class of X.
20. C OHOMOLOGY AND UNIVERSAL COEFFICIENT THEOREM
Cohomology.
Deﬁnition 20.1. Let R be a commutative ring. A cochain complex over R is sequence of R-module maps
···→ Cn−1 dn−1
→ Cn dn
→ Cn−1→···
such that dn◦ dn−1 = 0∀n. When R is not speciﬁed, we mean cochain complex of abelian groups (i.e.
R = Z).
Sometimes we just write the map by d and the cochain complex by (C•, d). Then dn = d|Cn and d2 = 0.
Deﬁnition 20.2. Given a cochain complex (C•, d), its n-cocycles Zn and n-coboundaries Bn are
Zn = Ker(d : Cn→ Cn+1), Bn = Im(d : Cn−1→ Cn).
d2 = 0 implies Bn⊂ Zn. We deﬁne the n-th cohomology group by
Hn(C•, d) := Zn
Bn = ker(dn)
im(dn−1) .
A cochain complex C• is called acyclic or exact if Hn(C•) = 0,∀n.
We are interested in the following relation between cochain and chain complex.
Deﬁnition 20.3. Let (C•, ∂) be a chain complex over R, and G be a R-module. We deﬁne its dual cochain
complex (C•, d) = HomR(C•, G) by
··· HomR(Cn−1, G)→ HomR(Cn, G)→ HomR(Cn+1, G)→···
Here given f∈ HomR(Cn, G), we deﬁne dn f∈ HomR(Cn+1, G) by
dn f (c) := f (∂n+1(c)), ∀c∈ Cn+1.

50 SI LI
Deﬁnition 20.4. Let G be an abelian group and X be a topological space. For n≥ 0, we deﬁne the group of
singular n-cochains in X with coefﬁcient in G to be
Sn(X; G) := Hom(Sn(X), G).
The dual cochain complex S•(X; G) = Hom(S•(X), G) is called the singular cochain complex with coefﬁ-
cient in G. Its cohomology is called the singular cohomology with coefﬁcient in G, denoted by
Hn(X; G) := Hn(S•(X; G)).
When G = Z, we simply write it as Hn(X).
Theorem 20.5. Hn(−; G) deﬁnes a contra-variant functor
Hn(−; G) : hTop→ Ab .
Example 20.6 (Dimension Axiom). Let X be a point. Then
Hn(X; G) =



G k = 0
0 k > 0
Lemma 20.7. Let G be a R-module. If 0→ A1→ A2→ A3→ 0 is an exact sequence of R-modules, then applying
HomR(−, G) gives an exact sequence
0→ HomR(A3, G)→ HomR(A2, G)→ HomR(A1, G).
If A3 is a free R-module (or more generally projective R-module), then the last morphism is also surjective.
Deﬁnition 20.8. Let G be an abelian group. Let A⊂ X be a subspace. We deﬁne the relative singular
cochain complex with coefﬁcient in G by
S•(X, A; G) := Hom(S•(X)/S•(A), G).
Its cohomology is called the relative singular cohomology, denoted by H•(X, A; G).
Since S•(X)/S•(A) is a free abelian group, we have a short exact sequence of cochain complex
0→ S•(X, A; G)→ S•(X; G)→ S•(A; G)→ 0
which induces a long exact sequence of cohomology groups
0→ H0(X, A; G)→ H0(X; G)→ H0(A; G)→ H1(X, A; G)→··· .
Moreover, the connecting maps
δ : Hn(A, G)→ Hn+1(X, A; G)
is natural in the same sense as homology case.
Theorem 20.9 (Excision). Let U⊂ A⊂ X be subspaces such that ¯U⊂ A◦ (the interior of A). Then the inclusion
i : (X− U, A− U) ↪→ (X, A) induces isomorphisms
i∗ : Hn(X, A; G)∼= Hn(X− U, A− U; G), ∀n.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 51
Universal Coefﬁcient Theorem for Cohomology.
Deﬁnition 20.10. Let M, N be two R-modules. Let P•→ M be a free R-module resolution of M:
··· Pn→ Pn−1→··· P1→ P0→ M→ 0
is an exact sequence of R-modules and Pi’s are free. We deﬁne the Ext group
Extk
R(M, N) = Hk(Hom(P•, N))
and the Tor group
TorR
k (M, N) = Hk(P•⊗R N).
Note that
Ext0
R(M, N) = HomR(M, N), Tor R
0 (M, N) = M⊗R N.
Ext and Tor are called the derived functors of Hom and ⊗. It is a classical result in homological algebra
that Extk
R(M, N) and TorR
k (M, N) don’t depend on the choice of resolution of M. They are functorial with
respect to both variables and TorR
k is symmetric in two variables
TorR
k (M, N) = TorR
k (N, M).
Moreover, for any short exact sequence of R-modules
0→ M1→ M2→ M3→ 0
there associate long exact sequences
0→ HomR(M3, N)→ HomR(M2, N)→ HomR(M1, N)
→ Ext1
R(M3, N)→ Ext1
R(M2, N)→ Ext1
R(M1, N)
→ Ext2
R(M3, N))→ Ext2
R(M2, N)→ Ext2
R(M1, N)→···
and
0→ HomR(N, M1)→ HomR(N, M2)→ HomR(N, M3)
→ Ext1
R(N, M1)→ Ext1
R(N, M2)→ Ext1
R(N, M3)
→ Ext2
R(N, M1))→ Ext2
R(N, M2)→ Ext2
R(N, M3)→···
and
···→ TorR
2 (M1, N)→ TorR
2 (M2, N)→ TorR
3 (M3, N)
→ TorR
1 (M1, N)→ TorR
1 (M2, N)→ TorR
1 (M3, N)
→ M1⊗R N→ M2⊗R N→ M3⊗R N→ 0
Now we focus on the case of abelian groups R = Z. For any abelian group M, let P0 be a free abelian
group such that P0→ M is surjective. Let P1 be its kernel. Then P1 is also free and
0→ P1→ P0→ M→ 0
deﬁnes a free resolution of abelian groups. This implies that
Extk(M, N) = 0, Tor k(M, N) = 0 for k≥ 2.
In the case of abelian groups we will simply denote
Ext(M, N) := Ext1
Z(M.N), Tor (M, N) := TorZ
1 (M, N) .

52 SI LI
Lemma 20.11. If either M is free or N is divisible, then Ext(M, N) = 0.
Proposition 20.12. Let (C•, ∂) be a chain complex of free abelian groups, then
Hn(Hom(C•, G))∼= Hom(Hn(C•), G)⊕ Ext(Hn−1(C•), G)
Proof. Let Bn be n-boundaries and Zn be n-cycles, which are both free. We have exact sequences
0→ Bn→ Zn→ Hn→ 0, 0 → Zn→ Cn→ Bn−1→ 0.
This implies exact sequences
0→ Hom(Hn, G)→ Hom(Zn, G)→ Hom(Bn, G)→ Ext(Hn, G)→ 0
and the split exact sequence
0→ Hom(Bn−1, G)→ Hom(Cn, G)→ Hom(Zn, G)→ 0.
Consider the commutative diagram with exact columns
0 0

Hom(Zn−1, G) //
OO
Hom(Bn−1, G)

Hom(Cn−1, G) //
OO
Hom(Cn, G) //

Hom(Cn+1, G)
Hom(Zn, G) //

Hom(Bn, G)
OO
0 0
OO
This implies a short exact sequence
0→ Ext(Hn−1, G)→ Hn(Hom(C•, G))→ Hom(Hn, G)→ 0
which is also split due to the split of the middle column in the above diagram. □
Theorem 20.13 (Universal Coefﬁcient Theorem for Cohomology) . Let G be an abelian group and X be a topo-
logical space. Then for any n≥ 0, there exists a split exact sequence
0→ Ext(Hn−1(X), G)→ Hn(X; G)→ Hom(Hn(X), G)→ 0
which induces isomorphisms
Hn(X; G)∼= Hom(Hn(X), G)⊕ Ext(Hn−1(X), G).
Proof. Apply the previous Lemma to C• = S•(X). □

INTRODUCTION TO ALGEBRAIC TOPOLOGY 53
Universal Coefﬁcient Theorem for Homology.
Deﬁnition 20.14. Let G be an abelian group. Let A⊂ X be a subspace. We deﬁne the relative singular
chain complex with coefﬁcient in G by
S•(X, A; G) := S•(X, A)⊗Z G
Its cohomology is called the relative singular homology with coefﬁcient in G, denoted by H•(X, A; G).
When A = ∅, we simply get the singular homology H•(X; G).
Similar long exact sequence for relative singular homologies follows from the exact sequence
0→ S•(A; G)→ S•(X; G)→ S•(X, A; G)→ 0.
Theorem 20.15 (Universal Coefﬁcient Theorem for homology). Let G be an abelian group and X be a topological
space. Then for any n≥ 0, there exists a split exact sequence
0→ Hn(X)⊗ G→ Hn(X; G)→ Tor(Hn−1(X), G)→ 0
which induces isomorphisms
Hn(X; G)∼= Hn(X)⊗ G⊕ Tor(Hn−1(X), G).
The proof is similar to the cohomology case.
21. E ILENBERG -Z ILBER THEOREM AND K ¨UNNETH FORMULA
Eilenberg-Zilber Theorem.
Deﬁnition 21.1. Let (C•, ∂C) and (D•, ∂D) be two chain complexes. We deﬁne their tensor product C•⊗ D•
as the chain complex
(C•⊗ D•)k := ∑
p+q=k
Cp⊗ Dq
with the boundary map
∂(cp⊗ dq) := ∂C(cp)⊗ dq + (−1)pcp⊗ ∂D(dq), cp∈ Cp, dq∈ Dq.
Proposition 21.2. Assume C• is chain homotopy equivalent to C′•. Then C•⊗ D• is chain homotopy equivalent to
C′•⊗ D•.
We would like to compare two functors from Top× Top→ Ch•:
S•(X× Y), S•(X)⊗ S•(Y).
We ﬁrst observe that there exists a canonical isomorphism
H0(X× Y)∼= H0(X)⊗ H0(Y).
The following theorem of Eilenberg-Zilber says that such initial condition determines a natural homotopy
equivalent between the above two functors which is unique up to chain homotopy.
Theorem 21.3 (Eilenberg-Zilber). Let X, Y be two topological spaces. Then there exists a chain equivalence
S•(X× Y)
F ..
S•(X)⊗ S•(Y)
G
mm

54 SI LI
which is natural with respect to X , Y and induce the canonical isomorphism H0(X× Y)∼= H0(X)⊗ H0(Y). Such
chain equivalence is unique up to chain homotopy. In particular, there are canonical isomorphisms
Hn(X× Y) = Hn(S•(X)⊗ S•(Y)), ∀n≥ 0.
F, G will be called Eilenberg-Zilber maps.
Proof. Observe that any map ∆p (σx,σy)
→ X× Y factors through
∆p δp
→ ∆p× ∆p σx×σy
→ X× Y
where ∆p δp
→ ∆p× ∆p is the diagonal map. This implies that a natural transformation of the functorS•(−,−)
is determined by its value on{δp}p≥0. For example,
F((σx, σy)) = ( σx⊗ σy)∗F(δp).
Similarly, a natural transformation of the functorS•(−)⊗ S•(−) is determined by its value on 1p⊗ 1q where
1p : ∆p→ ∆p is the identity map. For example, for any σx : ∆p→ X, σy : ∆q→ Y, we have
G(σx⊗ σy) = ( σx× σy)∗G(1p⊗ 1q).
Therefore F and G are completely determined by
fn := F(δn)∈
⨁
p+q=n
Sp(∆n)⊗ Sq(∆n), gn :=
⨁
p+q=n
G(1p⊗ 1q)∈
⨁
p+q=n
Sn(∆p× ∆q).
We will use the same notations as in the discussion of Barycentric decomposition. Then
fn◦ gn≃ δn∈ Sn(∆n× ∆n), gn◦ fn∈
⨁
p+q=n
(S•(∆p)⊗ S•(∆q))n.
Let us denote the following complexes
Cn = ∏
k≥0
(S•(∆k)⊗ S•(∆k))n+k, Dn = ∏
m≥0
(
⨁
p+q=m
Sn+p+q(∆p× ∆q)
)
with boundary map
∂ + ˜∂ : Cn→ Cn−1, ∂ + ˜∂ : Dn→ Dn−1
as follows. ∂ is the usual boundary map of singular chain complexes
∂ : (S•(∆k)⊗ S•(∆k))n→ (S•(∆k)⊗ S•(∆k))n−1, ∂ : Sn(∆p× ∆q)→ Sn−1(∆p× ∆q).
˜∂ is the map induced by composing with the face singular chain ˜∂∈⊕ kSk−1(∆k)
˜∂ : Sp(∆k−1)⊗ Sq(∆k−1)→ Sp(∆k)⊗ Sq(∆k), σp⊗ σq→ ˜∂◦ σp⊗ ˜∂◦ σq
and
˜∂ : Sn(∆p× ∆q)→ Sn(∆p+1× ∆q)⊕ Sn(∆p× ∆q+1), σp× σq→ (˜∂◦ σp)× σq + (−1)n−pσp× (˜∂◦ σq).
Then f = ( fn)∈ C0 and g = ( gn)∈ D0.
F, G are chain maps⇐⇒ f , g are 0-cycles in C•, D•
and natural chain homotopy of F, G are given by 0-boundaries. We claim that
Hn(C•) =



Z n = 0
0 n⁄= 0
, H n(D•) =



Z n = 0
0 n⁄= 0
.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 55
This follows from a spectral sequence computation by ﬁrst computing ∂-homology and then computing
˜∂-homology. For example the ﬁrst page (H•(C•, ∂), ˜∂) is
0→ Z 0→ Z 1→ Z 0→ Z 1→···
whose ˜∂-homology is now Z at degree 0. The case of D is similar. This implies that the initial condition
completely determines chain maps F, G up to chain homotopy.
Let us now analyze the composition F◦ G and G◦ F. We similarly form the chain complexes
C′
n = ∏
k≥0
Sn+k(∆k× ∆k), D′
n := ∏
m≥0
⨁
p+q=m
(S•(∆p)⊗ S•(∆q))n+p+q
with boundary map ∂ + ˜∂ deﬁned similarly. Homology of C′• controls natural chain maps of S•(X× Y) to
itself up to chain homotopy, and similarly for D′•. We still have
Hn(C′
•) =



Z n = 0
0 n⁄= 0
, H n(D′
•) =



Z n = 0
0 n⁄= 0
.
It follows that F◦ G and G◦ F are both naturally chain homotopic to the identity map. The theorem follows.
□
An explicit construction of G can be described as follows: given σp : ∆p→ X, σq : ∆q→ Y,
G(σp⊗ σq) : ∆p× ∆q→ X× Y
where we have to chop ∆p× ∆q into p + q-simplexes. This is the shufﬂe product.
An explicit construction of F can be given by Alexander-Whitney map described as follows.
Deﬁnition 21.4. Given a singular n-simplex σ : ∆n→ X and 0≤ p, q≤ n, we deﬁne
• the front p-face of σ to be the singular p-simplex
pσ : ∆p→ X, pσ(t0,··· , tp) := σ(t0,··· , tp, 0,··· , 0)
• the back q-face of σ to be the singular q-simplex
σq : ∆q→ X, σq(t0,··· , tq) := σ(0,··· , 0,t0,··· , tq).
Deﬁnition 21.5. Let X, Y be topological spaces. Let πX : X× Y→ X, πY : X× Y→ Y be the projections.
We deﬁne the Alexander-Whitney map
AW : S•(X× Y)→ S•(X)⊗ S•(Y)
by the natural transformation given by the formula
AW(σ) := ∑
p+q=n
p(πX◦ σ)⊗ (πY◦ σ)q .
Theorem 21.6. The Alexander-Whitney map is a chain homotopy equivalence.
Proof. It is easy to see that AW is a natural chain map which induces the canonical isomorphism
H0(X× Y)→ H0(X)⊗ H0(Y).
Therefore AW is a chain homotopy equivalence by Eilenberg-Zilber Theorem. □

56 SI LI
K¨ unneth formula.
Theorem 21.7 (Algebraic K ¨unneth formula). Let C• and D• be chain complex of free abelian groups. Then there
is a split exact sequence
0→ (H•(C)⊗ H•(D))n→ Hn(C•⊗ D•)→ Tor(H•(C), H•(D))n−1→ 0.
Here Tor(H•(C), H•(D))k = ⨁
p+q=k
Tor(Hp(C), Hq(D)).
Proof. Using the freeness of C• we can show that
H•(C•⊗ D•) = H•(C•⊗ H•(D)).
Applying Universal Coefﬁcient Theorem for Homology, we ﬁnd
0→ Hp(C)⊗ Hq(D)→ Hp+q(C•−q⊗ Hq(D))→ Tor(Hp−1(C), Hq(D))→ 0.
Summing over p, q gives the theorem. □
Theorem 21.8 (K ¨unneth formula). For any topological spaces X, Y and n≥ 0, there is a split exact sequence
0→
⨁
p+q=n
Hp(X)⊗ Hq(X)→ Hn(X× Y)→
⨁
p+q=n−1
Tor(Hp(X), Hq(Y))→ 0 .
Proof. This follows from Eilenberg-Zilber Theorem and algebraic K¨unneth formula.
□
22. C UP AND CAP PRODUCT
Let R be a commutative ring with unit. We have natural cochain maps
S•(X; R)⊗R S•(Y; R)→ Hom(S•(X)⊗ S•(Y), R)→ S•(X× Y; R)
where the ﬁrst map maps ϕp∈ Sp(X; R), ηq∈ Sq(X; R) to ϕp⊗ ηq where
ϕp⊗ ηq : σp⊗ σq→ ϕp(σp)· ηq(σq), σp∈ Sp(X), σq∈ Sq(X).
Here· is the product in R. This leads to a cochain map
S•(X; R)⊗R S•(Y; R)→ S•(X× Y; R)
which further induces
H•(X; R)⊗R H•(Y; R)→ H•(X× Y; R)
Cup product.
Deﬁnition 22.1. Let R be a commutative ring with unit. We deﬁne the cup product on cohomology groups
∪ : Hp(X; R)⊗R Hq(X; R)→ Hp+q(X; R)
by the composition
H•(X; R)⊗R H•(X; R)
∪
))
// H•(X× X; R)
∆∗

H•(X; R)
Here ∆ : X→ X× X is the diagonal map.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 57
Alexander-Whitney map gives a speciﬁc product formula
(α∪ β)(σ) = α(pσ)· β(σq) , α∈ Sp(X; R), β∈ Sq(X; R), σ : ∆p+q→ X.
Theorem 22.2. H•(X; R) is a graded commutative ring with uint:
(1) Unit: let 1∈ H0(X; R) be represented by the cocyle which takes every singular 0-simplex to 1∈ R. Then
1∪ α = α∪ 1 = α, ∀α∈ H•(X; R).
(2) Associativity:
(α∪ β)∪ γ = α∪ (β∪ γ).
(3) Graded commutativity:
α∪ β = (−1)pq β∪ α, ∀α∈ Hp(X; R), β∈ Hq(X; R).
Proof. Unit of 1 is checked easily. Observe that the following two compositions of Eilenberg-Zilber maps
are chain homotopic (similar to Eilenberg-Zilber Theorem)
S•(X× Y× Z)→ S•(X× Y)⊗ S•(Z)→ S•(X)⊗ S•(Y)⊗ S•(Z)
S•(X× Y× Z)→ S•(X)⊗ S•(Y× Z)→ S•(X)⊗ S•(Y)⊗ S•(Z).
Associativity follows from the commutative diagram (R is hidden for simplicity)
H•(X)⊗ H•(X)⊗ H•(X) //

H•(X× X)⊗ H•(X)

(∆×1)∗
// H•(X)⊗ H•(X)

H•(X)⊗ H•(X× X) //
(1×∆)∗

H•(X× X× X)
(∆×1)∗
//
(1×∆)∗

H•(X× X)
∆∗

H•(X)⊗ H•(X) // H•(X× X)
∆∗
// H•(X)
Graded commutativity follows from the fact that the interchange map of tensor product of chain complexes
T : C•⊗ D•→ D•⊗ C•
cp⊗ dq→ (−1)pqdq⊗ cp
is a chain isomorphism. Therefore the two chain maps
S•(X× Y)→ S•(Y× X)→ S•(Y)⊗ S•(X)
S•(X× Y)→ S•(X)× S•(Y) T→ S•(Y)⊗ S•(X)
are chain homotopic, again by the uniqueness in Eilenberg-Zilber Theorem.
Set Y = X we ﬁnd the following commutative diagram
H•(X)⊗ H•(X) //
T

H•(X× X)
=

H•(X)⊗ H•(X) // H•(X× X).
which gives graded commutativity.
Alternately, all the above can be checked explicitly using Alexander-Whitney map □

58 SI LI
Theorem 22.3. Let f : X→ Y be a continuous map. Then
f∗ : H•(Y; R)→ H•(X; R)
is a morphism of graded commutative rings, i.e. f ∗(α∪ β) = f∗α∪ f∗β. In other words, H•(−) deﬁnes a functor
from the category of topological spaces to the category of graded commutative rings.
Proof. The theorem follows from the commutative diagram
X
f //
∆

Y
∆

X× X
f× f // Y× Y.
□
Theorem 22.4 (K ¨unneth formula). Assumem R is a PID, andHi(X; R) are ﬁnitely generated R-module, then there
exists a split exact sequence of R-modules
0→
⨁
p+q=n
Hp(X; R)⊗ Hq(Y; R)→ Hn(X× Y; R)→
⨁
p+q=n+1
TorR
1 (Hp(X; R), Hq(Y; R)).
In particular, if H•(X; R) or H•(Y; R) are free R-modules, we have an isomorphism of graded commutative rings
H•(X× Y; R)∼= H•(X; R)⊗R H•(Y; R).
Example 22.5. H•(Sn) = Z[η]/η2 where η∈ Hn(Sn) is a generator.
Example 22.6. Let Tn = S1×···× S1 be the n-torus. Then
H•(Tn)∼= Z[η1,··· , ηn], ηiη=− ηjηi
is the exterior algebra with n generators. Each ηi corresponds a generator of H1(S1).
Proposition 22.7. H•(CPn) = Z[x]/xn+1, where x∈ H2(CPn) is a generator.
Proof. We prove by induction n. We know that
Hk(CPn) =



Z k = 2m≤ 2n
0 otherwise
Let x be a generator of H2(CPn). We only need to show that xk is a generator of H2k(CPn) for each k≤ n.
Using cellular chain complex, we know that for k < n
H2k(CPn)→ H2k(CPk)
is an isomorphism. By induction, this implies that xk is a generator of H2k(CPn) for k < n. Poincare duality
theorem (which will be proved in the next section) implies that
H2(CPn)⊗ H2n−2(CPn) ∪→ H2n(CPn)
is an isomorphism. This says that xn is a generator of H2n(CPn). This proves the proposition.
□

INTRODUCTION TO ALGEBRAIC TOPOLOGY 59
Cap product.
Deﬁnition 22.8. We deﬁne the evaluation map
⟨−,−⟩ : S•(X; R)×R S•(X; R)→ R
as follows: for α∈ Sp(X; R), σ∈ Sp(X), r∈ R,
⟨α, σ⊗ r⟩ := α(σ)· r.
The evaluation map is compatible with boundary map and induces an evaluation map
⟨−,−⟩ : Hp(X; R)⊗R Hp(X; R)→ R.
This generalized to
S•(X; R)⊗R S•(X× Y; R)→ S•(X; R)⊗R S•(X; R)⊗R S•(Y; R)
⟨−,−⟩⊗1
→ S•(Y; R)
which induces
Hp(X; R)⊗R Hp+q(X× Y; R)→ Hq(Y; R).
Deﬁnition 22.9. We deﬁne the cap product
∩ : Hp(X; R)⊗ Hp+q(X; R)→ Hq(X; R)
by the composition
Hp(X; R)⊗ Hp+q(X; R)
1⊗∆//
∩
**
Hp(X; R)⊗ Hp+q(X× X; R)

Hq(X; R)
Theorem 22.10. The cap product gives H•(X; R) a structure of H•(X; R)-module.
Theorem 22.11. The cap product extends naturally to the relative case: for any pair A⊂ X
∩ : Hp(X, A)⊗ Hp+q(X, A)→ Hq(X)
∩ : Hp(X)⊗ Hp+q(X, A)→ Hq(X, A)
Proof. Since S•(X, A)⊂ S•(X), we have
∩ : S•(X, A)× S•(X)→ S•(X).
We model the cap product on chains via the Alexander-Whitney map. Then
∩ : S•(X, A)× S•(A)→ 0.
Therefore∩ factors through
∩ : S•(X, A)× S•(X)
S•(A)→ S•(X).
Passing to homology (cohomology) we ﬁnd the ﬁrst cap product. The second one is proved similarly using
∩ : S•(X)× S•(X)
S•(A)→ S•(X)
S•(A) .
□

60 SI LI
23. P OINCAR ´E DUALITY
Deﬁnition 23.1. A topological manifold of dimension n , or a topological n-manifold, is a Hausdorff space
in which each point has an open neighborhood homeomorphic to Rn.
In this section, a manifold always means a topological manifold. For any point x∈ X, there exists an
open neighborhood U and a homeomorphism φ : U→ Rn. (U, φ) is called a chart around x.
Orientation.
Deﬁnition 23.2. Let X be a n-manifold. x∈ X be a point. A generator of
Hn(X, X− x)∼= Hn(Rn, Rn− 0)∼= Z
is called a local orientation of X at x.
For any x∈ X, there are two choices of local orientation at x. We obtain a two-sheet cover
π : ˜X→ X, where ˜X ={(x, µx)|µx is a local orientation of X at x}
Here π is the natural projection (x, µx)→ x. ˜X is topologized as follows. Let U be a small open ball in X.
Then for any x∈ U, we have an isomorphism
Hn(X, X− U)∼= Hn(X, X− x)
which induces a set theoretical identiﬁcation
π−1(U)∼= U× Z2.
Then we give a topology on ˜X by requiring all such identiﬁcations being homeomorphisms. In particular,
π : ˜X→ X is a Z2-covering map.
Deﬁnition 23.3. A (global) orientation of X is a section of π : ˜X→ X, i.e., a continuous map s : X→ ˜X
such that π◦ s = 1X. If an orientation exists, we say X is orientable.
Theorem 23.4. Let X be a connected manifold. Then X is orientable if and only if ˜X has two connected components.
In particular, a connected orientable manifold has precisely two orientations.
Example 23.5. A simply connected manifold is orientable.
Example 23.6. Let X be connected non-orientable manifold. Then ˜X is connected orientable.
Lemma 23.7. Let U⊂ Rn be open. Then the natural map
Hn(Rn, U)→ ∏
x∈Rn−U
Hn(Rn, Rn− x)
is injective.
Proof. This is equivalent to the injectivity of
˜Hn−1(U)→ ∏
x∈Rn−U
Hn−1(Rn− x).
Let α be a singular (n− 1)-chain representing a class[α]U in ˜Hn−1(U). We can choose a big ballB containing
U and ﬁnite small cubes D1,··· , DN such that Di is not a subset of U but
Supp(α)⊂ B− D1∪···∪ DN⊂ U.

INTRODUCTION TO ALGEBRAIC TOPOLOGY 61
Then α represents a class in ˜Hn−1(D1∪···∪ DN)∼= Hn(B, B− D1∪···∪ DN) which maps to zero in each
Hn(B, B− Di)∼= Hn(B, B− xi) where xi∈ Di− U. It follows via Mayer-Vietoris argument thatα is the zero
class in ˜Hn−1(D1∪···∪ DN), hence zero in ˜Hn−1(U). □
Fundamental class.
Theorem 23.8. Let X be a connected n-manifold. For any abelian group G, we have the following vanishing statement



Hi(X; G) = 0 i > n
Hn(X; G) = 0 if X is noncompact.
Proof. We prove the case for G = Z. General G is similar. We assume X is connected.
Step 1: X = U⊂ Rn is an open subset.
Let α∈ Si(U) represent an element of [α]∈ Hi(U). Let K⊂ U be a compact subset such that Supp(α)∈
K. Equip Rn with a CW structure in terms of small enough cubes such that
K⊂ L⊂ U
where L is a ﬁnite CW subcomplex. We have a commutative diagram
Hi+1(Rn, L) //

Hi+1(Rn, U)

Hi(L) // Hi(U)
By construction, [α]∈ Hi(U) lies in the image of Hi(L). But Hi+1(Rn, L)∼= Hcell
i+1(Rn, L) = 0 for i≥ n.
Step 2: X = U∪ V where U open is homeomorphic to Rn and V open satisﬁes the vanishing condition.
Consider the Mayer-Vietoris sequence
˜Hi(U)⊕ ˜Hi(V)→ ˜Hi(U∪ V)→ ˜Hi−1(U∩ V)→ ˜Hi−1(U)⊕ ˜Hi−1(V)
For i > n, we ﬁnd H i(U∪ V) = 0 by Step 1. Assume that X = U∪ V is not compact. We need to prove
˜Hn−1(U∩ V)→ ˜Hn−1(V)
is injective. The noncompactness and connectedness of X implies that
Hn(U∪ V)→ Hn(U∪ V, U∪ V− x)
is zero map for any x∈ X. Consider the commutative diagram, where x∈ U− U∩ V
Hn(U∪ V)
))
Hn(U∪ V, U∪ V− x)
∼=

Hn(U∪ V, U∩ V) //
((
Hn(V, U∩ V)

oo
Hn(U, U− x) Hn(U, U∩ V) //
OO
oo ˜Hn−1(U∩ V)

// 0
˜Hn−1(V)

62 SI LI
Let α∈ Hn(U, U∩ V) maps to ker ( ˜Hn−1(U∩ V)→ ˜Hn−1(V)). Diagram chasing implies that α maps to
Hn(U, U− x) for any x∈ U− U∩ V. Since x is arbitrary, this implies α = 0 by the previous lemma.
Step 3: General case. Let α∈S i(X) representing a class in H i(X). We can choose ﬁnite coordinate charts
U1,··· , UN such that Supp(α)⊂ U1∪···∪ UN. Then the class of α lies in the image of the map
Hi(U1∪···∪ UN)→ Hi(X).
We only need to prove the theorem forU1∪···∪ UN. This follows from Step 2 and induction on N. □
Deﬁnition 23.9. Let X be an n-manifold. A fundamental class of X at a subspace A⊂ X is an element
s∈ Hn(X, X− A) whose image
Hn(X, X− A)→ Hn(X, X− x)
deﬁnes a local orientation for each x∈ A. When A = X, s∈ Hn(X) is called a fundamental clas of X.
Theorem 23.10. Let X be an oriented n-manifold, K⊂ X be compact subspace. Then
(1) H i(X, X− K) = 0 for any i > n.
(2) The orientation of X deﬁnes a unique fundamental class of X at K.
In particular, if X is compact, then there exists a unique fundamental class of X associated to the orientation.
Proof.
Step 1: K is a compact subset inside a cooridinate chart U∼= Rn. Then
Hi(X, X− K)∼= Hi(U, U− K)∼= ˜Hi−1(U− K) = 0 i > n.
Take a big enough ball B such that K⊂ B⊂ U. The orientation of X at the local chart U determines an
element of Hn(X, X− U) which maps to the required fundamental class of X at K.
Step 2: K = K1∪ K2 where K1, K2, K1∩ K2 satisfy (1)(2). Using Mayer-Vietoris sequence
··· Hi+1(X, X− K1∩ K2)→ Hi(X, X− K1∪ K2)→ Hi(X, X− K1)⊕ Hi(X, X− K2)→ Hi(X, X− K1∩ K2)→···
we see K satisﬁes (1). The unique fundamental classes at K1 and K2 map to the unique fundamental class
at K1∩ K2, giving rise to a unique fundamental class at K1∪ K2 by the exact sequence
0→ Hn(X, X− K1∪ K2)→ Hn(X, X− K1)⊕ Hn(X, X− K2)→ Hn(X, X− K1∩ K2)
Step 3: For arbitrary K, it is covered by a ﬁnite number of coordinates charts {Ui}1≤i≤N. Let Ki = K∩ Ui.
Then K = K1∪···∪ KN. The theorem holds for K by induction on N and Step 1, 2. □
Poincar´ e duality.
Deﬁnition 23.11. LetK denote the set of compact subspaces of X. We deﬁne compactly supported coho-
mology of X by
Hk
c(X) := colim
K∈K
Hk(X, X− K)
where the colimit is taken with respect to the homomorphisms
Hk(X, X− K1)→ Hk(X, X− K2)
for K1⊂ K2 compact. In particular, if X is compact, then Hk
c(X) = Hk(X).
The functorial structure is with respect to the proper maps: let f : X→ Y be proper, then
f∗ : Hk
c(Y)→ Hk
c(X).

INTRODUCTION TO ALGEBRAIC TOPOLOGY 63
Example 23.12. Let X = Rn. Consider the sequence of compact subspaces B1⊂ B2⊂ B3⊂··· , where Bk
is the closed ball of radius k. Any compact subspace is contained in some ball. Therefore
Hi
c(Rn) = colim
k
Hi(Rn, Rn− Bk) = ˜Hi(Sn−1) =



Z i = n
0 i⁄= n
.
Theorem 23.13. Let X = U∪ V where U, V open. Then we have the Mayer-Vietoris exact sequence
···→ Hk
c(U∩ V)→ Hk
c(U)⊕ Hk
c(V)→ Hk
c(X)→ Hk+1
c (U∩ V)→···
Let X be an oriented n-manifold. For each compact K, let ξK∈ Hn(X, X− K) be the fundamental class
determined by the orientation. Taking the cap product we ﬁnd
DK : Hp(X, X− K)
∩ξK
→ Hn−p(X).
This passes to the colimit and induces a map
D : Hp
c (X)→ Hn−p(X).
Theorem 23.14 (Poincar´e Duality). Let X be an oriented n-manifold. Then for any p,
D : Hp
c (X)→ Hn−p(X)
is an isomorphism. In particular, if X is compact then Hp(X)∼= Hn−p(X).
Proof. We prove the theorem for all open subsetU of X.
Step 1: If the theorem holds for open U, V and U∩ V, then the theorem holds for U∪ V.
This follows from Mayer-Vietoris sequence and the commutative diagram
// Hk
c(U∩ V) //
D

Hk
c(U)⊕ Hk
c(V) //
D⊕D

Hk
c(U∪ V) //
D

Hk+1
c (U∩ V) //
D

···
// Hn−k(U∩ V) // Hn−k(U)⊕ Hn−k(V) // Hn−k(U∪ V) // Hn−k−1(U∩ V) //···
Step 2: Let U1⊂ U2⊂··· and U =∪iUi. Assume the theorem holds for Ui, then it holds for U.
This follows from the isomorphism
Hk
c(U) = colim
i
Hk
c(Ui), H n−k(U) = colim
i
Hn−k(Ui).
Step 3: The theorem holds for an open U contained in a coordinate chart.
This follows by expressing U as a countable union of convex subsets of Rn.
Step 4: For any open U.
By Step 2, 3 and Zorn’s lemma, there is a maximal open subsetU of X for which the theorem is true. By
Step 1, U must be the same as X. □
24. I NTERSECTION AND LEFSCHETZ FIXED POINT THEOREM
In this section X will be an oriented connected closed n-dim manifold. [X] its fundamental class.

64 SI LI
Intersection form. Poincar´e duality gives an isomorphism
Hi(X)
∩[X]
∼= Hn−i(X).
The cup product on cohomology has a geometric meaning under Poincar ´e duality as follows. Let Y, Z be
two oriented closed submanifold of X. Assume dim (Y) = i, dim(Z) = j, and Y intersects Z transversely
so that their intersection Y∩ Z is manifold of dimension i + j− n. Y∩ Z has an induced orientation. Let
[Y]∗∈ Hn−i(X) be the Poincar´e dual of the fundamental class [Y]∈ Hi(X). Then
[Y]∗∪ [Z]∗ = [Y∩ Z]∗ .
Therefore the cup product is interpreted as intersection under Poincar´e duality.
An important case is whenY and Z have complementary dimension, i.e. i + j = n so that Y∩ Z is a ﬁnite
set of points, whose signed sum gives the intersection number of Y and Z.
Deﬁnition 24.1. We deﬁne the intersection pairing
⟨−,−⟩ : Hi(X)× Hn−i(X)→ H0(X)∼= Z.
Equivalently, we have the pairing on cohomology
⟨−,−⟩ : Hi(X)× Hn−i(X)→ Hn(X)
[X]
∼= Z.
The intersection pairing is non-degenerate when torsion elements are factored out. In particular
Hi(X; Q)× Hn−i(X; Q)→ Q
is a non-degenerate pairing.
Example 24.2. T2 = S1× S1. Y1 = S1×{ 1}, Y2 ={1}× S1. Y1∩ Y2 is a point. This is dual to the ring
structure H•(T2) = Z[η1, η2], where ηi is dual to Yi.
Example 24.3. Let f : Σg→ Σh.
Lefschetz Fixed Point Theorem. Let us consider the diagonal ∆⊂ X× X. Let {ei} be a basis of H•(X; R),
consisting of elements of pure degree. Let ei be its dual basis of H•(X; Q) such that
⟨
ej, ei
⟩
= δj
i .
First we observe that
[∆]∈ Hn(X× X; Q)∼=⊕p Hp(X; Q)⊗ Hn−p(X; Q)
is given by
[∆] = ∑
i
ei⊗ ei.
This can be checked by intersecting with a basis of H•(X× X; Q).
Let f : X→ X be a smooth map. Let
Γ f :={(x, f (x))|x∈ X}⊂ X× X
be the graph of f . Let α∈ Hp(X), β∈ Hn−p(X). From the geometry of graph, we ﬁnd
[Γ f ]· α× β = (−1)p f∗α· β.
Applying this to [∆], we ﬁnd
[Γ f ]· [∆] = ∑
i
(−1)|ei| f∗ei· ei = ∑
p
(−1)p Tr( f∗ : Hp(X; Q)→ Hp(X; Q)).

INTRODUCTION TO ALGEBRAIC TOPOLOGY 65
Deﬁnition 24.4. We deﬁne the Lefschetz number of f by
L( f ) := ∑
p
(−1)p Tr( f∗ : Hp(X; Q)→ Hp(X; Q)) .
When Γ f and ∆ intersects transversely,
♯Fix( f ) = [ Γ f ]· [∆]
gives a signed count of ﬁxed points of the map f . This gives the Lefschetz Fixed Point Theorem
♯Fix( f ) = L( f ) .
In particular, if the right hand side is not zero, there must exist a ﬁxed point of f .
Example 24.5. Let n be even. Then any map f : CPn→ CPn has a ﬁxed point. In fact,
f∗ : H•(CPn; Q)→ H•(CPn; Q)
is a ring map. Let x∈ H2(CPn) be a generator, let f∗(x) = kx for some k∈ Z. Then
∑
p
(−1)p Tr( f∗|Hp(CPn;Q)) =
n
∑
i=0
kn
is an odd number, hence not zero. By Lefschetz Fixed Point Theorem, f must have a ﬁxed point.
Example 24.6. The Lefschetz number of the identity map id : X→ X is precisely the Euler characteristic
L(id) = χ(X).
Consider the sphere S2, and the map
f : S2→ S2, x→ x + v
|x + v| , v = (0, 0, 1/2).
f has two ﬁxed points: north and south pole, and f is homotopy to the identify. We ﬁnd
χ(S2) = L(id) = L( f ) = 2.
For another example, consider a compact connected Lie group G. Let g∈ G which is not identity but close
to identity. Then multiplication by g has no ﬁxed point, and it is hompotopic to the identity map. We ﬁnd
χ(G) = 0.
25. S PECTRAL SEQUENCE
Spectral sequences usually arise in two situations
(1) A Z-ﬁltration of a chain complex: a sequence of subcomplexes···⊂ Fp⊂ Fp+1⊂··· .
(2) A Z-ﬁltration of a topological space: a family of subspaces···⊂ Xp⊂ Xp+1⊂··· .
Deﬁnition 25.1. A ﬁltered R-module is an R-module A with an increasing sequence of submodules
···⊂ FpA⊂ Fp+1A⊂···
indexed by p∈ Z. We always assume that it is exhaustive and Hausdorff
⋃
p
FpA = A (exhaustive),
⋂
p
FpA = 0 (Hausdorff).

66 SI LI
The ﬁltration is bounded if FpA = 0 for p sufﬁciently small and FpA for p sufﬁciently large. The associated
graded module GF
• A is deﬁned by
GF
• (A) :=
⨁
p∈Z
GF
p A, GF
p A := FpA/Fp−1A.
A ﬁltered chain complex is a chain complex (C•, ∂) together with a ﬁltration FpCi of each Ci such that the
differential preserves the ﬁltration
∂(FpCi)⊂ FpCi−1.
In other words, we have an increasing sequence of subcomplexes FpC• of C•.
A ﬁltered chain complex induces a ﬁltration on its homology
Fp Hi(C•) = Im(Hi(FpC•)→ Hi(C•)).
In other words, an element[α]∈ Hi(C•) lies in Fp Hi(C•) if and only if there exists a representativex∈ FPCi
such that [α] = [ x]. Its graded piece is given by
GF
p Hi(C•) = Ker(∂ : FpCi→ FpCi−1)
Fp−1Ci + ∂Ci+1
.
Notation 25.2. In this section, our notation of quotient means the quotient of the numerator by its intersec-
tion with the denominator, i.e., A
B := A
A∩B .
Given a ﬁltered R-module A, we deﬁne its Rees module as a submodule of A[z, z−1] deﬁned by
AF :=
⨁
p∈Z
FpA zp⊂ A[z, z−1].
Our conditions for the ﬁltration can be interpreted as follows
(1) increasing ﬁtration: AF is a R[z]-submodule of A[z, z−1] and z : AF→ AF is injective.
(2) exhaustive: AF[z−1] := AF⊗R[z] R[z, z−1] equals A[z, z−1].
(3) Hausdorff: ⋂
p≥0
z−pAF = 0 in A[z, z−1].
We have
GF
• (A) := AF/zA F.
26. O BSTRUCTION THEORY
27. T HE THEOREM OF HUREWICZ
Deﬁnition 27.1. We deﬁne the Hurewicz map ρ : πn(X, A)→ Hn(X, A) by
ρ([ f ]) := f∗(η)
where f : (Dn, Sn−1)→ (X, A) represents an element of πn(X, A) and η is a generator of Hn(Dn, Sn−1).
The following diagram commutes
··· // πn(A) //

πn(X) //

πn(X, A) //

πn−1(A) //

···
··· // Hn(A) // Hn(X) // Hn(X, A) // Hn−1(A) //···

INTRODUCTION TO ALGEBRAIC TOPOLOGY 67
Theorem 27.2 (Hurewicz).
(1) If a space X is (n− 1)−connected, n≥ 2, then Hi(X) = 0 for i < n and πn(X)∼= Hn(X).
(2) If a pair (X, A) is (n− 1)−connected, n≥ 2, with A simply- connected and nonempty, then Hi(X, A) = 0
for i < n and πn(X, A)∼= Hn(X, A).
28. E ILENBERG -S TEENROD AXIOMS
In this section we discuss Eilenberg-Steenrod’s axiomatic approach to homology theory.
Eilenberg-Steenrod Axioms.
Deﬁnition 28.1. A homology theory consists of a sequence of functors Hn (n∈ Z) from the category of pairs
(X, A) of topological spaces to the category of abelian groups, together with a natural transformation
∂ : Hi(X, A)→ Hi−1(A) ( := Hi−1(A, ∅))
called the connecting map. They satisfy the following properties
(1) Exactness. For any pair (X, A) with inclusions i : A⊂ X, j : (X, ∅)⊂ (X, A), there is an exact
sequence
···→ Hq(A)
Hq(i)
→ Hq(X)
Hq(j)
→ Hq(X, A) ∂→ Hq−1(A)→
(2) Homotopy. If f0, f1 : (X, A)→ (Y, B) are homotopic, then
H( f0) = H( f1) : H•(X, A)→ H•(Y, B).
(3) Excision. For any pair (X, A), if U is a subset of X such that the closure of U is contained in the
interior of A, then the inclusion j : (X− U, A− U)⊂ (X, A) induces isomorphisms
H(j) : H•(X− U, A− U)∼= H•(X, A).
(4) Dimension. If ⋆ is a point, then Hi(⋆) = 0 for any i⁄= 0.
We also add two additional axioms
(5) Additivity. If X = ∐α Xα is a disjoint union, then
H•(X) =
⨁
α
H•(Xα).
(6) Weak equivalence. If f : (X, A)→ (Y, B) is a weak equivalence, then H•( f ) are isomorphism.
For a homology theory, H0(⋆) = G is called the coefﬁcient group of the theory.
Remark 28.2. The weak equivalence axiom ensures that a homology theory is uniquely determined by the
subcategory of CW complexes.
Deﬁnition 28.3. Let H, H′ be two homology theories. A natural transformation Φ : H→ H′ is a sequence
of natural transformations Φi : Hi→ H′
i such that the following diagram commutes for any pair (X, A)
Hi(X, A)
∂ //
Φi

Hi−1(A)
Φi−1

H′(X, A)
∂′
// H′
i−1(A)
If Φi is a natural isomorphism for each i, then we say H, H′ are naturally isomorphic.
Example 28.4. Singularity homology H(X, A; G) is a homology theory with coefﬁcient G.

68 SI LI
Given a homology theory, we can similarly deﬁne its reduced homology by
˜Hi(X, A) =



ker(H0(X)→ H0(⋆)) i = 0, A = ∅
Hi(X, A) otherwise
The reduced homology sequence is also exact.
Proposition 28.5. Let H be a homology theory with coefﬁcient G, Then
˜Hi(Sn) =



G i = n
0 i⁄= n
Hurewicz Theorem gives a natural isomorphism
Hn(X; Z)→ Hn(X)
from the singular homology to our given homology theory, for (n− 1)-connected space X. This is the key
to prove the following uniqueness theorem.
Theorem 28.6. Any homology theory is naturally isomorphic to the singular homology.
Proof. We only need to prove for CW complex. We can use the axioms to construct the cellular chain
complex Cn(X) = Hn(X(n)/X(n−1)) for any homology theory, and show by the same method that the
homology of
···→ Cn(X) d→ Cn−1(X)→···
is isomorphic to H•(X) of our given homolog theory. Hurewicz Theorem will imply that this chain complex
is isomorphic to the cellular chain complex associated to the singular homology. This proves the theorem.
□
Generalized homology theory.
Deﬁnition 28.7. A (co)-homology functor H that satisﬁes Eilenberg-Steenrod Axioms except the Dimension
axiom is called a generalized (co)-homology theory
Example 28.8 (K-theory).
Example 28.9 (Bordism).

