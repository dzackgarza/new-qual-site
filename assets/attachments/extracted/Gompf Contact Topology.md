Contact Topology
George D. Torres
M392C - Fall 2017
1 Plane Fields and Contact Structures 2
1.1 Euler Classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Classifying Rank 2 Vector Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Cobordism classes of framed links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.4 Contact Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 Gray’s Theorem 14
2.1 Local models for Legendrian and transverse knots . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.2 Surfaces and Characteristic Foliations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3 Convex Surfaces 22
3.1 Giroux’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.2 Generic convexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.3 The Flexibility Theorem and LeRP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4 Contact structures in 3-Manifolds 32
4.1 Tight and Overtwisted Contact Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2 Euler Classes of Tight Contact Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.3 Classiﬁcation Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
4.4 Classiﬁcation using Tori and Lens Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.5 Using Open Book Decompositions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5 Legendrian Knot and Link Theory 44
5.1 Knot Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.2 Knot Simplicity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.3 Stein Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
A Appendix 49
————————————————–
ThesearelecturenotesfromBobGompf’sContactTopologycourseM392CgivenFall2017atUTAustin. The
reader should be comfortable with essential notions of diﬀerential and algebraic topology as well as the basics
of knot theory. A prior knowledge of symplectic topology is recommended but not required. I found parts of
Laura Starkston’s thesis [3] useful to read alongside these lectures. Bob’s proofs tend to be very picture-heavy,
whichcanbehardtotranslateontoapage,sosomeproofshereinarenotinfullrigor. SpecialthankstoRiccardo
Pedrotti for various contributions and corrections. Please send any corrections togdavtor@math.utexas.edu.
Last updated: March 15, 2019
1

1. Plane Fields and Contact Structures
O
This is a course on contact manifolds, which are odd dimensional manifolds with an extra structure called a
contact structure. Most of our study will focus on three dimensional manifolds, though many of these notions
hold for any odd dimension. In this section, we will start with some preliminary deﬁnitions to motivate the
deﬁnition of a contact structure. Then we will embark on a classiﬁcation of vector bundles in order to classify
plane ﬁelds, after which we can give a proper deﬁnition of a contact structure.
O
Deﬁnition 1.1.A hyperplane ﬁeldon a manifoldM is a smoothly varying choice of planeξx⊂TxM.
Example1.2. Thesimplestplaneﬁeldon M = Rn isthehorizontalhyperplaneﬁeld ξ0;ateachpoint,weassign
the horizontal plane described bydxn = 0. These are uniquely tangent to the collection of horizontal planes in
Rn.
Hyperplane ﬁelds are closely related tofoliations on manifolds. There are two equivalent deﬁnitions of a
foliation on a n-manifoldM. It is a hyperplane ﬁeldξ such that:
1. ξ islocallymodeledbytheoneintheaboveexample. Thatis,thereisalocalchartaroundeverypointthat
is diﬀeomorphic toξ0.
2. A collection of surfacesSα everywhere tangent toξ such thatM =⊔αSα uniquely.
Sometimes we refer to a foliation by the collection of surfacesSα. A natural question to ask about a hyperplane
ﬁeld is if it arises from a foliation. When a hyperplane ﬁeld does (at least locally), it is called integrable. Given
a foliation, the collection of tangent spaces is an integrable hyperplane ﬁeld.
Example 1.3. We can foliateR2−{ 0} by concentric circles, shown below on the left. However, a small pertur-
bation to the hyperplanes can produce a foliation with spirals attracting to circles. In this case, the surfaces are
no longer compact as they were in the unperturbed case.
This example demonstrated one of two main stability problems with foliations:
1. Foliations are not stable under perturbation in dimension greater than1.
2. Evenifaperturbationresultsinanotherfoliation, theresultingsurfacesmighthaveverydiﬀerenttopolo-
gies.
2

1 Plane Fields and Contact Structures
Therefore, to study things that are stable, it’s better to look at structures that arenot foliations. This is the idea
behindacontactstructure. Acontactstructureon M isahyperplaneﬁeldthatdoesnotrestricttoanintegrable
hyperplane ﬁeld on any submanifold ofM. Such a ﬁeld is calledcompletely non-integrable. We will make all of
these deﬁnitions more precise later.
1.1 Euler Classes O
Deﬁnition 1.4.ACk distributionξ on ann-manifoldM is anm-planeξx at every pointx∈M such that locally
ξ is spanned bymlinearly independentCk vector ﬁelds. It is called a hyperplane ﬁeld ifm =n− 1and a plane
ﬁeld ifm = 2,n = 3. A smooth distribution is aC∞ distribution.
Exercise 1.5.Show that a hyperplane ﬁeld isCk if and only if it is locally the kernel of a nonzeroCk 1-form.
Proposition 1.6.ξ = ker(α)for some nonvanishing 1-formαglobally if and only ifξ is co-orientable (i.e. there exists an
orientable line ﬁeld transverse toξ).
Another way to deﬁne distributions is through the language of vector bundles. Recall that a vector bundle
π :E→B isasmoothsurjectionsuchthat π−1(x)isavectorspaceforevery x∈B. Itmustalsosatisfythelocal
trivialization condition: around every pointx∈B there is a neighborhoodU such thatU× Rk∼=π−1(U) and
the following diagram commutes:
π−1(U) U× Rk
U
∼=
π π1
A sub-bundle ofπ :E→B is a subsetF⊂E such thatπ :F→B is a vector bundle.
Deﬁnition 1.7.A distribution is a sub-bundle ofTM. In particular, a hyperplane ﬁeld is a codimension 1 sub-
bundle ofTM.
Proposition1.8. If (F,B,π )⊂ (E,B,π )isasub-bundle,thereexistsacomplementarysub-bundle (F′,B,π ′)suchthat
F⊕F′∼=E.
An important invariant that can be associated to vector bundles is the Euler class, which is a characteristic
class that measures how “twisted” the bundle is. To deﬁne this, letπ : E→ B be an oriented rankk vector
bundle over an oriented manifoldB. Further, letσ :B→E be a section transverse to the0 section ofπ. Since
it is transverse,σ−1(0) is a codimensionk submanifold ofB and hence represents a homology class[σ−1(0)]∈
Hn−k(B, Z). By Poincaré duality, there is a corresponding homology classe∈Hk(B, Z).
Deﬁnition 1.9.TheEuler classofπ :E→B ise∈Hk(B, Z) as above.
Proposition 1.10. The Euler class is well deﬁned.
Proof. (sketch)Theideaistouseacobordism. Let σ1 andσ2 betwosectionstransversetothezerosection. Then
these are homotopic (say, by linear homotopy) and so the preimagesσ−1
1 (0) andσ−1
2 (0) are cobordant.
□
Example 1.11. Consider the tangent bundleE = TB, so thatk = n. Then,e(E)∈ Hn(B)∼= Z (so long asB
is connected). In this case,e(E) is the Euler characteristicχ(B) (technically, it is⟨e(E), [B]⟩, where [B] is the
fundamental class ofB). This can be seen by using the self intersection deﬁnition of the Euler characteristic:
χ(M) =I(∆, ∆) =e(N∆) =e(T ∆) =e(TM )
Where ∆ is the diagonal inB×B,N∆ is the normal bundle to∆ andT ∆ is the tangent bundle to∆.
3

1 Plane Fields and Contact Structures
M
φ−1(p)
ψ−1(q)
p
q
γ
ψ
φ
Figure 1.1: The framed submanifoldsφ−1(p) andψ−1(q) and the induced pathγ.
1.2 Classifying Rank 2 Vector Bundles O
Ingeneral,characteristicclassesarenotenoughtocharacterizeallvectorbundles. However,forsmallranksthey
are enough.
Theorem1.12. Orientedrank 2vectorbundlesoveroriented,closedmanifoldsareclassiﬁedbytheEulerclass e(−). That
is, for eachx∈H2(M)∼=Hn−2(M), there is a unique bundleE→M such thate(E) =x.
Similarly, rank1 bundles are classiﬁed byω1∈H1(M; Z2), the Stiefel-Whitney class.
Corollary1.13. Orientedplaneﬁeldsonaclosed,oriented 3manifoldaredetermineduptoisomorphismas 2-planebundles
E bye(E)∈H1(M).
Remark1.14. Just because two plane ﬁelds have the same Euler class (and are hence isomorphic as sub-bundles
ofTM) doesn’t mean they are homotopic as sub-bundles. As a result, we’ll have to use a diﬀerent technique to
answer the question of homotopy.
Animportantfactistheeveryoriented 3manifoldhasatrivialtangentbundle 1. Thuswehavea(non-unique)
isomorphismτ : TM → M× R3. For now, we ﬁx the trivializationτ. Letξ be an oriented plane ﬁeld. Since
every plane inR3 has a unique positive unit normal, such a plane ﬁeld corresponds to a unit vector ﬁeld onM,
which corresponds to a mapM→S2. Therefore:
{Oriented plane ﬁelds up to homotopy} ⇐⇒[M,S 2]
An important understanding of[M,S 2] can be obtained using the Thom-Pontryagin construction.
Thom-Pontryagin Construction
LetM be a closed manifold, and consider the homotopy classes of maps[M,S k]. Givenφ :M→Sk, letp∈Sk
bearegularvalue, sothat φ−1(p)isaclosedmanifoldofcodimension k. Givenapositivebasisfor TpSk, weget
anormalframingon φ−1(p). Foradiﬀerentψ :M→Sk andregularvalue q∈Sk,assumewehaveahomotopy
Φ :I×M→I×Sk ofφandψ. Wethengetapath γ connectingpandq inSk,andhence Φ−1(γ)isacobordism
betweenφ−1(p) andψ−1(q). This cobordism is actually framed by pulling back a framing onγ. See Figure 1.1.
The conclusion is that ifφ andψ are homotopic, then framed submanifolds are framed cobordant.
Proposition 1.15. The framed cobordism above is an equivalence relation.
Thismeanswehaveawell-deﬁnedmapbetween [M,S k]andequivalenceclassesofframedcobordismclasses
of framed codimensionk submanifolds.
1This related to the fact that odd-dimensional manifolds have trivial Euler characteristic
4

1 Plane Fields and Contact Structures
Theorem 1.16. This correspondence is a bijection:
[M,S k] ⇐⇒ {framed cobordism classes of framed codimensionk submanifolds}
Proof:
Tocheckthatthismapisonto, let M0 beaframedcodimension k submanifoldof M. Theframinggives
usamapofthenormalbundle NM0→ Rk suchthattheimageof M0×{0}is 0. Butthenormalbundleis
identiﬁed with a tubular neighborhoodMϵ
0 ofM0, so we have a mapφ :Mϵ
0→ Rk. We can think of this
as a mapφ′ :Mϵ
0→Sk by sending the complement of Im(φ) to∞, where we are writingSk = Rk∪∞.
Now extend this to a smooth map on all ofM by sendingM\Mϵ
0 to∞ as well. Therefore we have the
desired mapφ′ :M→Sk.
To check injectivity, letφ0,φ 1 : M → Sk such that the corresponding framed submanifolds are
framed cobordant. We would like to show thatφ0 ∼ φ1. We extend φ1 and φ0 to a mapΦ : I×
M→ Sk using the given cobordism in the following way: we extendφ0 andφ1 to a map on a tubular
neighborhood of the cobordism (seen as a submanifold ofM×I), and send the rest ofM×I to a point
onSk like before. ThenΦ is the desired homotopy.
□
Remark 1.17. IfM is oriented, then so is every framed submanifold.
Example 1.18.Supposen =k andM connected. This correspondence is:
[M,S k] ⇐⇒ {framed cobordism classes of zero dimensional submanifolds}
The framed cobordism classes of zero manifolds isZ (given by the signed count) and the map[M,S k]→ Z is
thedegreemap. Whathappenswhen M isnon-orientable? Thentheframedcobordismclassesaredetermined
by their parity (because same-sign points can be cobordant in this case), so we have[M,S k]→ Z/2Z.
1.3 Cobordism classes of framed links O
Let’s return to the case that we were interested in to begin with:[M,S 2] for a closed, oriented3 manifoldM.
We now have:
{Oriented plane ﬁelds on M (up to homotopy)} ⇐⇒[M,S 2] ⇐⇒ {Framed cobordism classes of framed links}
Recallthattheﬁrstpartofthisbijectionisnon-canonical(dependsonthetrivialization τ). So,nowwecareabout
framedlinksin M. Everylinkisclosed,bythepreimagetheorem,sotheyrepresentelementsof H1(M; Z). This
is not a bijection, in general. However, it is onto.
Proposition 1.19. This is onto.
Proof:
Every class inH1(M) is represented by an oriented link. Since the normal bundle is trivial, any trivial-
ization gives us a framing of the link.
□
Denote Γτ to be the map that takes an oriented plane ﬁeld onM to the corresponding element ofH1(M)
using the correspondence above. Recall, we also have an Euler class to associate to a plane ﬁeldξ, which is an
element ofH2(M)∼=H1(M). This is not, however, the same asΓτ(ξ). To see this, consider the diagram:
ξ TS 2
M S2φτ
5

1 Plane Fields and Contact Structures
The top map sends a plane at a pointx∈M to the tangent space to the corresponding point on the sphere, and
φτ sends a pointx∈M to the unit normal vector ofξx. It is not hard to see that this commutes. Now consider
the standard vector ﬁeld onS2, which ﬂows from the north poleN to the south poleS, and call itv. We can
pull this back to a vector ﬁeldσ =φ∗
τ(v) inM in a way that is compatible with the above diagram:
ξ TS 2
M S2
σ
φτ
v
Wecanusethiscompute e(ξ). Thezerosetof φ∗
τvisφ−1
τ (N)∪φ−1
t (S). Infact,φ∗
τ istransversetothezerosection.
Then:
PD(e(ξ)) = [φ−1
τ (N)]| {z }
Γτ(ξ)
+ [φ−1
τ (S)]| {z }
Γτ(ξ)
= 2Γτ(ξ)
Where PD(−) is the Poincaré dual. So, the Euler class andΓτ(ξ) aren’t quite the same thing (depending on the
2-torsion inH1(M; Z)). In general,Γτ is a ﬁner invariant thane(−).
Remark 1.20. There is also an algebraic proof of this identity. In the diagrams above, we have realizedξ as the
pullback of the bundleTS 2→ S2 over the mapM→ S2. Euler classes (and characteristic classes in general)
behave nicely under pullbacks. That is, the induced map on cohomologyφ∗
τ : H2(S2)→ H2(M) sends Euler
classes to Euler classes:
PD(e(ξ)) = PD(φ∗
τ(e(TS 2))) = PD(φ∗
τ(2[S2]∗)) = 2 PD(φ∗
τ[S2]∗)
where [S2]∗ is the chosen generator ofH2(S2). Finish.
Corollary 1.21. An oriented plane bundleξ onM is realized as a plane ﬁeld if and only ife(ξ) = 2x forx∈H1(M).
Proof:
One direction is immediate from our calculation above. For(⇐), surjectivity ofΓτ gives usξ′ such that
Γτ(ξ′) =x. Thene(ξ′) =e(ξ), and henceξ∼=ξ′.
□
Suppose we are given two plane ﬁeldsξ,ξ′ such thate(ξ) = e(ξ′). Then TM ∼= ξ⊕ R andTM ∼= ξ′⊕ R
(where Risanorientedlinebundle). But ξ∼=ξ′ asbundles,sowegetanautomorphismof TM. Inotherwords,
there exists an automorphism ofTM sendingξ toξ′. The conclusion is that, if we forgetτ, all that remains is the
Euler class.
Example 1.22. ConsiderM = RP 3. We knowH1(RP 3) = Z/2Z. Note that only0∈ H1 can be represented as
2x, so every plane ﬁeld inRP 3 is trivial as a plane bundle. For ﬁxed choice ofτ, however, we get two values of
Γτ and therefore there are at least two diﬀerent plane ﬁelds that are not homotopic.
Exercise 1.23.Analyze the Lens spaceL(p,q ) in the same way. (Hint:H1(L(p,q )) = Z/pZ).
1.3.1 Relative Euler classes
LetM becompactandorientedofdimension n,butmaybenotclosed. Wecandothesamederivationasbeforeto
deﬁnetheEulerclassofa kbundleξ→M. Inthiscase,theEulerclasswillbearelativehomologyclassbecause
the intersection of a submanifold with the zero section can have boundary. That is,e(ξ)∈ Hn−k(M,∂M )∼=
Hk(M).2
Deﬁnition 1.24.Supposee(ξ|∂M ) = 0; then there exists a nowhere zero sectionv :∂M→ξ. Now, we look for
extensionsw ofv to all ofM transverse to the zero section onM. Therelative Euler classe(ξ,v )∈ Hn−k(M)∼=
Hk(M,∂M ) is [w−1(0)].
2This isomorphism is by Poincaré-Lefschetz duality
6

1 Plane Fields and Contact Structures
Remark 1.25. This can be interpreted using the long exact sequence of the pair(M,∂M ):
··· Hn−k(∂M ) Hn−k(M) Hn−k(M,∂M ) Hn−k−1(∂M ) ···δ
Assuminge(ξ|∂M ) = 0isequivalenttosaying δ(e(ξ)) = 0intheabovesequence. Byexactness,thereisaclassin
Hn−k(M)whoseimageis e(ξ). ThisistherelativeEulerclass. Poincaré-Lefschetzdualitygivesusanisomorphic
exact sequence, which shows the same sequence of Euler classes as cohomology elements:
··· Hk+1(X,∂M ) Hk(∂M ) Hk(M) Hk(M,∂M ) ···
Figure 1.2: A vector ﬁeld on∂F extended toF.
Example 1.26.Letm =k = 2, soξ→F is a 2-plane bundle over a surfaceF. Suppose also thatF is connected
and∂F ⁄=∅. We can choose nonzero vector ﬁelds on the boundary as shown in Figure 1.2. The extension will
in general have zeros on the interior ofF. Then the Euler class is the signed count:
e(ξ,v ) =
∑
v(x)=0
signv(x)
Changinge(ξ,v ) by±1 is the same as adding±1 twists tov|∂F. So, we can push these zeros to the boundary.
For suitablev, therefore,e(ξ,v ) = 0 and hencee(ξ) = 0. Thus everyξ→F is trivial.
Gompf analogy:F is like a jar full of butterﬂies whose boundary is the lid; once you release the lid, they all
escape and it becomes trivial.
Exercise 1.27. Show that not doing the ﬁx onv above retrieves the Poincaré Hopf theorem as in the boundary-
lesscase. Thatis,for F compact,connected,showthat χ(F ) =e(TF,v )whereoneachcomponentof ∂F,either
v is parallel to∂F orv is perpendicular to∂F.
Understanding [M3,S 2]→H1(M)
Onceagainlet M bethreedimensionalmanifold,connectedandclosed. Denotethemap Γ : [M3,S 2]→H1(M)
to be the composition of correspondences shown at the beginning of Section 1.3. We know that this is a sur-
jection, so a natural question is: givenx∈ H1(M), what isΓ−1(x)? In other terms, given two framed links of
thesamehomologyclass, whatistheambiguityinchoosingframedcobordismsbetweenthem? Luckilyforus,
cobordant is the same as homologous in this setting3, so we just need to focus on the framing ofx.
3This isn’t obvious, but we won’t prove it here.
7

1 Plane Fields and Contact Structures
Letη,η′ be (nonempty) framed links representingx. Then there is a cobordismF⊂ M×I betweenη and
η′4. If we allow for change of framing on one component of∂F, we can push out any zeros (demonstrated
above). Thisgivesusaframingon F. Thetwiststhatwehadtointroduceononeofthecomponentsintroduces
anatural(transitive) Zactionon Γ−1(x). Itistemptingtosay Γ−1(x)∼= Z, butthisisnotquitethecase. Thereis
an equivalence relation onΓ−1(x) that can be demonstrated by introducing a surface classβ∈H2(M). Embed
β awayfromtheboundaryof M×I,sothatitintersects F transversely. AsshowninFigure1.3,wecandeform 5
this intersection to get another cobordismF′.
Recall the intersection pairing forMn closed, oriented:
Hk(Mn)×Hn−k(Mn)→ Z
[N1]· [N2] =I(N1,N 2)
where I(N1,N 2) denotes the intersection number ofN1∩ N2. We claim that sewing inβ added e(NF ) =
([F ]+β)·([F ]+β)zerosontotheframingof F (whichcanbepushedtoasmanyadditionaltwistsonacomponent
ofη′). This follows from the next two claims.
Claim1.28. e(NF′)detectsthenumberofzeroesoftheframingofthenormalbundleof F′ obtainedbyextend-
ing the framing on the two links
Proof:
Noticethatbeing F′ orientedandofcodimension 2inM×I (whichisoriented),a 2-framingisuniquely
determined by a non-zero vector ﬁeld. In fact once we have such vector ﬁeldv on F′ we can deﬁne
another vector ﬁeldw onF′ by just point-wise rotating counter-clockwise the vector ﬁeldv. w is well-
deﬁnedsinceNF′isorientable(hencewecanrotatecounter-clockwiseinacoherentway)andit’sclearly
smooth, sincev is. Given instead any oriented2-framing ofNF′, by applying Gram-Schmidt orthonor-
malization process (which can be thought as an isotopy) we see that the two vector ﬁeldsv1,v 2 are
point-wiseorthonormal,i.e. onevectorﬁeldistheotheronerotatedby π/2counter-clockwise(oncewe
choose an orientation, and up to substitutingv1 with−v1).
□
Claim 1.29. LetF′ obtained fromF andβ as described, thene(NF′) = ([F ] +β)· ([F ] +β)
Proof:
Recall that by deﬁnition the Euler class (in homology) of a bundle is given by the intersection product
of the zero section with a generic section. Take a tubular neighborhood ofF′ and identify it with the
normal bundle. We can use a direction to push a copy ofF′ transverse to itself and the Euler class will
precisely be the homology class deﬁned by the intersection. The latter is[F′]· [F′]. We conclude by
observing that[F′] = [F ] +β.
□
We can now calculate the number of additional zeros to the framing:
([F ] +β)· ([F ] +β) = [F ]· [F ] +β·β + 2[F ]·β
But [F ]· [F ] = 0 because we can just move it oﬀ itself disjointly insideM×I. Similarly,β·β = 0. Therefore we
have added2[F ]·β twists to the framing ofη′.
Deﬁnition 1.30.A classx∈ Hn(X; Z)/torsion is said to be primitive ifa⁄= mb for every integerm > 1 and
b∈Hn(X; Z).
Lemma 1.31. For anyy∈H1(M) primitive, there existsβ∈H2(M) such thaty·β = 1.
Proof:
4The lifting of a cobordism inM to a cobordism inM×I is justiﬁed in Appendix A.1
5This deformation can be locally modeled on{xy = 0}→{ xy =ϵ} forx,y∈ C
8

1 Plane Fields and Contact Structures
Notice that we have:
y·β =⟨PD (y)⌣PD (β), [M]⟩
=⟨PD (y)⌣γ, [M]⟩
=−⟨γ, [M]⌢PD (y)⟩
=−⟨γ,y⟩
whereγ∈ H1(M; Z) is the Poincaré dual ofβ (recall thatM is a3-dimensional manifold). Assumey
is not primitive. We will show that that there can’t be any surfaceβ such that the intersection product
is±1. Ify = n·x for somex∈ H1(M) andn⁄=±1, then it’s clear by linearity that all the intersection
products will be multiple ofn, hence not1. On the other hand, lety∈ H1(M; Z)/torsion be primitive.
By The Universal Coeﬃcient theorem we know that
H1(M; Z)/torsion∼= HomZ(H1(M; Z); Z)
Observe now that sinceM is compact, all the homology groups are ﬁnitely generated, in particular
H1(M; Z)/torsion ∼= Zk, for somek ∈ N (the ﬁrst Betti number). This implies that we can write
y = ∑k
i=1λixi, wherexi’s form a basis forH1(M; Z)/torsion. Since y is primitive, it must be that
GCD(λ1,...,λ k) = 1 . This implies that we can ﬁnd another basis forZ containing y as one of the
generator (use the fact that coprimes coeﬃcients lets you build an unimodular matrix with integer en-
tries). Hence by the Universal Coeﬃcient Theorem we can consider the dual ofy,y∗∈ H1(M) and by
PD it represents a surface inM intersecting transverselyy in a single point.
□
Letx = dy fory primitive andd∈ N (such ad is called the divisibility ofx), and takeβ as in the Lemma
above. Then:
2x·β = 2dy·β = 2d
Therefore any two framings that diﬀer by2d twists on a boundary component are framed cobordant. Thus
Γ−1(x)∼= Z/2dZ. This proves:
Theorem 1.32. ForM a closed, oriented 3-fold,[M,S 2] has a canonicalZ action, and the set of orbits is canonically
identiﬁed withH1(M)∼=H2(M)via Γ. Moreover, for eachx∈H1(M), the orbitΓ−1(x)is the necklaceZ/2dZwhered
is the divisibility ofx inH1(M)/torsion.
This is proved with more rigor in Appendix A.1. In particular, there are always torsion elements (perhaps
zero) for whichd = 0, hence:
Corollary 1.33. Every suchM has inﬁnitely many homotopy classes of maps toS2, and therefore also inﬁnitely many
homotopy classes of plane ﬁelds that are trivial as bundles.
Remark1.34. Unfortunately,wehaven’tﬁxedtheissueoftrivializations. Ifwewanttosayanythingaboutplane
ﬁelds, we’d like to write down information that is independent ofτ. See [1] Ch. 11 for more discussion.
1.3.2 4-manifold digression
Deﬁnition 1.35.An almost complex structurea manifoldX is aC-vector space structure onTX. In other words,
it is a mapJ :TX→TX such thatJ◦J =−id and the following diagram commutes:
TX TX
X X
J
id
9

1 Plane Fields and Contact Structures
M
M
η
η′
β
F
Figure 1.3: Smoothly deforming the transverse intersection ofF andβ to give a cobordism ofη andη′.
Givenacodimension 1submanifoldM⊂X,then TxM⊂TxX isarealcodimension 1subspaceforevery x.
Thenξx :=JTxM∩TxM⊂TxX is a complex codimension1 complex subspace (because it is preserved under
applyingJ). This is the unique maximal complex subspace ofTxM, and it deﬁnes a plane ﬁeld onM.
Example 1.36.S2n−1⊂ Cn inherits a hyperplane ﬁeld. This is the standard contact structure onS2n−1.
For a closed, almost complex4 manifoldX, there is a relation on three of its invariants:
c1(X)2− 2χ(X)− 3σ(X) = 0
wherec1istheﬁrstChernclassand σ(X)isthesignature. Motivatedbythis,for (X,J )compactwithnon-empty
boundary∂X = (M3,ξ ), we deﬁne
θ(ξ) =c1(X)2− 2χ(X)− 3σ(X)
Thisisawell-deﬁnedinvariantoftheplaneﬁeld ξ (thatis,itisindependentof (X,J )). Thereisasubtlety: what
doesc2
1 mean for a manifold with boundary? It turns out it can be deﬁned whenevere(ξ) is a torsion element
by usingH1(M; Q).
1.4 Contact Structures O
We will now return to the notion of a contact structure and provide a more comprehensive deﬁnition. We will
start with dimension3 and deﬁne it for arbitrary dimensions after. Recall:
Deﬁnition1.37.Adistributionon M iscalleda foliation(orintegrable)ifitiseverywheretangenttosubmanifolds
disjointly ﬁllingM.
The Frobeneus theorem characterizes integrable distributions by a formula. Roughly, it says for all vector
ﬁeldsX,Y inξ, the Lie bracket[X,Y ] is inξ. This is both a necessary and suﬃcient condition. In the case of
hyperplane ﬁelds, the Frobeneus theorem is equivalent to:
Theorem 1.38.ξ is integrable if and only if locally there exists a1-formα with ker(α) =ξ such thatα∧dα = 0.
10

1 Plane Fields and Contact Structures
Notice that ifα′ is another form with ker(α′) =ξ, then there exists a nowhere zerof such thatα′ =fα and:
α′∧dα′ =fα∧d(fα) =f2α∧dα
Thereforeasquareof f pullsoutwheneverwetransform αbyα. Thereforethecondition α∧dα = 0isindepen-
dent ofα. Further, a co-orientable hyperplane ﬁeld is integrable if and only if there exists aglobalα such that
ξ = ker(α),α∧dα = 0.6
Example 1.39.Supposeα =dg for someg :M→ R. Then clearlydα = 0, so the associated foliation should be
integrable. The surfaces are precisely the level sets ofg. Ifα = fdg for some positive functionf, then we still
getα∧dα = 0.
Proposition 1.40. Givenα∈ Ω1(M) nonzero andη∈ Ωp(M), thenα∧η = 0 ⇐⇒ η|ξ = 0, whereξ = ker(α).
Proof:
Choose local coordinates atx so thatξx = 0× Rn−1⊂ Rn. Then we writeη = ∑ηIdxI. Notice that
αx = dx1 by construction. Thenα∧η = 0 if and only if all nonzeroηI involvedx1. In other words,
η =dx1∧ζ for someζ atx.
□
Corollary 1.41. Ahyperplanedistribution ξ isintegrableifandonlyif ξ = ker(α)locallyforsome αsuchthat dα|ξ = 0.
Deﬁnition 1.42.A plane ﬁeld on a manifoldM3 is acontact structureif and only if locally it is ker(α) and
α∧dα⁄= 0 everywhere. Equivalently,dα|ξ is never0. In the co-orientable case, we can assume thatα is global.
The ﬁrst observation about this deﬁnition is that it is an open condition. This is what buys us stability, as
mentionedatthestart. Additionally, α∧dαisavolumeform(butitisn’tcanonical,sincewecanalwaysre-scale
byf). However,suchre-scalingonlychangesbyapositivefunctioncoeﬃcient( f2),soatleastthereisacanonical
orientation onM induced byξ. This is true even whenξ is not co-orientable.
Deﬁnition 1.43.A diﬀeomorphismφ : (M,ξ )→ (M′,ξ′)is called acontactomorphismifdφx(ξx) =ξ′
φ(x) at every
point. Equivalently,φ∗(α) =α′ forα,α′ local 1-forms cutting outξ andξ′.
Deﬁnition 1.44.IfM isalreadyoriented, wecall ξ apositivecontactstructureiftheinducedcontactorientation
isthesameastheorientationof M. Thenwewrite α∧dα> 0. Otherwise,itiscalleda negativecontactstructure
and we writeα∧dα< 0.
Deﬁnition 1.45.(from Monograph: Eliashberg-Thurston) A plane ﬁeldξ on an oriented3 manifold M is a
positive confoliationif it is locally given as ker(α) whereα∧dα≥ 0.
1.4.1 Dimension greater than 3
To generalize the deﬁnition of contact structure to arbitrary odd dimensions, we replace “never 0” with “non-
degenerate.” Recall that a bilinear formω on a vector spaceV is non-degenerate if, for allv∈V nonzero, there
existsw∈V such thatω(v,w )⁄= 0. It is skew-symmetric ifω(v,w ) =−ω(w,v ).
Proposition 1.46. A skew symmetric bilinear form is non-degenerate if and only ifω∧n⁄= 0.
Deﬁnition 1.47.A hyperplane ﬁeld on a2n + 1 dimensional manifoldM is acontact structureif ξ = ker(α)
locally anddα|ξ is non-degenerate everywhere (i.e.α∧dα∧...∧dα⁄= 0).
Inthiscase, theparityofthenonzerowedgeformintheabovedeﬁnitiontellsusthat ξ orientsM ifnisodd
andorients ξ ifniseven. Whathappenswhen M isevendimensional? Wecan’tgetfullnon-degeneracy,butwe
cangeta 1-dimensionalnull-spaceof ξ. Therearecalledevencontactstructures,andthey’renotveryinteresting
(for the current discussion, at least). However, even dimensional manifolds can be equipped with a symplectic
structure. This is a closed non-degenerate2-formω∈ Ω2(M).
6This can be done by stitching together local forms using partitions of unity and scaling at their intersections.
11

1 Plane Fields and Contact Structures
y
x
Figure 1.4: The standard contact structure onR3. (Source: Wikipedia)
Example 1.48.LetM = R2n+1 with coordinates(x1,y 1,...,x n,yn,z ). Take then take:
α =dz +
∑
i
xidyi
This is known as the standard contact structure onR2n+1. We noticedα =∑dxi∧dyi. Thenξ = ker(α) is a
contact structure. Sinceα(∂z) = 1, we ﬁnd that∂z is not inξ, so this is a never vertical plane ﬁeld. Forn = 3,
the contact form isα =dz +xdy. The plane ﬁeld is sketched in Figure 1.4.
1.4.2 Contact curves
Deﬁnition1.49.Acurveinacontactmanifold (M3,ξ )isLegendrianifitiseverywheretangentto ξ. Itistransverse
if it is everywhere transverse toξ.
In the Legendrian case forR3, the tangent vectors must satisfydz +xdy = 0. In other words,dz
dy =−x.
Therefore we can recover the curve from itsfront projectionon to they-z plane. Since these planes are never
vertical,closedLegendriancurvesmustcontaincusps(seeFigure1.5). Itturnsouteverylinkin R3 isisotopicto
a Legendrian knot. Given a closed curveC bounding a regionR in thex-y plane, it lifts to a closed Legendrian
curve precisely when:
0 =−
∫
C
xdy =
∫∫
R
dx∧dy = signed area ofR
Remark 1.50. Legendrian curves can be seen as integral submanifolds of maximal dimension. Since we can’t
integrate the plane ﬁeld entirely, the best we can do is integrate it along a curve. This serves as a good deﬁni-
tion of Legendrian submanifolds in higher dimensions: in the presence of a contact structure, they are integral
submanifolds of maximal dimension.
Deﬁnition 1.51.We say two Legendrian links are Legendrian (resp. transverse)isotopic if they are isotopic
through Legendrian (resp. transverse) links.
LegendrianlinksarecompletelydeterminedbytheirfrontdirectionsmoduloLegendrianReidemeistermoves
in the plane. These are exactly analogous to the Reidemeister moves in classical knot theory (see Figure 1.6).
Example1.52. LetM = R3 andξ′ = ker(α′),where α′ =dx+ 1
2r2dθ. Inrectangularcoordinates,thisis xdy−ydx
2 .
This is a positive contact structure becausedα′ = dx∧dy. This produces a cylindrically symmetric contact
structure.
Exercise1.53. Letϕ : R3→ R3beϕ(x,y,z ) = (x,y,z +xy/2). Showthatϕ∗α′ =α,where α′isfromtheexample
above andα is the standard contact structure. This is an example of a contactomorphism.
12

1 Plane Fields and Contact Structures
Figure 1.5: Legendrian knots in they-z plane.
Figure 1.6: Legendrian Reidemeister moves.
13

2. Gray’s Theorem
O
Our next step in understanding contact structures is Gray’s Theorem, which characterizes isotopies of contact
structures. Itisacriticaltoolforunderstandingsubmanifoldsofcontactmanifolds. Inthissection,wewillshow
that Legendrian and transverse knots each respectively have local models that are all the same. While this is
not true for surfaces, we can use similar techniques to glean properties about the characteristic foliation of the
surface, which is a canonical foliation induced by the ambient contact structure.
O
We’ll start with a diﬀerential geometry refresher on Lie derivatives. Given a vector ﬁeldv onMn, locally
we get a ﬂowφt characterized bydφt(p)
dt = v(φt(p)). Givenα∈ Ωp(M), recall that the Lie derivative ofα with
respect tov by:
Lv(α) := d
dt(φ∗
tα)
⏐⏐⏐⏐
t=0
The Lie derivative generalizes the notion of directional derivative. The derivative at any other time is related to
the Lie derivative by:
d
dt(φ∗
tα) =φ∗
tLv(α)
Deﬁnition2.1.Givenavectorﬁeldv,thenthe contractionwithvisamap ιv : Ωp(M)→ Ωp−1(M)byα(v,w 1,...,w p−1) =
ιvα(w1,...,w p−1).
Proposition 2.2.ιv(α∧β) =ιvα∧β + (−1)dimαα∧ιvβ
Theorem 2.3. For a vector ﬁeldv onM, the Lie derivative is given by:
Lv =d◦ιv +ιv◦d
This is a version of Cartan’s formula. We can prove it using the following lemma:
Lemma 2.4. Suppose thatL1,L 2 are local linear operators onp-forms for allp such that:
1. Li◦d =d◦Li.
2. Li(α∧β) =Liα∧β +α∧Liβ.
3. L1 =L2 on Ω0(M).
ThenL1 =L2.
Proof:
Letα∈ Ωp(M)andwrite α =∑αIdxI locally. WenotethatL1(dxi) =d(L1(xi)) =d(L2(xi)) =L2(dxi),
and thereforeL1(dxI) =L2(dxI) for any multi-indexI. Then by properties2 and 3:
L1(α) =
∑
L1(αI)dxI +
∑
αIL1(dxI)
=
∑
L2(αI)dxI +
∑
αIL2(dxI)
=L2(α)
□
Proof (of Theorem 2.3):
14

2 Gray’s Theorem
Apply Lemma 2.4 withL1 =Lv andL2 =d◦ιv +ιv◦d. We have to check each condition:
1. Sincedφ∗α =φ∗dα, we haveLv(dα) =dLv(α). Additionally:
dL2 =d2ιv +dιvd =dιvd
=dιvd +ιvd2
= (dιv +ιvd)d =L2d
2. Exercise.
3. Letf be a 0 form. ThenL2(f) =d(ιvf) +ιvdf =df(v) =Lvf =L1(f).
□
Given a one parameter family of forms,αt∈ Ωp(M), (0≤t≤ 1) we have:
d
dt (φ∗
tαt) =φ∗
t
dαt
dt +φ∗
tLvα (2.0.1)
=φ∗
t
(dαt
dt +d(ιvαt) +ιvdαt
)
(2.0.2)
We claim that this also works isφt is an isotopy, wherev is the velocity ﬁeld of the isotopy. This is the case
whenφt comes from a time dependent vector ﬁeld. This can been seen by deﬁning a vector ﬁeldV onM× R
byV (x,t ) = (vt(x), 1). This is then a time independent vector ﬁeld onM× R, which we can integrate to get a
ﬂow. Restricting to the interval, we get an isotopyM×I→M.
Proposition 2.5. LetV be a ﬁnite dimensional vector space andω a skew symmetric, bilinear form. ThenT : V → V∗
deﬁned byιvω is an isomorphism if and only ifω is non-degenerate.
Proof:
For allv ⁄= 0 in V, there existsw such thatT (v)(w) = ω(v,w )⁄= 0. Therefore T is injective, and is
therefore an isomorphism sincedim(V ) = dim(V∗).
□
Theorem 2.6(Gray’s). Letξt, 0≤t≤ 1 be a (smoothly varying) one parameter family of contact structures onM that
is constant outside a subsetU with compact closure in the interior ofM. Then there exists an isotopyφt :M→M such
thatφ0 = id,φt = id outsideU, andφ∗
tξt =ξ0 for allt.
Proof:
Assume for now thatξ is co-oriented, so thatξt is globally ker(αt) for some 1-form familyαt. For each
t,dαt|ξt is non-degenerate. Then by the Proposition above, there is a unique vector ﬁeldvt onM such
that:
1. vt lies inξt for allt, i.e.ιvt(αt) = 0.
2. ιvt(dαt|ξt) =−dαt
dt|ξt.
Note thatvt doesn’t change if we re-scaleαt. Note that, outsideU,ξt =ξ0 for allt, soαt|ξ0 =αt|ξt = 0.
Then: dαt
dt
⏐⏐⏐
ξt
= dαt
dt
⏐⏐⏐
ξ0
= d
d(αt|ξ0) = 0
Therefore, by property 2 ofvt,vt = 0 for allt outsideU. This means we can integratevt to a globalφt.
15

2 Gray’s Theorem
Now all we must show is thatφ∗
tξt =ξ0. To show this, we diﬀerentiateφ∗
tαt using (2.0.2):
d
dt(φ∗
tαt) =φ∗
t
(dαt
dt +d(ιvαt) +ιvdαt
)
= 0 onξt.
where we used properties 1 and 2 above. Thus we have:
d
dt (φ∗
tαt)
⏐⏐⏐
φ∗
tξt
= 0
Note thatφ∗
tξt = ker(φ∗
tαt), so there must exist someft : M→ R such that d
dtφ∗
tαt = ftφ∗
tαt. For each
x∈M,thiscorrespondstoacurvein T∗
xM whosevelocityisradial(i.e. projectingtothesphereisgives
a constant curve). Thereforeφ∗
tαt is constant up to scaling. This implies then thatφ∗
tξt is constant.
□
Scholium2.7(Darboux’sTheorem). Everycontactmanifoldislocallystandard;thatis,aroundeverypointthere
are coordinates such that the the contact structure is contactomorphic to the standard contact structureξstd.
Proof:
Fix a pointp∈ M. There exists a a linear isomorphismR2n+1 → TpM that sendsξstd to R2n×{ 0}
to ξp (and all orientations agree). Extend this to a local chart aroundp. Let αt = (1 −t)αstd +tα,
where ker(α) = ξ and 0≤ t≤ 1. We noticeαt⁄= 0 at 0, hence near0. Similarly,dαt = (1−t)dαstd +
tdα is a symplectic form in a local chart, which implies thatαt is a contact form for allt on a small
neighborhood. Since ξt is constant at0, vt(0) = 0 for allt (where vt comes from the proof of Gray’s
Theorem). Therefore φt is deﬁned on some neighborhood of0 for allt. Then we compose this chart
withφ1 to get a contactomorphism ofξ andξstd.
□
This is analogous to Darboux’s theorem for symplectic topology. As an aside, a theorem of Cartan gives a
complete list of open conditions on distributions guaranteeing a ﬁxed local model:
1. Contact structures onM2n+1.
2. Evencontactstructureson M2n(theseareclassiﬁeduptohomotopythroughsuchstructuresbyhomotopy
theory).
3. Line ﬁelds (foliations). These are important in dynamical systems.
4. Engel structures: maximally non integrable 2-plane ﬁelds on 4-manifolds (not much known about these).
The following is a generalization of Darboux’s theorem in the case of a dimension3 manifold.
Theorem2.8. SupposeM3 isorientedand N containedintheinteriorof M iscompactconnectedsubset. Let ξ0 andξ1 be
positivecontactstructureson M suchthat ξ0|N =ξ1|N. Thenthereexistsaneighborhood U ofN suchthatid U isisotopic
relN to a diﬀeomorphism that is a contactomorphism nearN.
Proof:
Assumeξ0 andξ1 are co-oriented (the non co-orientable case is similar). Choose contact formsα0 and
α1 inducingthesameco-orientation. Let αt = (1−t)α0 +tα1. NearN,each αt iscontact(since dα0,dα 1
are positive area forms onξ0|N =ξ1|N). Now we apply Gray’s method as in the proof of Scholium 2.7.
□
16

2 Gray’s Theorem
2.1 Local models for Legendrian and transverse knots O
Suppose thatK0⊂ M0 andK1⊂ M1 are transverse knots. Thenξi|Ki is co-orientable, since an orientation on
each knot induces a co-orientation onξi restricted to the knot. There exists a diﬀeomorphism between tubular
neighborhoods ofKi preserving ξi|Ki, by a version of the Tubular Neighborhood Theorem. Now we can ap-
ply Theorem 2.8: every diﬀeomorphism of tubular neighborhoods is isotopic to a contactomorphism. In other
words, all transverse knots have the same local model. The following is one such model that we can easily con-
struct: if we equipR3 with the contact structure ker(dz +r2/2dθ) and mod out by unitz-translations, we get a
transverse knotS1×{ 0}⊂ S1× R2 (given by thez-axis).
What happens for Legendrian knots? LetK1,K 2 be Legendrian, and assumeξ|Ki is co-orientable. Then we
geta contactframing onKi(givenbytakinganormalvectorto Kicontainedin ξiateverypoint). Thenonceagain,
wegetcontactomorphictubularneighborhoodsasbefore, butthecontactframingsmustagreeuptoisotopy. A
standard model for this can be constructed inR3 withξ = ker(dz +xy). They-axis is Legendrian, so we mod
out by unity-translation to get a knot inS1× R2. In the non co-orientable case, instead of a framing we get a
contact line ﬁeld (perhaps not orientable). The standard local model is the same except theZ action now also
ﬂips the other two coordinates:(x,y,z )↦→ (−x,y + 1,−z).
Theorem 2.9. Let (M3,ξ ) be a three manifold with a contact structure. Then:
a) Every transverse knot in(M3,ξ ) has a neighborhood contactomorphic to a neighborhood of thez axis in(R3,dz +
r2/2dθ) mod unitz translations.
b) Every Legendrian knotK withξ|K orientable has a neighborhood contactomorphic to a neighborhood of they axis
in (R3,dz +xdy) mod unity translations.
Recall that from classical knot theory, there are two equivalence relations: isotopy (homotopy through em-
beddings) and ambient isotopy (homotopy through diﬀeomorphisms of the ambient space). For a compact
space, these are the same equivalence relation. This is is a version of the Isotopy Extension Theorem:
Theorem 2.10. Givenft :N→M an isotopy (of embeddings, say) whereN is compact, there exists an ambient isotopy
Φt :M→M with compact support in the interior ofM such thatΦ0 = idM and Φt◦f0 =ft.
Remark 2.11. This only works for the smooth category; it is not true in general topological categories.
Proof:
DeﬁneF : I×N → I×M by (t,n ) ↦→ (t,ft(n)). The tangent vectors give us a vector ﬁeldv on
F (I×N) such thatπ1(v) = 1, whereπ1 is projection onto the time coordinate. Then we extend this to
a compactly supported vector ﬁeld onI×M such thatπ1(v) = 1everywhere. Now there is an induced
ﬂowΦ : I×M→ I×M. Post composing with the projection on toM gives us the desired ambient
isotopy.
□
We would like a similar theorem for the contact category. It is in fact a corollary of Gray’s theorem:
Corollary2.12. Givenψt :M3→M3 anambientisotopywith ψ0 = idM andaﬁxedcontactstructure ξonM. Suppose
also thatψt preservesξ outside a subsetU with compact closure in the interior ofM. Then there exists an ambient isotopy
ψ′
t :M→M through contactomorphisms withψ′
0 = idM agreeing withψt outsideU.
Proof:
Letξt =ψ∗
tξ. Applying Gray’s theorem toξt, we get mapsφt such thatφ∗
tξt =ξ0 =ξ. By deﬁnition of
ξt, we have:
ξ =φ∗
tψ∗
tξ = (ψt◦φt)∗ξ
Now we letψ′
t =ψt◦φt.
□
17

2 Gray’s Theorem
Deﬁnition 2.13.A contact isotopyis an ambient isotopy through contactomorphisms.
Corollary 2.14. Every transverse or Legendrian isotopy of links is realized by an ambient contact isotopy.
2.2 Surfaces and Characteristic Foliations O
The case with surfaces is not as easy as with knots. Whereas we were able to show that every Legendrian or
transverse knot had the same local model in a contact3-manifold, such is not generally the case with surfaces
in a contact3-manifold. However, there is a naturally induced foliation on such surfaces, which is known as a
characteristic foliation.
LetF⊂ (M3,ξ )beasurface,where ξisaplaneﬁeldandeverythingisoriented. Forall x∈F,theintersection
ξx∩TxF hasdimension 1or 2. Thepointswherethisintersectionistransverse(“regularpoints”)givesasingular
line ﬁeldF onF. In the case where they are the same (“singular points”), we get a singular point ﬁeld. The
singular and regular points can be naturally oriented in the following way. A singular point is positive if the
orientations ofξx andTxF agree, and negative if they are opposite. At a regular pointx, orientF so that(v,w )
is a positive basis forTxF ifv positive forFx andw is positively co-oriented forξx.
Example 2.15. Ifξ is a foliation andF is one of the surfaces of the foliation, then the line ﬁeldF is singular
everywhere, and its orientation is either positive or negative everywhere depending onξ.
We would like a vector ﬁeld that cuts outF. Choose α∈ Ω1(M) such that ker(α) = ξ andα(v) > 0 for
positivev. Additionally, letω∈ Ω2(F ) be a positive area form. Deﬁnev onF such thatιv(ω) = α|F. We note
thatvx = 0 if and only if ker(α)x =ξx, which meansx is singular. Elsewhere,α(vx) =ω(vx,vx) = 0 for anyvx,
which meansvx spansFx. Moreover, by construction ofα(v)> 0, the direction ofv agrees with the orientation
ofF.
Corollary 2.16. The ﬁeldF determines a singular foliation by Legendrian curves onF given by integratingv.
This foliation is known as acharacteristic foliation.
Example 2.17. Let M = R3 and F be thex-y plane each with the usual orientation. Consider the contact
structure induced byα = dz +r2/2dθ. The singular point is at the origin, and it is positive. The non-singular
points are radial lines pointing outward (see Figure 2.1).
Example 2.18.Consider againM = R3 andF thex-y plane. Now letα =dz +xdy. The singular points are the
y axis and they are positive. The non-singular curves are lines parallel to thex axis intersecting they axis at a
perpendicular angle. The lines again point away from the singular points (see Figure 2.1).
Theorem 2.19. Let ξ be a positive contact structure onM3 and letF ⊂ M be a surface with induced characteristic
foliationF. Then:
1. The positive singular points ofF are sources, and the negative singular points ofF are sinks.
2. The singular points are nowhere dense.
To prove this, we will have to develop well-deﬁned notion of divergence near singular points ofF.
Deﬁnition 2.20.Given a vector ﬁeldv onMn with a volume formω (that is positive), deﬁne the divergence
divω(v) :M→ RbyLvω = (divωv)ω. Thisiswelldeﬁnedbecausethespaceofvolumeformsisonedimensional.
18

2 Gray’s Theorem
Figure2.1: Characteristicfoliationsofthe x-yplaneundertwodiﬀerentcontactstructuresof R3. Singularpoints
shown in red.
Given positively oriented local coordinates,ω =fdx1∧...∧dxn withf >0. Then by Cartan’s formula:
Lvω =dιvω +ιvdω
=d
( n∑
i=1
(−1)i−1fvidx1∧...∧ˆdxi∧...∧dxn
)
=
n∑
i=1
∂(fvi)
∂xi
dx1∧...∧dxn
= 1
f
n∑
i=1
∂(fvi)
∂xi
| {z }
divωv
ω
Then we can compute the divergence using the product rule:
divωv =
n∑
i=1
∂vi
∂xi
+ 1
f
n∑
i=1
∂f
∂xi
vi
=∇·v +d(ln(f))·v
Note that for the standard area inRn, the functionf is constant, sodivωv =∇·v. Whenv(x) = 0, we again get
divωv =∇·v. The left hand side of this inequality didn’t depend on local coordinates, and the right hand side
doesn’t depend on the choice of volume form. Therefore neither should depend on either. Moreover, at zeros
ofv, the sign ofdivωv doesn’t change under positive re-scaling ofv because:
∇·(gv) =∇g·v +g(∇·v) =g(∇·v)
Lemma 2.21. LetF be an oriented singular line ﬁeld determined byv onM (the zeros are ofv are the singular points
ofF). Supposev(x) = 0 and divωv⁄= 0 atx. Ifw also determinesF nearx, thenw = gv for some smooth function
g :M→ R.
Proof:
19

2 Gray’s Theorem
Away from singular points, we get a uniqueg >0 which is the scale factor betweenw andv. The issue
at a zero is thatv may vanish faster thanw, allowingg to become inﬁnite. Fix local coordinates with
x↔ 0. There existsi such that ∂vi
∂xi
⁄= 0, which means there exists a neighborhoodU of x such that
vi :U→ R is a local submersion at0. By the Local Submersion Theorem, there exists new coordinates
yj such thatvi = y1. Note that the locus wherevi = 0 is the same as wherewi = 0 nearx. Therefore
wi(y1,...,y n) =y1h(y1,...,y n) for some smoothh. Then letg = wi
vi
=h.
□
Deﬁnition 2.22.Under the previous hypothesis, deﬁnesignx(divF) := sign(divωv). If no suchv exists, we say
signx(divF) = 0.
Weclaimthisiswell-deﬁned(independentof ω andcoordinates)becauseitequalsthesignof divωwforany
w =gv and not vanishing to second order atx.
Theorem2.23. GivenF⊂M3beasurfacewithaplaneﬁeld ξonF,everythingoriented. Let signxξ = signx(α∧dα) =
sign(dα|ξx), where ker(α) =ξ. Supposex is a singular point ofF andα|F doesn’t vanish to second order. Then:
signx(divF) = (signxF)(signxξ)
Proof:
Letιvω = α|F for any positive choice ofα,ω such that ker(α) = ξ. Since v doesn’t vanish to second
order, we can use it to compute the sign of the divergence ofF:
(divωv)ω =Lvω =dιvω + 0 =dα|F
Then:
signx(divF) = sign(divωv) = sign(dα|F )
= (sign(dα|ξx))(signxF)
□
As a corollary, we can prove Theorem 2.19. For a positive contact structure,sign(divxF) = signxF, which
meanspositivesingularpointsaresourcesarenegativesingularpointsaresinks. Since signxF isneverzeroby
deﬁnition, the sign of the divergence ofF at a singular point is always nonzero. Therefore the singular locus of
F must locally lie in1 manifolds, and so the second part of Theorem 2.19 also follows.
Exercise 2.24.LetM = R3 and letα =dz +adx +bdy for (a,b )∈ R2−{ 0}. Determinesign(ξ)and divωv forF
on thex-y plane. Check that the characteristic foliation is given byxbya = c. Draw a picture and observe how
these vary witha andb. How issign(divωF) visible?
Theorem 2.25(Giroux et. al.). LetF⊂M3 be a compact surface with boundary (possibly empty) such thatF∩∂M is
a collection of components of∂F. Letξ0,ξ 1 be positive contact structures inducing the the same characteristic foliationF
onF with∂F Legendrian,ξ0 = ξ1 on∂M nearF. Then there exists an isotopyφt of a neighborhood ofF withφ0 = id
and∀t∈ [0, 1],φt(F ) =F preserving each leaf ofF. Moreover,φ∗
1ξ1 =ξ0 andφt ﬁxes eachp∈M on whichξ0 =ξ1.
Proof:
Assumeξ0,ξ 1 areco-orientable(generalcasefollowsbydoublecover). Choose αi suchthatker (αi) =ξi.
Thenweclaimthatthereexists g⁄= 0suchthat α1|F =gα0|F. Thisfollowssince ξ0 andξ1 intersectF in
the same way at regular points ofF. At singular points, ﬁxω onF such thatιviω =αi|F. By last time,
divωvi⁄= 0 atx, and so we getvi =gv0 forg⁄= 0 (see Lemma 2.21). Therefore we can re-scale byg and
wlogα0|F =α1|F.
Claim: Letαt = (1−t)α0 +tα1 for 0≤ t≤ 1. Then there exists a neighborhood ofF such thatαt is
contact for eacht.
20

2 Gray’s Theorem
Proof: Identify a neighborhood ofF with F× R, withz being the R coordinate. Then αt becomes a
family of formsβt,z +ut,zdz, whereβt,z∈ Ω1(F ) andut,z∈ Ω0(F ). Then:
dαt =dβt,z +
(
dut,z− ∂βt,z
∂z
)
dz
and:
αt∧dαt =
(
βt,z∧ (dut,z− ∂βt,z
∂z ) +ut,zdβt,z
)
dz
Notice that, onF,βt,0 anddβt,0 are independent oft sinceαt|F is the same for allt. Therefore atz = 0,
the above expression ofαt∧dαt is aﬃne int (i.e. not quadratic), which implies:
αt∧dαt = (1−t)α0∧dα0 +tdα1∧dα1
Thereforeαt∧dαt is also non-degenerate for allt. We can also extend this to a neighborhood ofF by
continuity. QED.
——————–
Now we apply Gray’s method. We construct the desiredφt by integratingvt such that:
• ιvtαt = 0 (⇐⇒ vt∈ξt).
• ιvtdαt|ξt =−dαt
dt|ξt.
OnF, we also haveαt|F is the same for allF becauseα0|F =α1|F. This impliesdαt
dt|F = 0. Moreover,
we claimvt lies inF. To show this we must demonstratevt ∈ TxF. This is trivial forx singular, so
assumex is regular. Letu spanFx; using the second condition from above:
ιvtdαt(u) =−dαt
dt (u) = 0
⇒dαt(vt,u ) = 0
Non-degeneracy ofdαt saysvt||u, so indeedvt∈TxF. Thereforeφt(F ) =F. The ﬂow restricted toF is
well deﬁned for allt since∂F is Legendrian, so the ﬂow doesn’t escape on the boundary. Therefore we
can extend this ﬂow to a neighborhood ofF and it satisﬁes the required conditions.
□
21

3. Convex Surfaces
O
Up to this point, we have shown that surfacesF inside a contact3 manifold have a canonical directed foliation
whose singular points have a well-deﬁned, nonzero, divergence. We have also shown that given two contact
structures on the ambient manifold inducing the same foliation, there is a contact isotopy sending one to the
other that moves along the leaves. The next step is to allow a perturbation ofF, possibly changing the contact
structure, and see what invariants there are. To do this, we will restrict our focus to convex surfaces, which we
will see carry extra structure in their foliations.
O
Deﬁnition3.1. Givenaplaneﬁeld ξ onM3 andavectorﬁeld v onM tangentto ∂M,wesay v preservesξ ifthe
correspondingﬂowdoes(locally). Inotherwords,if φt istheﬂowof v,then φ∗ξ =ξ. Ifξ iscontact,thenwesay
v is acontact vector ﬁeldif it preservesξ through contactomorphismsφt.
Proposition 3.2. The set of vector ﬁelds onM preservingξ is a vector subspace of all vector ﬁelds onM.
Proof:
Chooseαsuchthat ξ = ker(α). Thenvpreservesξ ifandonlyif Lvα =fvαforsome fv :M→ R. Using
Cartan’s formula:
dιvα +ιvdα =fvα
This is a linear condition inv. That is, if we replacev byaw +bv, the same still holds for the function
afv +bfw.
□
Deﬁnition 3.3.Given a three manifold with a plane ﬁeld(M,ξ ) andF⊂ M is a co-oriented surface, suppose
v is a vector ﬁeld deﬁned nearF tangent to∂M. We sayF is convexwith respect tov ifv preservesξ andv is
positively transverse toF everywhere. If such av exists, we sayF is convex.
A few observations:
a) IfF is convex with respect tov and with respect tow, thenF is convex with respect to(1−t)v +tw for
t∈ [0, 1].
b) If F is compact and convex with respect tov, then we can identify a tubular neighborhood ofF with
F× (−ϵ,ϵ ) so thatv↔ (0, 1) andξ becomes independent of the normal coordinate. Ifξ = ker(α), after
scalingα, we can assumeα is independent of the vertical coordinate as well:Lvα = 0.
Example3.4. Astandardpictureofthesecondobservationis M = R3,α =dz +xdy,and F thex-y plane. Then
F is convex with respect to the vertical vector ﬁeld∂
∂z. Another example is thez-x plane, which is convex with
respect tov = ∂
∂y.
Proposition 3.5.Forξ a contact structure onM andF a surface, anyp∈F∩int(M)has a convex neighborhood inF.
Proof:
Identify a neighborhood ofp inM with (R3,dz +xdy) sendingp↦→ 0. Let w = (1, 0,−y); the corre-
sponding ﬂow isφt(x,y,z ) = (x +t,y,z −ty). We leave it as an exercise to show that this is a contact
ﬂow(i.e.w wascontactvectorﬁeld). a Givenanyvector v = (v1,v 2,v 3)at 0,wecanextendittoacontact
vector ﬁeldv1w +v2 ∂
∂y +v3 ∂
∂z (since contact vector ﬁelds are a vector space). Then choosev transverse
22

3 Convex Surfaces
z
x
y
Figure 3.1: The local model forΓ(z axis),R+ (blue), andR− (red). The contact structure and vector ﬁeld∂
∂y are
shown at three points, one in each region.
toF at 0 and construct such a vector ﬁeld.
aThis can be veriﬁed either by computingφ∗
tα or by computingLwα
□
Letp be a regular point of the characteristic foliation onF induced by a plane ﬁeldξ in the interior ofM.
Thenphaslocalcoordinatesin F suchthatF ishorizontalinthe z-xplane(thisisdonebyusingthe tcoordinate
oftheﬂowasthe xaxis). UsingProposition3.5tochooseany v suchthat F islocallyconvexnear pwithrespect
tov. Inourlocalpicture,wecanidentify vwith ∂
∂y in R3. Sinceα(∂/∂z )> 0,wecanre-scalesothat α(∂/∂z ) = 1.
Sinceα is invariant undery translations, we can write:
α =dz +f(x,z )dy
⇒α∧dα =df∧dy∧dz = ∂f
∂zdx∧dy∧dz
Therefore sign(α∧dα) = sign(∂f/∂x ). Thereforeξ is a positive contact structure if and only if∂f
∂z > 0 (“left
twisting”). In contrast,ξ is a foliation if and only if∂f
∂x = 0.
Nowassume ξ isa positivecontactstructure. Let φ(x,y,z ) = (f(x,z ),y,z ). Noticethatthis isanorientation
preserving local diﬀeomorphism of a neighborhood ofp to thez-x plane because:
detdφ = ∂f
∂x > 0
Additionally,φ∗(dz +xdy) =dz +f(x,y )dy. Therefore we can change coordinates so thatα =dz +xdy. Under
all of this,F is still thez-x plane andF is still parallel to thex axis. This change of coordinates sendsp↦→
(x0, 0, 0). Without loss of generality, ifx0⁄= 0, we can assumex0 =±1 via the contactomorphismψ(x,y,z ) =
(x0/|x0|,y,z/|x0|). These correspond to the three diﬀerent cases ofα(v)> 0,α (v) = 0, andα(v)< 0.
Deﬁnition 3.6.LetF ⊂ (M,ξ ) be a surface convex with respect tov, whereξ is a positive contact structure.
Moreover, assume that everything is oriented and∂F is Legendrian. Thedividing setΓ is{p∈ F| v(p)∈ ξp}.
Similarly, letR± ={p∈F|α(v)>,< 0}.
23

3 Convex Surfaces
Remark 3.7. Notice that these three sets are disjoint andF = R+∪ Γ∪R−. Moreover, R± are open, all of
the positive singularities lie inR+, and all the negative singularities lie inR−. Also notice that each leaf ofF
intersects Γat most once, and the singular points lie inR± depending on their sign.
Theconstructionabovegaveusacanonicallocalmodelforeachofthesethreeregions(showninFigure3.1).
This model proves:
Proposition 3.8. GivenF⊂M convex with respect tov and∂F is Legendrian, thenΓ is an embedded1 manifold with
∂Γ = Γ∩∂F and Γ is everywhere transverse toF. Moreover, the leaves ofF are directed fromR+ toR−.
Our next job is to show that the topology of the dividing setΓdoesn’t depend on the choice of vector ﬁeldv
(i.e. they are all the same up to isotopy).
Theorem 3.9. Γis independent of the choice ofv up to isotopy preserving each leaf ofF.
Proof:
Givenv,w makingF convex, weknowthatF isconvexwithrespectto vt =tv + (1−t)w. Thisgivesus
a one parameter family of dividing setsΓt. Deﬁne:
ˆΓ =
⋃
t∈[0,1]
{t}× Γt⊂I×F
Observethat ˆΓisthezerosetof α(vt),where αisa1-formcuttingoutthecontactstructure. Locally,this
is (dz +xdy)(∂/∂y ) = x. In particular, ∂
∂x (α(vt))⁄= 0, which implies that0 is a regular value ofα(vt).
ThereforeˆΓ is a surface inI×F. Moreover,ˆΓ is everywhere transverse to{t}× F andI×{leaf}. This
meansF∩ (I×{leaf})isacurvewithuniquetangentvectorsprojectingto 1inI. Thesetangentvectors
can be extended to a vector ﬁeld onM that projects to1 onI everywhere. Integrating this vector ﬁeld
gives the desired isotopy.
□
Proposition 3.10. ForF compact, convex, and with Legendrian boundary, the dividing setΓ⁄=∅ for anyv.
Proof:
For anyα with ker(α) =ξ, then by Stokes:
∫
F
dα =
∫
∂F
α = 0
because∂F is Legendrian. SupposeΓ =∅, which means eitherF = R+ orF = R−. OrientF so that
F =R+. Byconvexity,identifyaneighborhoodof F withF× (−ϵ,ϵ )sothat ξ isverticallyinvariant. By
our orientation ofF, we haveα(∂/∂z )> 0 (for an orientation preserving choice of local coordinates, of
course). re-scaleα so thatα = dz +β forβ∈ Ω1(F ). Thendα = dβ and 0 < α∧dα = dβ∧dz, which
impliesdβ is a positive area form onF. However:
0 =
∫
F
dα =
∫
F
dβ >0
Which is a contradiction.
□
Remark 3.11. A similar argument can show the following facts as well:
a) For each compact surfaceΣ⊂R+, the foliationF must ﬂow out of∂Σ at some point.
b) For any positiveα with ker(α) =ξ, we have
∫
R+
dα> 0 and
∫
R−
dα< 0.
24

3 Convex Surfaces
3.1 Giroux’s Theorem O
Nowweconsidertheconverse: givenanysurface F andanysingularfoliation F ofthatsurface,doesthereexist
a contact structure that cuts outF? This is answered (with some assumptions) by Giroux’s theorem.
Deﬁnition 3.12.LetF be any compact, oriented surface andF be an oriented singular foliation ofF. LetΓ be
a compact, co-oriented 1-manifold with∂Γ = Γ∩∂F transversely. We sayΓ dividesF if there exists a positive
contact structure onF× R with characteristic foliationF and dividing setΓ (with respect to∂/∂z, wherez is
the R coordinate), co-oriented byF.
Before we state the theorem, we will establish some terminology. For any closed leaf of the foliationF, we
can deﬁne a monodromy associated to the local behavior of the foliation in a neighborhood of the leaf. Take a
normaldirectiontotheleafandidentifyitwiththeinterval I. Deﬁneφ :I→I byfollowingthefoliationuntilit
intersectsthenormalagain. Wesaythataclosedleafis attractiveifφ′(0)< 1andrepellantifφ′(0)> 1. Moreover,
we deﬁne:
K+ ={+ singular points}∪{ repellant closed leaves}
K− ={− singular points}∪{ attractive closed leaves}
Theorem 3.13(Giroux et. al.). LetF be a compact oriented surface with an oriented singular foliationF such that∂F
is a union of leaves and critical points. Suppose also that:
1. Each leaf limits ast→±∞ to a singular point or closed leaf (t is a parameter on the leaf).
2. Each singular point has nonzero divergence and each closed leaf is either repellant or attractive (i.e.φ′(0)⁄= 1).
3. No leaf runs fromK− toK+.
4. Thecollectionofsingularpointsof F hasﬁnitelymanyconnectedcomponentswhichcanbeorderedsothateachleaf
between points of the same sign preserves that order.7
Then there exists a compact, connected one-manifoldΓ dividingF. Moreover, it is unique to isotopy preserving the leaves
ofF and is characterized as intersecting precisely with those leaves running going fromK+ toK−.
Remark 3.14. The second requirement that each singular point has nonzero divergence is using the fact that
any foliation islocally cut out by a vector ﬁeld vanishing at the singular point. So, for any suchv, the second
condition is sayingdivωv⁄= 0, whereω is a positively oriented volume form onF. This is well-deﬁned by our
discussion of divergence in the previous section (c.f Deﬁnition 2.22).
Proof Idea:
The idea of this proof is to construct globally a volume formω and a vector ﬁeldv to get a uniquely
deﬁned 1-formα :=ιvω onF. This will hand us a contact structure onF and hence a dividing setΓ.
□
Exercise 3.15.Show that the hypotheses of Theorem 3.13 hold for generic a generic foliation ofF.
Corollary 3.16. A generic closed oriented surfaceF in a contact 3-manifold(M,ξ ) is convex.
Proof:
By generic surface, we really mean surface which gives rise to a generic characteristic foliation. Then
Theorem3.13applies, assumingExercise3.15. Thereforethereexistsan R-invariantcontactstructure ξ′
onF× R such thatF is a characteristic foliation induced byξ′ as well. We apply Theorem 2.25 to get a
contactomorphismof F× (−ϵ,ϵ )forsome ϵ> 0andatubularneighborhoodof F. Thismeansthat F is
convex with respect to the image of the vector ﬁeld∂
∂z onF× R under this contactomorphism.
7This rules out leaves that begin and end at the same singular point, among other cases.
25

3 Convex Surfaces
□
3.2 Generic convexity O
With some extra work, we can generalize Corollary 3.16 to generic surfaces with boundary. To do this, we
will need to understand some local models for∂F. From now on in this section,(M3,ξ ) is a positive contact
manifold,ξ is oriented, andF⊂M is a compact oriented surface with Legendrian boundary. AssumeF∩∂M
is a collection of componentsγ ofF. On any boundary component ofF, there are two framings: the normal
framing and the contact framing.
Deﬁnition 3.17.Forγ a component of∂F, thetwisting numberofγ relative toF is the number of right hand
twists of the contact framing relative to the normal framing onγ. It is denotedt(γ).
We can give canonical local models for∂F depending on the twisting number of a componentγ:
• (t(γ)< 0) This model is onR3 modulo unitx translation withξ = ker(sin(2πnx)dy + cos(2πnx)dz). The
surfaceF istheupper z-xhalf-plane. Thenumberofboundarycomponentsof Γis 2n. Whenγ∈∂M,we
can extend this model by locally modeling∂M as thex-y plane with transverse vector ﬁeld∂
∂z.
• (t(γ) = 0)Wemodelthisbythe y axisin R3 modulounit y translationwiththecontactform ξ = ker(dz +
xdy), whereF is thex-y half plane. Whenγ⊂∂M, we can’t get∂M convex ifF is convex (because∂
∂x is
not a contact vector ﬁeld).
• (t(γ)> 0) Finally, whent(γ) > 0, we claim that there is no convex local model. The conclusion is that,
givenF as before with standardF on∂M nearF∩∂M, we can perturbF relative to its boundary to be
convex near∂F if and only ift(γ)≤ 0.
Now we perturbF away from∂F to be generic (Corollary 3.16) so that it is convex and the only singular
points are isolated elliptic and hyperbolic points. How do we glue together these perturbations on the interior
ofF andnear ∂F togetconvexity? Theproblemhappenswhensingularcurvesnear ∂F reachintotheinterior,
where there are only isolated singular points.
Deﬁnition 3.18.Ifp is a point on the boundary of a singular curveC, it ishalf-elliptic if the foliation is locally
modeled by the diagram on the left and it ishalf-hyperbolic if the foliation is locally modeled by the diagram on
the right.
p pC C
Half-elliptic Half-hyperbolic
An explicit model for half-elliptic and half-hyperbolic points is given in the exercise below.
Exercise 3.19.LetF be the graph off : R2→ R deﬁned by:
f(x,y ) =
{ 0 y≤ 0
bxy y ≥ 0
Where we take the contact structuredz +xdy. Show that the singularity at0 is half-elliptic if−1 < b <0 and
half hyperbolic ifb <−1 orb >0. Show also thatξ twists right relative toF ifb <−1 and left relative toF if
b> −1.
26

3 Convex Surfaces
In the above exercise, the surface wasn’t smooth. However, it can be smoothed out on thex axis to give the
same picture of half-elliptic and half-hyperbolic singular points. These are the local models at the edge of the
transition between the two regions. We can choose half-elliptic or half-hyperbolic transitions whent(γ) < 0.
Fort(γ)> 0, we can only choose half-hyperbolic transitions which won’t be convex. If we assume the twisting
is strictly negative, we can glue together the perturbations in a convex manner.
Theorem3.20. GivenF asabove,if ∂M hasastandardcharacteristicfoliationnear ∂F andalltwistingnumbersare ≤ 0,
we can perturbF relative to its boundary to be convex.
3.3 The Flexibility Theorem and LeRP O
What follows is a series of technical theorems about dividing sets on convex surfaces. They are the tools that
allowustoperformmultipleproceduresonconvexsurfacesincontact3-manifoldsthatwillbeuseful. Theﬁrst
is known as Giroux’s ﬂexibility theorem:
Theorem 3.21(Flexibility Theorem). GivenF ⊂ (M,ξ ) a compact surface, convex with respect tov and∂F is Leg-
endrian. LetF1 be the characteristic foliation onF. Suppose thatF0 is another oriented singular foliation with the same
co-orienteddividingset Γ. Thenthereisanisotopy φt :F→M withφ0theinclusionand φ1(F0)inducedby ξ. Moreover,
φt ﬁxesΓ,preserveseachcurve(point)thatisaleaf(singularpoint)ofboth Fi (outsideapreassignedneighborhoodof ∂F),
and eachφt(F ) is convex with respect tov and is contained in a pre-assigned neighborhood ofF.
Proof:
Extendξ toξ1 onF× R so that it isR-invariant. By assumption, we also haveΓ dividingF0, so there
is ξ0 onF× R generatingF0. We claim without loss of generality thatξ0 = ξ1 on U× R for some
neighborhoodU of∂F∪ Γ. Wedothisbyisotopingboth F1,F0 near Γtobeperpendicularlytransverse
to Γ. Fortheboundary,weuseasimilarargumentwhen t(γ) = 0foreachcomponent γ. Whent(γ)< 0,
sincebothfoliationshavethesamedividingset Γ,theirtwistingnumbers(withrespectto ξ1 andξ1)are
the same:t(γ) =− 1
2#Γ∩γ. Then we can arrange the foliations to agree by composing with an isotopy
ofF, and so by Theorem 2.25 we can makeξ1 andξ0 agree onU via an isotopy.
Nowweconsider F\U,whichwecanassumetobeacompactsurface. Let Σbeacomponent. Since
Σ∩Γ =∅,withoutlossofgenerality Σ⊂ R+. OnΣ×R,wecandecomposetheoneforms αidetermining
ξi asαi =dz +βi, forβi∈ Ω1(F ). Letαt = (1−t)α0 +tα1 =dz +βt, where:
βt = (1−t)β0 +tβ1
Then:
αt∧dαt = (dz +βt)∧dβt = (1−t)dβ0∧dz +tdβ1∧dz >0
Now we use Gray’s method. We get an isotopyφt by integratingvt determined by:
1. vt∈ξt.
2. ιvtdαt|ξt =−dβt
dt|ξt.
We see thatvt is R-invariant because all equations above are. On∂Σ× R, we haveα0 = α1 (since the
boundaryiscontainedin U),andtherefore ∂βt
dt = 0⇒vt = 0. Projectingvt awayfromthe Rcomponent,
we get a well-deﬁned vector ﬁeld onΣ and so we also get a global isotopyφt on Σ. For allt∈ [0, 1], we
have thatφt(F ) projects diﬀeomorphically on toF and eachφt(F ) is convex with respect to∂/∂z.
All of these isotopies together give us an isotopyφt such thatφ1(F0) is induced byξ and eachφt
ﬁxesΓ. For any leafL of bothF1,F2, sinceα0|L = α1|L = 0, we haveαt|L = 0 ⇒ dβt
dt|L = 0. This
impliesvt is parallel toL and so it preserves the leaves. All of this works onF× R; but we would like
it to be true forF ⊂ M. To get this, we note that∃a >0 such thatφt(F )⊂ F× [−a,a ]. It suﬃces to
ﬁnd a contactomorphismF× [−a,a ]→F× [−ϵ,ϵ ]forϵ> 0such thatF× [−ϵ,ϵ ]is contactomorphic to
a neighborhood ofF⊂M. We start with an isotopyψt(x,z ) = (x,tz ) fort∈ [ϵ/a, 1]; this isn’t a contact
isotopya priori, so we must modify it. OnF× [−a,a ]writeα1 =udz +β foru∈ Ω0(F )andβ∈ Ω1(F ).
27

3 Convex Surfaces
Thenψ∗
t (α1) = tudz +β := α′
t. Now we apply Gray’s method to getvt such thatιvtdα′
t|ξ′
t =−udz|ξ′
t,
which isR invariant. It is also horizontal by plugging invt:
ιvtdα′
t(vt) = 0 =−udz(vt)⇒dz(vt) = 0
This gives us the desired isotopy.
□
Thenexttheoremtellsuswhenagiventwocurves C and Γcanberealizedasaleafanddividingsetofsome
foliation on a surface. The types of curvesC that we can do this for are what is called non-isolated:
Deﬁnition 3.22.Given a compact1-manifold Γ⊂F, whereF is a surface, a curveC⊂F is callednon-isolating
if every component ofF\ (Γ∪C) has closure intersectingΓ. IfC is instead a collection of curves, we say it is
non-isolating if each of its components is.
Theorem3.23. LetF⊂ (M,ξ )beacompactsurfaceand Γ⊂F beacompact 1-manifoldwith ∂Γ = Γ∩∂F. Assumethat
Γisco-orientedandseparates F intoregions R+,R−, wheretheco-orientationsends R+→R−. Further, letC⊂ int(F )
be a compact1-manifold whose boundary is contained inΓ. Then there exists a singular foliationF divided byΓ with the
property that∂F∪C is a union of leaves and singular points if and only ifC is non-isolated.
Corollary 3.24(LegendrianRealizationPrinciple) . LetF⊂ (M,ξ )beacompact,convexsurfacewith ∂F Legendrian
and dividing setΓ. Let (C,∂C )⊂ (int(F ), Γ) be a non-isolating 1-manifold. Then there is an isotopyφt ofF such that
φt(F ) is convex,φ0 is the inclusion,φ1(Γ) is the dividing set ofφ1(F ) andφ1(C) is Legendrian.
Note that ifC0⊂C is a compact Legendrian submanifold with∂C0⊂ Γ, we can assumeφt preservesC0.
3.3.1 Modifying Dividing Sets
Theorem3.25. LetF⊂ (M,ξ )beconvexwithLegendrianboundaryand F∩∂M =∂F. LetC⊂R+ beanon-isolating
circle in the interior ofF or letC be a boundary component ofF disjoint fromΓ. Then∃ an isotopy ofF relative to its
boundary changingΓby adding a tubular neighborhood ofC toR−.
Proof:
BytheLegendrianRealizationPrinciple(LeRP),wecanassumethat C isLegendrianinbothcases. Since
C∩ Γ =∅, we havet(C) = 0. Therefore the local model forC is they-axis in thex-y plane inR3 with
contactstructure dz+xdy,modulounit ytranslations. Wecanthenlocallyperturb F byaddingawrinkle
nearthe yaxis,asshowninFigure3.2a. Doingsointroducestwonewdividingcurvesthatboundanew
R− region containingC (Figure 3.2b).
□
Deﬁnition 3.26(Honda). A bypass for a convexF ⊂ (M,ξ ) is a convex diskD with Legendrian boundary
transverse toF with part of the boundary contained inF as shown below. Dividing sets are shown in blue and
singular points are shown in red.
Γ
F
28

3 Convex Surfaces
z
x
(a) Adding a wrinkle toF along they axis.
C
Γ
Γ
R+
R+
R−
(b) The resulting foliation ofF year they axis.
Figure 3.2: Perturbation of the surfaceF nearC, as viewed (a) from a transverse slice (x-z plane) and (b) from
above (stretched outx-y plane).
Remark3.27. Wecanassumethereareonlypositivesingularitiesontheboundarycomponentof Dnottouching
F by pairwise canceling positive and negative singular points (using the Flexibility Theorem).
Theorem 3.28(Honda). Given a bypassD, we can isotopeF nearD to be convex with dividing setΓas shown below.
↝
Proof (sketch):
Ifγ is the component ofD contained inF, we can complete it to a Legendrian loop. By LeRP, we can
assume this is a Legendrian circleC ofF (i.e. a leaf ofF). Then we build a wall aboveC underneath
D as shown in Figure 3.3. Note how we have thickened the wall slightly. Our strategy from here will
be to round the corners of this wall, both at its base where it meetsF and on top. The rounding of the
intersection of two surfaces joins their dividing sets as shown below.
↝
The rule is that at an upward bendΓ shifts left and at a downward bendΓ shifts right. When we
round the corners of the wall aboveC, the dividing sets then connect as shown in Figure 3.4. The
resulting dividing set structure is isotopic to what we set out for.
□
29

3 Convex Surfaces
F
C
Figure 3.3: The bypass diskD raised up alongC and thickened. Singular points and curves shown in red,
dividing sets show in in blue.
↝
Figure 3.4: Dividing sets onF after smoothing the edges of the bypass disk and wall.
Example 3.29. Consider the torusT 2. Assume for now that no curve ofΓ bounds a disk. Then all dividing
curvesmustbeparallelandtheremustbeanevennumberofthem(sothattheydivide T 2 intotwowell-deﬁned
regionsR+,R−). Then if there exists a bypassD, we can perform a bypass operation onΓ:
↝ =
Byrepeatingthisoperation,wecanreduce Γtotwodividingcurves. Afurtherbypassoperationtheremain-
ing two dividing curves produces:
30

3 Convex Surfaces
↝ =
This is known as a Dehn twist. At the level of homotopy, if we writeπ1(T 2) =⟨a,b⟩ wherea represents both
components ofΓ, we have multiplied each component ofΓ with by a representative ofb.
ThisconstructionisrelatedtotheclassiﬁcationofcontactstructuresonLensspaces L(p,q )andon T 2-bundles
overS1 done by Giroux and Honda independently.
31

4. Contact structures in 3-Manifolds
O
We now have enough convex surface machinery to begin analyzing and classifying contact structures in3-
manifolds. We’ll begin by proving an important theorem of Martinet, which says that all3-manifolds have
acontactstructure. Fromthere,wewilldeﬁnetightandovertwistedcontactstructures,withsomebriefdiscus-
sion on current knowledge of their classiﬁcation in3 and higher dimensions. From there, the remainder of the
section will specialize to tight contact structures in dimension3, which are in some sense the more interesting
of the two in dimension3.
O
Theorem 4.1(Martinet, ’71). Every closed, oriented3-manifold admits a contact structure.
Proposition 4.2. LetM be an oriented 3-manifold.
(a) Every linkL inM isC0 small isotopic to a Legendrian link.
(b) Every oriented Legendrian linkL inM isC∞ small isotopic to a transverse link that is positive with respect to the
co-orientation ofξ.
Proof:
We can use the standard local model discussed in Section 1.4.2 for each link component. This was the
y axis in (R3,dz +xdy) modulo unity translations. An arbitrarily small horizontal translation in the
x direction will makeL transverse toξ and the orientation induced can be either positive or negative
depending on which direction we translate. This proves part(b).
For part(a), we can assume thatL is generic with respect toξ, which means there are only ﬁnitely
manypointsoftangencyto ξ. Inbetweenthesepoints,we“takethespiralstaircase”near L,whichisan
arbitrarily close (inC0) Legendrian curve nearL. See Figure 4.1.
□
Figure 4.1: Front projection of aC0 Legendrian approximation to a curve inR3. (Source: [3].)
Recall thatS3 = ∂B4⊂ C2 inherits a plane ﬁeld which we will call the standard structure onS3. To do
construct it, writeS3 as the preimage of1 of the functionr2. Therefore ker(d(r2)) alongS3 isTS 3. Moreover,
there is acomplex structureJ onTS 3 inherited fromC2. Writeα =d(r2)◦J. Then weclaim thatξ = ker(α|S3)
is a positive contact form.
Exercise4.3. Verifythatthisisapositivecontactformbyshowingthat d(r2)∧α∧dαisapositivevolumeform
on C2, and thereforeα∧dα is a positive volume form onS3. Do this by showing that:
α =x1dy1−y1dx1 +x2dy2−y2dx2
andcomputing α∧dα. Canyoushowthatthisformrestrictedto S3−{∗} iscontactomorphicto (R3,dz +xdy)?
32

4 Contact structures in 3-Manifolds
Theorem 4.4(Rohlin ’51, Wallace). Every closed, oriented 3-manifold is obtained fromS3 by surgery on a linkL. (i.e.
by cutting a tubular neighborhood ofL out ofS3 and gluing in its placeS1×D2.)
Proof (of Theorem 4.1):
WriteM3 as a surgery onL⊂S3. SinceS3 has the standard contact structureξ constructed above, we
can makeL transverse toξ by Proposition 4.2. The standard model of a transverse circle is thez axis
in (R3,dz +r2/2dθ) modulo unitz translation. In this model, a tubular neighborhood of thez axis is a
torus whose foliation is a collection of lines at constant slope. We call these standard cylinders.
Byexcisinganeighborhoodof Landgluingcopiesof S1×D2togetM,wegetafoliationon ∂(S1×D2)
induced by the contact structure onS3 consisting of lines of a certain slope. We can assume the slope is
nonzero by shrinking the neighborhood. Note that we can changeS1×D2 by a Dehn twist, so without
loss of generality this spiral is left-handed as in the local model we just constructed. Therefore we can
identify∂(S1×D2) with a standard cylinder. Now we apply Giroux’s theorem (Theorem 2.25) to glue
by a contactomorphism in a neighborhood of∂(S1×D2).
□
Remark 4.5. While we used Rohlin and Wallace’s result to prove Martinet’s theorem, this is not how it was
originally proved.
4.1 Tight and Overtwisted Contact Structures O
Deﬁnition 4.6.Suppose K ⊂ (M3,ξ ) is Legendrian and null-homologous. Then for any oriented surfaceF
with∂F =K (knownasa Seifertsurface), wegetaframingon K. Deﬁnetb(K) :=t(K), thetwistingnumberof
K relative to this framing onF. This is known as theThurston-Bennequin invariant.
Remark 4.7. A fact we won’t prove here is that Seifert surfaces for a null homologous knotsK always exist and
always determine the same framing onK (up to homotopy).
Example 4.8. In R3 with the standard contact structure andK with the blackboard framing (from the front
projectionof K),wecallthenumberoftwistsinthisframingrelativeto F iscalledthe writheofK,denoted w(K).
TheThurston-Bennequininvariantisthen tb(K) =w(K)− #of left cusps. Thewrithesoftheknotspicturedin
Figure 1.5 are0 and +3, respectively. The Thurston-Bennequin invariants are then−1 and +1, respectively.
Remark 4.9. It is important to note that any one can add as many left (and right) cusps to a knot as one wishes,
so the Thurston-Bennequin invariant can be made as negative as we wish for any knot.
Deﬁnition 4.10.A contact manifold(M,ξ ) is overtwisted if it has a Legendrian unknotK with tb(K) = 0 .
Equivalently,itisovertwistedifthereexistsanembeddeddisk D⊂M suchthat TpD =ξp forall p∈∂D (called
anovertwisted disk). It is calledtight if it is not overtwisted.
A result of Bennequin in the 70’s is that(R3,ξstd) is tight. The key diﬀerence between tight and overtwisted
is in the regime of maximizingtb(−). If(M,ξ )is overtwisted, we can realize any knot type as Legendrian with
any value oftb(−); if it is tight, then every null-homologous knot has a maximal ﬁnite value oftb(−).
Example4.11. Consider R3 withthecontactstructure dz +r2/2dθ. Modifythecontactstructurebyaddinga 2π
twist in a cylindrical region. In this case, moving out radially fromr = 0 tor =∞ is 2π +π/2 twists (whereas
beforeitwasjust π/2). Thex-y planeisaconvexsurface,withtransversevectorﬁeld ∂/∂z,andwiththecontact
structure we have just constructed, there is a singular circle centered at the origin. This is a null-homologous
Legendrian unknotK with tb(K) = 0. Thus we have constructed overtwisted contact structure. The twist we
introduced to do this is known as aLutz twist.
For any(M3,ξ ) and any unknot, isotope it to be transverse toξ. Identifying it with thez axis in standard
model in the above example, we can perform a Lutz twist to produce an overtwisted contact structureξ′ onM.
Thus, by Martinet’s theorem, every closed, oriented3-manifold has an overtwisted positive contact structure.
33

Theorem 4.20. 4 Contact structures in 3-Manifolds
Example4.12. Nowconsider R3 withα0 = sin(2πnx)dy + cos(2πnx)dz. Letαt = (1−t)α0 +tdx. Onecancheck
that for anyt∈ [0, 1),αt is contact. This is a homotopy through confoliations todx.
The conclusion from theabove example is thatξ′ andξ are homotopic (through confoliations). We have just
unrigorously proved:
Proposition 4.13. Every contact structureξ is homotopic to an overtwisted contact structure.
There are recent stronger statements of this result for both regular contact structures in higher dimensions,
but also for even contact structures. The current thinking is that there is also a similar tight/overtwisted di-
chotomy for Engel structures on four manifolds.
Theorem 4.14(Eliashberg, 1980’s). Every homotopy class of plane ﬁelds on a closed, oriented3-manifold contains a
unique isotopy class of overtwisted contact structures.
Theorem 4.15(Borman, Eliashberg, Murphy ’14). In any odd dimension greater than1, there is a notion of an over-
twisted contact structure. Moreover, they satisfy the h-principle. In other words, the inclusion of overtwisted hyperplane
ﬁelds supporting a non-degenerate 2-form into the space of all contact structures is a homotopy equivalence.
Theorem 4.16(McDuﬀ). Even contact structures onM2n satisfy theh-principle.
Conjecture4.17. Thereexistsatight/overtwisteddichotomy forEngelstructureson M4 andtheovertwistedonessatisfy
theh-principle.
4.2 Euler Classes of Tight Contact Structures O
Thefocusfortheremainderofthisclasswillbedimensionthreemanifoldswithtightcontactstructures. Recall
from Exercise 1.27, for any compact oriented surfaceF, the Euler characteristicχ(F ) ise(TF,v ), wherev is a
nonvanishingvectorﬁeldon ∂F thatiseithernormalto ∂F ortangentto ∂F. Theideaforprovingthisistocap
oﬀtheboundarieswithdisksandextendthevectorﬁeldovertheresultingsurface. ThenusePoincaré-Hopf. If
F⊂ (M,ξ ) is a closed, oriented surface in a contact three-manifold, then we have a natural pairing:
⟨e(ξ), [F ]⟩ = PD(e(ξ))· [F ] =e(ξ|F )∈ Z
IfF insteadhadLegendrianboundary,we’dliketodosomethingsimilar. Agoodchoiceofnonvanishingvector
ﬁeldv on∂F is the tangent vector ﬁeld to∂F, since it is contained inξ.
Deﬁnition 4.18.The rotation numberof F ⊂ (M,ξ ) is r(F ) = e(ξ|F,v ), wherev is as above. If∂F =∅, the
rotation number is juste(ξF ).
Remark4.19. Justasabove,thiscanalsobeseenasthepairing ⟨e(ξ,v ), [F ]⟩inrelativehomologyandcohomology.
It can also be seen asPD(e(ξ,v ))·F where PD(e(ξ,v ))∈H1(M\∂F ).
Supposet(γ) = 0 for each componentγ ofF. PerturbF (rel boundary) to be convex with respect to some
v, which gives usΓ∩∂F =∅. Observe that on∂F,ξ =±TF , so we can changev to be normal to∂F in the
direction of the characteristic foliationF. Then we extendv generically overF so that it generatesF on the
interiorofF. Atthezerosof v,ξ =±TF sowecanperturb ξ tobeequalto ±TF nearthesepoints. Thisensures
indξvx =± indTF vx, whereindξvx is the index ofv when thought of as section ofξ and indTF vx is the index
ofv when thought of a section ofTF . Note that the resulting plane ﬁeld will not be a contact structure. Then:
r(F ) =
∑
v(x)=0
indξvx
=
∑
v(x)=0,x∈R+
indξvx +
∑
v(x)=0,R−
indξvx
=
∑
v(x)=0,x∈R+
indTF vx−
∑
v(x)=0,R−
indTF vx
=χ(R+)−χ(R−)
We have thus proven a special case of:
34

4 Contact structures in 3-Manifolds
Given a compact, convex, oriented surfaceF⊂ (M,ξ ) with Legendrian boundary, thenr(F ) =χ(R+)−χ(R−). In
particular ifF is closed, then⟨e(ξ), [F ]⟩ =χ(R+)−χ(R−).
The proof fort(γ)< 0 uses a similar idea by excising a neighborhood of∂F.
Theorem 4.21(Giroux criterion). LetF⊂ (M,ξ ) be a compact, connected, convex surface with Legendrian boundary
(everything oriented). ThenF has a tight neighborhood if and only if:
• (IfF⁄∼=S2) Γhas no circle bounding a disk inF.
• (IfF∼=S2) Γhas only one component.
Proof:
We will prove the forward implication by contrapositive and not prove the other direction. That is,
assume that both conclusions above are false. Without loss of generality, we claim we can assume that
Γ is not connected. To see this, suppose otherwise, i.e.Γ is connected. ThenF ⁄∼= S2 and Γ is a circle
bounding a disk. We then add a wrinkle by Theorem 3.25 and introduce more components ofΓ, so we
have reduced to the case whereΓis not connected.
Nowweassumethatthereexistsacirclecomponentof Γboundingadisk. Take Γ0acirclecomponent
that contains no other components, andC surrounding Γ0. We note thatC is non-isolating. By LeRP,
we can makeC Legendrian. ThenC bounds an overtwisted disk, so every neighborhood ofF must be
overtwisted (i.e. not tight).
□
Corollary 4.22. Every overtwisted contact structure contains disks as shown below.
•
(a) (b)
•
Where red denotes singular points, black denotes foliation leaves, and blue denotesΓ.
Proof:
UsetheovertwisteddiskconstructedintheproofofTheorem4.21andtheFlexibilityTheoremtorealize
either foliation.
□
Theorem 4.23. ForF⊂ (M,ξ ) a closed, oriented surface, withξ a tight contact structure, let:
ˆF =
∐
Fi⁄∼=S2
Fi
Where eachFi⊂F is a connected component ofF. Assume thatξ is tight. Then|⟨e(ξ),F⟩|≤− χ(ˆF ).
Proof:
35

4 Contact structures in 3-Manifolds
First assume thatF is connected. PerturbF so that it is convex, and apply Theorem 4.21. IfF ∼= S2
(and thereforeˆF =∅) thenR±∼=D2 soχ(R+) =χ(R−) and⟨e(ξ),F⟩ = 0 =−χ(∅) by Theorem 4.20. If
F⁄∼=S2, thenχ(R±)≤ 0. Again by Theorem 4.20, we have:
⟨e(ξ),F⟩ =χ(R+)−χ(R−)≤−χ(F )
because Γ is a disjoint union of circles, meaningχ(Γ) = 0, andF =R+⊔R−⊔ Γ. Doing the same but
withF reversely oriented, gives|⟨e(ξ),F⟩|≤− χ(ˆF ).
Now letF =∐Fi. Then by linear properties of⟨·,·⟩ andχ(−), we have:
|⟨e(ξ),F⟩| =
⏐⏐⏐
∑
⟨e(ξ),Fi⟩
⏐⏐⏐
≤
∑
|⟨e(ξ),Fi⟩|
≤
∑
(−χ(ˆFi)) =−χ(ˆF )
□
Corollary 4.24. For a closed, oriented3-manifold, there are only ﬁnitely many Euler classes of tight contact structures.
In order to prove this, we will use two facts:
1. For any closed, oriented3-manifoldM, a class inH2(M)/torsion∼= H1(M)/torsion is determined by its
pairing withH2(M).
2. Every elementH2(M) is realized by a closed, oriented surface (not necessarily connected).
The Corollary then follows by consideringH2(M) ∼= Zn (there is no torsion in penultimate dimension).
Choose a basis of this module and represent it by surfacesF1,...,F n. Given a tight contact structureξ, we can
consider|⟨e(ξ),Fi⟩|≤− χ(ˆFi). Thereareonlyﬁnitelymanypossibilitiesfor e(ξ)forevery i,byFact1. Therefore
there are only ﬁnitely manye(ξ)∈H2(M)/torsion. Since torsion subgroups are ﬁnite, the Corollary follows.
Remark 4.25. Recall for a ﬁxed trivializationτ ofTM, we get the invariantΓτ deﬁned in Section 1.3. The above
Corollary the also says that there are only ﬁnitely many values ofΓτ realized by a tightξ.
Theorem4.26 (Colin,Giroux,Honda) . Onlyﬁnitelymanyhomotopyclassesofplaneﬁeldsarerealizedbytightcontact
structures.
Example 4.27.M = S1×S2. ThenH2(M)∼= Z generated by{∗}× S2. By Theorem 4.23, every tight contact
structure hase(ξ) = 0. In fact, one can show that there exists a unique tight contact structure onM.
Example 4.28.LetM =T 3 be the3-torus. ThenH2(T 3)∼= Z3. A basis is given by tori each with a single point
in one of the three components. Once again, sinceχ(T 2) = 0, we havee(ξ) = 0 for any tight contact structure
ξ. In this case, all tight contact structures are homotopic through confoliations, however there is more than one
such tight structure.
We can strengthen Theorem 4.23 by consideringF with possibly non-empty boundary and using Theorem
4.20. Note that for a disconnected surfaceF =⊔Fi, the rotation number adds:r(F ) =∑r(Fi).
Theorem 4.29. IfF⊂ (Mξ ) is a compact, oriented surface with Legendrian boundary andξ is tight, lett1,...,t n be the
twisting numbers of the boundary components. Then|r(F )| +∑n
i=1ti≤−χ(ˆF ).
Proof:
As in our proof of Theorem 4.23, it suﬃces to show∑nti−r(F )≤− χ(ˆF ) because we get the other
inequality by reversing the orientation ofF. Without loss of generality, we assume that there are no
components ofF diﬀeomorphic toS2. We also assume that allti≤ 0, so that we can perturbF to be
convex by Theorem 3.20. WriteF =R+⊔ Γ⊔R−. The number of arcs inΓ (i.e. components ofΓ with
36

4 Contact structures in 3-Manifolds
boundary in∂F) is−∑nti, so that:
χ(F ) =χ(R+) +χ(R−) +
n∑
ti
We can place bounds onχ(R±) by considering the number of disks inF bounded byΓ and∂F. The
Giroux criterion rules out interior disks, sinceξ is tight, so that:
#disks≤−
n∑
ti
In particular:
χ(R−) +
n∑
ti≤ 0
Finally:
χ(F ) =χ(R+) +χ(R−) +
n∑
ti
≤χ(R+)−χ(R−)−
n∑
ti
=r(F )−
n∑
ti
The last equality came from Theorem 4.20.
□
We will return to justify the assumption thatti≤ 0 in our proof of Theorem 5.3.
4.3 Classiﬁcation Theory O
Givenaclosed,oriented 3-manifoldM,letT (M)denotethesetofalltight,positive,orientedcontactstructures
moduloisotopy. IfM iscompactwithboundary,thereisaninducedfoliation F on∂M foranycontactstructure.
Assume∂M is convex, and letTF(M, Γ) be the set of all tight, positive, oriented contact structures for a ﬁxed
foliationF on∂M dividedby Γ,moduloisotopy. Similarly,let C(M, Γ)bethesamethingbutwithoutassuming
tightness.
Theorem 4.30. GivenF0,F1 divided byΓ, there is a canonical bijection betweenTF0(M, Γ) andTF1(M, Γ).
Proof (sketch):
Flow∂M withfoliationF0 alongaconvexvectorﬁeldinside M togetanothercopyof ∂M withfoliation
F1 (using the Flexibility Theorem). This extends to a contact isotopy on all ofM, and hence gives us a
mapTF0(M, Γ)→TF1(M, Γ). One can check that it is a bijection.
□
In light of this, we drop the foliation subscript and just writeT (M, Γ). Given two three manifolds(M0,ξ 0)
and (M1,ξ 1)withboundary, theabovetheoremgivesusaprocedureforgluingthemalongtheboundarycom-
ponents with the same dividing setsΓi. The resulting contact structure may not be tight, however. This gives a
canonical map:
T (M0, Γ0)×T (M1, Γ1)→C(M0∪ΓiM1, Γj)
Where Γj are the remaining dividing sets that don’t match up anywhere.
Example4.31. ConsiderM =S2×I. Thereisexactlyonechoiceof Γon∂M thatgivestightcontactstructures,
whichisagreatcirclealongeachcomponent. ATheoremofEliashbergsays T (S2×I, Γ)hasauniqueelement.
37

4 Contact structures in 3-Manifolds
There are some corollaries of this example:
Corollary 4.32.T (B3, Γ) has a unique element andS3, R3 have unique positive tight contact structures.
Proof:
First we assume#T (B3, Γ) = 1. There are two copies ofB3 onS3, the north and south pole caps. The
complementofthesecapsis S3×I. SinceS2×I hasauniquetightcontactstructure,removingthepole
caps leaves us with a unique tight contact structure, and each cap only has one tight contact structure.
Sotheresultofgluingthecapsbackoncanonlyproduceonetightcontactstructureon S3,whichisthe
standard one.
To see that#T (B3, Γ) = 1 and #T (R3, Γ) = 1, we foliate each space by copies ofS2. The details are
left to the reader.
□
Corollary4.33 (Colin,Makar-Limanov). Givenatightthreemanifold (M,ξ ). Letφt :S2→M3beanisotopy. Perturb
it so thatφ0(S2) andφ1(S2) are convex with the same characteristic foliation (using the Flexibility Theorem). Then there
is a contact isotopy sendingφ0(S2) toφ1(S2).
Proof:
For anyt1,t 2 suﬃciently close, there exists aS2×I neighborhood containingφt1(S2) andφt2(S2). We
canmodifytheisotopytopassthroughﬁnitelymanysmoothlyembedded S2×I’s. Withoutlossofgen-
erality,allS2×I boundariesareconvex,sothatthecontactstructureonthe S2×I theyboundisstandard,
and thereforeI invariant. Thus we can modifyφ on [t1,t 2] to be a contact isotopy. Concatenating all of
these perturbed isotopies gives the desired contact isotopy.
□
A basic fact from three manifold theory is that every compact oriented3-manifold has a unique prime de-
composition under connected sum#. Then the question arises: are there any contact structures on the connect
sum that don’t come from gluing two contact structures? The answer is no:
Theorem 4.34(Colin, Makar-Limanov). LetM0,M 1 be connected3 manifolds with respective dividing setsΓ0, Γ1 on
their boundaries. There is a canonical bijectionT (M0, Γ0)×T (M1, Γ1)→T (M0#M1, Γ0∪ Γ1).
Proof:
Suppose we are given(Mi,ξi) tight fori = 0, 1. We want to construct a tight structure onM0#M1. Let
Bi⊂Mi be a three ball with convex boundary. This is unique up to isotopy, which is just a topological
fact. In fact, it is unique up to contact isotopy and perturbation of the foliation on its boundary, by the
Corollary above. We use these to perform the connect sumM0#M1, which induces a contact structure
ξ0#ξ1∈C(M0#M1, Γ0∪Γ1). Thisiswell-deﬁnedbecauseBiwereuniqueuptocontactisotopy. Toshow
thatξ0#ξ1 is tight, suppose it isn’t; then there is an overtwisted diskD inM0#M1 that must intersect
S = ∂B1≡ ∂B2. There is an isotopy shrinkingD to a disk inM1. Reversing this isotopy pushes the
sphereS oﬀ ofD. By the previous Corollary, there is a contact isotopy that does the same thing (up to
perturbingthefoliationon S). Thisgivesusacontactomorphismof (M0#M1,ξ 0#ξ1)pushingSoﬀofD,
which realizes an overtwisted diskD⊂M1, a contradiction. Thereforeξ1#ξ1∈T (M0#,M 1, Γ0∪ Γ1),
hence the map is well-deﬁned.
To show surjectivity, letξ be a contact structure onM0#M1. Take a convex sphereS and cut along
S. Thenglueintightballs Bi toMi. Iftheresultingstructureson M0 andM1 wereovertwisted,thenwe
couldshrink Biawayfromtheovertwisteddiskandﬁndanovertwisteddiskin M0#M1,acontradiction.
So the resulting structure is tight on eachM0,M 1.
To show injective, supposeξ0#ξ1 andξ′
0#ξ′
1 are isotopic contact structures. LetS = ∂(B3) be the
spherealongwhich M1 andM2 wereglued,andlet φt betheisotopyofthetwostructures. Thereisthen
a contact isotopyψ sendingS→φ1(S) by the Corollary above. Then the compositionψ◦φt. This ﬁxes
38

4 Contact structures in 3-Manifolds
S and sendsξ0→ ξ′
0 andξ1→ ξ′
1 on the respective componentsMi− int(B3). This isotopy extends to
all ofMi, so thatξi∼ξ′
i.
□
Corollary 4.35. #T (S2×S1) = 1.
Proof:
WriteS2×S1 as a self sum ofS3 (i.e. S3 glued to itself along two holes) and use Theorem 4.34.
□
4.4 Classiﬁcation using Tori and Lens Spaces O
Consider the Lens spaceL(p,q ), forp andq coprime. This is a quotient ofS3 and is a prime3 manifold (i.e. it
cannot be written as a nontrivial connect sum of two three manifolds).
Theorem 4.36. If [a1,a 2,a 3,...,a m] is the continued fraction expansion of−p
q forp andq coprime, then:
#T (L(p,q )) =
m∏
i=1
(|ai|− 1)
Deﬁnition 4.37.A contact structure onM is calleduniversally tightif it is tight and the pullback to an oriented
cover ofM is also tight.
Deﬁnition 4.38.An embedded torusT 2⊂M is calledincompressibleif the induced mapπ1(T 2)→π1(M)is an
injection. M is calledatoroidalif no such torus exists.
An example of a universally tight contact structure isξm = ker(sin(2πmx)dy + cos(2πnx)dz) on the three
torusT 3. It can be shown that the pullback ofξm to the universal coverR3 is the standard contact structure on
R3, which is tight.
Deﬁnition4.39. TheGirouxtorsion ofacontactthreemanifold (M,ξ )isthemaximal msuch (T 2×I,ξm)canbe
embedded contactomorphically intoM.
The following are a few recent results in classifying contact structures in prime three manifolds.
Theorem 4.40 (Colin et. al. 2000) . Every closed, oriented, prime three-manifold with an incompressible torus has
inﬁnitely many tight structures, each distinguished by Giroux torsion.
Theorem 4.41(Colin, Giroux, Honda). Every closed, oriented, atoroidal three manifold has only ﬁnitely many tight
structures.
Theorem 4.42. A closed, oriented, prime3-manifoldM withH2(M)⁄= 0 admits a universally tight positive contact
structure.
Proof Idea:
The original proof uses a result of Gabai from 1983 which used cut and paste methods to show thatM
admitsatautfoliation. Eliashberg-Thurstoninthemid90’sshowedhowtoperturbatightfoliationinto
a tight contact structure. A newer proof, due to Honda, Kazez, and Matić in 2001, used Gabai’s cut and
paste method directly in a contact setting. TheH2(M)⁄= 0 requirement comes from the fact that you
need a homologically essential foliation to get a taut foliation.
□
39

4 Contact structures in 3-Manifolds
(a) Cross-section of the bubble open
book decomposition of S3. Knot
shown in red.
(b)SeifertsurfaceofanegativeHopflink,which
isaﬁberofthenegativeHopfdecompositionof
S3.
Figure 4.2: Examples of open book decompositions ofS3. Second image source: Jack van Wijk, Eindhoven
University of Technology
Example4.43. ConsiderthePoincaréHomologySphere. Onewaytoconstructitis Σ =SO(3)/icosahedral group.
SinceSO(3)∼= SU (2)/±I andSU (2)∼= S3, the Poincaré Homology Sphere is a quotient ofS3 by a discrete
subgroup ofSU (2). Then the standard structureξ onS3 descends to a tight contact structure onΣ.
Theorem 4.44(Honda). The reversely oriented Poincaré homology sphereΣ admits no positive tight contact structure.
Corollary 4.45. Σ#Σ admits no tight contact structure.
4.5 Using Open Book Decompositions O
Deﬁnition 4.46.An open book decompositionof a three manifoldM is a linkL⊂ M (called thebinding) and a
bundle structureπ :M\L→S1 by Seifert surfaces. In other words,π−1(θ) is the interior of a compact surface
inM whose boundary isL. The ﬁbers ofπ are calledpages.
Example4.47. Thesimplestexampleofanopenbookdecompositionof S3 isgivenbyconsideringthecollection
of“bubbles”boundedbyanunknotinS3(seeFigure4.2a). Anothersuchdecompositionof S3iscalledtheHopf
decompositionH+, which is along positive Hopf links. The negative Hopf decompositionH− is the same but
along negative Hopf links.
Deﬁnition 4.48.Themonodromyof an open book decomposition with ﬁberF isφ :F→F such that:
M\L∼=F×I/(x, 1)∼ (φ(x), 0)
as bundles overS1, whereφ = id near∂F. The monodromy determinesM and the open book decomposition.
Theorem 4.49. Given open booksB0,B 1 for M0,M 1 respectively, there is an open bookB0#B1 on M0#M1. This
depends on the choice of an embedding(I,∂I )↪→ (F,∂F ) for each manifold, whereF is the ﬁber.
Proof:
40

4 Contact structures in 3-Manifolds
It suﬃces to construct this inC0 and then perturb it toC∞. Embed an intervalI into a ﬁberF0 ofM0
so that∂I⊂ ∂F0. Take a tubular neighborhood ofI inM0, which we can take to be a rectangular box
as shown in Figure 4.3a. Since we are working inC0, we can bend the ﬁbers so that the top and bottom
of the box are leaves. Doing this for bothM0,M 1, we then glueM0 andM1 along this ball by matching
the foliations rotated by90degrees (see ﬁgure 4.3b). This operation is called a plumbing. The resulting
manifold has an open book decomposition once we smooth the edges of the box.
□
Deﬁnition4.50.Givenanopenbook B0forM0,itspositiveornegative Hopfstabilization isB0#H±onM0#S3 =
M0.
Returning to the contact setting, we can give an alternative proof of Martinet’s theorem (due to Thurston-
Winkelkemper’75)thatusesopenbookdecompositions. AnoldtheoremofAlexandersaysthatany M3 admits
an open book decompositionB. Choose a1-formβ∈ Ω1(F ), whereF is a ﬁber ofB, such thatdβ is a positive
area form andβ is “standard” near∂F. Letβt = (1−t)β +tφ∗β, where0≤t≤ 1 andφ is the monodromy of
B. Theseareall“standard"neartheboundarybecause φistheidentitynear ∂F,and dβt isapositiveareaform.
Since we are gluingF×I alongφ, this extends to a formη onM\L by extending to theI coordinatez. Let
α =dz +ϵη forϵ> 0. Then:
α∧dα = (dz +ϵη)∧ϵdη
=ϵ( dz∧dη| {z }
(+) vol. form
+ϵη∧dη| {z }
small
)
We can then chooseϵ small enough so thatα∧dα is positive. Moreover, we can extendα toL by pulling back
the standard contact structure of a transverse knot in(R3,dz +r2/2dθ). Thereforeα deﬁnes a contact structure
on all ofM.
4.5.1 The Open Book Correspondence
Deﬁnition 4.51.An open book decompositionB supports a contact structureξ if there exists a one-parameter
family of plane ﬁeldsξt, 0≤ t≤ 1, such thatξ0 = ξ, for allt < 1, ξt is a contact structure transverse to thie
binding, andξ1 deﬁnes the foliation away from the link ofB.
Theorem 4.52. Every open book supports a unique positive contact structure up to isotopy.
Exercise4.53. Showthat H+supportsthestandardcontactstructure ξonS3usingtheHopfﬁbration. Showalso
thatH− supports a diﬀerent homotopy class of contact structure, which must therefore be overtwisted because
#T (S3) = 1.
A fact we won’t prove is that, givenBi supporting ξi on Mi fori = 0, 1, thenB0#B1 supports ξ1#ξ1 on
M0#M1. An immediate corollary, using Exercise 4.53, is:
Corollary 4.54.AnypositiveHopfstabilizationpreservesthecontactstructure. AnynegativeHopfstabilizationgivesan
overtwisted contact structure.
Therefore we have a well-deﬁned map:
{open books onM}/(+) Hopf stab. & isotopy→{ (+) contact structures}/isotopy
AtheoremofGiroux’03saysthatthisismapactuallyabijection. We’llcallthistheOpenBookCorrespondence.
Theorem 4.55(Harer Conjecture). Every ﬁbered link inS3 is made by plumbing and deplumbing Hopf bands, i.e. any
two open books inS3 are related by Hopf stabilizations.
Proof Idea (Goodman ’0?):
41

4 Contact structures in 3-Manifolds
(a)Atubularneighborhoodof I deformedtoaboxwhosetopandbottomareleavesof B0.F shown
in red and all other leaves intersecting the box shown in black.
F0
F1
(b)Gluingtheneighborhoodsof I byarotationby 90degrees. Embed-
dings ofI shown in black.
Figure 4.3: The plumbing operation to construct an open book decompositionB0#B1
42

4 Contact structures in 3-Manifolds
Giventwoopenbooks,lookatthecorrespondingcontactstructuresviathecorrespondenceabove. After
negativeHopfstabilization,theseareovertwisted. ByaddingmorenegativeHopfstabilizations,wecan
arrange these to be homotopic (and overtwisted), and therefore they are isotopic (by Theorem 4.14).
Thereforetheyrepresentthesameequivalenceclassofopenbook,andhencethebookswestartedwith
were related by Hopf stabilizations.
□
Open questions about the Open Book Correspondence:
1. How do we characterize open books supportingtight contact structures? It is known that if the mon-
odromyofanopenbookcanbewrittenasacompositeofrighthandedDehntwists,thenthecorrespond-
ing structure is tight. The converse, however, is not true.
2. What is the minimum genusg of pages of open book supporting a contact structure? Etnyre proved that
ξ overtwisted⇒g = 0. The converse isn’t true, sinceH+ is hasg = 0 but supports the tight structureξstd
onS3.
3. What is the smallest number of binding components supporting a given contact structure?
43

5. Legendrian Knot and Link Theory
O
Suppose we are given an oriented Legendrian knotK⊂ (M3,ξ ) that is nullhomologous. Recall the Thurston-
Bennequin invariant tb(K) = t(F,K ), whereF is a Seifert surface. Another invariant we had wasr(F ) =
⟨e(ξ,v ), [F ]⟩, wherev is tangent toK. A natural question is: under what circumstances isr(F ) an invariant of
K and not ofF? Notice that given Seifert surfacesF1,F 2 forK, we have:
r(F2)−r(F1) =⟨e(ξ,v ), [F2]− [F1]⟩ =⟨e(ξ), [F1−F2]⟩
WhereF1−F2 denotes the disjoint union ofF1 andF 2. To justify the last equality, letj : (M,∗)→ (M,K )
be the inclusion. Thenj∗ : H2(M,K )→ H2(M) is an isomorphism and sendse(ξ,v ) toe(ξ) and moreover
j∗([F1−F2]) = [F1]− [F2]. Then use the fact that⟨j∗·,·⟩ =⟨·,j∗·⟩.
If we assumee(ξ) = 0, the above equality shows thatr(F ) is independent ofF and only depends onK. In
this case, we write it asr(K). Thus we have two knot invariants,tb(K) andr(K) which are preserved under
contactomorphism.
Example 5.1.ForM = R3 withξstd, everyK⊂ R3 is nullhomologous ande(ξ) = 0 becauseH2(R3) = 0. Then
tb(K) andr(K) are deﬁned for all oriented Legendrian knots inR3.
RecallfromExample4.8thatweshowed tb(K) =w(K)−#left cusps,wherew(K)isthewritheof K. Tosee
whatr(K)is,wetrivialize ξ by∂/∂x andmeasuretwistingrelativeto TK. Usingfrontprojections,adownward
left cusp produces a positive twist and an upward right cusp produces a negative twist, so:
r(F ) = #downward left cusps− #upward right cusps
We could have also done this relative to−∂/∂x, to get:
r(F ) = #downward right cusps− #upward left cusps
Yet a third way to describer(F ) comes from averaging the two above:
r(F ) = 1
2 (#downward cusps− #upward cusps)
This is what we will use, since it is least confusing.
Now suppose thatK ⊂ (M,ξ ) is a nullhomologous, positively oriented transverse knot. Given a Seifert
surfaceF forK, we can choose the outward normalv toF to be inξ. Then we deﬁne the self-linking number
𝓁(K) =−⟨e(ξ,v ), [F ]⟩. Again this is independent ofF whene(ξ) = 0.
Proposition 5.2.ForK Legendrianasabove, ithasacanonicalpositivetransversepushoﬀ τK (Proposition4.2b). Then:
𝓁(τK ) = tb(K)−r(K)
Proof:
LetvK betangentto K,vF betheoutwardnormalto F,and vξ bethecontactframingin ξ. Thenr(K) =
⟨e(ξ,vK), [F ]⟩ =⟨e(ξ,vξ), [F ]⟩becausevξ isperpendicularto K. Thisisalsoequalto ⟨e(ξ,vξ, [τF ]⟩,since
τ is a local perturbation of the boundary. Then by deﬁnition oftb(K):
⟨e(ξ,vξ), [τF ]⟩ =⟨e(ξ,vF ), [τF ]⟩| {z }
−𝓁(τK )
+ tb(K)
□
44

5 Legendrian Knot and Link Theory
5.1 Knot Operations O
LetK(M) be the set of all oriented knots in a three manifoldM modulo isotopy. Then letL(M,ξ ) be the set of
allorientedLegendrianknotsmodulocontactisotopy. Alsolet T (M,ξ )bethesetofallpositivetransverseknots
modulo contact isotopy. Then the pushoﬀτ is a mapL(M,ξ )→ T (M,ξ ). Now we will deﬁne stabilizations
S± :L(M,ξ )→L (M,ξ ). To deﬁne these, consider the local model for a Legendrian knotK (R3 modulo unity
translation). Then the stabilization operations are:
K
S+K S−K
ForK as before, we can see thattb(S±K) = tb(K)− 1 andr(S±K) = r(K)± 1. Notice that applying a
stabilization gives us a bypass disk attached toK by ﬁlling in part ofS±K with a family of Legendrian curves:
Where the cusp marked in red became a singular point and the family of curves comprise the foliation on
the bypass.
Theorem 5.3. Forξ tight withe(ξ) = 0 andK∈L (M,ξ ) nullhomologous, oriented, then:
tb(K) +|r(K)|≤− χ(F )
whereF is any Seifert surface ofK.
Proof:
Itsuﬃcestoshowthat tb(K)+r(K)≤−χ(F )(theotherequalitycomesfromreversingtheorientationof
K). From Theorem 4.29, we already know that for any compact, connected, orientedF with nonempty
boundary:
|r(F )| +
∑
i
ti≤−χ(F )
where ti are the twisting numbers of the boundary components, when eachti ≤ 0. Performing S−
enoughtimes,wecanensurethat tb(∂F )≤ 0,sothateach ti≤ 0.a Thisprovestheresult,since tb(K) =
45

5 Legendrian Knot and Link Theory
∑
iti.
aThis also justiﬁes our assumption ofti≤ 0 in our proof of Theorem 4.29
□
As a consequence of this inequality, given any knot inS3, we can deﬁne an invariantTB(K) = max(tb(K)),
where the maximum is taken over Legendrian representativesK ofK.
Theorem 5.4. Letκ :L(M,ξ )→K (M) be the forgetful map. Thenκ induces a bijectionκ :L(M,ξ )/S±→K (M).
Proof Idea:
Surjectivity is a consequence of Proposition 4.2. To show injectivity, we note that an isotopy between
knotsisa1-parameterfamilyofknots. Anytwoknotsrepresentingthesameisotopyclasscanbeapprox-
imated by Legendrian curves and moreover the family of knots that are the isotopy can also be taken to
be Legendrian (we need to allowS± operations on the family to get this work).
□
Theorem 5.5. The transverse pushoﬀτ : L(M,ξ ) → T(M,ξ ) induces a bijectionτ : L(M,ξ )/S− → T(M,ξ ).
Similarly, it induces a bijectionL(M,ξ )/S+→T (M,−ξ).
Proof:
Proposition 4.2b shows thatτ is well deﬁned up to transverse isotopy. First we note thatτS−K = τK.
To show this, look at the standard model ofK in R3 mody translation. The transverse pushoﬀ ofS−K
is positively transverse toξ everywhere and is thus transverse isotopic toτK. This shows thatτ is
well-deﬁned. To show surjectivity, take a tubular neighborhood ofK inT (M,ξ ), which is modeled by
thez axis in(R3,dz +r2/2dθ) modz translation. The Legendrian helix around this neighborhood has
transverse pushoﬀ that is transverse isotopic toK.
To show injectivity, supposeK,K′ ∈L (M,ξ ) with τK and τK′ contact isotopic. Without loss of
generality,τK =τK′. Take a tubular neighborhoodN ofτK such thatK⊂∂N and similarly takeN′
a neighborhood ofτK = τK′ withK′⊂ ∂N′. LetN′′⊂ N∩N′ be a standard tubular neighborhood
ofτK withK′′⊂ ∂N′′ Legendrian withτK′′ = τK. We will show thatK,K′′ are isotopic up toS−,
then the same argument applies toK′,K′′ and henceK andK′ must also be isotopic same up toS−.
We see thatN− intN′′∼=T 2×I with tightξ. Moreover we can assume that it has a convex boundary
and each component has 2 dividing curves. These are classiﬁed. ExtendK to aK×I⊂ T 2×I. The
dividingset ΓonK×I givesbypassescomingfromstabilizations,i.e. K′′ismadefrom K bystabilizing.
Moreover, these stabilizations must be negative because𝓁(τK ) = tb(K)−r(K) being the same forK
andK′′ implies that there can be noS+ stabilizations.
□
Corollary 5.6. ForK∈T (M,ξ ) withξ tight andK nullhomologous, then𝓁(K)≤−χ(F ).
Proof:
WriteK =τK′. Then𝓁(K) =𝓁(τK′) = tb(K′)−r(K′)≤−χ(F ) by Proposition 5.2.
□
5.2 Knot Simplicity O
Theorem5.7 (Eliashberg-Fraser’98,Etnyre-Honda’01). Supposeanorientedknot K isanunknotin (M3,ξ ),ξ tight,
or a torus knot or a ﬁgure eight knot in(S3,ξstd), then Legendrian representatives ofK are classiﬁed bytb(K),r (K) and
46

5 Legendrian Knot and Link Theory
transverse representatives are classiﬁed by𝓁(K). Furthermore, they all come from representatives withtb(K) = TB(K)
byS± andτ operations. Moreover, the maximalTB representative is unique, except for left-handed torus knots.8
This theorem doesn’t generalize to other types of knots, as shown in the next example which uses the fol-
lowing theorem:
Theorem 5.8(Etnyre-Honda ’02). SupposeK = K1#...#Kn inS3, where eachKi is prime. Thenκ−1(K) is given
byκ−1(K1)×...×κ−1(Kn)up to commuting stabilizations between summands and permuting topologically equivalent
summands.
Theproofideaofthisissimilartotheproofwewroteforcharacterizingtightcontactstructureson M1#M2.
In fact, connected sums of knotsKi can be thought of special case of relative connected sums of relative three
manifolds (Mi,Ki).
Example5.9. Considertheconnectsumofreverselyorientedtorusknots K =Tp,q#Tp′,q′ (fordiﬀerentp′,p and
q′,q). WhataretheLegendrianrepresentativesof K with tb(−)maximal? Theabovetheoremsaysthat,foreach
summand tb(−) andr(−) are invariants of maximaltb represenatives ofK. However,r(K) = r(K1) +r(K2)
for anyK =K1#K2, so there are are non-equivalent Legendrian representatives with the same value ofr(−).
Deﬁnition5.10. Aknot K isLegendriansimple (resp. transversesimple)ifitsLegendrian(resp. transverse)repre-
sentatives are classiﬁed bytb(−),r (−) (resp. 𝓁(−)).
It is now known that there exist families of knots that are neither Legendrian simple nor transverse simple.
The ﬁrst examples of Legendrian non-simple knots came from contact homology.
5.3 Stein Manifolds O
Deﬁnition 5.11.A Stein manifoldis a complex submanifold ofCn that is a closed subset.
Remark 5.12. By the Maximum Modulus principle, any Stein manifold cannot be compact.
A simple Stein manifold isCn itself. Lettingφ(z) =||z||2, the level sets of this map are contact manifolds,
(forexample, S3⊂ C2). Thecontactform αisd(r2)◦irestrictedtothelevelsets,where iisthemultiplicationby
i map. This follows from the fact thatdα is the standard symplectic form onCn. More generally, for any Stein
manifoldV,φ|V has contact level sets that are tight. After a generic translation ofV,φ is a Morse function and
all of its critical points have index≤ dimCV = 1
2 dimRV.
Theorem 5.13. A complex manifoldV is Stein if and only if there exists a proper and bounded belowφ : V → R such
that all regular level sets are pseudo convex.
We haven’t deﬁned pseudo convex, but know that it is equivalent to being tight contact away from critical
points fordimCV = 2, and in dimension greater than2 it implies (but is not equivalent to) tight contact away
from critical points.
Theorem 5.14(Eliashberg ’90). A smooth2n manifold forn >2 admits a Stein structure if and only if there exists an
almost complex structure and exhausting Morse function with all indices≤n.
Deﬁnition 5.15.A Stein domainisφ−1((−∞,a ]) for a regular valuea.
Deﬁnition 5.16.(M,ξ ) is calledStein ﬁllableif it is the boundary of a Stein domain.
SinceaSteindomainisaKhälermanifold,itfollowsthatSteinﬁllable ⇒symplecticallyﬁllable,whichimplies
tightness.
Theorem5.17 (Lisca-Matić,Kronheimer-Mrowka). LetF beacompact,connected,orientedsurfaceembeddedsmoothly
inaSteinsurface X (dimCV = 2). IfF isnotanullhomotopicsphere,then F·F +|⟨c1(TX ), [F ]⟩|≤− χ(F ) = 2g(F )−2.
8In the left-hand torus knot case, it is still known which values oftb(−) andr(−) are realized.
47

5 Legendrian Knot and Link Theory
Remark 5.18. For a complex line bundleL,c1(L) =e(L).
Corollary 5.19. SupposeK is a Legendrian knot in the boundary (M,ξ ) of a Stein domainX andF⊂X is a compact,
connected oriented surface with∂F =K. Thentb(K) +|r(F )|≤− χ(F ).
Here,r(F ) denotes⟨c1(TX,v ), [F ]⟩ (sinceF isn’t a subset ofM, we can’t use our previous deﬁnition). This
is a reasonable deﬁnition becausec1(TX )|M =e(ξ). This generalizes Theorem 5.3.
Proof Idea:
Add a 2-handle toX alongK with framingtb(K)− 1. Then we get a new stein surfaceˆF ⊂ ˆX with
ˆF· ˆF = tb(K)− 1 and⟨c1(TX ),ˆF⟩ =r(F ). Sinceχ(ˆF ) = χ(F )− 1, the result follows by the previous
theorem.
□
Remark 5.20. An overtwisted diskD violates this formula becausetb(K) = 0 andχ(D) = 0. This proves that
the standard contact structure onR3 is tight.
Corollary 5.21. ForK⊂S3, TB(K)≤ 2(4-ball genus ofK)− 2.
48

Appendix
A.1 More details on Framed Cobordisms of Framed Links O
InSection1.3,weclaimedthatframedknotsin M inthesamehomologyclasswerecobordantin M×I,andthat
moreover this cobordismF could be embedded inM×I. To justify this, consider the edge homomorphism:
ed: ΩSO
∗ (X)→H∗(M; Z)
For∗≤ 3, this is an isomorphism, which sends[X,f ] to f∗[X]∈ H∗(M; Z). For∗ = 4 it is a surjection
(since the edge map doesn’t see the signature). It’s important to notice that the mapf is not required to be an
embedding (and in general the problem of representing an homology class via an embedded submanifold is
way harder than representing it just via a continuous map). In any case, for1-dimensional homology classes
(i.e. 1 dimensional submanifolds) we can homotope the mapf to be a an embedding, hence we can work with
embedded links representing homology classes.
Notice now that so far, this machinery tells us that whenever two links (which have to be think as pairs
(∐S1,ı )) represent the same homology class inM, there is an abstract cobordism between them. Can we em-
bed such cobordism intoM? (i.e. as a cobordism of links intoM) the answer is yes, and such cobordism takes
the name of Seifert surface. A proof of its existence can be found in [2], page XXI of the introduction.
Fortheexistenceofabordismconnectingthelinks η andη′ wecanargueasfollows. Considerthelongexact
sequence of the pair(M×I,∂ (M×I)), where∂(M×I) = (M× 0)⊔ (M× 1).
H2(M×I,∂ (M×I); Z) H1(∂(M×I); Z) H1(M×I; Z)δ i∗
and consider the element[η]− [η′]∈ H1(∂(M×I); Z). Since they both represent the same class inH1(M; Z),
using the homotopy equivalence betweenM andM×I and the fact that inclusion at level0 is the same map
in homology as inclusion at level1, we have thati∗([η]− [η′]) = 0 ∈ H1(M×I; Z). Hence there is a class
α∈H2(M×I,∂ (M×I); Z) s.t. δ(α) = [η]− [η′]. Since we can represents relative2-homology classes of a four
manifolds with surfaces with boundaries (with given boundary) we conclude that there exists an orientable
surface F whose boundary isη⊔−η′ (where the minus means reverse orientation).F realizes an oriented
cobordism betweenη andη′ inM×I.
Lemma A.1. The Z action onΓ−1(x) for anyx∈H1(M) is transitive.
Proof:
Recall that the action is the deﬁned in the following way: given a linkα0 with a framing, thenn· (α0)
is deﬁned to beα0 with the framing obtained by addingn-twists to the original framing on it. Now
let us consider another linkα1 in Γ−1(x) with its framing. We know that there is an oriented bordism
connectingα0 toα1. We extend, via a partition of unity argument, the framings on these links to the
interiorofthebordism. Clearlytheremightbesomezeroesherebutwecanpushthemoﬀinthedirection
ofα0 in order to get a framing. Doing this, we are changing the framing onα0 by a certain integern.
This means thatn·α0 is framed cobordant toα1, proving transitivity.
□
This shows thatΓ−1(x)∼= Z/mZfor somem(possibly zero). The content of Theorem 1.32 is that the integer
m is twice the divisibility ofx. The proof is as follows:
Proof (of Theorem 1.32):
49

A Appendix
As before, we start working inM×I. Let α be a link inΓ−1(x), then it’s enough to prove that any
framed cobordism betweeni0(α) andi1(α) induced a framing oni1(α) which diﬀers by2d twists form
theframinginducedbythetrivialframedcobordism. Let F besuchframedcobordism. Ifweintroduce
some zeroes on he framing onF we can assume that the framing oni0(α) andi1(α) coincide. Clearly
F is no more a framed cobordism but it keeps being an oriented cobordism, i.e. an oriented compact
surface with boundaryα. This suggests that if we glueM× 0 toM× 1 we can consider˜F,F with the
boundarycomponentsidentiﬁed,tobeasurfacewithoutboundary. Beforedoingthatnoticethatbyour
previous claims it’s enough to computee(NF⊂M×IF ) =F·F. Now thanks to the fact that the framing
on the boundary coincide, the normal bundleNF⊂M×I(F ) factors as a well-deﬁned normal bundle
N ˜F⊂M×S1( ˜F ) and any framing on the ﬁrst induces a framing on the second and vice-versa. Hence we
can computee(N ˜F ) = ˜F· ˜F. Now by Künneth theorem applied toH2(M×S1; Z) we have
H2(M×S1; Z)∼=H1(M; Z)⊗H1(S1; Z)⊕H2(M; Z)
which geometrically means that any2-homology class (for example˜F) is uniquely determined by a2
homology-classβ inM plus a2-homology class represented by a cylinder over a link inH1(M) with
glued boundary components. After moving the surface representingβ toM× 1
2 (parametrized as a
rotation in this "torus"), we see that
˜F· ˜F = ([α×S1] +β)· ([α×S1] +β)
= 2[α×S1]·β
Since the intersection product only cares about a neighbor of where the transverse intersection takes
place, it should be clear that[α×S1]·β = [α×I]·β =kd, wheredis the divisibility ofx = [α]andk is
any integer number. This concludes the proof.
□
50

References
[1] Gompf,Robert.Stipsicz,András. 4-ManifoldsandKirbyCalculus .GraduateStudiesinMathematics,American
Mathematical Society.
[2] Ranicki, Andrew.High-dimensional Knot Theory. Springer Monographs in Mathematics.
[3] Starkston,Laura. ContactStructuresandClassiﬁcationsofLegendrianandTransverseKnots ,Master’sthesis,Har-
vard University.http://www.math.harvard.edu/theses/senior/starkston/starkston.pdf.

