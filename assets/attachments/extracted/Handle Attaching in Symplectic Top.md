Handle attaching in symplectic
topology - a second glance
Alexander Fauck
August 2, 2016
Abstract
We give a corrected proof of Cieliebaks important result on the invariance of
symplectic homology under handle attachment. This paper is partly based on the
authors PhD-thesis, during which he was supported by the Studienstiftung des
deutschen Volkes, the graduate school of the SFB 647, “Raum, Zeit, Materie”,
and the Berlin Mathematical School.
1 Introduction
1.1 Symplectic topology and handle attaching
Symplectic geometry studies the topological, geometrical, dynamical structures of sym-
plectic manifolds, that is of even dimensional manifolds V , dim V = 2n, admitting a
2-form ω such that dω = 0 and ωn is a volume form. Such an ω is called a symplectic
form or structure.
In this program, symplectic topology studies symplectic manifolds with the help of tech-
niques that are similar to whose of algebraic topology in the study of general manifolds.
In particular, it constructs (co)homology theories in order to deﬁne invariants of sym-
plectic manifolds. One of these theories is symplectic homology SH – a Floer-type
homology for compact symplectic manifolds with contact type boundary (see 1.2).
On the other hand, there are topological techniques to construct new symplectic man-
ifolds from existing ones – in particular the attachment of a symplectic handle to a
symplectic manifold along a contact type boundary (see section 2 for a precise deﬁni-
tion). In 2001 Kai Cieliebak, [3], ﬁrst presented the following theorem which relates this
construction with the invariants deﬁned by SH.
1

Theorem 1 (Invariance ofSH under subcritical surgery) .
Let W and V be compact symplectic manifolds with contact type boundary and assume
that the Conley-Zehnder index is well-deﬁned on W . If V is obtained from W by attach-
ing to ∂W× [0, 1] a subcritical symplectic handle H2n
k , k <n, then it holds that
SH∗(V )∼=SH∗(W ) and SH∗(V )∼=SH∗(W ) ∀∗∈ Z.
Applications of this theorem include the vanishing of symplectic homology of subcritical
Stein manifolds, the proof of certain cases of the Cord conjecture (see [3]) and the distinc-
tion of exotic contact structures obtained by handle attachment (see [9]). Unfortunately,
Cieliebaks original proof of this theorem has two ﬂaws:
a) His version of the maximum principle is not strong enough for his purposes.
b) The statement about the existence of only one closed 1-periodic Hamiltonian orbit
on the handle is not true (see 2.3, Discussion 8).
The purpose of this paper is to ﬁx these problems, thus giving a clean and self-contained
proof of this important theorem in symplectic topology. It is organized as follows:
First, we give a short introduction to symplectic homology, prove a strong version of
the maximum principle and construct the transfer maps due to Viterbo. Then, we
study symplectic handle bodies, describe the attaching process and construct speciﬁc
Hamiltonians on them. Finally, we prove Theorem 1 and transfer it to Rabinowitz-Floer
homology with the help of recent results by Cieliebak and Oancea, [7].
1.2 Setup
Let (V,ω ) be a compact symplectic manifold with boundary ∂V = Σ. For the sake of
simplicity, we assume that the symplectic manifold (V,ω ) is a Liouville domain 1, i.e. we
assume that ω is exact with ω = dλ such that the Liouville vector ﬁeld Y deﬁned by
ω(Y,·) =λ points out ofV along Σ. Note that any hypersurface M inV transverse toY
is a contact manifold. That is to say that the 1-form α :=λ|TM is contact, i.e. satisﬁes
α∧ (dα)n−1⁄= 0 pointwise. We write ξ := kerα for the contact structure and R for the
Reeb vector ﬁeld deﬁned by dα(R,·) = 0 and α(R) = 1. The spectrum spec(Σ,α ) of a
contact form α on Σ is then deﬁned by
spec(Σ,α ) ={η∈ R|∃ closed orbit of R with period η}.
A symplectization of a contact manifold Σ with contact formα is a manifoldN = Σ×I,
where I⊂ R is an interval, together with the symplectic form ω :=d(erα), r∈I. The
ﬂowϕY of the Liouville vector ﬁeld on V allows us to identify a collar neighborhood of
Σ =∂V with the symplectization2(
Σ× (−δ, 0],d (erα)
)
,r∈ (−δ, 0], for δ small enough.
1The weaker conditions in [3], namely that
∫
T 2f ∗ω = 0∀f :T 2→V and that ∂V is a convex contact
boundary would also suﬃce.
2In fact, as Y points out of V along Σ and as V is compact, the negative ﬂow of Y stays in V for all
time, thus deﬁning an embedding Σ× (−∞, 0]↪→V .
2

This is in particular possible since
LYω =ιYdω +d(ιYω) = 0 +dλ =ω
LYλ =ιYdλ +d(ιYλ) =ιYω +dω(Y,Y ) =λ,
so that ϕY preservesω and expands α =λ|T Σ exponentially overtime.
The collar neighborhood allows us to deﬁne the completion ( ˆV, ˆω) of (V,ω ) by
ˆV :=V∪ϕY
(
Σ× (−δ,∞]
)
ˆω :=
{
ω on V
d(erα) on Σ × (−δ, 0].
A Hamiltonian on ˆV is a smooth S1-family of functions Ht : ˆV → R with Hamiltonian
vector ﬁeld Xt
H deﬁned by
ω(·,X t
H) =dHt. (for t∈S1 ﬁxed)
The Hamiltonian action of a loop x :S1→ˆV with respect to H is deﬁned by
AH(x) =
∫ 1
0
x∗λ−
∫ 1
0
Ht(x(t))dt.
The critical points of the functional AH are exactly the closed 1-periodic orbits of Xt
H.
We denote the set of these solutions byP(H). Let Jt denote anS1-family ofω-compatible
almost complex structures. As usual, ω-compatible means that ω(·,Jt·) deﬁnes a Rie-
mannian metric for every t. The L2-gradient ofAH with respect to this metric is then
given by
∇AH(x) =−J(∂tx−Xt
H).
AnAH-gradient trajectory u : R×S1→ ˆV is hence a solution of the following partial
diﬀerential equation:
∂su−∇AH = 0 ⇔ ∂su +J(∂tu−Xt
H) = 0 . (1)
In the course of this article, we will be also interested in homotopiesHs of Hamiltonians.
In this case, we call solutions of (1) still AHs-gradient trajectories, where Xt
H is then
depending on s.
For the construction of symplectic (co)homology we look at solutions u of (1) satisfying
lims→±∞ =x±(t)∈P (H). In general, these solutions might not stay in a compact subset
of ˆV , even for x± ﬁxed. Hence, it could be that the moduli space of these solutions has
no suitable compactiﬁcation. To avoid this problem, we make the following restrictions,
which will by Lemma 2 ensure that all solutions of (1) with asymptotics in P(H) stay
in a compact subset of ˆV :
• We call a Hamiltonian H (strongly) admissible , writing H ∈ Ad(V ), if all 1-
periodic orbits of XH are non-degenerate, i.e. if for the ﬂow ϕt
XH of XH holds
det(Dϕ1
XH−Id)⁄= 0 along each 1-periodic orbit x∈P (H), and if H is linear at
inﬁnity, that is if there exist α,β,R ∈ R with α⁄∈ Spec(Σ,λ ) such that H is on
Σ× [R,∞)⊂ˆV of the form
H =α·er +β or more general H =h(er), h : R→ R.
3

• We call a homotopy Hs between admissible Hamiltonians H± admissible if there
exist S,R > 0 such that Hs = H± for±s≥ S and on Σ× [R,∞) the homotopy
has the form
Hs =hs(er) with ∂s∂rHs≤ 0 on Σ × [R,∞).
• We call a Hamiltonian/homotopy H weakly admissible, writing H∈ Adw(V ), if
there exist S,R> 0 such that Hs =H± for±s≥S and on Σ× [R,∞) it has the
form
H =α·er−f(y) +β or H =h
(
er−f(y))
resp. Hs =hs(er−fs(y))
for a function f : Σ→ R. In the homotopy case we require that
(∂s∂rhs)
(
er−fs(y))
− (∂rhs)
(
er−fs(y))
·∂sfs(y)≤ 0, with < 0 on supp∂sf.
If ∂2
rh = 0 (e.g. if h is linear), then this is equivalent to ∂s∂rHs≤ 0.
• We call a possibly s-dependent almost complex structure J (weakly) admissible,
if it is cylindrical and time independent at inﬁnity, that is if
d
(
er−fs
)
◦Js =−λ on Σ × [R,∞)
for an R∈ R. We may write this shorter as d(ers)◦J =−λ for rs :=r−fs.
Lemma 2 (Maximum Principle ).
LetH be a (weakly) admissible Hamiltonian/homotopy and J an admissible almost com-
plex structure. Let x±∈P (H±), where H± are the ends of the possibly constant homo-
topy Hs. Then there exists a constant σ≤ 1 such that for Hσ·s and Jσ·s any solution u
of (1) with lim
s→±∞
u(s) =x± satisﬁes
er◦u(s,t )≤eC ∀(s,t )∈ R×S1
for some constant C≥ R not depending on u. If H is a (weakly) admissible Hamilto-
nian or a strongly admissible homotopy, then we may choose σ = 1, i.e. the Maximum
principle holds already for H and J.
Proof: Our proof is a generalization of similar proofs by A.Oancea,[11], and P.Seidel,
[14]. We give the proof only for homotopies Hs, which includes the Hamiltonian case by
constantHs =H. Let us consider the function ρ : R×S1→ R given by
ρ :=er−fs◦u =ers◦u, where rs :=r−fs.
To ease the notation, we will drop the index s, writing only H,h,f and J. Moreover,
we write h′ instead of ∂rh. However, we keep rs and we write us,ut for ∂su and ∂tu.
4

Calculation of ∆ρ
∂sρ =d
(
ers
)
(us) +
(
∂ser−fs
)
(u) =d
(
ers
)(
−J(ut−XH)
)
+er−fs(u)· (−∂sf)(u)
=λ(ut) +λ(XH)−ρ· (∂sf)(u)
=λ(ut)−ρ·h′(ρ)−ρ· (∂sf)(u),
as λ(XH) =ω(Y,XH) =dH(∂r) =∂rH =ρ·h′(ρ). Moreover, we have
∂tρ =d
(
ers
)
(ut) =d
(
ers
)
(Jus−XH) =−λ(us),
as the orbits of XHs stay in the level sets of ers and hence d
(
ers
)
(XHs) = 0. Therefore,
we obtain for the Lapacian of ρ
∆ρ =∂s
(
λ(ut)−ρ·
[
h′(ρ) + (∂sf)(u)
])
−∂tλ(us)
=dλ(us,ut)−λ( [us,ut]| {z }
=0
)−∂sρ· (∂sf)(u)−
(
−ρ(∂sf)(u) + d
(
ers
)
(us)
)
·h′(ρ)
| {z }
=dH(us)=dλ(us,XH)
−ρ·
[
(∂sh′)(ρ) +h′′(ρ)·∂sρ + (∂2
sf)(u) +d(∂sf)(us)
]
=ω(us,ut−XH| {z }
=Ju s
)−∂sρ·
(
(∂sf)(u) +ρ·h′′(ρ)
)
−ρ·d(∂sf)(us)
−ρ·
[
(∂sh′)(ρ)−h′(ρ)(∂sf)(u) + (∂2
sf)(u)
]
=|us|2−∂sρ·
(
(∂sf)(u) +ρ·h′′(ρ)
)
−ρ·d(∂sf)(us)
−ρ·
[
(∂sh′)(ρ)−h′(ρ)(∂sf)(u) + (∂2
sf)(u)
]
.
Abbreviating g(u) := (∂sf)(u) +ρ·h′′(ρ), we ﬁnd that this is equivalent to
∆ρ +∂sρ·g(u) =|us|2−ρ·d(∂sf)(us)−ρ·
[
(∂sh′)(ρ)−h′(ρ)(∂sf)(u) + (∂2
sf)(u)
]
. (∗)
Now if for C > Rholds on [C,∞)× Σ that the right-hand side of (∗) is non-negative,
thenρ satisﬁes on [C,∞)×Σ a maximum principle and cannot have a local maximum at
an interior point of u−1(
[C,∞)× Σ
)
. As the asymptotics of u lie outside of [C,∞)× Σ,
it follows that ρ =er−fs◦u≤eC everywhere.
Estimate of κ :=|us|2−ρ·d(∂sf)(us)
At ﬁrst glance, this term might be unbounded from below. However, as the Liouville
form λ = er·λ0 grows exponentially in r, we will see that κ is in fact bounded by a
constant, independent of u. Indeed, as d(∂sf) is an r-invariant 1-form, there exists a
vector ﬁeld ξs on Σ, such that
d(∂sf)(·) =dλ( 1
erξs,·) ⇒ ρ·d(∂sf)(us) =dλ(ξs,us).
Forc := sups|Jξs|, we ﬁnd that this last expression is bounded by c·|us|. It will be
usefull to introduce σ at this point. Note that if we replace fs byfσ·s, then κ becomes
|us|2−σ·ρ·d(∂sf)(us). Then, we have
κ =|us|2−σ·ρ·d(∂sf)(us)≥|us|2−σ·c·|us|≥− 1
4c2·σ2. (∗∗)
Here, the last estimate is the minimum of the parabola x2−cσx.
5

Finally note that outside the s-support of ∂sf, we have κ =|us|2≥ 0.
Estimate of the whole right-hand side of (∗)
Let us introduce σ everywhere in (∗). Then, we get the following
∆ρ +∂sρg (u) = |us|2−σρd (∂sf)(us)−ρ
[
σ(∂sh′)(ρ)−σ h′(ρ)(∂sf)(u) +σ2(∂2
sf)(u)
]
(∗∗)
≥ −ρ
[
σ
(
(∂sh′)(ρ)−h′(ρ)(∂sf)(u)
)
+σ2(∂2
sf)(u)
]
− 1
4c2·σ2. (∗∗∗ )
For weakly admissable, we assumed that ( ∂sh′)−h′(ρ)(∂sf)(u)≤ 0 with < 0 on the
s-support of ∂sf. As this support is bounded, we ﬁnd for σ suﬃciently small that
the expression in the brackets is non-positive. Fixing such a σ, we ﬁnd that for ρ >
R suﬃciently large that the right-hand side is in fact non-negative. This proves the
lemma.
Remark. • By decreasing σ, we can in fact achieve that C =R.
• If H is a Hamiltonian or a strongly admissible homotopy, then the term ( ∂2
sf)(u)
is zero and there is no need for a reparametrization by σ, i.e. we can choose σ = 1.
1.3 Symplectic homology
For a (weakly) admissible Hamiltonian H, we deﬁne the Floer homology FH∗(H) as
follows: The chain groups FC∗(H) are the Z2-vector space generated by P(H). Note
that due toh′⁄∈Spec(Σ,α ) and the non-degeneracy of the 1-periodic orbits, we ﬁnd that
P(H) is in fact a ﬁnite set. Thus, FC∗(H) is a ﬁnite vector space of dimension |P(H)|.
Forx±∈P (H) let ˆM(x−,x +) denote the space of solutions u of (1) with lim
s→±∞
u =x±.
There is an R-action on this space given by time shift. The quotient under this action
is called the moduli space of AH-gradient trajectories between x− and x+ and denoted
byM(x−,x +) := ˆM(x−,x +)/R.
For a generic J, the space M(x−,x +) is a manifold. Its zero-dimensional component
M0(x−,x +) is compact and hence a ﬁnite set. Let # 2M0(x−,x +) denote its cardinality
modulo 2. We deﬁne the operator ∂ :FC∗(H)→FC∗(H) as the linear extension of
∂x :=
∑
y∈P(H)
#2M0(y,x )·y.
A standard argument in Floer theory, involving the compactiﬁcation ofM1(y,x ), shows
that ∂2 = 0, so that ∂ is a boundary operator. We set as usual
FH∗(H) := ker∂
im ∂.
To a (weakly) admissible homotopyHs between admissible HamiltoniansH± we consider
forx±∈P (H±) the moduli space of s-dependentAHs-gradient trajectoriesMs(x−,x +).
Note that we have no time shift on this space, as equation (1) now depends on s.
6

We deﬁne the continuation map σ∗(H−,H +) : FC∗(H+) → FC∗(H−) as the linear
extension of
σ∗(H−,H +)x+ =
∑
x−∈P(H−)
#2M0
s(x−,x +)·x−.
By considering homotopies of homotopies, one sees that σ∗(H−,H +) is independent of
the chosen homotopy. By considering the compactiﬁcation of M1
s(x−,x +), we obtain
from Floer theory that∂◦σ∗ =σ∗◦∂, so thatσ∗(H−,H +) is a chain map, which descends
to a mapσ∗(H−,H +) :FH (H+)→FH (H−). For three admissible Hamiltonians H1,H 2
and H3, the maps σ∗ obey the composition rule
σ∗(H1,H 3) =σ∗(H1,H 2)◦σ∗(H2,H 3).
We introduce a partial ordering≺ onAdw(V ) by sayingH+≺H− if and only ifH+ <H−
on Σ×[R,∞) for someR. Observe that admissibility of a homotopyHs betweenH− and
H+ implies that H+≺H−. It follows from the above that the groups FH (H) together
with the maps σ∗(H−,H +) for H+≺ H− deﬁne a direct system over the directed set
(Adw(V ),≺). The symplectic homology groups SH∗(V ) are then deﬁned to be the direct
limit of this system:
SH∗(V ) := lim
−→
FH∗(H).
A coﬁnal sequence (Hn)⊂Adw(V ) is a sequence of Hamiltonians such that Hn≺Hn+1
and for any H∈ Adw(V ) there exists n∈ N such that H≺ Hn. It follows from the
deﬁnition of direct limits that it can be computed from any coﬁnal sequence, i.e. that
SH∗(V ) = lim
n→∞
FH∗(Hn).
More general, a set F⊂ Adw(V ) is coﬁnal if for any H∈ Adw(V ) there exists F∈F
such that H≺F . For coﬁnalF also holds SH∗(V ) = lim
−→
FH∗(F ),F ∈F .
Symplectic (co)homology can be given a Z-grading by the Conley-Zehnder index µCZ .
For that, we restrict ourself to contractible 1-periodic orbits ofXH, which is no restriction
ifV is simply connected. Moreover, we have to assume that
∫
S2s∗c1(TW ) = 0 for every
continuous map s :S2→V .
To compute µCZ (v) for a closed contractible 1-periodic Hamiltonian orbit v choose a
map u from the unit disc D ⊂ C to V such that u(e2πit) = v(t). Then choose a
symplectic trivialization Φ :D× R2n→u∗TV of the pullback bundle (u∗TV,u ∗ω). Such
trivializations exist and are homotopically unique asD is contractible. The linearization
of the Hamiltonian ﬂow ϕt
XH along v with respect to Φ deﬁnes a path Ψ in the group
Sp(2n) staring at 1 by
Ψ(t) := Φ(v(t))−1◦dϕt
XH(v(0))◦ Φ(v(0)).
The Conley-Zehnder index of this path is the index µCZ (v) (see [13] or 2.4 for µCZ of
paths in Sp(2n)). The assumption on the ﬁrst Chern class c1(TV ) guarantees that this
deﬁnition does not depend on the choice of u.
7

1.4 Action ﬁltration
The action functional AH provides ﬁltrations of SH(V ) as follows: For a (weakly)
admissible Hamiltonian H and b∈ R consider the subchain groups
FC<b
∗ (H)⊂FC∗(H),
which are generated by whose x∈P (H) withAH(x)<b . For a<b , we set
FC [a,b)
∗ (H) :=FC<b
∗ (H)
/
FC<a
∗ (H).
We call FC [a,b)
∗ (H) truncated chain groups in the action window [ a,b ). By setting
a =−∞, they include the cases FC [−∞,b)
∗ (H) =FC<b
∗ (H). Analogously one deﬁnes
FC≤b
∗ (B), FC>b
∗ (H) :=FC∗(H)
/
FC≤b
∗ (H), FC≥b
∗ (H),
FC (a,b]
∗ (H), FC(a,b)
∗ (H) and FC [a,b]
∗ (H).
Note that FC [a,b)
∗ (H) = FC (a,b)
∗ (H) if a⁄∈ AH(P(H)). In the following, we restrict
ourself for simplicity to FC (a,b)
∗ (H). However, most of the subsequent results hold also
for all other versions of action windows.
Lemma 3 below shows that the boundary operator ∂ reduces the action. It induces
therefore a boundary operator ∂ on the truncated chain groups and for this ∂ we deﬁne
FH (a,b)
∗ (H) := ker∂
im ∂.
Lemma 3. If H is a Hamiltonian or a (everywhere) monotone decreasing homotopy
and u a solution of (1) with lim
s→±∞
u =x±∈P (H), thenAH(x+)≥A H(x−).
Proof:
AH(x+)−AH(x−) =
∫ ∞
−∞
d
dsAH(u(s))ds
=
∫ ∞
−∞
||∇AH||2ds−
∫ ∞
−∞
∫ 1
0
( d
dsH
)
(u(s))dtds≥ 0.
Note that the second term is zero, if H does not depend on s, i.e. if H is a Hamiltonian.
This shows that the monotone decreasing condition is only needed for homotopies.
Let H−,H + be two (weakly) admissible Hamiltonians such that H− > H+ everywhere.
Then we may choose a monotone decreasing (weakly) admissible homotopy Hs between
them and it follows from Lemma 3 that the associated continuation map σ∗(H−,H +)
also decreases action. We obtain hence a well-deﬁned map
σ∗(H−,H +) :FH (a,b)
∗ (H+)→FH (a,b)
∗ (H−).
The truncated symplectic homology in the action window ( a,b ) is then deﬁned as the
direct limit under these maps:
SH (a,b)
∗ (V ) := lim
−→
FH (a,b)
∗ (H).
8

Attention: Without further restrictions, we have always
SH (a,b)(V ) = 0, for a> −∞ and SH (−∞,b)(V ) =SH(V ) for b< ∞.
To see this, take any coﬁnal sequence of Hamiltonians ( Hn) and take an increasing
sequence (βn)⊂ R such that βn > max
x∈P(Hn)
AHn(x). Deﬁne Kn := Hn +βn−a and
Ln :=Hn +βn−b, which yield also coﬁnal sequence satisfying
max
x∈P(Kn)
AKn(x) = max
x∈P(Hn)
AHn(x)−βn +a<a and max
x∈P(Ln)
ALn(x)<b.
It follows thatFC (a,b)
∗ (Kn) =FH (a,b)
∗ (Kn) = 0 for all n and henceSH (a,b)(V ) = 0, while
FC (−∞,b)
∗ (Ln) =FC∗(Ln) for all n and hence SH (−∞,b)(V ) =SH(V ).
To obtain a meaningful action ﬁltered version ofSH, we hence have to restrict further the
set of admissible Hamiltonians. For us, it will be enough to require that all Hamiltonians
H are smaller then 0 inside a ﬁxed Liouville subdomain 3 W⊂V bounded by a contact
hypersurface ∂W . We write SH (a,b)(W⊂V ) for the direct limit of these Hamiltonians 4,
as this ﬁltration ofSH∗(V ) gives informations about the embedded subdomainW . Note
that diﬀerent choices of W⊂V give diﬀerent ﬁltrations of SH(V )!
We remark that for the deﬁnition ofFH (a,b)
∗ (H) it suﬃces that only the 1-periodic orbits
x ofXH withAH(x)∈ (a,b ) are non-degenerate, as the others are discarded. Therefore,
we call a Hamiltonian H admissible for SH (a,b)
∗ (W⊂V ), writing H∈Ad(a,b)(W⊂V ), if
it satisﬁes
• H|W < 0
• H|Σ×[R,∞) =h(er) for R large
• all x∈P (a,b)(H) ={x∈P (H)|A H(x)∈ (a,b )} are non-degenerate.
The partial ordering on Ad(a,b)(W⊂ V ) is given by H ≺ K if H < K everywhere.
Similar, one deﬁnes weakly admissible Hamiltonians. Note that we are free to choose
for the computation of SH (a,b)(W⊂V ) coﬁnal sequences (Hn) which are also admissible
for the whole symplectic homology or coﬁnal sequences, where the 1-periodic orbits of
XHn are only non-degenerate in the action window ( a,b ).
Note that Ad(W⊂V ) :=Ad(−∞,∞)(W⊂V ) is coﬁnal in Adw(V ), so that
SH (−∞,∞)
∗ (W⊂V ) =SH∗(W⊂V ) =SH∗(V ).
When taking a coﬁnal sequence (Hn)⊂Ad(W⊂V ), we ﬁnd that the projection
FC∗(H)→FC>b
∗ (H) =FC∗(H)
/
FC≤b
∗ (H)
3Liouville subdomain means that W ⊂ V is a codimension 0 submanifold and that the Liouville
structure of W is the restriction of the Liouville structure of V .
4These Hamiltonians coincide with whose deﬁning SH (W ) in the sense of [7]. However, SH (W )⁄=
SH (W⊂V ) in general, as SH (W ) involves also limits over the action window and is hence an
invariant ofW , while SH∗(W⊂V ) is an invariant of V .
9

or the short exact sequence
0→FC (a,b)
∗ (H)→FC (a,c)
∗ (H)→FC (b,c)
∗ (H)→ 0
induce in homology the map
FH∗(H)→FH≥b
∗ (H)
respectively the long exact sequence
···→ FH (a,b)
∗ (H)→FH (a,c)
∗ (H)→FH (b,c)
∗ (H)→...
Applying the direct limit then yields the map
SH∗(V ) =SH∗(W⊂V )→SH>b
∗ (W⊂V )
and (as lim
−→
is an exact functor) the long exact sequence
···→ SH (a,b)
∗ (W⊂V )→SH (a,c)
∗ (W⊂V )→SH (b,c)
∗ (W⊂V )→...
1.5 Symplectic cohomology
By dualizing the constructions from the previous section, we obtain the symplectic
cohomology. Explicitly, we deﬁne for a (weakly) admissible Hamiltonian H the cochain
groups FC∗(H) again as the Z2-vector space generated by P(H). The coboundary
operator δ is then deﬁned as the linear extension of
δx :=
∑
y∈P(H)
#2M0(x,y )·y.
Note that the operator δ increases action. The analogue construction of chain maps
σ∗(H−,H +) associated to an admissible homotopy Hs between Hamiltonians H− and
H+ yields hence a map in the opposite direction (compared to σ∗(H−,H +))
σ∗(H−,H +) :FH∗(H−)→FH∗(H+),
where H− >H + on Σ× [R,∞) for R suﬃciently large. It obeys the composition rule
σ∗(H1,H 3) =σ∗(H2,H 3)◦σ∗(H1,H 2).
By taking the same partial ordering on Adw(V ) as for homology, we obtain hence an
inverse system. The symplectic cohomology SH∗(V ) is then deﬁned to be the inverse
limit of this system
SH∗(V ) := lim
←−
FH∗(H).
Again, it can be calculated using coﬁnal sequences ( Hn) of admissible Hamiltonians.
For the truncated version of symplectic cohomology, we now have to consider
FC∗
>a(H)⊂FC∗(H)
generated by those 1-periodic orbits with action greater then a.
10

Then, we deﬁne
FC∗
(a,b](H) :=FC∗
>a(H)
/
FC∗
>b(H)
and all other truncated groups accordingly. Asδ increases action, it is well-deﬁned on the
truncated chain groups and yields analogouslyFH∗
>a(H) andFH∗
(a,b)(H) as cohomology
groups. When considering only (globally) monotone decreasing homotopies, the chain
maps σ∗ are also well-deﬁned on truncated groups and we obtain as inverse limits
SH∗
>a(W⊂V ) = lim
←−
FH∗
>a(H), SH ∗
(a,b)(W⊂V ) = lim
←−
FH∗
(a,b)(H),
where we restricted again to H∈Adw(W⊂V ).
Unlike to the homology case, the long exact sequence
···→ FH∗
(b,c)(H)→FH∗
(a,c)(H)→FH∗
(a,b)(H)→...
induces in general not a long exact sequence in symplectic cohomology. This is due to
the fact that, in general, the inverse limit is not an exact functor, but only left exact
(see [1] or [8]). However, the inclusion FC∗
>a(H)→FC∗(H) still induces a map
SH∗
>a(W⊂V )→SH∗(W⊂V ) =SH∗(V ).
1.6 The transfer morphisms
In the following, we construct a map π∗(W,V ) : SH∗(V )→ SH∗(W ) for a Liouville
subdomain W⊂ V , as ﬁrst suggested by Viterbo in [16]. Analogously, we construct a
map π∗(W,V ) :SH∗(W )→SH∗(V ) in cohomology. The maps π∗(W,V ) and π∗(W,V )
are called transfer maps and they will provide the isomorphisms in Theorem 1.
As shown above, we have always maps SH∗(V )→SH>0
∗ (W⊂V ) and SH∗
>0(W⊂V )→
SH∗(V ). The maps π∗(W,V ) and π∗(W,V ) are obtained by showing the identities
SH>0
∗ (W⊂V ) = SH∗(W ) and SH∗
>0(W⊂V ) = SH∗(W ). This is done in Corollary 5
by giving an explicit coﬁnal sequence (Hn)⊂Ad(W⊂V ).
The following proposition is based on ideas by Viterbo, [16]. Its proof is taken from
McLean, [10]. We include it here for completeness and to add a missing argument for
the homotopy case. See also Cieliebak, [3], for a slightly diﬀerent approach.
Proposition 4 (McLean,[10]). There exists a coﬁnal sequence (Hn)⊂Ad(W⊂V ) and
a sequence of monotone decreasing admissible homotopies (Hn,n+1) between them such
that
1. Kn := Hn|W, Kn,n+1 := Hn,n+1|W are sequences of admissible Hamiltonians /
homotopies on (W,ω ).
2. all 1-periodic orbits of XHn in W have positive action and all 1-periodic orbits of
XHn in V\W have negative action.
3. all AH-gradient trajectories ofHn orHn,n+1 connecting 1-periodic orbits in W are
entirely contained in W .
11

Proof: It will be convenient to use z =er rather than r for the second coordinate in
the completions (ˆW,ˆω) and (ˆV, ˆω). Note that we can embed ˆW into ˆV using the ﬂow
of the Liouville vector ﬁeld Y . The cylindrical end ∂W× [1,∞) is then a subset of ˆV .
The second coordinates will be denoted zW for ∂W× (0,∞) and zV for ∂V × (0,∞).
Let αW := λ|T∂W , αV := λ|T∂V and assume that Spec(∂W,αW ) and Spec(∂V,α V ) are
discrete. Now let
k : N→ R+\
(
Spec(∂W,αW )∪ 4·Spec(∂V,α V )
)
be an increasing function such that k(n)→∞ . Let µ : N→ R+ be deﬁned by
µ(n) =dist
(
k(n),Spec (∂W,αW )
)
= min
a∈Spec(∂W,αW )
|k(n)−a|.
Choose an increasing sequence A =A(n) with A> 2k
µ > 1 and A(n + 1)> 2A(n)
which satisﬁes additionally the conditions (⊕) and (⊕⊕) below. Note that we can always
achieve 2k
µ > 1, as we may choose k arbitrarily large whilst making µ arbitrarily small.
Let also ε(n)> 0 be a sequence tending to zero.
zW= 1 zW=A z V= 2A+P
B
slopek
slope14k
Fig. 1: The Hamiltonian Hn
Next, we describe the Hamiltonian Hn (see Figure 1 for a schematic illustration). Let
Hn|W be a C2-small negative Morse function inside W\
(
∂W × [1− ε, 1)
)
and for
1−ε≤ zW ≤ A of the form Hn = g(z) with g(1) = −ε, g′≥ 0 and g′≡ k(n) for
1≤ zW≤ A−ε. For A≤ zW≤ 2A let Hn≡ B be constant with B being arbitrarily
close to k· (A− 1).
On ∂V× [1,∞) the Hamiltonain Hn should satisfy the following: Coming from ∂W we
keep Hn constant until we reach zV = 2A +P , where P is some constant such that
{zW≤ 1}⊂{ zV≤P}. Note that this implies {zW≤ 2A}⊂{ zV≤ 2A +P}. Then let
Hn =f(zV ) forzV≥ 2A +P with 0≤f′≤ 1
4k(n) andf′≡ 1
4k(n) forzV≥ 2A +P +ε.
As the action of an XH-orbit on a ﬁxed z-level is h′(z)·z−h(z), we distinguish ﬁve
types of 1-periodic orbits of XH:
12

• critical points inside W of action > 0 (as H is negative and C2-small inside W )
• non-constant orbits near zW = 1 of action≈g′(z)· 1> 0
• non-constant orbits on zW = a for a near A of action ≈ g′(a)· a− B <
(k−µ)·A−B≈−µ·A +k <−k <0
• critical points in A<z W ; zV < 2A +P of action−B <0
• non-constant orbits on zV = a for a near 2A +P of action ≈ f′(a)·a−B ≤
1
4k· (2A +P +ε)−B≈− 1
2kA +k· ( 1
4P + 1
4ε + 1)< 0 for A suﬃciently large (this
is condition (⊕)).
Obviously, (Hn) satisﬁes 1. and 2. of the proposition’s claims. It only remains to show
thatAH-gradient trajectories connecting two orbits of non-negative action are contained
entirely inside zW ≤ 1. By Gromov’s Monotonicity Lemma (see [15], Prop. 4.3.1 and
[12], Lem. 1) there exists a K >0 such that any J-holomorphic curve which intersects
zW = A and zW = 2A has area greater than KA. Note that inside A≤ zW ≤ 2A
the equation (1) reduces to an ordinary J-holomorphic curve equation, as XH ≡ 0
there. Any AH-gradient trajectory connecting two orbits of non-negative action which
intersects zW = A and zW = 2A has therefore area greater than KA – in other words
the action diﬀerence between its ends is greater than KA.
Fork(n) ﬁxed, the maximal action diﬀerence of two 1-periodic orbits in W is bounded
from above. So for A(n) suﬃciently large (this is condition (⊕⊕)) no suchAH-gradient
trajectory can touch zW = 2A. It follows then from the Maximum Principle that in fact
all theseAH-gradient trajectories have to remain inside zW≤ 1.
For the construction of the homotopiesHn,n+1 betweenHn andHn+1 we have to sharpen
this argument. As A(n+1) > 2A(n), we can take forHn,n+1 the following interpolations:
At ﬁrst, in time s∈ [0, 1/2], decrease Hn+1 in the area zW≤ 2A(n) to Hn and keep it
unchanged in zW≥A(n + 1). Then decrease in time s∈ [1/2, 1] the remaining part to
Hn (see Figures 2 and 3).
Fors∈ [−∞, 1/2] the homotopyHn,n+1 is then constantB(n+1) in the area A(n+1)≤
zW≤ 2A(n+1) so that noAH-gradient trajectory can leavezW≤ 1 in this time interval.
Fors∈ [1/2,∞] the homotopy Hn,n+1 is constant B(n) in the area A(n)≤zW≤ 2A(n)
so that again noAH-gradient trajectory can leave zW≤ 1 in this time interval.
Corollary 5. SH>0
∗ (W⊂V )≃SH∗(W ) and SH∗
>0(W⊂V )≃SH∗(W ).
Proof: We only prove the corollary for homology, cohomology being completely analog.
Take the sequence of Hamiltonians (Hn) constructed in Proposition 4. Clearly it is coﬁnal
and (Hn)⊂ Ad>0(W⊂V ), as 1-periodic orbits with positive action are either isolated
critical points inside W (asH is Morse and C2-small there) or isolated Reeb-orbits near
zW = 1 – in both cases non-degenerate. Hence we have
SH>0
∗ (W⊂V ) = lim
−→
FH>0
∗ (Hn).
13

Let ˜Hn ∈ Ad(W ) be the linear extension of Hn|W with slope k(n). Due to
k(n)⁄∈ Spec(∂W,λ ), we have obviously FC>0
∗ (Hn) = FC∗( ˜Hn). As any AH-gradient
trajectory connecting 1-periodic orbits inW stays inW , the two boundary operators∂Hn
and∂ ˜Hn coincide and we have FH>0
∗ (Hn) =FH∗( ˜Hn). As the AH-gradient trajectories
for the homotopies Hn,n+1 stay inside W , the continuation maps
σ(Hn+1,Hn) :FH>0
∗ (Hn)→FH>0
∗ (Hn+1)
coincide with the continuation maps
σ( ˜Hn+1, ˜Hn) :FH∗( ˜Hn)→FH∗( ˜Hn+1).
Hence we have SH>0
∗ (W⊂V ) = lim
−→
FH>0
∗ (Hn) = lim
−→
FH∗( ˜Hn) =SH∗(W ).
Hn
Hn+1
zW= 1A(n) 2A(n)A(n+ 1) 2A(n+ 1)
B(n+1)
B(n)
Fig. 2: Two Hamiltonian Hn and Hn+1
zW= 1A(n) 2A(n)A(n+ 1) 2A(n+ 1)
B(n+1)
B(n)
Fixed for times≥12 Fixed for times≤12
Fig. 3: The homotopy Hn,n+1 at time s = 1
2
14

2 Contact surgery and handle attaching
In this section, we describe the general construction for contact surgery, which is done by
attaching a symplectic handle H2n
k to the symplectization of a contact manifold. Then,
we describe the symplectic standard handle, which is a subset of R2n deﬁned as the
intersection of two sublevel sets {ψ <−1}∩{ φ >−1}, where φ and ψ are functions
on R2n. While φ is explicitly given, we describe the construction of a suitable ψ in 2.3.
Simultaneously, we describe how to extend an admissible Hamiltonian over the handle
to a new admissible Hamiltonian with only few new 1-periodic Hamiltonian orbits. The
calculation of Conley-Zehnder indices for these orbits on H2n
k and the proof of the main
theorem conclude the section.
2.1 Surgery along isotropic spheres
Let us brieﬂy recall the contact surgery construction due to Weinstein, [17]. Consider an
isotropic sphereSk−1 in a contact manifold (N 2n−1,ξ ). The 2-form ω =dλ for a contact
form λ (with ξ = kerλ) deﬁnes a natural conformal symplectic structure on ξ. Denote
the ω-orthogonal on ξ by⊥ω. Since S is isotropic, it holds that TS ⊂ TS⊥ω. So, the
normal bundle of S in N is given by
TN/TS =TN/ξ ⊕ ξ/(TS )⊥ω⊕ (TS )⊥ω/TS.
The Reeb ﬁeld Rλ trivializes TN/ξ . The bundle ξ/(TS )⊥ω is canonically isomorphic to
T∗S via v↦→ ιvω. The conformal symplectic normal bundle CSN (S) := (TS )⊥ω/TS
carries a natural conformal symplectic structure induced by ω.
Since S is a sphere, the embedding Sk−1⊂ Rk provides a natural trivialization of the
bundle RRλ⊕T∗S. This trivialization together with a conformally symplectic trivializa-
tion of CNS (S) speciﬁes a standard framing for S in N. Note that we have to assume
thatCNS (S) is trivializable. This holds certainly true forS =S0 ={N,S} (two points)
orS =Sn−1. In the latter case we have (TS )⊥ω =TS and henceCNS (S) = (0). There-
fore, taking connected sums and surgery along Legendrian spheres is always possible.
Following Weinstein, we deﬁne an isotropic setup as a quintuple ( P,ω,Y, Σ,S ), where
(P,ω ) is a symplectic manifold, Y a Liouville vector ﬁeld for ω, Σ a hypersurface trans-
verse to Y (so Σ is contact) and S an isotropic submanifold of Σ. In [17], Weinstein
proves the following variant of his famous neighborhood theorem for isotropic manifolds:
Proposition 6 (Weinstein). Let (P0,ω 0,Y 0, Σ0,S 0) and (P1,ω 1,Y 1, Σ1,S 1) be two iso-
tropic setups. Given a diﬀeomorphism from S0 to S1 covered by an isomorphism of
their symplectic subnormal bundles, there exist neighborhoods Uj of Sj in Pj and an
isomorphism of isotropic setups
φ : (U0,ω 0,Y 0, Σ0∩U,S 0)→ (U1,ω 1,Y 1, Σ1∩U1,S 1)
which restricts to the given mappings on S0.
We may now deﬁne contact surgery along an isotropic sphere as follows:
15

Let H2n
k ≈ Dk×D2n−k be a symplectic standard handle (see 2.2) and let Sk−1 be an
isotropic sphere in a contact manifold (N 2n−1,ξ ). Then, Proposition 6 allows us to glue
the (lower) boundary Sk×D2n−k of H2n
k to the symplectization N× [0, 1] along the
boundary part U1∩N× [0, 1] of a tubular neighborhood U1 of S×{ 1} (see Figure 4).
We obtain an exact symplectic manifold P :=N× [0, 1]∪SH2n
k with a Liouville vector
ﬁeld Y which is on N× [0, 1] simply ∂
∂t , where t denotes the coordinate on [0 , 1]. Note
that Y points inwards along ∂−P := N×{ 0} and outwards along the other boundary
component ∂+P . Both manifolds are hence contact and ∂+P is obtained from N by
surgery along S. Moreover, P is an exact symplectic cobordism between ∂−P and∂+P .
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/0/0/0/0/0/0/0/0/0
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
/1/1/1/1/1/1/1/1/1
Sk−1
N×[0,1]
Sk−1
H2nk
Fig. 4: N× [0, 1] with handle attached
2.2 A standard handle
In order to specify a standard handle H2n
k , we consider R2n with symplectic coordinates
(q,p ) = (q1,p 1,...,q n,pn) and the following Weinstein structure (cf. [17]):
λ :=
k∑
j=1
(2qjdpj +pjdqj) +
n∑
j=k+1
1
2 (qjdpj−pjdqj)
dλ =ω :=
n∑
j=1
dqj∧dpj
Y :=
k∑
j=1
(
2qj
∂
∂qj
−pj
∂
∂pj
)
+
n∑
j=k+1
1
2
(
qj
∂
∂qj
+pj
∂
∂pj
)
φ :=
k∑
j=1
(
q2
j− 1
2p2
j
)
+
n∑
j=k+1
Aj
2
(
q2
j +p2
j
)
, A j > 0 const.
Note that Y is in fact the Liouville vector ﬁeld for λ, as ιYω = λ. Moreover, observe
that (Y·φ)(q,p )> 0 for (q,p )⁄= (0, 0).
16

Let us introduce furthermore the following three functions:
x :=
k∑
j=1
q2
j y :=
k∑
j=1
1
2p2
j z :=
n∑
j=k+1
Aj
2
(
q2
j +p2
j
)
,
whose Hamiltonian vector ﬁelds are given by
Xx =
k∑
j=1
2qj
∂
∂pj
, X y =
k∑
j=1
−pj
∂
∂qj
, X z =
n∑
j=k+1
Aj
(
qj
∂
∂pj
−pj
∂
∂qj
)
.
This convention allows us to write φ =x−y +z and Xφ =Xx−Xy +Xz.
Now, consider the level surface Σ − :={φ =−1} and note that Y is transverse to Σ−,
as Y·φ|Σ− > 0. Hence, λ|T Σ− is a contact form. The set S :={x =z = 0, y = +1} is
an isotropic sphere in Σ− and the quintuple (R2n,ω,Y, Σ−,S ) will be the isotropic setup
where we glueH2n
k to a contact manifold. To specify a handle H2n
k , we choose a diﬀerent
Weinstein functionψ on R2n such that the following holds:
(ψ1) Xψ =Cx·Xx +Cy·Xy +Cz·Xz,
where Cx,CY,Cz are smooth functions on R2n such that Cx,Cz > 0, Cy < 0.
(ψ2) ψ =φ for y >1 +ε with ε arbitrarily small.
(ψ3) The closure {ψ <−1}∩{ φ> −1} is diﬀeomorphic to Dk×D2n−k.
/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
y= 1 +ε φ=−1
φ=−1
S
S
ψ=−1
ψ=−1
y= 1 +ε
z z
y
y
Fig. 5: The handle H2n
k
The handle is then deﬁned as H2n
k :={ψ <−1}∩{ φ> −1} (see Fig. 5).
17

Remark.
• If ψ(0) ⁄= −1, it follows from ( ψ1) that the level sets Σ + := {ψ = −1} and
Σ− ={φ =−1} are both contact hypersurfaces, as Y·ψ >0 away from 0. They
coincide fory≥ 1+ε due to (ψ2) and they contain the boundary ofH2n
k . Condition
(ψ3) on the other hand assures that Σ + is obtained from Σ− by surgery along S.
• Condition (ψ1) is automatically satisﬁed ifψ(p,q ) =ψ(x,y,z ) is given as a function
on x,y,z such that ∂xψ,∂zψ >0 and ∂yψ <0. The Hamiltonian vector ﬁeld Xψ
of ψ is then given by
Xψ =
(∂ψ
∂x·Xx + ∂ψ
∂y·Xy + ∂ψ
∂z ·Xz
)
.
• It follows from ( ψ2) that reducing ε makes the handle thinner. Note that one
can always choose ε so small, that the handle becomes so thin that its “lower”
boundary{φ =−1}∩ H2n
k lies inside any prescribed neighborhood of S.
• The handle stays unchanged if we take φ′ =α·φ +β and ψ′ =α·ψ +β, α >0,
provided that we set H2n
k ={ψ′ <−α +β}∩{ φ′ >−α +β}.
Discussion 7. Consider the Lyapunov functionf :=∑k
j=1qjpj. Note that (ψ1) implies
that Xψ·f >0 away from the critical points of f, which shows that all periodic orbits
of Xψ are contained in the set {x = y = 0}. The same holds true if we consider
ψ′ =α·ψ +β,α> 0, instead.
2.3 An explicit Hamiltonian on and near the handle
It is not diﬃcult to ﬁnd a Weinstein function ψ : R2n→ R which satisﬁes (ψ1)–(ψ3).
Fix ε> 0 and choose a smooth, monotone function g : R→ [0, 1] such that
g(t) =
{
0 for t≤ 0
1 for t≥ 1 +ε and 0 ≤g′(t)< 1
1 +ε/2.
Then set ψ :=x−y +z− (1 +ε/2) + (1 +ε/2)·g(y). (2)
In Section 1.3, we want to useψ as an admissible Hamiltonian which allows us to compare
the symplectic homologies of a Liouville domainW bounded by Σ− andW∪H2n
k bounded
by Σ+. We do this by extending an admissible Hamiltonian on W overH2n
k viaψ, where
we take great care not to create new 1-periodic orbits away from H2n
k . Hence, we need
that ψ is linear, i.e. of the form ψ =α·er +β, on regions which are identiﬁed with the
symplectizations of Σ±.
To be more precise, let Σ − ={φ =−1} and Σ + ={ψ =−1} be as above. As both
are hypersurfaces transversal to the Liouville vector ﬁeld Y , the ﬂow ϕ of Y provides
symplectic embeddings Φ± of the symplectizations of Σ± into R2n:
Φ± : Σ±× R→ R2n, Φ±(y,r ) =ϕr(y).
18

Σ−×R−
Σ+×R+
Σ−×R−
Σ+×R+ U
U
Fig. 6: The symplectizations of Σ± and areas where ψ is linear
On a symplectization (Σ× R,d (erλ)) of a contact manifold we deﬁne a function ˜hΣ by
˜hΣ(y,r ) :=α·er +β, α,β ∈ R.
We call such a function linear (in fact it is linear when using the coordinate z := er).
Observe that the Hamiltonian vector ﬁeld of ˜hΣ is given by X˜hΣ(s,t ) =α·Rλ(s), where
Rλ is the Reeb vector ﬁeld of λ, the contact form on Σ.
For Σ± we choose explicitly α = 1,β =−2, such that ˜h±
Σ(Σ±×{ 0}) =−1, and let
h±
Σ : Φ±(Σ±× R)→ R, h ±
Σ := ˜hΣ±◦ (Φ±)−1
be their pushforward onto Φ ±(Σ±× R) ⊂ R2n. Note that h+
Σ and h−
Σ coincide on
Φ±((Σ+∩Σ−)×R), as Φ− = Φ+ on (Σ−∩Σ+)×R. For the comparison of the symplectic
(co)homologies ofW andW∪H2n
k , we need a Hamiltonian that is linear on the negative
symplectization of Σ− and the positive symplectization of Σ +. As ψ will serve as such
a Hamiltonian, we require that ψ = h+
Σ on{ψ≥− 1} and ψ = h−
Σ on{φ≤− 1}\ U,
where U is a compact neighborhood of S ={x =z = 0, y= 1} (see Figure 6).
Discussion 8. It is the extension of ψ beyond the handle, that is not quite correct in
[3]: It is stated there that one can extend ψ on the positive symplectization of Σ + such
that the only 1-periodic orbit of Xψ on the handle is the constant orbit at the origin. It
is suggested that this can be done such that:
(A1) ψ =α·er +β, α⁄∈spec(Σ±) on Φ +(
Σ+× [0,∞)
)
and Φ−(
Σ−× (−∞, 0]
)
except
a small neighborhood of S,
(A2) ψ is increasing for y→ 0 on{x =z = 0},
(A3) ψ =α·er +β on{x =z = 0}⊂ Φ+(
Σ+× [0,∞)
)
.
19

Assumption (A2) is a consequence of (ψ1), while (A3) guarantees that Xψ has only the
origin as 1-periodic orbit (asα⁄∈spec(Σ±) and as all 1-periodic orbits lie in{x =y = 0}).
However, all 3 assumptions cannot be satisﬁed simultaneously. To see this consider a
path in R2n as depicted in Figure 7.
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/0
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/1
/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1/1
z z
y
y
γz
γy
Fig. 7: The problematic path
Here, path γz is an integral curve of Y in{x =y = 0}. As the origin is the only zero of
Y , it follows that limt→−∞γz(t) = 0. By (A3) and the continuity of ψ, we ﬁnd
ψ(0) = lim
t→−∞
α·er(γz(t)) +β =β.
With (A2), we ﬁnd then thatψ≤β on{x =z = 0} (on the pathγy). For x =z = 0 and
y≫ 1 however, we are on Φ−(
Σ−× (−∞, 0]
)
and require by (A1) that ψ =α·er +β,
which gives on this region the contradiction ψ =α·er +β >β≥ψ.
Our solution to this dilemma is to omit assumption (A3) and to allow ψ to have varying
slope α and constant β on{x = y = 0}, ﬁrst letting it grow very slowly coming from
the origin and increasing the slope sharply near Σ +.
This creates more than one 1-periodic Hamiltonian orbit on the handle. However, using
property (ψ1) and the Lyapunov function f as in Discussion 7, we can show that these
1-periodic Xψ-orbits stay all in the set {x = y = 0}. Moreover, they can be described
explicitly and are hence manageable.
For the construction of such a ψ, we need the following two technical lemma:
Lemma 9. Consider R2n with the standard symplectic structure, the Liouville vector
ﬁeld Y and the functions x,y,z as given in 2.2. Let Σ⊂ R2n be a smooth hypersurface
transverse to the Liouville vector ﬁeld Y (i.e. Σ is contact) such that its Reeb vector ﬁeld
R is of the form
R =cx·Xx +cy·Xy +cz·Xz,
wherecx,cy,cz : Σ→ R are smooth functions with cx,cz > 0,cy < 0 and Xx,Xy,Xz are
the Hamiltonian vector ﬁelds of x,y,z . Let ˜hΣ denote the function ˜hΣ(y,r ) =α·er +β
20

on the symplectization of Σ and let hΣ := ˜hΣ◦ Φ−1 be its pushforward onto R2n by
the symplectic embedding Φ : Σ × R→ R2n provided by the ﬂow ϕ of Y . Then, the
Hamiltonian vector ﬁeld Xh of hΣ is of the form
Xh =Cx·Xx +Cy·Xy +Cz·Xz,
whereCx,Cy,Cz∈C∞(R2n) are functions satisfying Cx,Cz > 0, Cy < 0.
Remark. The assumptions on Σ are satisﬁed, if Σ = ψ−1(c) for a function ψ on x,y,z
with ∂xψ
⏐⏐
Σ,∂zψ
⏐⏐
Σ > 0 and ∂yψ
⏐⏐
Σ < 0 and 0⁄∈ Σ.
Proof: AsX˜h =α·R on Σ× R, it follows that on R2n holdsXh|ϕt(Σ) =α·et·Rt, where
Rt is the Reeb vector ﬁeld onϕt(Σ). Recall the deﬁnitions of x,y,z andXx,Xy,Xz from
2.2. By assumption, the Reeb vector ﬁeld R on Σ satisﬁes
R =cxXx +cyXy +czXz =
k∑
j=1
(
cx 2qj
∂
∂pj
−cypj
∂
∂qj
)
+cz
n∑
j=k+1
(
qj
∂
∂pj
−pj
∂
∂qj
)
.
Moreover,Y is given by
Y =
k∑
j=1
(
2qj
∂
∂qj
−pj
∂
∂pj
)
+
n∑
j=k+1
1
2
(
qj
∂
∂qj
+pj
∂
∂pj
)
.
The ﬂow ϕt of Y is hence given by
ϕt(q,p ) =
(
...,e 2t·qj,e−t·pj,...| {z }
j=1,...,k
,...,e t/2·qj,et/2·pj,...| {z }
j=k+1,...,n
)
.
AsLYλ =λ andLYω =ω, we ﬁnd for R and any ξ∈Tϕt(p)ϕt(Σ) that
λϕt(p)
(
Dϕt
pR
)
=
(
ϕt∗
λ
)
p(R) = et·λp(R) = et,
ωϕt(p)
(
Dϕt
pR, ξ
)
=
(
ϕt∗
ω
)
p
(
R, (Dϕt
p)−1(ξ)
)
=et·ωp
(
R, (Dϕt
p)−1(ξ)
)
= 0,
as R is the Reeb vector ﬁeld and ( Dϕt
p)−1(ξ)∈T Σ. This shows that e−t·DϕtR is the
Reeb vector ﬁeld Rt of ϕt(Σ). Hence we ﬁnd for Xh that
Xh|ϕt(Σ) =α·et·Rt =α·Dϕt(R) =αe−tcxXx +αe2tcyXy +αet/2czXz,
which is exactly of the announced form.
Lemma 10. Let (Σ,α ) be a contact manifold with contact form α and symplectization(
Σ× R,d (erα)
)
. Let ε,δ,c > 0 be constants and let J be an almost complex structure 5
compatible with ω =d(erα) such that the norm ||R|| of the Reeb vector ﬁeld R satisﬁes
sup
y∈Σ
||R(y)|| = sup
y∈Σ
√
ω
(
R(y),JR (y)
)
=:d< ∞.
5For example, any cylindrical J would do, i.e. if d(er)◦J =−λ.
21

Then there exists a smooth monotone function g : R→ [0, 1] such that
g(er) = 0 for r≤−ε and g(er) = 1 for r≥ 0 ( ∗)
and for all φ,ψ ∈C1(Σ× R) with φ|Σ×{0} =ψ|Σ×{0} and|∂rφ(y,r )−∂rψ(y,r )|< cfor
all (y,r )∈ Σ× [−ε, 0], holds for their Hamiltonian vector ﬁelds Xφ,Xψ that
sup
(y,r)∈Σ×R
⏐⏐⏐
⏐⏐⏐Xφ+(ψ−φ)g(y,r )−
(
Xφ(y,r ) +
(
Xψ(y,r )−Xφ(y,r )
)
·g(er)
)⏐⏐⏐
⏐⏐⏐≤δ. (∗∗)
In other words, we can interpolate between φ and ψ along Σ× [−ε, 0], such that the
Hamiltonian vector ﬁeld Xφ+(ψ−φ)g of the interpolation is arbitrary close to the interpo-
lation of the Hamiltonian vector ﬁelds Xφ and Xψ.
Proof: As the Hamiltonian vector ﬁeld of er is the Reeb vector ﬁeld R, we calculate
Xφ+(ψ−φ)g(y,r ) =Xφ(y,r ) +
(
Xψ−Xφ
)
(y,r )·g(er) + (ψ−φ)(y,r )·g′(er)·R(y).
Therefore, (∗∗) translates to
||(ψ−φ)(y,r )·g′(er)·R(y)||≤ δ ∀(y,r )∈ Σ× [−ε, 0].
Using φ|Σ×{0} =ψ|Σ×{0}, we can estimate the left hand side as follows:
||(ψ−φ)(y,r )·g′(er)·R(y)|| =
⏐⏐⏐⏐
⏐⏐⏐⏐−
∫ 0
r
∂s(ψ−φ)(y,s )ds·g′(er)·R(y)
⏐⏐⏐⏐
⏐⏐⏐⏐
≤c· (−r)·g′(er)·d.
If we write z = er, we ﬁnd that (∗∗) is satisﬁed, if 0 ≤ g′(z)≤ −δ
cd logz∀z∈ [e−ε, 1]. As∫ 1
e−ε
−δ
cd logzdz =∞, we can choose a smooth function ˜g satisfying
0≤ ˜g(z)≤ −δ
cd· logz, ˜g≡ 0 for z≤e−ε or z≥ 1 and
∫ 1
e−ε
˜g(z)dz = 1.
Setting g(er) =g(z) :=
∫z
e−ε ˜g(s)ds then gives the desired function.
Now, we constructψ in two steps, ﬁrst deﬁning ψ on Φ−(
Σ−× (−∞, 0]
)
∪H2n
k and then
extending it to Φ +(
Σ+× [0,∞)
)
.
• Step 1: Recall that the isotropic sphere S⊂ Σ− ={φ =−1} is given by
S :={x =z = 0, y= 1}.
Consider the function h−
Σ as deﬁned on page 19. As the Reeb vector ﬁeld RΣ− of
(Σ−,λ|T Σ−) coincides with the Hamiltonian vector ﬁeld Xφ on S, we ﬁnd Xh−
Σ
=
RΣ− =Xφ and hencedh−
Σ =dφ onS. As also h−
Σ(Σ−) =φ(Σ−) =−1, we ﬁnd that
h−
Σ andφ coincide up to ﬁrst order on S. Therefore, given any neighborhood U of
22

S, there exists a function ˆφ ofx,y,z and a neighborhood ˆU⊂U, such that ˆφ≡h−
Σ
on R2n\U, ˆφ≡φ on ˆU and ˆφ is arbitrarilyC1-close toh−
Σ. As Xφ =Xx−Xy +Xz
and Xh−
Σ
= C−
x ·Xx +C−
y ·Xy +Cz·Xz with C−
x,C−
z > 0,C−
y < 0 by Lemma 9,
we can additionally arrange that
Xˆφ = ˆCx·Xx + ˆCy·Xy + ˆCz·Xz with ˆCx, ˆCz > 0, ˆCy < 0.
Let H2n
k be deﬁned by a function ˜ψ as in (2) and so thin, such that the lower
boundary H2n
k ∩ Σ− lies in ˆU. Then set
ˆψ :{φ≤− 1}∪ H2n
k → R ˆψ =



˜ψ on
( ˆU∩{φ≤− 1}
)
∪H2n
k
ˆφ on
(
U∩{φ≤− 1}
)
\ ˆU
h−
Σ on{φ≤− 1}\ U
.
Since ˜ψ = ˆφ outside a small neighborhood of H2n
k and ˆφ =h−
Σ outside U, we ﬁnd
that ˆψ is smooth on its domain. Moreover, as ˜ψ, ˆφ andh−
Σ satisfy (ψ1), so does ˆψ.
See Figure 8 for the areas where ˆψ is deﬁned.
S
S
H2nkˆU∩{φ≤−1} U∩{φ≤−1}
Fig. 8: Areas, where ˆψ is deﬁned
• Step 2 Consider the function h+
Σ associated to Σ + ={ ˆψ =−1} as deﬁned on page
19. We will now deﬁne ψ as an interpolation between ˆψ and h+
Σ, i.e.
ψ := ˆψ + (h+
Σ− ˆψ)·g(h+
Σ), (3)
where g is a function given by Lemma 10 such that for ε> 0 small holds
23

g(er− 2) = 0 for r≤−ε and g(er− 2) = 1 for r≥ 0, (∗)
and such that ψ satisﬁes (ψ1), i.e. Xψ = Cx·Xx +Cy·Xy +Cz·Xz, where
Cx,Cz,Cy∈C∞(R2n) and Cx,Cz > 0, Cy < 0.
For the following deﬁnitions of the areasA,B,B ± andB′ see Figure 9. Recall that
Σ+ = Σ− outsideU, so thath+
Σ =h−
Σ = ˆψ onA := Φ
(
(Σ−\U)×R
)
. Consequently,
we have by (3) thatψ =h+
Σ onA for anyg, so that (ψ1) holds there by Lemma 9.
Now consider B := Φ
(
Σ+∩ (H2n
k ∪U)× R
)
with the following subsets
B± := Φ
(
Σ+∩ (H2n
k ∪U)× R±)
,
B′ := Φ
(
Σ+∩ (H2n
k ∪U)× [−ε, 0]
)
⊂B−.
B−
U
U
A
A
A
A
B′ B′ B+B+
Fig. 9: Interpolation areas
Note that B′ is compact so that the following quantities are ﬁnite:
c := sup
p∈B′
⏐⏐Y· ˆψ(p)−Y·h+
Σ(p)
⏐⏐<∞, d := sup
p∈Σ+∩B′
⏐⏐⏐⏐R(p)
⏐⏐⏐⏐<∞.
Here, R is the Reeb vector ﬁeld on Σ + and Y the Liouville vector ﬁeld which is
also the vector ﬁeld corresponding to the partial derivative ∂r in the cylindrical
coordinates (y,r ) on the symplectization Σ +× R. As h+
Σ = er− 2 in these coor-
dinates we ﬁnd by Lemma 10 for δ >0 arbitrary a function g satisfying (∗) such
that with ψ given by (3), we have
sup
p∈B′
⏐⏐⏐
⏐⏐⏐Xψ(p)−
(
X ˆψ(p) +
(
Xh+
Σ
(p)−X ˆψ(p)
)
·g(h+
Σ(p))
)⏐⏐⏐
⏐⏐⏐≤δ,. (∗∗)
Note that Xg(h+
Σ) =g′(h+
Σ)·Xh+
Σ
and that by Step 1 and Lemma 9 holds
X ˆψ = ˆCx·Xx + ˆCy·Xy + ˆCz·Xz
Xh+
Σ
=C+
x·Xx +C+
y ·Xy +C+
z ·Xz,
where all coeﬃcient functions satisfy (ψ1).
24

As Xψ = X ˆψ on B−\B′ and Xψ = Xh+
Σ
on B+, we ﬁnd with ( ∗∗) for δ small
enough that ψ satisﬁes (ψ1) also on B and hence everywhere.
2.4 Closed orbits and Conley-Zehnder indices
Set ψ′ :=α·ψ +β. In the following we will determine all 1-periodic orbits of Xψ′ near
the handle H2n
k and calculate their Conley-Zehnder indices. Since ψ satisﬁes (ψ1) and
consequently also ψ′, Discussion 7 guarantees that the only periodic orbits of Xψ′ near
the handle lie in{x =y = 0}. By (ψ1), the Hamiltonian vector ﬁeld Xψ is given by
Xψ =α·
(
CxXx +CyXy +CzXz
)
,
where Cx,Cy,Cz∈C∞(R2n) are functions with Cx,Cz > 0, Cy < 0 and Xx,Xy and Xz
are the Hamiltonian vector ﬁelds of the functions x,y,z and given by
Xx =
k∑
j=1
2qj
∂
∂pj
, X y =
k∑
j=1
−pj
∂
∂qj
, X z =
n∑
j=k+1
Aj
(
qj
∂
∂pj
−pj
∂
∂qj
)
.
On
(
Σ+× [0,∞)
)
∩{x =y = 0}, we have by our construction ψ =h+
Σ and hence that
Xψ equals R, the Reeb vector ﬁeld of Σ +. To calculate R on Σ +∩{x = y = 0} note
that λ(Xz) = z and ω(Xz,·) =−dz =−d ˜ψ on Σ +∩{x = y = 0}. The value of z on
Σ+∩{x =y = 0} = ˜ψ−1(−1)∩{x =y = 0} is given by (2) as
−1 = 0− 0 +z− (1 +ε/2) ⇔ z =ε/2.
Hence we ﬁnd that R on Σ+∩{x =y = 0} is given by
R = 2
εXz = 2
ε·
n∑
j=k+1
Aj
(
qj
∂
∂pj
−pj
∂
∂qj
)
.
Still for x = y = 0 and z slightly smaller then ε/2 on the other hand, we have by the
construction of ψ that ψ = ˆψ = ˜ψ. Hence (2) gives ψ = ˆψ = ˜ψ = z− (1 +ε/2) and
thus Xψ = Xz on{x = y = 0,z < ε/2}. As ψ is a convex interpolation between ˆψ
and h+
Σ it follows that on {x =y = 0} we haveXψ =CzXz, where Cz is a z-dependent
interpolation between the constants 1 and 2 /ε. It follows that Xψ′ on{x = y = 0} is
given by
Xψ′ =αCz·Xz =αCz
n∑
j=k+1
Aj
(
qj
∂
∂pj
−pj
∂
∂qj
)
.
Now we can calculate the ﬂowϕt ofXψ′ on{x =y = 0}. First we calculate forz(ϕt(p,q ))
d
dtz
(
ϕt)
=dz(Xψ′) =α·Czdz(Xz) = 0.
25

It follows that z is constant along the ﬂow lines of ϕ. Now, consider for j =k + 1,...,n
the complex coordinates zj =qj +ipj. Then, we have on {x =y = 0}:
Xψ′ =αCz·
(
0,..., 0| {z }
j=1,...,k
,...,iA j·zj,...| {z }
j=k+1,...,n
)
.
As z(ϕt) is independent from t and hence d
dtCz(z(ϕt)) = 0, we obtain that the ﬂow ϕt
of Xψ′ on{x =y = 0} is given by
ϕt(0,zk+1,...,z n) =
(
0,..., 0, exp
(
iαCzAk+1t
)
·zk+1,..., exp
(
iαCzAnt
)
·zn
)
. (4)
By choosing the constants Aj linear independent over Q, we can arrange that the 1-
periodic orbits of Xψ′ on{x =y = 0} are isolated. They are all of the form
γ(t) =
(
0,..., 0,eiαCzAj0·zj0, 0,..., 0
)
, (5)
where αCz(
Aj0|zj0|2
2 )∈ 2πZ. The only exception is the one constant orbit at the origin.
Forα appropriately chosen, we can assume that there are only ﬁnitely many such orbits.
Now, we want to calculate the Conley-Zehnder indices µCZ of these orbits. Recall that
µCZ is a Maslov type index for paths Φ in the group of symplectic matrices Sp(2n). By
[13] the index is calculated as follows. Every smooth path Φ : [ a,b ]→ Sp(2n) can be
uniquely expressed as a solution of an ODE of the form
d
dtΦ(t) =J0S(t)Φ(t), Φ(a)∈Sp(2n),
where t↦→S(t) =S(t)T is a smooth path of symmetric matrices
A time t is called a crossing if det(Φ( t)− 1 ) = 0. The index µCZ is now the sum over
all crossings t of the signatures of S(t) restricted to ker(Φ(t)− 1 ). Note that if the end
pointsa andb are crossings, then only half the signature is added (see [13] for details). It
follows easily from this deﬁnition thatµCZ (Φ) = 0 ifsign(S) = 0 everywhere. Moreover,
the Conley-Zehnder index of the path Φ : [0 ,T ]→Sp(2n), Φ(t) =eit is given by
µCZ (Φ) =
⌊T
2π
⌋
+
⌈T
2π
⌉
.
Another important property of µCZ that we shall need is the additivity under products:
If Sp(2n)⊕Sp(2n′) is understood as the obvious subgroup of Sp
(
2(n +n′)
)
, then
µCZ (Φ⊕ Φ′) =µCZ (Φ) +µCZ (Φ′).
To calculateµCZ in our situation, let γ be a 1-periodic orbit of Xψ′ as in (5). In order to
calculate µCZ (γ), we identify Tγ(t)R2n with R2n in the natural way. This yields a path
26

Φψ in Sp(2n) given by Φψ(t) =Dϕt(z0). We diﬀerentiate Φψ on{x =y = 0} as
d
dtΦψ(t) = d
dtDϕt(z0) =D
(d
dtϕt(z0)
)
=DXψ′
(
ϕt(z0)
)
=D
(
CxXx +CyXy +CzXz
)(
ϕt(z0)
)
=α·diag
((
0 −Cy
2Cx 0
)
| {z }
j=1,...,k
,Aj
(
0 −Cz
Cz 0
)
| {z }
j>k,j⁄=j0
, Aj0
( −C′
zqj0pj0 −C′
zq2
j0−Cz
C′
zqj0pj0 +Cz C′
zp2
j0
))
◦ Φψ(t).
Here, we write C′
z := ∂zCz. Note that no derivatives of Cx,Cy,Cz are involved except
for j = j0, as qj = pj = 0 for j ⁄= j0 along γ. It follows that Φ ψ is of block form
Φψ =diag
(
Φ1
ψ,..., Φn
ψ
)
, where the paths of 2×2 matrices Φj
ψ are solutions of an ordinary
diﬀerential equation with initial value Φj
ψ(0) = 1 and
d
dtΦj
ψ(t) = α
( 0 −Cy
2Cx 0
)
Φj
ψ(t) =
(0 −1
1 0
)
α
(2Cx 0
0 Cy
)
Φj
ψ(t) j = 1,...,k
d
dtΦj
ψ(t) =αAj
( 0 −Cz
Cz 0
)
Φj
ψ(t) =
(0 −1
1 0
)
αAj
(Cz 0
0 Cz
)
Φj
ψ(t) j >k,j ⁄=j0
d
dtΦj0
ψ (t) =
(0 −1
1 0
)
αAj0
(C′
zq2
j0 +Cz C′
zqj0pj0
C′
zqj0pj0 C′
zp2
j0 +Cz
)
Φj0
ψ (t) j =j0.
As the matrix
( 2αCx 0
0 αCy
)
has for allt one positive and one negative eigenvalue, it follows
that its signature is always zero and hence by the Robbin-Salamon deﬁnition ofµCZ that
µCZ (Φj
ψ) = 0, j = 1,...,k . For j >k, j⁄=j0 on the other hand, we ﬁnd by the explicit
formula from above that
µCZ
(
Φj
ψ
)
=
⌊αAjCz
2π
⌋
+
⌈αAjCz
2π
⌉
, j >k, j ⁄=j0.
Forj0 ﬁnally, it is not diﬃcult to calculate, that the eigenvalues of the matrix are Cz
andCz +C′
z(q2
j0 +p2
j0). So depending on C′
z it has either signature 2 or 0. Hence we ﬁnd
that µCZ (Φj0
ψ )≥ 0 and therefore
µCZ (γ) =µCZ (Φψ)≥
∑
j>k,j⁄=j0
(⌊αAjCz
2π
⌋
+
⌈αAjCz
2π
⌉)
≥ α
2π·
∑
j>k,j⁄=j0
Aj, (6)
as 1≤ Cz≤ 2/ε. If α tends to +∞, we have therefore for all 1-periodic Hamiltonian
orbits γ near the handle that µCZ (γ) becomes arbitrarily large.
2.5 Proof of the Main Theorem
Recall that we have in 1.6 constructed the transfer maps
π∗(W,V ) :SH∗(V )→SH∗(W ) and π∗(W,V ) :SH∗(W )→SH∗(V ),
27

for an exactly embedded subdomain W⊂V . This was done in Corollary 5 by showing
the isomorphisms SH∗(W )∼= SH>0
∗ (W⊂V ) and SH∗(W )∼= SH∗
>0(W⊂V ) and then
applying the truncation maps SH(V )→SH>0
∗ (W⊂V ) and SH∗
>0(W⊂V )→SH∗(V ).
The main theorem, that we are going to prove now, states that the maps π∗(W,V ) and
π∗(W,V ) are isomorphisms if V is obtained from W by attaching a subcritical handle.
Proof of Theorem 1 .
The idea of the proof is to construct yet another coﬁnal sequence of Hamiltonians
(Hn)⊂Adw(V )∩Ad(W⊂V ) for which we can directly show that
SH∗(W )
(∗)
∼= SH>0
∗ (W⊂V )
(∗∗)
= lim
n→∞
FH>0
∗ (Hn)
(1)
≃ lim
n→∞
FH∗(Hn)
(∗∗)
= SH∗(V )
SH∗(W )
(∗)
∼= SH∗
>0(W⊂V )
(∗∗)
= lim
n→∞
FH∗
>0(Hn)
(2)
≃ lim
n→∞
FH∗(Hn)
(∗∗)
= SH∗(V ).
Note that the identities (∗∗) are given by the construction of SH∗ and SH∗, while the
isomorphisms (∗) have been shown in Corollary 5.
To start the contruction ﬁx sequences k(n)⁄∈ Spec(∂W,λ ), k(n)→∞ and ε(n)→ 0.
Then choose an increasing sequence of non-degenerate Hamiltonians Hn on W that is
on ∂W× (−ε(n), 0] of the form
Hn|∂W×(−ε(n),0] =k(n)·er−
(
1 +ε(n)
)
and extend Hn over the handle by a function ψ with α = k(n) and β =−1−ε(n) as
described in Section 2. For each n choose the handle so thin 6 such that each trajectory
ofXHn which leaves and reenters the handle has length greater than 1. Thus we obtain a
coﬁnal weakly admissible sequence (Hn), whose 1-periodic orbits having positive action
are all contained in W . Recall that we have the long exact sequences
···→ FH>0
j+1(Hn)→FH≤0
j (Hn)→FHj(Hn)→FH>0
j (Hn)→...
···→ FHj−1
≤0 (Hn)→FHj
>0(Hn)→FHj(Hn)→FHj
≤0(Hn)→...
and note that FH>0
j (Hn) is generated by all 1-periodic orbits of Hn inside W , while
FH≤0
j (Hn) is generated by all other orbits. The orbits of negative action all lie on
the handle and are explicitly given in (4). Observe that Hn is on the handle time-
independent. The orbits there are therefore of Morse-Bott type. We can now use either
the deﬁnition ofSH with Morse-Bott techniques, as described in [2], or perturb Hn near
these orbits to make it non-degenerate, as described in [4]. In both cases we obtain
for each orbit γ two generators in the chain complex whose indices are µCZ (γ) and
µCZ (γ) + 1. We have shown in Section 2.4 that the possible values of µCZ (γ) increase
to∞ as the slope α =k(n) tends to∞. Therefore, FH≤0
j (Hn) becomes eventually zero
for n large enough, as well as FH≤0
j+1(Hn). This implies for n large enough that
FHj(Hn)→FH>0
j (Hn)
6Note that diﬀerent choices of ψ give diﬀerent handles H 2n
k , however the completions ˆW #H 2n
k of the
resulting symplectic manifolds are symplectomorphic.
28

is an isomorphism. As the direct limit is an exact functor, these maps converge to an
isomorphism in the limit, proving (2). In the cohomology case, the line of arguments is
the same. Even though taking inverse limits is not exact, it still takes the isomorphism
FHj
>0(Hn)→FHj(Hn)
to an isomorphism in the limit, as it is left exact (see [8], Thm. 5.4 or [1], §6, no.3, prop.
4). This proves (5).
2.6 The invariance of Rabinowitz-Floer homology
Given a Liouville domain V , Rabinowitz-Floer homology RFH∗(V,∂V ) was deﬁned in
[5] as a Floer-type homology associated to the Rabinowitz action functional
AH
Rab(x,η ) :=AηH(x),
a Lagrange multiplier version of the Hamiltonian action functionalAH. Here, x :S1→V
is a loop, η∈ R and H : ˆV → R is a Hamiltonian such that ∂V = H1−(0) is a regular
hypersurface and XH|∂V = R. In [6], it was shown that RFH (V,∂V ) is isomorphic
to the symplectic homology ˇSH(V ) of V -shaped Hamiltonians. In [7], it is denoted as
SH(∂V ) and is deﬁned as follows:
Consider (weakly) admissible Hamiltonians H ∈ Adw(V ) as in 1.2 and require that
H|∂V < 0 (see ﬁgure 10). For homotopies Hs require that they are globally monotone
decreasing, so that for lim s→±∞Hs = H± the resulting continuation map σ∗(H−,H +)
respects action truncation as in 1.4. Then deﬁne
ˇSH∗(∂V ) := lim
−→
b→∞
lim
←−
a→−∞
lim
−→
H∈Ad(V ),
H|∂V <0
FH (a,b)(H).
One big diﬀerence in the deﬁnitions of SH(∂V ) andSH(V ) is that all 1-periodic orbits
r
FH(r)
∂V
Fig. 10: A V -shaped Hamiltonian
in the region F are discarded due to the restriction to a ﬁxed action window.
In [7], Cieliebak and Oancea introduce even more versions of SH, namely symplectic
homology of symplectic cobordisms. Given a Liouville domain V and a subdomain
W⊂V , we say that C :=V\W is an exact Liouville cobordism between ∂W and ∂V
with ﬁlling W . In order to deﬁne SH∗(C) we consider the subset Adw(C)⊂ Adw(V )
29

given by the condition H ∈ Adw(C)⇔ H|C < 0. Again, we consider only globally
monotone decreasing homotopies such that action windows are respected. Then we
deﬁne
SH∗(C) := lim
−→
b→∞
lim
←−
a→−∞
lim
−→
H∈Ad(C)
FH (a,b)(H).
There are yet two more ﬂavors of SH. Up to now, we have had H tend to +∞ on
certain subsets of V . However, we can let H also tend to−∞, but then we have to use
inverse limits, as we have continuation maps σ∗(H−,H +) : FH (H+)→ FH (H−) only
if H− > H+ due to the maximum principle. Let C− :=∂W and C+ :=∂V denote the
“lower” respectively “upper” boundary of C. Following [7], we deﬁne for H∈Adw(C):
SH∗(C,C−) := lim
−→
b→∞
lim
←−
a→−∞
lim
−→
H→∞,
on ˆV\V
lim
←−
H→−∞,
on W
FH (a,b)(H),
SH∗(C,C +) := lim
−→
b→∞
lim
←−
a→−∞
lim
−→
H→∞,
on W
lim
←−
H→−∞,
on ˆV\V
FH (a,b)(H).
H(r)
∂W ∂V
r
SH∗(C) SH∗(C,C+)SH∗(C,C−)
∂W ∂V ∂W ∂V
Fig. 11: Shapes of H for diﬀerent versions of SH
In [7],SH(C,C′) is also deﬁned for a pair of ﬁlled Liouville cobordismsC′⊂C, a version
which we shall not need. We only remark that for the Liouville domains W⊂ V and
C =V\W it holds that SH(V,W ) =SH(C,C−) directly by deﬁnition.
Theorem 11 (Invariance ofRFH under subcritical surgery) .
LetW and V be as in Theorem 1. Then it also holds that
RFH∗(V,∂V )∼=RFH∗(W,∂W ).
Proof: Set C =H2n
k =V\W and C− =∂W, C+ =∂V as above. Our proof follows
closely the one given in [7], prop. 9.14. However, our arguments diﬀer slightly as the
essential vanishing of SH∗(C,C−) is shown diﬀerently. The key tool for the demonstra-
tion is the long exact sequence in symplectic homology associated to a pair of Liouville
cobordisms (see [7], prop 7.3). First applied to W⊂V , this sequence reads as
SH∗(V )
π
→SH∗(W )→SH∗−1(V,W )→SH∗−1(V )
π
→SH∗−1(W ),
30

whereπ is the transfer map. As we have shown in the proof of Theorem 1,π is an isomor-
phism if V is obtained from W by attaching a subcritical handle. It follows hence that
SH∗(V,W ) = 0 for all∗∈ Z. As mentioned above SH∗(V,W ) =SH∗(C,C−). A duality
argument over the ﬁeld Z2 (see [7], prop. 3.4, 3.5) then shows that SH−∗(C,C +) = 0 as
well. Secondly, the long exact sequences for the pairs ∂W =C−⊂C and∂V =C+⊂C
give
SH∗(C,C−)→SH∗(C)→SH∗(∂W )→SH∗−1(C,C−),
SH∗(C,C +)→SH∗(C)→SH∗(∂V )→SH∗−1(C,C +).
As in both sequences the most left and right groups vanish, we get isomorphisms
RFH (W,∂W )∼=SH∗(∂W )∼=SH∗(C)∼=SH∗(∂V )∼=RFH∗(V,∂V ).
3 References
[1] N. Bourbaki. ´El´ ements de Math´ ematiques, Livre 2, Alg` ebre, Alg` ebre lin´ eaire. Dif-
fusion CCLS, Paris, 1962.
[2] F. Bourgeois and A. Oancea. Symplectic homology, autonomous Hamiltonians and
Morse-Bott moduli spaces. Duke Math. J. , (146):71–174, 2009.
[3] K. Cieliebak. Handle attaching in symplectic homology and the chord conjecture.
J. Eur. Math. Soc. (JEMS) 4 , pages 115–142, 2002.
[4] K. Cieliebak, A. Floer, H. Hofer, and K. Wysocki. Applications of symplectic
homology ii: Stability of the action spectrum. Math. Z., (223):27–45, 1996.
[5] K. Cieliebak and U. Frauenfelder. A Floer homology for exact contact embeddings.
Paciﬁc J. Math. 239 , pages 251–316, 2009.
[6] K. Cieliebak, U. Frauenfelder, and A. Oancea. Rabinowitz-Floer homology and
symplectic homology. Annales scientiﬁques de l’ENS 43, fascicule 6 , pages 957–
1015, 2010.
[7] K. Cieliebak and A. Oancea. Symplectic homology and the Eilenberg-Steenrod
axioms. 2015. arXiv:1511.00485v1.
[8] S. Eilenberg and N. Steenrod. Foundations of algebraic topology . Princeton Univ.
Press, Princeton, N.J., 1952.
[9] A. Fauck. Rabinowitz-Floer homology on Brieskorn manifolds . PhD thesis,
Humboldt-Universit¨ at zu Berlin, 2016. urn:nbn:de:kobv:11-100238399.
[10] M. McLean. Symplectic topology of Stein manifolds . PhD thesis, University of
Cambridge, 2008.
31

[11] A. Oancea. A survey of Floer homology for manifolds with contact type boundary
or symplectic homology. Ensaios Mat., (7), 2004.
[12] A. Oancea. The Kunneth formula in Floer homology for manifolds with restricted
contact type boundary. Math. Ann., (334), 2006.
[13] J. W. Robbin and D.A. Salamon. The Maslov index for paths. Topology 32, pages
827–844, 1993.
[14] P. Seidel. A biased view of symplectic cohomology. Current Developments in Math-
ematics, 2006:211–253, 2008.
[15] J.-C. Sikorav. Some properties of holomorphic curves in almost complex mani-
folds. In M. Audin and J. Lafontaine, editors, Holomorphic curves in Symplectic
Geometry. Eds. Birkh¨ auser, 1994.
[16] C. Viterbo. Functors and computations in Floer homology with applications, i.
GAFA Geom. funct. anal. 9 , pages 985–1033W, 1999.
[17] A. Weinstein. Contact surgery and symplectic handlebodies. Hokkaido Math. J.
20, pages 241–251, 1991.
32

