Chapter 2
2.1
1.1 Show that A has the right universal property. Let G be any sheaf and let F be the presheaf U↦→ A,
and suppose ϕ : F→ G. Let f∈ A(U ), i.e. f : U→ A is a continuous map. Write U = ∐Vα with Vα
the connected components of U so f (Vα) = aα∈A. Then we get bα =ϕVα (aα) since F(U ) = A for any U ,
and since G is a sheaf we obtain b∈ G(U ). We deﬁne ψ : A→ G by ψU (f ) = b. This map has the right
properties.
1.2 a) Observe (ker ϕ)P = lim−→U ∋P (kerϕ)(U ) = lim−→U ∋P kerϕU is a subgroup of FP , as is ker ϕP , so we show
equality inside FP . For x∈ (kerϕ)P pick (U,y ) representing x, with y∈ kerϕU . Then the image of y in FP ,
i.e. x, is mapped to zero by ϕP . Conversely, if x∈ kerϕP there exist ( U,y ) with y∈ F(U ) and ϕU (y) = 0 so
x∈ (kerϕ)P . For im ϕ one proceeds similarly, noting only that (im ϕ)P = lim−→U ∋P imϕU since the presheaf
“imϕ” and the sheaf im ϕ have the same stalks at every point.
b) The morphism ϕ is inj. resp surj. iﬀ (ker ϕ)P = 0 resp. (im ϕ)P = GP for all P . By part a), this holds iﬀ
kerϕP = 0 resp. im ϕP = GP for all P , that is, iﬀ ϕP is inj. resp. surj.
c) We have im ϕi−1 = ker ϕi iﬀ im ϕi−1
P = (im ϕi−1)P = (ker ϕi)P = ker ϕi
P .
1.3 a) By 1.2, ϕ is surjective iﬀ ϕP is surj. for all P , that is, iﬀ for all U and all s∈ G(U ) there exist
(Ui,ti)∈ FP with ti∈ F(Ui) such that ϕUi(ti)
⏐⏐
P =sP , or shrinking Ui if need be, iﬀ for all P∈U we have
ϕUi(ti) = s
⏐⏐
Ui
with each Ui a nbd of P . The Ui coverU .
b) Let F∞ be the sheaf of holomorphic fns on CP1 vanishing at ∞ and F0 the sheaf of holo. fns. vanishing
at 0. Let G be the sheaf of holo. fns. and ϕ : F∞⊕ F0→ G be given over an open U by (f1,f 2)↦→f1 +f2.
This is a surjective map of sheaves since it is obviously surjective on every neighborhood not containing both
∞, 0. However, the map on global sections is not surjective: any holo. function on CP1 is constant, so the
global sections of F∞ and F0 are just {0}, while the global sections of G are C.
1.4 a) If ϕU is injective for all U thenϕP : FP→ GP is injective for all P , and since F+
P = FP , G+
P = GP and
ϕ+
P =ϕP , we see that ϕ+ is injective by 1.2.
b) Since im ϕ(U )↪→ G(U ) for all U is injective (the map being just inclusion) we see that the induced map
imϕ→ G+ = G is injective by the above, so im ϕ is a subsheaf of G.
1.5 Reduce to the corresponding statement for abelian groups by Prop 1.1: ϕ is an isom. iﬀ ϕP is an isom.
for all P , iﬀ ϕP is inj. and surj. for all P , iﬀ ϕ is inj. and surj. by 1.2 b).
1.6 a) The natural map is F(U )→ F(U )/F′(U )→ (F/F′)(U ), and we may check surjectivity on stalks by
1.2. But FP → FP/F′
P is clearly surjective for all P . The sequences 0 → F′
P → FP/F′
P → 0→ induced
by 0 → F′(U )→ F(U )/F′(U )→ 0 are all exact, so the corresponding sequence of sheaves is exact, that is,
ker(F→ F/F′) = F′.
1

b) By 1.4 it suﬃces to show that ϕ : F′→ imϕ is surjective. Checking on stalks and using 1.2 reduces this
to the surjectivity of F′
P→ imϕP , which is a tautology. By abuse, we now consider F′ as a subsheaf of F.
We claim that the map F(U )→ F′′(U ) kills F′(U ) for each U . Indeed, any s∈ F′(U ) has image that is zero
in every stalk, and hence must be zero by the sheaf axioms. Thus we obtain a map F(U )/F′(U )→F ′′(U )
induced by F→ F′′, which gives a morphism F/F′→ F′′ that is an isomorphism on stalks by 1.2 and the
given exact sequence.
1.7 a) There is a natural map F→ imϕ induced by F(U )
ϕU
−−→imϕU→ (imϕ)(U ), and on stalks we have the
exact sequences 0 → kerϕP→ FP→ imϕP→ 0 where we have used 1.2 again. Thus by 1.2, the sequence
0→ kerϕ→ F→ imϕ→ 0 is exact, so 1.6 b) yields the result.
b) Similarly, the map G(U )→ G(U )/ imϕ(U )→ (cokerϕ)(U ) gives a map G→ cokerϕ, and identifying im ϕ
as a subsheaf of G by 1.4 b), we see that 0 → imϕ→ G→ cokerϕ→ 0 is exact on stalks, so is exact by 1.2.
Now use 1.6 b) again.
1.8 It suﬃces to show exactness at Γ( U, F) as injectivity holds since F′(U )→ F(U ) is injecitve for all U iﬀ
F′→ F is injective. Let φ : F→ F′′ and ψ : F′→ F. Then for s∈ F′(U ) we have
(φU◦ψU (s))P = lim−→U ⊇V ∋P
(φU◦ψU (s))
⏐⏐
V = lim−→U ⊇V ∋P
(φV◦ψV (s
⏐⏐
V )) = φP◦ψP (sP ) = 0 ,
so since F′′ is a sheaf we have φU◦ψU = 0. Conversely, suppose s∈ F(U ) has φU (s) = 0. Since the sequence
of stalks at P is exact, for each P ∈ U we have tP = ( Vi,ti) with ti ∈ F′(Vi) such that ψP (tp) = sP .
Shrinking Vi if need be, we may suppose ψVi(ti) = s
⏐⏐
Vi
. It follows that ψVi∩Vj (ti
⏐⏐
Vj ∩Vi
) = ψVi∩Vj (tj
⏐⏐
Vi∩Vj
)
as both are equal to s
⏐⏐
Vi∩Vj
. Since ψV is injective for all V , we have the compatibility condition on the ti
to ensure (observe the Vi cover U ) that they glue to a section t∈ F′(U ). Checking on stalks shows that
ψU (t) = s and left exactness of Γ( U,•) follows.
1.9 That F⊕ G is a sheaf is obvious. Moreover, if f : F→ H andg : G→ H are morphisms of sheaves, then
for every U we have maps of abelian groups F(U )→ H(U ) and G(U )→ H(U ) compatible with restriction.
By the universal property of direct sum in the category of abelian groups, we get unique homomorphisms
of ab. gpg. F(U )⊕ G(U )→ H(U ) for all U , and these are evidently compatible with restriction because
restriction is a homomorphism (in particular on H). This gives a morphism F⊕ G→ H, which must also be
unique.
If f : H→ F and g : H→ G are two morphisms, then for all U we have a unique morphism H(U )→
F(U )⊕ G(U ) (implicitly using that direct sum and product of ﬁnitely many gps. are isomorphic in category
of ab. gps.) and thus a unique morphism H→ F⊕ G, which is compatible with restriction because f,g are
morphisms of sheaves and hence themselves compatible with restriction.
1.10 By the universal property of direct limit in the category of ab. gps., there is a unique morphism of
presheaves “ lim−→Fi”→ G having the desired properties. Now use the universal property of the sheaﬁﬁcation
lim−→Fi of “ lim−→Fi”.
1.11 Let sj∈ lim−→i Fi(Vj) be sections compatible on overlaps with Vj coveringU⊂X. Since X is noetherian,
there are ﬁnitely many indices j1,...,j n such that Vj⊆ ⋃n
k=1Vjk for all j. Thus, to glue the sj we need
only glue sj1,...,s jn. By the deﬁnition of a directed system, there is an N >0 such that sjk∈ FN (Vjk ) for
all k and since FN is a sheaf and the Vjk coverU , we obtain a section s∈ lim−→i Fi agreeing with sj overVj
for all j; i.e. U↦→ lim−→i Fi(U ) is a sheaf (as the other sheaf axiom follows by an almost identical argument).
1.12 Let sj ={si
j}i∈ lim←−i Fi(Vj) be compatible sections, where Vj is a cover of U . Since each Fi is a sheaf,
the{si
j} glue to give si∈ Fi(U ) for each i. If φi′i : Fi′→ Fi then we have φi′i(si′ )P = (φi′i)P ((si′ )P ) = ( si)P
2

sinceφi′i
⏐⏐
Vj
(si′
j ) = si
j for all j andP∈Vj for some j. Thus we conclude that the si are compatible with the
given maps deﬁning the inverse system so we have an element s∈ lim←−i Fi(U ) restricting to sj over each Vj.
Suppose that fi : G→ Fi is a collection of morphisms, compatible with the inverse system morphisms.
Deﬁne f : G(U ) → lim←−i Fi(U ) by s ↦→ {fi(U )}i. The compatibility of the fi with the inverse system
morphisms ensure that this is an element of lim ←−i Fi(U ), and compatibility with the restriction morphisms
is clear (as the fi are sheaf morphisms). Thus we obtain f : G→ lim←−i Fi. Uniqueness follows easily as
πi◦f =fi where πi : lim←−i Fi→ Fi is projection onto the i th component.
1.14 The complement of Supp s is the set S ={P∈U
⏐⏐sP = 0}. If sP = 0 then there is a nbd. VP ofP such
that s
⏐⏐
VP
= 0, and hence for all Q∈VP we have sQ = 0 since the restriction maps are gp. homs. so map 0
to 0. Thus, VP⊆S which shows that S is open and hence Supp s is closed.
1.15 Let f,g : F
⏐⏐
U → G
⏐⏐
U . Deﬁne f +g : F
⏐⏐
U → G
⏐⏐
U by ( f +g)V (s) = fV (s) + gV (s). Observe that
this is a morphism of sheaves F
⏐⏐
U→ G
⏐⏐
U since the restriction maps are homomorphisms of abelian groups.
Suppose that fi : F
⏐⏐
Vi
→ G
⏐⏐
Vi
are compatible morphisms, with Vi a cover of U . Deﬁne f F
⏐⏐
U → G
⏐⏐
U as
follows: any V ⊆U is cover by Wi =V∩Vi. For s∈ F(V∩U ) let si =s
⏐⏐
Wi
and put ti =fi
⏐⏐
Wi
(si). Since
the fi are compatible on overlaps, so are the ti, which therefore glue to t∈ G(V∩U ). We set fV (s) = t.
We must check that this is compatible with the restriction maps: if V ′⊂ V then fV (s
⏐⏐
V ′) is the glueing
of fi
⏐⏐
V ′∩Wi
(si
⏐⏐
V ′∩Wi
) = ti
⏐⏐
V ′∩Wi
since the fi are morphisms. Since ( t
⏐⏐
V ′ )
⏐⏐
Wi
= ti, we obtain the desired
compatibility.
1.16 a) Since X is irreducible, it consists of one connected component, and hence any U⊆X is connected. If
V ⊂U andf :V →A is cts. then f (V ) = a for some a. We extend f to ~f :U→A by deﬁnining ~f (U ) = a.
b) By 1.8 we need only show that F(U )→ F′′(U ) is surjective. Let s∈ F′′(U ). By 1.3, there is a cover
{Ui}i∈I of U and sections ti∈ F(Ui) with ti↦→ s
⏐⏐
Ui
. Consider the set S of pairs ( J,z ) with J ⊆ I and
z∈ F(∪j∈JUj) with z↦→s
⏐⏐
∪j∈JUj
. We order S by ( J,z )≤ (J ′,z ′) iﬀ J⊆J ′ and z′⏐⏐
∪j∈JUj
=z. The set S
is nonempty as for any ﬁxed index j0∈ I we have ( {j0},tj0). Moreover, any chain of S is bounded above
by the sheaf axiom, so by Zorn’s lemma, S has a maximal element ( I0,z ). If I0⁄= I, pick i∈ I\I0, set
V =∪j∈I0Uj and let ti∈ F(Ui) be as above. Since x = z
⏐⏐
V ∩Ui
−ti
⏐⏐
V ∩Ui
↦→ 0∈ F′′(V∩Ui), there exists
vi∈ F′(V∩Ui) mapping to x. Since F′ is ﬂasque, we may lift vi to wi∈ F′(Ui) and deﬁne t′
i = ti +wi.
Thenz,t ′
i are compatible sections and glue to t∈ F(V∪Ui). Clearly t↦→s
⏐⏐
V ∪Ui
. Since I0 was chosen to be
maximal, we have i∈I0 so I =I0.
c) By part b) for V ⊆U we have a commutative diagram
0 /d47/d47F′(U ) /d47/d47
/d15/d15
F(U ) /d47/d47
/d15/d15
F′′(U ) /d47/d47
/d15/d15
0
0 /d47/d47F′(V ) /d47/d47F(V ) /d47/d47F′′(V ) /d47/d470
in which the ﬁrst two vertical arrows are surjective. It follows that the third is also, and hence that F′′ is
ﬂasque.
d) This amounts to the fact that V ⊆U implies f −1(V )⊆f −1(U ).
e) The sheaf G is ﬂasque since if V ⊆U then any s :V →∪ P ∈V FP may be extended to ~s :U→∪ P ∈U FP by
~s(P ) =
{
s(P ) if P∈V
0 otherwise .
Deﬁne φU : F(U )→ G(U ) by s↦→
(
P↦→sP
)
. This is injective since s = 0 iﬀ sP = 0 for all P iﬀ P↦→sP is
the zero map.
3

1.17 Suppose Q∈P . Then every open set containing Q containsP so lim−→U ∋QiP (A)(U ) = lim−→U ∋PA =A. If
Q⁄∈P then there exists an open U containingQ and not P . For any open V containingQ the set V∩U is
open, contains Q and not P . Since lim−→V ∋QiP (A)(V ) = lim−→V ∋QiP (V∩U ) = 0 we conclude that iP (A)Q = 0
for such Q. Observe that
i∗(A)(U ) = A(i−1(U )) =
{
A if P∈U
0 otherwise =iP (A)(U ).
1.18 Deﬁne ϕU : lim−→V ⊇f (U ) F(f −1(V ))→ F(U ) by the collection of maps res f −1(V ),U for all V occurring
in the direct limit (observe V ⊇ f (U ) implies f −1(V )⊇ U ). The universal property of sheaﬁﬁcation then
gives a map ϕ+ :f −1f∗F→ F that is functorial in F (essentialy because ϕ is just a collection of restriction
maps). Since f −1 is a functor from sheaves on Y to sheaves on X, this gives a map τ : Hom Y (G,f ∗F)→
HomX (f −1G, F) determined by g↦→ϕ+◦ (f −1g).
Now deﬁne ψU : G(U )→ limV ⊇f (f −1(U )) G(V ) by inclusion of G(U ) as a term in the direct limit (ob-
serve that U ⊇ f (f −1(U ))). Composing ψ with the map to the sheaﬁﬁcation yields a map ψ+ : G→
f∗f −1G, functorial in G (again, roughly because ψ is deﬁned by the identity map). Thus we can deﬁne
σ : Hom X (f −1G, F)→ HomY (G,f ∗F) by g↦→ (f∗g)◦ψ.
It remains to check that σ◦τ = id HomY and τ◦σ = id HomX . Perhaps a stalk calculation?
1.19 a) If P ∈ Z, every open V ∋ P in Z is of the form U∩Z for some open U in X. Thus, ( i∗F)P =
lim−→X⊇U ∋P F(U∩Z) = lim−→Z⊇V ∋P F(V ) = FP . If P⁄∈Z then since Z is closed there exists an open U∋P
with U∩Z = 0. Now ( i∗F)P = lim−→X⊇V ∋P F(V∩Z) = lim−→X⊇V ∋P F(V∩U∩Z) = 0.
b) Recall that the stalk of a presheaf is the stalk of its sheaﬁﬁcation at any point. If P ∈ U then
lim−→V ∋Pj!(V ) = lim−→V ∋Pj!(U∩V ) = lim−→W ∋P F(W ) = FP . If P⁄∈ U then no open set containing P is con-
tained in U , so lim−→V ∋Pj!(V ) = 0. If G is any sheaf on X with GP = FP forP∈U and GP = 0 otherwise, and
the restriction of G toU is F, then we have a map G→j!F given by composing G(V )
res
−−→G(U∩V ) = F(U∩V )
with the sheaﬁﬁcation map to j!F. The condition on stalks shows that this map is an isomorphism on all
stalks, hence an isomorphism of sheaves.
c) If V ⊆U we map F(V )→ F(V ) by the identity; otherwise we use the zero map. This gives a morphism
j!(F
⏐⏐
U )→ F. We use the map F→i∗i−1F =i∗(F
⏐⏐
Z) described in 1.18. The sequence we obtain is exact on
stalks (two cases: P∈Z or P∈U ) and hence exact.
2.2
2.1 Deﬁne ϕ : Spec Af→D(f ) by the map p↦→ p∩A =i−1(p) induced by the map i :A→Af . One checks
easily that ϕ is a homeomorphism with ϕ−1D(f )→ SpecAf given by p↦→ pe (by commutative algebra there
is a 1-1 corr. between primes of Af and primes of A not containing ( f )). For example, ϕ takes the basic
open set D(g/fr) to D(fg ) and so is an open map. We deﬁne ϕ# : OSpecA
⏐⏐
D(f )→ ϕ∗OSpecAf on basic
opens D(g)⊆ SpecA by OSpecA
⏐⏐
D(f )(D(g)) = Afg
id
−→(Af )g/1 = OSpecAf (ϕ−1(D(g))). This gives a well
deﬁned sheaf map since every point has a basic open nbd.
2.2 Let P ∈ U and V ∋ P be a nbd. of P in X such that ( V, OX
⏐⏐
V ) is aﬃne, say isomorphic to Spec R.
There exists a basic open nbd. D(f )⊆ U∩V containing P that is open in V . By 2.1, the locally ringed
space ( D(f ), (OX
⏐⏐
V )
⏐⏐
D(f )) is isomorphic to Spec Rf and is hence aﬃne. Thus ( U, OX
⏐⏐
U ) is a scheme.
2.3 a) Suppose OP reduced for all P and let s∈ OX (U ) be nilpotent. Then sn = 0 in every stalk, so sP = 0
for all P∈U hence s = 0 by the sheaf axiom. Conversely, suppose OX (U ) reduced for all U . If s∈ OP is
4

nilpotent, pick U,s ′ representing s so ( s′)n = 0 in sP hence there is a nbd. V of P with ( s′⏐⏐
U ∩V )n = 0 (as
restriction is a homomorphism) hence s′⏐⏐
U ∩V = 0 since OX (U∩V ) is reduced, whence s = 0 in sP .
b) Let P∈ X and let U∋ P be such that ( ϕ,ϕ #) : ( U, OX
⏐⏐
U )≃ SpecR is aﬃne. Then ( U, (OX )red
⏐⏐
U )≃
SpecRred. Indeed, the topological spaces Spec R and Spec Rred are homeomorphic (as every prime contains
the nilradical) via the surjection R→R/N. There is a natural map ψ : OSpecR→ OSpecRred deﬁned on the
basic open D(f ) by the quotient map Rf→ (Rf )red = (Rred)f (since localization commutes with quotients).
Then the map ( ψ◦ϕ#)V : OX (V )→ OSpecRred(ϕ−1(V )) is a map to a reduced ring, and therefore factors
through OV (V )red. The universal property of sheaﬁﬁcation then yields a map ( OX )red→ϕ∗OSpecRred that
is an isomorphism on stalks, hence an isomorphism.
c) This amounts to the commutative algebra statement that any map from a ring R to a reduced ring S
factors uniquely through Rred and the fact that the push forward of a reduced sheaf is reduced.
2.4 The result holds when X is aﬃne. In general, cover X by aﬃnes Ui and cover the double overlaps Ui∩Uj
by aﬃnes Uijk . Then we have an exact sequence of rings
0 /d47/d47Γ(X, OX )
g /d47/d47∏
i Γ(Ui, OUi)
f /d47/d47∏
i,j,k Γ(Uijk, OUijk )
where g is given by s↦→ ∏
is
⏐⏐
Ui
and f is given by ∏
isi↦→ ∏
i,j,k(si−sj)
⏐⏐
Uijk
. The functor Hom( A,•) is
left exact, so we obtain the exact sequence
0 /d47/d47Hom(A, Γ(X, OX )) /d47/d47∏
i Hom(A, Γ(Ui, OUi)) /d47/d47∏
i,j,k Hom(A, Γ(Uijk, OUijk ))
Meanwhile, since to give a morphism X → SpecA is to give morphisms Ui→ SpecA that agree on the
coverings of double overlaps, we have the exact sequence of sets
0 /d47/d47Hom(X, SpecA) /d47/d47∏
i Hom(Ui, SpecA) /d47/d47∏
i,j,k Hom(Uijk, SpecA)
(where ”kernel” is interpreted in the appropriate sense, i.e. in the category of sets). Piecing these sequences
together, we have
0 /d47/d47Hom(A, Γ(X, OX )) /d47/d47/d79/d79
/d15/d15
∏
i Hom(A, Γ(Ui, OUi)) /d47/d47
/d79/d79
/d15/d15
∏
i,j,k Hom(A, Γ(Uijk, OUijk ))/d79/d79
/d15/d15
0 /d47/d47Hom(X, SpecA) /d47/d47∏
i Hom(Ui, SpecA) /d47/d47∏
i,j,k Hom(Uijk, SpecA)
,
where the second two vertical arrows are bijections. Thus the ﬁrst is also.
2.5 The closed points of Spec Z are the prime ideals ( p) with p∈ Z not equal to 0. There is a single open
point (the generic point), namely (0). The basic open sets are of the form D(n) with n∈ Z and consist of
those primes not dividing n. The local ring at the closed point ( p) is Z(p) and the residue ﬁeld is Fp while
the local ring and residue ﬁeld at (0) are both Q. Since there is a unique homomorphism from Z to any ring
deﬁned by 1 ↦→ 1, 2.4 implies that every scheme X admits a unique morphism to Spec Z.
2.6 Let R be the zero ring. Then Spec R ={∅} and OSpecR(∅) = R = 0. There is a unique morphism
f : Spec R→X to any scheme X deﬁned by inclusion on topological spaces and OX→f∗OSpecR given by
the identically zero morphism.
2.7 Given a morphism ( ϕ,ϕ #) Spec K → X we obtain a point x = ϕ((0))∈ X and a sheaf morphism
ϕ# : OX→ ϕ∗OSpecK, which gives a local map of local rings ϕ#
x : OX,x→ OSpecK,(0) = K; in particular
mx↦→ 0 so we obtain a morphism k(x)→K which must be injective since k(x) is a ﬁeld. Conversely, given
5

a point x∈ X and an inclusion k(x) ↪→ K we deﬁne φ : Spec K→ X by φ((0)) = x and ϕ#
U : OX (U )→
OSpecK(ϕ−1(U )) for each open U in X by OX (U )→ OX,x→ k(x) ↪→ K, where the ﬁrst arrow is the zero
map when x⁄∈U and is inclusion into the direct limit when x∈U .
2.8 Suppose given a map ϕ : Spec k[ϵ]/ϵ2 ={(ϵ)}→ X as schemes over k. This gives a point ϕ(ϵ) = x∈X
together with the diagram of local rings
OX,x /d47/d47k[ϵ]/ϵ2
k
/d97/d97/d66/d66/d66/d66/d66/d66/d66/d66
/d60/d60/d121/d121/d121/d121/d121/d121/d121/d121/d121
(since (0) ∈ Speck↦→ (ϵ)∈ Speck[ϵ]/ϵ2). Since the map ϕx : OX,x→k[ϵ]/ϵ2 is local, we have ϕx(mx)⊆ (ϵ),
from which we deduce that the map k(x)→k[ϵ]/ϵ≃k is an isomorphism. Since ϵ2 = 0, we deﬁne ψ :mx→k
byψ(z) = ϕx(z)/ϵ and note that this is well deﬁned, k-linear (by the commutativity of the above diagram),
and kills m2
x so yields an element of Hom( mx/m2
x,k ).
Conversely, suppose given a point x∈X with residue ﬁeld k and a k-linear ψ :mx→k killing m2
x. We
deﬁneϕx : OX,x→k[ϵ]/ϵ2 byϕ(α+z) = α+ψ(z)ϵ, where α∈k andz∈mx (using that OX,x/mx≃k). One
checks using the linearity of ψ and the fact that ϵ2 = 0 and that ψ killsm2
x thatϕx is a local homomorphism
with the above diagram commuting. Finally, deﬁne a map ϕ : Spec k[ϵ]/ϵ2 → X by ϕ((ϵ)) = x and
ϕ# : OX→ OSpeck[ϵ]/ϵ2 by the map OX (U )→ OX,x
ϕx
−−→k[ϵ]/ϵ2 where the ﬁrst arrow is 0 if x⁄∈ U and is
inclusion into the direct limit otherwise. One easily checks that this gives a map of sheaves.
2.9 Suppose ζ1,ζ 2 are two generic points of Z. Then since ζi =Z, an open set contains ζ1 iﬀ it contains ζ2.
Letting U = Spec R be an aﬃne nbd. of ζ1, we identify ζi = pi∈ SpecR. Since p2∈ p1, we have p2⊇ p1
and vice versa, so ζ1 = ζ2. This settles uniqueness. As for existence, let Z be irreducible, nonempty, and
closed and let U⊆ Z be a (nonempty) open aﬃne. Then U = Spec R is dense in Z and irreducible. By
Zorn’s lemma, R has minimal primes, and the irreducibility of Spec R impliesR has a unique minimal prime,
ζ∈U . It follows that ζ =U (closure in U ) and since U is dense in Z, we have ζ =Z (closure in Z, hence
also X as Z is closed).
2.10 Observe that R[x] is a PID. The prime ideals of R[x] fall into three types:
1. The generic (and open) point (0), with residue ﬁeld R(x).
2. Closed points of the form ( x−α) with α∈ R. The residue ﬁeld in each case is R.
3. Closed points of the form ( x2 +αx +β), with residue ﬁeld C.
As a set, Spec R[x] = R∪ (C− R) = C with the bijection sending z∈ C to (( x−z)(x−z)) if z⁄∈ R and
to ( x−z) if z∈ R.
2.11 Again, Fp[x] is a PID, and the points of Spec Fp[x] are
1. The generic point (0) with residue ﬁeld Fp(x).
2. Closed points of the form ( f ) with f a monic irreducible polynomial of degree d≥ 1. The residue ﬁeld
is Fpd.
Since xpn
−x is the product of all monic irreducibles (over Fp) of degree d|n we get the formula
#{monic degree d irreducibles} =
∑
d|n
µ(d)pn/d
6

by m¨ obius inversion.
2.12
2.13 a) Let U be an open set of X that is not quasi-compact and {Ui} an open cover of U that does not
admit a ﬁnite subcover. Using the axiom of choice, we can ﬁnd a sequence of Ui, say Uij for 1 ≤j withUij+1
not contained in Vj :=∪1≤k≤jUik . Then the Vj form an ascending nonterminating chain of open subsets of
X. Conversely, suppose that X is noetherian and let {Ui} be an open cover of the open set U⊆ X. Let
S be the set of ﬁnite unions of the Ui, partially ordered by inclusion. Every chain evidently has an upper
bound, so by Zorn’s lemma S has a maximal element, which is easily seen to be U , viz. U is quasi-compact.
b) Let Ui be an open covering of X = Spec R. Covering each Ui by basic opens, we may suppose that the
Ui are all basic, Ui = D(fi). Then the fi generate the unit ideal, so in particular, ﬁnitely many of them
do, giving a ﬁnite subcover. Let R = k[xi] for 1 ≤ i be a polynomial ring in inﬁnitely many variables and
consider the set U = sup D(xi). This is not quasi-compact, so by a) Spec R is not noetherian.
c) Let U be an open set and Ui an open cover, which we may assume to be basic ( Ui =D(fi))as above. If A
is noetherian, then the ideal ( fi) is generated by ﬁnitely many of the fi, say fi :i∈J with # J <∞. Then
Ui with i∈J is a ﬁnite subcover.
d) Take A = k[xi]/(x2
i ) for 1 ≤ i. Evidently A is not noetherian, but the space Spec A consists of a single
point (0).
2.14 a) Recall that the set Proj S consists of those homogenous prime ideals that do not contain the irrelevant
idealS+. If every element S+ is nilpotent then S+ is contained in the nilradical and hence in every prime of
S, so Proj S is empty. Conversely, if Proj S =∅ then every homogenous prime ideal of S containsS+, so S+
is contained in the intersection of all homogenous prime ideals and is therefore contained in the nilradical.
b) Let p∈ U . Then there is some s∈ S+ with ϕ(s)⁄∈ p. The set D(ϕ(s)) is an open nbd of p in U .
The morphism f : U→ ProjS is given by contraction. Each homogenous prime of Proj T contracts to a
homogenous prime of S, and when p∈U , the contraction ϕ−1(p) does not contain all of S+ so is in Proj S.
Continuity follows since contraction preserves containment relations, and the sheaf map is given by.....
c) Since ϕ is graded, we have ϕ(S+)⊆ T+. If ϕd : Sd→ Td is an isomorphism for all d≥ d0 then every
prime that does not contain T+ cannot contain ϕ(S+): indeed, if there is some t∈Tr not in p then tk⁄∈p
for all k and since r >1 we may choose k so that rk > d0, thus producing tk =ϕ(s) for some s∈S+ so p
does not contain ϕ(S+), thus giving Proj T⊆U so in fact equality holds.
We now show that f : Proj T → ProjS is an isomorphism. Let {ti} generate T+, so {D+(ti)} is
a cover of Proj T . Then {D+(td0
i )} is also a cover of Proj T . Put si = ϕ−1(td0
i ) (here we use that ϕd
is an isomorphism for all d≥ d0). Then fi = f
⏐⏐
D+(ti) → D+(si) is a morphism of aﬃne schemes (as
D+(ti)≃ SpecT(ti) and D+(si)≃ SpecS(si)) corresponding to the ring homomorphism ϕi : S(si)→ T(ti)
induced by ϕ. But ϕi is an isomorphism since si has degree at least d0, and ϕd is an isomorphism for all
d≥d0. Thus, fi is an isomorphism. Now the D+(si) cover Proj S since any p∈ProjS fails to contain some
si (otherwise the contraction of p, which is in Proj T , contains ti for all i and hence T+, a contradiction),
so to show that f is an isomorphism we need only show it is injective (since a bijective local isomorphism
is an isomorphism and surjectivity follows from the fact that the D+(si) cover Proj S). If f (x) = f (y) then
ϕ−1(x) = ϕ−1(y) = p∈ ProjS, from which it follows that xd =yd for all d≥d0 (here xd =x∩Td). Pick
z∈x not in y and let s∈S+ be such that s⁄∈y (recall S+⁄⊆y). Then sd0z∈x is of degree at least d0 and
so is in y. Since y is prime, this implies that z∈y so f is injective, hence an isomorphism.
2.16 a) We have U∩Xf ={x∈ SpecB
⏐⏐fx =fx⁄∈mx⊆ OX,x} (wherefx =fx sincef andf agree in a nbd.
of x). Putting x =p⊆B this is {p∈ SpecB
⏐⏐fp⁄∈pBp} and it is easy to verify that fp⁄∈pBp iﬀ f⁄∈p, so
U∩Xf =D(f ). Hence Xf intersects every open aﬃne (hence every open) in a (union of) basic opens, and
so must be open (for x∈Xf pick an aﬃne open nbd. U of x in X so U∩Xf is open in U hence in X, and
is contained in Xf ).
7

b) Cover X by aﬃnes Ui = Spec Bi fori = 1 ...n and let ai =a
⏐⏐
Ui
andfi =f
⏐⏐
Ui
. By part a), Ui∩Xf =D(fi),
so ai = 0 on D(fi), i.e. ai = 0 in ( Bi)fi. Thus there is ri ≥ 0 such that aifri
i = 0 in Bi. Letting
N = max 1≤i≤nri we ﬁnd that the global section afN restricts to 0 on each Ui and is therefore 0.
c) Let Ui = Spec Bi for 1 ≤ i≤ n be a ﬁnite aﬃne cover of X. Put b
⏐⏐
Xf ∩Ui
= bi/fi
di
∈ (Bi)fi with
bi ∈ Bi. Set d = ∑
idi (ﬁnite) and b′
i = fd−dibi ∈ Γ(Ui, OX ). Since b′
i
⏐⏐
Xf
= fd−difdib we see that
(b′
i−b′
j)
⏐⏐
Ui∩Uj ∩Xf
= 0 so by part b), for each pair i,j there is an integer dij with fdij (bi′−bj′ ) = 0 as
an element of Γ( Ui∩Uj, OX ). Letting D = max i,jdij (ﬁnite since the double overlaps have ﬁnite aﬃne
covers by hypothesis) we ﬁnd that fDb′
i∈ Γ(Ui, OX ) are compatible on double overlaps, so give an element
a∈ Γ(X, OX ). By construction, a
⏐⏐
Xf ∩Ui
=fDb′
i =fD+db so in particular a
⏐⏐
Xf
=fD+db by the sheaf axiom.
d) Deﬁne ϕ :Af→ Γ(Xf, OXf ) by a/fn↦→a
⏐⏐
Xf
/fn⏐⏐
Xf
. (Observe that f
⏐⏐
Ui∩Xf
∈ Γ(Ui∩Xf, OXf ) = ( Bi)f
is a unit for all i and hence f
⏐⏐
Xf
∈ Γ(Xf, OXf ) is a unit). The map is a homomorphism since restriction is,
and is injective since otherwise fka = 0 for some k by part b), so a/fn = 0 in Af . Surjectivity is part c)
above.
2.17 a) Let gi : Ui→ f −1(Ui) be the inverse to f
⏐⏐
f −1(Ui) : f −1(Ui)→ Ui. Observe that gi.gj agree on
Ui∩Uj (because f
⏐⏐
Ui∩Uj
◦gi
⏐⏐
Ui∩Uj
=f
⏐⏐
Ui∩Uj
◦gj
⏐⏐
Ui∩Uj
= id Ui∩Uj andf
⏐⏐
Ui∩Uj
is an isomorphism, so we can
“cancel” the f from both sides). Thus we can glue the gi to get a morphism g :Y→X that is locally—hence
globally—inverse to f .
b) By 2.4, we have a morphism f : X→ SpecA corresponding to the identity ring homomorphism A→
Γ(X, OX ). By 2.16 d) we have Γ( Xf, OXf )≃Af , and the isomorphism makes the diagram
A
id /d47/d47
/d15/d15
Γ(X, OX )
res
/d15/d15
Af
∼ /d47/d47Γ(Xf, OXf )
commute, from which it follows that f
⏐⏐
Xf
: Xf → SpecAf is an isomorphism for each f = fi. Since the
fi generate the unit ideal, Spec Afi covers Spec A. Thus the hypothesis of part a) are satisﬁed, so f is an
isomorphism and X is aﬃne. The converse follows from the quasi-compactness of an aﬃne scheme; see 2.13
b).
2.18 a) D(f ) is empty iﬀ f is contained in the intersection of all primes; i.e. iﬀ f is nilpotent.
b) If the map of sheaves OX→f∗OY is injective then A = OX (X)→ OY (f −1(X)) = OY (Y ) = B is injective.
Conversely, if A→B is injective, then Af→Bϕ(f ) is injective for all f∈A (ifa/fk↦→ 0 then ϕ(f )mϕ(a) =
ϕ(fma) = 0 so fma = 0 since ϕ is injective). This shows that the map f # : OX (D(f ))→ OY (f −1(D(f )))
is injective for all f (where we use that f −1(D(f )) = D(ϕ(f ))). Thus the map of sheaves is injective since
it is injective on a base of opens of X, and hence injective on every stalk.
Let f∈ A. Then if D(f ) is nonempty, there exists q∈ SpecB with f⁄∈ ϕ−1(q), or what is the same,
every nonempty D(f )⊆ SpecA contains some f (q). Indeed, if f∈ϕ−1(q) for all q∈ SpecB then ϕ(f )∈q
for all q, and is hence nilpotent. As ϕ is an injective homomorphism, it follows that f is nilpotent and hence
by a) that D(f ) is empty. Thus f (Y ) is dense.
c) If ϕ is surjective, then A/ kerϕ≃B so their spectra are homeomorphic, and Spec A/ kerϕ =V (kerϕ)⊆
SpecA is a closed subset. Now let s∈ (f∗OY )p be represented by ~s∈ OY (f −1(U )). Shrinking if necessary,
we may suppose U = D(f ) is basic, so f −1(U ) = D(ϕ(f )) as above. Thus, ~s∈ Bϕ(f ). Since A→ B is
surjective, so is Af→ Bϕf , so there exists t∈ OX (U ) mapping to ~s. It follows that the induced maps on
stalks are all surjective, so the sheaf map is surjective.
d) Let X ′ = Spec A/ kerϕ. Then we have Y
ψ
− →X ′ φ
− →X, where φ is a homeomorphism onto a closed subset
by c) and ψ(Y ) is dense in X ′ by b). Since the composite is f (this is just the fact that the ring map A→B
8

factors through A/ kerϕ) and f (Y ) is homeomorphic to a closed subset of X, we conclude that ψ(Y )⊆X ′ is
dense and closed, so that ψ(Y ) = X ′. Moreover, since f,φ are homeomorphisms, so is ψ. We claim that ψ#
is an isomorphism. It is injective by b) and surjective since f # is surjective and the map f # : OX→f∗(OY )
factors as OX
φ#
−−→φ∗OX ′
φ∗(ψ#)
−−−−−→φ∗ψ∗ OY = f∗OY as f = φ◦ψ. Hence it is an isomorphism by 1.5. It
follows that Spec B≃ SpecA/ kerϕ from which we conclude that ϕ :A/ kerϕ→B is an isomorphism, i.e.
that ϕ is surjective.
2.19 ((i) =⇒ (ii)) Suppose Spec A =V (I)∪V (J) is disconnected. Pick a non-nilpotent, nonunit e1∈I (ifI
consists only of nilpotents then the disconnect is trivial). Then e2 = 1 −e1∈J, and hence e1e2 is in every
prime ideal and so nilpotent. That is, e1,e 2 as elements of Ared are orthogonal idempotents. We claim that
such idempotents can be lifted to A. Indeed, let N denote the nilradical of A. Let e′
1 be any lift of e1 to
A and put e′
2 = (1 −e′
1). Then e′
1e′
2 = n is nilpotent, so for some j we have e′
1
je′
2
j = 0. Set ˜ e1 = e′
1
j and
˜e2 =e′
2
j. Observe that ˜ e1≡e′
1 mod N and ˜e2≡e′
2 mod N since e′
1≡e′
1
2, e′
2≡e′
2
2 mod N . Moreover,
we have ˜e1 + ˜e2≡ 1 mod N since e′
1 +e′
2≡ 1 mod N . It follows that ˜ e1 + ˜e2 is a unit, say with inverse
a∈ A. Clearly a≡ 1 mod N . We now put e∗
1 = a˜e1 and e∗
2 = a˜e2. Then e∗
1 +e∗
2 = a(˜e1 + ˜e2) = 1 and
e∗
1e∗
2 = a2˜e1˜e2 = 0. Since a≡ 1 mod N we have e∗
1≡ ˜e1≡ e′
1 mod N so that e∗
1 lifts e1 and similarly e∗
2
lifts e2.
((ii) =⇒ (i)) Since e1e2 = 0 we see that Spec R = V (e1)∪V (e2). Moreover, V (e1)∩V (e2) = ∅ since no
prime can contain 1 = e1 +e2.
((ii) =⇒ (iii)) Suppose that A has orthogonal idempotents e1,e 2. Deﬁne ϕ : Ae1×Ae2 by ( u,v )↦→ u +v.
One checks this is a homomorphism. It is injective since if re1 = se2 then re2
1 = re1 = se1e2 = 0. It is
surjective since r =r(e1 +e2) = re1 +re2.
((iii) =⇒ (ii)) If A≃A1×A2 then e1 = (1, 0) and e2 = (0, 1) are orthogonal idempotents.
2.3
Nike’s trick: We will use the following “trick” repeatedly. Let Spec R, SpecR′⊆ X be aﬃne opens with
x∈ SpecR∩ SpecR′. Then there is an aﬃne neighborhood U of x that is basic open in both Spec R and
SpecR′.
3.1 The “if” direction is obvious. Conversely, let Spec Bi be an open aﬃne cover of Y with f −1(SpecBi)
covered by Spec Aij with Aij a ﬁnitely generated Bi-algebra for all j. Observe that f −1(Spec(Bi)b) is
covered by Spec( Aij)b (if f (x)∈ Spec(Bi)b then f (x) is a prime of Bi not containing b so x is a prime of
some Spec Aij not containing the image of b under the algebra map Bi→Aij) and that ( Aij)b is a ﬁnitely
generated ( Bi)b-algebra. Thus, the hypotheses are inherited by basic opens of Ui.
Now let Spec B⊆ Y be arbitrary. By “Nike’s trick,” there exists a cover of Spec B by aﬃnes that are
basic open in both SpecB and Spec Bi (for varying i). This allows us to reduce to the case that Y = Spec B
is aﬃne, with the same hypotheses as above, and we need only show that any aﬃne in the f −1(Y ) = X is a
ﬁnitely generated B-algebra.
Thus, let Spec Bbi be our cover of Spec B (constructed above) by basic opens with f −1(SpecBbi) covered
by Spec Aij and Aij a ﬁnitely generated Bbi = B[1/bi]-algebra, and hence a ﬁnitely generated B-algebra.
Let Spec A⊆X be arbitrary. By the Nike trick again, there is a cover Spec Aak of Spec A with each Spec Aak
basic open in both SpecA and Spec Aij (for varying i,j ). Each Aak is isomorphic to a localization of some
Aij and is therefore a ﬁnitely generated Aij-algebra, and hence also a ﬁnitely generated B-algebra.
Thus, we are reduced to the following problem: A is a ring with ( ak) generating the unit ideal, and
each Aak is a ﬁnitely generated B-algebra, and we must show that A is a f.g. B-algebra. We may clearly
assume that there are only ﬁnitely many ak and that we have x1,...,x n ∈ A with ∑xkak = 1. Let
Aak = B[yk1/αN
k ,yk2/αN
k ,...,y kmk/αN
k ] with ykl∈ A for all k,l . Put A′ = B[xk,ak,ykl] with k,l running
over all possible indices (a ﬁnite set!). Then A′ is obviously a B-subalgebra of A. Moreover, we have
Aak =A′
ak for all k. For any p∈ SpecA choose ak⁄∈p (since ( ak) is the unit ideal this is possible). Then
9

A′
p is a further localization of A′
ak = Aak , from which we conclude that A′
p = Ap for all p∈ SpecA. Thus
A =A′ is a ﬁnitely generated B-algebra.
3.2 As in 3.1, one direction is trivial. For the converse, let Spec B⊆ Y be arbitrary and suppose we have
a cover Spec Bi of Y with f −1(SpecBi) quasi-compact. Suppose f −1(SpecBi) is covered by {SpecAij}j∈Ji
with # Ji <∞ for each i. Then we can cover Spec B by ﬁnitely many opens of the form Spec( Bi)bi, say
for i∈I, and we have f −1(Spec(Bi)bi) = ∪j∈Ji Spec(Aij)bi so f −1(Spec(Bi)bi) is quasicompact. It follows
that f −1(SpecB) = ∪i∈I, j∈Ji(Aij)bi, and since # I <∞ and # Ji <∞ for all i∈ I, we conclude that
f −1(SpecB) is quasicompact.
3.3 a) If f is of ﬁnite type then it is clearly of locally ﬁnite type and quasi-compact. Conversely, if f is q-
compact and locally of ﬁnite type, then we have a covering of Y by aﬃnes Spec Bi withf −1(SpecBi) covered
by Spec Aij withAij ﬁnitely generated Bi-algebras. By 3.2, f −1(SpecBi) is quasi-compact, so ﬁnitely many
of the Spec Aij will do; i.e. f is of ﬁnite type.
b) By a) f is f.t. iﬀ. it is locally f.t. and q-compact. Now apply 3.1 and 3.2.
c) This was done in 3.1.
3.4 The “if” direction is obvious. Conversely, let Spec Bi be an open aﬃne cover of Y with f −1(SpecBi) =
SpecAi with Ai a ﬁnitely Bi-module. for all i. Observe that f −1(Spec(Bi)b) = Spec( Ai)b and that ( Ai)b is
a ﬁnite ( Bi)b-module so the hypotheses are inherited by basic opens of Spec Bi.
Now let Spec B ⊆ Y be arbitrary. By “Nike’s trick,” there exists a ﬁnite cover of Spec B by aﬃnes
that are basic open in both SpecB and Spec Bi (for varying i). This allows us to reduce to the case that
Y = Spec B is aﬃne with a covering Spec Bbi, by ﬁnitely many basic opens and f −1(SpecBbi) = Spec Ci
aﬃne with Ci a ﬁnite Bbi-module. We need only show that f −1(Y ) = X is aﬃne, equal to Spec A, with A
a ﬁnite B-module.
By 2.4, we have a ring homomorphism B → Γ(X, OX ) = A corresponding to the map f : X →
Y = Spec B. Moreover, we see that the bi generate the unit ideal in A because they do in B, and that
f −1(SpecBbi) = Xbi = Spec Ci is aﬃne and gives a ﬁnite cover of X. By 2.17, X = Spec A is aﬃne.
It remains to show that A is a ﬁnite B-module. We now know that Xbi = Spec Abi = Spec Ci, so
Abi≃Ci. That is, we are reduced to the following problem: A is a B-algebra and bi∈B is a ﬁnite collection
generating the unit ideal such that Abi is a ﬁnite Bbi-module, and we wish to conclude that A is a ﬁnite
B-module. Let {zij} for 1 ≤j≤mi generate Abi as a Bbi-module, where by clearing denominators we may
suppose that zij∈A. Any a∈A can be written a = ∑βijzij, whereβij∈Bbi. Since there are only ﬁnitely
manyβij, we can ﬁnd some N so that bN
i βij =γij∈B for all i,j . Then bN
i a = ∑γijzij for all i. Since bi
generate the unit ideal, so do bN
i , so we have ∑xibN
i = 1 for xi∈ B. Thus, putting µij = xiγij we have
µij∈B and a = ∑
i,jµijzij. Thus A is a ﬁnite B-module.
3.5 a) One reduces immediately to the aﬃne case, Spec B→ SpecA with B integral over A. The fact that
there are only ﬁnitely many primes of B lying over any given prime of A is standard Commutative Algebra.
b) This is the “going up” theorem from Commutative Algebra.
c) Take k[x]→k[x,y ]/(xy− 1)×k with the map p(x)↦→ (p(x),p (0)). The corresponding map of spectra is
surjective, ﬁnite type, and quasi-ﬁnite. However, k[x,y ]/(xy− 1)×k is not a ﬁnite k[x]-module.
3.6 Let U = Spec A be any aﬃne open. Since X is irreducible, xi = X so ξ∈ U . We claim that ξ is a
minimal prime of A. Indeed, is ζ∈ SpecA is contained in ξ, then X⊇ ζ⊇ ξ = X, so we have equality,
and the uniqueness of generic point (2.9) gives ζ = ξ. But OX (U ) = A is an integral domain as X is
integral, and there is a unique minimal prime (0) of any domain. It follows that Oξ = lim U ∋ξ OX (U ) =
limf ∈A−{0} OX (D(f )) = lim f ⁄∈AAf =A(0) = Frac A.
3.7 Let ξX,ξY be the generic points of X,Y resp. If U is an open set of Y not containing y = f (ξX ) then
f −1(U ) is an open set of X not containing ξX , and so must be empty. But then U∩f (X) = ∅ and f is not
10

dominant. We conclude that every open set of Y containsf (ξX ), and hence that f (ξX ) = ξY . We thus have
a local map of local rings f #
ξY
: OξY → OξX which is injective as OξY =K(Y ) is a ﬁeld, i.e. K(X) is a ﬁeld
extension of K(Y ). We claim that it is an algebraic ﬁeld extension. Indeed, If Spec B is any aﬃne open in Y
and Spec A is any aﬃne open in f −1(SpecB), then we have a ring homomorphism ϕ :B→A corresponding
tof : Spec A→ SpecB, and since f is generically ﬁnite, there are only ﬁnitely many primes of A lying over
(0)∈ B. If Frac A = K(X) is transcendental over Frac B = K(Y ) then A is transcendental over B, and
there are inﬁnitely many primes of A lying over (0) ∈ SpecB, contradicting the generic ﬁniteness assumption.
Hence K(X) is an algebraic, ﬁnitely generated (since f is of ﬁnite type) K(Y )-algebra, and is therefore a
ﬁnite extension of ﬁelds. It follows that there exists some b∈B with A ﬁnitely generated as a Bb-module.
Thus, we may shrink Spec B (if necessary) to obtain a cover of f −1(SpecB) by aﬃnes Spec Ai for 1 ≤i≤n
with each Ai a ﬁnite B-module. Now for each i < nthere exists ai∈ Ai such that Spec( Ai)ai⊆ SpecAn,
and since Ai is an integral B-extension, ai satisﬁes a monic polynomial ∑
kβikak
i = 0 with βik∈ B and
βi0⁄= 0. Let b = ∏
1≤i<nβi0, so b⁄= 0, and every prime of Ai containingai containsb for all i<n , that is,
Spec(Ai)b⊆ Spec(Ai)ai for all i<n . It follows that f −1(Bb) = ∪i<n Spec(Ai)b∪ Spec(An)b = Spec(An)b is
aﬃne, and since An is a ﬁnite B-module, (An)b is a ﬁnite Bb-module. As X,Y are integral (hence irreducible),
U = Spec Bb and f −1(U ) = Spec( An)b are dense in Y,X respectively, and f :f −1(U )→U is ﬁnite.
3.8 This is a standard application of The F ourfold W ay:
We wish to construct an X-scheme P (X)→ X for every scheme X with P (X) having some universal
property P in some subcategory of the category of X-schemes.
1. Prove that if P (X)→X exists for a single X, then the open subscheme in P (X) that lies over an open
subscheme U of X satisﬁes the universal property to be P (U ); in particular, existence for X implies
existence for any open subscheme of X.
2. Suppose the problem can be solved locally on a single X. That is, assume there is an open cover {Ui} of
X such that P (Ui)→Ui exists. Now consider Pij, the part of P (Ui) that lies over Uij =Ui∩Uj =Uji.
Notice that Pij andPji both satisfy the same universal property in the category of Uij-schemes, by step
1 (applied to the scheme Uij), so they are uniquely Uij-isomorphic, and the uniqueness ensures triple-
overlap consistency when comparing the various triples of isomorphisms we get over triple overlaps.
3. Using step 2, we may (for X and{Ui} as in step 2) glue the P (Ui) to make an X-scheme. Now this
glued X-scheme restricts over Ui to give the universal thing P (Ui)→Ui, and so one then can usually
exploit this to prove that the glued thing over X does in fact satisfy the universal property to serve as
the desired P (X)→X.
4. By steps 1–3, the existence problem for P (X) for any particular X is ”local on the base” (i.e., suﬃces
to solve the problem for the constituents of an open covering of X), and of course the uniqueness aspect
is generally OK by whatever universal property is to be satisﬁed by the construction. Now we may
suppose X is aﬃne and we perhaps make an explicit construction in this case, and thereby solve the
global problem in view of the preceding considerations.
Suppose that π : ~X→X exists and let U⊆X be open. We wish to show that π−1(U )≃ ~U . The scheme
π−1(U ) is normal because it is a subscheme of ~X and normality is a local property. It is integral because it is
reduced (again a local property) and irreducible (because it is an open subscheme of an irreducible scheme).
Moreover, if Z→ U is any normal integral U -scheme with dominant structure map, then Z becomes an
X-scheme with dominant structure map (since U is dense in X), and hence factors uniquely through ~X, and
it is clear that the image lies in p−1(U ), so p−1(U ) has the right universal property and is thus (isomorphic
to) ~U .
Next we show that it suﬃces to solve the existence of normalization locally on X. Indeed, let {Xi} be an
open cover of X and let ~Xi be the normalization of Xi. By 1), we get the normalization of Xij =Xi∩Xj in
two diﬀerent ways: one as a subscheme of ~Xi and the other as a subscheme of ~Xj. The uniqueness (which
11

is an immediate consequence of the universal property) yields an isomorphism φij identifying these two
constructions. Moreover, uniqueness up to unique isomorphism ensures that φjk◦φij =φik (triple overlap
compatibility), so that we can glue the ~Xi to obtain a scheme π : ~X→X.
We wish to show that ~X has the required universal property. Over each Xi, the scheme ~X restricts to
~Xi so given an integral normal scheme φ : Z→ X with dominant structure map, we obtain unique maps
φi :φ−1(Xi)→Xi (which must be dominant by irreducibility considerations) and hence unique factorizations
ψi :φ−1(Xi)→ ~Xi. The uniqueness of these maps ensures compatibility on overlaps, so we may glue them
to show that Z→X factors uniquely through ~X. Moreover, ~X is normal and reduced since ~Xi is for each
i (and these are local properties) and is irreducible since the ~Xi are irreducible and all intersect pairwise
(because ~Xi =π−1(Xi) and the Xi all intersect as X is irreducible).
We have reduced the existence of normalization to the case of aﬃne X = Spec A, with A a domain. Let B
be the integral closure of A in Frac A. Then every localization of B is integrally closed, so Spec B is normal,
and since A→B is injective, the map Spec B→ SpecA is dominant (2.18). If Z→ SpecA is a dominant
map with Z an integral normal scheme, then we have an injective (converse to 2.18 a)) map A→ Γ(Z, OZ) by
2.4. Since Γ( Z, OZ) is normal (as all localizations at prime ideals are) the morphism A→ Γ(Z, OZ) factors
throughB so by 2.4 again, the morphism Z→ SpecA factors through Spec B. This gives the normalization
for aﬃnes, and we are done.
Finally, if X is ﬁnite type over a ﬁeld, then we have a cover Xi = Spec Ai by aﬃnes with π−1(Xi) =
SpecBi withBi integral over Ai, so by Theorem 3.9A of Chapter I, Bi is a ﬁnite Ai-module and π is ﬁnite.
3.9 The ﬁber product X = A1
k×A1
k has the following universal property: to give a k-morphismY→X (with
Y a scheme over k) is to give k-morphisms φ1,φ 2 :Y → A1
k, that is, to give two k-algebra homomorphisms
k[x]→ Γ(Y, OY ). Thus, Hom( Y,X )≃ Γ(Y, OY )2 is a bijection. Since this is the universal property of A2
k, we
conclude that X≃ A2
k. We could also observe that X = Spec( k[x]⊗kk[y])≃ Speck[x,y ]. The underlying
point-set of the product has points that correspond to irreducible curves in A2
k (even if k is algebraically
closed). For example, we might take xy− 1. If such a point p were to correspond to an element of the
product set sp( A1
k)×sp(k) sp(A1
k) it would have to be the point ( i−1
1 (p),i −1
2 (p)) where i1 :k[x]→k[x,y ] and
i2 :k[y]→k[x,y ] are the natural inclusions. But for such p, the contraction of p viaij is (0) for j = 1, 2, so
the sets are not equal (Really I should give a cardinality argument).
b) Since k(s) = S−1k[s] and k(t) = T −1k[t] where S,T are the multiplicative subsets of k[s],k [t] consisting
of all nonzero elements, we have k(s)⊗kk(t) = S−1k[s]⊗kT −1k[t] = ( ST )−1k[s]⊗kk[t] = U −1k[s,t ], where U
is the multiplicative subset of k[s,t ] consisting of all nonzero polynomials P (s)Q(t). Since k[s,t ] and k[s] are
ﬁnitely generated k-algebras, they are Jacobson rings, so maximal ideals contract to maximal ideals under
the inclusion k[s] ↪→ k[s,t ] (see Eisenbud’s Commutative Algebra, Theorem 4.19). Thus, every maximal
ideal m of k[s,t ] contains some nonzero P (s). It follows that the expansion of m under k[s,t ]→U −1k[s,t ]
is the unit ideal. We conclude that the prime ideals of U −1k[s,t ] correspond to the height-1 prime ideals
of k[s,t ] not of the form P (s)Q(t). That is, the prime ideals of U −1k[s,t ] are principal, generated by
some irreducible g∈ k[s,t ]\ (k[s]∪k[t]). There are inﬁnitely many such irreducibles, and it follows that
Spec(U −1k[s,t ])≃ Speck(s)×k Speck(t) has inﬁnitely many points. Moreover, Spec k(s)×k Speck(t) is
1-dimensional as it is the spectrum of a ring in which every prime is principal.
3.10 a) We claim that the ﬁrst projection p :X×Y Speck(y)→X induces a homeomorphism Xy→f −1(y).
Letting Spec A be any aﬃne nbd. of y∈ Y , we see from the universal properties of ﬁber product that
Xy = (X×Y SpecA)×SpecA Speck(y) = ( f −1(SpecA))y, so we may suppose Y = Spec A is aﬃne. For any
open subset U⊆X we have p−1(U ) = U×Y Speck(y) (by universal properties). Moreover, if we can show
that p : p−1(U )→ U induces a homeomorphism Uy→ f −1(y)∩U then we can use universal properties to
glue and obtain the desired result (sketchy). Thus, we reduce to the case that X = Spec B is aﬃne. Let
p∈ SpecA =Y be the point y and let g =f #
Y :A→B be the ring map corresponding to f :X→Y making
B into an A-algebra. We have ring maps B
φ
− →B⊗AAp
ψ
− →B⊗Ak(p), and the projection p is the map
Spec(B⊗Ak(p))→ SpecB corresponding to ψ◦φ. We already know that Spec φ, Spec ψ are continuous.
12

Now ψ is surjective, so by 2.18 c), Spec ψ : Xy → Spec(B⊗A Ap) is a homeomorphism onto the closed
subset V (kerψ). We claim that Spec φ is a homeomorphism onto the set {q∈ SpecB : q∩S =∅}, where
S = g(A−p). (Spec φ is closed since Spec φ(V (I)) = V (φ−1(I))∩ (Specφ)(SpecB) is a closed subset of
the image of Spec φ, which are those primes of B not meeting S). Therefore, p is the composition of two
homeomorphisms and hence a homeomorphism. Since ker ψ =pB, we see that p is a homeomorphism onto
the set of primes q∈ SpecB such that q⊇pB =g(p)B and q∩S =q∩g(A−p) = 0, that is, g−1(q)⊇p
and g−1(q)⊆p, i.e. g−1(q) = p.
b) Assuming k to be algebraically closed, the ﬁber over y = (s−a)∈ Speck[s] consists (by part a) ) of
those primes in k[s,t ]/(s−t2) contracting to ( s−a), that is ( s−a,t−√a) and ( s−a,t +√a). The residue
ﬁeld at each point is k (deﬁned by mapping s→ a and t→±√a). If a = 0, the ﬁber over y = ( s) is the
scheme Spec( k[s,t ]/(s−t2)⊗k[s]k[s](s)/(s)) = Spec( k[s,t ]/(s−t2)⊗k[s]k) where the map k[s]→k sends s
to 0, so s acts on the left of the tensor product as 0. Thus, k[s,t ]/(s−t2)⊗k[s]k≃k[t]/t2 and the ﬁber is the
one-point non-reduced scheme Spec( k[t]/t2). The prime ideals of k[s,t ]/(s−t2) that contract to (0) ⊆k[s]
are those prime ideals of k[s,t ] containing ( s−t2) that contain no polynomials in s. The only such ideal is
(s−t2) (see 3.9 b) ). In other words, k[s,t ]/(s−t2)⊗k[s]k(s)≃ k(s)[t]/(s−t2) (a ﬁeld) so the ﬁber is a
one-point scheme with residue ﬁeld a degree-2 extension of k(s).
3.12 a) Since ϕ is surjective and degree-preserving, we have ϕ(S+) = T+ soU = Proj T . As ϕ is surjective, we
haveS/ kerϕ≃ T so since there is a 1-1 inclusion-preserving correspondence between homogeneous prime
ideals of S that contain ker ϕ and homogeneous prime ideals of S/ kerϕ, we conclude that f : Proj T →
ProjS is a homeomorphism onto V (kerϕ) (ker ϕ is a homogeneous ideal). We need only remark that
f # : OProjS→f∗OProjT is surjective. But this follows from the fact that OProjS(D+(f )) = S(f )→Tϕ(f ) =
OProjT (f −1(D+(f )) is surjective for any f ∈ S since S → T is surjective (equivalently Sϕ−1(p)→ Tp is
surjective for any prime p∈ ProjT , so the sheaf map is surjective on stalks).
b) Observe that ( S/I)d≃ (S/I ′)d for all d≥d0. By 2.14 c), the morphism f : Proj( S/I)→ Proj(S/I ′)
associated to S/I ′ → S/I is an isomorphism that is evidently compatible with the closed immersions
Proj(S/I)→ ProjS and Proj( S/I ′)→ ProjS since the ring maps are.
3.13 a) Let f :X→Y be a closed immersion. Observe that for U⊆Y open, the map f :f −1(U )→U is a
closed immersion (indeed, it is a homeomorphism onto the closed subset f (X)∩U of U and the sheaf map
OY
⏐⏐
U→f∗OX
⏐⏐
f −1(U ) is surjective since it is on stalks). Thus, being a closed immersion is local on the base.
We have already seen that being a ﬁnity-type morphism is local on the base (3.1, 3.3), so we reduce to the
case Y = Spec A whence X≃ SpecA/I. Since A/I is clearly a ﬁnitely generated A-algebra, we conclude
that f is ﬁnite-type.
b) By 3.3 a) it will suﬃce to show that f is locally of ﬁnite type. Let f :X→Y be an isomorphism onto
U⊆ Y and let Spec A be any aﬃne open of Y . Then f −1(SpecA) = f −1(U∩ SpecA), and we may cover
U∩ SpecA by open aﬃnes Spec Aai. Since f :X→U is an isomorphism, f −1(SpecA) is covered by open
aﬃnes isomorphic to Spec Aai, and each Aai is a ﬁnitely generated A-algebra.
c) Let X
f
− →Y
g
− →Z with f,g ﬁnite type, and let {SpecAi} be a covering of Z with g−1(SpecAi) =
∪nj
j=1 SpecBij and Bij a ﬁnitely generated Ai-algebra. By 3.1, f −1(SpecBij) = ∪mij
k=1 SpecCijk with Cijk a
ﬁnite Bij-algebra, and hence a ﬁnite Ai-algebra. Thus, ( g◦f )−1(SpecAi) = ∪j,k SpecCijk is a ﬁnite cover
with Cijk a ﬁnitely generated Ai-algebra for all i,j,k . Thus g◦f is of ﬁnite type.
d) Let f :X→S be an S-scheme and S′→S a base change. Because ﬁnite type is local on the base, we
may assume S = Spec A andS′ = Spec B are aﬃne. Let X =f −1(SpecA) be covered by Spec Ci, with Ci a
ﬁnite A-algebra. Then ( f ′)−1(S′) = X×SS′ is covered by Spec( B⊗ACi), and since Ci is a f.g. A-algebra,
B⊗ACi is a f.g. B-algebra.
e) We may assume S = Spec A is aﬃne. Let Spec Bi and Spec B′
j be ﬁnite covers of X,Y with Bi,B ′
j ﬁnite
A-algebras. Then Spec( Bi⊗AB′
j) is a ﬁnite cover of X×SY and Bi⊗ABj is a ﬁnite A-algebra.
f) Again, we need only check that f is locally ﬁnite type. Cover Z by open aﬃnes Spec Ci with ( g◦
f )−1(SpecCi) covered by ﬁnitely many Spec Aij ⊆ X. Now let Spec Bik be a cover of g−1(SpecAi) and
observe that f −1(SpecBik) is covered by a collection of the Spec Aij, so we have ring maps Ci→Bik→Aij
13

such that Aij is ﬁnite type over Ci, from which we conclude that Aij is ﬁnite type over Bik and hence that
f is locally of ﬁnite type.
g) Let Spec Ai be a ﬁnite cover of Y with Ai noetherian. By 3.1, f −1(Ai) can be covered by ﬁnitely many
SpecBij with Bij a ﬁnite Ai-algebra. Since each Ai is noetherian, so are all the Bij and Spec Bij is a ﬁnite
cover of X with Bij noetherian.
3.14 Let U⊆X be open and let Ui = Spec Ai be an aﬃne cover of X. We claim that x closed in U implies
x closed in Ui for all Ui∋ x. Indeed, pick a basic open Spec B inside Ui∩U containing x so the inclusion
Ui∩U ↪→Ui gives a ring homomorphism Ai→B. Both Ai and B are ﬁnitely generated k-algebras, hence
Jacobson rings, so maximal ideals contract to maximal ideals (c.f. 3.9). In particular, since x is closed in
Ui∩U , its image in Ui is closed. Since x is closed in each Ui and the Ui cover X, we conclude that x is
closed in X.
Thus it suﬃces to prove that every nonempty basic open subset of an aﬃne Spec A contains a maximal
ideal of A. But if f ∈ A is in every maximal ideal then it is nilpotent (as A is Jacobson) hence D(f ) is
empty.
As an example where this fails, let R be any local domain (for example, Z(3)). Then if f∈m\{ 0}, the
set D(f ) is nonempty and open, and contains no closed points.
3.15 a) We have ( iii) = ⇒ (i) = ⇒ (ii), so we show ( ii) = ⇒ (i) = ⇒ (iii). We claim that if K/k is
purely inseparable, then X irreducible implies XK irreducible. Indeed, if XK is not irreducible, then there
is an open aﬃne subset UK⊂XK with Γ( UK, OXK ) not a domain (take UK to be the union of two disjoint
open aﬃnes V1,V 2⊆ XK). Since Spec A is homeomorphic to Spec Ared, it will suﬃce to show that if A
is a domain so is A⊗kK for any purely inseparable extension K/k. But A⊗kK having a zero-divisor is
equivalent to a system of equations with coeﬃcients in k having a solution over K. We may suppose that
K/k is ﬁnite since any element of A⊗kK is contained in A⊗kL withL a ﬁnite extension of k. Thus, there
exists q = (char k)r for some r such that Kq⊆k. Letting {fi} be our system of equations with a solution
in K, we see that {fq
i} has s solution in k, and since x↦→ xq is injective, we obtain a zero-divisor in A,
contradicting our assumption.
We now prove that if k′/k is an extension of ﬁelds with k algebraically closed then {fj} with fj ∈
k[X1,...,X n] has a solution over k iﬀ it has one over k′. One direction is clear. For the opposite direction,
we prove the contrapositive. By the Nullstellensatz (crucially using that k is algebraically closed) if {fj}
has no solution over k then the fj generate the unit ideal of k[X1,...,X n], and hence they also generate the
unit ideal of k′[X1,...,X n] and therefore have no solution over k′.
Lastly, we show that ( i) = ⇒ (iii). We may suppose that K is an extension of k. Then having a zero
divisor in A⊗kK is equivalent to a system of equations with coeﬃcients in k having a solution over K, and
by the above result, such a system also has a solution over k whence A⊗kk is not a domain.
b) Obviously ( iii) = ⇒ (i) = ⇒ (ii), so it will suﬃce to prove ( ii) = ⇒ (i) = ⇒ (iii). We claim that
if K/k is separable then X reduced implies XK reduced. Indeed, we may suppose that X = Spec A is
aﬃne (for it suﬃces to show that UK is reduced for every aﬃne U⊆X) and we must therefore show that
Γ(UK) = A⊗kK is a reduced ring given that A is reduced. We may suppose that A is a domain: indeed,
A ↪→ ∏A/pi, so A⊗kK ↪→ ∏A/pi⊗kK as K/k is ﬂat, the product being over all minimal primes of A,
and a product of rings is reduced iﬀ each factor is. (We have also tacitly used that tensor product commutes
with ﬁnite direct products= ﬁnite direct sums, which employs the ﬁnite type hypothesis, i.e. that A has
ﬁnitely many minimal primes.) Since A↪→ Frac(A), it will suﬃce to show that F⊗kK is reduced for every
extension ﬁeld F/k . We may replace K by a ﬁnite extensionL/k since every element of F⊗kK is contained
in F⊗kL for some ﬁnite L (depending on the element). But then L≃k[T ]/(f ) with f∈k[T ] a separable
polynomial, so that F⊗kL≃F [t]/(f ) and f∈F [t] is still separable, so F [t]/(f ) is reduced. Since k/kp is
a separable extension, we have shown ( ii) =⇒ (i).
Now we show that if A⊗k k is reduced, then A⊗k K is reduced for any extension K/k of ﬁelds. We
reduce at once (by a further ﬁeld extension if necessary) to the case that K is an extension of k. But then
14

having a nilpotent element of A⊗kK is equivalent to giving a system of equations with coeﬃcients in k that
have a solution over K, and by the result in part a), must therefore have a solution over k.
c) Let k = Fp(T ) and K = Fp(T 1/p). Then Spec K is reduced but not geometrically reduced as Spec K×k
SpecK = Spec(K⊗kK) and K⊗kK has the nonzero nilpotent x = 1⊗T 1/p−T 1/p⊗1 with xp = 0. Similarly,
X = Spec R[x]/(x2 + 1) ≃ Spec C is irreducible (it is a single point) but not geometrically irreducible as
XC = Spec C[x]/(x2 + 1) = Spec( C⊕ C) = Spec C ∐ Spec C.
2.4
4.1 Let f : X→ Y be ﬁnite. Since properness is local on the base (cor 4.8), we may assume Y = Spec A
and f −1(Y ) = X = Spec B with B a ﬁnite A-module (since f is ﬁnite; c.f. 3.4). By Prop. 4.1, f :X→Y
is separated and it is of ﬁnite type since it is ﬁnite. We need to check that f ′ :X×Y Y ′→Y ′ is closed for
allY ′→Y . Since this is local on Y , we may suppose that Y ′ = Spec C is aﬃne. We are reduced to showing
that Spec B⊗AC→ SpecC induced by the map C→B⊗AC to the second factor is closed. But B⊗AC is
integral over C as B is integral over A (generated as a C module by gi⊗ 1 with gi a ﬁnite set of A-module
generators of B), so by 3.5 b), f ′ is closed and f is universally closed. Thus, f is proper.
4.2 Let h = (f,g ) : X→Y×SY . Observe that ( f,f ) = ∆ ◦f :X→Y×SY agrees with h on the open dense
subset U Since Y is separated, ∆ : Y →Y×SY is a closed immersion, so ∆ Y is closed. Thus, h−1(∆(Y ))
is a closed subset of X containing U (since h
⏐⏐
U = ∆ ◦f
⏐⏐
U ), and since U is dense, h−1(∆(Y )) = X, so
h(X)⊆ ∆(Y ) so f =g on X.
To check the sheaf maps are equal, we may suppose X = Spec B and Y = Spec A are aﬃne (since
equality of sheaf maps can be checked locally) and we have maps f #,g # : A→ B. For a∈ A consider
b = f #(a)−g#(a). Observe that b
⏐⏐
U = 0 so V (b)⊆ X contains the dense open U and hence V (b) = X.
Thus,b is nilpotent. Since X is reduced, b = 0 and we are done.
If X is nonreduced, this can fail. For example, take X = Spec Z[x]/(x2,xp ) for a prime p. We deﬁne
φi :X→X for i = 1, 2 by x↦→x, x↦→ 0 respectively. The open set U =X(p) = Spec Z[1/p] is dense in X
since X is irreducible (the unique minimal prime is ( x)) and φ1 =φ2 on U . However, φ1⁄=φ2 as they are
not induced by the same ring map.
Similarly, the result can fail for Y not separated. Take Y to be the aﬃne line with doubled origin and
let φ1 : Y → Y be the identity map and φ2 : Y → Y the map that switches the two copies of A1. Then
φ1 =φ2 on the dense open U consisting of Y minus the two origins, but not on all of Y .
4.3 Let f : X → S = Spec A be separated, and U = Spec B, V = Spec B′ aﬃne opens in X. Then
∆ : X→X×SX is a closed immersion, and by universal properties of the ﬁber product, we have U∩V =
∆−1(U×SV ). Since being a closed immersion is local, ∆ : U∩V →U×SV = Spec( B⊗AB′) is a closed
immersion, so in particular by 3.11 b), ∆( U∩V ) is aﬃne, which implies that U∩V is aﬃne as ∆ is a
homeomorphism.
As an example when this fails if X is nonseparated, let X be the aﬃne plane with the origin doubled
(over an algebraically closed ﬁeld k) and U,V the two copies of A2
k. Then U,V are open aﬃnes, but their
intersection is isomorphic to A2
k with the origin deleted, which is not aﬃne.
4.4 Let πX :X→S and πY :Y →S be the structure maps, and πZ :Z→S =πZ
⏐⏐
Z. Since πY◦f|Z =πZ
and πZ is proper by hypothesis and πY is separated, Prop. 4.8 tells us that f
⏐⏐
Z : Z→ f (Z) is proper.
Replace X by Z and Y by f (Z) so that we have f : X→ Y a surjective S-morphism and πX proper; we
wish to show πY is proper. Since X×Y Y×ST =X×ST for any S-schemeT , we see that the morphism
f× id : X×ST→Y×ST is the base change of f :X→Y andX×ST→T is the base change of X→S.
Thus, since properness and surjectivity are stable under base change (see below), we may replace X by
X×ST ,Y byY×ST ,S byT , and f byf× id to reduce showing that f is universally closed to just showing
that it is closed. But if W⊆Y is closed, then since f :X→Y is surjective, we have W =f (f −1(W )) and
15

hence πY (W ) = πY◦f (f −1(W )) = πX (f −1(W )) and this is closed since πX is proper (hence closed) and f
is continuous so f −1(W ) is closed.
To prove that surjectivity is stable under base change, observe that if f :X→S is a surjective map and
π :S′→S any base change, then ( f×1)−1(s′) is homeomorphic to X×SS′×S′ Speck(s′) = X×S Speck(s′) =
X×S π(s′), which is homeomorphic to f −1(π(s′)) and must therefore be nonempty as a set, since f is
surjective (we have used 3.10).
4.6 Let f : Spec B =X→Y = Spec A be proper, and let ϕ :A→B be the associated ring map. Since X,
Y are varieties, A andB are domains of ﬁnite type over an algebraically closed ﬁeld k. Let K = Frac B and
R be any valuation ring of K containing ϕ(A). The valuative criterion of properness ensures the existence
of a unique map Spec R→ SpecB making the diagram
SpecK /d47/d47
/d15/d15
SpecB
/d15/d15
SpecR
/d57/d57/d115/d115/d115/d115/d115 /d47/d47SpecA
commute. In other words, there is a unique map of rings B→R making
A /d47/d47
/d15/d15
R/d127 /d95
/d15/d15
B
/d62/d62/d126/d126/d126/d126/d31 /d127 /d47/d47K
commute, and we easily see this map is injective. Thus, B is contained in every valuation ring of K containing
A, so by 4.11 A, it is contained in the integral closure of A in K and is hence integral over A. By 3.4, we
conclude that f :X→Y is ﬁnite.
4.8 d) If πX : X→ Z and πY : Y → Z have P then since X×Z Y → Y is the base change Y → Z of
X→ Z, we see that X×Z Y → Y has P. SInce X×Z Y → Z is the composition X×Z Y → Y
πY
−−→Z of
two morphisms having P, it also has P.
e) The morphism Γ f :X→X×ZY is the base change of ∆ : Y→Y×ZY byf× id : X×ZY→Y×ZY ,
and since Y is separated, ∆ is a closed immersion. Since closed immersions are stable under base change,
Γf is also a closed immersion, hence has P. Now g◦f : X→ Z has P so the base change X×Z Y → Y
by Y → Z also has P. But f factors as X
Γf
− − →X×Z Y → Y and so is the composition of two morphisms
having P and therefore has P.
f) The morphism Xred→ X is a closed immersion, hence has P. Then the composite Xred→ X→ Y has
P and factors as Xred→ Yred→ Y by 2.3 c). Since Yred→ Y is separated (use the valuative criterion:
T = Spec R is reduced for any valuation ring R as valuation rings are domains, so the map Spec R→ Y
factors uniquely as Spec R→Yred→Y by 2.3) we conclude by e) that Xred→Yred has P.
2.5
5.1 a) Deﬁne a map ϕU : E(U ) → ˇˇE(U ) = Hom( H om(E, OX )
⏐⏐
U, OX
⏐⏐
U ) by sending e ∈ E(U ) to the
collection of maps {eV}V : Hom( E, OX )(U∩V )→ OX (U∩V ), with eV (σ) = σU ∩V (e
⏐⏐
U ∩V ), where σ :
E
⏐⏐
U ∩V → OX
⏐⏐
U ∩V . One checks that the stalk H om(E, OX )P is Hom( EP, OX,P ) (because E is coherent;
see, for example, Serre, “Faisceux Alg´ ebraiques Coh´ erents.” In general, the canonical map Hom( E, OX )P→
Hom(EP, OX,P ) is not an isomorphism.), and that the morphism we have deﬁned induces the stalk morphism
EP→ Hom(Hom(EP, OX,P ), OX,P ) given by eP↦→ (σP↦→σP (eP )). Since E is locally free of ﬁnite rank, the
stalk EP is free of ﬁnite rank, and the stalk map is the canonical isomorphism of a free module of ﬁnite rank
with its double dual. Since all of the induced stalk maps are isomorphisms, we have ˇˇE≃ E.
16

b) Deﬁne ϕU : Hom( E
⏐⏐
U, OX
⏐⏐
U )⊗ F(U )→ Hom(E
⏐⏐
U, F
⏐⏐
U ) by ( ϕU (ψ⊗f ))V (e) = ψV (e)·f
⏐⏐
V ∈ F(U∩V ),
where ψ ={ψV} and e∈ E(U∩V ). We extend this deﬁnition linearly. Observe that the restriction maps
are compatible and that the ϕU glue to give ϕ, since they are all canonically deﬁned. On stalks, ϕP is the
map Hom( EP, OX,P )⊗ FP → Hom(EP, FP ) given by ψ⊗f↦→ (e↦→ ψ(e)·n), which is an isomorphism of
OX,P -modules since EP is free (this is standard commutative algebra). Thus the map ϕ is an isomorphism.
c) Let ϕ : E⊗ F→ G and deﬁne F (ϕ) : F→ H om(E, G) by F (ϕ)V (f ) = {σW} where σW : E
⏐⏐
V (W )→
G
⏐⏐
V (W ) is e↦→ϕV ∩W (θ+(e⊗f
⏐⏐
W ∩V )), with θ+ : E(U )⊗F(U )→ (E⊗F)(U ) the sheaﬁﬁcation map. It is easily
checked that F (ϕ) is a map of sheaves of modules, so F gives a map Hom( E⊗ F, G)→ Hom(F, H om(E, G)).
We claim that F is injective. Indeed, if F (ϕ) = 0 then ϕV ∩W (θ+(e⊗f )) = 0 for all open V,W and
e⊗f∈ E(V∩W )⊗ F(V∩W ), which implies that ϕ is the zero map. Moreover, F is surjective as given
ψ : F→ H om(E, G) we deﬁne ϕU : E(U )⊗ F(U )→ G(U ) by ϕU (e⊗f ) = ( ψU (f ))U (e)∈ G(U ). It is
clear this deﬁnes morphism of sheaves (using the universal property of sheaﬁﬁcation) E⊗ F→ G such that
F (ϕ) = ψ. Surjectivity follows.
d) Let’s try to be slick about this: We have the identiﬁcation f∗F⊗OY E≃ f∗F⊗OY
ˇˇE by part a) and
f∗F⊗OY
ˇˇE≃ H om OY (ˇE,f ∗F) by part b). Using the canonical isomorphism
HomOX (f ∗G, F)≃ HomOY (G,f ∗F),
by patching together over opens we obtain an isomorphism of sheaves of OY -modules
H om OY (G,f ∗F)≃f∗H om OX (f ∗G, F).
Now let G = ˇE and combine with the above to obtain
f∗F⊗OY E≃ H om OY (ˇE,f ∗F)≃f∗H om OX (f ∗( ˇE), F)≃f∗(F⊗OX
ˇf ∗ ˇE),
where we have used b) again. Now we need only realize the isomorphism ˇf ∗ ˇE≃f ∗ ˇˇE of sheaves on X and
use part a). Observe that the two duals on the LHS are diﬀerent: the inner one is H om(•, OY ) while the
outer one is H om(•, OX ).
5.2 a) As R is a dvr, there are two open sets: X and{0} = D(m) for any m∈ P where P is the unique
nonzero prime ideal of R. As such, to give a sheaf of modules on X is to give a R-moduleM and a Rm =K-
module (vector space) L such that the restriction map M→ L is compatible with the module structures
R→ EndM and K→ EndL, i.e. such that we have a homomorphism of K-vector spaces M⊗RK→L.
b) The sheaf given above is quasi-coherent iﬀ, by 5.4, it is of the form ~M , in which case we must have
Mm =M⊗RK =L, with the map given above (coming from restriction) providing an isomorphism.
5.3 Let ϕ :M→ Γ(X, F) be an A-module homomorphism and for any f∈A deﬁne ψD(f ) :Mf→ F(D(f ))
byψD(f )(m/fn) = (1 /fn)·ϕ(m)
⏐⏐
D(f ). Observe this is well deﬁned since F(D(f )) is an Af -module, and that
the ψD(f ) patch together to give a morphism ψ : ~M → F (as is easily checked by looking at the double-
overlap condition). Given ψ∈ Hom( ~M, F) we deﬁne ϕ :M→ Γ(X, F) by ϕ =ψX . It is clear that these two
constructions provide inverses to eachother, so provide the desired isomorphism.
5.4 If F is quasi-coherent, then every point x∈ X has an aﬃne nbd. Spec A = U with F
⏐⏐
U≃ ~M for some
A-module M . Then M has presentation AI→ AJ→ M ; applying ~ and recalling that this is an exact
functor that commutes with arbitrary direct sum and that ~A = OX
⏐⏐
U , we obtain the exact sequence of
sheaves of modules
(OX
⏐⏐
U )I→ (OX
⏐⏐
U )J→ F
⏐⏐
U→ 0.
Observe that if F is coherent and X is noetherian, then A is a noetherian ring and M is a ﬁnitely generated—
hence ﬁnitely presented—module. We may therefore take the index sets I and J to be ﬁnite in this case.
17

Conversely, suppose that F
⏐⏐
U is the cokernel of the morphism
~An = ( OX
⏐⏐
U )I ϕ
− →(OX
⏐⏐
U )J.
Applying 5.3 to this morphism, we obtain an A module homomorphism ψ : AI→ AJ with ~ψ = ϕ. Thus,
letting M = coker ψ and applying ~ to the exact sequence AI ψ
− →AJ → M → 0, we obtain an exact
sequence of sheaves
(OX
⏐⏐
U )I ϕ
− →(OX
⏐⏐
U )J→ ~M→ 0.
Now use the snake lemma to obtain ~M≃ F
⏐⏐
U . If I,J are ﬁnite index sets and A is noetherian, then M is
ﬁnitely generated and hence F
⏐⏐
U is coherent.
5.5 a) Let X = Spec k[x,y ] and Y = Spec k[x] with f : X→ Y induced by the inclusion k[x] ↪→ k[x,y ].
Then f∗OX is not a coherent OY -module. Indeed, k[x,y ] is not a ﬁnitely generated k[x]-module; now use
Prop. 5.4.
b) Let f : X → Y be a closed immersion, and U = Spec A an aﬃne subset of Y , and V = f −1(U ).
Then f (V ) = U∩f (X) is a closed subset of U since f (X) is closed in Y , so by Corollary 5.10 we have
f (V )≃ SpecA/I for some ideal I of A. Since f : V → f (V ) is a homeomorphism, we conclude that
V = Spec B is aﬃne and since f # is surjective, that A/I→B is surjective. Hence A→B is surjective and
B is a ﬁnite A-module (generated by 1); thus f is ﬁnite.
c) Let f :X→Y be ﬁnite and F a coherent sheaf on X. By Prop. 5.4, f∗F is coherent on Y iﬀ for any aﬃne
U = Spec A, the restricted sheaf f∗F
⏐⏐
U is ~M for some ﬁnite A-moduleM . Since f is ﬁnite, f −1(U ) = Spec B
withB a ﬁnite A-module, and since F is coherent, we have F
⏐⏐
f −1(U )≃ ~M for some ﬁnite B-moduleM . Prop
5.2 (d) says that f∗F
⏐⏐
U≃ ~(AM ). Since B is a ﬁnite A-module and M is a ﬁnite B-module, M is a ﬁnite
A-module and hence f∗F is coherent.
5.6 a) By deﬁnition, Supp m ={x∈ SpecA : mx⁄= 0} ={p⊆ A : mp⁄= 0}. But mp = 0 iﬀ there exists
f⁄∈p with fm = 0, that is, iﬀ Ann m ⊊p. Hence Supp m =V (Annm).
b) Recall Supp F ={x∈X : Fx⁄= 0} =∪m∈MV (Annm) by part a). Since M is ﬁnitely generated, say by
m1,...,m n, we have ∪m∈MV (Annm) = ∪n
i=1V (Annmi) = V (∩n
i=1 Annmi) = V (AnnM ). (where did I use
the hypothesis that A is noetherian?
c) Let U = Spec A be any open aﬃne subset of X. By Prop. 5.4, we have F
⏐⏐
U = ~M with M a ﬁnitely
generatedA-module. By part b), Supp F∩U = Supp F
⏐⏐
U =V (AnnM ) is closed in U . It follows that Supp F
is closed (take Ui a ﬁnite aﬃne cover of X since X is noetherian; then Supp F =∪ Supp F∩Ui is closed).
Perhaps this only shows locally closed?
d) By 1.20, we have the exact sequence of sheaves on X
0→ H 0
Z (F)→ F→j∗(F
⏐⏐
U ),
where j∗ :U =X−Z→X is the inclusion. By Prop. 5.8, j∗(F
⏐⏐
U ) is quasi-coherent since X is noetherian.
By Prop. 5.7, H 0
Z is quasi-coherent since it is the kernel of a morphism of quasi-coherent sheaves. Now
ΓZ(F) = {m∈M : Supp m⊆V (a)} ={m∈M :V (Annm)⊆V (a)}
={m∈M : a⊆ Rad(Annm)} ={m∈M : anm = 0 for some n}
since A is noetherian, and hence a is ﬁnitely generated. Thus, Γ Z(F) = Γ a(M ). But since H 0
Z (F) is
quasi-coherent and Γ Z(F)≃ Γa(M ), Cor. 5.5 allows us to conclude that H 0
Z (F)≃ ~Γa(M ).
e) Let U = Spec A be any aﬃne. Then Z∩U is closed in U so is isomorphic to Spec A/a for some ideal a
(by Cor. 5.10), i.e. Z∩U =V (a). If F is quasi-coherent, we have F
⏐⏐
U≃ ~M by Prop. 5.4, and by part d)
we have H 0
Z (F)
⏐⏐
U≃ ~Γa(M ). It follows that H 0
Z (F) is quasi-coherent. If F is coherent, then M is a ﬁnitely
18

generated A module, so Γ a(M ) is a ﬁnitely generated A-module since A is noetherian so it is a submodule
of a noetherian module.
5.7 a) Let U = Spec A be a nbd. of x with F|U≃ ~M , with M a ﬁnite A-module, generated by m1,...,m n.
Then the images of mi in Fx generate Fx≃Mx as an Ax-module. Renumbering if necessary, we may assume
that (the images of) m1,...,m v generate Fx freely, and we replace M by the submodule generated by the
mi. Because X is noetherian, A is noetherian and M is ﬁnitely presented, so let nj for 1 ≤j≤m be a basis
for the module of relations. Since the images of mi in Fx generate freely, the image of each ni in Fx is zero,
so there is an open set Vi such that ni
⏐⏐
Vi
= 0 for each i. Let V =∩Vi; since there are ﬁnitely many ni, V
is a nbd of x which we may take to be a basic aﬃne open contained inside U . Then F
⏐⏐
V is generated freely
by the global sections mi.
b) One direction is obvious, and the converse is part a).
c) Suppose ﬁrst that F is locally free of rank 1. Then by 5.1 b) we have F⊗OX
ˇF≃ H om OX (F, F). We
deﬁne an isomorphism H om OX (F, F)≃ OX as follows: cover X by open aﬃnes Ui with F
⏐⏐
Ui
≃ OX so
H om OX (F, F)(Ui) = Hom OX (OX
⏐⏐
Ui
, OX
⏐⏐
Ui
), and we let ϕUi(ψ) = ψUi(1) with ψ : OX
⏐⏐
Ui
→ OX
⏐⏐
Ui
. This
gives a map H om OX (F, F)→ OX that is an isomorphism on each Ui, hence an isomorphism and F is
invertible. One easily checks that ˇF is coherent by looking locally and translating it into a question about
modules.
Conversely, suppose there exists G such that F⊗OX G≃ OX . Then ( F⊗OX G)x = Fx⊗OX,x Gx≃ OX,x for
allx∈X, so by part b) it is enough to show that if M,N areA-modules with ( A,m,k ) a local ring (here I am
using that F, G are coherent) and M⊗AN≃A then M≃A and N≃A. Indeed, we have an isomorphism
(this is tricky commutative algebra) M/mM⊗kN/nM≃ (M⊗A⊗N )⊗Ak≃k, so M/mM (and N/mN )
has rank 1; by Nakayama’s lemma, M is a rank 1 A-module. Let a∈ AnnM . Then a annihilates A since
M⊗AN≃A, and in particular, a· 1 = 0 so a = 0 and M is free of rank 1.
5.8 a) We show the complement is open. Let x∈X satisfy ϕ(x) = k <n and choose a nbd. U = Spec A of
x with F
⏐⏐
U≃ ~M with M a ﬁnitely generated A-module, generated by m1,...,m r. Since Fx⊗OX,x k(x)≃
Mp/pMp where p∈ SpecA corresponds to x∈ X, we may take ui ∈ M for 1 ≤ i≤ k with images a
generating set of Mp/pMp as a k(x) vector-space. NAK implies that the images of the ui generate MP as
anAp-module. Writing mj = ∑aij/fijui for each j (insideMp) and f = ∏
i,jfij, we see that p∈D(f ) and
if q∈D(f ) then mj∈Mq can be written as an Aq-linear combination of the (images of) ui. Since the mj
generate M as an A-module, their images generate Mq as an Aq-module, so the images of ui for 1 ≤i≤k
generate Mq as an Aq module whence ϕ(q)≤k<n . Observe that by taking n =k we have shown that the
sets{x :ϕ(x)<n} and{x :ϕ(x)≤n} are open (which follows anyway from the fact that Z is discrete).
b) If F is locally free, then U =ϕ−1(n) = {x :ϕ(x) = n} is open. Indeed, let x∈U . By 5.7 a), there is a
nbd V of X with F
⏐⏐
V free, necessarily of rank n, so for every y∈V we have ϕ(y) = n so U is open. Since
ϕ(x)≥ 0, we may ﬁnd x∈ X with ϕ(x) = n≥ 0 minimal. Then {x : ϕ(x) > n} =∪k>nϕ−1(k) is open
by the above and closed by part a). and since X is connected it is either empty or all of X. The latter
possibility is ruled out since we have one point x with ϕ(x) = n. Thus ϕ(y)≤n for all y∈X, and since n
was chosen minimally, we conclude that ϕ(y) = n for all y∈X.
c) Let U = Spec A be a nbd. of x∈ X with ϕ(x) = n and F
⏐⏐
U = ~M . By 5.7 b) it will suﬃce to show
that Mp is a free Ap-module for all p. Pick m1,...,m n∈ M whose images are a basis of Mp/pMp as an
Ap/p-vector space. By NAK, m1,...,m n generate Mp as an Ap-module, and thus also generate Mq as an
Aq-module for any q⊆ p; since ϕ(q) = ϕ(p), we must have that the images of m1,...,m n in Mq/qMq are
linearly independent over Aq/q for all q⊆p. Thus, if ∑aimi = 0 is any relation with ai∈Ap, then we have
ai = 0 in Aq/q for all q⊆p, or what is the same thing, that ai∈∩ q⊆pq. But as X is reduced, Ap is reduced,
so∩q⊆pq = 0 so ai = 0 and the mi are linearly independent over Ap so Mp is a free Ap-module.
5.10 a) Let s = ∑fj be in I with fj∈Sj. Then xn
is = ∑xn
ifj∈I so since I is homogeneous, xn
ifj∈I
for all i,j and hence I is homogeneous.
19

b) Two ideals I,J deﬁne the same closed subscheme iﬀ ~I = ~J, as subsheaves of OX . That is, iﬀ I(xi) =
~I(D+(xi)) = ~J(D+(xi)) = J(xi). Now I(xi) =J(xi) for all i iﬀ for any s∈I, there exists an integer m (which
we can take to be positive) such that xm
i s∈J, that is, s∈J. Indeed, s∈I iﬀ. xn
is∈I for some n and all
i iﬀ s∈ Ixi for all i. This is the case iﬀ there exists m∈ Z such that xm
i s∈ I(xi). Thus, I(xi) = J(xi) iﬀ
xk
is∈J for some k> 0, i.e. iﬀ s∈J. Interchanging the roles of I,J gives the desired result.
c) Observe that
Γ(X, IY (n)) = {s∈ Γ(X, OX (n)) = Sn :sp = 0 for all p∈Y}.
Thus, if s∈ Γ∗(IY ) then there exists m> 0 with ( xm
i s)p = 0 in Sp for all p∈Y , or ehat is the same thing,
there exists fi∈S−p withfixm
i s = 0 in S. Since xi generateS+, given any p∈Y , we can ﬁnd i such that
xi⁄∈p and hence fixm
i ∈S−p, whence sp = 0 so s∈ Γ∗(IY ).
d) This follows immediately from a)–c).
5.11 We assume S,T are generated by S1,T 1 overA. Let S1 be generated by s1,...,s a overA and T1 by
t1,...,t b overA. We claim there is an isomorphism of rings ( not a graded isomorphism)
S(si)⊗AT(tj )≃ (⊕d≥0Sd⊗Td)si⊗tj
.
Indeed, S(si)⊗AT(tj ) =⊕m,n(Sm)(si)⊗ (Tn)(tj ) and (⊕d≥0Sd⊗Td)si⊗tj
=⊕d≥0(Sd)(si)⊗ (Td)(tj ), and the
map ( Sm)(si)⊗ (Tn)(tj )→ (Sn)(si)⊗ (Tn)(tj ) is deﬁned (say for n≥m) by
s
sm
i
⊗ t
tn
j
↦→ s·sn−m
i
sn
i
⊗ t
tn
j
on simple tensors and extended by A-linearity. This gives the claimed isomorphism since the two sides of
the map are already equal inside S(si)⊗T(tj ). We thus have an isomorphism of aﬃne schemes
D+(si)×AD+(tj)≃ Spec(S(si)⊗T(tj ))
∼
← −Spec((S×AT )si⊗tj )≃D+(si⊗tj),
and these glue in the evident manner to give an isomorphism Proj( S×AT )→ ProjS×A ProjT .
5.15 a) By Prop 5.4, any quasi-coherent F has the form F = ~M for some A-module M (with Spec A = X
and A noetherian). Then the natural map lim−→αMα→M is an isomorphism, where {Mα}α are the ﬁnitely
generated submodules of M . Since the ~ operation commutes with direct limit (because tensor product
does) and is exact, we see that the natural map lim −→~Mα→ ~M is an isomorphism.
b) The sheaf i∗F is q-coh. by 5.8 c) since X is noetherian, so part a) applies. We claim that there is a
coherent subsheaf Fα ofi∗F with Fa
⏐⏐
U = F. Indeed, the sheaves Fα
⏐⏐
U are all subsheaves of the coherent sheaf
F, so any chain of these sheaves is bounded above (by a coherent sheaf!). Zorn’s lemma yields a maximal
subsheaf Fa
⏐⏐
U⊆ F and we claim equality holds. If not, there is some point P with ( Fa)P⁄= FP and hence
an open set V contained in U with Fa(V ) ⊊ F(V ), and we can take V small enough so that F
⏐⏐ = ~M and
Fa
⏐⏐
V = ~N with N ⊊ M and N,M f.g. O(V )-modules. Pick m∈ M\N and let N ′ be the O(V )-module
generated by m,N . Then ~N ′ is a coherent subsheaf of F strictly containing Fa as a subsheaf, contradicting
the maximality of Fa.
c)
2.7
7.1 Passing to stalks, we are reduced to the following: if ϕ :M→N is a surjective map of free A-modules
of rank 1 (with ( A,m,k ) local) then it is an isomorphism. By tensoring M→ N→ 0 with k, we see that
ϕ⊗ 1 is a surjective map of k vector spaces of the same dimension, hence an isomorphism. Thus, if x∈ kerϕ
20

then x⊗ 1 = 0, or what is the same, x∈ Mtors. But since M is free, we conclude that ker ϕ = 0 so ϕ is
an isomorphism. By identifying M,N with A (thought of as an A-module) One could also use a diﬀerent
result (cf. Matsumura, Th. 2.4) which states that for any ring A and any ﬁnite A-module M , any surjective
f :M→M is an isomorphism.
7.2
21

Chapter 3
3.2
2.3 a) Let 0 → F′ → F→ F′′ → 0 be exact. We know that 0 → Γ(X, F′)→ Γ(X, F)→ Γ(X, F′′) is
exact, so it follows that Γ Y (X, F′) ↪→ Γ(X, F). The image is contained in the subgroup Γ Y (X, F) because
the sequence on stalks 0 → F′
P → FP → F′′
P is exact for all P , so s∈ ΓY (X, F′) has nonzero stalk at
P iﬀ its image in Γ( X, F) has nonzero stalk at P . For this reason, the map Γ( X, F)→ Γ(X, F′′) induces
ΓY (X, F)→ ΓY (X, F′′). Now it is clear that the map Γ Y (X, F′)→ ΓY (X, F)→ ΓY (X, F′′) is the zero map
as it is induced by the map of usual global sections. It therefore remains to show that is s∈ ΓY (X, F) maps
to 0 in Γ Y (X, F′′) then it is in Γ Y (X, F′). We know that it is in the image of Γ( X, F′), and checking the
sequence on stalks shows that it is in Γ Y (X, F′) as required.
b)
3.3
3.1 If X = Spec A thenXred = Spec A/N is aﬃne, where N is the nilradical. Conversely, suppose that Xred
is aﬃne, and let N be the sheaf of nilpotents on X and F any quasi-coherent sheaf on X. Then for any j
we have an exact sequence
0→ N j+1· F→ N j· F→ N j· F/N j+1· F→ 0.
Observe that N j· F/N j+1· F is a q-coh. sheaf of OX/N -modules, i.e. a q-coh sheaf of modules on Xred.
Using Serre’s criterion, we may suppose that Hi(X, N j· F/N j+1· F) = 0 for all i≥ 1, and the long exact
sequence of cohomology associated to the short exact sequence above yields an isomorphism Hi(X, N j·F)≃
Hi(X, N j+1· F) for all j≥ 0 and all i≥ 2, and a surjection H 1(X, N j+1· F)→H 1(X, N j· F). Since X is
noetherian, we may cover it by ﬁnitely many aﬃnes Spec Ai with Ai noetherian and N j⏐⏐
SpecAi
= ~Nj
i with
Ni the module of nilpotents on Ai. By the Noetherian hypothesis, we can ﬁnd ji such that Nji
i = 0 for each
i and choosing j = max iji, we ﬁnd that N j is the zero sheaf on X and hence all the cohomology vanishes.
Thus, using the isomorphisms above and our surjection on H 1’s, we conclude that Hi(X, F) = 0 for all i> 0
and any q-coh. F, and hence that X is aﬃne,
3.2 Since X is noetherian, there are ﬁnitely many irreducible components, say Yi for q≤i≤n. Let Ii be
the ideal sheaf deﬁnining Yi and ﬁlter a q-coh sheaf F on X as
F⊃ I1· F⊃ I1I2· F⊃···⊃ I1I2··· In· F.
Breaking into short exact sequences
0→ I1··· Ik· F→ I1··· Ik−1· F→ I1··· Ik−1· F/I1··· Ik· F→ 0,
22

and the quotient sheaf I1··· Ik−1· F/I1··· Ik· F is a q-coh. sheaf of OX/Ik-modules, i.e. a q-coh sheaf
on Yk. The long exact cohomology sequences and the assumption that all the irreducible components are
aﬃne yields isomorphisms
Hi(X, F)≃Hi(X, I1··· In· F)
for all i> 1 and a surjection H 1(X, I1··· In· F) ↠H 1(X, F). However, I1··· In is the zero sheaf on X
because its support consists of those points P∈X not contained in any irreducible component. We conclude
by Serre’s criterion that X is aﬃne. The converse follows from the fact that a closed subscheme of an aﬃne
scheme is aﬃne.
3.3 a) Let 0 →M ′→M→M ′′→ 0 be an exact sequence of A-modules. Since Γ a(M ′) is a submodule of
M ′, we have Γ a(M ′) ↪→ Γa(M ). Moreover, since φ : M ′→ M is a homomorphism of A-modules, we have
φ(anm′) = anφ(m′) so if m′∈ Γa(M ′) then φ(m′)∈ Γa(M ). For the same reason, the image of Γ a(M )
under M → M ′′ is contained in Γ a(M ′′), and since M ′→ M → M ′′ is the zero map, its restriction to
Γa(M ′)→ Γa(M ′′) is zero. It remains to show that if m∈ Γa(M ) maps to zero in Γ a(M ′′) then it is in the
image of Γ a(M ′)→ Γa(M ). But if m↦→ 0 then there is m′∈ M ′ with φ(m′) = m. But then for some n,
φ(anm′) = anm = 0 and since φ is injective, we conclude that m′∈ Γa(M ′).
b) Let 0 →M→I · be an injective resolution of M . Then 0 → ~M→ ~I · is a ﬂasque resolution of ~M , so it
will suﬃce to show that Γ a(M )≃ ΓY (SpecA, ~M ) for any A-module M . Let f1,...,f s generate a so X−Y
is covered by D(fi). Then an element m∈ ΓY (SpecA, ~M ) is just an element m∈M such that mP = 0 for
all P⁄∈ Y . Equivalently, we must have m↦→ 0 in Mfi for all i since the D(fi) cover X−Y . Thus, there
is some n such that fn
i m = 0 for all i and hence m∈ Γa(M ). In the reverse direction, if m∈ Γa(M ) then
m∈ Γ(SpecA, ~M ) and m↦→ 0 in Mfi so m∈ ΓY (SpecA, ~M ).
c) It suﬃces to show that c∈Hi
a(M ) is killed by an for some n. But Hi
a(M ) is a quotient of a submodule of
Γa(I) for some I, so pick m∈ Γa(I) lifting c. Then by deﬁnition, there exists n with anm = 0 so the same
is true of c.
3.7 a) Pick generators f1,...,f s of a and observe that U =∪D(fi). Deﬁne
HomA(an,M )→ Γ(U, ~M ) = {(αi)∈
∏
Mfi :αi =αj∈Mfifj}
byϕ↦→
(ϕ(f n
i )
f n
i
)s
i=1.
In the reverse direction, suppose that
(mi
f
ni
i
)s
i=1∈ Γ(U, ~M ). Let m = max ni and deﬁne ϕ∈ Hom(an,M )
for any n≥ms as follows: let fj1
1 ··· fjs
s ∈ an and let i0 be the index for which ji0 is maximal, so ji0≥m.
Then deﬁne (to start oﬀ with)
ψ(fj1
1 ··· fjs
s ) = fj1
1 ··· ˆf
ji0
i0 ··· fjs
s ·f
ji0 −ni0
i0 mi0.
The problem is that this may not be well deﬁned. However, observe that since mifnj
j −mjfni
i is killed by a
power of fifj (cf. II,5.14), there is some large N such that φ := (f1··· fs)Nψ is well deﬁned.
It is not hard to check that this is well deﬁned (using the compatibility properties of the local sections
mi/fn1
i ) and inverse to the map deﬁned above, so we have the claimed isomorphism.
b) When M is injective, any section s∈ Γ(U, ~M ) gives a homomorphism an→M for some n, which extends
to a morphism A→M as M is injective and gives a section ~s∈ Γ(X, ~M ) restricting to s. In other words,
Γ(X, ~M )→ Γ(U, ~M ) is surjective and ~M is ﬂasque.
3.4
4.1 By II, 5.8, f∗F is a quasi-coherent sheaf on Y . Let U be an aﬃne covering of Y . Then since f is aﬃne,
f −1U is an aﬃne covering of X, so by Theorem 4.5, we have natural isomorphisms ˆHp(f −1U, F)≃Hp(X, F)
23

and ˆHp(U,f ∗F)≃Hp(Y,f ∗F) for all p≥ 0. But the Cech complexes for ˆHp(f −1U, F) and ˆHp(U,f ∗F) are,
respectively, ∏
i0<···<ip
F(f ∗Ui0...ip),
∏
i0<···<ip
F(f −1Ui0...ip),
where
f ∗Ui0...ip :=
p⋂
j=0
f −1Uij =f −1Ui0...ip,
so the Cech complexes are isomorphic, whence the cohomology groups are isomorphic.
4.2 a) We show that M = OX ﬁts the bill. Indeed, let Spec A∋y be an open aﬃne nbd of y∈Y , where y
is the generic point. Then Spec B =f −1(SpecA) is an open aﬃne nbd of the generic point x∈X, since f is
ﬁnite, hence aﬃne. Moreover, as f is ﬁnite, A→B makesB a ﬁnite A-module. Since X is aﬃne, the open
sets Xg for g∈ Γ(X, OX ) form a basis of opens of X, so let g∈ Γ(X, OX ) be such that x∈ Xg⊆ SpecB.
Put K = Frac B and k = Frac A (X,Y are assumed integral!). Then since B is A-ﬁnite, it follows that
K/k is ﬁnite, and we may pick a basis si,...,s m∈ B for K/k. Now si
⏐⏐
Xg
∈ Γ(Xg, OX ), so by II, Lemma
5.3 (b) there exists some n >0 such that xi := gnsi
⏐⏐
Xg
is a global section of OX , and hence an element of
Γ(Y,f ∗OX ). The xi then give a morphism Om
Y →f∗OX deﬁned by ( ti)↦→ ∑xiti. This is an isomorphism at
the generic point of Y since the map km→K deﬁned by ( ti)↦→ ∑tisi is an isomorphism.
b) Now let F be any coherent sheaf on Y and apply H om(·, F) to Om
Y → f∗OX to get a map β :
H om(f∗OX, F)→ H om(Om
Y, F). Observe that H om(f∗OX, F) is both a OY -module, and af∗OX -module
(via inner composition), so Ex. 5.17 (e) gives a coherent sheaf G on X with f∗G≃ H om(f∗OX, F). The
map β :f∗G→ Fm is an isomorphism at y since α is.
c) Since f is ﬁnite, f∗G is coherent by Ex. 5.5, so ker β and coker β are coherent by Prop. 5.7. It follows
that Y1 := Supp ker β and Y2 := Supp coker β are closed (let F be any coherent sheaf and suppose FP = 0.
Pick an aﬃne nbd Spec A of P with F
⏐⏐
SpecA = ~M and let M be generated by m1,...,m r over A. Then
(mi)P = 0 so we have opens Ui with mi
⏐⏐
Ui
= 0. Then V = U∩U1∩···∩ Ur is an open nbd of P with
F
⏐⏐
V = 0). Moreover, since β is an isomorphism at y, we have y⁄∈Yi for i = 1, 2. As f −1(Yi) is closed and
X is aﬃne, it is aﬃne, and f : f −1(Yi)→ Yi is then a ﬁnite morphism of integral noetherian schemes, so
we assume (using Noetherian induction) that this implies that Y1,Y 2 are aﬃne, and we must show that Y
is aﬃne. Let ji :Yi→Y be the inclusion. Then since Supp ker β =Y1 we have ( j1)∗(j1)∗ kerβ = ker β and
similarly for coker β; we may then apply Lemma 2.10 to conclude that
Hp(Y, kerβ) = Hp(Y1, (j1)∗ kerβ) = 0
since ( ji)∗ kerβ is coherent (Prop. 5.8) and Y1 is aﬃne by hypothesis (using Serre’s criterion Thm. 3.7).
Similarly,Hp(Y, cokerβ) = 0. But we have the exact sequence
0→ kerβ→f∗G→ Fm→ cokerβ→ 0
which gives two short exact sequences
0→ kerβ→f∗G→ imβ→ 0
and
0→ imβ→ Fm→ cokerβ→ 0.
Taking cohomology and using the fact that Hp(Y, kerβ) = Hp(Y, cokerβ) = 0 for all p> 0 (by Noetherian
induction hypothesis) yields an isomorphism
Hp(Y,f ∗G)≃Hp(Y, Fm) = Hp(Y, F)m.
24

By Ex. 4.1, using the fact that f is aﬃne, we have Hp(X, G) = Hp(Y,f ∗G). Finally, applying Serre’s criterion
and the hypothesis that X is aﬃne yields Hp(Y, F) = 0. Since F was arbitrary, we again apply Serre’s crit.
to conclude that Y is aﬃne. By Noetherian induction, we are done in the case that X, Y are integral. Ex.
3.1 and 3.2 allow us to immediately reduce to this case.
4.3 We cover U by the open aﬃnes D(x) = Spec k[x, 1/x,y ] and D(y) = k[y, 1/y,x ]. We have seen that
Γ(U, OX ) = k[x,y, 1/x, 1/y]. Thus, we have the Cech complex
k[x, 1/x,y ]⊕k[y, 1/y,x ]
d:(f,g)↦→f −g
−−−−−−−−→k[x,y, 1/x, 1/y]→ 0,
so ˆH 1(U, OX ) = k[x,y, 1/x, 1/y]/imd. But the image of d is just k[x,y ], so ˆH 1 is the k-vector space spanned
by{xiyj : i,j < 0}, and in particular is inﬁnite-dimensional, so by Serre’s criterion, we see that U is not
aﬃne.
4.5 We prove that Pic X≃ lim−→U
ˆH 1(U, O×
X ). Indeed, let F be an invertible sheaf, and let U be any cover
consisting of aﬃnes Ui withφi : OUi
∼
− →F
⏐⏐
Ui
. Then φ−1
i ◦φj : OUi∩Uj
∼
− →OUi∩Uj is an isomorphism, so gives
an element sij∈ O(Ui∩Uj)×. Moreover, we have sjk·s−1
ik ·sij = 1 since it comes from the isomorphism
φ−1
j φk◦φ−1
k φi◦φ−1
i φj = id, so we obtain an element of ker
(
O×
X (Ui∩Uj)→ O×
X (Ui∩Uj∩Uk)
)
, i.e. of
lim−→U
ˆH 1(U, O×
X ) (observe from that once the isomorphisms φi have been ﬁxed, the element of ˆH 1 deﬁned
behaves well under reﬁnement of open covers). The map Pic X→ ˆH 1(U, O×
X ) thus deﬁned is surjective, as
given any cocycle representing an element of ˆH 1, we obtain an invertible sheaf (by using the cocycle to glue
together the sheaves OUi just as above) that maps to it. The map is injective because if the cohomology
class obtained is zero, then the isomorphisms φi : OUi
∼
− →F
⏐⏐
Ui
are multiplication by elements si∈ O×
Ui, so
in fact F≃ OX as an OX -module. Using the isomorphism ˆH 1(U, O×
X )≃ H 1(X, O×
X ) of Ex. 4.4 completes
the proof.
4.7 We have
OX (V ) = k[x0/x2,x 1/x2]/(f (x0/x2,x 1/x2, 1)) = k[u,v ]/(f (u,v, 1))
and
OX (U ) = k[x0/x1,x 2/x1]/(f (x0/x1, 1,x 2/x1)) = k[u/v, 1/v]/(f (u/v, 1, 1/v))
and OX (U∩V ) = k[u,v, 1/v]/(f (u,v, 1)). Thus, the image OX (U )⊕ OX (V )→ OX (U∩V ) consists of all
pairs (α,β )∈k[u,v ]⊕k[u/v, 1/v] modulo f (u,v, 1) that are equal. Hence the image is spanned by uivj with
i≥ 0, j∈ Z and−j≥ i if j < 0 (otherwise no restriction) , so H 1 as a k-vector space is spanned by the
monomials uivj with 0 <−j < i. The relation f (u,v, 1) = 1 gives a linear dependence on ud in terms of
such monomials, so a basis for H 1 is{ui/vj : 0 < j < i < d}. Thus, dim kH 1 = (d− 1)(d− 2)/2. Now H 0
consists of those ( α,β )∈k[u,v ]⊕k[u/v, 1/v] that are equal modulo f (u,v, 1). By considering denominators,
we see that this consists of the constants k, so dim kH 0 = 1.
4.11 The proof is almost identical to that of 4.5. We have ˆH 0(U, F) = Γ( X, F) for any open covering F as
the proof of 4.1 clearly shows. In general, imbed F in a ﬂasque, q-coh sheaf G and let R be the quotient.
Because the intersections Ui0...ip have no nontrivial cohomology (for the sheaf F), we have exact sequences
0→ F(Ui0...ip)→ G(Ui0...ip)→ R(Ui0...ip)→ 0.
The proof now follows that of 4.5 verbatim.
25

3.5
5.1 Observe ﬁrst that the deﬁnition of χ makes sense by Theorem 5.2. The short exact sequence 0 → F′→
F→ F′′→ 0 gives a long exact sequence of k-vector spaces:
0→H 0(X, F′)→···→ Hi(X, F)→Hi(X, F′′)→Hi+1(X, F′)→··· ,
and this leads to the formula required formula.
5.7 We use Prop. 5.3.
a) By II, Cor. 4.8, the closed immersion i is proper, so by Caution 5.8.1, for any coherent sheaf F on Y ,
the sheaf i∗F is coherent on X. Thus let L be ample on X. Then then for every coherent F on Y , i∗F is
coherent on X, so by 5.3 there exists n0 s.t. for all i >0 and all n > n0 we have Hi(X,i ∗F⊗ Ln) = 0.
There is a natural surjective map i∗F⊗ Ln→ i∗(F⊗i∗L ) by II, Ex. 1.19, and thus a surjective map
Hi(X,i ∗F⊗ Ln)→Hi(X,i ∗(F⊗i∗Ln)) = Hi(Y, F⊗i∗Ln) by III, Lemma 2.10. We thus conclude that
Hi(Y, F⊗i∗Ln) = 0 for all i> 0 and all n>n 0, so by applying 5.3 again, we see that i∗L is ample on Y .
b) Let F be a coherent sheaf on X and consider the ﬁltration from III, Ex. 3.1. We thus obtain exact
sequences
0→ N i+1F⊗ Ln→ N iF⊗ Ln→ N iF/N i+1F⊗ Ln→.
Taking cohomology and using the isomorphism
N iF/N i+1F⊗OX Ln≃ N iF/N i+1F⊗OXred
(OXred⊗ L )n,
we see by 5.3 that if L⊗ OXred is ample on Xred then for any i> 1 and any coherent F on X there exists
n0 such that for all n > n0 and all j≥ 1 we have isomorphisms Hi(X, F⊗ Ln)≃ Hi(X, N jF⊗ Ln).
Takingj large enough so N j is the zero sheaf and considering the surjective maps H 1(X, N jF⊗ Ln)≃
H 1(X, F⊗ Ln), we conclude (again by 5.3) that L is ample on X. For the converse, we observe that the
natural map i :Xred→X is a closed immersion, with i∗L = L⊗ OXred. Thus, part a) yields the converse.
c) As in b), part a) yields one direction ( Xi→X is a closed immersion). For the other direction, we let F
be a coherent sheaf on X and ﬁlter F as in Ex. 3.2, so as to obtain exact sequences
0→ I1··· Ik· F⊗ Ln→ I1··· Ik−1· F⊗ Ln→ I1··· Ik−1· F/I1··· Ik· F⊗ Ln→ 0,
with Ii the ideal sheaf of Xi. Now
I1··· Ik−1· F/I1··· Ik· F⊗OX Ln≃ I1··· Ik−1· F/I1··· Ik· F⊗OXk
(OXk⊗OX L )n
since I1··· Ik−1·F/I1··· Ik·F is a sheaf of OX/Ik = OXk -modules. The long exact cohomology sequences
and the hypothesis that L⊗OX OXi is ample on Xi yields, via 5.3, an n0 such that for all i > 0 and all
n>n 0 there are isomorphisms
Hi(X, F⊗ Ln)≃Hi(X, I1··· In· F⊗ Ln)
for all i> 1 and a surjection H 1(X, I1··· In· F⊗ Ln) ↠H 1(X, F⊗ Ln). However, I1··· In is the zero
sheaf on X as we saw in Ex. 3.2, so we conclude that Hi(X, F⊗ Ln) = 0 for all i >0 and all n > n0, so
that L is ample by 5.3.
d) Parts b) and c) allow us at once to reduce to the case of X and Y integral. Let F be any coherent sheaf
onY . Then we have seen in the proof of Ex. 4.2 that there is a sheaf G onX and a morphism β :f∗G→ Fr
that is an isomorphism at the generic point of Y . Proceeding as in Ex. 4.2 by Noetherian induction and
using the long exact cohomology sequences associated to
0→ kerβ⊗ Lnr→f∗G⊗ Lnr→ imβ⊗ Lnr→ 0
26

and
0→ imβ⊗ Lnr→ (F⊗ Ln)r→ cokerβ⊗ Lnr→ 0
we conclude that Hi(Y, (F⊗ Ln)r)≃Hi(Y,f ∗G⊗ Lnr). Now the natural map L→f∗f ∗L yields a map
Hi(Y,f ∗G⊗ Lnr)→Hi(Y,f ∗(G⊗ (f ∗L )nr)),
and by Ex. 4.1, we have
Hi(Y,f ∗(G⊗ (f ∗L )nr)) = Hi(X, G⊗ (f ∗L )nr).
HMMMMMMMMMMM????
5.10 Let OX (1) be a very ample invertible sheaf on X. Then we have short exact sequences
0→ Fi/ kerαi⊗ OX (n)
αi
−→Fi+1(n)
αi+1
−−−→imαi+1⊗ OX (n)→ 0
and
0→ imαi⊗ OX (n)→ Fi+1(n)→ cokerαi⊗ OX (n)→ 0
for all i≥ 1 and all n> 0. Exactness implies that coker αi = Fi+1/imαi = Fi+1/ kerαi+1. Since the Fi are
coherent, all the sheaves in the exact sequences above are coherent. Now use 5.3 to ﬁnd ni such that for all
n>n i and all j we have
Hi(imαi⊗ OX (n)) = Fi/ kerαi⊗ OX (n) = 0
and let N = max ini. Then for all n > N we have exact sequences (from the long exact sequences of
cohomology and the fact that we have forced all the H 1’s to vanish)
0→ Γ(X, Fi/ kerαi⊗ OX (n))→ Γ(X, Fi+1(n))→ Γ(X, imαi+1⊗ OX (n))→ 0
and
0→ Γ(X, imαi⊗ OX (n))→ Γ(X, Fi+1(n))→ Γ(X, cokerαi⊗ OX (n))→ 0.
Using the fact that coker αi = Fi+1/imαi = Fi+1/ kerαi+1 as noted above and splicing these exact sequences
back together shows that for all n>N we have an exact sequence
Γ(X, F1(n))→ Γ(X, F2(n))→... → Γ(X, Fr(n)),
as desired.
27

Chapter 4
4.1
1.1 Consider the divisor nP for a positive integer n. We have
l(nP )−l(K−nP ) = n + 1−g,
so choosing n > gand observing that l(K−nP )≥ 0, we conclude that l(nP ) > 1, which is to say that
dimkH 0(X, L (nP )) = dim k Γ(X, L (nP )) > 1, so there is a nonconstant rational function f ∈ L (nP ).
Then f is regular everywhere but P , where it must have a pole.
1.2 We ﬁrst claim that there is a function fi with a pole at Pi and nonvanishing at Pj for all j. Indeed,
choose n suﬃciently large so
l(nPi−
∑
j⁄=i
Pj) = n + 1−g− (r− 1)
and
l(nPi−
∑
j⁄=i,k
Pj) = n + 1−g− (r− 1) + 1 .
Since we have the obvious containment
H 0(X, L (nPi−
∑
j⁄=i
Pj))⊆H 0(X, L (nPi−
∑
j⁄=i,k
Pj)),
dimension considerations show that there is a function gi,k with a pole at Pi and vanishing at Pj for j⁄=k,
but nonvanishing for j =k. Then the function fi := ∑
kgi,k has a pole at Pi and f (Pj) = gi,j(Pj)⁄= 0. We
now let F = ∏
ifi. Then F has a pole at Pi for all i because there can be no cancellation by our construction.
1.3 The hypotheses allow us to embed X in a proper curve ~X and we let S = ~X\X ={P1,...,P r} (as it
is a closed subset and nonempty since X is not proper). By 1.2, we have a function f with poles at Pi and
regular elsewhere, so f : ~X→ P1 satisﬁesf −1(A1) = X. By II 6.8, as f is nonconstant and ~X is proper, we
conclude that f is a ﬁnite morphism, and in particular aﬃne. Hence f −1(A1) = X is aﬃne.
1.4 Let X be a separated one-dimensional scheme over k none of whose irreducible components are proper.
By III Ex. 3.1 we know that X is aﬃne iﬀ Xred is aﬃne, so we may assume X reduced. Similarly, III Ex.
3.2 allows us to suppose that X is irreducible, hence integral. Now let f : ~X→X be the normalization. It
is a ﬁnite surjective morphism with ~X an integral, normal, separated, one-dimensional scheme over k, hence
by I 6.2A it is regular also. If X is not proper, neither is ~X, as the image of a proper scheme under a ﬁnite
morphism is again proper by II, Ex. 4.4. So assume ~X is not proper. Then we may apply 1.3 to conclude
that if ~X is aﬃne. Finally, we apply III, Ex. 4.2 (as f is ﬁnite) and conclude that X is aﬃne.
28

1.5 Let D be eﬀective, so we have the containment H 0(X, L (K−D))⊆H 0(X, L (K)), with equality holding
iﬀ deg D = 0 or g = 0. Then l(D)− 1 = deg D +l(K−D)−g≤ degD, with equality iﬀ deg D = 0 (i.e.
D = 0 since D is eﬀective) of g = 0.
1.6 It follows from II, 6.9 that deg f = deg(f )∞, the degree of the divisor of poles of f . Let P be any point
ofX. Then l((g + 1)P ) = 2 + l(K− (g + 1)P )> 1, so there exists a function f with (g + 1)P− (f )∞ eﬀective,
or what is the same, a morphism f :X→ P1 of degree deg f≤g + 1.
1.7 The only non-obvious part is that |K| has no base points. If P is a base point of |K| then every eﬀective
divisor linearly equivalent to K has support containing P , so every f∈H 0(X, L (K)) has a zero at P . In
other words, the containment H 0(X, L ((K−P ))⊆H 0(X, L (K)) is an equality, so l(K−P ) = l(K) = 2.
Then l(P ) = l(K−P ) = 2 by Riemann-Roch. We conclude that there is a function f with a simple pole
at P , so this deﬁnes a morphism X → P1 of degree 1, (as in Ex. 1.6) which must be an isomorphism,
contradicting the assumption that g = 2. Thus |K| is base-point free, so we use II, 7.8.1 to get a morphism
f :X→ P1 of degree deg K = 2.
1.10 Following the proof of 1.3.7, it is enough to show that for any divisor D of degree 0 supported in Xreg
there exists a point P∈Xreg with D∼P−P0. Using Ex. 1.9 and the hypothesis that pa = 1, we have
l(D +P0)−l(K−D−P0) = 1 ,
and as K−D−P0 has degree −1, there exists a function f with ( f ) + D +P0≥ 0, and comparing degrees
shows that we must have( f ) + D +P0 =P for some point P , necessarily in Xreg asD is supported in Xreg.
29

